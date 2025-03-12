#ifndef __TOKEN_H__
#define __TOKEN_H__

#define TOK_END         0
#define TOK_SYM         1
#define TOK_STR         '"'

#define TOK_EOVER       -1
#define TOK_ETOK        -2
#define TOK_ESTR        -3

extern void toknew(char *str);
extern char *tokraw(void);
extern int token(char **tok);

#endif /* __TOKEN_H__ */
