#include <sm64/types.h>
#include <sm64/game.h>
#include <sm64/object.h>
#include <sm64/obj_lib.h>
#include <sm64/obj_physics.h>
#include <sm64/math.h>
#include <sm64/map.h>

s16 obj_physics_80330E20 = 0;
u32 obj_physics_80330E24[4] = {0};
OBJECT *obj_ground = NULL;

void obj_physics_802C89F0(void)
{
    MAP_PLANE *ground;
    UNUSED OBJECT *obj;
    float x;
    float y;
    float z;
    float ground_y;
    int code;
    if (obj_mario == NULL) return;
    x = obj_mario->o_pos_x;
    y = obj_mario->o_pos_y;
    z = obj_mario->o_pos_z;
    ground_y = map_80381900(x, y, z, &ground);
    if (obj_lib_802A3634(y - ground_y) < 4) code = 0;
    else                                    code = 1;
    switch (code)
    {
        case 1:
            obj_ground = NULL;
            obj_mario->obj_ground = NULL;
            break;
        case 0:
            if (ground != NULL && ground->obj != NULL)
            {
                obj_ground = ground->obj;
                obj_mario->obj_ground = ground->obj;
            }
            else
            {
                obj_ground = NULL;
                obj_mario->obj_ground = NULL;
            }
            break;
    }
}

void mario_pos_get(float *x, float *y, float *z)
{
    *x = player_data[0].pos[0];
    *y = player_data[0].pos[1];
    *z = player_data[0].pos[2];
}

void mario_pos_set(float x, float y, float z)
{
    player_data[0].pos[0] = x;
    player_data[0].pos[1] = y;
    player_data[0].pos[2] = z;
}

void obj_physics_802C8BC8(int ismario, OBJECT *obj)
{
    float px;
    float py;
    float pz;
    float gx;
    float gy;
    float gz;
    VECF pos;
    VECF off;
    VECF new;
    VECS ang;
    ang[0] = obj->o_ang_vel_x;
    ang[1] = obj->o_ang_vel_y;
    ang[2] = obj->o_ang_vel_z;
    if (ismario)
    {
        obj_physics_80330E20 = 0;
        mario_pos_get(&px, &py, &pz);
    }
    else
    {
        px = object->o_pos_x;
        py = object->o_pos_y;
        pz = object->o_pos_z;
    }
    px += obj->o_vel_x;
    pz += obj->o_vel_z;
    if (ang[0] != 0 || ang[1] != 0 || ang[2] != 0)
    {
        UNUSED SHORT ax = ang[0];
        UNUSED SHORT az = ang[2];
        UNUSED SHORT ay = obj->o_shape_ang_y;
        MTXF mf;
        if (ismario) player_data[0].ang[1] += ang[1];
        gx = obj->o_pos_x;
        gy = obj->o_pos_y;
        gz = obj->o_pos_z;
        pos[0] = px - gx;
        pos[1] = py - gy;
        pos[2] = pz - gz;
        ang[0] = obj->o_shape_ang_x - obj->o_ang_vel_x;
        ang[1] = obj->o_shape_ang_y - obj->o_ang_vel_y;
        ang[2] = obj->o_shape_ang_z - obj->o_ang_vel_z;
        mtxf_posang(mf, pos, ang);
        obj_lib_8029F274(mf, off, pos);
        ang[0] = obj->o_shape_ang_x;
        ang[1] = obj->o_shape_ang_y;
        ang[2] = obj->o_shape_ang_z;
        mtxf_posang(mf, pos, ang);
        obj_lib_8029F200(mf, new, off);
        px = new[0] + gx;
        py = new[1] + gy;
        pz = new[2] + gz;
    }
    if (ismario)
    {
        mario_pos_set(px, py, pz);
    }
    else
    {
        object->o_pos_x = px;
        object->o_pos_y = py;
        object->o_pos_z = pz;
    }
}

void obj_physics_802C8EC0(void)
{
    OBJECT *obj = obj_ground;
    if (!(object_8033D480 & 0x40))
    {
        if (obj_mario != NULL && obj != NULL) obj_physics_802C8BC8(TRUE, obj);
    }
}

void obj_physics_802C8F28(void)
{
    obj_ground = NULL;
}
