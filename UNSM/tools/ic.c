#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "lib/token.h"
#include "lib/token.c"

#define ERR_INTERNAL    "internal error"
#define ERR_SYNTAX      "syntax error"
#define ERR_TOK         "invalid token"
#define ERR_STR         "unterminated string"
#define ERR_INT         "invalid integer"
#define ERR_NOTE        "invalid note"
#define ERR_COMMAND     "invalid command"
#define ERR_NOWAVE      "missing wave"
#define ERR_READ        "read error"
#define ERR_NOTAIFC     "not an AIFC file"
#define ERR_ILLFMT      "illegal format"

static char *fn;
static unsigned int ln;
static char *root;
static const char *output;

static void error(const char *err)
{
	if (fn)
	{
		if (ln) fprintf(stderr, "%s:%u: %s\n", fn, ln, err);
		else    fprintf(stderr, "%s: %s\n", fn, err);
	}
	else fprintf(stderr, "%s\n", err);
	exit(1);
}

static void unexpected(char *tok, int t)
{
	if (tok)    fprintf(stderr, "%s:%u: unexpected token '%s'\n", fn, ln, tok);
	else        fprintf(stderr, "%s:%u: unexpected token '%c'\n", fn, ln, t);
	exit(1);
}

static void undefined(const char *name)
{
	fprintf(stderr, "%s:%u: '%s' undefined\n", fn, ln, name);
	exit(1);
}

static void redefined(const char *name)
{
	fprintf(stderr, "%s:%u: '%s' redefined\n", fn, ln, name);
	exit(1);
}

static void redefidx(const char *name, int i)
{
	fprintf(stderr, "%s:%u: %s %d redefined\n", fn, ln, name, i);
	exit(1);
}

/******************************************************************************/

typedef struct item
{
	struct item *prev, *next;
	const char *name;
}
ITEM;

typedef struct list
{
	ITEM *root, *item;
}
LIST;

static void ListAppend(LIST *list, const char *name, void *data)
{
	ITEM *item = data;
	item->prev = list->item;
	item->next = NULL;
	item->name = name;
	if (!list->root) list->root = item;
	if (list->item) list->item->next = item;
	list->item = item;
}

static void *ListFind(LIST *list, const char *name)
{
	ITEM *item;
	for (item = list->item; item; item = item->prev)
	{
		if (!strcmp(item->name, name)) return item;
	}
	return NULL;
}

typedef struct book
{
	short *data;
	unsigned int size;
	short order, npredictors;
}
BOOK;

typedef struct loop
{
	short *data;
	unsigned int size;
	unsigned int start, end, count;
}
LOOP;

typedef struct sound
{
	struct sound *prev, *next;
	const char *name;
	unsigned int addr;
	short *data;
	unsigned int size;
	float rate;
	BOOK book;
	LOOP loop;
}
SOUND;

typedef struct wave
{
	struct wave *prev, *next;
	const char *name;
	char *path;
	LIST sound;
	int ref;
}
WAVE;

typedef struct envelope
{
	struct envelope *prev, *next;
	const char *name;
	unsigned int addr;
	short *data;
	int alloc, len;
}
ENVELOPE;

typedef struct bsnd
{
	struct bsnd *prev, *next;
	const char *name;
	unsigned int addr;
	SOUND *sound;
}
BSND;

typedef struct inst
{
	struct inst *prev, *next;
	const char *name;
	unsigned int addr;
	ENVELOPE *env;
	BSND *bsnd[3];
	float freq[3];
	unsigned char rel, pan, min, max;
}
INST;

typedef struct bank
{
	struct bank *prev, *next;
	const char *name;
	char *path;
	WAVE *wave;
	LIST bsnd, env, inst, perc;
	INST **itab, **ptab;
	int ialloc, palloc, ninst, nperc;
	unsigned int date;
}
BANK;

static LIST wavelist;
static LIST banklist;
static WAVE *wavep;
static BANK *bankp;
static INST *instp;

