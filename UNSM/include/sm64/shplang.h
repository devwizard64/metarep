#ifndef __SM64_SHPLANG_H__
#define __SM64_SHPLANG_H__

#include <ultra64.h>
#include <sm64/types.h>
#include <sm64/defshape.h>
#include <sm64/defshadow.h>
#include <sm64/defbackground.h>
#include <sm64/defweather.h>
#include <sm64/defshplang.h>
#include <sm64/script_c.h>

#define sExecute(script) \
	_C(SHP_CMD_EXECUTE, 0, 0), \
	_P(script)
#define sExit() \
	_C(SHP_CMD_EXIT, 0, 0)
#define sJump(script) \
	_C(SHP_CMD_JUMP, 0, 0), \
	_P(script)
#define sCall(script) \
	_C(SHP_CMD_JUMP, 1, 0), \
	_P(script)
#define sReturn() \
	_C(SHP_CMD_RETURN, 0, 0)
#define sStart() \
	_C(SHP_CMD_START, 0, 0)
#define sEnd() \
	_C(SHP_CMD_END, 0, 0)
#define sStore(index) \
	_C(SHP_CMD_STORE, 0, index)
#define sFlag(flag) \
	_C(SHP_CMD_FLAG, 0, flag)
#define sSetFlag(flag) \
	_C(SHP_CMD_FLAG, 1, flag)
#define sClrFlag(flag) \
	_C(SHP_CMD_FLAG, 2, flag)
#define sScene(x, y, w, h, n) \
	_C(SHP_CMD_SCENE, 0, n), \
	_H(x, y), \
	_H(w, h)
#define sOrtho(scale) \
	_C(SHP_CMD_ORTHO, 0, scale)
#define sPersp(fovy, n, f) \
	_C(SHP_CMD_PERSP, 0, fovy), \
	_H(n, f)
#define sPerspective(fovy, n, f, callback) \
	_C(SHP_CMD_PERSP, 1, fovy), \
	_H(n, f), \
	_P(callback)
#define sEmpty() \
	_C(SHP_CMD_EMPTY, 0, 0)
#define sLayer(depth) \
	_C(SHP_CMD_LAYER, depth, 0)
#define sLOD(min, max) \
	_C(SHP_CMD_LOD, 0, 0), \
	_H(min, max)
#define sSelect(arg, callback) \
	_C(SHP_CMD_SELECT, 0, arg), \
	_P(callback)
#define sCamera(arg, eye_x, eye_y, eye_z, look_x, look_y, look_z, callback) \
	_C(SHP_CMD_CAMERA, 0, arg), \
	_H(eye_x, eye_y), \
	_H(eye_z, look_x), \
	_H(look_y, look_z), \
	_P(callback)
#define sCoord(posx, posy, posz, angx, angy, angz) \
	_C(SHP_CMD_COORD, 0x00, 0), \
	_H(posx, posy), \
	_H(posz, angx), \
	_H(angy, angz)
#define sCoordPos(posx, posy, posz) \
	_C(SHP_CMD_COORD, 0x10, posx), \
	_H(posy, posz)
#define sCoordAng(angx, angy, angz) \
	_C(SHP_CMD_COORD, 0x20, angx), \
	_H(angy, angz)
#define sCoordAngY(angy) \
	_C(SHP_CMD_COORD, 0x30, angy)
#define sGfxCoord(layer, gfx, posx, posy, posz, angx, angy, angz) \
	_C(SHP_CMD_COORD, 0x80 | layer, 0), \
	_H(posx, posy), \
	_H(posz, angx), \
	_H(angy, angz), \
	_P(gfx)
#define sGfxCoordPos(layer, gfx, posx, posy, posz) \
	_C(SHP_CMD_COORD, 0x90 | layer, posx), \
	_H(posy, posz)
#define sGfxCoordAng(layer, gfx, angx, angy, angz) \
	_C(SHP_CMD_COORD, 0xA0 | layer, angx), \
	_H(angy, angz), \
	_P(gfx)
#define sGfxCoordAngY(layer, gfx, angy) \
	_C(SHP_CMD_COORD, 0xB0 | layer, angy), \
	_P(gfx)
#define sPos(posx, posy, posz) \
	_C(SHP_CMD_POS, 0x00, posx), \
	_H(posy, posz)
#define sGfxPos(layer, gfx, posx, posy, posz) \
	_C(SHP_CMD_POS, 0x80 | layer, posx), \
	_H(posy, posz), \
	_P(gfx)
#define sAng(angx, angy, angz) \
	_C(SHP_CMD_ANG, 0x00, angx), \
	_H(angy, angz)
