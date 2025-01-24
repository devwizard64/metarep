#ifndef __SM64_PRGLANG_H__
#define __SM64_PRGLANG_H__

#include <sm64/segment.h>
#include <sm64/defaudio.h>
#include <sm64/defshape.h>
#include <sm64/defwipe.h>
#include <sm64/defscene.h>
#include <sm64/defgame.h>
#include <sm64/defstage.h>
#include <sm64/defprglang.h>
#include <sm64/script_s.h>

#define FALSE   0
#define TRUE    1

#define pExecute(seg, start, end, script) \
	_C(PRG_CMD_EXECUTE, 4*4, seg); \
	_P(start); \
	_P(end); \
	_P(script)
#define pChain(seg, start, end, script) \
	_C(PRG_CMD_CHAIN, 4*4, seg); \
	_P(start); \
	_P(end); \
	_P(script)
#define pExit() \
	_C(PRG_CMD_EXIT, 4*1, 0)
#define pSleep(x) \
	_C(PRG_CMD_SLEEP, 4*1, x)
#define pFreeze(x) \
	_C(PRG_CMD_FREEZE, 4*1, x)
#define pJump(script) \
	_C(PRG_CMD_JUMP, 4*2, 0); \
	_P(script)
#define pCall(script) \
	_C(PRG_CMD_CALL, 4*2, 0); \
	_P(script)
#define pReturn() \
	_C(PRG_CMD_RETURN, 4*1, 0)
#define pFor(count) \
	_C(PRG_CMD_FOR, 4*1, count)
#define pDone() \
	_C(PRG_CMD_DONE, 4*1, 0)
#define pRepeat() \
	_C(PRG_CMD_REPEAT, 4*1, 0)
