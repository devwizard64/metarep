#ifndef __SM64_OBJLANG_H__
#define __SM64_OBJLANG_H__

#include <sm64/defshape.h>
#include <sm64/defobject.h>
#include <sm64/defobjlang.h>
#include <sm64/scriptasm.h>

#define objInit(type) \
	_C(OBJ_CMD_INIT, type, 0)
#define objSleep(time) \
	_C(OBJ_CMD_SLEEP, 0, time)
#define objCall(script) \
	_C(OBJ_CMD_CALL, 0, 0); \
	_P(script)
#define objReturn() \
	_C(OBJ_CMD_RETURN, 0, 0)
#define objJump(script) \
	_C(OBJ_CMD_JUMP, 0, 0); \
	_P(script)
#define objFor(count) \
	_C(OBJ_CMD_FOR, 0, count)
#define objFend() \
	_C(OBJ_CMD_FEND, 0, 0)
#define objFcontinue() \
	_C(OBJ_CMD_FCONTINUE, 0, 0)
#define objWhile() \
	_C(OBJ_CMD_WHILE, 0, 0)
#define objWend() \
	_C(OBJ_CMD_WEND, 0, 0)
#define objExit() \
	_C(OBJ_CMD_EXIT, 0, 0)
#define objEnd() \
	_C(OBJ_CMD_END, 0, 0)
#define objCallback(callback) \
	_C(OBJ_CMD_CALLBACK, 0, 0); \
	_P(callback)
#define objAddF(work, val) \
	_C(OBJ_CMD_ADDF, work, val)
#define objSetF(work, val) \
	_C(OBJ_CMD_SETF, work, val)
#define objAddI(work, val) \
	_C(OBJ_CMD_ADDI, work, val)
#define objSetI(work, val) \
	_C(OBJ_CMD_SETI, work, val)
#define objSetFlag(work, val) \
	_C(OBJ_CMD_SETFLAG, work, val)
#define objClrFlag(work, val) \
	_C(OBJ_CMD_CLRFLAG, work, val)
#define objSetRandA(work, start, shift) \
	_C(OBJ_CMD_SETRANDA, work, start); \
	_H(shift, 0)
#define objSetRandF(work, start, range) \
	_C(OBJ_CMD_SETRANDF, work, start); \
	_H(range, 0)
#define objSetRandI(work, start, range) \
	_C(OBJ_CMD_SETRANDI, work, start); \
	_H(range, 0)
#define objAddRandF(work, start, range) \
	_C(OBJ_CMD_ADDRANDF, work, start); \
	_H(range, 0)
#define objAddRandA(work, start, shift) \
	_C(OBJ_CMD_ADDRANDA, work, start); \
	_H(shift, 0)
/* 24 */
/* 25 */
/* 26 */
#define objSetShape(shape) \
	_C(OBJ_CMD_SETSHAPE, 0, shape)
#define objMakeObj(shape, script) \
	_C(OBJ_CMD_MAKEOBJ, 0, 0); \
	_W(shape); \
	_P(script)
#define objDestroy() \
	_C(OBJ_CMD_DESTROY, 0, 0)
#define objGround() \
	_C(OBJ_CMD_GROUND, 0, 0)
#define objAddFW(work, a, b) \
	_B(OBJ_CMD_ADDFW, work, a, b)
#define objAddIW(work, a, b) \
	_B(OBJ_CMD_ADDIW, work, a, b)
#define objBillboard() \
	_C(OBJ_CMD_BILLBOARD, 0, 0)
#define objHide() \
	_C(OBJ_CMD_HIDE, 0, 0)
#define objSetHitBox(radius, height) \
	_C(OBJ_CMD_SETHITBOX, 0, 0); \
	_H(radius, height)
/* 36 */
#define objSleepW(work) \
	_C(OBJ_CMD_SLEEPW, work, 0)
#define objFor2(count) \
	_C(OBJ_CMD_FOR2, count, 0)
#define objSetPtr(work, ptr) \
	_C(OBJ_CMD_SETPTR, work, 0); \
	_P(ptr)
#define objSetAnime(anime) \
	_C(OBJ_CMD_SETANIME, anime, 0)
#define objMakeObjCode(shape, script, code) \
	_C(OBJ_CMD_MAKEOBJCODE, 0, code); \
	_W(shape); \
	_P(script)
#define objSetMap(map) \
	_C(OBJ_CMD_SETMAP, 0, 0); \
	_P(map)
#define objSetHitBoxOff(radius, height, offset) \
	_C(OBJ_CMD_SETHITBOXOFF, 0, 0); \
	_H(radius, height); \
	_H(offset, 0)
#define objMakeChild(shape, script) \
	_C(OBJ_CMD_MAKECHILD, 0, 0); \
	_W(shape); \
	_P(script)
#define objSavePos() \
	_C(OBJ_CMD_SAVEPOS, 0, 0)
#define objSetDmgBox(radius, height) \
	_C(OBJ_CMD_SETDMGBOX, 0, 0); \
	_H(radius, height)
#define objSetHitType(type) \
	_C(OBJ_CMD_SETHITTYPE, 0, 0); \
	_W(type)
#define objSetPhysics(radius, gravity, density, drag, friction, bounce) \
	_C(OBJ_CMD_SETPHYSICS, 0, 0); \
	_H(radius, gravity); \
	_H(density, drag); \
	_H(friction, bounce); \
	_H(0, 0)
#define objSetHitFlag(flag) \
	_C(OBJ_CMD_SETHITFLAG, 0, 0); \
	_W(flag)
#define objSetScale(scale) \
	_C(OBJ_CMD_SETSCALE, 0, scale)
#define objClrParentFlagW(work, flag) \
	_C(OBJ_CMD_CLRPARENTFLAGW, work, 0); \
	_W(flag)
#define objInc(work, period) \
	_C(OBJ_CMD_INC, work, period)
#define objClrActive() \
	_C(OBJ_CMD_CLRACTIVE, 0, 0)
#define objSetS(work, val) \
	_C(OBJ_CMD_SETS, work, 0); \
	_W(val)
#define objMakeSplash(splash) \
	_C(OBJ_CMD_MAKESPLASH, 0, 0); \
	_P(splash)

#endif /* __SM64_OBJLANG_H__ */
