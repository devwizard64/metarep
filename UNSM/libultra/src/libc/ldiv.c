#include <stdlib.h>

ldiv_t ldiv(long numer, long denom)
{
	ldiv_t val;
	val.quot = numer / denom;
	val.rem = numer - denom*val.quot;
	if (val.quot < 0 && 0 < val.rem)
	{
		val.quot += 1;
		val.rem -= denom;
	}
	return val;
}

lldiv_t lldiv(long long numer, long long denom)
{
	lldiv_t val;
	val.quot = numer / denom;
	val.rem = numer - denom*val.quot;
	if (val.quot < 0 && 0 < val.rem)
	{
		val.quot += 1;
		val.rem -= denom;
	}
	return val;
}
