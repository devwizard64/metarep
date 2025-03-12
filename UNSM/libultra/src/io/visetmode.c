#include <ultra64.h>
#include <assert.h>
#include "osint.h"
#include "viint.h"












































void osViSetMode(OSViMode *modep)
{
	register u32 saveMask;
#ifdef _DEBUG
	if (!__osViDevMgr.active)
	{
		__osError(ERR_OSVISETMODE, 0);
		return;
	}
	assert(modep != NULL);
#endif
	saveMask = __osDisableInt();
	__osViNext->modep = modep;
	__osViNext->state = VI_STATE_NORMAL|VI_STATE_MODE;
	__osViNext->control = __osViNext->modep->comRegs.ctrl;
	__osRestoreInt(saveMask);
}