static const float Na_FreqTable[] =
{
 0.105112, 0.111362, 0.117984, 0.125000, 0.132433, 0.140308, 0.148651, 0.157490,
 0.166855, 0.176777, 0.187288, 0.198425, 0.210224, 0.222725, 0.235969, 0.250000,
 0.264866, 0.280616, 0.297302, 0.314980, 0.333710, 0.353553, 0.374577, 0.396850,
 0.420448, 0.445449, 0.471937, 0.500000, 0.529732, 0.561231, 0.594604, 0.629961,
 0.667420, 0.707107, 0.749154, 0.793701, 0.840897, 0.890899, 0.943875, 1.000000,
 1.059463, 1.122462, 1.189207, 1.259921, 1.334840, 1.414214, 1.498307, 1.587401,
 1.681793, 1.781798, 1.887749, 2.000000, 2.118926, 2.244924, 2.378414, 2.519842,
 2.669680, 2.828428, 2.996615, 3.174803, 3.363586, 3.563596, 3.775498, 4.000000,
 4.237853, 4.489849, 4.756829, 5.039685, 5.339360, 5.656855, 5.993229, 6.349606,
 6.727173, 7.127192, 7.550996, 8.000000, 8.475705, 8.979697, 9.513658,10.079370,
10.678720,11.313710,11.986459,12.699211,13.454346,14.254383,15.101993,16.000000,
16.951410,17.959394,19.027315,20.158740,21.357440,22.627420,23.972918,25.398422,
26.908691,28.508766,30.203985,32.000000,33.902820,35.918790,38.054630,40.317480,
42.714880,45.254840,47.945835,50.796844,53.817383,57.017532,60.407970,64.000000,
67.805640,71.837580,76.109260,80.634960,85.429760,45.254840,47.945835,50.796844,
53.817383,57.017532,60.407970,64.000000,67.805640,71.837580,76.109260,80.634960,
};

static double SoundRate(short x, long long y)
{
	union {long long ll; double d;} pkt;
	pkt.ll = (long long)(0x3FF+(x-0x3FFF)) << 52 | (y >> 11 & 0xFFFFFFFFFFFFF);
	return pkt.d;
}

#define SHORT(i) ((short)(buf[i] << 8 | buf[i+1]))
#define UINT(i) (buf[i] << 24 | buf[i+1] << 16 | buf[i+2] << 8 | buf[i+3])
#define LONGLONG(i) ((long long)UINT(i) << 32 | UINT(i+4))

#define SoundLoadBlk(b, fp) \
	(fread((b)->data = malloc((b)->size), 1, (b)->size, fp) != (b)->size)