#define pUntil(cmp, val) \
	_B(PRG_CMD_UNTIL, 4*2, PRG_CMP_##cmp, 0); \
	_W(val);
#define pJumpIf(cmp, val, script) \
	_B(PRG_CMD_JUMPIF, 4*3, PRG_CMP_##cmp, 0); \
	_W(val); \
	_P(script)
#define pCallIf(cmp, val, script) \
	_B(PRG_CMD_CALLIF, 4*3, PRG_CMP_##cmp, 0); \
	_W(val); \
	_P(script)
#define pIf(cmp, val) \
	_B(PRG_CMD_IF, 4*3, PRG_CMP_##cmp, 0); \
	_W(val)
#define pElse() \
	_C(PRG_CMD_ELSE, 4*1, 0)
#define pEndif() \
	_C(PRG_CMD_ENDIF, 4*1, 0)
#define pCallback(callback, arg) \
	_C(PRG_CMD_CALLBACK, 4*2, arg); \
	_P(callback)
#define pProcess(callback, arg) \
	_C(PRG_CMD_PROCESS, 4*2, arg); \
	_P(callback)
#define pSet(val) \
	_C(PRG_CMD_SET, 4*1, val)
#define pPush() \
	_C(PRG_CMD_PUSH, 4*1, 0)
#define pPull() \
	_C(PRG_CMD_PULL, 4*1, 0)
#define pLoadCode(addr, start, end) \
	_C(PRG_CMD_LOADCODE, 4*4, 0); \
	_P(addr); \
	_P(start); \
	_P(end)
#define pLoadData(seg, start, end) \
	_C(PRG_CMD_LOADDATA, 4*3, seg); \
	_P(start); \
	_P(end)
#define pLoadPres(seg, start, end) \
	_C(PRG_CMD_LOADPRES, 4*3, seg); \
	_P(start); \
	_P(end)
#define pLoadFace(arg) \
	_C(PRG_CMD_LOADFACE, 4*1, arg)
#define pLoadText(seg, start, end) \
	_C(PRG_CMD_LOADTEXT, 4*3, seg); \
	_P(start); \
	_P(end)
#define pStageInit() \
	_C(PRG_CMD_STAGEINIT, 4*1, 0)
#define pStageExit() \
	_C(PRG_CMD_STAGEEXIT, 4*1, 0)
#define pStageStart() \
	_C(PRG_CMD_STAGESTART, 4*1, 0)
#define pStageEnd() \
	_C(PRG_CMD_STAGEEND, 4*1, 0)
#define pSceneStart(scene, script) \
	_B(PRG_CMD_SCENESTART, 4*2, scene, 0); \
	_P(script)
#define pSceneEnd() \
	_C(PRG_CMD_SCENEEND, 4*1, 0)
#define pShapeGfx(shape, gfx, layer) \
	_C(PRG_CMD_SHAPEGFX, 4*2, layer << 12 | (shape)); \
	_P(gfx)
#define pShape(shape, script) \
	_C(PRG_CMD_SHAPE, 4*2, shape); \
	_P(script)
#define pShapeScale(shape, gfx, layer, scale) \
	_C(PRG_CMD_SHAPESCALE, 4*3, layer << 12 | (shape)); \
	_P(gfx); \
	_F(scale)
#define pObj( \
	mask, shape, posx, posy, posz, angx, angy, angz, \
	a0, a1, flag, script \
) \
	_B(PRG_CMD_OBJECT, 4*6, mask, shape); \
	_H(posx, posy); \
	_H(posz, angx); \
	_H(angy, angz); \
	_C(a0, a1, flag); \
	_P(script)
#define pObject( \
	shape, posx, posy, posz, angx, angy, angz, \
	a0, a1, flag, script \
) \
	pObj(037, shape, posx, posy, posz, angx, angy, angz, a0, a1, flag, script)
#define pPlayer(shape, arg0, arg1, flag, script) \
	_B(PRG_CMD_PLAYER, 4*3, 0, shape); \
	_C(arg0, arg1, flag); \
	_P(script)
#define pMario() \
	pPlayer(S_MARIO, 0, 0, 1, o_mario)
#define pPort(index, stage, scene, port) \
	_B(PRG_CMD_PORT, 4*2, index, stage); \
	_B(scene, port, 0x00, 0)
#define pPortMid(index, stage, scene, port) \
	_B(PRG_CMD_PORT, 4*2, index, stage); \
	_B(scene, port, 0x80, 0)
#define pBGPort(index, stage, scene, port) \
	_B(PRG_CMD_BGPORT, 4*2, index, stage); \
	_B(scene, port, 0x00, 0)
#define pBGPortMid(index, stage, scene, port) \
	_B(PRG_CMD_BGPORT, 4*2, index, stage); \
	_B(scene, port, 0x80, 0)
#define pConnect(index, scene, offx, offy, offz) \
	_B(PRG_CMD_CONNECT, 4*3, index, scene); \
	_H(offx, offy); \
	_H(offz, 0)
#define pSceneOpen(scene) \
	_B(PRG_CMD_SCENEOPEN, 4*1, scene, 0)
#define pSceneClose(scene) \
	_B(PRG_CMD_SCENECLOSE, 4*1, scene, 0)
#define pPlayerOpen(scene, angy, posx, posy, posz) \
	_B(PRG_CMD_PLAYEROPEN, 4*3, scene, 0); \
	_H(angy, posx); \
	_H(posy, posz)
#define pPlayerClose() \
	_C(PRG_CMD_PLAYERCLOSE, 4*1, 0)
#define pSceneProc() \
	_C(PRG_CMD_SCENEPROC, 4*2, 0)
#define pMap(map) \
	_C(PRG_CMD_MAP, 4*2, 0); \
	_P(map)
#define pArea(area) \
	_C(PRG_CMD_AREA, 4*2, 0); \
	_P(area)
#define pMessage(type, msg) \
	_B(PRG_CMD_MESSAGE, 4*1, type, msg)
#define pEnv(env) \
	_C(PRG_CMD_ENV, 4*1, env)
/* 50 */
#define pWipe(type, time, r, g, b) \
	_B(PRG_CMD_WIPE, 4*2, type, time); \
	_B(r, g, b, 0)
#define pViBlack(arg) \
	_B(PRG_CMD_VIBLACK, 4*1, arg, 0)
#define pViGamma(arg) \
	_B(PRG_CMD_VIGAMMA, 4*1, arg, 0)
#define pBGM(mode, bgm) \
	_C(PRG_CMD_BGM, 4*2, mode); \
	_H(bgm, 0)
#define pPlayBGM(bgm) \
	_C(PRG_CMD_PLAYBGM, 4*1, bgm)
#define pAudFadeout(fadeout) \
	_C(PRG_CMD_AUDFADEOUT, 4*1, fadeout)
#define pTag(tag) \
	_C(PRG_CMD_TAG, 4*2, 0); \
	_P(tag)
#define p58(a, b, c, d, e) \
	_C(PRG_CMD_58, 4*3, a); \
	_H(b, c); \
	_H(d, e)
#define pJet(index, mode, posx, posy, posz, arg) \
	_B(PRG_CMD_JET, 4*3, index, mode); \
	_H(posx, posy); \
	_H(posz, arg)
#define pStore(var) \
	_B(PRG_CMD_VAR, 4*1, 0, PRG_VAR_##var)
#define pLoad(var) \
	_B(PRG_CMD_VAR, 4*1, 1, PRG_VAR_##var)

#endif /* __SM64_PRGLANG_H__ */
