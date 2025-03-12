#ifndef __SM64_SEQLANG_H__
#define __SM64_SEQLANG_H__

#include <sm64/segment.h>
#include <sm64/defaudio.h>
#include <sm64/defshape.h>
#include <sm64/defobject.h>
#include <sm64/defwipe.h>
#include <sm64/defscene.h>
#include <sm64/defgame.h>
#include <sm64/defstage.h>
#include <sm64/defseqlang.h>
#include <sm64/scriptasm.h>

#define FALSE   0
#define TRUE    1

#define seqExecute(seg, start, end, script) \
	_C(SEQ_CMD_EXECUTE, 4*4, seg); \
	_P(start); \
	_P(end); \
	_P(script)
#define seqChain(seg, start, end, script) \
	_C(SEQ_CMD_CHAIN, 4*4, seg); \
	_P(start); \
	_P(end); \
	_P(script)
#define seqExit() \
	_C(SEQ_CMD_EXIT, 4*1, 0)
#define seqSleep(x) \
	_C(SEQ_CMD_SLEEP, 4*1, x)
#define seqFreeze(x) \
	_C(SEQ_CMD_FREEZE, 4*1, x)
#define seqJump(script) \
	_C(SEQ_CMD_JUMP, 4*2, 0); \
	_P(script)
#define seqCall(script) \
	_C(SEQ_CMD_CALL, 4*2, 0); \
	_P(script)
#define seqReturn() \
	_C(SEQ_CMD_RETURN, 4*1, 0)
#define seqFor(count) \
	_C(SEQ_CMD_FOR, 4*1, count)
#define seqDone() \
	_C(SEQ_CMD_DONE, 4*1, 0)
#define seqRepeat() \
	_C(SEQ_CMD_REPEAT, 4*1, 0)
