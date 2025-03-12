#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <getopt.h>

static int error(const char *err)
{
	fprintf(stderr, "error: %s\n", err);
	return 1;
}

typedef struct vtx
{
	short x, y, z;
}
VTX;

typedef struct map
{
	VTX *vtx;
	int valloc, vcount;
}
MAP;

typedef struct tri
{
	short v0, v1, v2;
	char *attr, *area;
}
TRI;

typedef struct bg
{
	struct bg *next;
	char *code;
	TRI *tri;
	int talloc, tcount;
}
BG;

static void vtx_append(MAP *map, int x, int y, int z)
{
	VTX *vtx;
	if (map->vcount >= map->valloc)
	{
		map->vtx = realloc(map->vtx, sizeof(VTX)*(map->valloc += 1024));
	}
	vtx = &map->vtx[map->vcount++];
	vtx->x = x;
	vtx->y = y;
	vtx->z = z;
}

static void tri_append(BG *bg, int v0, int v1, int v2, char *attr, char *area)
{
	TRI *tri;
	if (bg->tcount >= bg->talloc)
	{
		bg->tri = realloc(bg->tri, sizeof(TRI)*(bg->talloc += 1024));
	}
	tri = &bg->tri[bg->tcount++];
	tri->v0 = v0;
	tri->v1 = v1;
	tri->v2 = v2;
	tri->attr = attr;
	tri->area = area;
}

static int tri_get(short *v)
{
	long x;
	char *str;
	if (!(str = strtok(NULL, " "))) return 0;
	if (!(x = strtol(str, NULL, 0))) return -1;
	*v = x-1;
	return 1;
}

int main(int argc, char *argv[])
{
	int i, result;
	MAP map;
	BG *root = NULL, **next = &root, *bg = NULL;
	char *attr = NULL, *area = NULL;
	FILE *fp;
	char *line = NULL;
	size_t linesize = 0;
	if (argc < 3 || argc > 4)
	{
		fprintf(stderr, "usage: %s <obj> <map> [area]\n", argv[0]);
		return 1;
	}
	if (!(fp = fopen(argv[1], "r")))
	{
		fprintf(stderr, "error: could not open '%s'\n", argv[1]);
		return 1;
	}
	memset(&map, 0, sizeof(MAP));
	while (getline(&line, &linesize, fp) > 0)
	{
		short v[3];
		char *tok = strtok(line, " ");
		if (!strcmp(tok, "v"))
		{
			for (i = 0; i < 3; i++) v[i] = strtof(strtok(NULL, " "), NULL);
			vtx_append(&map, v[0], v[1], v[2]);
			if (map.vcount > 10921) return error("vtx over");
		}
		else if (!strcmp(tok, "f"))
		{
			if (!bg)
			{
				*next = bg = calloc(1, sizeof(BG));
				bg->code = "0";
				bg->tri = NULL;
			}
			for (i = 0; i < 3; i++)
			{
				if (tri_get(&v[i]) < 1) return error("face malformed");
			}
			tri_append(bg, v[0], v[1], v[2], attr, area);
			while ((result = tri_get(&v[2])))
			{
				if (result < 0) return error("face malformed");
				tri_append(bg, v[0], v[1], v[2], attr, area);
				v[1] = v[2];
			}
		}
		else if (!strcmp(tok, "usemtl"))
		{
			char *code = strtok(NULL, "\n;");
			if ((area = strtok(NULL, "\n;"))) area = strdup(area);
			code = strtok(code, ",");
			if ((attr = strtok(NULL, ","))) attr = strdup(attr);
			for (bg = root; bg; bg = bg->next)
			{
				if (!strcmp(code, bg->code)) break;
			}
			if (!bg)
			{
				*next = bg = calloc(1, sizeof(BG));
				next = &bg->next;
				bg->code = strdup(code);
				bg->tri = NULL;
			}
		}
	}
	free(line);
	fclose(fp);
	if (!(fp = fopen(argv[2], "w")))
	{
		fprintf(stderr, "error: could not open '%s'\n", argv[2]);
		return 1;
	}
	fprintf(fp, "MAP_VTX,%d,\n", map.vcount);
	for (i = 0; i < map.vcount; i++)
	{
		VTX *vtx = &map.vtx[i];
		fprintf(fp, "%d,%d,%d,\n", vtx->x, vtx->y, vtx->z);
	}
	for (bg = root; bg; bg = bg->next)
	{
		fprintf(fp, "%s,%d,\n", bg->code, bg->tcount);
		for (i = 0; i < bg->tcount; i++)
		{
			TRI *tri = &bg->tri[i];
			fprintf(fp, "%d,%d,%d,", tri->v0, tri->v1, tri->v2);
			if (tri->attr) fprintf(fp, "%s,", tri->attr);
			fputc('\n', fp);
		}
	}
	fputs("MAP_BGEND,\n", fp);
	if (argc > 3)
	{
		if (!(fp = fopen(argv[3], "w")))
		{
			fprintf(stderr, "error: could not open '%s'\n", argv[3]);
			return 1;
		}
		for (bg = root; bg; bg = bg->next)
		{
			for (i = 0; i < bg->tcount; i++)
			{
				TRI *tri = &bg->tri[i];
				if (!tri->area) return error("null area");
				fprintf(fp, "%s,", tri->area);
			}
			fputc('\n', fp);
		}
	}
	return 0;
}
