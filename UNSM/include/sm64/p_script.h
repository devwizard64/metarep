#ifndef __SM64_P_SCRIPT_H__
#define __SM64_P_SCRIPT_H__

#include <sm64/segment.h>
#include <sm64/defstage.h>
#include <sm64/defscene.h>
#include <sm64/defshape.h>
#include <sm64/defaudio.h>
#include <sm64/script_s.h>

#define FALSE   0
#define TRUE    1

#define P_CMP_AND               0
#define P_CMP_NAND              1
#define P_CMP_EQ                2
#define P_CMP_NE                3
#define P_CMP_GT                4
#define P_CMP_GE                5
#define P_CMP_LT                6
#define P_CMP_LE                7

#define P_VAR_SAVE              0
#define P_VAR_COURSE            1
#define P_VAR_LEVEL             2
#define P_VAR_STAGE             3
#define P_VAR_SCENE             4

#define pExecute(seg, start, end, script) \
	_C(0x00, 0x10, seg); \
	_P(start); \
	_P(end); \
	_P(script)
#define pChain(seg, start, end, script) \
	_C(0x01, 0x10, seg); \
	_P(start); \
	_P(end); \
	_P(script)
#define pExit() \
	_C(0x02, 0x04, 0)
#define pSleep(x) \
	_C(0x03, 0x04, x)
#define pFreeze(x) \
	_C(0x04, 0x04, x)
#define pJump(script) \
	_C(0x05, 0x08, 0); \
	_P(script)
#define pCall(script) \
	_C(0x06, 0x08, 0); \
	_P(script)
#define pReturn() \
	_C(0x07, 0x04, 0)
#define pFor(count) \
	_C(0x08, 0x04, count)
#define pDone() \
	_C(0x09, 0x04, 0)
#define pDo() \
	_C(0x0A, 0x04, 0)
