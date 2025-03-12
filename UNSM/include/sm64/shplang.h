#ifndef __SM64_SHPLANG_H__
#define __SM64_SHPLANG_H__

#include <ultra64.h>
#include <sm64/types.h>
#include <sm64/defshape.h>
#include <sm64/defshadow.h>
#include <sm64/defbackground.h>
#include <sm64/defweather.h>
#include <sm64/defshplang.h>
#include <sm64/scriptc.h>

#define shpExecute(script) \
	_C(SHP_CMD_EXECUTE, 0, 0), \
	_P(script)
#define shpExit() \
	_C(SHP_CMD_EXIT, 0, 0)
#define shpJump(script) \
	_C(SHP_CMD_JUMP, 0, 0), \
	_P(script)
#define shpCall(script) \
	_C(SHP_CMD_JUMP, 1, 0), \
	_P(script)
#define shpReturn() \
	_C(SHP_CMD_RETURN, 0, 0)
#define shpBegin() \
	_C(SHP_CMD_BEGIN, 0, 0)
#define shpEnd() \
	_C(SHP_CMD_END, 0, 0)
#define shpStore(index) \
	_C(SHP_CMD_STORE, 0, index)
#define shpFlag(flag) \
	_C(SHP_CMD_FLAG, 0, flag)
#define shpSetFlag(flag) \
	_C(SHP_CMD_FLAG, 1, flag)
#define shpClrFlag(flag) \
	_C(SHP_CMD_FLAG, 2, flag)
#define shpScene(x, y, w, h, n) \
	_C(SHP_CMD_SCENE, 0, n), \
	_H(x, y), \
	_H(w, h)
#define shpOrtho(scale) \
	_C(SHP_CMD_ORTHO, 0, scale)
#define shpPersp(fovy, n, f) \
	_C(SHP_CMD_PERSP, 0, fovy), \
	_H(n, f)
#define shpPerspective(fovy, n, f, callback) \
	_C(SHP_CMD_PERSP, 1, fovy), \
	_H(n, f), \
	_P(callback)
#define shpEmpty() \
	_C(SHP_CMD_EMPTY, 0, 0)
#define shpLayer(depth) \
	_C(SHP_CMD_LAYER, depth, 0)
#define shpLOD(min, max) \
	_C(SHP_CMD_LOD, 0, 0), \
	_H(min, max)
#define shpSelect(arg, callback) \
	_C(SHP_CMD_SELECT, 0, arg), \
	_P(callback)
#define shpCamera(arg, eye_x, eye_y, eye_z, look_x, look_y, look_z, callback) \
	_C(SHP_CMD_CAMERA, 0, arg), \
	_H(eye_x, eye_y), \
	_H(eye_z, look_x), \
	_H(look_y, look_z), \
	_P(callback)
#define shpCoord(posx, posy, posz, angx, angy, angz) \
	_C(SHP_CMD_COORD, 0x00, 0), \
	_H(posx, posy), \
	_H(posz, angx), \
	_H(angy, angz)
#define shpCoordPos(posx, posy, posz) \
	_C(SHP_CMD_COORD, 0x10, posx), \
	_H(posy, posz)
#define shpCoordAng(angx, angy, angz) \
	_C(SHP_CMD_COORD, 0x20, angx), \
	_H(angy, angz)
#define shpCoordAngY(angy) \
	_C(SHP_CMD_COORD, 0x30, angy)
#define shpGfxCoord(layer, gfx, posx, posy, posz, angx, angy, angz) \
	_C(SHP_CMD_COORD, 0x80 | layer, 0), \
	_H(posx, posy), \
	_H(posz, angx), \
	_H(angy, angz), \
	_P(gfx)
#define shpGfxCoordPos(layer, gfx, posx, posy, posz) \
	_C(SHP_CMD_COORD, 0x90 | layer, posx), \
	_H(posy, posz)
#define shpGfxCoordAng(layer, gfx, angx, angy, angz) \
	_C(SHP_CMD_COORD, 0xA0 | layer, angx), \
	_H(angy, angz), \
	_P(gfx)
#define shpGfxCoordAngY(layer, gfx, angy) \
	_C(SHP_CMD_COORD, 0xB0 | layer, angy), \
	_P(gfx)