static const char *SoundLoad(SOUND *sound, FILE *fp)
{
	unsigned char buf[64];
	if (fread(buf, 1, 12, fp) != 12) return ERR_READ;
	if (memcmp(&buf[0], "FORM", 4)) return ERR_NOTAIFC;
	if (memcmp(&buf[8], "AIFC", 4)) return ERR_NOTAIFC;
	while (fread(buf, 1, 8, fp) == 8)
	{
		unsigned int size = UINT(4);
		long off = ftell(fp) + size;
		if (!memcmp(buf, "COMM", 4))
		{
			if (fread(buf, 1, 34, fp) != 34) return ERR_READ;
			if (SHORT(0) != 1 || SHORT(6) != 16) return ERR_ILLFMT;
			if (memcmp(&buf[18], "VAPC\13VADPCM ~4-1", 16)) return ERR_ILLFMT;
			sound->rate = (float)SoundRate(SHORT(8), LONGLONG(10)) / 32000;
		}
		else if (!memcmp(buf, "APPL", 4))
		{
			if (fread(buf, 1, 16, fp) != 16) return ERR_READ;
			if (!memcmp(buf, "stoc\13VADPCM", 11))
			{
				if (!memcmp(&buf[11], "CODES", 5))
				{
					if (fread(buf, 1, 6, fp) != 6) return ERR_READ;
					if (SHORT(0) != 1) return ERR_ILLFMT;
					sound->book.order = SHORT(2);
					sound->book.npredictors = SHORT(4);
					sound->book.size = 16 << sound->book.npredictors;
					if (SoundLoadBlk(&sound->book, fp)) return ERR_READ;
				}
				else if (!memcmp(&buf[11], "LOOPS", 5))
				{
					if (fread(buf, 1, 16, fp) != 16) return ERR_READ;
					if (SHORT(0) != 1 || SHORT(2) != 1) return ERR_ILLFMT;
					sound->loop.start = UINT(4);
					sound->loop.end = UINT(8);
					sound->loop.count = UINT(12);
					sound->loop.size = 32;
					if (SoundLoadBlk(&sound->loop, fp)) return ERR_READ;
				}
			}
		}
		else if (!memcmp(buf, "SSND", 4))
		{
			if (fread(buf, 1, 8, fp) != 8) return ERR_READ;
			if (UINT(0) != 0 || UINT(4) != 0) return ERR_ILLFMT;
			sound->size = size - 8;
			if (SoundLoadBlk(sound, fp)) return ERR_READ;
		}
		fseek(fp, off, SEEK_SET);
	}
	return NULL;
}

static int strtoint(const char *str, int base)
{
	long x;
	char *endptr;
	if (*str == '\0') error(ERR_INT);
	x = strtol(str, &endptr, base);
	if (*endptr != '\0') error(ERR_INT);
	if (x != (int)x) error(ERR_INT);
	return x;
}

static int strtonote(const char *str)
{
	static const signed char notetab[] = {0, 2, -9, -7, -5, -4, -2};
	int note, octave;
	if (*str < 'A' || *str > 'G') error(ERR_NOTE);
	note = notetab[*str++ - 'A'];
	switch (*str)
	{
	case 'b': str++; note--; break;
	case 's': str++; note++; break;
	}
	octave = strtoint(str, 10);
	if (octave < -4 || octave > 11) error(ERR_NOTE);
	return note + 12*octave;
}

static char *makepath(const char *dir, const char *name, const char *ext)
{
	char *path = malloc(strlen(dir)+1+strlen(name)+strlen(ext)+1);
	strcpy(path, dir);
	strcat(path, "/");
	strcat(path, name);
	strcat(path, ext);
	return path;
}

#define CMD_ROOT 0
#define CMD_WAVE 1
#define CMD_BANK 2
#define CMD_INST 3
#define CMD_PERC 4

static short stack[3];
static int sp, pc;

static char *name;
static int limit;

static void Name(char *tok)
{
	name = strdup(tok);
}

static void Limit(char *tok)
{
	limit = strtonote(tok);
	if (limit < 0 || limit > 127) error(ERR_NOTE);
}

static void Next(char *tok, int t)
{
	if (t == '}')
	{
	}
	else if (t == ',')
	{
		pc -= 2;
	}
	else unexpected(tok, t);
}

static void Term(char *tok, int t)
{
	if (t == '}')
	{
		pc++;
	}
	else if (t == ',')
	{
	}
	else unexpected(tok, t);
}

static void Wave(char *tok)
{
	if (ListFind(&wavelist, tok)) redefined(tok);
	stack[++sp] = CMD_WAVE;
	wavep = calloc(1, sizeof(WAVE));
	wavep->path = makepath(output, tok, ".tbl");
	ListAppend(&wavelist, strdup(tok), wavep);
}

static void Bank(char *tok)
{
	if (ListFind(&banklist, tok)) redefined(tok);
	stack[++sp] = CMD_BANK;
	bankp = calloc(1, sizeof(BANK));
	bankp->path = makepath(output, tok, ".ctl");
	ListAppend(&banklist, strdup(tok), bankp);
}

static void WBExit()
{
	wavep = NULL;
	bankp = NULL;
}

