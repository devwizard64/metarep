#include <sm64.h>

Mtx mtx_1 = gdSPDefMatrix(
	1, 0, 0, 0,
	0, 1, 0, 0,
	0, 0, 1, 0,
	0, 0, 0, 1
);
FVEC fvec_0 = {0, 0, 0};
SVEC svec_0 = {0, 0, 0};
FVEC fvec_1 = {1, 1, 1};
SVEC svec_1 = {1, 1, 1};

float *FVecCpy(FVEC dst, FVEC src)
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

float *FVecSet(FVEC v, float x, float y, float z)
{
	v[0] = x;
	v[1] = y;
	v[2] = z;
#ifdef sgi
	return (float *)&v;
#else
	return v;
#endif
}

float *FVecAdd(FVEC v, FVEC a)
{
	v[0] += a[0];
	v[1] += a[1];
	v[2] += a[2];
#ifdef sgi
	return (float *)&v;
#else
	return v;
#endif
}

float *FVecAddTo(FVEC v, FVEC a, FVEC b)
{
	v[0] = a[0] + b[0];
	v[1] = a[1] + b[1];
	v[2] = a[2] + b[2];
#ifdef sgi
	return (float *)&v;
#else
	return v;
#endif
}

short *SVecCpy(SVEC dst, SVEC src)
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

short *SVecSet(SVEC v, SHORT x, SHORT y, SHORT z)
{
	v[0] = x;
	v[1] = y;
	v[2] = z;
#ifdef sgi
	return (short *)&v;
#else
	return v;
#endif
}

short *SVecAdd(SVEC v, SVEC a)
{
	v[0] += a[0];
	v[1] += a[1];
	v[2] += a[2];
#ifdef sgi
	return (short *)&v;
#else
	return v;
#endif
}

short *SVecAddTo(SVEC v, SVEC a, SVEC b)
{
	v[0] = a[0] + b[0];
	v[1] = a[1] + b[1];
	v[2] = a[2] + b[2];
#ifdef sgi
	return (short *)&v;
#else
	return v;
#endif
}

short *SVecSub(SVEC v, SVEC a)
{
	v[0] -= a[0];
	v[1] -= a[1];
	v[2] -= a[2];
#ifdef sgi
	return (short *)&v;
#else
	return v;
#endif
}

float *SVecToFVec(FVEC dst, SVEC src)
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

short *FVecToSVec(SVEC dst, FVEC src)
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

float *CalcNormal(FVEC v, FVEC v0, FVEC v1, FVEC v2)
{
#define CROSS(x0, y0, x1, y1, x2, y2) \
	(((y1)-(y0))*((x2)-(x1)) - ((y2)-(y1))*((x1)-(x0)))
	v[0] = CROSS(v0[2], v0[1], v1[2], v1[1], v2[2], v2[1]);
	v[1] = CROSS(v0[0], v0[2], v1[0], v1[2], v2[0], v2[2]);
	v[2] = CROSS(v0[1], v0[0], v1[1], v1[0], v2[1], v2[0]);
#undef CROSS
#ifdef sgi
	return (float *)&v;
#else
	return v;
#endif
}

float *CrossProduct(FVEC v, FVEC a, FVEC b)
{
	v[0] = a[1]*b[2] - b[1]*a[2];
	v[1] = a[2]*b[0] - b[2]*a[0];
	v[2] = a[0]*b[1] - b[0]*a[1];
#ifdef sgi
	return (float *)&v;
#else
	return v;
#endif
}

float *Normalize(FVEC v)
{
	float d = 1 / DIST3(v[0], v[1], v[2]);
	v[0] *= d;
	v[1] *= d;
	v[2] *= d;
#ifdef sgi
	return (float *)&v;
#else
	return v;
#endif
}

void FMtxCpy(FMTX dst, FMTX src)
{
#ifdef sgi
	register int i;
	register int *d = (int *)dst;
	register int *s = (int *)src;
	for (i = 0; i < 16; i++) *d++ = *s++;
#else
	bcopy(src, dst, sizeof(FMTX));
#endif
}

void FMtxIdent(FMTX m)
{
#ifdef sgi
	register int i;
	register float *f;
	for (f = &m[0][1], i = 0; i < 14; i++, f += 1) *f = 0;
	for (f = &m[0][0], i = 0; i <  4; i++, f += 5) *f = 1;
#else
	guMtxIdentF(m);
#endif
}

void FMtxPos(FMTX m, FVEC pos)
{
	FMtxIdent(m);
	m[3][0] = pos[0];
	m[3][1] = pos[1];
	m[3][2] = pos[2];
}

