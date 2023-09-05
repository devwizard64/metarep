#include <sm64.h>

Mtx mtx_1 = gdSPDefMatrix(
	1, 0, 0, 0,
	0, 1, 0, 0,
	0, 0, 1, 0,
	0, 0, 0, 1
);
VECF vecf_0 = {0, 0, 0};
VECS vecs_0 = {0, 0, 0};
VECF vecf_1 = {1, 1, 1};
VECS vecs_1 = {1, 1, 1};

float *vecf_cpy(VECF dst, VECF src)
{
	dst[0] = src[0];
	dst[1] = src[1];
	dst[2] = src[2];
#ifdef sgi
	return (float *)&dst;
#else
	return dst;
#endif
}

float *vecf_set(VECF vf, float x, float y, float z)
{
	vf[0] = x;
	vf[1] = y;
	vf[2] = z;
#ifdef sgi
	return (float *)&vf;
#else
	return vf;
#endif
}

float *vecf_add(VECF vf, VECF a)
{
	vf[0] += a[0];
	vf[1] += a[1];
	vf[2] += a[2];
#ifdef sgi
	return (float *)&vf;
#else
	return vf;
#endif
}

float *vecf_addto(VECF vf, VECF a, VECF b)
{
	vf[0] = a[0] + b[0];
	vf[1] = a[1] + b[1];
	vf[2] = a[2] + b[2];
#ifdef sgi
	return (float *)&vf;
#else
	return vf;
#endif
}

short *vecs_cpy(VECS dst, VECS src)
{
	dst[0] = src[0];
	dst[1] = src[1];
	dst[2] = src[2];
#ifdef sgi
	return (short *)&dst;
#else
	return dst;
#endif
}

short *vecs_set(VECS vs, SHORT x, SHORT y, SHORT z)
{
	vs[0] = x;
	vs[1] = y;
	vs[2] = z;
#ifdef sgi
	return (short *)&vs;
#else
	return vs;
#endif
}

short *vecs_add(VECS vs, VECS a)
{
	vs[0] += a[0];
	vs[1] += a[1];
	vs[2] += a[2];
#ifdef sgi
	return (short *)&vs;
#else
	return vs;
#endif
}

short *vecs_addto(VECS vs, VECS a, VECS b)
{
	vs[0] = a[0] + b[0];
	vs[1] = a[1] + b[1];
	vs[2] = a[2] + b[2];
#ifdef sgi
	return (short *)&vs;
#else
	return vs;
#endif
}

short *vecs_sub(VECS vs, VECS a)
{
	vs[0] -= a[0];
	vs[1] -= a[1];
	vs[2] -= a[2];
#ifdef sgi
	return (short *)&vs;
#else
	return vs;
#endif
}

float *vecs_to_vecf(VECF dst, VECS src)
{
	dst[0] = src[0];
	dst[1] = src[1];
	dst[2] = src[2];
#ifdef sgi
	return (float *)&dst;
#else
	return dst;
#endif
}

short *vecf_to_vecs(VECS dst, VECF src)
{
	dst[0] = src[0] + (src[0] > 0 ? 0.5F : -0.5F);
	dst[1] = src[1] + (src[1] > 0 ? 0.5F : -0.5F);
	dst[2] = src[2] + (src[2] > 0 ? 0.5F : -0.5F);
#ifdef sgi
	return (short *)&dst;
#else
	return dst;
#endif
}

float *vecf_normal(VECF vf, VECF v0, VECF v1, VECF v2)
{
#define CROSS(x0, y0, x1, y1, x2, y2) \
	(((y1)-(y0))*((x2)-(x1)) - ((y2)-(y1))*((x1)-(x0)))
	vf[0] = CROSS(v0[2], v0[1], v1[2], v1[1], v2[2], v2[1]);
	vf[1] = CROSS(v0[0], v0[2], v1[0], v1[2], v2[0], v2[2]);
	vf[2] = CROSS(v0[1], v0[0], v1[1], v1[0], v2[1], v2[0]);
#undef CROSS
#ifdef sgi
	return (float *)&vf;
#else
	return vf;
#endif
}

