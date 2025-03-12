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
#define ERR_SUB         "unterminated substitution"
#define ERR_FLAG        "invalid flag"
#define ERR_COMMAND     "invalid command"
#define ERR_EXTRA       "extra token at end of line"
#define ERR_EOL         "unexpected end of line"
#define ERR_NOENDSEG    "missing endseg"
#define ERR_INSEGMENT   "already in segment"
#define ERR_NOSEGMENT   "not in segment"
#define ERR_NONAME      "missing name"
#define ERR_NOOBJECT    "need OBJECT flag"
#define ERR_BOOT1       "first segment must be BOOT"
#define ERR_BOOT2       "multiple BOOT segments"

static char *fn;
static unsigned int ln;

static void error(const char *err)
{
	if (fn) fprintf(stderr, "%s:%u: %s\n", fn, ln, err);
	else    fprintf(stderr, "internal error\n");
	exit(1);
}

/******************************************************************************/

static int gettok(void *tok)
{
	int t = token(tok);
	if (t < 0)
	{
		switch (t)
		{
		case TOK_ETOK: error(ERR_TOK); break;
		case TOK_ESTR: error(ERR_STR); break;
		}
		error(ERR_INTERNAL);
	}
	return t;
}

static void getend(void)
{
	if (gettok(NULL)) error(ERR_EXTRA);
}

static char *getraw(void)
{
	char *tok;
	if (!(tok = tokraw())) error(ERR_EOL);
	return strdup(tok);
}

static char *getsym(void)
{
	int t;
	char *tok;
	if ((t = gettok(&tok)) != TOK_SYM)
	{
		if (t == TOK_END) return NULL;
		error(ERR_SYNTAX);
	}
	return tok;
}

static int getint(void)
{
	long x;
	char *tok, *endptr;
	if (gettok(&tok) != TOK_SYM) error(ERR_SYNTAX);
	x = strtol(tok, &endptr, 0);
	if (*endptr != '\0') error(ERR_INT);
	return x;
}

static char *getstr(void)
{
	char *tok;
	if (gettok(&tok) != TOK_STR) error(ERR_SYNTAX);
	return strdup(tok);
}

static char *pathcat(char *dst, const char *src)
{
	if (src)
	{
		if (dst)
		{
			return strcat(dst = realloc(dst, strlen(dst)+strlen(src)+1), src);
		}
		return strdup(src);
	}
	return dst;
}

static char *getpath(void)
{
	int c;
	char *tok, *str, *path = NULL;
	char buf[2];
	if (gettok(&tok) != TOK_STR) error(ERR_SYNTAX);
	while ((str = strchr(tok, '$')))
	{
		*str++ = '\0';
		path = pathcat(path, tok);
		tok = str;
		switch (c = *tok++)
		{
		case '(':
			if (!(str = strchr(tok, ')'))) error(ERR_SUB);
			*str++ = '\0';
			pathcat(path, getenv(tok));
			tok = str;
			break;
		default:
			buf[0] = c;
			buf[1] = '\0';
			pathcat(path, getenv(buf));
			break;
		}
	}
	return pathcat(path, tok);
}

/******************************************************************************/

#define OBJECT  1
#define BOOT    2

typedef struct segment
{
	struct segment *next;
	char *name;
	char *address;
	char *maxaddr;
	char *entry;
	char *stack;
	char **include;
	int incalloc, ninclude;
	int flags;
}
SEGMENT;

static SEGMENT *root, **next, *segment;

static void cmd_beginseg(void)
{
	getend();
	if (segment) error(ERR_INSEGMENT);
	segment = calloc(1, sizeof(SEGMENT));
}

static void cmd_endseg(void)
{
	getend();
	if (!segment) error(ERR_NOSEGMENT);
	if (!segment->name) error(ERR_NONAME);
	if (!(segment->flags & OBJECT)) error(ERR_NOOBJECT);
	if (segment->flags & BOOT)
	{
		if (root) error(ERR_BOOT2);
	}
	else
	{
		if (!root) error(ERR_BOOT1);
	}
	*next = segment;
	next = &segment->next;
	segment = NULL;
}

static void cmd_name(void)
{
	if (!segment) error(ERR_NOSEGMENT);
	segment->name = getstr();
	getend();
}

static const char *const flagtab[] =
{
	"OBJECT",
	"BOOT",
	NULL,
};

static void cmd_flags(void)
{
	int i;
	char *tok;
	if (!segment) error(ERR_NOSEGMENT);
	while ((tok = getsym()))
	{
		for (i = 0;; i++)
		{
			if (!flagtab[i]) error(ERR_FLAG);
			if (!strcmp(tok, flagtab[i]))
			{
				segment->flags |= 1 << i;
				break;
			}
		}
	}
}

static void cmd_address(void)
{
	if (!segment) error(ERR_NOSEGMENT);
	segment->address = getraw();
}

static void cmd_number(void)
{
	if (!segment) error(ERR_NOSEGMENT);
	sprintf(segment->address = malloc(16), "0x%08X", getint() << 24);
}

static void cmd_maxaddr(void)
{
	if (!segment) error(ERR_NOSEGMENT);
	segment->maxaddr = getraw();
}

static void cmd_entry(void)
{
	if (!segment) error(ERR_NOSEGMENT);
	segment->entry = getraw();
}

static void cmd_stack(void)
{
	if (!segment) error(ERR_NOSEGMENT);
	segment->stack = getraw();
}