void FMtxLookAt(FMTX m, FVEC eye, FVEC look, SHORT angz)
{
	register float d;
	float dx, dz, xy, yy, zy, xz, yz, zz, xx, yx, zx;
	dx = look[0] - eye[0];
	dz = look[2] - eye[2];
	d = -1.0 / DIST2(dx, dz);
	dx *= d;
	dz *= d;
	yy = COS(angz);
	xy = SIN(angz) * dz;
	zy = -SIN(angz) * dx;
	xz = look[0] - eye[0];
	yz = look[1] - eye[1];
	zz = look[2] - eye[2];
	d = -1.0 / DIST3(xz, yz, zz);
	xz *= d;
	yz *= d;
	zz *= d;
	xx = yy*zz - zy*yz;
	yx = zy*xz - xy*zz;
	zx = xy*yz - yy*xz;
	d = 1.0 / DIST3(xx, yx, zx);
	xx *= d;
	yx *= d;
	zx *= d;
	xy = yz*zx - zz*yx;
	yy = zz*xx - xz*zx;
	zy = xz*yx - yz*xx;
	d = 1.0 / DIST3(xy, yy, zy);
	xy *= d;
	yy *= d;
	zy *= d;
	m[0][0] = xx;
	m[1][0] = yx;
	m[2][0] = zx;
	m[3][0] = -(eye[0]*xx + eye[1]*yx + eye[2]*zx);
	m[0][1] = xy;
	m[1][1] = yy;
	m[2][1] = zy;
	m[3][1] = -(eye[0]*xy + eye[1]*yy + eye[2]*zy);
	m[0][2] = xz;
	m[1][2] = yz;
	m[2][2] = zz;
	m[3][2] = -(eye[0]*xz + eye[1]*yz + eye[2]*zz);
	m[0][3] = 0;
	m[1][3] = 0;
	m[2][3] = 0;
	m[3][3] = 1;
}

void FMtxCoord(FMTX m, FVEC pos, SVEC ang)
{
	register float sx = SIN(ang[0]);
	register float cx = COS(ang[0]);
	register float sy = SIN(ang[1]);
	register float cy = COS(ang[1]);
	register float sz = SIN(ang[2]);
	register float cz = COS(ang[2]);
	m[0][0] =  cy*cz + sx*sy*sz;
	m[1][0] = -cy*sz + sx*sy*cz;
	m[2][0] = cx*sy;
	m[3][0] = pos[0];
	m[0][1] = cx*sz;
	m[1][1] = cx*cz;
	m[2][1] = -sx;
	m[3][1] = pos[1];
	m[0][2] = -sy*cz + sx*cy*sz;
	m[1][2] =  sy*sz + sx*cy*cz;
	m[2][2] = cx*cy;
	m[3][2] = pos[2];
	m[0][3] = m[1][3] = m[2][3] = 0;
	m[3][3] = 1;
}

void FMtxJoint(FMTX m, FVEC pos, SVEC ang)
{
	register float sx = SIN(ang[0]);
	register float cx = COS(ang[0]);
	register float sy = SIN(ang[1]);
	register float cy = COS(ang[1]);
	register float sz = SIN(ang[2]);
	register float cz = COS(ang[2]);
	m[0][0] = cy*cz;
	m[0][1] = cy*sz;
	m[0][2] = -sy;
	m[0][3] = 0;
	m[1][0] = sx*sy*cz - cx*sz;
	m[1][1] = sx*sy*sz + cx*cz;
	m[1][2] = sx*cy;
	m[1][3] = 0;
	m[2][0] = cx*sy*cz + sx*sz;
	m[2][1] = cx*sy*sz - sx*cz;
	m[2][2] = cx*cy;
	m[2][3] = 0;
	m[3][0] = pos[0];
	m[3][1] = pos[1];
	m[3][2] = pos[2];
	m[3][3] = 1;
}

void FMtxBillboard(FMTX dst, FMTX src, FVEC pos, SHORT angz)
{
	dst[0][0] = COS(angz);
	dst[0][1] = SIN(angz);
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
	dst[3][0] = MDOT4(src, 0, pos[0], pos[1], pos[2]);
	dst[3][1] = MDOT4(src, 1, pos[0], pos[1], pos[2]);
	dst[3][2] = MDOT4(src, 2, pos[0], pos[1], pos[2]);
	dst[3][3] = 1;
}

