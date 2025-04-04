#ifndef _MBI_H_
#define	_MBI_H_

/**************************************************************************
 *									  *
 *		 Copyright (C) 1994, Silicon Graphics, Inc.		  *
 *									  *
 *  These coded instructions, statements, and computer programs  contain  *
 *  unpublished  proprietary  information of Silicon Graphics, Inc., and  *
 *  are protected by Federal copyright law.  They  may  not be disclosed  *
 *  to  third  parties  or copied or duplicated in any form, in whole or  *
 *  in part, without the prior written consent of Silicon Graphics, Inc.  *
 *									  *
 **************************************************************************/

/**************************************************************************
 *
 *  $Revision: 1.134 $
 *  $Date: 1997/02/11 08:25:28 $
 *  $Source: /disk6/Master/cvsmdev2/PR/include/mbi.h,v $
 *
 **************************************************************************/

/*
 * Header file for the Media Binary Interface
 *
 * NOTE: This file is included by the RSP microcode, so any C-specific
 * constructs must be bracketed by #ifdef _LANGUAGE_C
 *
 */


/*
 * the SHIFT macros are used to build display list commands, inserting
 * bit-fields into a 32-bit word. They take a value, a shift amount, 
 * and a width.
 *
 * For the left shift, the lower bits of the value are masked, 
 * then shifted left.
 *
 * For the right shift, the value is shifted right, then the lower bits
 * are masked.
 *
 * (NOTE: _SHIFTL(v, 0, 32) won't work, just use an assignment)
 *
 */
#define _SHIFTL(v, s, w)	\
    ((unsigned int) (((unsigned int)(v) & ((0x01 << (w)) - 1)) << (s)))
#define _SHIFTR(v, s, w)	\
    ((unsigned int)(((unsigned int)(v) >> (s)) & ((0x01 << (w)) - 1)))

#define _SHIFT _SHIFTL	/* old, for compatibility only */

#define G_ON	(1)
#define G_OFF	(0)

/**************************************************************************
 *
 * Graphics Binary Interface
 *
 **************************************************************************/

#include <PR/gbi.h>

/**************************************************************************
 *
 * Audio Binary Interface
 *
 **************************************************************************/

#include <PR/abi.h>

/**************************************************************************
 *
 * Task list
 *
 **************************************************************************/

#define	M_GFXTASK	1
#define	M_AUDTASK	2
#define	M_VIDTASK	3

/**************************************************************************
 *
 * Segment macros and definitions
 *
 **************************************************************************/

#define	NUM_SEGMENTS		(16)
#define	SEGMENT_OFFSET(a)	((unsigned int)(a) & 0x00ffffff)
#define	SEGMENT_NUMBER(a)	((unsigned int)(a) >> 24)
#define	SEGMENT_ADDR(num, off)	(((num) << 24) + (off))

#ifndef NULL
#define NULL 0
#endif

#endif /* !_MBI_H_ */
