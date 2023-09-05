#ifndef __SM64_OBJLANG_H__
#define __SM64_OBJLANG_H__

#include <sm64/defshape.h>
#include <sm64/defobject.h>
#include <sm64/script_s.h>

#define oInit(type) \
	_C(0x00, type, 0)
#define oSleep(time) \
	_C(0x01, 0, time)
#define oCall(script) \
	_C(0x02, 0, 0); \
	_P(script)
#define oReturn() \
	_C(0x03, 0, 0)
#define oJump(script) \
	_C(0x04, 0, 0); \
	_P(script)
#define oFor(count) \
	_C(0x05, 0, count)
#define oFend() \
	_C(0x06, 0, 0)
#define oFcontinue() \
	_C(0x07, 0, 0)
#define oWhile() \
	_C(0x08, 0, 0)
#define oWend() \
	_C(0x09, 0, 0)
#define oExit() \
	_C(0x0A, 0, 0)
#define oEnd() \
	_C(0x0B, 0, 0)
#define oCallback(callback) \
	_C(0x0C, 0, 0); \
	_P(callback)
#define oAddF(mem, val) \
	_C(0x0D, mem, val)
#define oSetF(mem, val) \
	_C(0x0E, mem, val)
#define oAddI(mem, val) \
	_C(0x0F, mem, val)
#define oSetI(mem, val) \
	_C(0x10, mem, val)
#define oSetFlag(mem, val) \
	_C(0x11, mem, val)
#define oClrFlag(mem, val) \
	_C(0x12, mem, val)
#define oSetRandA(mem, val, shift) \
	_C(0x13, mem, val); \
	_H(shift, 0)
#define oSetRandF(mem, val, mul) \
	_C(0x14, mem, val); \
	_H(mul, 0)
#define oSetRandI(mem, val, mul) \
	_C(0x15, mem, val); \
	_H(mul, 0)
#define oAddRandF(mem, val, mul) \
	_C(0x16, mem, val); \
	_H(mul, 0)
#define oAddRandA(mem, val, shift) \
	_C(0x17, mem, val); \
	_H(shift, 0)
/* 0x18 */
/* 0x19 */
/* 0x1A */
#define oShape(shape) \
	_C(0x1B, 0, shape)
#define oObject(shape, script) \
	_C(0x1C, 0, 0); \
	_W(shape); \
	_P(script)
#define oDestroy() \
	_C(0x1D, 0, 0)
#define oGround() \
	_C(0x1E, 0, 0)
#define oMemAddF(mem, a, b) \
	_B(0x1F, mem, a, b)
#define oMemAddI(mem, a, b) \
	_B(0x20, mem, a, b)
#define oBillboard() \
	_C(0x21, 0, 0)
#define oShapeHide() \
	_C(0x22, 0, 0)
#define oColHit(radius, height) \
	_C(0x23, 0, 0); \
	_H(radius, height)
/* 0x24 */
#define oMemSleep(mem) \
	_C(0x25, mem, 0)
#define oFor2(count) \
	_C(0x26, count, 0)
#define oPtr(mem, ptr) \
	_C(0x27, mem, 0); \
	_P(ptr)
#define oAnime(anime) \
	_C(0x28, anime, 0)
#define oObjectArg(shape, script, arg) \
	_C(0x29, 0, arg); \
	_W(shape); \
	_P(script)
#define oMap(map) \
	_C(0x2A, 0, 0); \
	_P(map)
#define oColOff(radius, height, offset) \
	_C(0x2B, 0, 0); \
	_H(radius, height); \
	_H(offset, 0)
#define oChild(shape, script) \
	_C(0x2C, 0, 0); \
	_W(shape); \
	_P(script)
#define oOrigin() \
	_C(0x2D, 0, 0)
#define oColDmg(radius, height) \
	_C(0x2E, 0, 0); \
	_H(radius, height)
#define oColType(type) \
	_C(0x2F, 0, 0); \
	_W(type)
#define oPhysics(wall_r, gravity, bounce, drag, friction, density, g, h) \
	_C(0x30, 0, 0); \
	_H(wall_r, gravity); \
	_H(bounce, drag); \
	_H(friction, density); \
	_H(g, h)
#define oColArg(arg) \
	_C(0x31, 0, 0); \
	_W(arg)
#define oScale(scale) \
	_C(0x32, 0, scale)
#define oMemClrFlag(mem, flag) \
	_C(0x33, mem, 0); \
	_W(flag)
#define oInc(mem, time) \
	_C(0x34, mem, time)
#define oShapeDisable() \
	_C(0x35, 0, 0)
#define oSetS(mem, val) \
	_C(0x36, 0, 0); \
	_W(val)
#define oSplash(splash) \
	_C(0x37, 0, 0); \
	_P(splash)

#endif /* __SM64_OBJLANG_H__ */
