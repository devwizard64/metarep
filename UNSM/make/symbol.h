stack_main              = 0x80200200;

/******************************************************************************
 * data                                                                       *
 ******************************************************************************/

/* src/main.S */
scheduler_vq_audio      = 0x8032D560;
scheduler_vq_video      = 0x8032D564;
scheduler_task          = 0x8032D568;
scheduler_audtask       = 0x8032D56C;
scheduler_gfxtask       = 0x8032D570;
scheduler_audtask_next  = 0x8032D574;
scheduler_gfxtask_next  = 0x8032D578;
scheduler_audio         = 0x8032D57C;
scheduler_vi            = 0x8032D580;
scheduler_reset         = 0x8032D584;
scheduler_reset_timer   = 0x8032D588;
debug_stage             = 0x8032D58C;
debug_thread            = 0x8032D590;
debug_time              = 0x8032D594;
debug_mem               = 0x8032D598;
debug_time_table        = 0x8032D59C;
debug_mem_table         = 0x8032D5AC;
debug_time_index        = 0x8032D5BC;
debug_mem_index         = 0x8032D5C0;

/* src/app.S */
video_frame             = 0x8032D5D4;
video_vi                = 0x8032D5D8;
video_dl                = 0x8032D5DC;
video_callback          = 0x8032D5E0;
controller_p1           = 0x8032D5EC;

_80330D30   = 0x80330D30;
_80330D78   = 0x80330D78;

/******************************************************************************
 * rodata                                                                     *
 ******************************************************************************/

/******************************************************************************
 * bss                                                                        *
 ******************************************************************************/

/* src/main.S */
thread_fault            = 0x8033A580;
thread_idle             = 0x8033A730;
thread_scheduler        = 0x8033A8E0;
thread_app              = 0x8033AA90;
thread_audio            = 0x8033AC40;
mq_pi                   = 0x8033ADF0;
mq_scheduler            = 0x8033AE08;
mq_scheduler_task       = 0x8033AE20;
msg_app                 = 0x8033AE38;
msg_pi                  = 0x8033AE40;
msg_si                  = 0x8033AEC0;
msg_scheduler           = 0x8033AEC8;
msg_scheduler_task      = 0x8033AF08;
iomesg_app              = 0x8033AF48;
msg_null                = 0x8033AF5C;
mq_app                  = 0x8033AF60;
mq_si                   = 0x8033AF78;

/* src/app.S */
controller_table        = 0x8033AF90;
contstatus_table        = 0x8033AFE8;
contpad_table           = 0x8033AFF8;
video_vq                = 0x8033B010;
video_task              = 0x8033B068;
video_gfx               = 0x8033B06C;
video_mem               = 0x8033B070;
video_buf               = 0x8033B074;

/******************************************************************************
 * face                                                                       *
 ******************************************************************************/

data_face_04000000 = 0x04000000;
data_face_04000650 = 0x04000650;
data_face_04004F90 = 0x04004F90;