float *vecf_cross(VECF vf, VECF a, VECF b)
{
	vf[0] = a[1]*b[2] - b[1]*a[2];
	vf[1] = a[2]*b[0] - b[2]*a[0];
	vf[2] = a[0]*b[1] - b[0]*a[1];
#ifdef sgi
	return (float *)&vf;
#else
	return vf;
#endif
}

float *vecf_normalize(VECF vf)
{
	float d = 1 / sqrtf(vf[0]*vf[0] + vf[1]*vf[1] + vf[2]*vf[2]);
	vf[0] *= d;
	vf[1] *= d;
	vf[2] *= d;
#ifdef sgi
	return (float *)&vf;
#else
	return vf;
#endif
}

void mtxf_cpy(MTXF dst, MTXF src)
{
	register int i;
	register int *d = (int *)dst;
	register int *s = (int *)src;
	for (i = 0; i < 16; i++) *d++ = *s++;
}

void mtxf_identity(MTXF mf)
{
	register int i;
	register float *f;
	for (i = 0, f = &mf[0][1]; i < 14; i++, f++) *f = 0;
	for (i = 0, f = &mf[0][0]; i < 4; i++, f += 5) *f = 1;
}

void mtxf_pos(MTXF mf, VECF pos)
{
	mtxf_identity(mf);
	mf[3][0] = pos[0];
	mf[3][1] = pos[1];
	mf[3][2] = pos[2];
}

void mtxf_lookat(MTXF mf, VECF eye, VECF look, SHORT az)
{
	register float d;
	float dx, dz, xy, yy, zy, xz, yz, zz, xx, yx, zx;
	dx = look[0] - eye[0];
	dz = look[2] - eye[2];
	d = (DOUBLE)-1 / sqrtf(dx*dx + dz*dz);
	dx *= d;
	dz *= d;
	yy = cos(az);
	xy = sin(az) * dz;
	zy = -sin(az) * dx;
	xz = look[0] - eye[0];
	yz = look[1] - eye[1];
	zz = look[2] - eye[2];
	d = (DOUBLE)-1 / sqrtf(xz*xz + yz*yz + zz*zz);
	xz *= d;
	yz *= d;
	zz *= d;
	xx = yy*zz - zy*yz;
	yx = zy*xz - xy*zz;
	zx = xy*yz - yy*xz;
	d = (DOUBLE)1 / sqrtf(xx*xx + yx*yx + zx*zx);
	xx *= d;
	yx *= d;
	zx *= d;
	xy = yz*zx - zz*yx;
	yy = zz*xx - xz*zx;
	zy = xz*yx - yz*xx;
	d = (DOUBLE)1 / sqrtf(xy*xy + yy*yy + zy*zy);
	xy *= d;
	yy *= d;
	zy *= d;
	mf[0][0] = xx;
	mf[1][0] = yx;
	mf[2][0] = zx;
	mf[3][0] = -(eye[0]*xx + eye[1]*yx + eye[2]*zx);
	mf[0][1] = xy;
	mf[1][1] = yy;
	mf[2][1] = zy;
	mf[3][1] = -(eye[0]*xy + eye[1]*yy + eye[2]*zy);
	mf[0][2] = xz;
	mf[1][2] = yz;
	mf[2][2] = zz;
	mf[3][2] = -(eye[0]*xz + eye[1]*yz + eye[2]*zz);
	mf[0][3] = 0;
	mf[1][3] = 0;
	mf[2][3] = 0;
	mf[3][3] = 1;
}