#define seqUntil(cmp, val) \
	_B(SEQ_CMD_UNTIL, 4*2, SEQ_CMP_##cmp, 0); \
	_W(val);
#define seqJumpIf(cmp, val, script) \
	_B(SEQ_CMD_JUMPIF, 4*3, SEQ_CMP_##cmp, 0); \
	_W(val); \
	_P(script)
#define seqCallIf(cmp, val, script) \
	_B(SEQ_CMD_CALLIF, 4*3, SEQ_CMP_##cmp, 0); \
	_W(val); \
	_P(script)
#define seqIf(cmp, val) \
	_B(SEQ_CMD_IF, 4*3, SEQ_CMP_##cmp, 0); \
	_W(val)
#define seqElse() \
	_C(SEQ_CMD_ELSE, 4*1, 0)
#define seqEndif() \
	_C(SEQ_CMD_ENDIF, 4*1, 0)
#define seqCallback(callback, arg) \
	_C(SEQ_CMD_CALLBACK, 4*2, arg); \
	_P(callback)
#define seqProcess(callback, arg) \
	_C(SEQ_CMD_PROCESS, 4*2, arg); \
	_P(callback)
#define seqSet(val) \
	_C(SEQ_CMD_SET, 4*1, val)
#define seqPush() \
	_C(SEQ_CMD_PUSH, 4*1, 0)
#define seqPull() \
	_C(SEQ_CMD_PULL, 4*1, 0)
#define seqLoadCode(addr, start, end) \
	_C(SEQ_CMD_LOADCODE, 4*4, 0); \
	_P(addr); \
	_P(start); \
	_P(end)
#define seqLoadData(seg, start, end) \
	_C(SEQ_CMD_LOADDATA, 4*3, seg); \
	_P(start); \
	_P(end)
#define seqLoadPres(seg, start, end) \
	_C(SEQ_CMD_LOADPRES, 4*3, seg); \
	_P(start); \
	_P(end)
#define seqLoadFace(arg) \
	_C(SEQ_CMD_LOADFACE, 4*1, arg)
#define seqLoadText(seg, start, end) \
	_C(SEQ_CMD_LOADTEXT, 4*3, seg); \
	_P(start); \
	_P(end)
#define seqStageInit() \
	_C(SEQ_CMD_STAGEINIT, 4*1, 0)
#define seqStageExit() \
	_C(SEQ_CMD_STAGEEXIT, 4*1, 0)
#define seqCompileBegin() \
	_C(SEQ_CMD_COMPILEBEGIN, 4*1, 0)
#define seqCompileEnd() \
	_C(SEQ_CMD_COMPILEEND, 4*1, 0)
#define seqSceneBegin(scene, script) \
	_B(SEQ_CMD_SCENEBEGIN, 4*2, scene, 0); \
	_P(script)
#define seqSceneEnd() \
	_C(SEQ_CMD_SCENEEND, 4*1, 0)
#define seqShapeGfx(shape, gfx, layer) \
	_C(SEQ_CMD_SHAPEGFX, 4*2, layer << 12 | (shape)); \
	_P(gfx)
#define seqShape(shape, script) \
	_C(SEQ_CMD_SHAPE, 4*2, shape); \
	_P(script)
#define seqShapeScale(shape, gfx, layer, scale) \
	_C(SEQ_CMD_SHAPESCALE, 4*3, layer << 12 | (shape)); \
	_P(gfx); \
	_F(scale)
#define seqObj( \
	mask, shape, posx, posy, posz, angx, angy, angz, \
	a0, a1, flag, script \
) \
	_B(SEQ_CMD_OBJECT, 4*6, mask, shape); \
	_H(posx, posy); \
	_H(posz, angx); \
	_H(angy, angz); \
	_C(a0, a1, flag); \
	_P(script)
#define seqObject( \
	shape, posx, posy, posz, angx, angy, angz, \
	a0, a1, flag, script \
) \
	seqObj(037, shape, posx, posy, posz, angx, angy, angz, a0, a1, flag, script)
#define seqPlayer(shape, arg0, arg1, flag, script) \
	_B(SEQ_CMD_PLAYER, 4*3, 0, shape); \
	_C(arg0, arg1, flag); \
	_P(script)
#define seqMario() \
	seqPlayer(S_MARIO, 0, 0, ACTOR_MARIO, obj_mario)
#define seqPort(index, stage, scene, port) \
	_B(SEQ_CMD_PORT, 4*2, index, stage); \
	_B(scene, port, 0x00, 0)
#define seqPortMid(index, stage, scene, port) \
	_B(SEQ_CMD_PORT, 4*2, index, stage); \
	_B(scene, port, 0x80, 0)
#define seqBGPort(index, stage, scene, port) \
	_B(SEQ_CMD_BGPORT, 4*2, index, stage); \
	_B(scene, port, 0x00, 0)
#define seqBGPortMid(index, stage, scene, port) \
	_B(SEQ_CMD_BGPORT, 4*2, index, stage); \
	_B(scene, port, 0x80, 0)
#define seqConnect(index, scene, offx, offy, offz) \
	_B(SEQ_CMD_CONNECT, 4*3, index, scene); \
	_H(offx, offy); \
	_H(offz, 0)
#define seqSceneOpen(scene) \
	_B(SEQ_CMD_SCENEOPEN, 4*1, scene, 0)
#define seqSceneClose(scene) \
	_B(SEQ_CMD_SCENECLOSE, 4*1, scene, 0)
#define seqPlayerOpen(scene, angy, posx, posy, posz) \
	_B(SEQ_CMD_PLAYEROPEN, 4*3, scene, 0); \
	_H(angy, posx); \
	_H(posy, posz)
#define seqPlayerClose() \
	_C(SEQ_CMD_PLAYERCLOSE, 4*1, 0)
#define seqSceneProc() \
	_C(SEQ_CMD_SCENEPROC, 4*2, 0)
#define seqMap(map) \
	_C(SEQ_CMD_MAP, 4*2, 0); \
	_P(map)
#define seqArea(area) \
	_C(SEQ_CMD_AREA, 4*2, 0); \
	_P(area)
#define seqMessage(type, msg) \
	_B(SEQ_CMD_MESSAGE, 4*1, type, msg)
#define seqEnv(env) \
	_C(SEQ_CMD_ENV, 4*1, env)
/* 50 */
#define seqWipe(type, time, r, g, b) \
	_B(SEQ_CMD_WIPE, 4*2, type, time); \
	_B(r, g, b, 0)
#define seqViBlack(arg) \
	_B(SEQ_CMD_VIBLACK, 4*1, arg, 0)
#define seqViGamma(arg) \
	_B(SEQ_CMD_VIGAMMA, 4*1, arg, 0)
#define seqBGM(mode, bgm) \
	_C(SEQ_CMD_BGM, 4*2, mode); \
	_H(bgm, 0)
#define seqPlayBGM(bgm) \
	_C(SEQ_CMD_PLAYBGM, 4*1, bgm)
#define seqAudFadeout(fadeout) \
	_C(SEQ_CMD_AUDFADEOUT, 4*1, fadeout)
#define seqTag(tag) \
	_C(SEQ_CMD_TAG, 4*2, 0); \
	_P(tag)
#define seq58(a, b, c, d, e) \
	_C(SEQ_CMD_58, 4*3, a); \
	_H(b, c); \
	_H(d, e)
#define seqJet(index, mode, posx, posy, posz, arg) \
	_B(SEQ_CMD_JET, 4*3, index, mode); \
	_H(posx, posy); \
	_H(posz, arg)
#define seqStore(var) \
	_B(SEQ_CMD_VAR, 4*1, 0, SEQ_VAR_##var)
#define seqLoad(var) \
	_B(SEQ_CMD_VAR, 4*1, 1, SEQ_VAR_##var)

#endif /* __SM64_SEQLANG_H__ */