static void WSound(char *tok)
{
	SOUND *sound;
	const char *err;
	char *path = NULL;
	FILE *fp = NULL;
	if (ListFind(&wavep->sound, name)) redefined(name);
	sound = calloc(1, sizeof(SOUND));
	if (
		!(root && (fp = fopen(path = makepath(root, tok, ""), "rb"))) &&
		!(fp = fopen(tok, "rb"))
	)
	{
		fprintf(stderr, "error: %s: file not found\n", tok);
		exit(1);
	}
	if ((err = SoundLoad(sound, fp)))
	{
		fprintf(stderr, "%s: %s\n", tok, err);
		exit(1);
	}
	fclose(fp);
	free(path);
	ListAppend(&wavep->sound, name, sound);
}

static void BDate(char *tok)
{
	bankp->date = strtoint(tok, 16);
}

static void BWave(char *tok)
{
	if (!(wavep = ListFind(&wavelist, tok))) undefined(tok);
	bankp->wave = wavep;
	wavep->ref++;
}

static void BEnv(char *tok)
{
	ENVELOPE *env;
	if (ListFind(&bankp->env, tok)) redefined(tok);
	env = calloc(1, sizeof(ENVELOPE));
	ListAppend(&bankp->env, strdup(tok), env);
}

static void BEnvItem(char *tok, int t)
{
	ENVELOPE *env = (ENVELOPE *)bankp->env.item;
	if (t == '}')
	{
		pc++;
	}
	else if (t == TOK_SYM)
	{
		if (env->len >= env->alloc) env->data = realloc(
			env->data, sizeof(short)*(env->alloc += 8)
		);
		env->data[env->len++] = strtoint(tok, 0);
	}
	else unexpected(tok, t);
}

static void BInst(char *tok)
{
	int i = strtoint(tok, 0);
	if (i < bankp->ninst && bankp->itab[i]) redefidx("instrument", i);
	stack[++sp] = CMD_INST;
	instp = calloc(1, sizeof(INST));
	instp->rel = 208;
	instp->max = 127;
	if (i >= bankp->ialloc)
	{
		bankp->itab =
			realloc(bankp->itab, sizeof(INST *)*(bankp->ialloc += 16));
		memset(&bankp->itab[bankp->ialloc-16], 0, sizeof(INST *)*16);
	}
	bankp->itab[i] = instp;
	if (bankp->ninst < i+1) bankp->ninst = i+1;
	ListAppend(&bankp->inst, NULL, instp);
}

static void BPerc(char *tok)
{
	int i = strtoint(tok, 0);
	if (i < bankp->nperc && bankp->ptab[i]) redefidx("percussion", i);
	stack[++sp] = CMD_PERC;
	instp = calloc(1, sizeof(INST));
	instp->rel = 10;
	instp->pan = 63;
	if (i >= bankp->palloc)
	{
		bankp->ptab =
			realloc(bankp->ptab, sizeof(INST *)*(bankp->palloc += 64));
		memset(&bankp->ptab[bankp->palloc-64], 0, sizeof(INST *)*64);
	}
	bankp->ptab[i] = instp;
	if (bankp->nperc < i+1) bankp->nperc = i+1;
	if (bankp->ninst <  10) bankp->ninst = 10;
	ListAppend(&bankp->perc, NULL, instp);
}

static void IRel(char *tok)
{
	instp->rel = strtoint(tok, 0);
}

static void IPan(char *tok)
{
	instp->pan = strtoint(tok, 0);
}

static void IEnv(char *tok)
{
	if (!(instp->env = ListFind(&bankp->env, tok))) undefined(tok);
}