void mtxf_coord(MTXF mf, VECF pos, VECS ang)
{
	register float sx = sin(ang[0]);
	register float cx = cos(ang[0]);
	register float sy = sin(ang[1]);
	register float cy = cos(ang[1]);
	register float sz = sin(ang[2]);
	register float cz = cos(ang[2]);
	mf[0][0] =  cy*cz + sx*sy*sz;
	mf[1][0] = -cy*sz + sx*sy*cz;
	mf[2][0] = cx*sy;
	mf[3][0] = pos[0];
	mf[0][1] = cx*sz;
	mf[1][1] = cx*cz;
	mf[2][1] = -sx;
	mf[3][1] = pos[1];
	mf[0][2] = -sy*cz + sx*cy*sz;
	mf[1][2] =  sy*sz + sx*cy*cz;
	mf[2][2] = cx*cy;
	mf[3][2] = pos[2];
	mf[0][3] = mf[1][3] = mf[2][3] = 0;
	mf[3][3] = 1;
}

void mtxf_joint(MTXF mf, VECF pos, VECS ang)
{
	register float sx = sin(ang[0]);
	register float cx = cos(ang[0]);
	register float sy = sin(ang[1]);
	register float cy = cos(ang[1]);
	register float sz = sin(ang[2]);
	register float cz = cos(ang[2]);
	mf[0][0] = cy*cz;
	mf[0][1] = cy*sz;
	mf[0][2] = -sy;
	mf[0][3] = 0;
	mf[1][0] = sx*sy*cz - cx*sz;
	mf[1][1] = sx*sy*sz + cx*cz;
	mf[1][2] = sx*cy;
	mf[1][3] = 0;
	mf[2][0] = cx*sy*cz + sx*sz;
	mf[2][1] = cx*sy*sz - sx*cz;
	mf[2][2] = cx*cy;
	mf[2][3] = 0;
	mf[3][0] = pos[0];
	mf[3][1] = pos[1];
	mf[3][2] = pos[2];
	mf[3][3] = 1;
}

void mtxf_billboard(MTXF dst, MTXF src, VECF pos, SHORT az)
{
	dst[0][0] = cos(az);
	dst[0][1] = sin(az);
	dst[0][2] = 0;
	dst[0][3] = 0;
	dst[1][0] = -dst[0][1];
	dst[1][1] =  dst[0][0];
	dst[1][2] = 0;
	dst[1][3] = 0;
	dst[2][0] = 0;
	dst[2][1] = 0;
	dst[2][2] = 1;
	dst[2][3] = 0;
#define x pos[0]
#define y pos[1]
#define z pos[2]
	dst[3][0] = src[0][0]*x + src[1][0]*y + src[2][0]*z + src[3][0];
	dst[3][1] = src[0][1]*x + src[1][1]*y + src[2][1]*z + src[3][1];
	dst[3][2] = src[0][2]*x + src[1][2]*y + src[2][2]*z + src[3][2];
#undef x
#undef y
#undef z
	dst[3][3] = 1;
}

void mtxf_stand(MTXF mf, VECF vy, VECF pos, SHORT ay)
{
	VECF forward, vx, vz;
	vecf_set(forward, sin(ay), 0, cos(ay));
	vecf_normalize(vy);
	vecf_cross(vx, vy, forward);
	vecf_normalize(vx);
	vecf_cross(vz, vx, vy);
	vecf_normalize(vz);
	mf[0][0] = vx[0];
	mf[0][1] = vx[1];
	mf[0][2] = vx[2];
	mf[3][0] = pos[0];
	mf[1][0] = vy[0];
	mf[1][1] = vy[1];
	mf[1][2] = vy[2];
	mf[3][1] = pos[1];
	mf[2][0] = vz[0];
	mf[2][1] = vz[1];
	mf[2][2] = vz[2];
	mf[3][2] = pos[2];
	mf[0][3] = 0;
	mf[1][3] = 0;
	mf[2][3] = 0;
	mf[3][3] = 1;
}

