#include <sm64/types.h>
#include <sm64/object.h>
#include <sm64/obj_lib.h>
#include <sm64/obj_sfx.h>
#include <sm64/o_script.h>
#include <sm64/audio/g.h>

void obj_sfx_802CA040(OBJ_SFX *sfx)
{
    int i = object->o_anime_index;
    switch (sfx[i].flag)
    {
        case 0:
            break;
        case 1:
        {
            int frame;
            if ((frame = sfx[i].l) >= 0)
            {
                if (obj_lib_802A0008(frame)) obj_sfx_802CA1E0(sfx[i].se);
            }
            if ((frame = sfx[i].r) >= 0)
            {
                if (obj_lib_802A0008(frame)) obj_sfx_802CA1E0(sfx[i].se);
            }
            break;
        }
    }
}

extern O_SCRIPT o_1300229C[];

void obj_sfx_802CA144(NA_SE se)
{
    OBJECT *obj = obj_lib_8029EDCC(object, 0, o_1300229C);
    obj->mem[O_MEM_V0].s32 = se;
}

void obj_sfx_802CA190(NA_SE se)
{
    if (object->list.s.s.flag & 1) Na_SE_obj(se, object);
}

void obj_sfx_802CA1E0(NA_SE se)
{
    if (object->list.s.s.flag & 1) Na_SE_obj(se, object);
}

UNUSED static int obj_sfx_802CA230(float x)
{
    int y;
    if      (x <  500) y = 127;
    else if (x > 1500) y = 0;
    else               y = (x-500)/1000*64 + 60;
    return y;
}

UNUSED static int obj_sfx_802CA2D4(float x)
{
    int y;
    if      (x < 1300) y = 127;
    else if (x > 2300) y = 0;
    else               y = (x-1000)/1000*64 + 60;
    return y;
}