static void ISndCommon(char *tok, int i)
{
	BSND *bsnd;
	int note = strtonote(tok);
	if (stack[sp] == CMD_INST) note = 39-(note-39);
	if (note < 0 || note > 127) error(ERR_NOTE);
	if (!wavep) error(ERR_NOWAVE);
	if (!(bsnd = ListFind(&bankp->bsnd, name)))
	{
		SOUND *sound;
		if (!(sound = ListFind(&wavep->sound, name))) undefined(name);
		bsnd = calloc(1, sizeof(BSND));
		bsnd->sound = sound;
		ListAppend(&bankp->bsnd, name, bsnd);
	}
	else
	{
		free(name);
	}
	instp->bsnd[i] = bsnd;
	instp->freq[i] = bsnd->sound->rate * Na_FreqTable[note];
}

static void ISndL(char *tok)
{
	ISndCommon(tok, 0);
	instp->min = limit;
}

static void ISnd(char *tok)
{
	ISndCommon(tok, 1);
}

static void ISndH(char *tok)
{
	ISndCommon(tok, 2);
	instp->max = limit;
}

static void IExit()
{
	instp = NULL;
}

typedef void (*SEQ)();

typedef struct cmd
{
	const char *name;
	const char *tok;
	const SEQ *seq;
}
CMD;

static const char tok_root[] = {TOK_SYM,'{',TOK_END};
static const char tok_exit[] = {'}',';',TOK_END};
static const char tok_wsound[] = {TOK_SYM,'"',';',TOK_END};
static const char tok_entry[] = {'=',TOK_SYM,';',TOK_END};
static const char tok_benv[] = {TOK_SYM,'{',' ',' ',';',TOK_END};
static const char tok_binst[] = {'[',TOK_SYM,']','=','{',TOK_END};
static const char tok_isndL[] =
	{'=','{',TOK_SYM,',',TOK_SYM,',',TOK_SYM,' ','}',';',TOK_END};
static const char tok_isnd[] =
	{'=','{',TOK_SYM,',',TOK_SYM,' ','}',';',TOK_END};

static const SEQ seq_wave[] = {Wave, NULL};
static const SEQ seq_bank[] = {Bank, NULL};
static const SEQ seq_wbexit[] = {WBExit, NULL};
static const SEQ seq_wsound[] = {Name, WSound, NULL};
static const SEQ seq_bdate[] = {NULL, BDate, NULL};
static const SEQ seq_bwave[] = {BWave, NULL};
static const SEQ seq_benv[] = {BEnv, NULL, BEnvItem, Next, NULL};
static const SEQ seq_binst[] = {NULL, BInst, NULL, NULL, NULL};
static const SEQ seq_bperc[] = {NULL, BPerc, NULL, NULL, NULL};
static const SEQ seq_irel[] = {NULL, IRel, NULL};
static const SEQ seq_ipan[] = {NULL, IPan, NULL};
static const SEQ seq_ienv[] = {NULL, IEnv, NULL};
static const SEQ seq_isndL[] =
	{NULL, NULL, Limit, NULL, Name, NULL, ISndL, Term, NULL, NULL};
static const SEQ seq_isnd[] =
	{NULL, NULL, Name, NULL, ISnd, Term, NULL, NULL};
static const SEQ seq_isndH[] =
	{NULL, NULL, Limit, NULL, Name, NULL, ISndH, Term, NULL, NULL};
static const SEQ seq_iexit[] = {IExit, NULL};

static const CMD cmd_root[] =
{
	{"wave", tok_root, seq_wave},
	{"bank", tok_root, seq_bank},
	{0},
};

static const CMD cmd_wave[] =
{
	{"sound", tok_wsound, seq_wsound},
	{NULL, tok_exit, seq_wbexit},
};

static const CMD cmd_bank[] =
{
	{"date", tok_entry, seq_bdate},
	{"wave", &tok_entry[1], seq_bwave},
	{"envelope", tok_benv, seq_benv},
	{"instrument", tok_binst, seq_binst},
	{"percussion", tok_binst, seq_bperc},
	{NULL, tok_exit, seq_wbexit},
};