void mtxf_ground(MTXF mf, VECF pos, SHORT ay, float radius)
{
	BGFACE *ground;
	VECF v0, v1, v2, forward, vx, vy, vz;
	float y;
	float height = -radius*3;
	v0[0] = pos[0] + sin(ay+0x2AAA)*radius;
	v0[2] = pos[2] + cos(ay+0x2AAA)*radius;
	v1[0] = pos[0] + sin(ay+0x8000)*radius;
	v1[2] = pos[2] + cos(ay+0x8000)*radius;
	v2[0] = pos[0] + sin(ay+0xD555)*radius;
	v2[2] = pos[2] + cos(ay+0xD555)*radius;
	v0[1] = bg_check_ground(v0[0], pos[1] + 150, v0[2], &ground);
	v1[1] = bg_check_ground(v1[0], pos[1] + 150, v1[2], &ground);
	v2[1] = bg_check_ground(v2[0], pos[1] + 150, v2[2], &ground);
	if (v0[1]-pos[1] < height) v0[1] = pos[1];
	if (v1[1]-pos[1] < height) v1[1] = pos[1];
	if (v2[1]-pos[1] < height) v2[1] = pos[1];
	y = (v0[1]+v1[1]+v2[1]) / 3;
	vecf_set(forward, sin(ay), 0, cos(ay));
	vecf_normal(vy, v0, v1, v2);
	vecf_normalize(vy);
	vecf_cross(vx, vy, forward);
	vecf_normalize(vx);
	vecf_cross(vz, vx, vy);
	vecf_normalize(vz);
	mf[0][0] = vx[0];
	mf[0][1] = vx[1];
	mf[0][2] = vx[2];
	mf[3][0] = pos[0];
	mf[1][0] = vy[0];
	mf[1][1] = vy[1];
	mf[1][2] = vy[2];
	mf[3][1] = y < pos[1] ? pos[1] : y;
	mf[2][0] = vz[0];
	mf[2][1] = vz[1];
	mf[2][2] = vz[2];
	mf[3][2] = pos[2];
	mf[0][3] = 0;
	mf[1][3] = 0;
	mf[2][3] = 0;
	mf[3][3] = 1;
}

void mtxf_cat(MTXF mf, MTXF a, MTXF b)
{
	MTXF m;
	register float x, y, z;
	x = a[0][0]; y = a[0][1]; z = a[0][2];
	m[0][0] = x*b[0][0] + y*b[1][0] + z*b[2][0];
	m[0][1] = x*b[0][1] + y*b[1][1] + z*b[2][1];
	m[0][2] = x*b[0][2] + y*b[1][2] + z*b[2][2];
	x = a[1][0]; y = a[1][1]; z = a[1][2];
	m[1][0] = x*b[0][0] + y*b[1][0] + z*b[2][0];
	m[1][1] = x*b[0][1] + y*b[1][1] + z*b[2][1];
	m[1][2] = x*b[0][2] + y*b[1][2] + z*b[2][2];
	x = a[2][0]; y = a[2][1]; z = a[2][2];
	m[2][0] = x*b[0][0] + y*b[1][0] + z*b[2][0];
	m[2][1] = x*b[0][1] + y*b[1][1] + z*b[2][1];
	m[2][2] = x*b[0][2] + y*b[1][2] + z*b[2][2];
	x = a[3][0]; y = a[3][1]; z = a[3][2];
	m[3][0] = x*b[0][0] + y*b[1][0] + z*b[2][0] + b[3][0];
	m[3][1] = x*b[0][1] + y*b[1][1] + z*b[2][1] + b[3][1];
	m[3][2] = x*b[0][2] + y*b[1][2] + z*b[2][2] + b[3][2];
	m[0][3] = m[1][3] = m[2][3] = 0;
	m[3][3] = 1;
	mtxf_cpy(mf, m);
}

void mtxf_scale(MTXF dst, MTXF src, VECF scale)
{
	register int i;
	for (i = 0; i < 4; i++)
	{
		dst[0][i] = src[0][i]*scale[0];
		dst[1][i] = src[1][i]*scale[1];
		dst[2][i] = src[2][i]*scale[2];
		dst[3][i] = src[3][i];
	}
}