void FMtxStand(FMTX m, FVEC vy, FVEC pos, SHORT angy)
{
	FVEC forward, vx, vz;
	FVecSet(forward, SIN(angy), 0, COS(angy));
	Normalize(vy);
	CrossProduct(vx, vy, forward);
	Normalize(vx);
	CrossProduct(vz, vx, vy);
	Normalize(vz);
	m[0][0] = vx[0];
	m[0][1] = vx[1];
	m[0][2] = vx[2];
	m[3][0] = pos[0];
	m[1][0] = vy[0];
	m[1][1] = vy[1];
	m[1][2] = vy[2];
	m[3][1] = pos[1];
	m[2][0] = vz[0];
	m[2][1] = vz[1];
	m[2][2] = vz[2];
	m[3][2] = pos[2];
	m[0][3] = 0;
	m[1][3] = 0;
	m[2][3] = 0;
	m[3][3] = 1;
}

void FMtxGround(FMTX m, FVEC pos, SHORT angy, float radius)
{
	BGFACE *ground;
	FVEC v0, v1, v2, forward, vx, vy, vz;
	float y;
	float height = -radius*3;
	v0[0] = pos[0] + SIN(angy+DEG( 60))*radius;
	v0[2] = pos[2] + COS(angy+DEG( 60))*radius;
	v1[0] = pos[0] + SIN(angy+DEG(180))*radius;
	v1[2] = pos[2] + COS(angy+DEG(180))*radius;
	v2[0] = pos[0] + SIN(angy+DEG(300))*radius;
	v2[2] = pos[2] + COS(angy+DEG(300))*radius;
	v0[1] = BGCheckGround(v0[0], pos[1] + 150, v0[2], &ground);
	v1[1] = BGCheckGround(v1[0], pos[1] + 150, v1[2], &ground);
	v2[1] = BGCheckGround(v2[0], pos[1] + 150, v2[2], &ground);
	if (v0[1]-pos[1] < height) v0[1] = pos[1];
	if (v1[1]-pos[1] < height) v1[1] = pos[1];
	if (v2[1]-pos[1] < height) v2[1] = pos[1];
	y = (v0[1]+v1[1]+v2[1]) / 3;
	FVecSet(forward, SIN(angy), 0, COS(angy));
	CalcNormal(vy, v0, v1, v2);
	Normalize(vy);
	CrossProduct(vx, vy, forward);
	Normalize(vx);
	CrossProduct(vz, vx, vy);
	Normalize(vz);
	m[0][0] = vx[0];
	m[0][1] = vx[1];
	m[0][2] = vx[2];
	m[3][0] = pos[0];
	m[1][0] = vy[0];
	m[1][1] = vy[1];
	m[1][2] = vy[2];
	m[3][1] = y < pos[1] ? pos[1] : y;
	m[2][0] = vz[0];
	m[2][1] = vz[1];
	m[2][2] = vz[2];
	m[3][2] = pos[2];
	m[0][3] = 0;
	m[1][3] = 0;
	m[2][3] = 0;
	m[3][3] = 1;
}

void FMtxCatAffine(FMTX m, FMTX a, FMTX b)
{
	FMTX tmp;
	register float x, y, z;
	x = a[0][0]; y = a[0][1]; z = a[0][2];
	tmp[0][0] = x*b[0][0] + y*b[1][0] + z*b[2][0];
	tmp[0][1] = x*b[0][1] + y*b[1][1] + z*b[2][1];
	tmp[0][2] = x*b[0][2] + y*b[1][2] + z*b[2][2];
	x = a[1][0]; y = a[1][1]; z = a[1][2];
	tmp[1][0] = x*b[0][0] + y*b[1][0] + z*b[2][0];
	tmp[1][1] = x*b[0][1] + y*b[1][1] + z*b[2][1];
	tmp[1][2] = x*b[0][2] + y*b[1][2] + z*b[2][2];
	x = a[2][0]; y = a[2][1]; z = a[2][2];
	tmp[2][0] = x*b[0][0] + y*b[1][0] + z*b[2][0];
	tmp[2][1] = x*b[0][1] + y*b[1][1] + z*b[2][1];
	tmp[2][2] = x*b[0][2] + y*b[1][2] + z*b[2][2];
	x = a[3][0]; y = a[3][1]; z = a[3][2];
	tmp[3][0] = x*b[0][0] + y*b[1][0] + z*b[2][0] + b[3][0];
	tmp[3][1] = x*b[0][1] + y*b[1][1] + z*b[2][1] + b[3][1];
	tmp[3][2] = x*b[0][2] + y*b[1][2] + z*b[2][2] + b[3][2];
	tmp[0][3] = tmp[1][3] = tmp[2][3] = 0;
	tmp[3][3] = 1;
	FMtxCpy(m, tmp);
}

