#include "token.h"
#include <string.h>
#include <ctype.h>

static char *tokptr;
static char tokchr;

void toknew(char *str)
{
	tokptr = str;
	tokchr = '\0';
	while (*str != '\0') str++;
	while (str != tokptr && isspace(str[-1])) str--;
	*str = '\0';
}

char *tokraw(void)
{
	if (tokptr)
	{
		if (tokchr != '\0')
		{
			*tokptr = tokchr;
			tokchr = '\0';
		}
		while (isspace(*tokptr)) tokptr++;
	}
	return tokptr;
}

int token(char **tok)
{
	int c;
	char *str;
	if (tok) *tok = NULL;
	if (!(str = tokraw())) return TOK_EOVER;
	if ((c = *str) == '\0')
	{
		str = NULL;
		c = TOK_END;
	}
	else if (c == '"')
	{
		str++;
		if (tok) *tok = str;
		for (; (c = *str) != '"'; str++)
		{
			if (c == '\0')
			{
				tokptr = NULL;
				return TOK_ESTR;
			}
			if (c == '\\')
			{
				switch (*str)
				{
				case '"':
				case '\\':
					strcpy(str, str+1);
					str--;
					break;
				}
			}
		}
		*str++ = '\0';
		c = TOK_STR;
	}
	else if (strchr(",;=[]{}", c))
	{
		str++;
	}
	else
	{
		if (tok) *tok = str;
		for (; (c = *str) != '\0'; str++)
		{
			if (strchr("!#$%&'()*/:<>?@\\^`|~", c))
			{
				tokptr = NULL;
				return TOK_ETOK;
			}
			if (strchr(",;=[]{}", c))
			{
				tokchr = *str;
				*str = '\0';
				break;
			}
			if (isspace(c))
			{
				*str++ = '\0';
				break;
			}
		}
		c = TOK_SYM;
	}
	tokptr = str;
	return c;
}