#define pWhile(cmp, val) \
	_B(0x0B, 0x08, P_CMP_##cmp, 0); \
	_W(val);
#define pJumpIf(cmp, val, script) \
	_B(0x0C, 0x0C, P_CMP_##cmp, 0); \
	_W(val); \
	_P(script)
#define pCallIf(cmp, val, script) \
	_B(0x0D, 0x0C, P_CMP_##cmp, 0); \
	_W(val); \
	_P(script)
#define pIf(cmp, val) \
	_B(0x0E, 0x0C, P_CMP_##cmp, 0); \
	_W(val)
#define pElse() \
	_C(0x0F, 0x04, 0)
#define pEndif() \
	_C(0x10, 0x04, 0)
#define pCallback(callback, arg) \
	_C(0x11, 0x08, arg); \
	_P(callback)
#define pProcess(callback, arg) \
	_C(0x12, 0x08, arg); \
	_P(callback)
#define pSet(val) \
	_C(0x13, 0x04, val)
#define pPush() \
	_C(0x14, 0x04, 0)
#define pPull() \
	_C(0x15, 0x04, 0)
#define pLoadCode(addr, start, end) \
	_C(0x16, 0x10, 0); \
	_P(addr); \
	_P(start); \
	_P(end)
#define pLoadData(seg, start, end) \
	_C(0x17, 0x0C, seg); \
	_P(start); \
	_P(end)
#define pLoadSzp(seg, start, end) \
	_C(0x18, 0x0C, seg); \
	_P(start); \
	_P(end)
#define pLoadFace(arg) \
	_C(0x19, 0x04, arg)
#define pLoadTxt(seg, start, end) \
	_C(0x1A, 0x0C, seg); \
	_P(start); \
	_P(end)
#define pStageInit() \
	_C(0x1B, 0x04, 0)
#define pStageExit() \
	_C(0x1C, 0x04, 0)
#define pStageStart() \
	_C(0x1D, 0x04, 0)
#define pStageEnd() \
	_C(0x1E, 0x04, 0)
#define pSceneStart(scene, script) \
	_B(0x1F, 0x08, scene, 0); \
	_P(script)
#define pSceneEnd() \
	_C(0x20, 0x04, 0)
#define pShapeGfx(shape, gfx, layer) \
	_C(0x21, 0x08, layer << 12 | (shape)); \
	_P(gfx)
#define pShapeScript(shape, script) \
	_C(0x22, 0x08, shape); \
	_P(script)
#define pShapeScale(shape, gfx, layer, scale) \
	_C(0x23, 0x08, layer << 12 | (shape)); \
	_P(gfx); \
	_F(scale)
#define pObjectMask( \
	mask, shape, px, py, pz, ax, ay, az, \
	arg0, arg1, flag, script \
) \
	_B(0x24, 0x18, mask, shape); \
	_H(px, py); \
	_H(pz, ax); \
	_H(ay, az); \
	_C(arg0, arg1, flag); \
	_P(script)
#define pObject( \
	shape, px, py, pz, ax, ay, az, \
	arg0, arg1, flag, script \
) \
	pObjectMask(0x1F, shape, px, py, pz, ax, ay, az, arg0, arg1, flag, script)
#define pPlayer(shape, arg0, arg1, flag, script) \
	_B(0x25, 0x0C, 0, shape); \
	_C(arg0, arg1, flag); \
	_P(script)
#define pMario() \
	pPlayer(S_MARIO, 0, 0, 1, o_mario)
#define pPort(index, stage, scene, port) \
	_B(0x26, 0x08, index, stage); \
	_B(scene, port, 0x00, 0)
#define pPortMid(index, stage, scene, port) \
	_B(0x26, 0x08, index, stage); \
	_B(scene, port, 0x80, 0)
#define pBGPort(index, stage, scene, port) \
	_B(0x27, 0x08, index, stage); \
	_B(scene, port, 0x00, 0)
#define pBGPortMid(index, stage, scene, port) \
	_B(0x27, 0x08, index, stage); \
	_B(scene, port, 0x80, 0)
#define pConnect(index, scene, px, py, pz) \
	_B(0x28, 0x0C, index, scene); \
	_H(px, py); \
	_H(pz, 0)
#define pSceneOpen(scene) \
	_B(0x29, 0x04, scene, 0)
#define pSceneClose(scene) \
	_B(0x2A, 0x04, scene, 0)
#define pPlayerOpen(scene, ay, px, py, pz) \
	_B(0x2B, 0x0C, scene, 0); \
	_H(ay, px); \
	_H(py, pz)
/* 0x2C PlayerClose */
#define pSceneUpdate() \
	_C(0x2D, 0x08, 0)
#define pMap(map) \
	_C(0x2E, 0x08, 0); \
	_P(map)
#define pArea(area) \
	_C(0x2F, 0x08, 0); \
	_P(area)
#define pMsg(type, msg) \
	_B(0x30, 0x04, type, msg)
#define pEnv(env) \
	_C(0x31, 0x04, env)
/* 0x32 */
#define pWipe(type, time, r, g, b) \
	_B(0x33, 0x08, type, time); \
	_B(r, g, b, 0)
#define pViBlack(arg) \
	_B(0x34, 0x04, arg, 0)
#define pViGamma(arg) \
	_B(0x35, 0x04, arg, 0)
#define pBgm(mode, bgm) \
	_C(0x36, 0x08, mode); \
	_H(bgm, 0)
#define pBgmPlay(bgm) \
	_C(0x37, 0x04, bgm)
#define pBgmStop(time) \
	_C(0x38, 0x04, (time)-2)
#define pObj(obj) \
	_C(0x39, 0x08, 0); \
	_P(obj)
/* 0x3A wind */
#define pJet(index, mode, px, py, pz, arg) \
	_B(0x3B, 0x0C, index, mode); \
	_H(px, py); \
	_H(pz, arg)
#define pStore(var) \
	_B(0x3C, 0x04, 0, P_VAR_##var)
#define pLoad(var) \
	_B(0x3C, 0x04, 1, P_VAR_##var)

#endif /* __SM64_P_SCRIPT_H__ */
