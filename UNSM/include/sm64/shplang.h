#ifndef __SM64_SHPLANG_H__
#define __SM64_SHPLANG_H__

#include <ultra64.h>
#include <sm64/types.h>
#include <sm64/defshape.h>
#include <sm64/defback.h>
#include <sm64/defweather.h>
#include <sm64/script_c.h>

#define sExecute(script) \
	_C(0x00, 0, 0), \
	_P(script)
#define sExit() \
	_C(0x01, 0, 0)
#define sJump(script) \
	_C(0x02, 0, 0), \
	_P(script)
#define sCall(script) \
	_C(0x02, 1, 0), \
	_P(script)
#define sReturn() \
	_C(0x03, 0, 0)
#define sStart() \
	_C(0x04, 0, 0)
#define sEnd() \
	_C(0x05, 0, 0)
#define sStore(index) \
	_C(0x06, 0, index)
#define sFlag(flag) \
	_C(0x07, 0, flag)
#define sSetFlag(flag) \
	_C(0x07, 1, flag)
#define sClrFlag(flag) \
	_C(0x07, 2, flag)
#define sScene(x, y, w, h, n) \
	_C(0x08, 0, n), \
	_H(x, y), \
	_H(w, h)
#define sOrtho(scale) \
	_C(0x09, 0, scale)
#define sPersp(fovy, n, f) \
	_C(0x0A, 0, fovy), \
	_H(n, f)
#define sPerspective(fovy, n, f, callback) \
	_C(0x0A, 1, fovy), \
	_H(n, f), \
	_P(callback)
#define sEmpty() \
	_C(0x0B, 0, 0)
#define sLayer(depth) \
	_C(0x0C, depth, 0)
#define sLOD(min, max) \
	_C(0x0D, 0, 0), \
	_H(min, max)
#define sSelect(arg, callback) \
	_C(0x0E, 0, arg), \
	_P(callback)
#define sCamera(arg, px, py, pz, lx, ly, lz, callback) \
	_C(0x0F, 0, arg), \
	_H(px, py), \
	_H(pz, lx), \
	_H(ly, lz), \
	_P(callback)
#define sCoord(px, py, pz, ax, ay, az) \
	_C(0x10, 0x00, 0), \
	_H(px, py), \
	_H(pz, ax), \
	_H(ay, az)
#define sCoordPos(px, py, pz) \
	_C(0x10, 0x10, px), \
	_H(py, pz)
#define sCoordAng(ax, ay, az) \
	_C(0x10, 0x20, ax), \
	_H(ay, az)
#define sCoordAY(ay) \
	_C(0x10, 0x30, ay)
#define sGfxCoord(layer, gfx, px, py, pz, ax, ay, az) \
	_C(0x10, 0x80 | layer, 0), \
	_H(px, py), \
	_H(pz, ax), \
	_H(ay, az), \
	_P(gfx)
#define sGfxCoordPos(layer, gfx, px, py, pz) \
	_C(0x10, 0x90 | layer, px), \
	_H(py, pz)
#define sGfxCoordAng(layer, gfx, ax, ay, az) \
	_C(0x10, 0xA0 | layer, ax), \
	_H(ay, az), \
	_P(gfx)
#define sGfxCoordAY(layer, gfx, ay) \
	_C(0x10, 0xB0 | layer, ay), \
	_P(gfx)
#define sPos(px, py, pz) \
	_C(0x11, 0x00, px), \
	_H(py, pz)
#define sGfxPos(layer, gfx, px, py, pz) \
	_C(0x11, 0x80 | layer, px), \
	_H(py, pz), \
	_P(gfx)
#define sAng(ax, ay, az) \
	_C(0x12, 0x00, ax), \
	_H(ay, az)
#define sGfxAng(layer, gfx, ax, ay, az) \
	_C(0x11, 0x80 | layer, ax), \
	_H(ay, az), \
	_P(gfx)
#define sJoint(layer, gfx, px, py, pz) \
	_C(0x13, layer, px), \
	_H(py, pz), \
	_P(gfx)
#define sBillboard(px, py, pz) \
	_C(0x14, 0x00, px), \
	_H(py, pz)
#define sGfxBillboard(layer, gfx, px, py, pz) \
	_C(0x14, 0x80 | layer, px), \
	_H(py, pz), \
	_P(gfx)
#define sGfx(layer, gfx) \
	_C(0x15, layer, 0), \
	_P(gfx)
#define sShadow(size, alpha, type) \
	_C(0x16, 0, type), \
	_H(alpha, size)
#define sObject() \
	_C(0x17, 0, 0)
#define sCallback(arg, callback) \
	_C(0x18, 0, arg), \
	_P(callback)
#define sBackground(arg, callback) \
	_C(0x19, 0, arg), \
	_P(callback)