static void cmd_include(void)
{
	if (!segment) error(ERR_NOSEGMENT);
	if (segment->ninclude >= segment->incalloc) segment->include = realloc(
		segment->include, sizeof(char *)*(segment->incalloc += 64)
	);
	segment->include[segment->ninclude++] = getpath();
	getend();
}

typedef struct cmd
{
	const char *name;
	void (*exec)(void);
}
CMD;

static CMD cmdtab[] =
{
	{"beginseg",    cmd_beginseg},
	{"endseg",      cmd_endseg},
	{"name",        cmd_name},
	{"flags",       cmd_flags},
	{"address",     cmd_address},
	{"number",      cmd_number},
	{"maxaddr",     cmd_maxaddr},
	{"entry",       cmd_entry},
	{"stack",       cmd_stack},
	{"include",     cmd_include},
	{0},
};

/******************************************************************************/

typedef struct section
{
	char flag;
	const char *name;
	const char *const *section;
}
SECTION;

static const char *const sec_text[] = {".text*", NULL};
static const char *const sec_data[] = {".data", ".rodata*", NULL};
static const char *const sec_sdata[] = {".sdata", ".lit8", ".lit4", NULL};
static const char *const sec_sbss[] = {".sbss", ".scommon", NULL};
static const char *const sec_bss[] = {".bss", "COMMON", NULL};

static const SECTION sectiontab[] =
{
	{1, "text", sec_text},
	{1, "data", sec_data},
	{1, "sdata", sec_sdata},
	{0, "sbss", sec_sbss},
	{0, "bss", sec_bss},
};

static const char *const bootfmt[] =
{
	"\t__crt0BssStart = _%sSegmentBssStart;\n",
	"\t__crt0BssEnd = _%sSegmentBssEnd;\n",
	"\tENTRY(_%sSegmentTextStart)\n",
	NULL,
};

static const char *const segfmt[] =
{
	"\t_%sSegmentRomEnd = __rom;\n",
	"\t_%sSegmentStart = ", "ADDR(.%s.text);\n",
	"\t_%sSegmentTextStart = ", "ADDR(.%s.text);\n",
	"\t_%sSegmentTextEnd = ", "ADDR(.%s.text) + ", "SIZEOF(.%s.text);\n",
	"\t_%sSegmentDataStart = ", "ADDR(.%s.data);\n",
	"\t_%sSegmentDataEnd = ", "ADDR(.%s.data) + ", "SIZEOF(.%s.data) + ",
		"SIZEOF(.%s.sdata);\n",
	"\t_%sSegmentBssStart = ", "ADDR(.%s.sbss);\n",
	"\t_%sSegmentBssEnd = ", "ADDR(.%s.sbss) + ", "SIZEOF(.%s.sbss) + ",
		"SIZEOF(.%s.bss);\n",
	"\t_%sSegmentEnd = ", "ADDR(.%s.bss) + ", "SIZEOF(.%s.bss);\n",
	NULL,
};

static void printflist(const char *const *fmt, const char *str)
{
	while (*fmt) printf(*fmt++, str);
}

int main(void)
{
	int i, n, x;
	SEGMENT *seg;
	char *line = NULL;
	size_t linesize = 0;
	next = &root;
	for (ln = 1; getline(&line, &linesize, stdin) > 0; ln++)
	{
		char *tok;
		switch (line[0])
		{
		case '#':
			free(fn);
			fn = NULL;
			toknew(line+1);
			ln = getint();
			fn = getstr();
			break;
		default:
			toknew(line);
			if (!(tok = getsym())) continue;
			for (i = 0;; i++)
			{
				if (!cmdtab[i].name) error(ERR_COMMAND);
				if (!strcmp(tok, cmdtab[i].name))
				{
					cmdtab[i].exec();
					break;
				}
			}
			break;
		}
	}
	free(line);
	if (segment) error(ERR_NOENDSEG);
	printf(
		"OUTPUT_ARCH(mips)\n"
		"SECTIONS\n"
		"{\n"
		"\t__rom = 0x1000;\n"
	);
	for (seg = root; seg; seg = seg->next)
	{
		if (seg->flags & BOOT)
		{
			if (seg->entry) printf("\t__crt0Entry = %s;\n", seg->entry);
			if (seg->stack) printf("\t__crt0Stack = %s;\n", seg->stack);
			printflist(bootfmt, seg->name);
		}
		if (seg->address) printf("\t. = %s;\n", seg->address);
		printf("\t_%sSegmentRomStart = __rom;\n", seg->name);
		for (i = 0; i < 5; i++)
		{
			const SECTION *sec = &sectiontab[i];
			printf(
				"\t.%s.%s : AT(__rom) SUBALIGN(16) {\n", seg->name, sec->name
			);
			if (i == 0 && seg->flags & BOOT) printf("\t\t. += 0x50;\n");
			for (n = 0; n < seg->ninclude; n++)
			{
				for (x = 0; sec->section[x]; x++)
				{
					printf(
						"\t\t%s(%s); . = ALIGN(16);\n",
						seg->include[n], sec->section[x]
					);
				}
			}
			printf("\t}\n");
			if (sec->flag)
			{
				printf("\t__rom += SIZEOF(.%s.%s);\n", seg->name, sec->name);
			}
		}
		if (seg->flags & BOOT) printf(
			"\tASSERT(__rom <= 0x101000, "
			"\"error: boot segment is too large\")\n"
		);
		if (seg->maxaddr) printf(
			"\tASSERT(. <= (%s), \"error: segment '%s' is too large\")\n",
			seg->maxaddr, seg->name
		);
		printflist(segfmt, seg->name);
	}
	printf("\t/DISCARD/ : { *(*) }\n}\n");
	return 0;
}