void mtxf_transform(MTXF mf, VECS vs)
{
	register float x = vs[0];
	register float y = vs[1];
	register float z = vs[2];
	vs[0] = x*mf[0][0] + y*mf[1][0] + z*mf[2][0] + mf[3][0];
	vs[1] = x*mf[0][1] + y*mf[1][1] + z*mf[2][1] + mf[3][1];
	vs[2] = x*mf[0][2] + y*mf[1][2] + z*mf[2][2] + mf[3][2];
}

void mtxf_to_mtx(Mtx *m, MTXF mf)
{
	int x;
	register int i;
	register short *h = (short *)m;
	register short *l = (short *)m + 16;
	register float *f = (float *)mf;
	for (i = 0; i < 16; i++)
	{
		x = *f++ * 0x10000;
#ifdef sgi
		*h++ = ((short *)&x)[0];
		*l++ = ((short *)&x)[1];
#else
		*h++ = x >> 16;
		*l++ = x >>  0;
#endif
	}
}

void mtx_az(Mtx *m, SHORT az)
{
	MTXF mf;
	mtxf_identity(mf);
	mf[0][0] = cos(az);
	mf[0][1] = sin(az);
	mf[1][0] = -mf[0][1];
	mf[1][1] =  mf[0][0];
	mtxf_to_mtx(m, mf);
}

void vecf_untransform(VECF vf, MTXF mf, MTXF cam)
{
	float x = cam[3][0]*cam[0][0] + cam[3][1]*cam[0][1] + cam[3][2]*cam[0][2];
	float y = cam[3][0]*cam[1][0] + cam[3][1]*cam[1][1] + cam[3][2]*cam[1][2];
	float z = cam[3][0]*cam[2][0] + cam[3][1]*cam[2][1] + cam[3][2]*cam[2][2];
	vf[0] = mf[3][0]*cam[0][0] + mf[3][1]*cam[0][1] + mf[3][2]*cam[0][2] - x;
	vf[1] = mf[3][0]*cam[1][0] + mf[3][1]*cam[1][1] + mf[3][2]*cam[1][2] - y;
	vf[2] = mf[3][0]*cam[2][0] + mf[3][1]*cam[2][1] + mf[3][2]*cam[2][2] - z;
}

void cartesian_to_polar(VECF a, VECF b, float *dist, short *ax, short *ay)
{
	register float dx = b[0]-a[0];
	register float dy = b[1]-a[1];
	register float dz = b[2]-a[2];
	*dist = sqrtf(dx*dx + dy*dy + dz*dz);
	*ax = atan2(sqrtf(dx*dx + dz*dz), dy);
	*ay = atan2(dz, dx);
}

void polar_to_cartesian(VECF a, VECF b, float dist, SHORT ax, SHORT ay)
{
	b[0] = a[0] + dist*cos(ax)*sin(ay);
	b[1] = a[1] + dist*sin(ax);
	b[2] = a[2] + dist*cos(ax)*cos(ay);
}

int converge_i(int x, int dst, int inc, int dec)
{
	if (x < dst)
	{
		if ((x += inc) > dst) x = dst;
	}
	else
	{
		if ((x -= dec) < dst) x = dst;
	}
	return x;
}

float converge_f(float x, float dst, float inc, float dec)
{
	if (x < dst)
	{
		if ((x += inc) > dst) x = dst;
	}
	else
	{
		if ((x -= dec) < dst) x = dst;
	}
	return x;
}

static int atan_yx(float y, float x)
{
	USHORT ang;
	if (x == 0) ang = math_atan[0];
	else        ang = math_atan[(int)(y/x * 1024 + 0.5F)];
	return ang;
}

