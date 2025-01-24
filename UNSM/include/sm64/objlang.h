#ifndef __SM64_OBJLANG_H__
#define __SM64_OBJLANG_H__

#include <sm64/defshape.h>
#include <sm64/defobject.h>
#include <sm64/defobjlang.h>
#include <sm64/script_s.h>

#define oInit(type) \
	_C(OBJ_CMD_INIT, type, 0)
#define oSleep(time) \
	_C(OBJ_CMD_SLEEP, 0, time)
#define oCall(script) \
	_C(OBJ_CMD_CALL, 0, 0); \
	_P(script)
#define oReturn() \
	_C(OBJ_CMD_RETURN, 0, 0)
#define oJump(script) \
	_C(OBJ_CMD_JUMP, 0, 0); \
	_P(script)
#define oFor(count) \
	_C(OBJ_CMD_FOR, 0, count)
#define oFend() \
	_C(OBJ_CMD_FEND, 0, 0)
#define oFcontinue() \
	_C(OBJ_CMD_FCONTINUE, 0, 0)
#define oWhile() \
	_C(OBJ_CMD_WHILE, 0, 0)
#define oWend() \
	_C(OBJ_CMD_WEND, 0, 0)
#define oExit() \
	_C(OBJ_CMD_EXIT, 0, 0)
#define oEnd() \
	_C(OBJ_CMD_END, 0, 0)
#define oCallback(callback) \
	_C(OBJ_CMD_CALLBACK, 0, 0); \
	_P(callback)
#define oAddF(mem, val) \
	_C(OBJ_CMD_ADDF, mem, val)
#define oSetF(mem, val) \
	_C(OBJ_CMD_SETF, mem, val)
#define oAddI(mem, val) \
	_C(OBJ_CMD_ADDI, mem, val)
#define oSetI(mem, val) \
	_C(OBJ_CMD_SETI, mem, val)
#define oSetFlag(mem, val) \
	_C(OBJ_CMD_SETFLAG, mem, val)
#define oClrFlag(mem, val) \
	_C(OBJ_CMD_CLRFLAG, mem, val)
#define oSetRandA(mem, add, shift) \
	_C(OBJ_CMD_SETRANDA, mem, add); \
	_H(shift, 0)
#define oSetRandF(mem, add, mul) \
	_C(OBJ_CMD_SETRANDF, mem, add); \
	_H(mul, 0)
#define oSetRandI(mem, add, mul) \
	_C(OBJ_CMD_SETRANDI, mem, add); \
	_H(mul, 0)
#define oAddRandF(mem, add, mul) \
	_C(OBJ_CMD_ADDRANDF, mem, add); \
	_H(mul, 0)
#define oAddRandA(mem, add, shift) \
	_C(OBJ_CMD_ADDRANDA, mem, add); \
	_H(shift, 0)
/* 24 */
/* 25 */
/* 26 */
#define oShape(shape) \
	_C(OBJ_CMD_SHAPE, 0, shape)
#define oMakeObj(shape, script) \
	_C(OBJ_CMD_MAKEOBJ, 0, 0); \
	_W(shape); \
	_P(script)
#define oDestroy() \
	_C(OBJ_CMD_DESTROY, 0, 0)
#define oGround() \
	_C(OBJ_CMD_GROUND, 0, 0)
#define oMemAddF(mem, a, b) \
	_B(OBJ_CMD_MEMADDF, mem, a, b)
#define oMemAddI(mem, a, b) \
	_B(OBJ_CMD_MEMADDI, mem, a, b)
#define oBillboard() \
	_C(OBJ_CMD_BILLBOARD, 0, 0)
#define oHide() \
	_C(OBJ_CMD_HIDE, 0, 0)
#define oHitBox(radius, height) \
	_C(OBJ_CMD_HITBOX, 0, 0); \
	_H(radius, height)
/* 36 */
#define oMemSleep(mem) \
	_C(OBJ_CMD_MEMSLEEP, mem, 0)
#define oFor2(count) \
	_C(OBJ_CMD_FOR2, count, 0)
#define oPtr(mem, ptr) \
	_C(OBJ_CMD_PTR, mem, 0); \
	_P(ptr)
#define oAnime(anime) \
	_C(OBJ_CMD_ANIME, anime, 0)
#define oMakeObjCode(shape, script, code) \
	_C(OBJ_CMD_MAKEOBJCODE, 0, code); \
	_W(shape); \
	_P(script)
#define oMap(map) \
	_C(OBJ_CMD_MAP, 0, 0); \
	_P(map)
#define oHitBoxOff(radius, height, offset) \
	_C(OBJ_CMD_HITBOXOFF, 0, 0); \
	_H(radius, height); \
	_H(offset, 0)
#define oMakeChild(shape, script) \
	_C(OBJ_CMD_MAKECHILD, 0, 0); \
	_W(shape); \
	_P(script)
#define oSavePos() \
	_C(OBJ_CMD_SAVEPOS, 0, 0)
#define oDmgBox(radius, height) \
	_C(OBJ_CMD_DMGBOX, 0, 0); \
	_H(radius, height)
#define oHitType(type) \
	_C(OBJ_CMD_HITTYPE, 0, 0); \
	_W(type)
#define oPhysics(radius, gravity, density, drag, friction, bounce) \
	_C(OBJ_CMD_PHYSICS, 0, 0); \
	_H(radius, gravity); \
	_H(density, drag); \
	_H(friction, bounce); \
	_H(0, 0)
#define oHitFlag(flag) \
	_C(OBJ_CMD_HITFLAG, 0, 0); \
	_W(flag)
#define oScale(scale) \
	_C(OBJ_CMD_SCALE, 0, scale)
#define oMemClrParentFlag(mem, flag) \
	_C(OBJ_CMD_MEMCLRPARENTFLAG, mem, 0); \
	_W(flag)
#define oInc(mem, period) \
	_C(OBJ_CMD_INC, mem, period)
#define oClrActive() \
	_C(OBJ_CMD_CLRACTIVE, 0, 0)
#define oSetS(mem, val) \
	_C(OBJ_CMD_SETS, mem, 0); \
	_W(val)
#define oSplash(splash) \
	_C(OBJ_CMD_SPLASH, 0, 0); \
	_P(splash)

#endif /* __SM64_OBJLANG_H__ */