#define sGfxAng(layer, gfx, angx, angy, angz) \
	_C(SHP_CMD_ANG, 0x80 | layer, angx), \
	_H(angy, angz), \
	_P(gfx)
#define sJoint(layer, gfx, posx, posy, posz) \
	_C(SHP_CMD_JOINT, layer, posx), \
	_H(posy, posz), \
	_P(gfx)
#define sBillboard(posx, posy, posz) \
	_C(SHP_CMD_BILLBOARD, 0x00, posx), \
	_H(posy, posz)
#define sGfxBillboard(layer, gfx, posx, posy, posz) \
	_C(SHP_CMD_BILLBOARD, 0x80 | layer, posx), \
	_H(posy, posz), \
	_P(gfx)
#define sGfx(layer, gfx) \
	_C(SHP_CMD_GFX, layer, 0), \
	_P(gfx)
#define sShadow(size, alpha, type) \
	_C(SHP_CMD_SHADOW, 0, type), \
	_H(alpha, size)
#define sObject() \
	_C(SHP_CMD_OBJECT, 0, 0)
#define sCallback(arg, callback) \
	_C(SHP_CMD_CALLBACK, 0, arg), \
	_P(callback)
#define sBackground(arg, callback) \
	_C(SHP_CMD_BACK, 0, arg), \
	_P(callback)
/* 26 */
#define sBranch(index) \
	_C(SHP_CMD_BRANCH, 0, index)
#define sHand(posx, posy, posz, arg, callback) \
	_C(SHP_CMD_HAND, arg, posx), \
	_H(posy, posz), \
	_P(callback)
#define sScale(scale) \
	_C(SHP_CMD_SCALE, 0x00, 0), \
	_F(scale)
#define sGfxScale(layer, gfx, scale) \
	_C(SHP_CMD_SCALE, 0x80 | layer, 0), \
	_F(scale), \
	_P(gfx)
/* 30 */
/* 31 */
#define sCull(dist) \
	_C(SHP_CMD_CULL, 0, dist)

typedef struct shape SHAPE;

extern void *CtrlWeather(int code, SHAPE *shape, void *data);
extern void *CtrlBackground(int code, SHAPE *shape, void *data);
extern void *CtrlCamera(int code, SHAPE *shape, void *data);
extern void *CtrlPerspective(int code, SHAPE *shape, void *data);
extern void *CtrlCannonOverlay(int code, SHAPE *shape, void *data);

extern void *Ctrl_pldemo_80257198(int, SHAPE *, void *); /* select */

extern void *CtrlObjectHand(int, SHAPE *, void *); /* callback */
extern void *CtrlObjectAlpha(int, SHAPE *, void *); /* callback */
extern void *CtrlObjectShape(int, SHAPE *, void *); /* select */
extern void *CtrlArea(int, SHAPE *, void *); /* select */
extern void *Ctrl_objectlib_802A45E4(int, SHAPE *, void *); /* callback */

extern void *Ctrl_object_a_802A719C(int, SHAPE *, void *); /* callback */
extern void *Ctrl_object_a_802B798C(int, SHAPE *, void *); /* callback */
extern void *Ctrl_object_a_802B7C64(int, SHAPE *, void *); /* select */
extern void *Ctrl_object_a_802B7D44(int, SHAPE *, void *); /* callback */
extern void *Ctrl_object_a_802BA2B0(int, SHAPE *, void *); /* callback */
extern void *Ctrl_object_a_802BFBAC(int, SHAPE *, void *); /* select */

extern void *CtrlPoolLevel(int code, SHAPE *shape, void *data);
extern void *CtrlWaterProc(int code, SHAPE *shape, void *data);
extern void *CtrlWaterDraw(int code, SHAPE *shape, void *data);
extern void *CtrlFluid(int code, SHAPE *shape, void *data);
extern void *CtrlFluidL(int code, SHAPE *shape, void *data);
extern void *CtrlFluidDrawL(int code, SHAPE *shape, void *data);
extern void *CtrlFluidDrawS(int code, SHAPE *shape, void *data);
extern void *CtrlFluidProc(int code, SHAPE *shape, void *data);

extern void *CtrlWaveDraw(int code, SHAPE *shape, void *data);
extern void *CtrlWaveProc(int code, SHAPE *shape, void *data);

extern void *Ctrl_object_c_8030D93C(int, SHAPE *, void *); /* callback */
extern void *Ctrl_object_c_8030D9AC(int, SHAPE *, void *); /* callback */

#endif /* __SM64_SHPLANG_H__ */