/* 0x1A */
#define sLoad(index) \
	_C(0x1B, 0, index)
#define sHand(px, py, pz, arg, callback) \
	_C(0x1C, arg, px), \
	_H(py, pz), \
	_P(callback)
#define sScale(scale) \
	_C(0x1D, 0x00, 0), \
	_F(scale)
#define sGfxScale(layer, gfx, scale) \
	_C(0x1D, 0x80 | layer, 0), \
	_F(scale), \
	_P(gfx)
/* 0x1E */
/* 0x1F */
#define sCull(dist) \
	_C(0x20, 0, dist)

typedef struct shape SHAPE;

extern void *s_pl_demo_80257198(int, SHAPE *, void *); /* select */

extern void *s_stage_weather(int, SHAPE *, void *);
extern void *s_stage_back(int, SHAPE *, void *);
extern void *s_face_main(int, SHAPE *, void *);
extern void *s_player_alpha(int, SHAPE *, void *);
extern void *s_player_select_lod(int, SHAPE *, void *);
extern void *s_player_select_eyes(int, SHAPE *, void *);
extern void *s_player_ang_torso(int, SHAPE *, void *);
extern void *s_player_ang_neck(int, SHAPE *, void *);
extern void *s_mario_select_glove(int, SHAPE *, void *);
extern void *s_mario_punch(int, SHAPE *, void *);
extern void *s_player_select_cap(int, SHAPE *, void *);
extern void *s_player_select_head(int, SHAPE *, void *);
extern void *s_player_ang_wing(int, SHAPE *, void *);
extern void *s_player_hand(int, SHAPE *, void *);
extern void *s_inside_mirror(int, SHAPE *, void *);
extern void *s_player_mirror(int, SHAPE *, void *);

extern void *s_stage_camera(int, SHAPE *, void *);
extern void *s_stage_perspective(int, SHAPE *, void *);

extern void *s_objlib_8029D890(int, SHAPE *, void *); /* callback */
extern void *s_objlib_8029D924(int, SHAPE *, void *); /* callback */
extern void *s_objlib_8029DB48(int, SHAPE *, void *); /* select */
extern void *s_objlib_8029DBD4(int, SHAPE *, void *); /* select */
extern void *s_objlib_802A45E4(int, SHAPE *, void *); /* callback */

extern void *s_object_a_802A719C(int, SHAPE *, void *); /* callback */
extern void *s_mario_pos_child(int, SHAPE *, void *);
extern void *s_object_a_802B798C(int, SHAPE *, void *); /* callback */
extern void *s_object_a_802B7C64(int, SHAPE *, void *); /* select */
extern void *s_object_a_802B7D44(int, SHAPE *, void *); /* callback */
extern void *s_object_a_802BA2B0(int, SHAPE *, void *); /* callback */
extern void *s_object_a_802BFBAC(int, SHAPE *, void *); /* select */

extern void *s_wipe_802CD1E8(int, SHAPE *, void *); /* callback */

extern void *s_scroll_802D0080(int, SHAPE *, void *); /* callback */
extern void *s_scroll_802D01E0(int, SHAPE *, void *); /* callback */
extern void *s_scroll_802D104C(int, SHAPE *, void *); /* callback */
extern void *s_scroll_802D1B70(int, SHAPE *, void *); /* callback */
extern void *s_scroll_802D1CDC(int, SHAPE *, void *); /* callback */
extern void *s_scroll_802D1E48(int, SHAPE *, void *); /* callback */
extern void *s_scroll_802D1FA8(int, SHAPE *, void *); /* callback */
extern void *s_scroll_802D2108(int, SHAPE *, void *); /* callback */

extern void *s_obj_shape_802D2360(int, SHAPE *, void *); /* callback */
extern void *s_obj_shape_802D2470(int, SHAPE *, void *); /* callback */
extern void *s_obj_shape_802D2520(int, SHAPE *, void *); /* callback */
extern void *s_obj_shape_802D28CC(int, SHAPE *, void *); /* callback */

extern void *s_wave_802D5B98(int, SHAPE *, void *); /* callback */
extern void *s_wave_802D5D0C(int, SHAPE *, void *); /* callback */

extern void *s_object_c_8030D93C(int, SHAPE *, void *); /* callback */
extern void *s_object_c_8030D9AC(int, SHAPE *, void *); /* callback */

extern void *s_title_logo(int, SHAPE *, void *);
extern void *s_title_symbol(int, SHAPE *, void *);
extern void *s_title_back(int, SHAPE *, void *);
extern void *s_gameover_back(int, SHAPE *, void *);

extern void *s_fileselect_main(int, SHAPE *, void *);

extern void *s_starselect_main(int, SHAPE *, void *);

#endif /* __SM64_SHPLANG_H__ */