void FMtxScale(FMTX dst, FMTX src, FVEC scale)
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

void Transform(FMTX m, SVEC v)
{
	register float x = v[0];
	register float y = v[1];
	register float z = v[2];
	v[0] = x*m[0][0] + y*m[1][0] + z*m[2][0] + m[3][0];
	v[1] = x*m[0][1] + y*m[1][1] + z*m[2][1] + m[3][1];
	v[2] = x*m[0][2] + y*m[1][2] + z*m[2][2] + m[3][2];
}

void FMtxToMtx(Mtx *m, FMTX fm)
{
#ifdef sgi
	int x;
	register int i;
	register short *h = (short *)m;
	register short *l = (short *)m + 16;
	register float *f = (float *)fm;
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
#else
	guMtxF2L(fm, m);
#endif
}

void MtxAngZ(Mtx *m, SHORT angz)
{
	FMTX fm;
	FMtxIdent(fm);
	fm[0][0] = COS(angz);
	fm[0][1] = SIN(angz);
	fm[1][0] = -fm[0][1];
	fm[1][1] =  fm[0][0];
	FMtxToMtx(m, fm);
}

void CalcScenePos(FVEC v, FMTX m, FMTX cam)
{
	float x = cam[3][0]*cam[0][0] + cam[3][1]*cam[0][1] + cam[3][2]*cam[0][2];
	float y = cam[3][0]*cam[1][0] + cam[3][1]*cam[1][1] + cam[3][2]*cam[1][2];
	float z = cam[3][0]*cam[2][0] + cam[3][1]*cam[2][1] + cam[3][2]*cam[2][2];
	v[0] = m[3][0]*cam[0][0] + m[3][1]*cam[0][1] + m[3][2]*cam[0][2] - x;
	v[1] = m[3][0]*cam[1][0] + m[3][1]*cam[1][1] + m[3][2]*cam[1][2] - y;
	v[2] = m[3][0]*cam[2][0] + m[3][1]*cam[2][1] + m[3][2]*cam[2][2] - z;
}

void CartesianToPolar(FVEC a, FVEC b, float *dist, short *angx, short *angy)
{
	register float dx = b[0]-a[0];
	register float dy = b[1]-a[1];
	register float dz = b[2]-a[2];
	*dist = DIST3(dx, dy, dz);
	*angx = ATAN2(DIST2(dx, dz), dy);
	*angy = ATAN2(dz, dx);
}

void PolarToCartesian(FVEC a, FVEC b, float dist, SHORT angx, SHORT angy)
{
	b[0] = a[0] + dist*COS(angx)*SIN(angy);
	b[1] = a[1] + dist*SIN(angx);
	b[2] = a[2] + dist*COS(angx)*COS(angy);
}

int ConvergeI(int x, int dst, int inc, int dec)
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

float ConvergeF(float x, float dst, float inc, float dec)
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

static int AtanRef(float y, float x)
{
	USHORT ang;
	if (x == 0) ang = atantable[0];
	else        ang = atantable[(int)(y/x * 1024 + 0.5F)];
	return ang;
}

short ATAN2(float y, float x)
{
	USHORT ang;
	if (x >= 0)
	{
		if (y >= 0)
		{
			if (y >= x) ang = 0x0000 + AtanRef(x, y);
			else        ang = 0x4000 - AtanRef(y, x);
		}
		else
		{
			y = -y;
			if (y < x)  ang = 0x4000 + AtanRef(y, x);
			else        ang = 0x8000 - AtanRef(x, y);
		}
	}
	else
	{
		x = -x;
		if (y < 0)
		{
			y = -y;
			if (y >= x) ang = 0x8000 + AtanRef(x, y);
			else        ang = 0xC000 - AtanRef(y, x);
		}
		else
		{
			if (y < x)  ang = 0xC000 + AtanRef(y, x);
			else        ang = 0x0000 - AtanRef(x, y);
		}
	}
	return ang;
}

float ATAN2F(float y, float x)
{
	return (float)ATAN2(y, x) * M_PI/0x8000;
}

static BSPLINE *bspline;
static float bspline_phase;
static int bspline_mode;

static void BSplineCurve(float curve[4], float p, UNUSED int mode)
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

void BSplineInit(BSPLINE *b)
{
	bspline = b;
	bspline_phase = 0;
	bspline_mode = 1;
}

int BSplineProc(FVEC dst)
{
	float curve[4];
	int i, result = FALSE;
	FVecCpy(dst, fvec_0);
	BSplineCurve(curve, bspline_phase, bspline_mode);
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