#define shpPos(posx, posy, posz) \
	_C(SHP_CMD_POS, 0x00, posx), \
	_H(posy, posz)
#define shpGfxPos(layer, gfx, posx, posy, posz) \
	_C(SHP_CMD_POS, 0x80 | layer, posx), \
	_H(posy, posz), \
	_P(gfx)
#define shpAng(angx, angy, angz) \
	_C(SHP_CMD_ANG, 0x00, angx), \
	_H(angy, angz)
#define shpGfxAng(layer, gfx, angx, angy, angz) \
	_C(SHP_CMD_ANG, 0x80 | layer, angx), \
	_H(angy, angz), \
	_P(gfx)
#define shpJoint(layer, gfx, posx, posy, posz) \
	_C(SHP_CMD_JOINT, layer, posx), \
	_H(posy, posz), \
	_P(gfx)
#define shpBillboard(posx, posy, posz) \
	_C(SHP_CMD_BILLBOARD, 0x00, posx), \
	_H(posy, posz)
#define shpGfxBillboard(layer, gfx, posx, posy, posz) \
	_C(SHP_CMD_BILLBOARD, 0x80 | layer, posx), \
	_H(posy, posz), \
	_P(gfx)
#define shpGfx(layer, gfx) \
	_C(SHP_CMD_GFX, layer, 0), \
	_P(gfx)
#define shpShadow(size, alpha, type) \
	_C(SHP_CMD_SHADOW, 0, type), \
	_H(alpha, size)
#define shpObject() \
	_C(SHP_CMD_OBJECT, 0, 0)
#define shpCallback(arg, callback) \
	_C(SHP_CMD_CALLBACK, 0, arg), \
	_P(callback)
#define shpBackground(arg, callback) \
	_C(SHP_CMD_BACK, 0, arg), \
	_P(callback)
/* 26 */
#define shpBranch(index) \
	_C(SHP_CMD_BRANCH, 0, index)
#define shpHand(posx, posy, posz, arg, callback) \
	_C(SHP_CMD_HAND, arg, posx), \
	_H(posy, posz), \
	_P(callback)
#define shpScale(scale) \
	_C(SHP_CMD_SCALE, 0x00, 0), \
	_F(scale)
#define shpGfxScale(layer, gfx, scale) \
	_C(SHP_CMD_SCALE, 0x80 | layer, 0), \
	_F(scale), \
	_P(gfx)
/* 30 */
/* 31 */
#define shpCull(dist) \
	_C(SHP_CMD_CULL, 0, dist)

typedef struct shape SHAPE;

extern void *CtrlWeather(int code, SHAPE *shape, void *data);
extern void *CtrlBackground(int code, SHAPE *shape, void *data);
extern void *CtrlCamera(int code, SHAPE *shape, void *data);
extern void *CtrlPerspective(int code, SHAPE *shape, void *data);
extern void *CtrlCannonOverlay(int code, SHAPE *shape, void *data);

extern void *Ctrl_pldemo_80257198(int code, SHAPE *shape, void *data);

extern void *CtrlObjectHand(int code, SHAPE *shape, void *data);
extern void *CtrlObjectAlpha(int code, SHAPE *shape, void *data);
extern void *CtrlObjectShape(int code, SHAPE *shape, void *data);
extern void *CtrlArea(int code, SHAPE *shape, void *data);
extern void *Ctrl_objectlib_802A45E4(int code, SHAPE *shape, void *data);

extern void *Ctrl_enemya_802A719C(int, SHAPE *, void *); /* callback */
extern void *Ctrl_enemya_802B798C(int, SHAPE *, void *); /* callback */
extern void *Ctrl_enemya_802B7C64(int, SHAPE *, void *); /* select */
extern void *Ctrl_enemya_802B7D44(int, SHAPE *, void *); /* callback */
extern void *Ctrl_enemya_802BA2B0(int, SHAPE *, void *); /* callback */
extern void *Ctrl_enemya_802BFBAC(int, SHAPE *, void *); /* select */

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

extern void *Ctrl_enemyc_8030D93C(int, SHAPE *, void *); /* callback */
extern void *Ctrl_enemyc_8030D9AC(int, SHAPE *, void *); /* callback */

#endif /* __SM64_SHPLANG_H__ */
