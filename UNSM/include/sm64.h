#include <ultra64.h>
#ifdef sgi
#include <bstring.h>
#endif
#include <string.h>

#include <sm64/types.h>
#include <sm64/gbiext.h>
#include <sm64/segment.h>

#include <sm64/defmath.h>
#include <sm64/defaudio.h>
#include <sm64/defshape.h>
#include <sm64/defobject.h>
#include <sm64/defmap.h>
#include <sm64/defwipe.h>
#include <sm64/defshadow.h>
#include <sm64/defbackground.h>
#include <sm64/defwave.h>
#include <sm64/defchar.h>
#include <sm64/defmessage.h>
#include <sm64/defweather.h>
#include <sm64/defmapobj.h>
#include <sm64/deftag.h>
#include <sm64/defscene.h>
#include <sm64/defplayer.h>
#include <sm64/defanime.h>
#include <sm64/defgame.h>
#include <sm64/defstage.h>
#include <sm64/defcourse.h>
#include <sm64/defbackup.h>
#include <sm64/defshplang.h>
#include <sm64/defseqlang.h>
#include <sm64/defobjlang.h>

extern char __dummy0[];
extern char __dummy1[];
extern char __dummy2[];
extern char __dummy3[];
extern char __dummy4[];
extern char __dummy5[];
extern char __dummy6[];
extern char __dummy7[];
extern char __dummy8[];
extern char __dummy9[];
extern char __dummy10[];
extern char __dummy11[];
extern char __dummy12[];
extern char __dummy13[];
extern char __dummy14[];
extern char __dummy15[];
extern char __dummy16[];
extern char __dummy17[];
extern char __dummy18[];
extern char __dummy19[];
extern char __dummy20[];
extern char __dummy21[];
extern char __dummy22[];
extern char __dummy23[];
extern char __dummy24[];
extern char __dummy25[];
extern char __dummy26[];
extern char __dummy27[];
extern char __dummy28[];
extern char __dummy29[];
extern char __dummy30[];
extern char __dummy31[];
extern char __dummy32[];
extern char __dummy33[];
extern char __dummy34[];
extern char __dummy35[];
extern char __dummy36[];
extern char __dummy37[];
extern char __dummy38[];
extern char __dummy39[];
extern char __dummy40[];
extern char __dummy41[];
extern char __dummy42[];
extern char __dummy43[];
extern char __dummy44[];
extern char __dummy45[];
extern char __dummy46[];
extern char __dummy47[];
extern char __dummy48[];
extern char __dummy49[];
extern char __dummy50[];
extern char __dummy51[];
extern char __dummy52[];
extern char __dummy53[];
extern char __dummy54[];
extern char __dummy55[];
extern char __dummy56[];
extern char __dummy57[];
extern char __dummy58[];
extern char __dummy59[];
extern char __dummy60[];
extern char __dummy61[];
extern char __dummy62[];
extern char __dummy63[];
extern char __dummy64[];
extern char __dummy65[];
extern char __dummy66[];
extern char __dummy67[];
extern char __dummy68[];
extern char __dummy69[];
extern char __dummy70[];
extern char __dummy71[];
extern char __dummy72[];
extern char __dummy73[];
extern char __dummy74[];
extern char __dummy75[];
extern char __dummy76[];
extern char __dummy77[];
extern char __dummy78[];
extern char __dummy79[];
extern char __dummy80[];
extern char __dummy81[];
extern char __dummy82[];
extern char __dummy83[];
extern char __dummy84[];
extern char __dummy85[];
extern char __dummy86[];
extern char __dummy87[];
extern char __dummy88[];
extern char __dummy89[];
extern char __dummy90[];
extern char __dummy91[];
extern char __dummy92[];
extern char __dummy93[];
extern char __dummy94[];
extern char __dummy95[];
extern char __dummy96[];
extern char __dummy97[];
extern char __dummy98[];
extern char __dummy99[];

#include <sm64/math.h>
#include <sm64/memory.h>
#include <sm64/disk.h>

#include <sm64/main.h>
#include <sm64/graphics.h>
#include <sm64/Na.h>
#include <sm64/audio.h>
#include <sm64/motor.h>
#include <sm64/time.h>

#include <sm64/shape.h>
#include <sm64/draw.h>
#include <sm64/script.h>
#include <sm64/object.h>
#include <sm64/map.h>

#include <sm64/objectlib.h>
#include <sm64/debug.h>
#include <sm64/wipe.h>
#include <sm64/shadow.h>
#include <sm64/background.h>
#include <sm64/water.h>
#include <sm64/objshape.h>
#include <sm64/wave.h>
#include <sm64/dprint.h>
#include <sm64/message.h>
#include <sm64/tag.h>
#include <sm64/hud.h>

#include <sm64/camera.h>
#include <sm64/scene.h>
#include <sm64/player.h>
#include <sm64/game.h>
#include <sm64/course.h>
#include <sm64/backup.h>

extern char __dummy100[];
extern char __dummy101[];
extern char __dummy102[];
extern char __dummy103[];
extern char __dummy104[];
extern char __dummy105[];
extern char __dummy106[];
extern char __dummy107[];
extern char __dummy108[];
extern char __dummy109[];
extern char __dummy110[];
extern char __dummy111[];
extern char __dummy112[];
extern char __dummy113[];
extern char __dummy114[];
extern char __dummy115[];
extern char __dummy116[];
extern char __dummy117[];
extern char __dummy118[];
extern char __dummy119[];
extern char __dummy120[];
extern char __dummy121[];
extern char __dummy122[];
extern char __dummy123[];
extern char __dummy124[];
extern char __dummy125[];
extern char __dummy126[];
extern char __dummy127[];
extern char __dummy128[];
extern char __dummy129[];
extern char __dummy130[];
extern char __dummy131[];
extern char __dummy132[];
extern char __dummy133[];
extern char __dummy134[];
extern char __dummy135[];
extern char __dummy136[];
extern char __dummy137[];
extern char __dummy138[];
extern char __dummy139[];
extern char __dummy140[];
extern char __dummy141[];
extern char __dummy142[];
extern char __dummy143[];
extern char __dummy144[];
extern char __dummy145[];
extern char __dummy146[];
extern char __dummy147[];
extern char __dummy148[];
extern char __dummy149[];

#include <sm64/buffer.h>

#include <sm64/enemya.h>
#include <sm64/enemyb.h>
#include <sm64/enemyc.h>

#include <sm64/weather.h>

#include <sm64/face.h>
