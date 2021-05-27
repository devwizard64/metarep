#ifndef _FILE_H_
#define _FILE_H_

#ifdef __ASSEMBLER__

#define TABLE(table)            .word (table##_end-table##_start)/8, 0
#define FILE(file)              .word file, file##_end - file

#define MOTION(motion, flag, height, start, end, frame, joint)  \
    .half flag, height, start, end, frame, joint;               \
    .word motion##_val - motion;                                \
    .word motion##_tbl - motion;                                \
    .word motion##_end - motion

#define DEMO(stage)             .byte stage, 0, 0, 0

#endif /* __ASSEMBLER__ */

#endif /* _FILE_H_ */