short atan2(float y, float x)
{
	short ang;
	if (x >= 0)
	{
		if (y >= 0)
		{
			if (y >= x) ang = 0x0000 + atan_yx(x, y);
			else        ang = 0x4000 - atan_yx(y, x);
		}
		else
		{
			y = -y;
			if (y < x)  ang = 0x4000 + atan_yx(y, x);
			else        ang = 0x8000 - atan_yx(x, y);
		}
	}
	else
	{
		x = -x;
		if (y < 0)
		{
			y = -y;
			if (y >= x) ang = 0x8000 + atan_yx(x, y);
			else        ang = 0xC000 - atan_yx(y, x);
		}
		else
		{
			if (y < x)  ang = 0xC000 + atan_yx(y, x);
			else        ang = 0x0000 - atan_yx(x, y);
		}
	}
	return ang;
}

float atan2f(float y, float x)
{
	return (float)atan2(y, x) * (DOUBLE)M_PI/0x8000;
}

static BSPLINE *bspline;
static float bspline_phase;
static int bspline_mode;

void bspline_curve(float curve[4], float p, UNUSED int mode)
{
	float n = 1 - p;
	float nn = n*n;
	float nnn = nn*n;
	float pp = p*p;
	float ppp = pp*p;
	switch (bspline_mode)
	{
	case 1:
		curve[0] =  nnn;
		curve[1] =  ppp*( 7/ 4.0F) - pp*(9/2.0F) + p*(3/1.0F);
		curve[2] = -ppp*(11/12.0F) + pp*(3/2.0F);
		curve[3] =  ppp*( 1/ 6.0F);
		break;
	case 2:
		curve[0] =  nnn*( 1/ 4.0F);
		curve[1] =  ppp*( 7/12.0F) - pp*(5/4.0F) + p*(1/4.0F) + (7/12.0F);
		curve[2] = -ppp*( 1/ 2.0F) + pp*(1/2.0F) + p*(1/2.0F) + (1/ 6.0F);
		curve[3] =  ppp*( 1/ 6.0F);
		break;
	case 3:
		curve[0] =  nnn*( 1/ 6.0F);
		curve[1] =  ppp*( 1/ 2.0F) - pp                       + (2/ 3.0F);
		curve[2] = -ppp*( 1/ 2.0F) + pp*(1/2.0F) + p*(1/2.0F) + (1/ 6.0F);
		curve[3] =  ppp*( 1/ 6.0F);
		break;
	case 4:
		curve[0] =  nnn*( 1/ 6.0F);
		curve[1] = -nnn*( 1/ 2.0F) + nn*(1/2.0F) + n*(1/2.0F) + (1/ 6.0F);
		curve[2] =  nnn*( 7/12.0F) - nn*(5/4.0F) + n*(1/4.0F) + (7/12.0F);
		curve[3] =  ppp*( 1/ 4.0F);
		break;
	case 5:
		curve[0] =  nnn*( 1/ 6.0F);
		curve[1] = -nnn*(11/12.0F) + nn*(3/2.0F);
		curve[2] =  nnn*( 7/ 4.0F) - nn*(9/2.0F) + n*(3/1.0F);
		curve[3] =  ppp;
		break;
	}
}

void bspline_init(BSPLINE *b)
{
	bspline = b;
	bspline_phase = 0;
	bspline_mode = 1;
}

int bspline_update(VECF dst)
{
	float curve[4];
	int i;
	int result = FALSE;
	vecf_cpy(dst, vecf_0);
	bspline_curve(curve, bspline_phase, bspline_mode);
	for (i = 0; i < 4; i++)
	{
		dst[0] += curve[i] * bspline[i].pos[0];
		dst[1] += curve[i] * bspline[i].pos[1];
		dst[2] += curve[i] * bspline[i].pos[2];
	}
	if ((bspline_phase += (float)bspline[0].time/1000) >= 1)
	{
		bspline++;
		bspline_phase -= 1;
		switch (bspline_mode)
		{
		case 5:
			result = TRUE;
			break;
		case 3:
			if (bspline[2].time == 0) bspline_mode = 4;
			break;
		default:
			bspline_mode++;
			break;
		}
	}
	return result;
}