static const CMD cmd_inst[] =
{
	{"release", tok_entry, seq_irel},
	{"envelope", tok_entry, seq_ienv},
	{"soundL", tok_isndL, seq_isndL},
	{"sound", tok_isnd, seq_isnd},
	{"soundH", tok_isndL, seq_isndH},
	{NULL, tok_exit, seq_iexit},
};

static const CMD cmd_perc[] =
{
	{"release", tok_entry, seq_irel},
	{"pan", tok_entry, seq_ipan},
	{"envelope", tok_entry, seq_ienv},
	{"sound", tok_isnd, seq_isnd},
	{NULL, tok_exit, seq_iexit},
};

static const CMD *const cmdtab[] =
{
	cmd_root,
	cmd_wave,
	cmd_bank,
	cmd_inst,
	cmd_perc,
};

#define ALIGN(x) (((x)+15) & ~15)

static void falign(FILE *fp)
{
	static char zero[16];
	fwrite(zero, 1, -ftell(fp) & 15, fp);
}

#define fwriteblk(fp, blk) fwrite((blk)->data, 1, (blk)->size, fp)

static void fputshort(short s, FILE *fp)
{
	fputc(s >> 8, fp);
	fputc(s >> 0, fp);
}

static void fputint(int i, FILE *fp)
{
	fputc(i >> 24, fp);
	fputc(i >> 16, fp);
	fputc(i >>  8, fp);
	fputc(i >>  0, fp);
}

static void fputfloat(float f, FILE *fp)
{
	union {int i; float f;} pkt;
	pkt.f = f;
	fputint(pkt.i, fp);
}

#define fputaddr(obj, fp) fputint((obj) ? (obj)->addr : 0, fp)

