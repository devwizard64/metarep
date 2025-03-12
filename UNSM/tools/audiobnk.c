#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static const char *fn;
static unsigned int ln;

static void error(const char *err)
{
	fprintf(stderr, "%s:%u: %s\n", fn, ln, err);
	exit(1);
}

typedef struct bnk
{
	struct bnk *next;
	unsigned char len;
	unsigned char data[256];
}
BNK;

static BNK *getbnk(char *line)
{
	BNK *bnk = NULL;
	char *tok, *end;
	for (tok = strtok(line, " "); tok && *tok != '#'; tok = strtok(NULL, " "))
	{
		long x = strtol(tok, &end, 0);
		if (tok == end) error("syntax error");
		if (!bnk) bnk = calloc(1, sizeof(BNK));
		bnk->data[bnk->len++] = x;
	}
	return bnk;
}

int main(int argc, char *argv[])
{
	int i, count = 0, ptr;
	BNK *root = NULL, **next = &root, *bnk;
	FILE *fp;
	char *line = NULL;
	size_t linesize = 0;
	if (argc != 2)
	{
		fprintf(stderr, "usage: %s <bnk>\n", argv[0]);
		return 1;
	}
	if (!(fp = fopen(fn = argv[1], "r")))
	{
		fprintf(stderr, "error: could not open '%s'\n", fn);
		return 1;
	}
	for (ln = 1; getline(&line, &linesize, fp) > 0; ln++)
	{
		if ((bnk = getbnk(line)))
		{
			*next = bnk;
			next = &bnk->next;
			count++;
		}
	}
	free(line);
	fclose(fp);
	printf(".data\n");
	ptr = 2*count;
	for (bnk = root; bnk; bnk = bnk->next)
	{
		printf(".short %d\n", ptr);
		ptr += 1+bnk->len;
	}
	for (bnk = root; bnk; bnk = bnk->next)
	{
		printf(".byte %d", bnk->len);
		for (i = 0; i < bnk->len; i++) printf(",%d", bnk->data[i]);
		putchar('\n');
	}
	return 0;
}