int main(int argc, char *argv[])
{
	int i, t;
	unsigned int addr;
	char *tok;
	const CMD *cmd = NULL;
	SOUND *sound;
	WAVE *wave;
	BSND *bsnd;
	ENVELOPE *env;
	INST *inst;
	BANK *bank;
	FILE *fp;
	char *line = NULL;
	size_t linesize = 0;
	if (argc != 2)
	{
		fprintf(stderr, "usage: %s <output>\n", argv[0]);
		return 1;
	}
	output = argv[1];
	for (ln = 1; getline(&line, &linesize, stdin) > 0; ln++)
	{
		switch (line[0])
		{
		case '#':
			free(fn);
			fn = NULL;
			free(root);
			root = NULL;
			toknew(line+1);
			if (token(&tok) != TOK_SYM) error(ERR_INTERNAL);
			ln = strtoint(tok, 0);
			if (token(&tok) != TOK_STR) error(ERR_INTERNAL);
			fn = strdup(tok);
			if ((tok = strrchr(fn, '/')))
			{
				size_t n = tok-fn;
				memcpy(root = malloc(n+1), fn, n);
				root[n] = '\0';
			}
			break;
		default:
			toknew(line);
			while ((t = token(&tok)))
			{
				if (t < 0)
				{
					switch (t)
					{
					case TOK_ETOK: error(ERR_TOK); break;
					case TOK_ESTR: error(ERR_STR); break;
					}
					error(ERR_INTERNAL);
				}
				if (!cmd)
				{
					if (!(cmd = cmdtab[stack[sp]])) error(ERR_INTERNAL);
					if (t == TOK_SYM)
					{
						for (; cmd->name; cmd++)
						{
							if (!strcmp(cmd->name, tok)) break;
						}
						if (!cmd->name) error(ERR_COMMAND);
						pc = 0;
						continue;
					}
					else
					{
						if (--sp < 0) error(ERR_SYNTAX);
						for (; cmd->name; cmd++);
						pc = 0;
					}
				}
				if (cmd->tok[pc] != ' ' && t != cmd->tok[pc])
				{
					unexpected(tok, t);
				}
				if (cmd->seq[pc]) cmd->seq[pc](tok, t);
				if (cmd->tok[++pc] == TOK_END) cmd = NULL;
			}
		}
	}
	free(line);
	for (wave = (WAVE *)wavelist.root; wave; wave = wave->next)
	{
		if (!(fp = fopen(wave->path, "wb")))
		{
			fprintf(stderr, "error: could not open '%s'\n", wave->path);
			return 1;
		}
		for (sound = (SOUND *)wave->sound.root; sound; sound = sound->next)
		{
			falign(fp);
			sound->addr = ftell(fp);
			fwriteblk(fp, sound);
		}
		fclose(fp);
	}
	for (bank = (BANK *)banklist.root; bank; bank = bank->next)
	{
		wave = bank->wave;
		if (!(fp = fopen(bank->path, "wb")))
		{
			fprintf(stderr, "error: could not open '%s'\n", bank->path);
			return 1;
		}
		fputint(bank->ninst, fp);
		fputint(bank->nperc, fp);
		fputint(wave->ref > 1, fp);
		fputint(bank->date, fp);
		for (i = 0; i < 1+bank->ninst; i++) fputint(0, fp);
		falign(fp);
		addr = ALIGN(4*(1+bank->ninst));
		for (bsnd = (BSND *)bank->bsnd.root; bsnd; bsnd = bsnd->next)
		{
			unsigned int loop = 0, book = 0;
			sound = bsnd->sound;
			bsnd->addr = addr;
			addr += ALIGN(20);
			if (sound->book.data)
			{
				book = addr;
				addr += ALIGN(8+sound->book.size);
			}
			if (sound->loop.data)
			{
				loop = addr;
				addr += ALIGN(12);
				if (sound->loop.count) addr += ALIGN(32);
			}
			fputint(0, fp);
			fputint(sound->addr, fp);
			fputint(loop, fp);
			fputint(book, fp);
			fputint(sound->size, fp);
			falign(fp);
			fputint(sound->book.order, fp);
			fputint(sound->book.npredictors, fp);
			if (sound->book.data) fwriteblk(fp, &sound->book);
			falign(fp);
			fputint(sound->loop.start, fp);
			fputint(sound->loop.end, fp);
			fputint(sound->loop.count, fp);
			falign(fp);
			if (sound->loop.count) fwriteblk(fp, &sound->loop);
			falign(fp);
		}
		for (env = (ENVELOPE *)bank->env.root; env; env = env->next)
		{
			env->addr = addr;
			addr += ALIGN(2*env->len);
			for (i = 0; i < env->len; i++) fputshort(env->data[i], fp);
			falign(fp);
		}
		for (inst = (INST *)bank->inst.root; inst; inst = inst->next)
		{
			inst->addr = addr;
			addr += ALIGN(32);
			fputc(0, fp);
			fputc(inst->min, fp);
			fputc(inst->max, fp);
			fputc(inst->rel, fp);
			fputaddr(inst->env, fp);
			for (i = 0; i < 3; i++)
			{
				fputaddr(inst->bsnd[i], fp);
				fputfloat(inst->freq[i], fp);
			}
			falign(fp);
		}
		if (bank->nperc > 0)
		{
			for (inst = (INST *)bank->perc.root; inst; inst = inst->next)
			{
				inst->addr = addr;
				addr += ALIGN(16);
				fputc(inst->rel, fp);
				fputc(inst->pan, fp);
				fputc(0, fp);
				fputc(0, fp);
				fputaddr(inst->bsnd[1], fp);
				fputfloat(inst->freq[1], fp);
				fputaddr(inst->env, fp);
				falign(fp);
			}
			for (i = 0; i < bank->nperc; i++) fputaddr(bank->ptab[i], fp);
			falign(fp);
			fseek(fp, 16, SEEK_SET);
			fputint(addr, fp);
		}
		fseek(fp, 20, SEEK_SET);
		for (i = 0; i < bank->ninst; i++) fputaddr(bank->itab[i], fp);
		puts(bank->path);
		puts(wave->path);
	}
	return 0;
}
