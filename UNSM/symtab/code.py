import main
# import ultra

sym_J0_rspboot_text = {
	0x8032A320: main.sym("rspbootTextStart"),
	0x8032A3F0: main.sym("rspbootTextEnd"),
}

sym_J0_gspFast3D_fifo_text = {
	0x8032A3F0: main.sym("gspFast3D_fifoTextStart"),
	0x8032B7F8: main.sym("gspFast3D_fifoTextEnd"),
}

sym_J0_aspMain_text = {
	0x8032B800: main.sym("aspMainTextStart"),
	0x8032C620: main.sym("aspMainTextEnd"),
}

sym_J0_gspFast3D_fifo_data = {
	0x80338750: main.sym("gspFast3D_fifoDataStart"),
	0x80338F50: main.sym("gspFast3D_fifoDataEnd"),
}

sym_J0_aspMain_data = {
	0x80338F50: main.sym("aspMainDataStart"),
	0x80339210: main.sym("aspMainDataEnd"),
}

sym_J0_crt0_text = {
	# ==========================================================================
	# text
	# ==========================================================================

	# src/crt0.s
	0x80246000: main.sym("_start", flag={"GLOBL"}),

	0x80200A00: main.sym("entry_stack+1024"),
	0x80339210: main.sym("_codeSegmentBssStart"),
}

sym_J0_code_text = {
	0x000F4210: main.sym("_ulibSegmentRomStart"),
	0x001076A0: main.sym("_ulibSegmentRomEnd"),

	# ==========================================================================
	# text
	# ==========================================================================

	# src/main.c
	0x80246050: main.sym("DebugCheck", flag={"GLOBL"}),
	0x80246170: main.sym("dummy"),
	0x802461CC: main.sym("DebugEntry"),
	0x802461DC: main.sym("DebugSchedProc"),
	0x802461EC: main.sym("DebugSchedVI"),
	0x802461FC: main.sym("ScInit"),
	0x802462E0: main.sym("ScInitMem"),
	0x80246338: main.sym("CreateThread"),
	0x8024639C: main.sym("ScEventPreNMI"),
	0x802463EC: main.sym("ScTaskFlush"),
	0x8024651C: main.sym("ScTaskStart"),
	0x8024659C: main.sym("ScTaskYield"),
	0x802465EC: main.sym("ScEventGfxTask"),
	0x80246648: main.sym("ScSkipAudTask"),
	0x8024669C: main.sym("ScEventVI"),
	0x802467FC: main.sym("ScEventSP"),
	0x8024694C: main.sym("ScEventDP"),
	0x802469B8: main.sym("SchedProc"),
	0x80246A9C: main.sym("L80246A9C", flag={"GLOBL","LOCAL"}),
	0x80246AAC: main.sym("L80246AAC", flag={"GLOBL","LOCAL"}),
	0x80246ABC: main.sym("L80246ABC", flag={"GLOBL","LOCAL"}),
	0x80246ACC: main.sym("L80246ACC", flag={"GLOBL","LOCAL"}),
	0x80246ADC: main.sym("L80246ADC", flag={"GLOBL","LOCAL"}),
	0x80246B14: main.sym("ScSetClient", flag={"GLOBL"}),
	0x80246B74: main.sym("ScQueueTask", flag={"GLOBL"}),
	0x80246BB4: main.sym("ScQueueAudTask", flag={"GLOBL"}),
	0x80246C10: main.sym("ScQueueGfxTask", flag={"GLOBL"}),
	0x80246C9C: main.sym("ScAudEnable", flag={"GLOBL"}),
	0x80246CB8: main.sym("ScAudDisable", flag={"GLOBL"}),
	0x80246CF0: main.sym("IdleProc"),
	0x80246DC4: main.sym("entry", flag={"GLOBL"}),

	# src/graphics.c
	0x80246E40: main.sym("GfxInitDP"),
	0x80247174: main.sym("GfxInitSP"),
	0x80247254: main.sym("GfxInitZB"),
	0x80247398: main.sym("GfxInitCB"),
	0x80247488: main.sym("GfxClear", flag={"GLOBL"}),
	0x802475F0: main.sym("GfxVpClear", flag={"GLOBL"}),
	0x8024781C: main.sym("GfxDrawBorder"),
	0x8024798C: main.sym("GfxVpScissor", flag={"GLOBL"}),
	0x80247B0C: main.sym("GfxMakeTask"),
	0x80247C9C: main.sym("GfxStart", flag={"GLOBL"}),
	0x80247CE4: main.sym("GfxEnd", flag={"GLOBL"}),
	0x80247D84: main.sym("GfxReset"),
	0x80247ED8: main.sym("FrameInit"),
	0x80247FAC: main.sym("FrameStart"),
	0x80248060: main.sym("FrameEnd"),
	0x802481B0: main.sym("DemoRecord"),
	0x802482D4: main.sym("ContProcStick"),
	0x80248468: main.sym("DemoProc"),
	0x80248608: main.sym("ContProc"),
	0x802487F4: main.sym("ContInit"),
	0x80248934: main.sym("GfxInit"),
	0x80248AC0: main.sym("GfxProc", flag={"GLOBL"}),

	# src/audio.c
	0x80248C10: main.sym("AudResetMute", flag={"GLOBL"}),
	0x80248C28: main.sym("AudSetMute", flag={"GLOBL"}),
	0x80248CB8: main.sym("AudClrMute", flag={"GLOBL"}),
	0x80248D48: main.sym("AudLock", flag={"GLOBL"}),
	0x80248D90: main.sym("AudUnlock", flag={"GLOBL"}),
	0x80248DD8: main.sym("AudSetMode", flag={"GLOBL"}),
	0x80248E24: main.sym("AudPlayFaceSound", flag={"GLOBL"}),
	0x80248FBC: main.sym("AudProcWaveSound", flag={"GLOBL"}),
	0x80249040: main.sym("AudProcEndlessMusic", flag={"GLOBL"}),
	0x80249148: main.sym("AudPlayBGM", flag={"GLOBL"}),
	0x802491FC: main.sym("AudFadeout", flag={"GLOBL"}),
	0x8024924C: main.sym("AudFadeoutBGM", flag={"GLOBL"}),
	0x802492A0: main.sym("AudPlayStageBGM", flag={"GLOBL"}),
	0x802492E0: main.sym("AudPlayShellBGM", flag={"GLOBL"}),
	0x8024931C: main.sym("AudStopShellBGM", flag={"GLOBL"}),
	0x80249368: main.sym("AudPlaySpecialBGM", flag={"GLOBL"}),
	0x802493D4: main.sym("AudFadeoutSpecialBGM", flag={"GLOBL"}),
	0x80249418: main.sym("AudStopSpecialBGM", flag={"GLOBL"}),
	0x80249464: main.sym("AudPlayLevelSe", flag={"GLOBL"}),
	0x802494A8: main.sym("AudTick", flag={"GLOBL"}),
	0x802494D0: main.sym("AudProc", flag={"GLOBL"}),

	# src/game.c
	0x802495B0: main.sym("GmTimeCtrl", flag={"GLOBL"}),
	0x80249688: main.sym("GmCheckPause"),
	0x80249734: main.sym("GmSetState"),
	0x8024975C: main.sym("GmExit"),
	0x80249788: main.sym("GmFadeout", flag={"GLOBL"}),
	0x802497FC: main.sym("game_8024982C"),
	0x8024980C: main.sym("GmInitMessage", flag={"GLOBL"}),
	0x8024992C: main.sym("PL_InitDoor"),
	0x802499E0: main.sym("PL_InitCap"),
	0x80249A84: main.sym("PL_InitState"),
	0x80249AC4: main.sym("L80249AF4", flag={"GLOBL","LOCAL"}),
	0x80249ADC: main.sym("L80249B0C", flag={"GLOBL","LOCAL"}),
	0x80249AF8: main.sym("L80249B28", flag={"GLOBL","LOCAL"}),
	0x80249B10: main.sym("L80249B40", flag={"GLOBL","LOCAL"}),
	0x80249B28: main.sym("L80249B58", flag={"GLOBL","LOCAL"}),
	0x80249B44: main.sym("L80249B74", flag={"GLOBL","LOCAL"}),
	0x80249B5C: main.sym("L80249B8C", flag={"GLOBL","LOCAL"}),
	0x80249B78: main.sym("L80249BA8", flag={"GLOBL","LOCAL"}),
	0x80249B90: main.sym("L80249BC0", flag={"GLOBL","LOCAL"}),
	0x80249BA8: main.sym("L80249BD8", flag={"GLOBL","LOCAL"}),
	0x80249BC0: main.sym("L80249BF0", flag={"GLOBL","LOCAL"}),
	0x80249BDC: main.sym("L80249C0C", flag={"GLOBL","LOCAL"}),
	0x80249BF8: main.sym("L80249C28", flag={"GLOBL","LOCAL"}),
	0x80249C10: main.sym("L80249C40", flag={"GLOBL","LOCAL"}),
	0x80249C28: main.sym("L80249C58", flag={"GLOBL","LOCAL"}),
	0x80249C40: main.sym("L80249C70", flag={"GLOBL","LOCAL"}),
	0x80249C58: main.sym("L80249C88", flag={"GLOBL","LOCAL"}),
	0x80249C70: main.sym("L80249CA0", flag={"GLOBL","LOCAL"}),
	0x80249C88: main.sym("L80249CB8", flag={"GLOBL","LOCAL"}),
	0x80249CA8: main.sym("GmInitPort"),
	0x80249E74: main.sym("L80249EA4", flag={"GLOBL","LOCAL"}),
	0x80249E94: main.sym("L80249EC4", flag={"GLOBL","LOCAL"}),
	0x80249EB4: main.sym("L80249EE4", flag={"GLOBL","LOCAL"}),
	0x80249ED8: main.sym("L80249F08", flag={"GLOBL","LOCAL"}),
	0x80249EFC: main.sym("L80249F2C", flag={"GLOBL","LOCAL"}),
	0x80249F1C: main.sym("L80249F4C", flag={"GLOBL","LOCAL"}),
	0x80249F3C: main.sym("L80249F6C", flag={"GLOBL","LOCAL"}),
	0x8024A02C: main.sym("GmProcEntry"),
	0x8024A094: main.sym("GmInitStage"),
	0x8024A0E0: main.sym("GmInitStaff"),
	0x8024A27C: main.sym("GmProcConnect"),
	0x8024A48C: main.sym("GmIsSameBGM"),
	0x8024A594: main.sym("GmSetEntry"),
	0x8024A648: main.sym("GmGetBGPort"),
	0x8024A6F0: main.sym("GmProcBGPort"),
	0x8024A860: main.sym("PL_Fade", flag={"GLOBL"}),
	0x8024A8D8: main.sym("L8024AA44", flag={"GLOBL","LOCAL"}),
	0x8024A91C: main.sym("L8024AA88", flag={"GLOBL","LOCAL"}),
	0x8024A960: main.sym("L8024AACC", flag={"GLOBL","LOCAL"}),
	0x8024A9A0: main.sym("L8024AB0C", flag={"GLOBL","LOCAL"}),
	0x8024AA08: main.sym("L8024AB74", flag={"GLOBL","LOCAL"}),
	0x8024AA80: main.sym("L8024ABEC", flag={"GLOBL","LOCAL"}),
	0x8024AABC: main.sym("L8024AC3C", flag={"GLOBL","LOCAL"}),
	0x8024AB0C: main.sym("L8024AC8C", flag={"GLOBL","LOCAL"}),
	0x8024AB70: main.sym("L8024ACF0", flag={"GLOBL","LOCAL"}),
	0x8024ABE0: main.sym("L8024AD60", flag={"GLOBL","LOCAL"}),
	0x8024AC40: main.sym("L8024ADC0", flag={"GLOBL","LOCAL"}),
	0x8024AC6C: main.sym("L8024ADEC", flag={"GLOBL","LOCAL"}),
	0x8024ACE0: main.sym("L8024AE60", flag={"GLOBL","LOCAL"}),
	0x8024AD5C: main.sym("GmProcFade"),
	0x8024AE44: main.sym("L8024AFC4", flag={"GLOBL","LOCAL"}),
	0x8024AE5C: main.sym("L8024AFDC", flag={"GLOBL","LOCAL"}),
	0x8024AE78: main.sym("L8024AFF8", flag={"GLOBL","LOCAL"}),
	0x8024AE88: main.sym("L8024B008", flag={"GLOBL","LOCAL"}),
	0x8024AEBC: main.sym("L8024B03C", flag={"GLOBL","LOCAL"}),
	0x8024AFBC: main.sym("GmProcHUD"),
	0x8024B1F0: main.sym("GmSceneProc"),
	0x8024B244: main.sym("GmProcNormal"),
	0x8024B434: main.sym("GmProcPause"),
	0x8024B52C: main.sym("GmProcFrameAdv"),
	0x8024B5F8: main.sym("GmFreeze", flag={"GLOBL"}),
	0x8024B620: main.sym("GmProcFreeze"),
	0x8024B6E0: main.sym("GmProcExit"),
	0x8024B7A0: main.sym("GmProcExitOLD"),
	0x8024B818: main.sym("GmProc"),
	0x8024B84C: main.sym("L8024B9EC", flag={"GLOBL","LOCAL"}),
	0x8024B860: main.sym("L8024BA00", flag={"GLOBL","LOCAL"}),
	0x8024B874: main.sym("L8024BA14", flag={"GLOBL","LOCAL"}),
	0x8024B888: main.sym("L8024BA28", flag={"GLOBL","LOCAL"}),
	0x8024B89C: main.sym("L8024BA3C", flag={"GLOBL","LOCAL"}),
	0x8024B8B0: main.sym("L8024BA50", flag={"GLOBL","LOCAL"}),
	0x8024B8EC: main.sym("GmInit"),
	0x8024BB38: main.sym("GameProc", flag={"GLOBL"}),
	0x8024BBBC: main.sym("GameInit", flag={"GLOBL"}),
	0x8024BC74: main.sym("GameCheckSelect", flag={"GLOBL"}),
	0x8024BE00: main.sym("EndingSound", flag={"GLOBL"}),

	# src/collision.c
	0x8024BE50: main.sym("ObjGetCapFlag"),
	0x8024BF18: main.sym("PL_IsFacingObj"),
	0x8024BFCC: main.sym("PL_GetAngToObj", flag={"GLOBL"}),
	0x8024C038: main.sym("PL_CheckAttack"),
	0x8024C37C: main.sym("ObjAttack"),
	0x8024C3F0: main.sym("L8024C590", flag={"GLOBL","LOCAL"}),
	0x8024C400: main.sym("L8024C5A0", flag={"GLOBL","LOCAL"}),
	0x8024C410: main.sym("L8024C5B0", flag={"GLOBL","LOCAL"}),
	0x8024C420: main.sym("L8024C5C0", flag={"GLOBL","LOCAL"}),
	0x8024C450: main.sym("L8024C5F0", flag={"GLOBL","LOCAL"}),
	0x8024C478: main.sym("PL_StopRide", flag={"GLOBL"}),
	0x8024C4CC: main.sym("PL_TakeObject", flag={"GLOBL"}),
	0x8024C520: main.sym("PL_DropObject", flag={"GLOBL"}),
	0x8024C5E0: main.sym("PL_ThrowObject", flag={"GLOBL"}),
	0x8024C6F4: main.sym("PL_DropAll", flag={"GLOBL"}),
	0x8024C75C: main.sym("PL_IsWearingDefCap", flag={"GLOBL"}),
	0x8024C788: main.sym("PL_BlowCap", flag={"GLOBL"}),
	0x8024C8C8: main.sym("MarioStealCap", flag={"GLOBL"}),
	0x8024C958: main.sym("MarioReturnCap", flag={"GLOBL"}),
	0x8024C9B8: main.sym("PL_IsTaking"),
	0x8024CA5C: main.sym("PL_GetHitObj", flag={"GLOBL"}),
	0x8024CADC: main.sym("PL_CheckTaking", flag={"GLOBL"}),
	0x8024CC68: main.sym("PL_BumpObject"),
	0x8024CF14: main.sym("PL_Stomp"),
	0x8024CF90: main.sym("PL_HeadAttack"),
	0x8024CFCC: main.sym("PL_GetBlowState"),
	0x8024D11C: main.sym("PL_GetDamageState"),
	0x8024D3D8: main.sym("PL_RepelFromObj"),
	0x8024D58C: main.sym("PL_PunchKickRecoil"),
	0x8024D664: main.sym("PL_GetDoorCode"),
	0x8024D710: main.sym("PL_TakeDamage"),
	0x8024D7F8: main.sym("PL_CheckDamage"),
	0x8024D90C: main.sym("collision_8024DAAC"),
	0x8024D98C: main.sym("PL_CollideCoin"),
	0x8024DA50: main.sym("PL_CollideRecover"),
	0x8024DA88: main.sym("PL_CollideStar"),
	0x8024DCA4: main.sym("PL_CollideCage"),
	0x8024DD68: main.sym("PL_CollidePipe"),
	0x8024DF1C: main.sym("PL_CollidePortDoor"),
	0x8024E154: main.sym("PL_GetStarDoorFlag", flag={"GLOBL"}),
	0x8024E1E0: main.sym("L8024E388", flag={"GLOBL","LOCAL"}),
	0x8024E208: main.sym("L8024E3B0", flag={"GLOBL","LOCAL"}),
	0x8024E230: main.sym("L8024E3D8", flag={"GLOBL","LOCAL"}),
	0x8024E240: main.sym("L8024E3E8", flag={"GLOBL","LOCAL"}),
	0x8024E250: main.sym("L8024E3F8", flag={"GLOBL","LOCAL"}),
	0x8024E260: main.sym("L8024E408", flag={"GLOBL","LOCAL"}),
	0x8024E278: main.sym("PL_CollideDoor"),
	0x8024E3FC: main.sym("L8024E5A4", flag={"GLOBL","LOCAL"}),
	0x8024E40C: main.sym("L8024E5B4", flag={"GLOBL","LOCAL"}),
	0x8024E41C: main.sym("L8024E5C4", flag={"GLOBL","LOCAL"}),
	0x8024E42C: main.sym("L8024E5D4", flag={"GLOBL","LOCAL"}),
	0x8024E43C: main.sym("L8024E5E4", flag={"GLOBL","LOCAL"}),
	0x8024E44C: main.sym("L8024E5F4", flag={"GLOBL","LOCAL"}),
	0x8024E45C: main.sym("L8024E604", flag={"GLOBL","LOCAL"}),
	0x8024E544: main.sym("PL_CollideCannon"),
	0x8024E5D0: main.sym("PL_CollideIgloo"),
	0x8024E62C: main.sym("PL_CollideTornado"),
	0x8024E748: main.sym("PL_CollideWhirlpool"),
	0x8024E828: main.sym("PL_CollideWind"),
	0x8024E930: main.sym("PL_CollideBurn"),
	0x8024EAAC: main.sym("PL_CollideBullet"),
	0x8024EBDC: main.sym("PL_CollideClam"),
	0x8024EC9C: main.sym("PL_CollideBump"),
	0x8024EE50: main.sym("PL_CollideElecShock"),
	0x8024EF8C: main.sym("PL_CollideDummy"),
	0x8024EFC8: main.sym("PL_CollideEnemy"),
	0x8024F038: main.sym("PL_CollideFlyEnemy"),
	0x8024F194: main.sym("PL_CollideBounce"),
	0x8024F2D4: main.sym("PL_CollideSpiny"),
	0x8024F384: main.sym("PL_CollideDamage"),
	0x8024F3F4: main.sym("PL_CollideItemBox"),
	0x8024F4CC: main.sym("PL_CollideShell"),
	0x8024F5D0: main.sym("PL_CheckTaken"),
	0x8024F6E4: main.sym("PL_CollidePole"),
	0x8024F888: main.sym("PL_CollideHang"),
	0x8024F958: main.sym("PL_CollideCap"),
	0x8024FB54: main.sym("PL_CollideTake"),
	0x8024FC94: main.sym("PL_CanOpenMessage"),
	0x8024FD2C: main.sym("PL_CheckReading"),
	0x8024FEC0: main.sym("PL_CheckTalking"),
	0x8024FFC0: main.sym("PL_CollideMessage"),
	0x80250058: main.sym("PL_CheckPunchKickWall"),
	0x80250218: main.sym("PL_CheckCollision", flag={"GLOBL"}),
	0x802503F0: main.sym("PL_CheckFall"),
	0x80250484: main.sym("PL_GroundBurn"),
	0x8025054C: main.sym("PL_StartTimer"),
	0x802505A0: main.sym("PL_StopTimer"),
	0x80250624: main.sym("PL_CheckGroundCollision", flag={"GLOBL"}),

	# src/player.c
	0x80250770: main.sym("PL_IsAnimeLast1F", flag={"GLOBL"}),
	0x802507AC: main.sym("PL_IsAnimeLast2F", flag={"GLOBL"}),
	0x802507E8: main.sym("PL_SetAnime", flag={"GLOBL"}),
	0x80250934: main.sym("PL_SetAnimeV", flag={"GLOBL"}),
	0x80250AAC: main.sym("PL_SetAnimeFrame", flag={"GLOBL"}),
	0x80250B68: main.sym("PL_IsAnimeAtFrame", flag={"GLOBL"}),
	0x80250C84: main.sym("PL_GetAnimePos", flag={"GLOBL"}),
	0x80250E50: main.sym("PL_UseAnimePos", flag={"GLOBL"}),
	0x80250F0C: main.sym("PL_GetAnimeY", flag={"GLOBL"}),
	0x80250F50: main.sym("PL_TrigSound", flag={"GLOBL"}),
	0x80250FBC: main.sym("PL_TrigJumpVoice", flag={"GLOBL"}),
	0x80251048: main.sym("PL_SetSpeedEffect", flag={"GLOBL"}),
	0x802510E4: main.sym("PL_PlayEffect", flag={"GLOBL"}),
	0x80251218: main.sym("PL_TrigEffect", flag={"GLOBL"}),
	0x80251280: main.sym("PL_PlayLandEffect", flag={"GLOBL"}),
	0x802512E4: main.sym("PL_TrigLandEffect", flag={"GLOBL"}),
	0x80251348: main.sym("PL_PlayFallEffect", flag={"GLOBL"}),
	0x802513AC: main.sym("PL_TrigFallEffect", flag={"GLOBL"}),
	0x80251410: main.sym("PL_TrigJumpEffect", flag={"GLOBL"}),
	0x802514DC: main.sym("PL_SetSpeed", flag={"GLOBL"}),
	0x80251550: main.sym("PL_GetSlip", flag={"GLOBL"}),
	0x802515EC: main.sym("L80251818", flag={"GLOBL","LOCAL"}),
	0x802515FC: main.sym("L80251828", flag={"GLOBL","LOCAL"}),
	0x8025160C: main.sym("L80251838", flag={"GLOBL","LOCAL"}),
	0x8025161C: main.sym("L80251848", flag={"GLOBL","LOCAL"}),
	0x8025167C: main.sym("PL_GetSurface", flag={"GLOBL"}),
	0x8025177C: main.sym("L802519A8", flag={"GLOBL","LOCAL"}),
	0x80251788: main.sym("L802519B4", flag={"GLOBL","LOCAL"}),
	0x80251798: main.sym("L802519C4", flag={"GLOBL","LOCAL"}),
	0x802517A8: main.sym("L802519D4", flag={"GLOBL","LOCAL"}),
	0x802517B8: main.sym("L802519E4", flag={"GLOBL","LOCAL"}),
	0x802517C8: main.sym("L802519F4", flag={"GLOBL","LOCAL"}),
	0x8025181C: main.sym("PL_CheckWall", flag={"GLOBL"}),
	0x802518D0: main.sym("PL_CheckRoof", flag={"GLOBL"}),
	0x80251928: main.sym("PL_IsFaceDownSlope", flag={"GLOBL"}),
	0x802519A8: main.sym("PL_IsSlipMin", flag={"GLOBL"}),
	0x80251AD0: main.sym("PL_IsSlipMax", flag={"GLOBL"}),
	0x80251BF8: main.sym("PL_IsSlipJump"),
	0x80251CF8: main.sym("PL_CheckGroundYNear", flag={"GLOBL"}),
	0x80251DD4: main.sym("PL_GetGroundAngX", flag={"GLOBL"}),
	0x80251F74: main.sym("player_802521A0", flag={"GLOBL"}),
	0x80252070: main.sym("PL_SetSlipJump"),
	0x8025219C: main.sym("PL_SetJumpSpeed"),
	0x80252234: main.sym("PL_SetJump"),
	0x802523E0: main.sym("L8025260C", flag={"GLOBL","LOCAL"}),
	0x80252478: main.sym("L802526A4", flag={"GLOBL","LOCAL"}),
	0x802524F4: main.sym("L80252720", flag={"GLOBL","LOCAL"}),
	0x80252534: main.sym("L80252760", flag={"GLOBL","LOCAL"}),
	0x802525B8: main.sym("L802527E4", flag={"GLOBL","LOCAL"}),
	0x8025266C: main.sym("L80252898", flag={"GLOBL","LOCAL"}),
	0x80252778: main.sym("L802529A4", flag={"GLOBL","LOCAL"}),
	0x802527B8: main.sym("PL_SetMove"),
	0x802529A8: main.sym("PL_SetSwim"),
	0x802529EC: main.sym("PL_SetDemo"),
	0x80252AC8: main.sym("PL_SetState", flag={"GLOBL"}),
	0x80252C30: main.sym("PL_SetTripJump", flag={"GLOBL"}),
	0x80252E74: main.sym("PL_SetStateJump", flag={"GLOBL"}),
	0x80252F4C: main.sym("PL_SetStateDrop", flag={"GLOBL"}),
	0x80252F98: main.sym("PL_SetStateDamage", flag={"GLOBL"}),
	0x80252FEC: main.sym("PL_CheckMotion", flag={"GLOBL"}),
	0x802530D4: main.sym("PL_CheckMotionTake", flag={"GLOBL"}),
	0x802531B8: main.sym("PL_EnterField", flag={"GLOBL"}),
	0x8025325C: main.sym("PL_EnterWater", flag={"GLOBL"}),
	0x8025335C: main.sym("PL_ProcPress"),
	0x802534F4: main.sym("PL_ProcDebug"),
	0x8025360C: main.sym("PL_ProcButton"),
	0x80253730: main.sym("PL_ProcStick"),
	0x80253834: main.sym("PL_ProcBG"),
	0x80253B2C: main.sym("PL_ProcStatus"),
	0x80253C94: main.sym("PL_ProcSwimCamera"),
	0x80253E34: main.sym("PL_ProcPower"),
	0x80254088: main.sym("PL_ProcInfo"),
	0x8025410C: main.sym("PL_InitShape"),
	0x80254164: main.sym("PL_ProcSink"),
	0x802541BC: main.sym("PL_ProcCap"),
	0x8025435C: main.sym("PL_ProcShape"),
	0x8025453C: main.sym("DebugCap"),
	0x80254604: main.sym("MarioExec", flag={"GLOBL"}),
	0x802548BC: main.sym("MarioEnter", flag={"GLOBL"}),
	0x80254CE0: main.sym("MarioInit", flag={"GLOBL"}),

	# src/physics.c
	0x80254E20: main.sym("PL_GetTrampolinePower", flag={"GLOBL"}),
	0x80254E3C: main.sym("PL_ProcTrampoline", flag={"GLOBL"}),
	0x80254E50: main.sym("TrampolineProc", flag={"GLOBL"}),
	0x80254E60: main.sym("BumpCollision", flag={"GLOBL"}),
	0x80254FD8: main.sym("BumpInit", flag={"GLOBL"}),
	0x8025509C: main.sym("PL_Reflect", flag={"GLOBL"}),
	0x802551B4: main.sym("PL_Sink", flag={"GLOBL"}),
	0x80255250: main.sym("L802554B0", flag={"GLOBL","LOCAL"}),
	0x8025529C: main.sym("L802554FC", flag={"GLOBL","LOCAL"}),
	0x802552E8: main.sym("L80255548", flag={"GLOBL","LOCAL"}),
	0x80255334: main.sym("L80255594", flag={"GLOBL","LOCAL"}),
	0x80255394: main.sym("L802555F4", flag={"GLOBL","LOCAL"}),
	0x802553C0: main.sym("L80255620", flag={"GLOBL","LOCAL"}),
	0x802553F4: main.sym("PL_SteepFall", flag={"GLOBL"}),
	0x802554AC: main.sym("PL_ProcQuicksand", flag={"GLOBL"}),
	0x802555AC: main.sym("PL_ProcWind", flag={"GLOBL"}),
	0x80255788: main.sym("PL_Stop", flag={"GLOBL"}),
	0x8025580C: main.sym("PL_ProcWait", flag={"GLOBL"}),
	0x802558DC: main.sym("PL_CheckWalk"),
	0x80255B60: main.sym("PL_ProcWalk", flag={"GLOBL"}),
	0x80255C9C: main.sym("PL_CheckLedge"),
	0x80255E84: main.sym("PL_CheckJump"),
	0x802562B8: main.sym("PL_ProcSpinGravity"),
	0x8025635C: main.sym("PL_IsJumpCancel"),
	0x802563F4: main.sym("PL_ProcGravity"),
	0x802567D0: main.sym("PL_ProcUpWind"),
	0x80256940: main.sym("PL_ProcJump", flag={"GLOBL"}),
	0x80256AF4: main.sym("PL_SetSpeed3D"),
	0x80256BA8: main.sym("PL_SetSpeed2D"),

	# src/pldemo.c
	0x80256C20: main.sym("pldemo_80256E00"),
	0x80256CA8: main.sym("StaffDraw", flag={"GLOBL"}),
	0x80256DE8: main.sym("pldemo_80257060", flag={"GLOBL"}),
	0x80256E64: main.sym("pldemo_802570DC", flag={"GLOBL"}),
	0x80256F20: main.sym("Ctrl_pldemo_80257198", flag={"GLOBL"}),
	0x80256FF8: main.sym("pldemo_80257270"),
	0x80257038: main.sym("pldemo_802572B0"),
	0x802570C4: main.sym("pldemo_8025733C"),
	0x802571D8: main.sym("pldemo_80257450"),
	0x80257270: main.sym("pldemo_802574E8"),
	0x802572D0: main.sym("pldemo_80257548"),
	0x80257330: main.sym("pldemo_802575A8", flag={"GLOBL"}),
	0x802573C8: main.sym("pldemo_80257640", flag={"GLOBL"}),
	0x802574D0: main.sym("pldemo_80257748"),
	0x80257708: main.sym("pldemo_80257980"),
	0x80257794: main.sym("pldemo_80257A0C"),
	0x80257838: main.sym("pldemo_80257AB0"),
	0x80257A6C: main.sym("pldemo_80257CE4"),
	0x80257C34: main.sym("pldemo_80257EAC"),
	0x80257F0C: main.sym("pldemo_80258184"),
	0x802581A8: main.sym("pldemo_80258420"),
	0x80258264: main.sym("pldemo_802584DC"),
	0x80258348: main.sym("pldemo_802585C0"),
	0x80258454: main.sym("pldemo_802586CC"),
	0x802584CC: main.sym("pldemo_80258744"),
	0x80258574: main.sym("pldemo_802587EC"),
	0x802585C4: main.sym("pldemo_8025883C"),
	0x80258614: main.sym("pldemo_8025888C"),
	0x80258680: main.sym("pldemo_802588F8"),
	0x802586EC: main.sym("pldemo_80258964"),
	0x80258804: main.sym("pldemo_80258A7C"),
	0x802588AC: main.sym("pldemo_80258B24"),
	0x80258930: main.sym("pldemo_80258BA8"),
	0x80258B34: main.sym("pldemo_80258DAC"),
	0x80258D1C: main.sym("pldemo_80258F94"),
	0x80258FEC: main.sym("pldemo_80259264"),
	0x80259154: main.sym("pldemo_802593CC"),
	0x8025925C: main.sym("pldemo_802594D4"),
	0x80259390: main.sym("pldemo_80259608"),
	0x802594C8: main.sym("pldemo_80259740"),
	0x80259534: main.sym("pldemo_802597AC"),
	0x802595DC: main.sym("pldemo_80259854"),
	0x80259658: main.sym("pldemo_802598D0"),
	0x802599B8: main.sym("pldemo_80259C30"),
	0x80259A70: main.sym("pldemo_80259CE8"),
	0x80259AFC: main.sym("pldemo_80259D74"),
	0x80259B88: main.sym("pldemo_80259E00"),
	0x80259C80: main.sym("pldemo_80259EF8"),
	0x80259D54: main.sym("pldemo_80259FCC"),
	0x80259DC8: main.sym("pldemo_8025A040"),
	0x80259E44: main.sym("pldemo_8025A0BC"),
	0x80259F34: main.sym("L8025A1AC", flag={"GLOBL","LOCAL"}),
	0x80259FCC: main.sym("L8025A244", flag={"GLOBL","LOCAL"}),
	0x8025A068: main.sym("L8025A2E0", flag={"GLOBL","LOCAL"}),
	0x8025A1D8: main.sym("L8025A450", flag={"GLOBL","LOCAL"}),
	0x8025A21C: main.sym("pldemo_8025A494"),
	0x8025A398: main.sym("pldemo_8025A610"),
	0x8025A484: main.sym("pldemo_8025A6FC"),
	0x8025A5E0: main.sym("pldemo_8025A858"),
	0x8025A734: main.sym("pldemo_8025A9AC"),
	0x8025AB94: main.sym("pldemo_8025AE0C"),
	0x8025AC30: main.sym("pldemo_8025AEA8"),
	0x8025AD84: main.sym("pldemo_8025AFFC"),
	0x8025ADD8: main.sym("pldemo_8025B050"),
	0x8025AE2C: main.sym("pldemo_8025B0A4"),
	0x8025AE80: main.sym("pldemo_8025B0F8"),
	0x8025AEA4: main.sym("pldemo_8025B11C"),
	0x8025AF00: main.sym("pldemo_8025B178"),
	0x8025AFBC: main.sym("pldemo_8025B234"),
	0x8025B074: main.sym("pldemo_8025B2EC"),
	0x8025B160: main.sym("pldemo_8025B404"),
	0x8025B1B0: main.sym("pldemo_8025B454"),
	0x8025B27C: main.sym("pldemo_8025B520"),
	0x8025B2E8: main.sym("pldemo_8025B58C"),
	0x8025B320: main.sym("L8025B5C4", flag={"GLOBL","LOCAL"}),
	0x8025B330: main.sym("L8025B5D4", flag={"GLOBL","LOCAL"}),
	0x8025B340: main.sym("L8025B5E4", flag={"GLOBL","LOCAL"}),
	0x8025B350: main.sym("L8025B5F4", flag={"GLOBL","LOCAL"}),
	0x8025B360: main.sym("L8025B604", flag={"GLOBL","LOCAL"}),
	0x8025B370: main.sym("L8025B614", flag={"GLOBL","LOCAL"}),
	0x8025B380: main.sym("L8025B624", flag={"GLOBL","LOCAL"}),
	0x8025B3B0: main.sym("pldemo_8025B654"),
	0x8025B4BC: main.sym("pldemo_8025B760"),
	0x8025B704: main.sym("pldemo_8025B9A8"),
	0x8025B948: main.sym("pldemo_8025BBEC"),
	0x8025B9DC: main.sym("pldemo_8025BC80"),
	0x8025BC14: main.sym("pldemo_8025BEB8"),
	0x8025BCC0: main.sym("pldemo_8025BF64"),
	0x8025BD70: main.sym("pldemo_8025C014"),
	0x8025BE20: main.sym("pldemo_8025C0C4"),
	0x8025BF1C: main.sym("pldemo_8025C1C0"),
	0x8025C1F4: main.sym("pldemo_8025C498"),
	0x8025C35C: main.sym("pldemo_8025C600"),
	0x8025C454: main.sym("pldemo_8025C6F8"),
	0x8025C620: main.sym("pldemo_8025C904"),
	0x8025C71C: main.sym("pldemo_8025CA48"),
	0x8025C8B0: main.sym("pldemo_8025CBDC"),
	0x8025CA34: main.sym("pldemo_8025CD6C"),
	0x8025CB88: main.sym("pldemo_8025CEF0"),
	0x8025CC64: main.sym("pldemo_8025CFE4"),
	0x8025CCC0: main.sym("pldemo_8025D040"),
	0x8025CCF8: main.sym("L8025D078", flag={"GLOBL","LOCAL"}),
	0x8025CD08: main.sym("L8025D088", flag={"GLOBL","LOCAL"}),
	0x8025CD18: main.sym("L8025D098", flag={"GLOBL","LOCAL"}),
	0x8025CD28: main.sym("L8025D0A8", flag={"GLOBL","LOCAL"}),
	0x8025CD38: main.sym("L8025D0B8", flag={"GLOBL","LOCAL"}),
	0x8025CD48: main.sym("L8025D0C8", flag={"GLOBL","LOCAL"}),
	0x8025CD58: main.sym("L8025D0D8", flag={"GLOBL","LOCAL"}),
	0x8025CD68: main.sym("L8025D0E8", flag={"GLOBL","LOCAL"}),
	0x8025CD78: main.sym("L8025D0F8", flag={"GLOBL","LOCAL"}),
	0x8025CD88: main.sym("L8025D108", flag={"GLOBL","LOCAL"}),
	0x8025CD98: main.sym("L8025D118", flag={"GLOBL","LOCAL"}),
	0x8025CDA8: main.sym("L8025D128", flag={"GLOBL","LOCAL"}),
	0x8025CDB8: main.sym("L8025D138", flag={"GLOBL","LOCAL"}),
	0x8025CE54: main.sym("pldemo_8025D1D4"),
	0x8025D170: main.sym("pldemo_8025D4F0"),
	0x8025D38C: main.sym("pldemo_8025D70C"),
	0x8025D418: main.sym("PL_ExecDemo", flag={"GLOBL"}),
	0x8025D5AC: main.sym("L8025D92C", flag={"GLOBL","LOCAL"}),
	0x8025D5D4: main.sym("L8025D954", flag={"GLOBL","LOCAL"}),
	0x8025D5E8: main.sym("L8025D968", flag={"GLOBL","LOCAL"}),
	0x8025D5FC: main.sym("L8025D97C", flag={"GLOBL","LOCAL"}),
	0x8025D610: main.sym("L8025D990", flag={"GLOBL","LOCAL"}),
	0x8025D64C: main.sym("L8025D9CC", flag={"GLOBL","LOCAL"}),
	0x8025D660: main.sym("L8025D9E0", flag={"GLOBL","LOCAL"}),
	0x8025D674: main.sym("L8025D9F4", flag={"GLOBL","LOCAL"}),
	0x8025D688: main.sym("L8025DA08", flag={"GLOBL","LOCAL"}),
	0x8025D69C: main.sym("L8025DA1C", flag={"GLOBL","LOCAL"}),
	0x8025D6B0: main.sym("L8025DA30", flag={"GLOBL","LOCAL"}),
	0x8025D6C4: main.sym("L8025DA44", flag={"GLOBL","LOCAL"}),
	0x8025D6D8: main.sym("L8025DA58", flag={"GLOBL","LOCAL"}),
	0x8025D6EC: main.sym("L8025DA6C", flag={"GLOBL","LOCAL"}),
	0x8025D700: main.sym("L8025DA80", flag={"GLOBL","LOCAL"}),
	0x8025D714: main.sym("L8025DA94", flag={"GLOBL","LOCAL"}),
	0x8025D728: main.sym("L8025DAA8", flag={"GLOBL","LOCAL"}),
	0x8025D73C: main.sym("L8025DABC", flag={"GLOBL","LOCAL"}),
	0x8025D750: main.sym("L8025DAD0", flag={"GLOBL","LOCAL"}),
	0x8025D764: main.sym("L8025DAE4", flag={"GLOBL","LOCAL"}),
	0x8025D778: main.sym("L8025DAF8", flag={"GLOBL","LOCAL"}),
	0x8025D78C: main.sym("L8025DB0C", flag={"GLOBL","LOCAL"}),
	0x8025D7A0: main.sym("L8025DB20", flag={"GLOBL","LOCAL"}),
	0x8025D7B4: main.sym("L8025DB34", flag={"GLOBL","LOCAL"}),
	0x8025D7C8: main.sym("L8025DB48", flag={"GLOBL","LOCAL"}),
	0x8025D7DC: main.sym("L8025DB5C", flag={"GLOBL","LOCAL"}),
	0x8025D7F0: main.sym("L8025DB70", flag={"GLOBL","LOCAL"}),
	0x8025D804: main.sym("L8025DB84", flag={"GLOBL","LOCAL"}),
	0x8025D818: main.sym("L8025DB98", flag={"GLOBL","LOCAL"}),
	0x8025D82C: main.sym("L8025DBAC", flag={"GLOBL","LOCAL"}),
	0x8025D840: main.sym("L8025DBC0", flag={"GLOBL","LOCAL"}),
	0x8025D854: main.sym("L8025DBD4", flag={"GLOBL","LOCAL"}),
	0x8025D868: main.sym("L8025DBE8", flag={"GLOBL","LOCAL"}),
	0x8025D87C: main.sym("L8025DBFC", flag={"GLOBL","LOCAL"}),
	0x8025D890: main.sym("L8025DC10", flag={"GLOBL","LOCAL"}),
	0x8025D8A4: main.sym("L8025DC24", flag={"GLOBL","LOCAL"}),
	0x8025D8B8: main.sym("L8025DC38", flag={"GLOBL","LOCAL"}),
	0x8025D8CC: main.sym("L8025DC4C", flag={"GLOBL","LOCAL"}),
	0x8025D8F4: main.sym("L8025DC74", flag={"GLOBL","LOCAL"}),
	0x8025D908: main.sym("L8025DC88", flag={"GLOBL","LOCAL"}),
	0x8025D91C: main.sym("L8025DC9C", flag={"GLOBL","LOCAL"}),
	0x8025D930: main.sym("L8025DCB0", flag={"GLOBL","LOCAL"}),
	0x8025D944: main.sym("L8025DCC4", flag={"GLOBL","LOCAL"}),
	0x8025D958: main.sym("L8025DCD8", flag={"GLOBL","LOCAL"}),
	0x8025D96C: main.sym("L8025DCEC", flag={"GLOBL","LOCAL"}),
	0x8025D980: main.sym("L8025DD00", flag={"GLOBL","LOCAL"}),
	0x8025D994: main.sym("L8025DD14", flag={"GLOBL","LOCAL"}),

	# src/plspec.c
	0x8025D9F0: main.sym("plspec_8025DD70"),
	0x8025DA9C: main.sym("plspec_8025DE1C"),
	0x8025DB84: main.sym("plspec_8025DF04"),
	0x8025DE9C: main.sym("plspec_8025E21C"),
	0x8025E218: main.sym("plspec_8025E5A8"),
	0x8025E3CC: main.sym("plspec_8025E7A4"),
	0x8025E458: main.sym("plspec_8025E830"),
	0x8025E558: main.sym("plspec_8025E930"),
	0x8025E658: main.sym("plspec_8025EA30"),
	0x8025E778: main.sym("plspec_8025EB50"),
	0x8025E924: main.sym("plspec_8025ECFC"),
	0x8025EAF8: main.sym("plspec_8025EED0"),
	0x8025EB80: main.sym("plspec_8025EF58"),
	0x8025ECDC: main.sym("plspec_8025F0B4"),
	0x8025EE0C: main.sym("plspec_8025F1E4"),
	0x8025EFAC: main.sym("plspec_8025F384"),
	0x8025F0DC: main.sym("plspec_8025F4B4"),
	0x8025F188: main.sym("plspec_8025F560"),
	0x8025F26C: main.sym("plspec_8025F644"),
	0x8025F2E8: main.sym("plspec_8025F6C0"),
	0x8025F598: main.sym("plspec_8025F970"),
	0x8025F68C: main.sym("plspec_8025FA64"),
	0x8025F710: main.sym("plspec_8025FAE8"),
	0x8025F7B8: main.sym("plspec_8025FB90"),
	0x8025F894: main.sym("plspec_8025FC6C"),
	0x8025FD7C: main.sym("plspec_80260154"),
	0x80260190: main.sym("plspec_80260568"),
	0x802601F8: main.sym("PL_ExecSpec", flag={"GLOBL"}),
	0x80260370: main.sym("L80260748", flag={"GLOBL","LOCAL"}),
	0x80260384: main.sym("L8026075C", flag={"GLOBL","LOCAL"}),
	0x80260398: main.sym("L80260770", flag={"GLOBL","LOCAL"}),
	0x802603AC: main.sym("L80260784", flag={"GLOBL","LOCAL"}),
	0x802603C0: main.sym("L80260798", flag={"GLOBL","LOCAL"}),

	# src/plwait.c
	0x802604E0: main.sym("plwait_802608B0"),
	0x802606DC: main.sym("plwait_80260AAC"),
	0x802608E4: main.sym("plwait_80260CB4"),
	0x80260BC4: main.sym("plwait_80260F94"),
	0x80260C30: main.sym("plwait_80261000"),
	0x80260E38: main.sym("plwait_80261268"),
	0x80261108: main.sym("plwait_802614FC"),
	0x80261280: main.sym("plwait_8026168C"),
	0x802614CC: main.sym("plwait_802618D8"),
	0x802615C4: main.sym("plwait_802619D0"),
	0x802616C4: main.sym("plwait_80261AD0"),
	0x802617EC: main.sym("plwait_80261BF8"),
	0x802618E0: main.sym("plwait_80261CEC"),
	0x802619A8: main.sym("plwait_80261DB4"),
	0x80261B64: main.sym("plwait_80261F70"),
	0x80261C74: main.sym("plwait_80262080"),
	0x80261D70: main.sym("plwait_8026217C"),
	0x80261DD0: main.sym("plwait_802621DC"),
	0x80261ED0: main.sym("plwait_802622DC"),
	0x80261F8C: main.sym("plwait_80262398"),
	0x80262084: main.sym("plwait_80262490"),
	0x80262124: main.sym("plwait_80262530"),
	0x80262244: main.sym("plwait_80262650"),
	0x80262364: main.sym("plwait_80262770"),
	0x80262484: main.sym("plwait_80262890"),
	0x80262574: main.sym("plwait_80262980"),
	0x802627B8: main.sym("plwait_80262BC4"),
	0x80262828: main.sym("plwait_80262C34"),
	0x8026295C: main.sym("plwait_80262D68"),
	0x802629B8: main.sym("plwait_80262DC4"),
	0x80262A14: main.sym("plwait_80262E20"),
	0x80262A88: main.sym("plwait_80262E94"),
	0x80262AE4: main.sym("plwait_80262EF0"),
	0x80262B44: main.sym("plwait_80262F50"),
	0x80262BE0: main.sym("plwait_80262FEC"),
	0x80262C50: main.sym("plwait_8026305C"),
	0x80262CEC: main.sym("plwait_802630F8"),
	0x80262DE4: main.sym("plwait_802631F0"),
	0x80262EDC: main.sym("plwait_802632E8"),
	0x80262FA8: main.sym("plwait_802633B4"),
	0x80263100: main.sym("plwait_8026350C"),
	0x802631DC: main.sym("plwait_802635E8"),
	0x80263378: main.sym("plwait_80263784"),
	0x8026348C: main.sym("PL_ExecWait", flag={"GLOBL"}),
	0x8026372C: main.sym("L80263B38", flag={"GLOBL","LOCAL"}),
	0x80263740: main.sym("L80263B4C", flag={"GLOBL","LOCAL"}),
	0x8026377C: main.sym("L80263B88", flag={"GLOBL","LOCAL"}),
	0x802637E0: main.sym("L80263BEC", flag={"GLOBL","LOCAL"}),
	0x802637F4: main.sym("L80263C00", flag={"GLOBL","LOCAL"}),
	0x80263808: main.sym("L80263C14", flag={"GLOBL","LOCAL"}),
	0x8026381C: main.sym("L80263C28", flag={"GLOBL","LOCAL"}),
	0x80263830: main.sym("L80263C3C", flag={"GLOBL","LOCAL"}),
	0x80263844: main.sym("L80263C50", flag={"GLOBL","LOCAL"}),
	0x80263858: main.sym("L80263C64", flag={"GLOBL","LOCAL"}),
	0x8026386C: main.sym("L80263C78", flag={"GLOBL","LOCAL"}),
	0x80263880: main.sym("L80263C8C", flag={"GLOBL","LOCAL"}),
	0x802638A8: main.sym("L80263CB4", flag={"GLOBL","LOCAL"}),
	0x802638BC: main.sym("L80263CC8", flag={"GLOBL","LOCAL"}),
	0x802638D0: main.sym("L80263CDC", flag={"GLOBL","LOCAL"}),
	0x802638E4: main.sym("L80263CF0", flag={"GLOBL","LOCAL"}),
	0x802638F8: main.sym("L80263D04", flag={"GLOBL","LOCAL"}),
	0x8026390C: main.sym("L80263D18", flag={"GLOBL","LOCAL"}),
	0x80263920: main.sym("L80263D2C", flag={"GLOBL","LOCAL"}),
	0x80263948: main.sym("L80263D54", flag={"GLOBL","LOCAL"}),
	0x80263970: main.sym("L80263D7C", flag={"GLOBL","LOCAL"}),
	0x80263984: main.sym("L80263D90", flag={"GLOBL","LOCAL"}),
	0x80263998: main.sym("L80263DA4", flag={"GLOBL","LOCAL"}),
	0x802639C0: main.sym("L80263DCC", flag={"GLOBL","LOCAL"}),
	0x802639D4: main.sym("L80263DE0", flag={"GLOBL","LOCAL"}),
	0x802639FC: main.sym("L80263E08", flag={"GLOBL","LOCAL"}),

	# src/plmove.c
	0x80263A50: main.sym("plmove_80263E60"),
	0x80263AD4: main.sym("plmove_80263EE4", flag={"GLOBL"}),
	0x80263C14: main.sym("plmove_80264024"),
	0x80263C8C: main.sym("plmove_8026409C"),
	0x80263CEC: main.sym("plmove_802640FC"),
	0x80263EA4: main.sym("plmove_802642B4"),
	0x80263F30: main.sym("plmove_80264340"),
	0x80263FFC: main.sym("plmove_8026440C"),
	0x80264330: main.sym("plmove_80264740"),
	0x80264744: main.sym("plmove_80264B54"),
	0x80264970: main.sym("plmove_80264D80"),
	0x80264A08: main.sym("plmove_80264E18"),
	0x80264C70: main.sym("plmove_80265080"),
	0x80264DA0: main.sym("plmove_802651B0"),
	0x80264E34: main.sym("plmove_80265244"),
	0x80265048: main.sym("plmove_80265458"),
	0x80265104: main.sym("plmove_80265514"),
	0x80265148: main.sym("plmove_80265558"),
	0x80265210: main.sym("plmove_80265620"),
	0x802652F0: main.sym("plmove_80265700"),
	0x8026570C: main.sym("plmove_80265B1C"),
	0x80265980: main.sym("plmove_80265D90"),
	0x802659E8: main.sym("plmove_80265DF8"),
	0x80265C28: main.sym("plmove_80266038"),
	0x80265DBC: main.sym("plmove_802661CC"),
	0x80265F44: main.sym("plmove_80266354"),
	0x802661A4: main.sym("plmove_802665B4"),
	0x80266324: main.sym("plmove_80266734"),
	0x8026658C: main.sym("plmove_8026699C"),
	0x802666E8: main.sym("plmove_80266AF8"),
	0x8026693C: main.sym("plmove_80266D4C"),
	0x80266A38: main.sym("plmove_80266E48"),
	0x80266BB8: main.sym("plmove_80266FC8"),
	0x80266E30: main.sym("plmove_80267240"),
	0x802670F4: main.sym("plmove_80267504"),
	0x80267318: main.sym("plmove_80267728"),
	0x8026754C: main.sym("plmove_8026795C"),
	0x80267814: main.sym("plmove_80267C24"),
	0x802678D4: main.sym("plmove_80267CE4"),
	0x80267B74: main.sym("plmove_80267FA4"),
	0x80267C44: main.sym("plmove_80268074"),
	0x80267CA4: main.sym("plmove_802680D4"),
	0x80267D38: main.sym("plmove_80268168"),
	0x80267F08: main.sym("plmove_80268338"),
	0x8026807C: main.sym("plmove_802684AC"),
	0x80268190: main.sym("plmove_802685C0"),
	0x802681D8: main.sym("plmove_80268608"),
	0x80268254: main.sym("plmove_80268684"),
	0x80268388: main.sym("plmove_802687B8"),
	0x802685C8: main.sym("plmove_802689F8"),
	0x80268670: main.sym("plmove_80268ADC"),
	0x802686F8: main.sym("plmove_80268B64"),
	0x80268744: main.sym("plmove_80268BB0"),
	0x80268790: main.sym("plmove_80268BFC"),
	0x802687DC: main.sym("plmove_80268C48"),
	0x80268828: main.sym("plmove_80268C94"),
	0x80268898: main.sym("plmove_80268D04"),
	0x80268960: main.sym("plmove_80268DCC"),
	0x80268B0C: main.sym("plmove_80268F78"),
	0x80268C9C: main.sym("plmove_80269108"),
	0x80268D04: main.sym("plmove_80269170"),
	0x80268D6C: main.sym("plmove_802691D8"),
	0x80268DF8: main.sym("plmove_80269264"),
	0x80268E94: main.sym("plmove_80269300"),
	0x80268F30: main.sym("plmove_8026939C"),
	0x80269010: main.sym("plmove_8026947C"),
	0x80269078: main.sym("plmove_802694E4"),
	0x8026911C: main.sym("plmove_80269588"),
	0x802691D4: main.sym("plmove_80269640"),
	0x8026931C: main.sym("plmove_80269788"),
	0x80269370: main.sym("plmove_802697DC"),
	0x802693C4: main.sym("plmove_80269830"),
	0x802694E8: main.sym("PL_ExecMove", flag={"GLOBL"}),
	0x80269780: main.sym("L80269BEC", flag={"GLOBL","LOCAL"}),
	0x80269794: main.sym("L80269C00", flag={"GLOBL","LOCAL"}),
	0x802697A8: main.sym("L80269C14", flag={"GLOBL","LOCAL"}),
	0x802697BC: main.sym("L80269C28", flag={"GLOBL","LOCAL"}),
	0x8026980C: main.sym("L80269C78", flag={"GLOBL","LOCAL"}),
	0x80269834: main.sym("L80269CA0", flag={"GLOBL","LOCAL"}),
	0x802698E8: main.sym("L80269D54", flag={"GLOBL","LOCAL"}),
	0x802698FC: main.sym("L80269D68", flag={"GLOBL","LOCAL"}),
	0x80269910: main.sym("L80269D7C", flag={"GLOBL","LOCAL"}),
	0x80269924: main.sym("L80269D90", flag={"GLOBL","LOCAL"}),
	0x80269938: main.sym("L80269DA4", flag={"GLOBL","LOCAL"}),
	0x8026994C: main.sym("L80269DB8", flag={"GLOBL","LOCAL"}),
	0x80269960: main.sym("L80269DCC", flag={"GLOBL","LOCAL"}),
	0x80269974: main.sym("L80269DE0", flag={"GLOBL","LOCAL"}),
	0x80269988: main.sym("L80269DF4", flag={"GLOBL","LOCAL"}),
	0x8026999C: main.sym("L80269E08", flag={"GLOBL","LOCAL"}),
	0x802699B0: main.sym("L80269E1C", flag={"GLOBL","LOCAL"}),
	0x802699C4: main.sym("L80269E30", flag={"GLOBL","LOCAL"}),
	0x802699D8: main.sym("L80269E44", flag={"GLOBL","LOCAL"}),
	0x802699EC: main.sym("L80269E58", flag={"GLOBL","LOCAL"}),
	0x80269A00: main.sym("L80269E6C", flag={"GLOBL","LOCAL"}),
	0x80269A14: main.sym("L80269E80", flag={"GLOBL","LOCAL"}),
	0x80269A28: main.sym("L80269E94", flag={"GLOBL","LOCAL"}),
	0x80269A3C: main.sym("L80269EA8", flag={"GLOBL","LOCAL"}),
	0x80269A50: main.sym("L80269EBC", flag={"GLOBL","LOCAL"}),
	0x80269A64: main.sym("L80269ED0", flag={"GLOBL","LOCAL"}),

	# src/pljump.c
	0x80269AD0: main.sym("pljump_80269F40"),
	0x80269B50: main.sym("pljump_80269FC0"),
	0x80269C20: main.sym("pljump_8026A12C"),
	0x80269D18: main.sym("pljump_8026A224"),
	0x80269EF4: main.sym("pljump_8026A400"),
	0x80269F88: main.sym("pljump_8026A494"),
	0x8026A08C: main.sym("pljump_8026A598"),
	0x8026A120: main.sym("pljump_8026A62C"),
	0x8026A324: main.sym("pljump_8026A818"),
	0x8026A554: main.sym("pljump_8026AA48"),
	0x8026A7E4: main.sym("pljump_8026ACD8"),
	0x8026A968: main.sym("pljump_8026AE5C"),
	0x8026AB10: main.sym("pljump_8026B004"),
	0x8026AC88: main.sym("pljump_8026B17C"),
	0x8026AF50: main.sym("pljump_8026B444"),
	0x8026AFA8: main.sym("L8026B49C", flag={"GLOBL","LOCAL"}),
	0x8026AFBC: main.sym("L8026B4B0", flag={"GLOBL","LOCAL"}),
	0x8026AFEC: main.sym("L8026B4E0", flag={"GLOBL","LOCAL"}),
	0x8026B138: main.sym("L8026B62C", flag={"GLOBL","LOCAL"}),
	0x8026B160: main.sym("L8026B654", flag={"GLOBL","LOCAL"}),
	0x8026B17C: main.sym("L8026B670", flag={"GLOBL","LOCAL"}),
	0x8026B18C: main.sym("L8026B680", flag={"GLOBL","LOCAL"}),
	0x8026B1AC: main.sym("pljump_8026B6A0"),
	0x8026B24C: main.sym("pljump_8026B740"),
	0x8026B320: main.sym("pljump_8026B814"),
	0x8026B41C: main.sym("pljump_8026B90C"),
	0x8026B4BC: main.sym("pljump_8026B9AC"),
	0x8026B5C8: main.sym("pljump_8026BAB8"),
	0x8026B6C4: main.sym("pljump_8026BBB4"),
	0x8026B7D0: main.sym("pljump_8026BCC0"),
	0x8026B8DC: main.sym("pljump_8026BDCC"),
	0x8026B988: main.sym("pljump_8026BE78"),
	0x8026BA50: main.sym("pljump_8026BF40"),
	0x8026BB44: main.sym("pljump_8026C034"),
	0x8026BCF0: main.sym("pljump_8026C1E0"),
	0x8026BFC8: main.sym("pljump_8026C4B8"),
	0x8026C0E0: main.sym("pljump_8026C5D0"),
	0x8026C23C: main.sym("pljump_8026C738"),
	0x8026C384: main.sym("pljump_8026C880"),
	0x8026C500: main.sym("pljump_8026C9FC"),
	0x8026C810: main.sym("pljump_8026CD0C"),
	0x8026C954: main.sym("pljump_8026CE50"),
	0x8026CA2C: main.sym("pljump_8026CF28"),
	0x8026CCB4: main.sym("pljump_8026D1B0"),
	0x8026CDFC: main.sym("pljump_8026D33C"),
	0x8026CE88: main.sym("pljump_8026D3C8"),
	0x8026CF08: main.sym("pljump_8026D43C"),
	0x8026CF88: main.sym("pljump_8026D4B0"),
	0x8026CFEC: main.sym("pljump_8026D508"),
	0x8026D050: main.sym("pljump_8026D560"),
	0x8026D0F8: main.sym("pljump_8026D608"),
	0x8026D1EC: main.sym("pljump_8026D6FC"),
	0x8026D26C: main.sym("pljump_8026D770"),
	0x8026D498: main.sym("pljump_8026D988"),
	0x8026D664: main.sym("pljump_8026DB54"),
	0x8026D804: main.sym("pljump_8026DCF4"),
	0x8026D9A8: main.sym("pljump_8026DE98"),
	0x8026DB98: main.sym("pljump_8026E088"),
	0x8026DDC4: main.sym("pljump_8026E2B4"),
	0x8026E0AC: main.sym("pljump_8026E59C"),
	0x8026E320: main.sym("pljump_8026E810"),
	0x8026E478: main.sym("pljump_8026E968"),
	0x8026E710: main.sym("pljump_8026EC00"),
	0x8026EC2C: main.sym("pljump_8026F158"),
	0x8026EDC0: main.sym("pljump_8026F2EC"),
	0x8026F0A8: main.sym("pljump_8026F614"),
	0x8026F0F4: main.sym("pljump_8026F660"),
	0x8026F2D4: main.sym("pljump_8026F840"),
	0x8026F4AC: main.sym("pljump_8026FA18"),
	0x8026F598: main.sym("PL_ExecJump", flag={"GLOBL"}),
	0x8026F804: main.sym("L8026FD70", flag={"GLOBL","LOCAL"}),
	0x8026F818: main.sym("L8026FD84", flag={"GLOBL","LOCAL"}),
	0x8026F82C: main.sym("L8026FD98", flag={"GLOBL","LOCAL"}),
	0x8026F840: main.sym("L8026FDAC", flag={"GLOBL","LOCAL"}),
	0x8026F854: main.sym("L8026FDC0", flag={"GLOBL","LOCAL"}),
	0x8026F868: main.sym("L8026FDD4", flag={"GLOBL","LOCAL"}),
	0x8026F87C: main.sym("L8026FDE8", flag={"GLOBL","LOCAL"}),
	0x8026F8A4: main.sym("L8026FE10", flag={"GLOBL","LOCAL"}),
	0x8026F8B8: main.sym("L8026FE24", flag={"GLOBL","LOCAL"}),
	0x8026F8CC: main.sym("L8026FE38", flag={"GLOBL","LOCAL"}),
	0x8026F8E0: main.sym("L8026FE4C", flag={"GLOBL","LOCAL"}),
	0x8026F8F4: main.sym("L8026FE60", flag={"GLOBL","LOCAL"}),
	0x8026F908: main.sym("L8026FE74", flag={"GLOBL","LOCAL"}),
	0x8026F91C: main.sym("L8026FE88", flag={"GLOBL","LOCAL"}),
	0x8026F930: main.sym("L8026FE9C", flag={"GLOBL","LOCAL"}),
	0x8026F980: main.sym("L8026FEEC", flag={"GLOBL","LOCAL"}),
	0x8026F994: main.sym("L8026FF00", flag={"GLOBL","LOCAL"}),
	0x8026F9A8: main.sym("L8026FF14", flag={"GLOBL","LOCAL"}),
	0x8026F9BC: main.sym("L8026FF28", flag={"GLOBL","LOCAL"}),
	0x8026F9D0: main.sym("L8026FF3C", flag={"GLOBL","LOCAL"}),
	0x8026F9F8: main.sym("L8026FF64", flag={"GLOBL","LOCAL"}),
	0x8026FA20: main.sym("L8026FF8C", flag={"GLOBL","LOCAL"}),
	0x8026FA34: main.sym("L8026FFA0", flag={"GLOBL","LOCAL"}),
	0x8026FA48: main.sym("L8026FFB4", flag={"GLOBL","LOCAL"}),
	0x8026FA5C: main.sym("L8026FFC8", flag={"GLOBL","LOCAL"}),
	0x8026FA70: main.sym("L8026FFDC", flag={"GLOBL","LOCAL"}),
	0x8026FA98: main.sym("L80270004", flag={"GLOBL","LOCAL"}),
	0x8026FAC0: main.sym("L8027002C", flag={"GLOBL","LOCAL"}),
	0x8026FAD4: main.sym("L80270040", flag={"GLOBL","LOCAL"}),
	0x8026FAE8: main.sym("L80270054", flag={"GLOBL","LOCAL"}),
	0x8026FB4C: main.sym("L802700B8", flag={"GLOBL","LOCAL"}),
	0x8026FB74: main.sym("L802700E0", flag={"GLOBL","LOCAL"}),

	# src/plswim.c
	0x8026FBA0: main.sym("plswim_80270110"),
	0x8026FC5C: main.sym("plswim_802701CC"),
	0x8026FCC4: main.sym("plswim_80270234"),
	0x8026FD94: main.sym("plswim_80270304"),
	0x8026FF90: main.sym("plswim_80270500"),
	0x802703A8: main.sym("plswim_80270918"),
	0x80270504: main.sym("plswim_80270A74"),
	0x802705DC: main.sym("plswim_80270B4C"),
	0x80270724: main.sym("plswim_80270C94"),
	0x802708D0: main.sym("plswim_80270E40"),
	0x80270A68: main.sym("plswim_80270FD8"),
	0x80270B54: main.sym("plswim_802710C4"),
	0x80270C64: main.sym("plswim_802711D4"),
	0x80270D50: main.sym("plswim_802712C0"),
	0x80270E4C: main.sym("plswim_802713BC"),
	0x80270F38: main.sym("plswim_802714A8"),
	0x8027107C: main.sym("plswim_802715EC"),
	0x802710CC: main.sym("plswim_8027163C"),
	0x80271194: main.sym("plswim_80271704"),
	0x802713A8: main.sym("plswim_80271918"),
	0x8027140C: main.sym("plswim_8027197C"),
	0x80271530: main.sym("plswim_80271AA0"),
	0x80271794: main.sym("plswim_80271D04"),
	0x80271944: main.sym("plswim_80271EB4"),
	0x80271ABC: main.sym("plswim_8027202C"),
	0x80271CFC: main.sym("plswim_8027226C"),
	0x80271E80: main.sym("plswim_802723F0"),
	0x80271FD8: main.sym("plswim_80272548"),
	0x8027210C: main.sym("plswim_8027267C"),
	0x80272208: main.sym("plswim_80272778"),
	0x80272300: main.sym("plswim_80272870"),
	0x802724F0: main.sym("plswim_80272A60"),
	0x802725AC: main.sym("plswim_80272B1C"),
	0x802725F4: main.sym("plswim_80272B64"),
	0x8027263C: main.sym("plswim_80272BAC"),
	0x8027274C: main.sym("plswim_80272CBC"),
	0x80272850: main.sym("plswim_80272DC0"),
	0x802728CC: main.sym("plswim_80272E3C"),
	0x80272A78: main.sym("L80272FE8", flag={"GLOBL","LOCAL"}),
	0x80272A94: main.sym("L80273004", flag={"GLOBL","LOCAL"}),
	0x80272AB0: main.sym("L80273020", flag={"GLOBL","LOCAL"}),
	0x80272ACC: main.sym("L8027303C", flag={"GLOBL","LOCAL"}),
	0x80272AE8: main.sym("L80273058", flag={"GLOBL","LOCAL"}),
	0x80272B00: main.sym("L80273070", flag={"GLOBL","LOCAL"}),
	0x80272B48: main.sym("L802730B8", flag={"GLOBL","LOCAL"}),
	0x80272B5C: main.sym("L802730CC", flag={"GLOBL","LOCAL"}),
	0x80272B70: main.sym("L802730E0", flag={"GLOBL","LOCAL"}),
	0x80272B84: main.sym("L802730F4", flag={"GLOBL","LOCAL"}),
	0x80272B98: main.sym("L80273108", flag={"GLOBL","LOCAL"}),
	0x80272BAC: main.sym("L8027311C", flag={"GLOBL","LOCAL"}),
	0x80272BF0: main.sym("plswim_80273160"),
	0x80272FA8: main.sym("plswim_80273518"),
	0x80273034: main.sym("plswim_802735A4"),
	0x802730A8: main.sym("plswim_80273618"),
	0x80273284: main.sym("plswim_802737F4"),
	0x802734BC: main.sym("plswim_80273A2C"),
	0x80273664: main.sym("plswim_80273BD4"),
	0x80273760: main.sym("plswim_80273CD0"),
	0x80273904: main.sym("plswim_80273E74"),
	0x80273AC0: main.sym("plswim_80274030"),
	0x80273BC4: main.sym("plswim_80274134"),
	0x80273CF8: main.sym("plswim_80274268"),
	0x80273E14: main.sym("plswim_80274384"),
	0x80273F3C: main.sym("plswim_802744AC"),
	0x80274010: main.sym("plswim_80274580"),
	0x80274118: main.sym("plswim_80274688"),
	0x802741EC: main.sym("plswim_8027475C"),
	0x802742F4: main.sym("plswim_80274864"),
	0x8027442C: main.sym("PL_ExecSwim", flag={"GLOBL"}),
	0x8027474C: main.sym("L80274CBC", flag={"GLOBL","LOCAL"}),
	0x80274760: main.sym("L80274CD0", flag={"GLOBL","LOCAL"}),
	0x80274774: main.sym("L80274CE4", flag={"GLOBL","LOCAL"}),
	0x80274788: main.sym("L80274CF8", flag={"GLOBL","LOCAL"}),
	0x8027479C: main.sym("L80274D0C", flag={"GLOBL","LOCAL"}),
	0x802747B0: main.sym("L80274D20", flag={"GLOBL","LOCAL"}),
	0x802747C4: main.sym("L80274D34", flag={"GLOBL","LOCAL"}),
	0x802747D8: main.sym("L80274D48", flag={"GLOBL","LOCAL"}),
	0x802747EC: main.sym("L80274D5C", flag={"GLOBL","LOCAL"}),
	0x8027483C: main.sym("L80274DAC", flag={"GLOBL","LOCAL"}),
	0x80274878: main.sym("L80274DE8", flag={"GLOBL","LOCAL"}),
	0x8027488C: main.sym("L80274DFC", flag={"GLOBL","LOCAL"}),
	0x802748B4: main.sym("L80274E24", flag={"GLOBL","LOCAL"}),
	0x802748F0: main.sym("L80274E60", flag={"GLOBL","LOCAL"}),
	0x80274904: main.sym("L80274E74", flag={"GLOBL","LOCAL"}),
	0x80274918: main.sym("L80274E88", flag={"GLOBL","LOCAL"}),

	# src/pltake.c
	0x80274940: main.sym("pltake_80274EB0"),
	0x802749A0: main.sym("pltake_80274F10", flag={"GLOBL"}),
	0x80274A20: main.sym("L80274F90", flag={"GLOBL","LOCAL"}),
	0x80274A38: main.sym("L80274FA8", flag={"GLOBL","LOCAL"}),
	0x80274AE0: main.sym("L80275050", flag={"GLOBL","LOCAL"}),
	0x80274B5C: main.sym("L802750CC", flag={"GLOBL","LOCAL"}),
	0x80274B74: main.sym("L802750E4", flag={"GLOBL","LOCAL"}),
	0x80274C00: main.sym("L80275170", flag={"GLOBL","LOCAL"}),
	0x80274C7C: main.sym("L802751EC", flag={"GLOBL","LOCAL"}),
	0x80274D10: main.sym("L80275280", flag={"GLOBL","LOCAL"}),
	0x80274D98: main.sym("L80275308", flag={"GLOBL","LOCAL"}),
	0x80274DB8: main.sym("pltake_80275328"),
	0x80274EFC: main.sym("pltake_8027546C"),
	0x8027508C: main.sym("pltake_802755FC"),
	0x80275158: main.sym("pltake_802756C8"),
	0x80275224: main.sym("pltake_80275794"),
	0x80275350: main.sym("pltake_802758C0"),
	0x80275444: main.sym("pltake_802759B4"),
	0x80275510: main.sym("pltake_80275A80"),
	0x802755C4: main.sym("pltake_80275B34"),
	0x802758C8: main.sym("pltake_80275E78"),
	0x8027595C: main.sym("pltake_80275F0C"),
	0x80275A30: main.sym("PL_ExecTake", flag={"GLOBL"}),
	0x80275B18: main.sym("L802760C8", flag={"GLOBL","LOCAL"}),
	0x80275B2C: main.sym("L802760DC", flag={"GLOBL","LOCAL"}),
	0x80275B40: main.sym("L802760F0", flag={"GLOBL","LOCAL"}),
	0x80275B54: main.sym("L80276104", flag={"GLOBL","LOCAL"}),
	0x80275B90: main.sym("L80276140", flag={"GLOBL","LOCAL"}),
	0x80275BA4: main.sym("L80276154", flag={"GLOBL","LOCAL"}),
	0x80275BB8: main.sym("L80276168", flag={"GLOBL","LOCAL"}),
	0x80275BCC: main.sym("L8027617C", flag={"GLOBL","LOCAL"}),

	# src/callback.c
	0x80275C20: main.sym("CtrlWeather", flag={"GLOBL"}),
	0x80275E24: main.sym("CtrlBackground", flag={"GLOBL"}),
	0x80275F00: main.sym("CtrlFace", flag={"GLOBL"}),
	0x80275FCC: main.sym("callback_8027657C"),
	0x8027604C: main.sym("callback_802765FC"),
	0x80276104: main.sym("callback_802766B4"),
	0x80276208: main.sym("callback_802767B8"),
	0x80276254: main.sym("callback_80276804"),
	0x8027629C: main.sym("callback_8027684C", flag={"GLOBL"}),
	0x802762F8: main.sym("L802768A8", flag={"GLOBL","LOCAL"}),
	0x80276308: main.sym("L802768B8", flag={"GLOBL","LOCAL"}),
	0x80276318: main.sym("L802768C8", flag={"GLOBL","LOCAL"}),
	0x80276328: main.sym("L802768D8", flag={"GLOBL","LOCAL"}),
	0x80276338: main.sym("L802768E8", flag={"GLOBL","LOCAL"}),
	0x80276360: main.sym("callback_80276910", flag={"GLOBL"}),
	0x802764F0: main.sym("callback_80276AA0"),
	0x80276608: main.sym("callback_80276BB8", flag={"GLOBL"}),
	0x8027671C: main.sym("callback_80276CCC", flag={"GLOBL"}),
	0x802769E0: main.sym("callback_80276F90"),
	0x80276AF4: main.sym("CtrlPlayerAlpha", flag={"GLOBL"}),
	0x80276BA0: main.sym("CtrlPlayerLOD", flag={"GLOBL"}),
	0x80276C0C: main.sym("CtrlPlayerEyes", flag={"GLOBL"}),
	0x80276CE4: main.sym("CtrlPlayerTorso", flag={"GLOBL"}),
	0x80276DF4: main.sym("CtrlPlayerNeck", flag={"GLOBL"}),
	0x80276F44: main.sym("CtrlMarioHand", flag={"GLOBL"}),
	0x8027701C: main.sym("CtrlMarioPunch", flag={"GLOBL"}),
	0x80277128: main.sym("CtrlPlayerCap", flag={"GLOBL"}),
	0x80277190: main.sym("CtrlPlayerHead", flag={"GLOBL"}),
	0x80277274: main.sym("CtrlPlayerWing", flag={"GLOBL"}),
	0x802773AC: main.sym("CtrlPlayerHand", flag={"GLOBL"}),
	0x80277564: main.sym("CtrlInsideMirror", flag={"GLOBL"}),
	0x802777BC: main.sym("CtrlMarioMirror", flag={"GLOBL"}),

	# src/memory.c
	0x80277930: main.sym("SegmentSet", flag={"GLOBL"}),
	0x80277970: main.sym("SegmentGet", flag={"GLOBL"}),
	0x802779A0: main.sym("SegmentToVirtual", flag={"GLOBL"}),
	0x802779F8: main.sym("VirtualToSegment", flag={"GLOBL"}),
	0x80277A40: main.sym("SegmentWrite", flag={"GLOBL"}),
	0x80277AC4: main.sym("MemInit", flag={"GLOBL"}),
	0x80277B70: main.sym("MemAlloc", flag={"GLOBL"}),
	0x80277C88: main.sym("MemFree", flag={"GLOBL"}),
	0x80277DA8: main.sym("MemRealloc", flag={"GLOBL"}),
	0x80277E18: main.sym("MemAvailable", flag={"GLOBL"}),
	0x80277E38: main.sym("MemPush", flag={"GLOBL"}),
	0x80277EE8: main.sym("MemPull", flag={"GLOBL"}),
	0x80277F54: main.sym("MemRead", flag={"GLOBL"}),
	0x80278060: main.sym("MemLoad", flag={"GLOBL"}),
	0x802780DC: main.sym("MemLoadData", flag={"GLOBL"}),
	0x80278140: main.sym("MemLoadCode", flag={"GLOBL"}),
	0x80278228: main.sym("MemLoadPres", flag={"GLOBL"}),
	0x80278304: main.sym("MemLoadText", flag={"GLOBL"}),
	0x802783C4: main.sym("MemLoadULib", flag={"GLOBL"}),
	0x80278464: main.sym("ArenaCreate", flag={"GLOBL"}),
	0x80278508: main.sym("ArenaAlloc", flag={"GLOBL"}),
	0x80278578: main.sym("ArenaResize", flag={"GLOBL"}),
	0x802785E8: main.sym("HeapCreate", flag={"GLOBL"}),
	0x802786A8: main.sym("HeapAlloc", flag={"GLOBL"}),
	0x802787C4: main.sym("HeapFree", flag={"GLOBL"}),
	0x8027897C: main.sym("GfxAlloc", flag={"GLOBL"}),
	0x802789F0: main.sym("BankLoadInfo"),
	0x80278A78: main.sym("BankInit", flag={"GLOBL"}),
	0x80278AD4: main.sym("BankLoad", flag={"GLOBL"}),

	# src/backup.c
	0x80278BB0: main.sym("BuInitDebug"),
	0x80278BC4: main.sym("BackupRead"),
	0x80278C68: main.sym("BackupWrite"),
	0x80278D10: main.sym("BuCheckSum"),
	0x80278D64: main.sym("BuCheck"),
	0x80278DEC: main.sym("BuCheckSet"),
	0x80278E4C: main.sym("BuInfoRecover"),
	0x80278EF0: main.sym("BuInfoWrite"),
	0x80278F6C: main.sym("BuInfoErase"),
	0x80278FF0: main.sym("BuGetTime"),
	0x80279024: main.sym("BuSetTime"),
	0x802790A0: main.sym("BuUpdateTime"),
	0x80279150: main.sym("BuUpdateTimeAll"),
	0x80279198: main.sym("BuFileRecover"),
	0x80279290: main.sym("BuFileWrite", flag={"GLOBL"}),
	0x8027934C: main.sym("BuFileErase", flag={"GLOBL"}),
	0x802793B0: main.sym("BuFileCopy", flag={"GLOBL"}),
	0x8027942C: main.sym("BackupInit", flag={"GLOBL"}),
	0x80279618: main.sym("BuReset", flag={"GLOBL"}),
	0x80279694: main.sym("BuSet", flag={"GLOBL"}),
	0x80279894: main.sym("BuFileIsActive", flag={"GLOBL"}),
	0x802798D0: main.sym("BuGetHiScore", flag={"GLOBL"}),
	0x802799D0: main.sym("BuFileStarCount", flag={"GLOBL"}),
	0x80279A60: main.sym("BuFileStarRange", flag={"GLOBL"}),
	0x80279AF8: main.sym("BuSetFlag", flag={"GLOBL"}),
	0x80279B44: main.sym("BuClrFlag", flag={"GLOBL"}),
	0x80279BBC: main.sym("BuGetFlag", flag={"GLOBL"}),
	0x80279C18: main.sym("BuFileGetStar", flag={"GLOBL"}),
	0x80279C8C: main.sym("BuFileSetStar", flag={"GLOBL"}),
	0x80279D60: main.sym("BuFileGetCoin", flag={"GLOBL"}),
	0x80279D90: main.sym("BuGetCannon", flag={"GLOBL"}),
	0x80279DE0: main.sym("BuSetCannon", flag={"GLOBL"}),
	0x80279E68: main.sym("BuSetCap", flag={"GLOBL"}),
	0x80279EFC: main.sym("BuGetCap", flag={"GLOBL"}),
	0x80279FB4: main.sym("BuSetSound", flag={"GLOBL"}),
	0x8027A004: main.sym("BuGetSound", flag={"GLOBL"}),
	0x8027A024: main.sym("BuInitCap", flag={"GLOBL"}),
	0x8027A0E8: main.sym("BuClrMid", flag={"GLOBL"}),
	0x8027A100: main.sym("BuSetMid", flag={"GLOBL"}),
	0x8027A168: main.sym("BuGetMid", flag={"GLOBL"}),

	# src/scene.c
	0x8027A220: main.sym("SnSetVp", flag={"GLOBL"}),
	0x8027A28C: main.sym("SnSetBlank"),
	0x8027A300: main.sym("SceneDemo", flag={"GLOBL"}),
	0x8027A38C: main.sym("SnGetPortType", flag={"GLOBL"}),
	0x8027A418: main.sym("SnGetPort", flag={"GLOBL"}),
	0x8027A478: main.sym("ObjGetPort"),
	0x8027A4C4: main.sym("SnInitPort"),
	0x8027A554: main.sym("SceneInit", flag={"GLOBL"}),
	0x8027A7C4: main.sym("SceneExit", flag={"GLOBL"}),
	0x8027A894: main.sym("SceneOpen", flag={"GLOBL"}),
	0x8027A998: main.sym("SceneClose", flag={"GLOBL"}),
	0x8027AA0C: main.sym("SnOpenPlayer", flag={"GLOBL"}),
	0x8027AA88: main.sym("SnClosePlayer", flag={"GLOBL"}),
	0x8027AB10: main.sym("SceneSet", flag={"GLOBL"}),
	0x8027ABB4: main.sym("SceneProc", flag={"GLOBL"}),
	0x8027ABF0: main.sym("SnWipe", flag={"GLOBL"}),
	0x8027ADAC: main.sym("SnWipeDelay", flag={"GLOBL"}),
	0x8027AE04: main.sym("SceneDraw", flag={"GLOBL"}),

	# src/draw.c
	0x8027B110: main.sym("DrawLayerList"),
	0x8027B354: main.sym("DrawLayerGfx"),
	0x8027B450: main.sym("DrawLayer"),
	0x8027B4E8: main.sym("DrawOrtho"),
	0x8027B6C4: main.sym("DrawPersp"),
	0x8027B840: main.sym("DrawLOD"),
	0x8027B8D4: main.sym("DrawSelect"),
	0x8027B9A8: main.sym("DrawCamera"),
	0x8027BB64: main.sym("DrawCoord"),
	0x8027BC88: main.sym("DrawPos"),
	0x8027BDAC: main.sym("DrawAng"),
	0x8027BEC4: main.sym("DrawScale"),
	0x8027BFE4: main.sym("DrawBillboard"),
	0x8027C18C: main.sym("DrawGfx"),
	0x8027C1F4: main.sym("DrawCallback"),
	0x8027C2A8: main.sym("DrawBack"),
	0x8027C4C0: main.sym("DrawJoint"),
	0x8027C988: main.sym("DrawSkeleton"),
	0x8027CB08: main.sym("DrawShadow"),
	0x8027CF68: main.sym("SObjIsVisible"),
	0x8027D14C: main.sym("DrawObject"),
	0x8027D460: main.sym("DrawBranch"),
	0x8027D4D4: main.sym("DrawHand"),
	0x8027D8B8: main.sym("DrawChild"),
	0x8027D8F8: main.sym("DrawShape"),
	0x8027D9E0: main.sym("L8027DF90", flag={"GLOBL","LOCAL"}),
	0x8027D9F0: main.sym("L8027DFA0", flag={"GLOBL","LOCAL"}),
	0x8027DA00: main.sym("L8027DFB0", flag={"GLOBL","LOCAL"}),
	0x8027DA10: main.sym("L8027DFC0", flag={"GLOBL","LOCAL"}),
	0x8027DA20: main.sym("L8027DFD0", flag={"GLOBL","LOCAL"}),
	0x8027DA30: main.sym("L8027DFE0", flag={"GLOBL","LOCAL"}),
	0x8027DA40: main.sym("L8027DFF0", flag={"GLOBL","LOCAL"}),
	0x8027DA50: main.sym("L8027E000", flag={"GLOBL","LOCAL"}),
	0x8027DA60: main.sym("L8027E010", flag={"GLOBL","LOCAL"}),
	0x8027DA70: main.sym("L8027E020", flag={"GLOBL","LOCAL"}),
	0x8027DA80: main.sym("L8027E030", flag={"GLOBL","LOCAL"}),
	0x8027DA90: main.sym("L8027E040", flag={"GLOBL","LOCAL"}),
	0x8027DAA0: main.sym("L8027E050", flag={"GLOBL","LOCAL"}),
	0x8027DAB0: main.sym("L8027E060", flag={"GLOBL","LOCAL"}),
	0x8027DAC0: main.sym("L8027E070", flag={"GLOBL","LOCAL"}),
	0x8027DAD0: main.sym("L8027E080", flag={"GLOBL","LOCAL"}),
	0x8027DAE0: main.sym("L8027E090", flag={"GLOBL","LOCAL"}),
	0x8027DAF0: main.sym("L8027E0A0", flag={"GLOBL","LOCAL"}),
	0x8027DB00: main.sym("L8027E0B0", flag={"GLOBL","LOCAL"}),
	0x8027DB10: main.sym("L8027E0C0", flag={"GLOBL","LOCAL"}),
	0x8027DB80: main.sym("DrawScene", flag={"GLOBL"}),

	# src/time.c
	0x8027DE30: main.sym("TimeGfxCPU", flag={"GLOBL"}),
	0x8027DEE0: main.sym("TimeAudCPU", flag={"GLOBL"}),
	0x8027DF70: main.sym("TimeGfxRCP", flag={"GLOBL"}),
	0x8027E01C: main.sym("TimeAudRCP", flag={"GLOBL"}),
	0x8027E0AC: main.sym("TimeDrawD"),
	0x8027E3A8: main.sym("TimeDrawScale"),
	0x8027E61C: main.sym("TimeDrawAbs"),
	0x8027E8FC: main.sym("TimeDrawRel"),
	0x8027EEB0: main.sym("TimeDraw", flag={"GLOBL"}),

	# src/slidec.s
	0x8027EF30: main.sym("slidec", flag={"GLOBL"}),

	# src/camera.c
	0x8027EFE0: main.sym("camera_8027F590", flag={"GLOBL"}),
	0x8027F01C: main.sym("L8027F5CC", flag={"GLOBL","LOCAL"}),
	0x8027F03C: main.sym("L8027F5EC", flag={"GLOBL","LOCAL"}),
	0x8027F064: main.sym("L8027F614", flag={"GLOBL","LOCAL"}),
	0x8027F07C: main.sym("L8027F62C", flag={"GLOBL","LOCAL"}),
	0x8027F11C: main.sym("L8027F6CC", flag={"GLOBL","LOCAL"}),
	0x8027F1BC: main.sym("L8027F76C", flag={"GLOBL","LOCAL"}),
	0x8027F25C: main.sym("L8027F80C", flag={"GLOBL","LOCAL"}),
	0x8027F284: main.sym("L8027F834", flag={"GLOBL","LOCAL"}),
	0x8027F2EC: main.sym("L8027F89C", flag={"GLOBL","LOCAL"}),
	0x8027F308: main.sym("camera_8027F8B8", flag={"GLOBL"}),
	0x8027F340: main.sym("L8027F8F0", flag={"GLOBL","LOCAL"}),
	0x8027F358: main.sym("L8027F908", flag={"GLOBL","LOCAL"}),
	0x8027F370: main.sym("L8027F920", flag={"GLOBL","LOCAL"}),
	0x8027F388: main.sym("L8027F938", flag={"GLOBL","LOCAL"}),
	0x8027F3A0: main.sym("L8027F950", flag={"GLOBL","LOCAL"}),
	0x8027F3B8: main.sym("L8027F968", flag={"GLOBL","LOCAL"}),
	0x8027F3D0: main.sym("L8027F980", flag={"GLOBL","LOCAL"}),
	0x8027F3F8: main.sym("L8027F9A8", flag={"GLOBL","LOCAL"}),
	0x8027F410: main.sym("L8027F9C0", flag={"GLOBL","LOCAL"}),
	0x8027F428: main.sym("L8027F9D8", flag={"GLOBL","LOCAL"}),
	0x8027F440: main.sym("camera_8027F9F0", flag={"GLOBL"}),
	#0x8027FB74: main.sym("camera_8027FB74"),
	0x8027F668: main.sym("camera_8027FC18"),
	0x8027F870: main.sym("camera_8027FE20"),
	#0x8027FF00: main.sym("camera_8027FF00"),
	0x8027FA48: main.sym("camera_8027FFF8"),
	0x8027FDB8: main.sym("camera_80280368"),
	0x8027FF44: main.sym("camera_802804F4"),
	0x802800F4: main.sym("camera_802806A4"),
	0x80280260: main.sym("camera_80280810", flag={"GLOBL"}),
	0x802803C0: main.sym("camera_80280970", flag={"GLOBL"}),
	0x80280550: main.sym("camera_80280B00"),
	0x80280BD8: main.sym("camera_80281188"),
	0x80280E0C: main.sym("camera_802813BC"),
	0x80280E3C: main.sym("camera_802813EC"),
	0x80280EBC: main.sym("camera_8028146C"),
	0x80280FD8: main.sym("camera_80281588"),
	0x802810F0: main.sym("camera_802816A0", flag={"GLOBL"}),
	0x8028124C: main.sym("camera_802817FC"),
	0x80281354: main.sym("camera_80281904", flag={"GLOBL"}),
	0x80281CD0: main.sym("camera_80282280", flag={"GLOBL"}),
	0x802820F0: main.sym("camera_802826A0", flag={"GLOBL"}),
	0x8028265C: main.sym("camera_80282C0C", flag={"GLOBL"}),
	#0x80282C28: main.sym("camera_80282C28"),
	0x8028268C: main.sym("camera_80282C3C"),
	0x802826CC: main.sym("camera_80282C7C"),
	0x80282730: main.sym("camera_80282CE0"),
	0x802827C8: main.sym("camera_80282D78", flag={"GLOBL"}),
	0x80282D90: main.sym("camera_80283340"),
	0x80282FC8: main.sym("camera_80283578"),
	0x80283434: main.sym("camera_802839E4"),
	0x80283468: main.sym("camera_80283A18", flag={"GLOBL"}),
	0x80283484: main.sym("camera_80283A34"),
	0x802834B8: main.sym("camera_80283A68", flag={"GLOBL"}),
	0x80283548: main.sym("camera_80283AF8"),
	0x80284708: main.sym("camera_80284CB8"),
	0x8028474C: main.sym("camera_80284CFC"),
	0x80284788: main.sym("camera_80284D38"),
	0x802847C4: main.sym("camera_80284D74", flag={"GLOBL"}),
	0x80284AFC: main.sym("camera_802850AC"),
	0x80284B3C: main.sym("camera_802850EC", flag={"GLOBL"}),
	#0x8028517C: main.sym("camera_8028517C"),
	0x80284C2C: main.sym("camera_802851DC"),
	0x80284CBC: main.sym("camera_8028526C"),
	0x80284D44: main.sym("camera_802852F4"),
	0x80284DC0: main.sym("camera_80285370"),
	0x80285258: main.sym("camera_80285808", flag={"GLOBL"}),
	0x802852F4: main.sym("camera_802858A4"),
	0x8028547C: main.sym("camera_80285A2C"),
	0x80285770: main.sym("camera_80285D20"),
	0x80285928: main.sym("camera_80285ED8", flag={"GLOBL"}),
	0x802859B0: main.sym("camera_80285F60"),
	0x80285A8C: main.sym("camera_8028603C"),
	0x80285AD8: main.sym("camera_80286088"),
	0x80285BD8: main.sym("camera_80286188", flag={"GLOBL"}),
	0x80285E70: main.sym("camera_80286420"),
	0x80286348: main.sym("camera_802868F8", flag={"GLOBL"}),
	0x802866D4: main.sym("L80286C84", flag={"GLOBL","LOCAL"}),
	0x802866E4: main.sym("L80286C94", flag={"GLOBL","LOCAL"}),
	0x802866F4: main.sym("L80286CA4", flag={"GLOBL","LOCAL"}),
	0x80286704: main.sym("L80286CB4", flag={"GLOBL","LOCAL"}),
	0x80286714: main.sym("L80286CC4", flag={"GLOBL","LOCAL"}),
	0x80286724: main.sym("L80286CD4", flag={"GLOBL","LOCAL"}),
	0x80286734: main.sym("L80286CE4", flag={"GLOBL","LOCAL"}),
	0x80286744: main.sym("L80286CF4", flag={"GLOBL","LOCAL"}),
	0x80286754: main.sym("L80286D04", flag={"GLOBL","LOCAL"}),
	0x80286764: main.sym("L80286D14", flag={"GLOBL","LOCAL"}),
	0x80286774: main.sym("L80286D24", flag={"GLOBL","LOCAL"}),
	0x80286784: main.sym("L80286D34", flag={"GLOBL","LOCAL"}),
	0x80286794: main.sym("L80286D44", flag={"GLOBL","LOCAL"}),
	0x802867A4: main.sym("L80286D54", flag={"GLOBL","LOCAL"}),
	0x802867B4: main.sym("L80286D64", flag={"GLOBL","LOCAL"}),
	0x802869B8: main.sym("camera_80286F68", flag={"GLOBL"}),
	0x80286C9C: main.sym("camera_8028724C"),
	0x80286F7C: main.sym("L8028752C", flag={"GLOBL","LOCAL"}),
	0x80286F90: main.sym("L80287578", flag={"GLOBL","LOCAL"}),
	0x80286FA4: main.sym("L8028758C", flag={"GLOBL","LOCAL"}),
	0x80286FB8: main.sym("L802875A0", flag={"GLOBL","LOCAL"}),
	0x8028707C: main.sym("L80287664", flag={"GLOBL","LOCAL"}),
	0x80287094: main.sym("L8028767C", flag={"GLOBL","LOCAL"}),
	0x802870AC: main.sym("L80287694", flag={"GLOBL","LOCAL"}),
	0x802870C8: main.sym("L802876B0", flag={"GLOBL","LOCAL"}),
	0x802870E0: main.sym("L802876C8", flag={"GLOBL","LOCAL"}),
	0x80287104: main.sym("L802876EC", flag={"GLOBL","LOCAL"}),
	0x80287404: main.sym("camera_802879EC"),
	0x802875DC: main.sym("camera_80287BC4", flag={"GLOBL"}),
	0x802875F8: main.sym("camera_80287BE0"),
	0x802876D0: main.sym("camera_80287CB8"),
	#0x80287D30: main.sym("CtrlCamera", flag={"GLOBL"}),
	0x802877D8: main.sym("camera_80287DC0"),
	0x802877EC: main.sym("camera_80287DD4"),
	0x80287800: main.sym("camera_80287DE8"),
	0x80287840: main.sym("camera_80287E28"),
	0x80287868: main.sym("camera_80287E50"),
	#0x80287E78: main.sym("camera_80287E78"),
	0x802878B8: main.sym("camera_80287EA0"),
	0x80287CFC: main.sym("camera_802882E4"),
	0x8028803C: main.sym("camera_80288624", flag={"GLOBL"}),
	0x80288130: main.sym("camera_80288718"),
	0x802882A0: main.sym("camera_80288888"),
	0x802882CC: main.sym("L802888B4", flag={"GLOBL","LOCAL"}),
	0x802882F0: main.sym("L802888D8", flag={"GLOBL","LOCAL"}),
	0x80288314: main.sym("L802888FC", flag={"GLOBL","LOCAL"}),
	0x80288338: main.sym("L80288920", flag={"GLOBL","LOCAL"}),
	0x8028835C: main.sym("L80288944", flag={"GLOBL","LOCAL"}),
	0x80288380: main.sym("L80288968", flag={"GLOBL","LOCAL"}),
	0x802883C8: main.sym("camera_802889B0"),
	0x802886FC: main.sym("camera_80288CE4"),
	0x80288880: main.sym("camera_80288E68"),
	0x80288974: main.sym("camera_80288F5C"),
	0x80288BB0: main.sym("camera_80289198"),
	0x80288C2C: main.sym("camera_80289214"),
	0x80288CF0: main.sym("camera_802892D8"),
	0x80288D74: main.sym("camera_8028935C"),
	0x80288E0C: main.sym("camera_802893F4"),
	0x80288EA0: main.sym("camera_80289488"),
	0x80288ECC: main.sym("camera_802894B4"),
	0x80288F84: main.sym("camera_8028956C"),
	0x80289028: main.sym("camera_80289610"),
	0x8028909C: main.sym("camera_80289684"),
	0x80289110: main.sym("camera_802896F8"),
	0x80289184: main.sym("camera_8028976C"),
	0x80289264: main.sym("camera_8028984C"),
	0x80289354: main.sym("camera_8028993C"),
	0x802893E4: main.sym("camera_802899CC"),
	0x80289524: main.sym("camera_80289B0C", flag={"GLOBL"}),
	0x80289618: main.sym("camera_80289C00"),
	0x80289738: main.sym("camera_80289D20"),
	0x802899A0: main.sym("camera_80289F88"),
	0x80289A98: main.sym("camera_8028A080"),
	0x80289B0C: main.sym("camera_8028A0F4"),
	0x80289F04: main.sym("camera_8028A4EC"),
	0x8028A0D4: main.sym("camera_8028A6BC"),
	0x8028A204: main.sym("camera_8028A7EC"),
	0x8028A24C: main.sym("camera_8028A834"),
	0x8028A300: main.sym("camera_8028A8E8"),
	0x8028A440: main.sym("camera_8028AA28"),
	0x8028A4F0: main.sym("camera_8028AAD8"),
	0x8028A578: main.sym("camera_8028AB60"),
	0x8028A640: main.sym("camera_8028AC28"),
	0x8028A6E4: main.sym("camera_8028ACCC"),
	0x8028A764: main.sym("camera_8028AD4C"),
	0x8028A834: main.sym("camera_8028AE1C"),
	0x8028A908: main.sym("camera_8028AEF0"),
	0x8028A964: main.sym("camera_8028AF4C"),
	0x8028AA24: main.sym("camera_8028B00C"),
	0x8028AA80: main.sym("camera_8028B068"),
	#0x8028B11C: main.sym("camera_8028B11C"),
	0x8028ABE8: main.sym("camera_8028B1D0"),
	0x8028AC30: main.sym("camera_8028B218"),
	0x8028AD44: main.sym("camera_8028B32C"),
	0x8028AE50: main.sym("camera_8028B438"),
	0x8028AF24: main.sym("camera_8028B50C"),
	0x8028B13C: main.sym("camera_8028B724"),
	0x8028B16C: main.sym("camera_8028B754"),
	0x8028B19C: main.sym("camera_8028B784"),
	0x8028B1DC: main.sym("camera_8028B7C4"),
	0x8028B21C: main.sym("camera_8028B804"),
	0x8028B268: main.sym("camera_8028B850"),
	0x8028B29C: main.sym("camera_8028B884"),
	0x8028B2D0: main.sym("camera_8028B8B8"),
	0x8028B304: main.sym("camera_8028B8EC"),
	0x8028B338: main.sym("camera_8028B920"),
	0x8028B36C: main.sym("camera_8028B954"),
	0x8028B3DC: main.sym("camera_8028B9C4"),
	0x8028B740: main.sym("camera_8028BD34", flag={"GLOBL"}),
	0x8028B7A4: main.sym("camera_8028BD98"),
	0x8028BA38: main.sym("camera_8028C038"),
	0x8028BB3C: main.sym("camera_8028C13C"),
	0x8028BB8C: main.sym("camera_8028C18C"),
	0x8028BC6C: main.sym("camera_8028C26C"),
	0x8028BCC8: main.sym("camera_8028C2C8"),
	0x8028C058: main.sym("L8028C658", flag={"GLOBL","LOCAL"}),
	0x8028C068: main.sym("L8028C668", flag={"GLOBL","LOCAL"}),
	0x8028C078: main.sym("L8028C678", flag={"GLOBL","LOCAL"}),
	0x8028C088: main.sym("L8028C688", flag={"GLOBL","LOCAL"}),
	0x8028C098: main.sym("L8028C698", flag={"GLOBL","LOCAL"}),
	0x8028C0A8: main.sym("L8028C6A8", flag={"GLOBL","LOCAL"}),
	0x8028C124: main.sym("L8028C724", flag={"GLOBL","LOCAL"}),
	0x8028C134: main.sym("L8028C734", flag={"GLOBL","LOCAL"}),
	0x8028C144: main.sym("L8028C744", flag={"GLOBL","LOCAL"}),
	0x8028C154: main.sym("L8028C754", flag={"GLOBL","LOCAL"}),
	0x8028C164: main.sym("L8028C764", flag={"GLOBL","LOCAL"}),
	0x8028C1A0: main.sym("camera_8028C7A0", flag={"GLOBL"}),
	0x8028C2F0: main.sym("camera_8028C8F0"),
	#0x8028C9AC: main.sym("camera_8028C9AC"),
	0x8028C3CC: main.sym("camera_8028C9CC"),
	#0x8028CB08: main.sym("camera_8028CB08"),
	0x8028C5F0: main.sym("camera_8028CBF0"),
	0x8028C794: main.sym("camera_8028CD94"),
	0x8028C7EC: main.sym("camera_8028CDEC"),
	0x8028C824: main.sym("camera_8028CE24"),
	#0x8028D41C: main.sym("camera_8028D41C"),
	0x8028CE4C: main.sym("camera_8028D44C"),
	0x8028CFAC: main.sym("camera_8028D5AC"),
	0x8028CFFC: main.sym("camera_8028D5FC"),
	0x8028D058: main.sym("camera_8028D658"),
	0x8028D098: main.sym("camera_8028D698"),
	0x8028D19C: main.sym("camera_8028D79C"),
	0x8028D288: main.sym("camera_8028D888"),
	0x8028D32C: main.sym("camera_8028D92C"),
	0x8028D418: main.sym("camera_8028DA18", flag={"GLOBL"}),
	0x8028D450: main.sym("camera_8028DA50", flag={"GLOBL"}),
	0x8028D4EC: main.sym("camera_8028DAEC", flag={"GLOBL"}),
	0x8028D538: main.sym("camera_8028DB38", flag={"GLOBL"}),
	0x8028D5B4: main.sym("camera_8028DBB4", flag={"GLOBL"}),
	0x8028D5F4: main.sym("camera_8028DBF4", flag={"GLOBL"}),
	0x8028D61C: main.sym("camera_8028DC1C", flag={"GLOBL"}),
	0x8028D670: main.sym("camera_8028DC70", flag={"GLOBL"}),
	0x8028D6A4: main.sym("camera_8028DCA4"),
	0x8028D748: main.sym("camera_8028DD48", flag={"GLOBL"}),
	0x8028D808: main.sym("camera_8028DE2C", flag={"GLOBL"}),
	0x8028D838: main.sym("camera_8028DE5C", flag={"GLOBL"}),
	0x8028D86C: main.sym("camera_8028DE90", flag={"GLOBL"}),
	0x8028D8A0: main.sym("camera_8028DEC4", flag={"GLOBL"}),
	0x8028D8D4: main.sym("camera_8028DEF8", flag={"GLOBL"}),
	0x8028D900: main.sym("camera_8028DF24", flag={"GLOBL"}),
	0x8028D948: main.sym("camera_8028DF6C", flag={"GLOBL"}),
	0x8028D990: main.sym("camera_8028DFB4", flag={"GLOBL"}),
	0x8028D9C4: main.sym("camera_8028DFE8", flag={"GLOBL"}),
	0x8028D9F8: main.sym("camera_8028E01C", flag={"GLOBL"}),
	0x8028DA40: main.sym("camera_8028E064", flag={"GLOBL"}),
	0x8028DA74: main.sym("camera_8028E098", flag={"GLOBL"}),
	0x8028DAC8: main.sym("camera_8028E0EC", flag={"GLOBL"}),
	0x8028DB40: main.sym("camera_8028E164", flag={"GLOBL"}),
	0x8028DBEC: main.sym("camera_8028E210", flag={"GLOBL"}),
	0x8028DC74: main.sym("camera_8028E298", flag={"GLOBL"}),
	0x8028DCDC: main.sym("camera_8028E300", flag={"GLOBL"}),
	#0x8028E334: main.sym("camera_8028E334"),
	0x8028DD68: main.sym("camera_8028E38C", flag={"GLOBL"}),
	0x8028DD94: main.sym("camera_8028E3B8", flag={"GLOBL"}),
	0x8028DDCC: main.sym("camera_8028E3F0", flag={"GLOBL"}),
	0x8028DDF8: main.sym("camera_8028E41C", flag={"GLOBL"}),
	0x8028DE2C: main.sym("camera_8028E450", flag={"GLOBL"}),
	0x8028DE58: main.sym("camera_8028E47C", flag={"GLOBL"}),
	0x8028DF00: main.sym("camera_8028E524", flag={"GLOBL"}),
	0x8028DF38: main.sym("camera_8028E55C", flag={"GLOBL"}),
	0x8028DF70: main.sym("camera_8028E594", flag={"GLOBL"}),
	0x8028DFA8: main.sym("camera_8028E5CC", flag={"GLOBL"}),
	0x8028DFE0: main.sym("camera_8028E604", flag={"GLOBL"}),
	0x8028E018: main.sym("camera_8028E63C", flag={"GLOBL"}),
	0x8028E050: main.sym("camera_8028E674", flag={"GLOBL"}),
	0x8028E0A0: main.sym("camera_8028E6C4", flag={"GLOBL"}),
	0x8028E0F0: main.sym("camera_8028E714", flag={"GLOBL"}),
	0x8028E134: main.sym("camera_8028E758", flag={"GLOBL"}),
	0x8028E16C: main.sym("camera_8028E790", flag={"GLOBL"}),
	0x8028E1A4: main.sym("camera_8028E7C8", flag={"GLOBL"}),
	0x8028E1F4: main.sym("camera_8028E818", flag={"GLOBL"}),
	0x8028E244: main.sym("camera_8028E868", flag={"GLOBL"}),
	0x8028E27C: main.sym("camera_8028E8A0", flag={"GLOBL"}),
	0x8028E2A8: main.sym("camera_8028E8CC", flag={"GLOBL"}),
	0x8028E30C: main.sym("camera_8028E930", flag={"GLOBL"}),
	0x8028E350: main.sym("camera_8028E974", flag={"GLOBL"}),
	0x8028E37C: main.sym("camera_8028E9A0", flag={"GLOBL"}),
	0x8028E3B4: main.sym("camera_8028E9D8", flag={"GLOBL"}),
	0x8028E404: main.sym("camera_8028EA28", flag={"GLOBL"}),
	0x8028E43C: main.sym("camera_8028EA60", flag={"GLOBL"}),
	0x8028E48C: main.sym("camera_8028EAB0", flag={"GLOBL"}),
	0x8028E4C4: main.sym("camera_8028EAE8", flag={"GLOBL"}),
	0x8028E514: main.sym("camera_8028EB38", flag={"GLOBL"}),
	0x8028E564: main.sym("camera_8028EB88", flag={"GLOBL"}),
	0x8028E59C: main.sym("camera_8028EBC0", flag={"GLOBL"}),
	0x8028E5E0: main.sym("camera_8028EC04", flag={"GLOBL"}),
	0x8028E608: main.sym("camera_8028EC2C", flag={"GLOBL"}),
	0x8028E634: main.sym("camera_8028EC58"),
	0x8028E70C: main.sym("camera_8028ED30"),
	0x8028E774: main.sym("camera_8028ED98"),
	0x8028E88C: main.sym("camera_8028EEB0"),
	0x8028F04C: main.sym("camera_8028F670"),
	0x8028F2F0: main.sym("camera_8028F914"),
	0x8028F678: main.sym("camera_8028FC9C"),
	0x8028F800: main.sym("camera_8028FE24"),
	0x8028F834: main.sym("camera_8028FE58"),
	#0x8028FE84: main.sym("camera_8028FE84"),
	0x8028F8E0: main.sym("camera_8028FF04", flag={"GLOBL"}),
	0x8028F9A4: main.sym("camera_8028FFC8", flag={"GLOBL"}),
	0x8028F9E8: main.sym("camera_8029000C", flag={"GLOBL"}),
	0x8028FA74: main.sym("camera_80290098"),
	0x8028FABC: main.sym("camera_802900E0"),
	0x8028FAE0: main.sym("camera_80290104"),
	0x8028FB44: main.sym("camera_80290168"),
	0x8028FB80: main.sym("camera_802901A4"),
	0x8028FBD8: main.sym("camera_802901FC"),
	0x8028FD94: main.sym("camera_802903B8"),
	#0x8029040C: main.sym("camera_8029040C"),
	0x8028FE1C: main.sym("camera_80290440", flag={"GLOBL"}),
	#0x80290474: main.sym("camera_80290474"),
	#0x802904A8: main.sym("camera_802904A8"),
	#0x802904E4: main.sym("camera_802904E4"),
	0x8028FEDC: main.sym("camera_8029051C"),
	0x8028FEFC: main.sym("camera_8029053C"),
	0x80290144: main.sym("camera_80290784"),
	0x802901B4: main.sym("camera_802907F4"),
	0x80290224: main.sym("camera_80290864"),
	0x802902A8: main.sym("camera_802908E8"),
	#0x80290938: main.sym("camera_80290938"),
	#0x80290984: main.sym("camera_80290984"),
	0x80290390: main.sym("camera_802909D0"),
	#0x80290A5C: main.sym("camera_80290A5C"),
	#0x80290A90: main.sym("camera_80290A90"),
	0x8029047C: main.sym("camera_80290ABC"),
	0x80290514: main.sym("camera_80290B54"),
	0x80290564: main.sym("camera_80290BA4"),
	0x80290598: main.sym("camera_80290BD8"),
	#0x80290C08: main.sym("camera_80290C08"),
	0x802905DC: main.sym("camera_80290C1C", flag={"GLOBL"}),
	0x802905F0: main.sym("camera_80290C30", flag={"GLOBL"}),
	#0x80290C44: main.sym("camera_80290C44"),
	#0x80290C9C: main.sym("camera_80290C9C"),
	0x80290750: main.sym("camera_80290D90", flag={"GLOBL"}),
	0x802907C0: main.sym("camera_80290E00", flag={"GLOBL"}),
	#0x80290E74: main.sym("camera_80290E74"),
	#0x80290EB0: main.sym("camera_80290EB0"),
	0x802908DC: main.sym("camera_80290F1C", flag={"GLOBL"}),
	0x8029094C: main.sym("camera_80290F8C", flag={"GLOBL"}),
	#0x80291074: main.sym("camera_80291074"),
	0x80290AC8: main.sym("camera_80291108", flag={"GLOBL"}),
	#0x802911C8: main.sym("camera_802911C8"),
	#0x80291208: main.sym("camera_80291208"),
	#0x8029127C: main.sym("camera_8029127C"),
	#0x802912B8: main.sym("camera_802912B8"),
	0x80290D14: main.sym("camera_80291354", flag={"GLOBL"}),
	0x80290DEC: main.sym("camera_8029142C", flag={"GLOBL"}),
	#0x802914CC: main.sym("camera_802914CC"),
	0x80290ED4: main.sym("camera_80291514", flag={"GLOBL"}),
	0x80290F94: main.sym("camera_802915D4", flag={"GLOBL"}),
	#0x80291654: main.sym("camera_80291654"),
	#0x802916B8: main.sym("camera_802916B8"),
	0x80291134: main.sym("camera_80291774", flag={"GLOBL"}),
	#0x802917E4: main.sym("camera_802917E4"),
	#0x8029184C: main.sym("camera_8029184C"),
	0x80291230: main.sym("camera_80291870", flag={"GLOBL"}),
	0x802912E4: main.sym("camera_80291924", flag={"GLOBL"}),
	#0x80291964: main.sym("camera_80291964"),
	#0x802919DC: main.sym("camera_802919DC"),
	#0x80291AB4: main.sym("camera_80291AB4"),
	#0x80291B18: main.sym("camera_80291B18"),
	#0x80291B68: main.sym("camera_80291B68"),
	#0x80291BF4: main.sym("camera_80291BF4"),
	#0x80291C3C: main.sym("camera_80291C3C"),
	0x80291690: main.sym("camera_80291CD0", flag={"GLOBL"}),
	#0x80291DB0: main.sym("camera_80291DB0"),
	#0x80291E84: main.sym("camera_80291E84"),
	#0x80291F18: main.sym("camera_80291F18"),
	#0x80292038: main.sym("camera_80292038"),
	0x80291B24: main.sym("camera_80292164", flag={"GLOBL"}),
	0x80291BBC: main.sym("camera_802921FC"),
	#0x8029228C: main.sym("camera_8029228C"),
	#0x80292324: main.sym("camera_80292324"),
	#0x80292370: main.sym("camera_80292370"),
	#0x802923B8: main.sym("camera_802923B8"),
	#0x80292400: main.sym("camera_80292400"),
	#0x80292414: main.sym("camera_80292414"),
	#0x8029244C: main.sym("camera_8029244C"),
	#0x80292484: main.sym("camera_80292484"),
	0x80291E78: main.sym("camera_802924B8", flag={"GLOBL"}),
	0x80291FE8: main.sym("camera_80292628"),
	#0x802926DC: main.sym("camera_802926DC"),
	#0x802927D0: main.sym("camera_802927D0"),
	#0x80292868: main.sym("camera_80292868"),
	#0x80292974: main.sym("camera_80292974"),
	#0x80292A20: main.sym("camera_80292A20"),
	#0x80292A4C: main.sym("camera_80292A4C"),
	0x80292440: main.sym("camera_80292A80", flag={"GLOBL"}),
	#0x80292C00: main.sym("camera_80292C00"),
	#0x80292D80: main.sym("camera_80292D80"),
	#0x80292E2C: main.sym("camera_80292E2C"),
	0x80292884: main.sym("camera_80292EC4"),
	#0x80292F40: main.sym("camera_80292F40"),
	#0x80292F98: main.sym("camera_80292F98"),
	#0x80292FE4: main.sym("camera_80292FE4"),
	0x802929D8: main.sym("camera_80293018", flag={"GLOBL"}),
	#0x802930F0: main.sym("camera_802930F0"),
	#0x80293164: main.sym("camera_80293164"),
	#0x802931C0: main.sym("camera_802931C0"),
	#0x80293220: main.sym("camera_80293220"),
	#0x8029328C: main.sym("camera_8029328C"),
	#0x802932F4: main.sym("camera_802932F4"),
	#0x80293328: main.sym("camera_80293328"),
	#0x80293354: main.sym("camera_80293354"),
	0x80292D4C: main.sym("camera_8029338C", flag={"GLOBL"}),
	#0x80293488: main.sym("camera_80293488"),
	#0x802934B4: main.sym("camera_802934B4"),
	0x80292E98: main.sym("camera_802934D8"),
	#0x80293548: main.sym("camera_80293548"),
	0x80292FA0: main.sym("camera_802935E0"),
	#0x80293624: main.sym("camera_80293624"),
	#0x8029369C: main.sym("camera_8029369C"),
	#0x802936DC: main.sym("camera_802936DC"),
	0x802930C8: main.sym("camera_80293708"),
	#0x80293734: main.sym("camera_80293734"),
	#0x802937E8: main.sym("camera_802937E8"),
	0x8029322C: main.sym("camera_8029386C", flag={"GLOBL"}),
	0x80293288: main.sym("camera_802938C8", flag={"GLOBL"}),
	0x80293304: main.sym("camera_80293944", flag={"GLOBL"}),
	#0x80293ABC: main.sym("camera_80293ABC"),
	#0x80293AE8: main.sym("camera_80293AE8"),
	#0x80293B70: main.sym("camera_80293B70"),
	#0x80293BF4: main.sym("camera_80293BF4"),
	0x802935EC: main.sym("camera_80293C2C", flag={"GLOBL"}),
	0x80293670: main.sym("camera_80293CB0", flag={"GLOBL"}),
	0x8029371C: main.sym("camera_80293D5C", flag={"GLOBL"}),
	#0x80293D90: main.sym("camera_80293D90"),
	#0x80293DD4: main.sym("camera_80293DD4"),
	0x8029383C: main.sym("camera_80293E7C", flag={"GLOBL"}),
	0x80293898: main.sym("camera_80293ED8", flag={"GLOBL"}),
	#0x80293F2C: main.sym("camera_80293F2C"),
	0x80293930: main.sym("camera_80293F70", flag={"GLOBL"}),
	#0x80293FCC: main.sym("camera_80293FCC"),
	#0x80294024: main.sym("camera_80294024"),
	#0x80294088: main.sym("camera_80294088"),
	#0x802940CC: main.sym("camera_802940CC"),
	#0x8029410C: main.sym("camera_8029410C"),
	#0x802942CC: main.sym("camera_802942CC"),
	0x80293CB0: main.sym("camera_802942F0", flag={"GLOBL"}),
	0x80293D94: main.sym("camera_802943D4", flag={"GLOBL"}),
	0x80293DE8: main.sym("camera_80294428"),
	#0x80294718: main.sym("camera_80294718"),
	#0x802947A4: main.sym("camera_802947A4"),
	0x802941CC: main.sym("camera_8029480C"),
	#0x802948A0: main.sym("camera_802948A0"),
	0x802943D4: main.sym("camera_80294A14", flag={"GLOBL"}),
	0x80294454: main.sym("camera_80294A94", flag={"GLOBL"}),
	0x802944A8: main.sym("camera_80294AE8"),
	0x80294538: main.sym("camera_80294B78"),
	#0x80294BB4: main.sym("camera_80294BB4"),
	#0x80294C28: main.sym("camera_80294C28"),
	0x8029461C: main.sym("camera_80294C5C", flag={"GLOBL"}),
	#0x80294CC4: main.sym("camera_80294CC4"),
	#0x80294D48: main.sym("camera_80294D48"),
	#0x80294D88: main.sym("camera_80294D88"),
	0x80294774: main.sym("camera_80294DB4", flag={"GLOBL"}),
	#0x80294E24: main.sym("camera_80294E24"),
	#0x80294EA8: main.sym("camera_80294EA8"),
	0x802948A8: main.sym("camera_80294EE8", flag={"GLOBL"}),
	#0x80294F58: main.sym("camera_80294F58"),
	#0x80294F94: main.sym("camera_80294F94"),
	0x802949AC: main.sym("camera_80294FEC", flag={"GLOBL"}),
	#0x802950B0: main.sym("camera_802950B0"),
	#0x80295140: main.sym("camera_80295140"),
	#0x802951F0: main.sym("camera_802951F0"),
	0x80294C30: main.sym("camera_80295270", flag={"GLOBL"}),
	#0x80295310: main.sym("camera_80295310"),
	#0x802953DC: main.sym("camera_802953DC"),
	0x80294DD8: main.sym("camera_80295418", flag={"GLOBL"}),
	#0x80295480: main.sym("camera_80295480"),
	#0x802954EC: main.sym("camera_802954EC"),
	#0x80295518: main.sym("camera_80295518"),
	#0x80295580: main.sym("camera_80295580"),
	#0x80295670: main.sym("camera_80295670"),
	#0x80295740: main.sym("camera_80295740"),
	#0x8029576C: main.sym("camera_8029576C"),
	0x80295188: main.sym("camera_802957C8", flag={"GLOBL"}),
	0x80295254: main.sym("camera_80295894", flag={"GLOBL"}),
	#0x802958D4: main.sym("camera_802958D4"),
	0x802952F0: main.sym("camera_80295930", flag={"GLOBL"}),
	#0x802959CC: main.sym("camera_802959CC"),
	#0x80295A58: main.sym("camera_80295A58"),
	#0x80295BF0: main.sym("camera_80295BF0"),
	#0x80295E24: main.sym("camera_80295E24"),
	0x80295804: main.sym("camera_80295E8C", flag={"GLOBL"}),
	0x80295928: main.sym("camera_80295FB0", flag={"GLOBL"}),
	0x80295950: main.sym("camera_80295FD8", flag={"GLOBL"}),
	#0x80296020: main.sym("camera_80296020"),
	#0x802960B0: main.sym("camera_802960B0"),
	0x80295AD8: main.sym("camera_80296160", flag={"GLOBL"}),
	0x80295C40: main.sym("camera_802962C8", flag={"GLOBL"}),
	0x80295C68: main.sym("camera_802962F0", flag={"GLOBL"}),
	#0x80296318: main.sym("camera_80296318"),
	#0x802963B8: main.sym("camera_802963B8"),
	#0x8029652C: main.sym("camera_8029652C"),
	#0x8029665C: main.sym("camera_8029665C"),
	#0x8029669C: main.sym("camera_8029669C"),
	#0x802966E4: main.sym("camera_802966E4"),
	0x80296088: main.sym("camera_80296710", flag={"GLOBL"}),
	0x8029613C: main.sym("camera_802967C4", flag={"GLOBL"}),
	#0x8029685C: main.sym("camera_8029685C"),
	0x80296218: main.sym("camera_802968A0", flag={"GLOBL"}),
	#0x8029695C: main.sym("camera_8029695C"),
	0x80296370: main.sym("camera_802969F8", flag={"GLOBL"}),
	#0x80296A64: main.sym("camera_80296A64"),
	0x802964A8: main.sym("camera_80296B30", flag={"GLOBL"}),
	#0x80296BC8: main.sym("camera_80296BC8"),
	#0x80296C4C: main.sym("camera_80296C4C"),
	#0x80296D60: main.sym("camera_80296D60"),
	#0x80296DA8: main.sym("camera_80296DA8"),
	#0x80296EB4: main.sym("camera_80296EB4"),
	#0x80296F38: main.sym("camera_80296F38"),
	#0x80296F70: main.sym("camera_80296F70"),
	0x80296920: main.sym("camera_80296FA8", flag={"GLOBL"}),
	#0x80297148: main.sym("camera_80297148"),
	#0x8029720C: main.sym("camera_8029720C"),
	#0x80297290: main.sym("camera_80297290"),
	#0x802972EC: main.sym("camera_802972EC"),
	#0x80297300: main.sym("camera_80297300"),
	#0x80297384: main.sym("camera_80297384"),
	0x80296D28: main.sym("camera_802973B0", flag={"GLOBL"}),
	0x80296DDC: main.sym("camera_80297464"),
	#0x80297560: main.sym("camera_80297560"),
	#0x8029758C: main.sym("camera_8029758C"),
	#0x802975C4: main.sym("camera_802975C4"),
	0x80296F6C: main.sym("camera_8029762C", flag={"GLOBL"}),
	#0x802976BC: main.sym("camera_802976BC"),
	#0x80297728: main.sym("camera_80297728"),
	#0x80297748: main.sym("camera_80297748"),
	#0x80297784: main.sym("camera_80297784"),
	#0x802977C8: main.sym("camera_802977C8"),
	#0x802977F4: main.sym("camera_802977F4"),
	#0x80297820: main.sym("camera_80297820"),
	0x80297160: main.sym("camera_8029784C", flag={"GLOBL"}),
	0x80297204: main.sym("camera_80297908", flag={"GLOBL"}),
	0x80297334: main.sym("camera_80297A38", flag={"GLOBL"}),
	0x80297360: main.sym("camera_80297A64", flag={"GLOBL"}),
	#0x80297B58: main.sym("camera_80297B58"),
	0x80297468: main.sym("camera_80297B84", flag={"GLOBL"}),
	#0x80297C14: main.sym("camera_80297C14"),
	0x80297524: main.sym("camera_80297C40", flag={"GLOBL"}),
	0x80297644: main.sym("L80297D60", flag={"GLOBL","LOCAL"}),
	0x80297684: main.sym("L80297DA0", flag={"GLOBL","LOCAL"}),
	0x802976E4: main.sym("L80297E00", flag={"GLOBL","LOCAL"}),
	0x80297704: main.sym("L80297E20", flag={"GLOBL","LOCAL"}),
	0x80297744: main.sym("L80297E60", flag={"GLOBL","LOCAL"}),
	0x80297784: main.sym("L80297EA0", flag={"GLOBL","LOCAL"}),
	0x802977A4: main.sym("L80297EC0", flag={"GLOBL","LOCAL"}),
	0x802977E4: main.sym("L80297F00", flag={"GLOBL","LOCAL"}),
	0x80297804: main.sym("L80297F20", flag={"GLOBL","LOCAL"}),
	0x80297824: main.sym("L80297F40", flag={"GLOBL","LOCAL"}),
	0x80297908: main.sym("L80298024", flag={"GLOBL","LOCAL"}),
	#0x802980DC: main.sym("camera_802980DC"),
	#0x8029819C: main.sym("camera_8029819C"),
	#0x80298218: main.sym("camera_80298218"),
	#0x80298254: main.sym("camera_80298254"),
	#0x80298290: main.sym("camera_80298290"),
	0x80297C98: main.sym("camera_802983B4", flag={"GLOBL"}),
	0x80297D3C: main.sym("camera_80298458", flag={"GLOBL"}),
	#0x802984A0: main.sym("camera_802984A0"),
	0x80297D98: main.sym("camera_802984B4", flag={"GLOBL"}),
	#0x802987B0: main.sym("camera_802987B0"),
	#0x8029894C: main.sym("camera_8029894C"),
	#0x802989E8: main.sym("camera_802989E8"),
	0x802983DC: main.sym("camera_80298AF8", flag={"GLOBL"}),
	0x80298484: main.sym("camera_80298BA0", flag={"GLOBL"}),
	0x80298510: main.sym("camera_80298C2C", flag={"GLOBL"}),
	0x802985B0: main.sym("camera_80298CCC", flag={"GLOBL"}),
	0x80298628: main.sym("camera_80298D44", flag={"GLOBL"}),
	0x80298680: main.sym("camera_80298D9C", flag={"GLOBL"}),
	0x802988CC: main.sym("camera_80298FE8", flag={"GLOBL"}),
	0x802989E4: main.sym("camera_80299100", flag={"GLOBL"}),
	0x80298A38: main.sym("camera_80299154", flag={"GLOBL"}),
	0x80298A8C: main.sym("camera_802991A8", flag={"GLOBL"}),
	0x80298AD4: main.sym("camera_802991F0", flag={"GLOBL"}),
	0x80298BB0: main.sym("camera_802992CC", flag={"GLOBL"}),
	0x80298C44: main.sym("camera_80299360", flag={"GLOBL"}),
	0x80298CE8: main.sym("camera_80299404", flag={"GLOBL"}),
	0x80298DCC: main.sym("camera_802994E8"),
	0x80298E50: main.sym("L8029956C", flag={"GLOBL","LOCAL"}),
	0x80298E98: main.sym("L802995B4", flag={"GLOBL","LOCAL"}),
	0x80298EE0: main.sym("L802995FC", flag={"GLOBL","LOCAL"}),
	0x80298F28: main.sym("L80299644", flag={"GLOBL","LOCAL"}),
	0x80298F70: main.sym("L8029968C", flag={"GLOBL","LOCAL"}),
	0x80298FB8: main.sym("L802996D4", flag={"GLOBL","LOCAL"}),
	0x80299000: main.sym("L8029971C", flag={"GLOBL","LOCAL"}),
	0x80299048: main.sym("L80299764", flag={"GLOBL","LOCAL"}),
	0x80299090: main.sym("L802997AC", flag={"GLOBL","LOCAL"}),
	0x802990D8: main.sym("L802997F4", flag={"GLOBL","LOCAL"}),
	0x80299120: main.sym("L8029983C", flag={"GLOBL","LOCAL"}),
	0x80299168: main.sym("L80299884", flag={"GLOBL","LOCAL"}),
	0x802991B0: main.sym("L802998CC", flag={"GLOBL","LOCAL"}),
	0x802991F8: main.sym("L80299914", flag={"GLOBL","LOCAL"}),
	0x80299240: main.sym("L8029995C", flag={"GLOBL","LOCAL"}),
	0x80299288: main.sym("L802999A4", flag={"GLOBL","LOCAL"}),
	0x802992D0: main.sym("L802999EC", flag={"GLOBL","LOCAL"}),
	0x80299318: main.sym("L80299A34", flag={"GLOBL","LOCAL"}),
	0x80299360: main.sym("L80299A7C", flag={"GLOBL","LOCAL"}),
	0x802993A8: main.sym("L80299AC4", flag={"GLOBL","LOCAL"}),
	0x802993F0: main.sym("L80299B0C", flag={"GLOBL","LOCAL"}),
	0x80299438: main.sym("L80299B54", flag={"GLOBL","LOCAL"}),
	0x80299480: main.sym("L80299B9C", flag={"GLOBL","LOCAL"}),
	0x802994C8: main.sym("L80299BE4", flag={"GLOBL","LOCAL"}),
	0x80299510: main.sym("L80299C2C", flag={"GLOBL","LOCAL"}),
	0x80299558: main.sym("L80299C74", flag={"GLOBL","LOCAL"}),
	0x802995A0: main.sym("L80299CBC", flag={"GLOBL","LOCAL"}),
	0x802995E8: main.sym("L80299D04", flag={"GLOBL","LOCAL"}),
	0x80299630: main.sym("L80299D4C", flag={"GLOBL","LOCAL"}),
	0x80299678: main.sym("L80299D94", flag={"GLOBL","LOCAL"}),
	0x802996C0: main.sym("L80299DDC", flag={"GLOBL","LOCAL"}),
	0x80299708: main.sym("L80299E24", flag={"GLOBL","LOCAL"}),
	0x80299750: main.sym("L80299E6C", flag={"GLOBL","LOCAL"}),
	0x80299798: main.sym("L80299EB4", flag={"GLOBL","LOCAL"}),
	0x802997E0: main.sym("L80299EFC", flag={"GLOBL","LOCAL"}),
	0x80299828: main.sym("L80299F44", flag={"GLOBL","LOCAL"}),
	0x80299870: main.sym("L80299F8C", flag={"GLOBL","LOCAL"}),
	0x802998B8: main.sym("L80299FD4", flag={"GLOBL","LOCAL"}),
	0x80299900: main.sym("L8029A01C", flag={"GLOBL","LOCAL"}),
	0x80299948: main.sym("L8029A064", flag={"GLOBL","LOCAL"}),
	0x80299990: main.sym("L8029A0AC", flag={"GLOBL","LOCAL"}),
	0x802999D8: main.sym("L8029A0F4", flag={"GLOBL","LOCAL"}),
	0x80299A20: main.sym("L8029A13C", flag={"GLOBL","LOCAL"}),
	0x80299A68: main.sym("L8029A184", flag={"GLOBL","LOCAL"}),
	0x80299AB0: main.sym("L8029A1CC", flag={"GLOBL","LOCAL"}),
	0x80299AF8: main.sym("L8029A214", flag={"GLOBL","LOCAL"}),
	0x80299BDC: main.sym("camera_8029A2F8"),
	0x80299C60: main.sym("camera_8029A37C"),
	0x80299C98: main.sym("camera_8029A3B4"),
	0x80299D00: main.sym("camera_8029A41C"),
	0x80299DB4: main.sym("camera_8029A4D0"),
	#0x8029A5BC: main.sym("camera_8029A5BC"),
	0x80299ECC: main.sym("camera_8029A5E8"),
	0x80299EF0: main.sym("camera_8029A60C"),
	0x80299F30: main.sym("camera_8029A64C"),
	0x80299F54: main.sym("camera_8029A670"),
	0x80299F78: main.sym("camera_8029A694"),
	0x80299FD8: main.sym("camera_8029A6F4"),
	#0x8029A81C: main.sym("camera_8029A81C"),
	0x8029A13C: main.sym("camera_8029A858"),
	0x8029A178: main.sym("camera_8029A894"),
	0x8029A1B4: main.sym("camera_8029A8D0"),
	0x8029A24C: main.sym("camera_8029A968"),
	0x8029A288: main.sym("camera_8029A9A4"),
	#0x8029AA3C: main.sym("CtrlPerspective", flag={"GLOBL"}),
	0x8029A390: main.sym("L8029AAAC", flag={"GLOBL","LOCAL"}),
	0x8029A3A0: main.sym("L8029AABC", flag={"GLOBL","LOCAL"}),
	0x8029A3B0: main.sym("L8029AACC", flag={"GLOBL","LOCAL"}),
	0x8029A3C0: main.sym("L8029AADC", flag={"GLOBL","LOCAL"}),
	0x8029A3D0: main.sym("L8029AAEC", flag={"GLOBL","LOCAL"}),
	0x8029A3E0: main.sym("L8029AAFC", flag={"GLOBL","LOCAL"}),
	0x8029A3F0: main.sym("L8029AB0C", flag={"GLOBL","LOCAL"}),
	0x8029A400: main.sym("L8029AB1C", flag={"GLOBL","LOCAL"}),
	0x8029A410: main.sym("L8029AB2C", flag={"GLOBL","LOCAL"}),
	0x8029A420: main.sym("L8029AB3C", flag={"GLOBL","LOCAL"}),
	0x8029A430: main.sym("L8029AB4C", flag={"GLOBL","LOCAL"}),
	0x8029A440: main.sym("L8029AB5C", flag={"GLOBL","LOCAL"}),
	0x8029A478: main.sym("camera_8029AB94"),
	0x8029A494: main.sym("camera_8029ABB0"),
	0x8029A514: main.sym("camera_8029AC30"),
	#0x8029AD80: main.sym("camera_8029AD80"),
	#0x8029AE40: main.sym("camera_8029AE40"),
	0x8029A7DC: main.sym("camera_8029AEF8"),
	0x8029A87C: main.sym("camera_8029AF98"),
	#0x8029B08C: main.sym("camera_8029B08C", flag={"GLOBL"}),
	0x8029AB70: main.sym("camera_8029B28C"),
	0x8029AC3C: main.sym("camera_8029B358"),
	0x8029ACAC: main.sym("camera_8029B3C8"),
	#0x8029B49C: main.sym("camera_8029B49C", flag={"GLOBL"}),
	#0x8029BDE4: main.sym("camera_8029BDE4", flag={"GLOBL"}),
	#0x8029BF64: main.sym("camera_8029BF64", flag={"GLOBL"}),
	0x8029B964: main.sym("camera_8029C0E4"),
	#0x8029C254: main.sym("camera_8029C254", flag={"GLOBL"}),
	0x8029BB7C: main.sym("L8029C2FC", flag={"GLOBL","LOCAL"}),
	0x8029BBA0: main.sym("L8029C320", flag={"GLOBL","LOCAL"}),
	0x8029BBC4: main.sym("L8029C344", flag={"GLOBL","LOCAL"}),
	0x8029BDD4: main.sym("L8029C554", flag={"GLOBL","LOCAL"}),
	0x8029BE6C: main.sym("L8029C5EC", flag={"GLOBL","LOCAL"}),

	# src/course.c
	0x8029BFF0: main.sym("CourseInit", flag={"GLOBL"}),

	# src/object.c
	0x8029C000: main.sym("Player_CopyInfo"),
	0x8029C24C: main.sym("Player_SetEffect"),
	0x8029C2D8: main.sym("Mario_Proc", flag={"GLOBL"}),
	0x8029C3B4: main.sym("ObjListExecNormal"),
	0x8029C448: main.sym("ObjListExecFrozen"),
	0x8029C5A8: main.sym("ObjListExec"),
	0x8029C618: main.sym("ObjListCleanup"),
	0x8029C6D8: main.sym("ObjSetActorFlag", flag={"GLOBL"}),
	0x8029C75C: main.sym("ObjectClose", flag={"GLOBL"}),
	0x8029C830: main.sym("ObjectOpen", flag={"GLOBL"}),
	0x8029CA50: main.sym("object_8029D1D8"),
	0x8029CA60: main.sym("ObjectInit", flag={"GLOBL"}),
	0x8029CB9C: main.sym("ObjectExec1"),
	0x8029CBEC: main.sym("ObjectExec2"),
	0x8029CCA0: main.sym("ObjectCleanup"),
	0x8029CD48: main.sym("object_8029D4D0"),
	0x8029CF08: main.sym("ObjectProc", flag={"GLOBL"}),

	# src/objectlib.c
	0x8029D100: main.sym("CtrlObjectHand", flag={"GLOBL"}),
	#0x8029D924: main.sym("CtrlObjectAlpha", flag={"GLOBL"}),
	#0x8029DB48: main.sym("CtrlObjectShape", flag={"GLOBL"}),
	#0x8029DBD4: main.sym("CtrlArea", flag={"GLOBL"}),
	0x8029D558: main.sym("ObjSetPosRelXFM", flag={"GLOBL"}),
	0x8029D62C: main.sym("ObjFMtxScaleCopy", flag={"GLOBL"}),
	0x8029D704: main.sym("FMtxInvCatAffine", flag={"GLOBL"}),
	0x8029DA34: main.sym("ObjectSetTake", flag={"GLOBL"}),
	0x8029DB00: main.sym("ObjCalcDist2D", flag={"GLOBL"}),
	0x8029DB7C: main.sym("ObjCalcDist3D", flag={"GLOBL"}),
	0x8029DC1C: main.sym("ObjectAccelerate", flag={"GLOBL"}),
	0x8029DC6C: main.sym("Accelerate", flag={"GLOBL"}),
	0x8029DD18: main.sym("ApproachPos", flag={"GLOBL"}),
	0x8029DDB4: main.sym("ApproachAng", flag={"GLOBL"}),
	0x8029DE70: main.sym("ObjectTurn", flag={"GLOBL"}),
	0x8029DF18: main.sym("ObjCalcAngY", flag={"GLOBL"}),
	0x8029DF98: main.sym("ObjectTurnTo", flag={"GLOBL"}),
	0x8029E140: main.sym("ObjSetRel", flag={"GLOBL"}),
	0x8029E198: main.sym("ObjSetPos", flag={"GLOBL"}),
	0x8029E1F0: main.sym("ObjSetAng", flag={"GLOBL"}),
	0x8029E230: main.sym("ObjMakeAt", flag={"GLOBL"}),
	0x8029E2A8: main.sym("ObjMakeRel", flag={"GLOBL"}),
	#0x8029EAAC: main.sym("ObjMakeHereMtx"),
	0x8029E388: main.sym("ObjMakeSplash", flag={"GLOBL"}),
	0x8029E5A4: main.sym("ObjMake", flag={"GLOBL"}),
	0x8029E650: main.sym("ObjMakeHere", flag={"GLOBL"}),
	0x8029E6A8: main.sym("ObjMakeEffect", flag={"GLOBL"}),
	0x8029E73C: main.sym("ObjMakeHereScale", flag={"GLOBL"}),
	0x8029E7A4: main.sym("ObjAddRelPos"),
	0x8029E7E8: main.sym("ObjMakeRelHere", flag={"GLOBL"}),
	0x8029E880: main.sym("ObjMakeRelHereScale", flag={"GLOBL"}),
	#0x8029F070: main.sym("ObjectMove3D"),
	0x8029E94C: main.sym("ObjCopyShapeOff", flag={"GLOBL"}),
	0x8029E964: main.sym("ObjCopyCoord", flag={"GLOBL"}),
	0x8029E9A4: main.sym("ObjCopyPos", flag={"GLOBL"}),
	0x8029E9CC: main.sym("ObjCopyAng"),
	0x8029EA0C: main.sym("ObjSetShapePos", flag={"GLOBL"}),
	#0x8029F1B0: main.sym("ObjStartAnime"),
	0x8029EA84: main.sym("MtxTransform3", flag={"GLOBL"}),
	0x8029EAF8: main.sym("InvTransform3", flag={"GLOBL"}),
	0x8029EB70: main.sym("ObjScaleMtx"),
	0x8029EC2C: main.sym("ObjCopyScale", flag={"GLOBL"}),
	0x8029EC54: main.sym("ObjSetScaleXYZ", flag={"GLOBL"}),
	0x8029EC88: main.sym("ObjSetScale", flag={"GLOBL"}),
	0x8029ECB4: main.sym("ObjectSetScale", flag={"GLOBL"}),
	0x8029ECE8: main.sym("ObjectStartAnime", flag={"GLOBL"}),
	0x8029ED38: main.sym("ObjectSetAnime", flag={"GLOBL"}),
	0x8029ED98: main.sym("ObjectSetAnimeV", flag={"GLOBL"}),
	0x8029EE20: main.sym("ObjInitAnime", flag={"GLOBL"}),
	#0x8029F600: main.sym("ObjActivate"),
	0x8029EEA4: main.sym("ObjectSetActive", flag={"GLOBL"}),
	#0x8029F644: main.sym("ObjDeactivate"),
	0x8029EEF0: main.sym("ObjectClrActive", flag={"GLOBL"}),
	0x8029EF18: main.sym("ObjectShow", flag={"GLOBL"}),
	0x8029EF40: main.sym("ObjectHide", flag={"GLOBL"}),
	0x8029EF64: main.sym("ObjectSetPosOff", flag={"GLOBL"}),
	0x8029F05C: main.sym("ObjectSetPosOffParent"),
	0x8029F0A4: main.sym("objectlib_8029F820", flag={"GLOBL"}),
	#0x8029F848: main.sym("objectlib_8029F848"),
	0x8029F170: main.sym("ObjSetShapeAng", flag={"GLOBL"}),
	0x8029F198: main.sym("ObjGetScriptType", flag={"GLOBL"}),
	0x8029F1E0: main.sym("ObjectFindObj", flag={"GLOBL"}),
	0x8029F21C: main.sym("ObjectFindDist", flag={"GLOBL"}),
	0x8029F270: main.sym("ObjectFind", flag={"GLOBL"}),
	0x8029F3A0: main.sym("ObjGetEffect", flag={"GLOBL"}),
	#0x8029FB68: main.sym("ObjCountEffect"),
	0x8029F460: main.sym("ObjCount", flag={"GLOBL"}),
	0x8029F520: main.sym("ObjectFindTake", flag={"GLOBL"}),
	0x8029F610: main.sym("ObjectResetState"),
	0x8029F638: main.sym("ObjectInitState", flag={"GLOBL"}),
	0x8029F684: main.sym("ObjectMatchP1Speed", flag={"GLOBL"}),
	0x8029F6F0: main.sym("ObjectAnimeHold", flag={"GLOBL"}),
	0x8029F728: main.sym("ObjectAnimeHoldEnd", flag={"GLOBL"}),
	0x8029F788: main.sym("objectlib_8029FF04", flag={"GLOBL"}),
	0x8029F828: main.sym("objectlib_8029FFA4", flag={"GLOBL"}),
	0x8029F88C: main.sym("ObjectIsAnimeFrame", flag={"GLOBL"}),
	0x8029F8D4: main.sym("ObjectIsAnimeFrameRange", flag={"GLOBL"}),
	#0x802A00AC: main.sym("ObjectIsAnimeFrameTable"),
	0x8029F998: main.sym("Player1IsJump", flag={"GLOBL"}),
	0x8029F9D8: main.sym("objectlib_802A0154", flag={"GLOBL"}),
	0x8029FA1C: main.sym("ObjectSetAnimeJump", flag={"GLOBL"}),
	0x8029FA5C: main.sym("objectlib_802A01D8", flag={"GLOBL"}),
	0x8029FAB8: main.sym("objectlib_802A0234"),
	0x8029FC04: main.sym("objectlib_802A0380", flag={"GLOBL"}),
	0x8029FCF8: main.sym("objectlib_802A0474", flag={"GLOBL"}),
	0x8029FD44: main.sym("ObjectSetShape", flag={"GLOBL"}),
	#0x802A04F0: main.sym("Player1SetFlag"),
	0x8029FD98: main.sym("ObjectCheckHitResult", flag={"GLOBL"}),
	0x8029FDEC: main.sym("ObjKill", flag={"GLOBL"}),
	0x8029FE00: main.sym("objectlib_802A057C", flag={"GLOBL"}),
	0x8029FE38: main.sym("ObjectHitOFF", flag={"GLOBL"}),
	0x8029FE58: main.sym("ObjectHitON", flag={"GLOBL"}),
	0x8029FE74: main.sym("ObjHitON", flag={"GLOBL"}),
	0x8029FE88: main.sym("ObjectCheckGroundY", flag={"GLOBL"}),
	0x8029FED0: main.sym("ObjectCheckGround", flag={"GLOBL"}),
	0x8029FF20: main.sym("CalcDrag"),
	0x802A0020: main.sym("ObjectCalcDrag", flag={"GLOBL"}),
	0x802A006C: main.sym("objectlib_802A07E8"),
	0x802A0334: main.sym("objectlib_802A0AB0"),
	0x802A0460: main.sym("objectlib_802A0BDC"),
	0x802A0608: main.sym("objectlib_802A0D84"),
	0x802A06EC: main.sym("objectlib_802A0E68", flag={"GLOBL"}),
	#0x802A10E0: main.sym("objectlib_802A10E0"),
	0x802A0974: main.sym("CheckFlag"),
	#0x802A113C: main.sym("ObjectHitWall"),
	0x802A0A2C: main.sym("DeltaAng", flag={"GLOBL"}),
	0x802A0A90: main.sym("ObjectMoveF", flag={"GLOBL"}),
	0x802A0B28: main.sym("ObjectMoveY", flag={"GLOBL"}),
	0x802A0B8C: main.sym("ObjectCalcVelF", flag={"GLOBL"}),
	0x802A0BF4: main.sym("objectlib_802A1370", flag={"GLOBL"}),
	0x802A0CA8: main.sym("ObjIsObjHit", flag={"GLOBL"}),
	0x802A0D10: main.sym("ObjectSetScript", flag={"GLOBL"}),
	0x802A0D48: main.sym("ObjSetScript", flag={"GLOBL"}),
	0x802A0D80: main.sym("ObjectHasScript", flag={"GLOBL"}),
	0x802A0DD8: main.sym("ObjHasScript", flag={"GLOBL"}),
	0x802A0E30: main.sym("ObjectDistMarioToSave", flag={"GLOBL"}),
	0x802A0EB8: main.sym("ObjectDistToSave", flag={"GLOBL"}),
	#0x802A16AC: main.sym("ObjectInSaveSquare"),
	#0x802A1774: main.sym("ObjectInSaveRect"),
	0x802A10D0: main.sym("ObjectSavePos", flag={"GLOBL"}),
	0x802A1110: main.sym("ObjectSavePosStop", flag={"GLOBL"}),
	0x802A1160: main.sym("ObjectShake", flag={"GLOBL"}),
	0x802A11B4: main.sym("objectlib_802A1930", flag={"GLOBL"}),
	#0x802A1960: main.sym("objectlib_802A1960"),
	0x802A1230: main.sym("ObjSetBillboard", flag={"GLOBL"}),
	0x802A124C: main.sym("ObjectSetHitBox", flag={"GLOBL"}),
	0x802A1274: main.sym("ObjectSetDmgBox", flag={"GLOBL"}),
	0x802A129C: main.sym("ObjectMakeCoinCommon"),
	0x802A13B8: main.sym("objectlib_802A1B34"),
	0x802A1410: main.sym("ObjectMakeCoin", flag={"GLOBL"}),
	0x802A1460: main.sym("objectlib_802A1BDC", flag={"GLOBL"}),
	#0x802A1C68: main.sym("ObjectDistToSaveY"),
	#0x802A1CC4: main.sym("objectlib_802A1CC4"),
	0x802A1600: main.sym("objectlib_802A1D7C"),
	0x802A17C0: main.sym("ObjectCheckWall", flag={"GLOBL"}),
	0x802A1978: main.sym("objectlib_802A20F4"),
	0x802A1A2C: main.sym("objectlib_802A21D4"),
	0x802A1B78: main.sym("objectlib_802A2320", flag={"GLOBL"}),
	0x802A1BA0: main.sym("objectlib_802A2348", flag={"GLOBL"}),
	0x802A1D28: main.sym("objectlib_802A24D0"),
	0x802A1E0C: main.sym("ObjectProcMove", flag={"GLOBL"}),
	0x802A1E9C: main.sym("ObjectProcMoveF", flag={"GLOBL"}),
	#0x802A2674: main.sym("ObjCopyCoordOff"),
	0x802A1FA0: main.sym("ObjectAngToSave", flag={"GLOBL"}),
	0x802A2008: main.sym("ObjCopyCoordToShape", flag={"GLOBL"}),
	0x802A205C: main.sym("ObjAddTransform", flag={"GLOBL"}),
	0x802A2188: main.sym("ObjCalcMtx", flag={"GLOBL"}),
	0x802A2270: main.sym("ObjSetMtx", flag={"GLOBL"}),
	0x802A22DC: main.sym("ObjCalcRel", flag={"GLOBL"}),
	#0x802A2B28: main.sym("ObjClrRel"),
	#0x802A2B6C: main.sym("ObjectRotate"),
	0x802A241C: main.sym("ObjectRotateShape", flag={"GLOBL"}),
	#0x802A2C1C: main.sym("ObjectSyncAng"),
	0x802A24B4: main.sym("ObjectProcPath", flag={"GLOBL"}),
	0x802A272C: main.sym("ChainInit", flag={"GLOBL"}),
	0x802A276C: main.sym("RandRange", flag={"GLOBL"}),
	0x802A27B4: main.sym("ObjRandScale", flag={"GLOBL"}),
	0x802A2818: main.sym("ObjRandOff3D", flag={"GLOBL"}),
	0x802A28E4: main.sym("ObjRandOff2D", flag={"GLOBL"}),
	0x802A297C: main.sym("ObjCalcVelULF"),
	0x802A2A38: main.sym("ObjectMoveULF", flag={"GLOBL"}),
	0x802A2AC0: main.sym("objectlib_802A3268", flag={"GLOBL"}),
	0x802A2B04: main.sym("ObjectMakeParticle", flag={"GLOBL"}),
	0x802A2CFC: main.sym("ObjSetHitInfo", flag={"GLOBL"}),
	0x802A2E5C: main.sym("GetSign", flag={"GLOBL"}),
	0x802A2E8C: main.sym("fabsf", flag={"GLOBL"}),
	0x802A2ECC: main.sym("abs", flag={"GLOBL"}),
	0x802A2EFC: main.sym("ObjectFlash", flag={"GLOBL"}),
	0x802A2FAC: main.sym("objectlib_802A3754", flag={"GLOBL"}),
	0x802A3004: main.sym("objectlib_802A37AC", flag={"GLOBL"}),
	0x802A3034: main.sym("objectlib_802A37DC", flag={"GLOBL"}),
	0x802A3070: main.sym("ObjectRepelMario2D", flag={"GLOBL"}),
	0x802A3164: main.sym("ObjectRepelMario3D", flag={"GLOBL"}),
	#0x802A399C: main.sym("objectlib_802A399C", flag={"GLOBL"}),
	#0x802A3A3C: main.sym("objectlib_802A3A3C"),
	0x802A32A4: main.sym("objectlib_802A3A4C", flag={"GLOBL"}),
	0x802A32E0: main.sym("objectlib_802A3A88", flag={"GLOBL"}),
	#0x802A3B28: main.sym("objectlib_802A3B28"),
	0x802A3398: main.sym("ObjectScaleTime", flag={"GLOBL"}),
	0x802A3470: main.sym("ObjectDebugPos", flag={"GLOBL"}),
	#0x802A3CEC: main.sym("objectlib_802A3CEC"),
	0x802A3554: main.sym("ObjectIsMarioRide", flag={"GLOBL"}),
	#0x802A3D40: main.sym("objectlib_802A3D40"),
	0x802A362C: main.sym("objectlib_802A3DD4", flag={"GLOBL"}),
	0x802A3688: main.sym("ObjectCallState", flag={"GLOBL"}),
	0x802A36D8: main.sym("objectlib_802A3E80"),
	#0x802A3EF8: main.sym("objectlib_802A3EF8"),
	0x802A377C: main.sym("GetBit", flag={"GLOBL"}),
	0x802A37A0: main.sym("objectlib_802A3F48", flag={"GLOBL"}),
	0x802A38A4: main.sym("objectlib_802A404C", flag={"GLOBL"}),
	0x802A3910: main.sym("InTable", flag={"GLOBL"}),
	#0x802A4110: main.sym("objectlib_802A4110"),
	0x802A3978: main.sym("ObjectAreaInit", flag={"GLOBL"}),
	0x802A3A68: main.sym("ObjectAreaProc", flag={"GLOBL"}),
	0x802A3BB8: main.sym("objectlib_802A4360", flag={"GLOBL"}),
	0x802A3C98: main.sym("objectlib_802A4440", flag={"GLOBL"}),
	0x802A3D4C: main.sym("ObjSetMap", flag={"GLOBL"}),
	0x802A3D84: main.sym("objectlib_802A452C", flag={"GLOBL"}),
	0x802A3DBC: main.sym("objectlib_802A4564", flag={"GLOBL"}),
	#0x802A45E4: main.sym("Ctrl_objectlib_802A45E4", flag={"GLOBL"}),
	#0x802A462C: main.sym("Ctrl_objectlib_802A462C"),
	0x802A3F24: main.sym("ObjIsHide", flag={"GLOBL"}),
	0x802A3F5C: main.sym("objectlib_802A4704", flag={"GLOBL"}),
	0x802A3F80: main.sym("objectlib_802A4728", flag={"GLOBL"}),
	0x802A3FA8: main.sym("objectlib_802A4750", flag={"GLOBL"}),
	0x802A3FCC: main.sym("objectlib_802A4774", flag={"GLOBL"}),
	0x802A3FF8: main.sym("objectlib_802A47A0", flag={"GLOBL"}),
	0x802A4114: main.sym("objectlib_802A48BC", flag={"GLOBL"}),
	0x802A4154: main.sym("objectlib_802A48FC"),
	0x802A41B8: main.sym("objectlib_802A4960", flag={"GLOBL"}),
	0x802A420C: main.sym("L802A49B4", flag={"GLOBL","LOCAL"}),
	0x802A4268: main.sym("L802A4A28", flag={"GLOBL","LOCAL"}),
	0x802A4298: main.sym("L802A4A58", flag={"GLOBL","LOCAL"}),
	0x802A42EC: main.sym("L802A4AAC", flag={"GLOBL","LOCAL"}),
	0x802A4370: main.sym("L802A4B30", flag={"GLOBL","LOCAL"}),
	0x802A4424: main.sym("objectlib_802A4BE4", flag={"GLOBL"}),
	0x802A472C: main.sym("ObjectHasShapeID", flag={"GLOBL"}),
	0x802A4780: main.sym("ObjectStand", flag={"GLOBL"}),
	#0x802A5034: main.sym("MarioInRect"),
	0x802A4924: main.sym("objectlib_802A50FC", flag={"GLOBL"}),
	0x802A4964: main.sym("objectlib_802A513C", flag={"GLOBL"}),
	0x802A49D4: main.sym("objectlib_802A51AC", flag={"GLOBL"}),
	0x802A4A50: main.sym("ObjCopyActorInfo", flag={"GLOBL"}),
	0x802A4A70: main.sym("ObjectSetAnimeFrame", flag={"GLOBL"}),
	0x802A4AB0: main.sym("objectlib_802A5288", flag={"GLOBL"}),
	0x802A4AEC: main.sym("ObjectSetAnimeHoldEnd", flag={"GLOBL"}),
	0x802A4B20: main.sym("objectlib_802A52F8", flag={"GLOBL"}),
	0x802A4B80: main.sym("objectlib_802A5358", flag={"GLOBL"}),
	#0x802A540C: main.sym("objectlib_802A540C"),
	#0x802A5460: main.sym("objectlib_802A5460"),
	0x802A4CC0: main.sym("objectlib_802A5498", flag={"GLOBL"}),
	0x802A4D00: main.sym("objectlib_802A54D8", flag={"GLOBL"}),
	0x802A4D4C: main.sym("objectlib_802A5524", flag={"GLOBL"}),

	# src/object_a.c
	0x802A4DB0: main.sym("object_a_802A5620"),
	#0x802A56BC: main.sym("object_a_802A56BC", flag={"GLOBL"}),
	0x802A4E94: main.sym("L802A5704", flag={"GLOBL","LOCAL"}),
	0x802A4EF8: main.sym("L802A5768", flag={"GLOBL","LOCAL"}),
	0x802A4F80: main.sym("L802A57F0", flag={"GLOBL","LOCAL"}),
	0x802A4FB4: main.sym("L802A5824", flag={"GLOBL","LOCAL"}),
	0x802A5034: main.sym("L802A58A4", flag={"GLOBL","LOCAL"}),
	#0x802A58DC: main.sym("object_a_802A58DC", flag={"GLOBL"}),
	0x802A510C: main.sym("object_a_802A597C", flag={"GLOBL"}),
	0x802A51D4: main.sym("object_a_802A5A44", flag={"GLOBL"}),
	#0x802A5AA0: main.sym("object_a_802A5AA0", flag={"GLOBL"}),
	0x802A525C: main.sym("object_a_802A5ACC"),
	#0x802A5BD4: main.sym("object_a_802A5BD4", flag={"GLOBL"}),
	0x802A54DC: main.sym("object_a_802A5D4C", flag={"GLOBL"}),
	0x802A5CA8: main.sym("object_a_802A6518", flag={"GLOBL"}),
	0x802A6030: main.sym("object_a_802A68A0", flag={"GLOBL"}),
	0x802A6268: main.sym("object_a_802A6AD8", flag={"GLOBL"}),
	#0x802A6B7C: main.sym("object_a_802A6B7C", flag={"GLOBL"}),
	#0x802A6C20: main.sym("object_a_802A6C20", flag={"GLOBL"}),
	#0x802A6C74: main.sym("object_a_802A6C74", flag={"GLOBL"}),
	#0x802A6CF4: main.sym("object_a_802A6CF4", flag={"GLOBL"}),
	#0x802A6D64: main.sym("object_a_802A6D64", flag={"GLOBL"}),
	0x802A6680: main.sym("object_a_802A6EE4", flag={"GLOBL"}),
	0x802A67BC: main.sym("object_a_802A7020", flag={"GLOBL"}),
	0x802A6828: main.sym("object_a_802A708C", flag={"GLOBL"}),
	0x802A68FC: main.sym("object_a_802A7160", flag={"GLOBL"}),
	#0x802A7170: main.sym("object_a_802A7170", flag={"GLOBL"}),
	#0x802A719C: main.sym("Ctrl_object_a_802A719C", flag={"GLOBL"}),
	#0x802A7230: main.sym("object_a_802A7230", flag={"GLOBL"}),
	0x802A6A00: main.sym("object_a_802A7264", flag={"GLOBL"}),
	0x802A6AF8: main.sym("object_a_802A7384"),
	0x802A6B4C: main.sym("object_a_802A73D8", flag={"GLOBL"}),
	0x802A6D0C: main.sym("object_a_802A7598", flag={"GLOBL"}),
	0x802A6F78: main.sym("object_a_802A7804", flag={"GLOBL"}),
	0x802A704C: main.sym("object_a_802A78D8", flag={"GLOBL"}),
	0x802A71D4: main.sym("object_a_802A7A60", flag={"GLOBL"}),
	0x802A72A8: main.sym("object_a_802A7B1C", flag={"GLOBL"}),
	0x802A72E8: main.sym("object_a_802A7B5C", flag={"GLOBL"}),
	0x802A74A0: main.sym("object_a_802A7D14", flag={"GLOBL"}),
	0x802A74D8: main.sym("L802A7D4C", flag={"GLOBL","LOCAL"}),
	0x802A7594: main.sym("L802A7E08", flag={"GLOBL","LOCAL"}),
	0x802A7668: main.sym("L802A7EDC", flag={"GLOBL","LOCAL"}),
	0x802A7694: main.sym("L802A7F08", flag={"GLOBL","LOCAL"}),
	0x802A76FC: main.sym("L802A7F70", flag={"GLOBL","LOCAL"}),
	0x802A7748: main.sym("object_a_802A7FBC"),
	#0x802A8064: main.sym("object_a_802A8064", flag={"GLOBL"}),
	#0x802A816C: main.sym("object_a_802A816C", flag={"GLOBL"}),
	#0x802A81E8: main.sym("object_a_802A81E8", flag={"GLOBL"}),
	#0x802A821C: main.sym("object_a_802A821C", flag={"GLOBL"}),
	#0x802A8370: main.sym("object_a_802A8370", flag={"GLOBL"}),
	#0x802A83A0: main.sym("object_a_802A83A0", flag={"GLOBL"}),
	#0x802A8630: main.sym("object_a_802A8630", flag={"GLOBL"}),
	#0x802A86BC: main.sym("object_a_802A86BC"),
	#0x802A870C: main.sym("object_a_802A870C", flag={"GLOBL"}),
	#0x802A88A4: main.sym("object_a_802A88A4", flag={"GLOBL"}),
	0x802A81C4: main.sym("object_a_802A8A38"),
	#0x802A8B18: main.sym("object_a_802A8B18", flag={"GLOBL"}),
	#0x802A8BC0: main.sym("object_a_802A8BC0", flag={"GLOBL"}),
	#0x802A8C88: main.sym("object_a_802A8C88", flag={"GLOBL"}),
	#0x802A8CDC: main.sym("object_a_802A8CDC", flag={"GLOBL"}),
	#0x802A8D48: main.sym("object_a_802A8D48", flag={"GLOBL"}),
	#0x802A8D98: main.sym("object_a_802A8D98", flag={"GLOBL"}),
	0x802A854C: main.sym("object_a_802A8DC0", flag={"GLOBL"}),
	0x802A86CC: main.sym("object_a_802A8F40", flag={"GLOBL"}),
	0x802A88A0: main.sym("object_a_802A9114", flag={"GLOBL"}),
	0x802A8A88: main.sym("object_a_802A92FC", flag={"GLOBL"}),
	0x802A8B84: main.sym("object_a_802A93F8", flag={"GLOBL"}),
	0x802A8BCC: main.sym("object_a_802A9440", flag={"GLOBL"}),
	0x802A8BEC: main.sym("object_a_802A9460", flag={"GLOBL"}),
	0x802A9120: main.sym("object_a_802A9994", flag={"GLOBL"}),
	#0x802A94F8: main.sym("object_a_802A94F8", flag={"GLOBL"}),
	0x802A8D18: main.sym("object_a_802A958C"),
	#0x802A9708: main.sym("object_a_802A9708", flag={"GLOBL"}),
	#0x802A973C: main.sym("object_a_802A973C"),
	0x802A9050: main.sym("object_a_802A98C4"),
	#0x802A9994: main.sym("object_a_802A9994", flag={"GLOBL"}),
	0x802A9494: main.sym("object_a_802A9D08", flag={"GLOBL"}),
	0x802A96E0: main.sym("object_a_802A9F54", flag={"GLOBL"}),
	0x802A9754: main.sym("object_a_802A9FC8", flag={"GLOBL"}),
	0x802A97B8: main.sym("object_a_802AA02C"),
	#0x802AA0AC: main.sym("object_a_802AA0AC", flag={"GLOBL"}),
	#0x802AA1B8: main.sym("object_a_802AA1B8", flag={"GLOBL"}),
	0x802A9A0C: main.sym("object_a_802AA280"),
	0x802A9B54: main.sym("object_a_802AA3C8"),
	#0x802AA3F4: main.sym("object_a_802AA3F4", flag={"GLOBL"}),
	#0x802AA700: main.sym("object_a_802AA700", flag={"GLOBL"}),
	#0x802AA774: main.sym("object_a_802AA774", flag={"GLOBL"}),
	#0x802AA830: main.sym("object_a_802AA830", flag={"GLOBL"}),
	0x802AA0D4: main.sym("object_a_802AA948"),
	#0x802AA97C: main.sym("object_a_802AA97C", flag={"GLOBL"}),
	#0x802AAA60: main.sym("object_a_802AAA60", flag={"GLOBL"}),
	#0x802AAB54: main.sym("object_a_802AAB54", flag={"GLOBL"}),
	#0x802AAC48: main.sym("object_a_802AAC48", flag={"GLOBL"}),
	0x802AA618: main.sym("object_a_802AAE8C", flag={"GLOBL"}),
	#0x802AAF48: main.sym("object_a_802AAF48", flag={"GLOBL"}),
	0x802AA788: main.sym("object_a_802AAFFC"),
	0x802AA7EC: main.sym("object_a_802AB060"),
	0x802AA8E4: main.sym("object_a_802AB158"),
	0x802AA918: main.sym("object_a_802AB18C"),
	#0x802AB1C8: main.sym("object_a_802AB1C8", flag={"GLOBL"}),
	0x802AACE4: main.sym("object_a_802AB558", flag={"GLOBL"}),
	0x802AAD54: main.sym("object_a_802AB5C8"),
	#0x802AB650: main.sym("object_a_802AB650", flag={"GLOBL"}),
	#0x802AB70C: main.sym("object_a_802AB70C", flag={"GLOBL"}),
	#0x802AB748: main.sym("object_a_802AB748", flag={"GLOBL"}),
	#0x802AB7A4: main.sym("object_a_802AB7A4", flag={"GLOBL"}),
	#0x802AB860: main.sym("object_a_802AB860", flag={"GLOBL"}),
	#0x802ABA40: main.sym("object_a_802ABA40", flag={"GLOBL"}),
	0x802AB364: main.sym("object_a_802ABC04"),
	0x802AB3D0: main.sym("L802ABC70", flag={"GLOBL","LOCAL"}),
	0x802AB408: main.sym("L802ABCA8", flag={"GLOBL","LOCAL"}),
	0x802AB458: main.sym("L802ABCF8", flag={"GLOBL","LOCAL"}),
	0x802AB4E8: main.sym("L802ABD88", flag={"GLOBL","LOCAL"}),
	0x802AB580: main.sym("L802ABE20", flag={"GLOBL","LOCAL"}),
	#0x802ABEE4: main.sym("object_a_802ABEE4", flag={"GLOBL"}),
	#0x802ABF0C: main.sym("object_a_802ABF0C", flag={"GLOBL"}),
	0x802AB7C8: main.sym("object_a_802AC068", flag={"GLOBL"}),
	0x802AB8BC: main.sym("object_a_802AC15C", flag={"GLOBL"}),
	#0x802AC294: main.sym("object_a_802AC294", flag={"GLOBL"}),
	#0x802AC2C0: main.sym("object_a_802AC2C0", flag={"GLOBL"}),
	#0x802AC2EC: main.sym("object_a_802AC2EC", flag={"GLOBL"}),
	#0x802AC3A8: main.sym("object_a_802AC3A8", flag={"GLOBL"}),
	#0x802AC4A0: main.sym("object_a_802AC4A0", flag={"GLOBL"}),
	#0x802AC5B4: main.sym("object_a_802AC5B4", flag={"GLOBL"}),
	#0x802AC678: main.sym("object_a_802AC678", flag={"GLOBL"}),
	#0x802AC78C: main.sym("object_a_802AC78C", flag={"GLOBL"}),
	#0x802AC864: main.sym("object_a_802AC864", flag={"GLOBL"}),
	0x802AC070: main.sym("object_a_802AC910"),
	0x802AC0B8: main.sym("object_a_802AC958"),
	0x802AC130: main.sym("object_a_802AC9D0"),
	0x802AC1CC: main.sym("object_a_802ACA6C"),
	#0x802ACAC8: main.sym("object_a_802ACAC8", flag={"GLOBL"}),
	0x802AC2F0: main.sym("L802ACB90", flag={"GLOBL","LOCAL"}),
	0x802AC300: main.sym("L802ACBA0", flag={"GLOBL","LOCAL"}),
	0x802AC318: main.sym("L802ACBB8", flag={"GLOBL","LOCAL"}),
	0x802AC330: main.sym("L802ACBD0", flag={"GLOBL","LOCAL"}),
	0x802AC348: main.sym("L802ACBE8", flag={"GLOBL","LOCAL"}),
	#0x802ACC3C: main.sym("object_a_802ACC3C", flag={"GLOBL"}),
	0x802AC5E0: main.sym("object_a_802ACE80"),
	0x802AC7D8: main.sym("object_a_802AD078", flag={"GLOBL"}),
	0x802AC86C: main.sym("object_a_802AD10C", flag={"GLOBL"}),
	0x802AC904: main.sym("object_a_802AD1A4", flag={"GLOBL"}),
	0x802AC998: main.sym("object_a_802AD238", flag={"GLOBL"}),
	0x802ACA30: main.sym("object_a_802AD2D0", flag={"GLOBL"}),
	#0x802AD34C: main.sym("object_a_802AD34C", flag={"GLOBL"}),
	#0x802AD378: main.sym("object_a_802AD378", flag={"GLOBL"}),
	0x802ACCE0: main.sym("object_a_802AD580", flag={"GLOBL"}),
	0x802ACECC: main.sym("object_a_802AD76C", flag={"GLOBL"}),
	0x802ACF54: main.sym("object_a_802AD7F4", flag={"GLOBL"}),
	0x802ACF88: main.sym("object_a_802AD828", flag={"GLOBL"}),
	#0x802AD890: main.sym("object_a_802AD890", flag={"GLOBL"}),
	0x802AD01C: main.sym("object_a_802AD8BC"),
	0x802AD050: main.sym("object_a_802AD8F0", flag={"GLOBL"}),
	0x802AD1AC: main.sym("object_a_802ADA4C", flag={"GLOBL"}),
	0x802AD2E8: main.sym("object_a_802ADB88", flag={"GLOBL"}),
	0x802AD444: main.sym("object_a_802ADCE4", flag={"GLOBL"}),
	0x802AD4D0: main.sym("object_a_802ADD70", flag={"GLOBL"}),
	#0x802ADDF8: main.sym("object_a_802ADDF8", flag={"GLOBL"}),
	#0x802ADF6C: main.sym("object_a_802ADF6C", flag={"GLOBL"}),
	#0x802ADF98: main.sym("object_a_802ADF98", flag={"GLOBL"}),
	#0x802ADFD8: main.sym("object_a_802ADFD8", flag={"GLOBL"}),
	0x802AD82C: main.sym("object_a_802AE0CC", flag={"GLOBL"}),
	#0x802AE238: main.sym("object_a_802AE238", flag={"GLOBL"}),
	#0x802AE304: main.sym("object_a_802AE304", flag={"GLOBL"}),
	0x802ADA94: main.sym("object_a_802AE334", flag={"GLOBL"}),
	#0x802AE360: main.sym("object_a_802AE360", flag={"GLOBL"}),
	#0x802AE394: main.sym("object_a_802AE394"),
	0x802ADBBC: main.sym("object_a_802AE45C"),
	#0x802AE48C: main.sym("object_a_802AE48C", flag={"GLOBL"}),
	0x802ADC20: main.sym("object_a_802AE4C0", flag={"GLOBL"}),
	#0x802AE534: main.sym("object_a_802AE534", flag={"GLOBL"}),
	#0x802AE85C: main.sym("object_a_802AE85C", flag={"GLOBL"}),
	#0x802AE908: main.sym("object_a_802AE908", flag={"GLOBL"}),
	0x802AE1CC: main.sym("object_a_802AEA6C", flag={"GLOBL"}),
	0x802AE218: main.sym("object_a_802AEAB8", flag={"GLOBL"}),
	0x802AE27C: main.sym("object_a_802AEB1C", flag={"GLOBL"}),
	0x802AE2D4: main.sym("object_a_802AEB74", flag={"GLOBL"}),
	#0x802AEB9C: main.sym("object_a_802AEB9C", flag={"GLOBL"}),
	#0x802AEBC8: main.sym("object_a_802AEBC8", flag={"GLOBL"}),
	#0x802AEC40: main.sym("object_a_802AEC40", flag={"GLOBL"}),
	#0x802AECA8: main.sym("object_a_802AECA8", flag={"GLOBL"}),
	#0x802AECDC: main.sym("object_a_802AECDC", flag={"GLOBL"}),
	#0x802AEDC0: main.sym("object_a_802AEDC0", flag={"GLOBL"}),
	0x802AE594: main.sym("L802AEE34", flag={"GLOBL","LOCAL"}),
	0x802AE5C8: main.sym("L802AEE68", flag={"GLOBL","LOCAL"}),
	0x802AE5D0: main.sym("L802AEE70", flag={"GLOBL","LOCAL"}),
	#0x802AEEA4: main.sym("object_a_802AEEA4", flag={"GLOBL"}),
	#0x802AEF1C: main.sym("object_a_802AEF1C", flag={"GLOBL"}),
	0x802AE948: main.sym("object_a_802AF1E8", flag={"GLOBL"}),
	#0x802AF3FC: main.sym("object_a_802AF3FC", flag={"GLOBL"}),
	#0x802AF448: main.sym("object_a_802AF448", flag={"GLOBL"}),
	#0x802AF5F8: main.sym("object_a_802AF5F8", flag={"GLOBL"}),
	#0x802AF7C4: main.sym("object_a_802AF7C4", flag={"GLOBL"}),
	#0x802AF9CC: main.sym("object_a_802AF9CC", flag={"GLOBL"}),
	#0x802AFA0C: main.sym("object_a_802AFA0C", flag={"GLOBL"}),
	#0x802AFAE4: main.sym("object_a_802AFAE4", flag={"GLOBL"}),
	#0x802AFBF8: main.sym("object_a_802AFBF8", flag={"GLOBL"}),
	#0x802AFCE4: main.sym("object_a_802AFCE4", flag={"GLOBL"}),
	#0x802AFD1C: main.sym("object_a_802AFD1C", flag={"GLOBL"}),
	#0x802AFEE8: main.sym("object_a_802AFEE8", flag={"GLOBL"}),
	#0x802AFF30: main.sym("object_a_802AFF30", flag={"GLOBL"}),
	#0x802B00E4: main.sym("object_a_802B00E4", flag={"GLOBL"}),
	0x802AF9A4: main.sym("object_a_802B0244"),
	0x802AFAFC: main.sym("object_a_802B039C"),
	#0x802B04B4: main.sym("object_a_802B04B4", flag={"GLOBL"}),
	#0x802B0614: main.sym("object_a_802B0614", flag={"GLOBL"}),
	#0x802B0974: main.sym("object_a_802B0974", flag={"GLOBL"}),
	0x802B02FC: main.sym("object_a_802B0B9C"),
	#0x802B0BEC: main.sym("object_a_802B0BEC", flag={"GLOBL"}),
	0x802B039C: main.sym("L802B0C3C", flag={"GLOBL","LOCAL"}),
	0x802B03BC: main.sym("L802B0C5C", flag={"GLOBL","LOCAL"}),
	0x802B03EC: main.sym("L802B0C8C", flag={"GLOBL","LOCAL"}),
	0x802B041C: main.sym("L802B0CBC", flag={"GLOBL","LOCAL"}),
	0x802B044C: main.sym("L802B0CEC", flag={"GLOBL","LOCAL"}),
	#0x802B0D48: main.sym("object_a_802B0D48", flag={"GLOBL"}),
	#0x802B0DF0: main.sym("object_a_802B0DF0", flag={"GLOBL"}),
	#0x802B1278: main.sym("object_a_802B1278", flag={"GLOBL"}),
	0x802B0A10: main.sym("L802B12B0", flag={"GLOBL","LOCAL"}),
	0x802B0AA4: main.sym("L802B1344", flag={"GLOBL","LOCAL"}),
	0x802B0B00: main.sym("L802B13A0", flag={"GLOBL","LOCAL"}),
	0x802B0BD0: main.sym("L802B1470", flag={"GLOBL","LOCAL"}),
	0x802B0C14: main.sym("L802B14B4", flag={"GLOBL","LOCAL"}),
	0x802B0C54: main.sym("object_a_802B14F4"),
	#0x802B15E8: main.sym("object_a_802B15E8", flag={"GLOBL"}),
	0x802B0E74: main.sym("object_a_802B1714"),
	0x802B0F54: main.sym("object_a_802B17F4"),
	0x802B1138: main.sym("object_a_802B19D8"),
	#0x802B1AE0: main.sym("object_a_802B1AE0", flag={"GLOBL"}),
	#0x802B1B2C: main.sym("object_a_802B1B2C", flag={"GLOBL"}),
	#0x802B1BB0: main.sym("CtrlMarioCopyParentPos", flag={"GLOBL"}),
	#0x802B1C54: main.sym("object_a_802B1C54", flag={"GLOBL"}),
	0x802B14DC: main.sym("object_a_802B1D7C", flag={"GLOBL"}),
	0x802B15CC: main.sym("object_a_802B1E6C", flag={"GLOBL"}),
	0x802B1754: main.sym("object_a_802B1FF4", flag={"GLOBL"}),
	0x802B1800: main.sym("object_a_802B20A0", flag={"GLOBL"}),
	0x802B18B4: main.sym("object_a_802B2154"),
	#0x802B2278: main.sym("object_a_802B2278", flag={"GLOBL"}),
	#0x802B2340: main.sym("object_a_802B2340", flag={"GLOBL"}),
	#0x802B23E0: main.sym("object_a_802B23E0", flag={"GLOBL"}),
	#0x802B2494: main.sym("object_a_802B2494", flag={"GLOBL"}),
	#0x802B25AC: main.sym("object_a_802B25AC", flag={"GLOBL"}),
	0x802B1E04: main.sym("object_a_802B26A4", flag={"GLOBL"}),
	0x802B1F38: main.sym("object_a_802B27D8", flag={"GLOBL"}),
	0x802B1F84: main.sym("object_a_802B2824"),
	#0x802B288C: main.sym("object_a_802B288C", flag={"GLOBL"}),
	#0x802B29B8: main.sym("object_a_802B29B8", flag={"GLOBL"}),
	0x802B2164: main.sym("L802B2A04", flag={"GLOBL","LOCAL"}),
	0x802B21EC: main.sym("L802B2A8C", flag={"GLOBL","LOCAL"}),
	0x802B2284: main.sym("L802B2B24", flag={"GLOBL","LOCAL"}),
	0x802B22D4: main.sym("L802B2B74", flag={"GLOBL","LOCAL"}),
	0x802B2308: main.sym("L802B2BA8", flag={"GLOBL","LOCAL"}),
	0x802B2328: main.sym("object_a_802B2BC8"),
	#0x802B2D10: main.sym("object_a_802B2D10", flag={"GLOBL"}),
	0x802B250C: main.sym("object_a_802B2DAC", flag={"GLOBL"}),
	0x802B2694: main.sym("object_a_802B2F34", flag={"GLOBL"}),
	0x802B27C4: main.sym("object_a_802B3064", flag={"GLOBL"}),
	#0x802B3108: main.sym("object_a_802B3108", flag={"GLOBL"}),
	0x802B2894: main.sym("object_a_802B3134"),
	0x802B29B0: main.sym("object_a_802B3250"),
	#0x802B329C: main.sym("object_a_802B329C", flag={"GLOBL"}),
	#0x802B3600: main.sym("object_a_802B3600", flag={"GLOBL"}),
	#0x802B37B8: main.sym("object_a_802B37B8", flag={"GLOBL"}),
	#0x802B3810: main.sym("object_a_802B3810", flag={"GLOBL"}),
	0x802B2F90: main.sym("object_a_802B3830", flag={"GLOBL"}),
	0x802B3018: main.sym("object_a_802B38B8", flag={"GLOBL"}),
	0x802B30AC: main.sym("object_a_802B394C", flag={"GLOBL"}),
	0x802B3268: main.sym("object_a_802B3B08", flag={"GLOBL"}),
	0x802B3284: main.sym("object_a_802B3B24", flag={"GLOBL"}),
	#0x802B3BE0: main.sym("object_a_802B3BE0", flag={"GLOBL"}),
	0x802B338C: main.sym("object_a_802B3C2C", flag={"GLOBL"}),
	0x802B343C: main.sym("object_a_802B3CDC", flag={"GLOBL"}),
	0x802B3470: main.sym("object_a_802B3D10", flag={"GLOBL"}),
	#0x802B3D74: main.sym("object_a_802B3D74", flag={"GLOBL"}),
	#0x802B3DF4: main.sym("object_a_802B3DF4", flag={"GLOBL"}),
	#0x802B4080: main.sym("object_a_802B4080", flag={"GLOBL"}),
	0x802B38B4: main.sym("object_a_802B4184"),
	0x802B392C: main.sym("object_a_802B41FC"),
	0x802B39B8: main.sym("object_a_802B4288"),
	0x802B3A30: main.sym("object_a_802B4300"),
	0x802B3A98: main.sym("object_a_802B4368"),
	0x802B3B0C: main.sym("object_a_802B43DC"),
	0x802B3BA8: main.sym("object_a_802B4478", flag={"GLOBL"}),
	0x802B3BEC: main.sym("object_a_802B44BC", flag={"GLOBL"}),
	#0x802B459C: main.sym("object_a_802B459C"),
	0x802B3D24: main.sym("object_a_802B45F4"),
	0x802B3E44: main.sym("object_a_802B473C"),
	0x802B3FDC: main.sym("object_a_802B48D4"),
	0x802B4124: main.sym("object_a_802B4A1C"),
	0x802B4144: main.sym("object_a_802B4A3C"),
	0x802B4A44: main.sym("object_a_802B53F4"),
	0x802B41FC: main.sym("object_a_802B4BAC", flag={"GLOBL"}),
	0x802B4238: main.sym("object_a_802B4BE8", flag={"GLOBL"}),
	0x802B42F4: main.sym("object_a_802B4CA4", flag={"GLOBL"}),
	0x802B4364: main.sym("object_a_802B4D14", flag={"GLOBL"}),
	0x802B4550: main.sym("object_a_802B4F00", flag={"GLOBL"}),
	0x802B4754: main.sym("object_a_802B5104", flag={"GLOBL"}),
	0x802B4868: main.sym("object_a_802B5218", flag={"GLOBL"}),
	#0x802B53F4: main.sym("object_a_802B53F4"),
	0x802B4A94: main.sym("object_a_802B5444"),
	0x802B4BA4: main.sym("object_a_802B5554"),
	0x802B4C1C: main.sym("object_a_802B55CC", flag={"GLOBL"}),
	0x802B4DB4: main.sym("object_a_802B5798", flag={"GLOBL"}),
	0x802B4ED8: main.sym("object_a_802B58BC", flag={"GLOBL"}),
	0x802B4FE8: main.sym("object_a_802B59CC", flag={"GLOBL"}),
	0x802B5108: main.sym("object_a_802B5AEC"),
	0x802B521C: main.sym("object_a_802B5C00", flag={"GLOBL"}),
	0x802B525C: main.sym("object_a_802B5C40", flag={"GLOBL"}),
	0x802B5588: main.sym("object_a_802B5F6C"),
	0x802B5608: main.sym("object_a_802B5FEC", flag={"GLOBL"}),
	0x802B5738: main.sym("object_a_802B611C"),
	0x802B57AC: main.sym("object_a_802B6190", flag={"GLOBL"}),
	0x802B5C10: main.sym("object_a_802B6568", flag={"GLOBL"}),
	0x802B5C78: main.sym("object_a_802B65D0"),
	0x802B5D18: main.sym("object_a_802B6670"),
	0x802B5DD8: main.sym("object_a_802B6730"),
	0x802B5E7C: main.sym("object_a_802B67D4"),
	0x802B5F20: main.sym("object_a_802B6878"),
	0x802B60B8: main.sym("object_a_802B6A10"),
	0x802B6120: main.sym("object_a_802B6A78"),
	0x802B6254: main.sym("object_a_802B6BAC"),
	0x802B6398: main.sym("object_a_802B6CF0", flag={"GLOBL"}),
	0x802B63D0: main.sym("L802B6D28", flag={"GLOBL","LOCAL"}),
	0x802B63E0: main.sym("L802B6D38", flag={"GLOBL","LOCAL"}),
	0x802B63F0: main.sym("L802B6D48", flag={"GLOBL","LOCAL"}),
	0x802B6468: main.sym("L802B6DC0", flag={"GLOBL","LOCAL"}),
	0x802B6494: main.sym("L802B6DEC", flag={"GLOBL","LOCAL"}),
	0x802B649C: main.sym("L802B6DF4", flag={"GLOBL","LOCAL"}),
	0x802B64C8: main.sym("L802B6E20", flag={"GLOBL","LOCAL"}),
	0x802B64D0: main.sym("L802B6E28", flag={"GLOBL","LOCAL"}),
	0x802B64E8: main.sym("object_a_802B6E40"),
	0x802B6588: main.sym("object_a_802B6EE0", flag={"GLOBL"}),
	0x802B67C4: main.sym("object_a_802B711C"),
	0x802B688C: main.sym("object_a_802B71E4"),
	0x802B697C: main.sym("object_a_802B72D4"),
	0x802B6AC0: main.sym("object_a_802B7418"),
	#0x802B75A4: main.sym("object_a_802B75A4", flag={"GLOBL"}),
	#0x802B7878: main.sym("object_a_802B7878", flag={"GLOBL"}),
	#0x802B798C: main.sym("Ctrl_object_a_802B798C", flag={"GLOBL"}),
	0x802B70C8: main.sym("object_a_802B7A20"),
	0x802B7120: main.sym("L802B7A78", flag={"GLOBL","LOCAL"}),
	0x802B7190: main.sym("L802B7AE8", flag={"GLOBL","LOCAL"}),
	0x802B71B8: main.sym("L802B7B10", flag={"GLOBL","LOCAL"}),
	0x802B71E0: main.sym("L802B7B38", flag={"GLOBL","LOCAL"}),
	0x802B7204: main.sym("L802B7B5C", flag={"GLOBL","LOCAL"}),
	0x802B7244: main.sym("L802B7B9C", flag={"GLOBL","LOCAL"}),
	0x802B7268: main.sym("L802B7BC0", flag={"GLOBL","LOCAL"}),
	0x802B72A8: main.sym("L802B7C00", flag={"GLOBL","LOCAL"}),
	0x802B72CC: main.sym("L802B7C24", flag={"GLOBL","LOCAL"}),
	#0x802B7C64: main.sym("Ctrl_object_a_802B7C64", flag={"GLOBL"}),
	#0x802B7D44: main.sym("Ctrl_object_a_802B7D44", flag={"GLOBL"}),
	0x802B7510: main.sym("object_a_802B7E68", flag={"GLOBL"}),
	0x802B7598: main.sym("object_a_802B7EF0", flag={"GLOBL"}),
	0x802B76CC: main.sym("object_a_802B8024", flag={"GLOBL"}),
	#0x802B8384: main.sym("object_a_802B8384", flag={"GLOBL"}),
	0x802B7A58: main.sym("object_a_802B83B0"),
	0x802B7ADC: main.sym("object_a_802B8434"),
	#0x802B84AC: main.sym("object_a_802B84AC", flag={"GLOBL"}),
	#0x802B85B0: main.sym("object_a_802B85B0", flag={"GLOBL"}),
	0x802B7CFC: main.sym("object_a_802B8654"),
	#0x802B8734: main.sym("object_a_802B8734", flag={"GLOBL"}),
	#0x802B8960: main.sym("object_a_802B8960", flag={"GLOBL"}),
	#0x802B89EC: main.sym("object_a_802B89EC", flag={"GLOBL"}),
	#0x802B8B1C: main.sym("object_a_802B8B1C", flag={"GLOBL"}),
	#0x802B8C38: main.sym("object_a_802B8C38", flag={"GLOBL"}),
	#0x802B8D68: main.sym("object_a_802B8D68", flag={"GLOBL"}),
	#0x802B8E7C: main.sym("object_a_802B8E7C", flag={"GLOBL"}),
	#0x802B9034: main.sym("object_a_802B9034", flag={"GLOBL"}),
	#0x802B90EC: main.sym("object_a_802B90EC", flag={"GLOBL"}),
	#0x802B921C: main.sym("object_a_802B921C", flag={"GLOBL"}),
	#0x802B935C: main.sym("object_a_802B935C", flag={"GLOBL"}),
	#0x802B9790: main.sym("object_a_802B9790", flag={"GLOBL"}),
	0x802B8F7C: main.sym("object_a_802B98D4"),
	#0x802B98FC: main.sym("object_a_802B98FC", flag={"GLOBL"}),
	0x802B9120: main.sym("object_a_802B9A78"),
	0x802B91A0: main.sym("object_a_802B9AF8"),
	#0x802B9BB4: main.sym("object_a_802B9BB4", flag={"GLOBL"}),
	#0x802B9BD8: main.sym("object_a_802B9BD8", flag={"GLOBL"}),
	0x802B9308: main.sym("L802B9C60", flag={"GLOBL","LOCAL"}),
	0x802B9348: main.sym("L802B9CA0", flag={"GLOBL","LOCAL"}),
	0x802B9368: main.sym("L802B9CC0", flag={"GLOBL","LOCAL"}),
	0x802B937C: main.sym("L802B9CD4", flag={"GLOBL","LOCAL"}),
	0x802B939C: main.sym("L802B9CF4", flag={"GLOBL","LOCAL"}),
	#0x802B9E94: main.sym("object_a_802B9E94", flag={"GLOBL"}),
	0x802B95A4: main.sym("object_a_802B9EFC"),
	0x802B95DC: main.sym("L802B9F34", flag={"GLOBL","LOCAL"}),
	0x802B9610: main.sym("L802B9F68", flag={"GLOBL","LOCAL"}),
	0x802B9664: main.sym("L802B9FBC", flag={"GLOBL","LOCAL"}),
	0x802B96B0: main.sym("L802BA008", flag={"GLOBL","LOCAL"}),
	0x802B970C: main.sym("L802BA064", flag={"GLOBL","LOCAL"}),
	0x802B97C4: main.sym("L802BA11C", flag={"GLOBL","LOCAL"}),
	0x802B97E4: main.sym("object_a_802BA13C"),
	#0x802BA19C: main.sym("object_a_802BA19C", flag={"GLOBL"}),
	#0x802BA1E0: main.sym("object_a_802BA1E0", flag={"GLOBL"}),
	#0x802BA25C: main.sym("object_a_802BA25C", flag={"GLOBL"}),
	#0x802BA2B0: main.sym("Ctrl_object_a_802BA2B0", flag={"GLOBL"}),
	#0x802BA2F8: main.sym("object_a_802BA2F8", flag={"GLOBL"}),
	#0x802BA458: main.sym("object_a_802BA458", flag={"GLOBL"}),
	#0x802BA5BC: main.sym("object_a_802BA5BC", flag={"GLOBL"}),
	#0x802BA608: main.sym("object_a_802BA608", flag={"GLOBL"}),
	0x802B9E88: main.sym("object_a_802BA7E0"),
	0x802B9F10: main.sym("object_a_802BA868"),
	#0x802BA8C4: main.sym("object_a_802BA8C4"),
	0x802BA000: main.sym("object_a_802BA958"),
	0x802BA224: main.sym("object_a_802BAB7C", flag={"GLOBL"}),
	0x802BA4E8: main.sym("object_a_802BAE40", flag={"GLOBL"}),
	0x802BA56C: main.sym("object_a_802BAEC4", flag={"GLOBL"}),
	0x802BA5B8: main.sym("object_a_802BAF10", flag={"GLOBL"}),
	0x802BA60C: main.sym("object_a_802BAF64", flag={"GLOBL"}),
	0x802BA724: main.sym("object_a_802BB07C", flag={"GLOBL"}),
	0x802BA930: main.sym("object_a_802BB288", flag={"GLOBL"}),
	0x802BAA60: main.sym("object_a_802BB3B8", flag={"GLOBL"}),
	0x802BAB10: main.sym("L802BB468", flag={"GLOBL","LOCAL"}),
	0x802BABB0: main.sym("L802BB508", flag={"GLOBL","LOCAL"}),
	0x802BAC0C: main.sym("L802BB564", flag={"GLOBL","LOCAL"}),
	0x802BAC4C: main.sym("L802BB5A4", flag={"GLOBL","LOCAL"}),
	0x802BAC9C: main.sym("L802BB5F4", flag={"GLOBL","LOCAL"}),
	0x802BACE0: main.sym("L802BB638", flag={"GLOBL","LOCAL"}),
	0x802BAD88: main.sym("L802BB6E0", flag={"GLOBL","LOCAL"}),
	0x802BADF0: main.sym("L802BB748", flag={"GLOBL","LOCAL"}),
	0x802BAE40: main.sym("object_a_802BB798"),
	#0x802BB838: main.sym("object_a_802BB838"),
	0x802BAF30: main.sym("object_a_802BB888"),
	0x802BB0E4: main.sym("object_a_802BBA3C"),
	0x802BB11C: main.sym("L802BBA74", flag={"GLOBL","LOCAL"}),
	0x802BB15C: main.sym("L802BBAB4", flag={"GLOBL","LOCAL"}),
	0x802BB1A4: main.sym("L802BBAFC", flag={"GLOBL","LOCAL"}),
	0x802BB1AC: main.sym("L802BBB04", flag={"GLOBL","LOCAL"}),
	0x802BB208: main.sym("L802BBB60", flag={"GLOBL","LOCAL"}),
	0x802BB228: main.sym("L802BBB80", flag={"GLOBL","LOCAL"}),
	#0x802BBB98: main.sym("object_a_802BBB98", flag={"GLOBL"}),
	#0x802BBC0C: main.sym("object_a_802BBC0C", flag={"GLOBL"}),
	0x802BB414: main.sym("object_a_802BBD6C"),
	0x802BB680: main.sym("object_a_802BBFD8"),
	#0x802BC0F0: main.sym("object_a_802BC0F0", flag={"GLOBL"}),
	#0x802BC22C: main.sym("object_a_802BC22C", flag={"GLOBL"}),
	#0x802BC294: main.sym("object_a_802BC294", flag={"GLOBL"}),
	0x802BB9F0: main.sym("object_a_802BC348"),
	0x802BBB9C: main.sym("object_a_802BC4F4", flag={"GLOBL"}),
	0x802BBBE0: main.sym("object_a_802BC538", flag={"GLOBL"}),
	0x802BBC38: main.sym("object_a_802BC590", flag={"GLOBL"}),
	0x802BBCA4: main.sym("object_a_802BC5FC", flag={"GLOBL"}),
	#0x802BC618: main.sym("object_a_802BC618", flag={"GLOBL"}),
	#0x802BC660: main.sym("object_a_802BC660", flag={"GLOBL"}),
	#0x802BC728: main.sym("object_a_802BC728", flag={"GLOBL"}),
	#0x802BC898: main.sym("object_a_802BC898", flag={"GLOBL"}),
	0x802BBFDC: main.sym("object_a_802BC934"),
	#0x802BCA74: main.sym("object_a_802BCA74", flag={"GLOBL"}),
	0x802BC184: main.sym("L802BCADC", flag={"GLOBL","LOCAL"}),
	0x802BC1CC: main.sym("L802BCB24", flag={"GLOBL","LOCAL"}),
	0x802BC24C: main.sym("L802BCBA4", flag={"GLOBL","LOCAL"}),
	0x802BC2C4: main.sym("L802BCC1C", flag={"GLOBL","LOCAL"}),
	0x802BC338: main.sym("L802BCC90", flag={"GLOBL","LOCAL"}),
	0x802BC390: main.sym("object_a_802BCCE8"),
	#0x802BCDA8: main.sym("object_a_802BCDA8", flag={"GLOBL"}),
	#0x802BCE58: main.sym("object_a_802BCE58", flag={"GLOBL"}),
	0x802BC544: main.sym("object_a_802BCE9C"),
	#0x802BCF40: main.sym("object_a_802BCF40", flag={"GLOBL"}),
	0x802BC66C: main.sym("object_a_802BCFC4"),
	#0x802BD058: main.sym("object_a_802BD058", flag={"GLOBL"}),
	0x802BCA8C: main.sym("object_a_802BD3E4"),
	#0x802BD488: main.sym("object_a_802BD488", flag={"GLOBL"}),
	0x802BCC84: main.sym("object_a_802BD5DC"),
	0x802BCCD4: main.sym("object_a_802BD62C"),
	#0x802BD680: main.sym("object_a_802BD680", flag={"GLOBL"}),
	0x802BCF78: main.sym("object_a_802BD8D0"),
	0x802BCFC4: main.sym("object_a_802BD91C"),
	0x802BD1AC: main.sym("object_a_802BDB04", flag={"GLOBL"}),
	0x802BD1E4: main.sym("object_a_802BDB3C", flag={"GLOBL"}),
	0x802BD21C: main.sym("object_a_802BDB74", flag={"GLOBL"}),
	0x802BD254: main.sym("object_a_802BDBAC", flag={"GLOBL"}),
	0x802BD28C: main.sym("object_a_802BDBE4", flag={"GLOBL"}),
	0x802BD324: main.sym("object_a_802BDC7C", flag={"GLOBL"}),
	0x802BD370: main.sym("object_a_802BDCC8", flag={"GLOBL"}),
	0x802BD3BC: main.sym("object_a_802BDD14", flag={"GLOBL"}),
	#0x802BDD68: main.sym("object_a_802BDD68", flag={"GLOBL"}),
	0x802BD444: main.sym("object_a_802BDD9C", flag={"GLOBL"}),
	0x802BD4A8: main.sym("object_a_802BDE10"),
	0x802BD584: main.sym("object_a_802BDEEC", flag={"GLOBL"}),
	0x802BD6C0: main.sym("object_a_802BE034", flag={"GLOBL"}),
	#0x802BE0B8: main.sym("object_a_802BE0B8"),
	0x802BD734: main.sym("object_a_802BE0EC", flag={"GLOBL"}),
	0x802BD790: main.sym("object_a_802BE150", flag={"GLOBL"}),
	0x802BD86C: main.sym("object_a_802BE234", flag={"GLOBL"}),
	0x802BD8B0: main.sym("object_a_802BE278", flag={"GLOBL"}),
	0x802BD988: main.sym("object_a_802BE350", flag={"GLOBL"}),
	0x802BDAD4: main.sym("object_a_802BE49C"),
	0x802BDB44: main.sym("object_a_802BE50C", flag={"GLOBL"}),
	#0x802BE5A0: main.sym("object_a_802BE5A0", flag={"GLOBL"}),
	0x802BDC60: main.sym("object_a_802BE628"),
	0x802BDD0C: main.sym("object_a_802BE6D4"),
	#0x802BE79C: main.sym("object_a_802BE79C", flag={"GLOBL"}),
	0x802BDEE0: main.sym("object_a_802BE8A8", flag={"GLOBL"}),
	0x802BDEF0: main.sym("object_a_802BE8B8", flag={"GLOBL"}),
	0x802BDF2C: main.sym("object_a_802BE8F4"),
	0x802BE014: main.sym("object_a_802BE9DC"),
	0x802BE14C: main.sym("object_a_802BEB14", flag={"GLOBL"}),
	0x802BE18C: main.sym("object_a_802BEB54", flag={"GLOBL"}),
	0x802BE1C4: main.sym("object_a_802BEB8C", flag={"GLOBL"}),
	0x802BE1FC: main.sym("object_a_802BEBC4", flag={"GLOBL"}),
	0x802BE234: main.sym("object_a_802BEBFC", flag={"GLOBL"}),
	#0x802BEC34: main.sym("object_a_802BEC34", flag={"GLOBL"}),
	0x802BE2E8: main.sym("object_a_802BECB0"),
	0x802BE3B4: main.sym("object_a_802BED7C", flag={"GLOBL"}),
	0x802BE424: main.sym("object_a_802BEDEC", flag={"GLOBL"}),
	0x802BE5C4: main.sym("object_a_802BEF8C", flag={"GLOBL"}),
	0x802BE80C: main.sym("object_a_802BF1D8", flag={"GLOBL"}),
	#0x802BF3C0: main.sym("object_a_802BF3C0", flag={"GLOBL"}),
	0x802BEA58: main.sym("object_a_802BF424"),
	0x802BEAA8: main.sym("object_a_802BF474", flag={"GLOBL"}),
	0x802BEBB0: main.sym("object_a_802BF57C", flag={"GLOBL"}),
	0x802BEC7C: main.sym("object_a_802BF648", flag={"GLOBL"}),
	0x802BED18: main.sym("object_a_802BF6E4", flag={"GLOBL"}),
	0x802BED94: main.sym("object_a_802BF760", flag={"GLOBL"}),
	0x802BEF40: main.sym("object_a_802BF90C", flag={"GLOBL"}),
	0x802BF048: main.sym("object_a_802BFA14"),
	#0x802BFA88: main.sym("object_a_802BFA88", flag={"GLOBL"}),
	#0x802BFBAC: main.sym("Ctrl_object_a_802BFBAC", flag={"GLOBL"}),
	0x802BF30C: main.sym("object_a_802BFCD8", flag={"GLOBL"}),
	0x802BF4EC: main.sym("object_a_802BFEB8", flag={"GLOBL"}),
	0x802BF554: main.sym("object_a_802BFF20", flag={"GLOBL"}),
	#0x802BFF3C: main.sym("object_a_802BFF3C", flag={"GLOBL"}),
	0x802BF59C: main.sym("object_a_802BFF68"),
	0x802BF6E8: main.sym("object_a_802C00B4", flag={"GLOBL"}),
	0x802BF97C: main.sym("object_a_802C0348", flag={"GLOBL"}),
	0x802BFCDC: main.sym("object_a_802C06A8", flag={"GLOBL"}),
	#0x802C0768: main.sym("object_a_802C0768", flag={"GLOBL"}),
	#0x802C08A8: main.sym("object_a_802C08A8", flag={"GLOBL"}),
	0x802C00E0: main.sym("object_a_802C0AAC", flag={"GLOBL"}),
	0x802C0184: main.sym("object_a_802C0B50", flag={"GLOBL"}),
	0x802C01D8: main.sym("object_a_802C0BA4", flag={"GLOBL"}),
	0x802C01F8: main.sym("object_a_802C0BC4", flag={"GLOBL"}),
	#0x802C0BE0: main.sym("object_a_802C0BE0", flag={"GLOBL"}),
	0x802C0240: main.sym("object_a_802C0C0C"),
	0x802C0308: main.sym("object_a_802C0CD4", flag={"GLOBL"}),
	0x802C0378: main.sym("object_a_802C0D44", flag={"GLOBL"}),
	0x802C05C4: main.sym("object_a_802C0F90", flag={"GLOBL"}),
	#0x802C1204: main.sym("object_a_802C1204", flag={"GLOBL"}),
	#0x802C12C0: main.sym("object_a_802C12C0", flag={"GLOBL"}),
	0x802C093C: main.sym("object_a_802C1308", flag={"GLOBL"}),
	0x802C0A20: main.sym("object_a_802C13EC", flag={"GLOBL"}),
	0x802C0AE4: main.sym("object_a_802C14B0", flag={"GLOBL"}),
	0x802C0BEC: main.sym("object_a_802C15B8", flag={"GLOBL"}),
	0x802C0DF0: main.sym("object_a_802C17BC"),
	0x802C0F04: main.sym("object_a_802C18D0", flag={"GLOBL"}),
	0x802C0FBC: main.sym("object_a_802C1988", flag={"GLOBL"}),
	#0x802C19C0: main.sym("object_a_802C19C0", flag={"GLOBL"}),
	#0x802C19FC: main.sym("object_a_802C19FC", flag={"GLOBL"}),
	#0x802C1A40: main.sym("object_a_802C1A40", flag={"GLOBL"}),
	#0x802C1A80: main.sym("object_a_802C1A80", flag={"GLOBL"}),
	#0x802C1A90: main.sym("object_a_802C1A90", flag={"GLOBL"}),
	#0x802C1C44: main.sym("object_a_802C1C44", flag={"GLOBL"}),
	#0x802C1CD4: main.sym("object_a_802C1CD4", flag={"GLOBL"}),
	#0x802C1E10: main.sym("object_a_802C1E10", flag={"GLOBL"}),
	#0x802C2190: main.sym("object_a_802C2190", flag={"GLOBL"}),
	#0x802C2274: main.sym("object_a_802C2274", flag={"GLOBL"}),
	#0x802C22B8: main.sym("object_a_802C22B8", flag={"GLOBL"}),
	#0x802C242C: main.sym("object_a_802C242C", flag={"GLOBL"}),
	#0x802C263C: main.sym("object_a_802C263C", flag={"GLOBL"}),
	#0x802C26F8: main.sym("object_a_802C26F8", flag={"GLOBL"}),
	#0x802C2930: main.sym("object_a_802C2930", flag={"GLOBL"}),
	#0x802C2A24: main.sym("object_a_802C2A24", flag={"GLOBL"}),
	0x802C231C: main.sym("object_a_802C2CE8"),
	0x802C24F0: main.sym("object_a_802C2EBC", flag={"GLOBL"}),
	0x802C25F0: main.sym("object_a_802C2FBC", flag={"GLOBL"}),
	0x802C27F8: main.sym("object_a_802C31C4", flag={"GLOBL"}),
	#0x802C329C: main.sym("object_a_802C329C", flag={"GLOBL"}),
	#0x802C32E8: main.sym("object_a_802C32E8", flag={"GLOBL"}),
	0x802C2A28: main.sym("object_a_802C33F4"),
	#0x802C3440: main.sym("object_a_802C3440", flag={"GLOBL"}),
	0x802C2A94: main.sym("object_a_802C3460"),
	0x802C2B68: main.sym("object_a_802C3534"),
	#0x802C3684: main.sym("object_a_802C3684", flag={"GLOBL"}),
	0x802C2D7C: main.sym("object_a_802C3748"),
	0x802C2EB8: main.sym("object_a_802C3884"),
	0x802C3008: main.sym("object_a_802C39D4"),
	0x802C313C: main.sym("object_a_802C3B08"),
	0x802C3238: main.sym("object_a_802C3C04"),
	0x802C3304: main.sym("object_a_802C3CD0"),
	0x802C3384: main.sym("object_a_802C3D50"),
	0x802C33D0: main.sym("object_a_802C3D9C"),
	0x802C34B4: main.sym("object_a_802C3E80"),
	0x802C35C0: main.sym("object_a_802C3F8C"),
	0x802C3738: main.sym("object_a_802C4118"),
	0x802C3778: main.sym("object_a_802C4158"),
	0x802C3830: main.sym("object_a_802C4210"),
	0x802C3A14: main.sym("object_a_802C43F4", flag={"GLOBL"}),
	0x802C3B28: main.sym("object_a_802C4508", flag={"GLOBL"}),
	0x802C3BD0: main.sym("object_a_802C45B0", flag={"GLOBL"}),
	0x802C3CF8: main.sym("object_a_802C46D8", flag={"GLOBL"}),
	0x802C3D40: main.sym("object_a_802C4720", flag={"GLOBL"}),
	0x802C3DB0: main.sym("object_a_802C4790", flag={"GLOBL"}),
	#0x802C4824: main.sym("object_a_802C4824", flag={"GLOBL"}),
	0x802C3EE0: main.sym("object_a_802C48C0", flag={"GLOBL"}),
	0x802C4000: main.sym("object_a_802C49F0", flag={"GLOBL"}),
	0x802C4164: main.sym("object_a_802C4B54", flag={"GLOBL"}),
	0x802C41AC: main.sym("object_a_802C4B9C"),
	0x802C41E4: main.sym("object_a_802C4BD4"),
	0x802C4220: main.sym("object_a_802C4C10"),
	0x802C4280: main.sym("object_a_802C4C70", flag={"GLOBL"}),
	0x802C43E4: main.sym("object_a_802C4DD4", flag={"GLOBL"}),
	#0x802C4F30: main.sym("object_a_802C4F30", flag={"GLOBL"}),
	0x802C45B8: main.sym("object_a_802C4FB0", flag={"GLOBL"}),
	0x802C4644: main.sym("object_a_802C503C", flag={"GLOBL"}),
	0x802C46E0: main.sym("object_a_802C50D8", flag={"GLOBL"}),
	0x802C4728: main.sym("object_a_802C5120", flag={"GLOBL"}),
	#0x802C515C: main.sym("object_a_802C515C", flag={"GLOBL"}),
	#0x802C51D4: main.sym("object_a_802C51D4", flag={"GLOBL"}),
	#0x802C5224: main.sym("object_a_802C5224", flag={"GLOBL"}),
	0x802C49E0: main.sym("object_a_802C53CC"),
	#0x802C53EC: main.sym("object_a_802C53EC", flag={"GLOBL"}),
	#0x802C5414: main.sym("object_a_802C5414", flag={"GLOBL"}),
	#0x802C5688: main.sym("object_a_802C5688", flag={"GLOBL"}),
	#0x802C5890: main.sym("object_a_802C5890", flag={"GLOBL"}),
	#0x802C5A38: main.sym("object_a_802C5A38", flag={"GLOBL"}),
	0x802C50F4: main.sym("object_a_802C5B54"),
	#0x802C5CA8: main.sym("object_a_802C5CA8", flag={"GLOBL"}),
	#0x802C5DC0: main.sym("object_a_802C5DC0", flag={"GLOBL"}),
	#0x802C5F48: main.sym("object_a_802C5F48", flag={"GLOBL"}),
	#0x802C5FDC: main.sym("object_a_802C5FDC", flag={"GLOBL"}),
	#0x802C6050: main.sym("object_a_802C6050", flag={"GLOBL"}),
	#0x802C60AC: main.sym("object_a_802C60AC", flag={"GLOBL"}),
	0x802C567C: main.sym("object_a_802C6150"),
	0x802C5700: main.sym("object_a_802C61D4"),
	0x802C57A4: main.sym("object_a_802C6278"),
	0x802C57E8: main.sym("object_a_802C62BC"),
	0x802C5854: main.sym("object_a_802C6328"),
	#0x802C6348: main.sym("object_a_802C6348", flag={"GLOBL"}),
	0x802C58AC: main.sym("L802C6380", flag={"GLOBL","LOCAL"}),
	0x802C58BC: main.sym("L802C6390", flag={"GLOBL","LOCAL"}),
	0x802C58CC: main.sym("L802C63A0", flag={"GLOBL","LOCAL"}),
	0x802C58DC: main.sym("L802C63B0", flag={"GLOBL","LOCAL"}),
	0x802C58EC: main.sym("L802C63C0", flag={"GLOBL","LOCAL"}),
	0x802C5914: main.sym("object_a_802C63E8", flag={"GLOBL"}),
	#0x802C64A4: main.sym("object_a_802C64A4", flag={"GLOBL"}),
	0x802C5A64: main.sym("object_a_802C6538"),
	#0x802C65C0: main.sym("object_a_802C65C0", flag={"GLOBL"}),
	0x802C5B94: main.sym("L802C6668", flag={"GLOBL","LOCAL"}),
	0x802C5C1C: main.sym("L802C66F0", flag={"GLOBL","LOCAL"}),
	0x802C5DB8: main.sym("L802C688C", flag={"GLOBL","LOCAL"}),
	0x802C5E4C: main.sym("L802C6920", flag={"GLOBL","LOCAL"}),
	0x802C5EBC: main.sym("L802C6990", flag={"GLOBL","LOCAL"}),
	0x802C5F48: main.sym("L802C6A1C", flag={"GLOBL","LOCAL"}),
	#0x802C6B6C: main.sym("object_a_802C6B6C", flag={"GLOBL"}),
	0x802C61CC: main.sym("object_a_802C6CA0"),
	0x802C6298: main.sym("object_a_802C6D6C", flag={"GLOBL"}),
	0x802C63F4: main.sym("object_a_802C6EC8", flag={"GLOBL"}),
	0x802C64DC: main.sym("object_a_802C6FB0", flag={"GLOBL"}),
	0x802C6638: main.sym("object_a_802C710C", flag={"GLOBL"}),
	0x802C6780: main.sym("object_a_802C7254", flag={"GLOBL"}),
	0x802C67E0: main.sym("object_a_802C72B4", flag={"GLOBL"}),
	0x802C68AC: main.sym("object_a_802C7380", flag={"GLOBL"}),
	0x802C6954: main.sym("object_a_802C7428"),
	0x802C6B28: main.sym("object_a_802C75FC"),
	0x802C6C00: main.sym("object_a_802C76D4", flag={"GLOBL"}),
	0x802C6D84: main.sym("object_a_802C7858", flag={"GLOBL"}),
	0x802C6EC4: main.sym("object_a_802C7998", flag={"GLOBL"}),
	#0x802C79D8: main.sym("object_a_802C79D8", flag={"GLOBL"}),
	#0x802C7A70: main.sym("object_a_802C7A70", flag={"GLOBL"}),
	#0x802C7B14: main.sym("object_a_802C7B14", flag={"GLOBL"}),
	#0x802C7CAC: main.sym("object_a_802C7CAC", flag={"GLOBL"}),
	#0x802C7D40: main.sym("object_a_802C7D40", flag={"GLOBL"}),
	#0x802C7D90: main.sym("object_a_802C7D90", flag={"GLOBL"}),
	#0x802C7DFC: main.sym("object_a_802C7DFC", flag={"GLOBL"}),
	#0x802C7E5C: main.sym("object_a_802C7E5C", flag={"GLOBL"}),
	#0x802C7F98: main.sym("object_a_802C7F98", flag={"GLOBL"}),
	0x802C76E0: main.sym("object_a_802C81B4", flag={"GLOBL"}),
	#0x802C834C: main.sym("object_a_802C834C", flag={"GLOBL"}),
	0x802C7AD0: main.sym("object_a_802C85A4"),
	#0x802C863C: main.sym("object_a_802C863C", flag={"GLOBL"}),

	# src/ride.c
	0x802C7F20: main.sym("PLRideFind", flag={"GLOBL"}),
	0x802C807C: main.sym("MarioGetPos", flag={"GLOBL"}),
	0x802C80BC: main.sym("MarioSetPos", flag={"GLOBL"}),
	0x802C80F8: main.sym("RideProc", flag={"GLOBL"}),
	0x802C83F0: main.sym("PLRideProc", flag={"GLOBL"}),

	# src/hitcheck.c
	0x802C8460: main.sym("ObjDebugHit"),
	0x802C8504: main.sym("ObjCheckHit"),
	0x802C870C: main.sym("ObjCheckDmg"),
	0x802C88A8: main.sym("HitClear"),
	0x802C8918: main.sym("HitCheckList"),
	0x802C89CC: main.sym("HitCheckPlayer"),
	0x802C8AD4: main.sym("HitCheckEnemyB"),
	0x802C8B50: main.sym("HitCheckAttack"),
	0x802C8C44: main.sym("HitCheck", flag={"GLOBL"}),

	# src/objlist.c
	0x802C8CF0: main.sym("ListInit"),
	0x802C8D60: main.sym("ListAlloc"),
	0x802C8DC4: main.sym("ObjListAlloc"),
	0x802C8E70: main.sym("ListFree"),
	0x802C8EA4: main.sym("ObjListFree"),
	0x802C8ED8: main.sym("ObjFreeListInit", flag={"GLOBL"}),
	0x802C8F5C: main.sym("ObjRootListInit", flag={"GLOBL"}),
	0x802C8FF8: main.sym("objlist_802C9AD8"),
	0x802C9088: main.sym("ObjFree", flag={"GLOBL"}),
	0x802C9120: main.sym("ObjAlloc"),
	0x802C937C: main.sym("ObjInitGround"),
	0x802C9424: main.sym("ObjCreate", flag={"GLOBL"}),
	0x802C9548: main.sym("ObjDestroy", flag={"GLOBL"}),

	# src/objsound.c
	0x802C9560: main.sym("ObjectStepSound", flag={"GLOBL"}),
	0x802C9664: main.sym("ObjectMakeSound", flag={"GLOBL"}),
	0x802C96B0: main.sym("ObjectLevelSound", flag={"GLOBL"}),
	0x802C9700: main.sym("ObjectPlaySound", flag={"GLOBL"}),
	0x802C9750: main.sym("SeCalcVol1"),
	0x802C97F4: main.sym("SeCalcVol2"),

	0x802C9890: main.sym("_802CA370"),
	0x802C98A0: main.sym("_802CA380"),
	0x802C98B0: main.sym("_802CA390"),
	0x802C98C0: main.sym("_802CA3A0"),

	# src/debug.c
	0x802C98D0: main.sym("DbTimeStart", flag={"GLOBL"}),
	0x802C9900: main.sym("DbTimeCount", flag={"GLOBL"}),
	0x802C9938: main.sym("DbPrintInit"),
	0x802C9980: main.sym("DbPrintEntry"),
	0x802C9A3C: main.sym("DbPrintOffset", flag={"GLOBL"}),
	0x802C9A88: main.sym("DbPrintErr", flag={"GLOBL"}),
	0x802C9AD8: main.sym("DbPrint", flag={"GLOBL"}),
	0x802C9B38: main.sym("DbPrintInfo", flag={"GLOBL"}),
	0x802C9BA0: main.sym("DbPrintTitle", flag={"GLOBL"}),
	0x802C9BF0: main.sym("DbPlayerMapInfo"),
	0x802C9E08: main.sym("DbPlayerCheckInfo"),
	0x802C9E38: main.sym("DbResultCheckInfo"),
	0x802C9E6C: main.sym("DbPlayerStageInfo"),
	0x802C9EB0: main.sym("DbPrintEdit"),
	0x802C9F8C: main.sym("DbResultEffectInfo"),
	0x802C9FC8: main.sym("DbResultEnemyInfo"),
	0x802CA004: main.sym("DbProcButton"),
	0x802CA0CC: main.sym("DebugInit", flag={"GLOBL"}),
	0x802CA140: main.sym("DebugClear", flag={"GLOBL"}),
	0x802CA1E8: main.sym("DebugProcSeq"),
	0x802CA2E8: main.sym("DebugProcPage"),
	0x802CA3BC: main.sym("DebugProcEdit"),
	0x802CA5D0: main.sym("DebugExec", flag={"GLOBL"}),
	0x802CA5E0: main.sym("DebugResult", flag={"GLOBL"}),
	0x802CA6E0: main.sym("DebugPlayer", flag={"GLOBL"}),
	0x802CA784: main.sym("DebugProc", flag={"GLOBL"}),
	0x802CA8B4: main.sym("DebugPrintMoveStatus"),
	0x802CAA84: main.sym("DebugSetHit"),

	# src/wipe.c
	0x802CAAE0: main.sym("WpStep"),
	0x802CAB60: main.sym("WpFadeAlpha"),
	0x802CADB4: main.sym("WpFadeVtx"),
	0x802CAF38: main.sym("WpFadeGfx"),
	0x802CB0E4: main.sym("WpFadeIn"),
	0x802CB140: main.sym("WpFadeOut"),
	0x802CB19C: main.sym("WpWindowSize"),
	0x802CB274: main.sym("WpWindowDist"),
	0x802CB384: main.sym("WpWindowAng"),
	0x802CB400: main.sym("WpWindowX"),
	0x802CB484: main.sym("WpWindowY"),
	0x802CB508: main.sym("WpWindowVtxSet"),
	0x802CB6A0: main.sym("WpWindowVtx"),
	0x802CB9F8: main.sym("WpWindow"),
	0x802CC108: main.sym("WipeDraw", flag={"GLOBL"}),
	0x802CC148: main.sym("L802CCC28", flag={"GLOBL","LOCAL"}),
	0x802CC168: main.sym("L802CCC48", flag={"GLOBL","LOCAL"}),
	0x802CC188: main.sym("L802CCC68", flag={"GLOBL","LOCAL"}),
	0x802CC1B0: main.sym("L802CCC90", flag={"GLOBL","LOCAL"}),
	0x802CC1D8: main.sym("L802CCCB8", flag={"GLOBL","LOCAL"}),
	0x802CC200: main.sym("L802CCCE0", flag={"GLOBL","LOCAL"}),
	0x802CC228: main.sym("L802CCD08", flag={"GLOBL","LOCAL"}),
	0x802CC254: main.sym("L802CCD34", flag={"GLOBL","LOCAL"}),
	0x802CC280: main.sym("L802CCD60", flag={"GLOBL","LOCAL"}),
	0x802CC2A8: main.sym("L802CCD88", flag={"GLOBL","LOCAL"}),
	0x802CC2D0: main.sym("L802CCDB0", flag={"GLOBL","LOCAL"}),
	0x802CC2E8: main.sym("CannonOverlayGfx"),
	0x802CC708: main.sym("CtrlCannonOverlay", flag={"GLOBL"}),

	# src/shadow.c
	0x802CC7A0: main.sym("ShRotate"),
	0x802CC848: main.sym("ShAtan2"),
	0x802CC8A8: main.sym("ShScaleSize"),
	0x802CC964: main.sym("ShCutSize"),
	0x802CC9AC: main.sym("ShScaleAlpha"),
	0x802CCB34: main.sym("ShCheckWater"),
	0x802CCBE4: main.sym("ShInit"),
	0x802CCE58: main.sym("ShVtxST9"),
	0x802CCEA8: main.sym("ShVtxST4"),
	0x802CCF0C: main.sym("ShSetVtx"),
	0x802CD040: main.sym("ShProject"),
	0x802CD094: main.sym("ShCalcVtxOff"),
	0x802CD160: main.sym("ShCalcVtxPos"),
	0x802CD3B4: main.sym("ShPlaneCalc"),
	0x802CD45C: main.sym("ShCalcVtx"),
	0x802CD648: main.sym("ShGfx"),
	0x802CD7DC: main.sym("ShFadeIn"),
	0x802CD90C: main.sym("ShFadeOut"),
	0x802CDA44: main.sym("ShFadePlayer"),
	0x802CDBB0: main.sym("ShCheckPlayer"),
	0x802CDCBC: main.sym("ShDrawPlayer"),
	0x802CDEF0: main.sym("ShDrawCircle9"),
	0x802CE008: main.sym("ShDrawCircle4"),
	0x802CE124: main.sym("ShDrawCircle4Flat"),
	0x802CE2E0: main.sym("ShGfxSquare"),
	0x802CE48C: main.sym("ShInitSquare"),
	0x802CE5A0: main.sym("ShDrawSquare"),
	0x802CE710: main.sym("ShDrawRect"),
	0x802CE86C: main.sym("ShadowDraw", flag={"GLOBL"}),
	0x802CE93C: main.sym("L802CF41C", flag={"GLOBL","LOCAL"}),
	0x802CE964: main.sym("L802CF444", flag={"GLOBL","LOCAL"}),
	0x802CE98C: main.sym("L802CF46C", flag={"GLOBL","LOCAL"}),
	0x802CE9B4: main.sym("L802CF494", flag={"GLOBL","LOCAL"}),
	0x802CE9E4: main.sym("L802CF4C4", flag={"GLOBL","LOCAL"}),
	0x802CEA14: main.sym("L802CF4F4", flag={"GLOBL","LOCAL"}),
	0x802CEA70: main.sym("L802CF550", flag={"GLOBL","LOCAL"}),

	# src/background.c
	0x802CEAD0: main.sym("BackPosX"),
	0x802CEBBC: main.sym("BackPosY"),
	0x802CEC9C: main.sym("BackIndex"),
	0x802CED24: main.sym("BackVtx"),
	0x802CEF4C: main.sym("BackTile"),
	0x802CF188: main.sym("BackMtx"),
	0x802CF2A8: main.sym("BackGfx"),
	0x802CF414: main.sym("BackgroundDraw", flag={"GLOBL"}),

	# src/water.c
	0x802CF5A0: main.sym("CtrlPoolLevel", flag={"GLOBL"}),
	0x802CF700: main.sym("CtrlWaterProc", flag={"GLOBL"}),
	0x802CF774: main.sym("WaterSetVtx"),
	0x802CF9A4: main.sym("WaterDrawPlane"),
	0x802CFFA4: main.sym("WaterDraw"),
	0x802D00D0: main.sym("WaterGfx"),
	0x802D01A4: main.sym("WaterGetInfo"),
	0x802D0448: main.sym("WaterGfxStart"),
	0x802D056C: main.sym("CtrlWaterDraw", flag={"GLOBL"}),
	0x802D0850: main.sym("FluidProc"),
	0x802D08EC: main.sym("FluidSetVtx0"),
	0x802D0A94: main.sym("FluidSetVtxN"),
	0x802D0DD4: main.sym("FluidGfx"),
	0x802D1090: main.sym("CtrlFluid", flag={"GLOBL"}),
	0x802D11FC: main.sym("CtrlFluidL", flag={"GLOBL"}),
	0x802D1368: main.sym("CtrlFluidDrawL", flag={"GLOBL"}),
	0x802D14C8: main.sym("CtrlFluidDrawS", flag={"GLOBL"}),
	0x802D1628: main.sym("CtrlFluidProc", flag={"GLOBL"}),

	# src/objshape.c
	0x802D1730: main.sym("VtxSet", flag={"GLOBL"}),
	0x802D17E4: main.sym("RoundFtoS", flag={"GLOBL"}),
	0x802D1880: main.sym("Ctrl_objshape_802D2360", flag={"GLOBL"}),
	0x802D1990: main.sym("Ctrl_objshape_802D2470", flag={"GLOBL"}),
	0x802D1A40: main.sym("Ctrl_objshape_802D2520", flag={"GLOBL"}),
	0x802D1DEC: main.sym("EndingDraw", flag={"GLOBL"}),

	# src/wave.c
	0x802D1EE0: main.sym("WaveStopAll"),
	0x802D1F94: main.sym("WaveYPosY"),
	0x802D2028: main.sym("WaveYPosZ"),
	0x802D20A4: main.sym("WaveGetCenterY"),
	0x802D2160: main.sym("WaveXStep"),
	0x802D22A0: main.sym("WaveXPosX"),
	0x802D231C: main.sym("WaveGetCenterX"),
	0x802D23D8: main.sym("WaveStart"),
	0x802D251C: main.sym("WaveProcV10Still"),
	0x802D26BC: main.sym("WaveProcV10Touch"),
	0x802D279C: main.sym("WaveProcV20Still"),
	0x802D293C: main.sym("WaveProcV20Touch"),
	0x802D2A1C: main.sym("WaveProcH10Still"),
	0x802D2BCC: main.sym("WaveProcH10Touch"),
	0x802D2CBC: main.sym("WaveProcH20Still"),
	0x802D2E5C: main.sym("WaveProcH20Touch"),
	0x802D2F4C: main.sym("WaveProcFlag"),
	0x802D310C: main.sym("WaveProcMove"),
	0x802D320C: main.sym("WaveCalcZ"),
	0x802D338C: main.sym("WaveGetZ"),
	0x802D3404: main.sym("WaveMakeVtx"),
	0x802D356C: main.sym("WaveMakeTri"),
	0x802D3918: main.sym("WaveScaleNormal"),
	0x802D39DC: main.sym("WaveCalcNormal"),
	0x802D3CF0: main.sym("WaveDrawMesh"),
	0x802D43FC: main.sym("WaveTransform"),
	0x802D45FC: main.sym("WaveGfxShade"),
	0x802D4874: main.sym("WaveGfxEnvMap"),
	0x802D4A8C: main.sym("WaveGfxMove"),
	0x802D4BAC: main.sym("WaveGfxStat"),
	0x802D4C98: main.sym("WaveExit"),
	0x802D4CC8: main.sym("WaveMoveDemo"),
	0x802D4E04: main.sym("WaveSetLayer"),
	0x802D4E5C: main.sym("WaveGfx"),
	0x802D4EC8: main.sym("WaveProcV"),
	0x802D4FC0: main.sym("WaveProcH"),
	0x802D50B8: main.sym("CtrlWaveDraw", flag={"GLOBL"}),
	0x802D522C: main.sym("CtrlWaveProc", flag={"GLOBL"}),

	# src/dprint.c
	0x802D5320: main.sym("Powi"),
	0x802D5374: main.sym("dprintFormat"),
	0x802D5664: main.sym("dprintGetFmt"),
	0x802D57F8: main.sym("dprintf", flag={"GLOBL"}),
	0x802D5A74: main.sym("dprint", flag={"GLOBL"}),
	0x802D5BE0: main.sym("dprintc", flag={"GLOBL"}),
	0x802D5D78: main.sym("dprintCvt"),
	0x802D5F18: main.sym("dprintDrawTxt"),
	0x802D5FEC: main.sym("dprintClamp"),
	0x802D605C: main.sym("dprintDrawChar"),
	0x802D61A8: main.sym("dprintDraw", flag={"GLOBL"}),

	# src/message.c
	0x802D6440: main.sym("GfxLoadIdent"),
	0x802D6590: main.sym("GfxTranslate", flag={"GLOBL"}),
	0x802D6694: main.sym("GfxRotate", flag={"GLOBL"}),
	0x802D67A0: main.sym("GfxScale", flag={"GLOBL"}),
	0x802D68A4: main.sym("GfxScreenProj", flag={"GLOBL"}),
	0x802D69A0: main.sym("UnpackI1"),
	0x802D6AFC: main.sym("PrintLgChar"),
	0x802D6BFC: main.sym("PrintLg", flag={"GLOBL"}),
	0x802D6ED0: main.sym("Print16", flag={"GLOBL"}),
	0x802D719C: main.sym("PrintSm", flag={"GLOBL"}),
	0x802D75CC: main.sym("Print8", flag={"GLOBL"}),
	0x802D7924: main.sym("CursorProc", flag={"GLOBL"}),
	0x802D7B3C: main.sym("StrCenterX", flag={"GLOBL"}),
	0x802D7CC0: main.sym("PrintCoin", flag={"GLOBL"}),
	0x802D7D88: main.sym("PrintStar", flag={"GLOBL"}),
	0x802D7E3C: main.sym("itostr", flag={"GLOBL"}),
	0x802D7F74: main.sym("MsgGet", flag={"GLOBL"}),
	0x802D7F90: main.sym("MsgOpen", flag={"GLOBL"}),
	0x802D7FCC: main.sym("MsgOpenInt", flag={"GLOBL"}),
	0x802D8010: main.sym("MsgOpenSignpost", flag={"GLOBL"}),
	0x802D8050: main.sym("MsgOpenPrompt", flag={"GLOBL"}),
	0x802D8098: main.sym("MsgClose", flag={"GLOBL"}),
	0x802D8134: main.sym("MsgDrawBack"),
	0x802D8450: main.sym("MsgSetColor"),
	0x802D8690: main.sym("MsgNewline"),
	0x802D875C: main.sym_fnc("MsgKuten", arg=(
		"char *space",
		"short *count",
	)), # JAPANESE
	0x802D8830: main.sym("MsgFmtInt"),
	0x802D8954: main.sym("MsgClamp"),
	0x802D8980: main.sym("MsgDraw"),
	0x802D8B38: main.sym("L802D99D4", flag={"GLOBL","LOCAL"}),
	0x802D8B74: main.sym("L802D9A10", flag={"GLOBL","LOCAL"}),
	0x802D8BA4: main.sym("L802D9A40", flag={"GLOBL","LOCAL"}),
	0x802D8BB4: main.sym("L802D9A50", flag={"GLOBL","LOCAL"}),
	0x802D8C04: main.sym("L802D9B08", flag={"GLOBL","LOCAL"}),
	0x802D8C18: main.sym("L802D9B1C", flag={"GLOBL","LOCAL"}),
	0x802D8ED4: main.sym("MsgDrawCursor"),
	0x802D9030: main.sym("MsgDrawNextPage"),
	0x802D91C0: main.sym("MsgProcEndSound"),
	0x802D93E0: main.sym("MsgProc"),
	0x802D9A14: main.sym("MenuOpen", flag={"GLOBL"}),
	0x802D9A48: main.sym("StaffClear", flag={"GLOBL"}),
	0x802D9A60: main.sym("StaffDrawStart", flag={"GLOBL"}),
	0x802D9AE8: main.sym("StaffDrawEnd", flag={"GLOBL"}),
	0x802D9B68: main.sym("StaffCvt"),
	0x802D9C38: main.sym("StaffPrint", flag={"GLOBL"}),
	0x802D9CE8: main.sym("CaptionOpen", flag={"GLOBL"}),
	0x802D9D5C: main.sym("CaptionDraw", flag={"GLOBL"}),
	0x802D9F58: main.sym("OpeningDraw"),
	0x802DA218: main.sym("DrawCannonReticle", flag={"GLOBL"}),
	0x802DA4DC: main.sym("PauseMenu_Init", flag={"GLOBL"}),
	0x802DA4F4: main.sym("PauseMenu_InitCourse"),
	0x802DA544: main.sym("MenuDrawBack"),
	0x802DA624: main.sym("PauseMenu_PutRedCoin"),
	0x802DA874: main.sym("PauseMenu_DrawRedCoin"),
	0x802DA8EC: main.sym("PauseMenu_DrawCourse"),
	0x802DAC7C: main.sym("PauseMenu_ProcCamera"),
	0x802DAF9C: main.sym("PauseMenu_ProcCourse"),
	0x802DB284: main.sym("PauseMenu_DrawScoreBox"),
	0x802DB540: main.sym("PauseMenu_InitSelect"),
	0x802DB5A0: main.sym("PauseMenu_DrawSelect"),
	0x802DB698: main.sym("PauseMenu_DrawStar"),
	0x802DB840: main.sym("PauseMenu_ProcScore"),
	0x802DBBB0: main.sym("PauseMenu_Proc"),
	0x802DBE2C: main.sym("SaveMenu_DrawBanner"),
	0x802DC050: main.sym("SaveMenu_ProcDemo"),
	0x802DC2B4: main.sym("SaveMenu_ProcStar"),
	0x802DC330: main.sym("SaveMenu_Draw"),
	0x802DC938: main.sym("SaveMenu_ProcSave"),
	0x802DCBD4: main.sym("SaveMenu_Proc"),
	0x802DCD98: main.sym("MessageProc", flag={"GLOBL"}),

	# src/weather.c
	0x802DCEE0: main.sym("SnowInit"),
	0x802DD028: main.sym("SnowProc"),
	0x802DD1AC: main.sym("WeatherFree"),
	0x802DD204: main.sym("WeatherGetCoord", flag={"GLOBL"}),
	0x802DD32C: main.sym("WeatherSetCoord"),
	0x802DD450: main.sym("SnowIsVisible"),
	0x802DD548: main.sym("SnowMakeSnow"),
	0x802DD978: main.sym("SnowMakeBlizzard"),
	0x802DDDC4: main.sym("BubbleIsVisible"),
	0x802DDE28: main.sym("SnowMakeBubble"),
	0x802DE01C: main.sym("WeatherXfm", flag={"GLOBL"}),
	0x802DE424: main.sym("SnowVtx"),
	0x802DE838: main.sym("SnowGfx"),
	0x802DECB8: main.sym("WeatherDraw", flag={"GLOBL"}),

	# src/lava.c
	0x802DEE40: main.sym("LavaIsVisible"),
	0x802DEEF0: main.sym("FlowerRand"),
	0x802DEF70: main.sym("LavaMakeFlower"),
	0x802DF210: main.sym("LavaNew"),
	0x802DF57C: main.sym("LavaMakeLava"),
	0x802DF74C: main.sym("WhirpoolMove"),
	0x802DF998: main.sym("WhirpoolIsVisible"),
	0x802DFA24: main.sym("LavaMakeWhirlpool"),
	0x802DFF14: main.sym("JetIsVisible"),
	0x802DFFA8: main.sym("LavaMakeJet"),
	0x802E0328: main.sym("LavaInit"),
	0x802E035C: main.sym("L802E126C", flag={"GLOBL","LOCAL"}),
	0x802E0364: main.sym("L802E1274", flag={"GLOBL","LOCAL"}),
	0x802E0384: main.sym("L802E1294", flag={"GLOBL","LOCAL"}),
	0x802E03A4: main.sym("L802E12B4", flag={"GLOBL","LOCAL"}),
	0x802E03B8: main.sym("L802E12C8", flag={"GLOBL","LOCAL"}),
	0x802E03CC: main.sym("L802E12DC", flag={"GLOBL","LOCAL"}),
	0x802E0504: main.sym("LavaMake"),
	0x802E0708: main.sym("LavaVtx"),
	0x802E0B10: main.sym("LavaTxt"),
	0x802E0CA8: main.sym("LavaGfx"),
	0x802E0FC8: main.sym("LavaProc"),
	0x802E1038: main.sym("LavaDraw", flag={"GLOBL"}),

	# src/tag.c
	0x802E1190: main.sym("TagAng"),
	0x802E1224: main.sym("TagEnterCode"),
	0x802E12CC: main.sym("TagEnterArg"),
	0x802E1374: main.sym("TagEnterXYZ"),
	0x802E142C: main.sym("TagEnterOLD"),
	0x802E1504: main.sym("TagObjLoad", flag={"GLOBL"}),
	0x802E1780: main.sym("TagLoad", flag={"GLOBL"}),
	0x802E1848: main.sym("L802E2758", flag={"GLOBL","LOCAL"}),
	0x802E187C: main.sym("L802E278C", flag={"GLOBL","LOCAL"}),
	0x802E18B0: main.sym("L802E27C0", flag={"GLOBL","LOCAL"}),
	0x802E18E4: main.sym("L802E27F4", flag={"GLOBL","LOCAL"}),
	0x802E1918: main.sym("L802E2828", flag={"GLOBL","LOCAL"}),
	0x802E194C: main.sym("L802E285C", flag={"GLOBL","LOCAL"}),
	0x802E1980: main.sym("L802E2890", flag={"GLOBL","LOCAL"}),
	0x802E19B4: main.sym("L802E28C4", flag={"GLOBL","LOCAL"}),
	0x802E19DC: main.sym("MapObjLoad", flag={"GLOBL"}),
	0x802E1B9C: main.sym("L802E2AAC", flag={"GLOBL","LOCAL"}),
	0x802E1BC8: main.sym("L802E2AD8", flag={"GLOBL","LOCAL"}),
	0x802E1C20: main.sym("L802E2B30", flag={"GLOBL","LOCAL"}),
	0x802E1CA0: main.sym("L802E2BB0", flag={"GLOBL","LOCAL"}),
	0x802E1D4C: main.sym("L802E2C5C", flag={"GLOBL","LOCAL"}),

	# src/hud.c
	0x802E1DE0: main.sym("HUD_DrawChar"),
	0x802E1F48: main.sym("HUD_Draw8x8"),
	0x802E21A4: main.sym("MeterDrawN"),
	0x802E2304: main.sym("MeterDraw"),
	0x802E24A8: main.sym("MeterAlert"),
	0x802E2520: main.sym("MeterShow"),
	0x802E25D4: main.sym("MeterHide"),
	0x802E261C: main.sym("MeterProc"),
	0x802E2744: main.sym("HUD_DrawPower"),
	0x802E2834: main.sym("HUD_DrawLife"),
	0x802E2898: main.sym("HUD_DrawCoin"),
	0x802E28FC: main.sym("HUD_DrawStar"),
	0x802E29D4: main.sym("HUD_DrawKey"),
	0x802E2A4C: main.sym("HUD_DrawTime"),
	0x802E2C0C: main.sym("HUD_SetCamera", flag={"GLOBL"}),
	0x802E2C2C: main.sym("HUD_DrawCamera"),
	0x802E2E1C: main.sym("HUD_Draw", flag={"GLOBL"}),

	# src/object_b.c
	0x802E2F40: main.sym("object_b_802E3E50", flag={"GLOBL"}),
	#0x802E3E68: main.sym("object_b_802E3E68"),
	0x802E3058: main.sym("object_b_802E3F68"),
	0x802E309C: main.sym("object_b_802E3FAC"),
	0x802E314C: main.sym("object_b_802E405C"),
	0x802E3294: main.sym("object_b_802E41A4"),
	0x802E33D0: main.sym("object_b_802E42E0"),
	0x802E34D4: main.sym("object_b_802E43E4"),
	0x802E354C: main.sym("object_b_802E445C"),
	0x802E3904: main.sym("object_b_802E4814"),
	0x802E3DDC: main.sym("object_b_802E4CEC"),
	0x802E3E78: main.sym("object_b_802E4D88"),
	0x802E3F80: main.sym("object_b_802E4E90"),
	0x802E4204: main.sym("object_b_802E5114"),
	0x802E4250: main.sym("object_b_802E5160"),
	0x802E42F8: main.sym("object_b_802E5208"),
	0x802E43A8: main.sym("object_b_802E52B8"),
	0x802E4450: main.sym("object_b_802E5360"),
	0x802E44E4: main.sym("object_b_802E53F4"),
	0x802E45A0: main.sym("object_b_802E54B0"),
	0x802E46C0: main.sym("object_b_802E55D0"),
	0x802E478C: main.sym("object_b_802E569C"),
	0x802E4850: main.sym("object_b_802E5760"),
	0x802E4914: main.sym("object_b_802E5824"),
	0x802E49A4: main.sym("object_b_802E58B4"),
	0x802E4A38: main.sym("object_b_802E5948"),
	0x802E4B70: main.sym("object_b_802E5A80"),
	0x802E4C08: main.sym("object_b_802E5B18"),
	0x802E4D5C: main.sym("object_b_802E5C6C"),
	#0x802E5D04: main.sym("object_b_802E5D04"),
	0x802E4ED8: main.sym("object_b_802E5DE8"),
	0x802E4F5C: main.sym("object_b_802E5E6C"),
	0x802E4F94: main.sym("object_b_802E5EA4"),
	#0x802E5EE8: main.sym("object_b_802E5EE8", flag={"GLOBL"}),
	#0x802E5F64: main.sym("object_b_802E5F64", flag={"GLOBL"}),
	#0x802E6098: main.sym("object_b_802E6098", flag={"GLOBL"}),
	#0x802E6114: main.sym("object_b_802E6114", flag={"GLOBL"}),
	#0x802E62A4: main.sym("object_b_802E62A4", flag={"GLOBL"}),
	0x802E540C: main.sym("object_b_802E631C"),
	0x802E54DC: main.sym("object_b_802E63EC"),
	#0x802E6474: main.sym("object_b_802E6474", flag={"GLOBL"}),
	0x802E55E0: main.sym("L802E64F0", flag={"GLOBL","LOCAL"}),
	0x802E5630: main.sym("L802E6540", flag={"GLOBL","LOCAL"}),
	0x802E5640: main.sym("L802E6550", flag={"GLOBL","LOCAL"}),
	0x802E5660: main.sym("L802E6570", flag={"GLOBL","LOCAL"}),
	0x802E5698: main.sym("L802E65A8", flag={"GLOBL","LOCAL"}),
	#0x802E6628: main.sym("object_b_802E6628", flag={"GLOBL"}),
	0x802E5750: main.sym("L802E6660", flag={"GLOBL","LOCAL"}),
	0x802E57C4: main.sym("L802E66D4", flag={"GLOBL","LOCAL"}),
	0x802E57D4: main.sym("L802E66E4", flag={"GLOBL","LOCAL"}),
	0x802E57F4: main.sym("L802E6704", flag={"GLOBL","LOCAL"}),
	0x802E582C: main.sym("L802E673C", flag={"GLOBL","LOCAL"}),
	#0x802E6790: main.sym("object_b_802E6790", flag={"GLOBL"}),
	#0x802E67DC: main.sym("object_b_802E67DC", flag={"GLOBL"}),
	#0x802E6A2C: main.sym("object_b_802E6A2C", flag={"GLOBL"}),
	0x802E5B7C: main.sym("object_b_802E6A8C"),
	0x802E5BE8: main.sym("object_b_802E6AF8"),
	0x802E5CC4: main.sym("object_b_802E6BD4"),
	0x802E5DE0: main.sym("object_b_802E6CF0"),
	0x802E5EB8: main.sym("object_b_802E6DC8"),
	0x802E5F74: main.sym("object_b_802E6E84"),
	0x802E5FC8: main.sym("object_b_802E6ED8"),
	0x802E6110: main.sym("object_b_802E7020"),
	0x802E6224: main.sym("object_b_802E7134"),
	0x802E6270: main.sym("object_b_802E7180"),
	0x802E6310: main.sym("object_b_802E7220"),
	0x802E6370: main.sym("object_b_802E7280"),
	0x802E6414: main.sym("object_b_802E7324"),
	#0x802E742C: main.sym("object_b_802E742C", flag={"GLOBL"}),
	#0x802E75A0: main.sym("object_b_802E75A0", flag={"GLOBL"}),
	#0x802E76AC: main.sym("object_b_802E76AC", flag={"GLOBL"}),
	0x802E67FC: main.sym("object_b_802E770C"),
	0x802E6904: main.sym("object_b_802E7814"),
	0x802E6ACC: main.sym("object_b_802E79DC"),
	0x802E6BF0: main.sym("object_b_802E7B00"),
	0x802E6CA0: main.sym("object_b_802E7BB0"),
	#0x802E7C4C: main.sym("object_b_802E7C4C", flag={"GLOBL"}),
	0x802E6D80: main.sym("object_b_802E7C90", flag={"GLOBL"}),
	0x802E6E3C: main.sym("object_b_802E7D4C"),
	#0x802E7E54: main.sym("object_b_802E7E54", flag={"GLOBL"}),
	#0x802E7F70: main.sym("object_b_802E7F70", flag={"GLOBL"}),
	0x802E70A8: main.sym("object_b_802E7FB8"),
	0x802E70DC: main.sym("object_b_802E7FEC"),
	#0x802E80DC: main.sym("object_b_802E80DC", flag={"GLOBL"}),
	#0x802E82B0: main.sym("object_b_802E82B0", flag={"GLOBL"}),
	#0x802E8388: main.sym("object_b_802E8388", flag={"GLOBL"}),
	0x802E753C: main.sym("object_b_802E844C"),
	0x802E75BC: main.sym("object_b_802E84CC"),
	0x802E7708: main.sym("object_b_802E8618"),
	0x802E794C: main.sym("object_b_802E885C"),
	0x802E7A10: main.sym("object_b_802E8920"),
	#0x802E89D4: main.sym("object_b_802E89D4", flag={"GLOBL"}),
	0x802E7AFC: main.sym("L802E8A0C", flag={"GLOBL","LOCAL"}),
	0x802E7B54: main.sym("L802E8A64", flag={"GLOBL","LOCAL"}),
	0x802E7B64: main.sym("L802E8A74", flag={"GLOBL","LOCAL"}),
	0x802E7B80: main.sym("L802E8A90", flag={"GLOBL","LOCAL"}),
	0x802E7B90: main.sym("L802E8AA0", flag={"GLOBL","LOCAL"}),
	#0x802E8AE4: main.sym("object_b_802E8AE4", flag={"GLOBL"}),
	0x802E7D08: main.sym("object_b_802E8C18"),
	0x802E7E88: main.sym("object_b_802E8D98"),
	#0x802E8ECC: main.sym("object_b_802E8ECC", flag={"GLOBL"}),
	#0x802E8F68: main.sym("object_b_802E8F68", flag={"GLOBL"}),
	0x802E8108: main.sym("object_b_802E9018"),
	0x802E8368: main.sym("object_b_802E9278"),
	0x802E8560: main.sym("object_b_802E9470"),
	0x802E85D4: main.sym("object_b_802E94E4"),
	0x802E8638: main.sym("object_b_802E9548"),
	#0x802E96C8: main.sym("object_b_802E96C8", flag={"GLOBL"}),
	#0x802E9764: main.sym("object_b_802E9764", flag={"GLOBL"}),
	0x802E88EC: main.sym("object_b_802E97FC"),
	0x802E89B0: main.sym("object_b_802E98C0"),
	0x802E8B3C: main.sym("object_b_802E9A4C"),
	0x802E8DE4: main.sym("object_b_802E9CF4"),
	0x802E8E88: main.sym("object_b_802E9D98"),
	0x802E9050: main.sym("object_b_802E9F60"),
	0x802E9234: main.sym("object_b_802EA144"),
	0x802E9348: main.sym("object_b_802EA258"),
	0x802E94E0: main.sym("object_b_802EA3F0"),
	0x802E95DC: main.sym("object_b_802EA4EC"),
	#0x802EA588: main.sym("object_b_802EA588", flag={"GLOBL"}),
	#0x802EA6A8: main.sym("object_b_802EA6A8", flag={"GLOBL"}),
	0x802E97E8: main.sym("object_b_802EA6F8"),
	0x802E984C: main.sym("object_b_802EA75C"),
	#0x802EA7E0: main.sym("object_b_802EA7E0", flag={"GLOBL"}),
	#0x802EA888: main.sym("object_b_802EA888", flag={"GLOBL"}),
	#0x802EA934: main.sym("object_b_802EA934", flag={"GLOBL"}),
	#0x802EAA10: main.sym("object_b_802EAA10", flag={"GLOBL"}),
	#0x802EAA50: main.sym("object_b_802EAA50", flag={"GLOBL"}),
	#0x802EAA8C: main.sym("object_b_802EAA8C", flag={"GLOBL"}),
	#0x802EAAD0: main.sym("object_b_802EAAD0", flag={"GLOBL"}),
	#0x802EABF0: main.sym("object_b_802EABF0", flag={"GLOBL"}),
	#0x802EAC3C: main.sym("object_b_802EAC3C", flag={"GLOBL"}),
	#0x802EAD3C: main.sym("object_b_802EAD3C", flag={"GLOBL"}),
	#0x802EAEF8: main.sym("object_b_802EAEF8", flag={"GLOBL"}),
	0x802EA074: main.sym("object_b_802EAF84"),
	#0x802EB05C: main.sym("object_b_802EB05C", flag={"GLOBL"}),
	#0x802EB104: main.sym("object_b_802EB104", flag={"GLOBL"}),
	0x802EA2B0: main.sym("object_b_802EB1C0"),
	0x802EA378: main.sym("object_b_802EB288"),
	0x802EA4E0: main.sym("object_b_802EB3F0"),
	0x802EA600: main.sym("object_b_802EB510"),
	0x802EA6B4: main.sym("object_b_802EB5C4"),
	0x802EA720: main.sym("object_b_802EB630"),
	0x802EA834: main.sym("object_b_802EB744"),
	0x802EA8D0: main.sym("object_b_802EB7E0"),
	0x802EA9A0: main.sym("object_b_802EB8B0"),
	#0x802EB9D0: main.sym("object_b_802EB9D0", flag={"GLOBL"}),
	0x802EAC64: main.sym("object_b_802EBB74"),
	#0x802EBC00: main.sym("object_b_802EBC00", flag={"GLOBL"}),
	0x802EAD78: main.sym("object_b_802EBC88"),
	#0x802EBCE0: main.sym("object_b_802EBCE0", flag={"GLOBL"}),
	0x802EAE84: main.sym("L802EBD94", flag={"GLOBL","LOCAL"}),
	0x802EAEF4: main.sym("L802EBE04", flag={"GLOBL","LOCAL"}),
	0x802EAF0C: main.sym("L802EBE1C", flag={"GLOBL","LOCAL"}),
	0x802EAF24: main.sym("L802EBE34", flag={"GLOBL","LOCAL"}),
	0x802EAF3C: main.sym("L802EBE4C", flag={"GLOBL","LOCAL"}),
	0x802EAF8C: main.sym("L802EBE9C", flag={"GLOBL","LOCAL"}),
	0x802EB060: main.sym("object_b_802EBF70"),
	0x802EB120: main.sym("object_b_802EC030"),
	#0x802EC1B0: main.sym("object_b_802EC1B0", flag={"GLOBL"}),
	0x802EB2F0: main.sym("object_b_802EC200"),
	0x802EB4A8: main.sym("object_b_802EC3D0"),
	0x802EB5B8: main.sym("object_b_802EC4E0"),
	0x802EB674: main.sym("object_b_802EC59C"),
	#0x802EC75C: main.sym("object_b_802EC75C", flag={"GLOBL"}),
	#0x802EC7CC: main.sym("object_b_802EC7CC"),
	0x802EB8F0: main.sym("object_b_802EC818"),
	#0x802EC908: main.sym("object_b_802EC908", flag={"GLOBL"}),
	#0x802EC9B8: main.sym("object_b_802EC9B8", flag={"GLOBL"}),
	0x802EBAC8: main.sym("object_b_802EC9F0"),
	#0x802ECBA4: main.sym("object_b_802ECBA4", flag={"GLOBL"}),
	#0x802ECC14: main.sym("object_b_802ECC14", flag={"GLOBL"}),
	#0x802ECD0C: main.sym("object_b_802ECD0C", flag={"GLOBL"}),
	#0x802ECEA0: main.sym("object_b_802ECEA0", flag={"GLOBL"}),
	#0x802ECFAC: main.sym("object_b_802ECFAC", flag={"GLOBL"}),
	0x802EC164: main.sym("object_b_802ED10C"),
	0x802EC2E4: main.sym("object_b_802ED28C"),
	#0x802ED39C: main.sym("object_b_802ED39C", flag={"GLOBL"}),
	#0x802ED40C: main.sym("object_b_802ED40C", flag={"GLOBL"}),
	#0x802ED45C: main.sym("object_b_802ED45C", flag={"GLOBL"}),
	#0x802ED498: main.sym("object_b_802ED498", flag={"GLOBL"}),
	#0x802ED62C: main.sym("object_b_802ED62C", flag={"GLOBL"}),
	#0x802ED78C: main.sym("object_b_802ED78C", flag={"GLOBL"}),
	#0x802ED7FC: main.sym("object_b_802ED7FC", flag={"GLOBL"}),
	#0x802EDACC: main.sym("object_b_802EDACC", flag={"GLOBL"}),
	#0x802EDB2C: main.sym("object_b_802EDB2C", flag={"GLOBL"}),
	#0x802EDDFC: main.sym("object_b_802EDDFC", flag={"GLOBL"}),
	#0x802EDF28: main.sym("object_b_802EDF28", flag={"GLOBL"}),
	#0x802EE124: main.sym("object_b_802EE124", flag={"GLOBL"}),
	0x802ED1A8: main.sym("object_b_802EE1A0"),
	0x802ED270: main.sym("object_b_802EE268"),
	0x802ED2C0: main.sym("L802EE2B8", flag={"GLOBL","LOCAL"}),
	0x802ED340: main.sym("L802EE338", flag={"GLOBL","LOCAL"}),
	0x802ED398: main.sym("L802EE390", flag={"GLOBL","LOCAL"}),
	0x802ED3C8: main.sym("L802EE3C0", flag={"GLOBL","LOCAL"}),
	0x802ED434: main.sym("L802EE42C", flag={"GLOBL","LOCAL"}),
	0x802ED474: main.sym("object_b_802EE46C"),
	0x802ED5A0: main.sym("object_b_802EE598"),
	0x802ED724: main.sym("object_b_802EE728"),
	0x802ED774: main.sym("object_b_802EE778"),
	#0x802EE7E0: main.sym("object_b_802EE7E0", flag={"GLOBL"}),
	0x802ED814: main.sym("L802EE818", flag={"GLOBL","LOCAL"}),
	0x802ED878: main.sym("L802EE87C", flag={"GLOBL","LOCAL"}),
	0x802ED8A8: main.sym("L802EE8AC", flag={"GLOBL","LOCAL"}),
	0x802ED8B8: main.sym("L802EE8BC", flag={"GLOBL","LOCAL"}),
	0x802ED8C8: main.sym("L802EE8CC", flag={"GLOBL","LOCAL"}),
	#0x802EE8F4: main.sym("object_b_802EE8F4", flag={"GLOBL"}),
	#0x802EE9CC: main.sym("object_b_802EE9CC", flag={"GLOBL"}),
	0x802EDA14: main.sym("object_b_802EEA24"),
	0x802EDA6C: main.sym("object_b_802EEA7C"),
	0x802EDAA4: main.sym("L802EEAB4", flag={"GLOBL","LOCAL"}),
	0x802EDAC4: main.sym("L802EEAD4", flag={"GLOBL","LOCAL"}),
	0x802EDAE4: main.sym("L802EEAF4", flag={"GLOBL","LOCAL"}),
	0x802EDB04: main.sym("L802EEB14", flag={"GLOBL","LOCAL"}),
	0x802EDB20: main.sym("L802EEB30", flag={"GLOBL","LOCAL"}),
	0x802EDB54: main.sym("object_b_802EEB64"),
	0x802EDCA8: main.sym("object_b_802EECB8"),
	0x802EDD04: main.sym("L802EED14", flag={"GLOBL","LOCAL"}),
	0x802EDD24: main.sym("L802EED34", flag={"GLOBL","LOCAL"}),
	0x802EDD44: main.sym("L802EED54", flag={"GLOBL","LOCAL"}),
	0x802EDD64: main.sym("L802EED74", flag={"GLOBL","LOCAL"}),
	0x802EDD84: main.sym("L802EED94", flag={"GLOBL","LOCAL"}),
	#0x802EEDF0: main.sym("object_b_802EEDF0", flag={"GLOBL"}),
	#0x802EEEB4: main.sym("object_b_802EEEB4", flag={"GLOBL"}),
	#0x802EEF9C: main.sym("object_b_802EEF9C", flag={"GLOBL"}),
	#0x802EF0E8: main.sym("object_b_802EF0E8", flag={"GLOBL"}),
	#0x802EF21C: main.sym("object_b_802EF21C", flag={"GLOBL"}),
	#0x802EF274: main.sym("object_b_802EF274", flag={"GLOBL"}),
	0x802EE33C: main.sym("object_b_802EF34C", flag={"GLOBL"}),
	0x802EE3E4: main.sym("object_b_802EF3F4"),
	#0x802EF524: main.sym("object_b_802EF524", flag={"GLOBL"}),
	#0x802EF63C: main.sym("object_b_802EF63C", flag={"GLOBL"}),
	#0x802EF66C: main.sym("object_b_802EF66C", flag={"GLOBL"}),
	#0x802EF820: main.sym("object_b_802EF820", flag={"GLOBL"}),
	#0x802EF858: main.sym("object_b_802EF858", flag={"GLOBL"}),
	#0x802EFCD0: main.sym("object_b_802EFCD0", flag={"GLOBL"}),
	#0x802EFD8C: main.sym("object_b_802EFD8C", flag={"GLOBL"}),
	#0x802EFE64: main.sym("object_b_802EFE64", flag={"GLOBL"}),
	#0x802EFEF4: main.sym("object_b_802EFEF4", flag={"GLOBL"}),
	#0x802F0104: main.sym("object_b_802F0104", flag={"GLOBL"}),
	#0x802F0168: main.sym("object_b_802F0168", flag={"GLOBL"}),
	0x802EF238: main.sym("object_b_802F0288"),
	0x802EF450: main.sym("object_b_802F04A0"),
	#0x802F05B4: main.sym("object_b_802F05B4", flag={"GLOBL"}),
	#0x802F06A8: main.sym("object_b_802F06A8", flag={"GLOBL"}),
	#0x802F0714: main.sym("object_b_802F0714", flag={"GLOBL"}),
	#0x802F0788: main.sym("object_b_802F0788", flag={"GLOBL"}),
	#0x802F07F4: main.sym("object_b_802F07F4", flag={"GLOBL"}),
	#0x802F0820: main.sym("object_b_802F0820", flag={"GLOBL"}),
	#0x802F084C: main.sym("object_b_802F084C", flag={"GLOBL"}),
	#0x802F0898: main.sym("object_b_802F0898", flag={"GLOBL"}),
	#0x802F0950: main.sym("object_b_802F0950", flag={"GLOBL"}),
	#0x802F09A4: main.sym("object_b_802F09A4", flag={"GLOBL"}),
	#0x802F09F0: main.sym("object_b_802F09F0", flag={"GLOBL"}),
	#0x802F0A40: main.sym("object_b_802F0A40", flag={"GLOBL"}),
	0x802EFB2C: main.sym("object_b_802F0B7C"),
	0x802EFB84: main.sym("object_b_802F0BD4"),
	0x802EFC44: main.sym("object_b_802F0C94"),
	0x802EFDA0: main.sym("object_b_802F0DF0"),
	0x802EFF58: main.sym("object_b_802F0FA8"),
	#0x802F105C: main.sym("object_b_802F105C", flag={"GLOBL"}),
	0x802F0044: main.sym("L802F1094", flag={"GLOBL","LOCAL"}),
	0x802F00DC: main.sym("L802F112C", flag={"GLOBL","LOCAL"}),
	0x802F0108: main.sym("L802F1158", flag={"GLOBL","LOCAL"}),
	0x802F0134: main.sym("L802F1184", flag={"GLOBL","LOCAL"}),
	0x802F0144: main.sym("L802F1194", flag={"GLOBL","LOCAL"}),
	#0x802F120C: main.sym("object_b_802F120C", flag={"GLOBL"}),
	#0x802F1370: main.sym("object_b_802F1370", flag={"GLOBL"}),
	0x802F0358: main.sym("L802F13A8", flag={"GLOBL","LOCAL"}),
	0x802F0394: main.sym("L802F13E4", flag={"GLOBL","LOCAL"}),
	0x802F039C: main.sym("L802F13EC", flag={"GLOBL","LOCAL"}),
	0x802F03D0: main.sym("L802F1420", flag={"GLOBL","LOCAL"}),
	0x802F043C: main.sym("L802F148C", flag={"GLOBL","LOCAL"}),
	#0x802F151C: main.sym("object_b_802F151C", flag={"GLOBL"}),
	#0x802F15A8: main.sym("object_b_802F15A8", flag={"GLOBL"}),
	0x802F05DC: main.sym("object_b_802F162C"),
	#0x802F1714: main.sym("object_b_802F1714", flag={"GLOBL"}),
	#0x802F17F0: main.sym("object_b_802F17F0", flag={"GLOBL"}),
	0x802F0904: main.sym("object_b_802F1954"),
	0x802F0978: main.sym("object_b_802F19C8"),
	0x802F09C0: main.sym("object_b_802F1A10"),
	0x802F0A0C: main.sym("L802F1A5C", flag={"GLOBL","LOCAL"}),
	0x802F0A20: main.sym("L802F1A70", flag={"GLOBL","LOCAL"}),
	0x802F0A4C: main.sym("L802F1A9C", flag={"GLOBL","LOCAL"}),
	0x802F0ABC: main.sym("L802F1B0C", flag={"GLOBL","LOCAL"}),
	0x802F0AE8: main.sym("L802F1B38", flag={"GLOBL","LOCAL"}),
	0x802F0B58: main.sym("L802F1BA8", flag={"GLOBL","LOCAL"}),
	0x802F0B68: main.sym("object_b_802F1BB8"),
	#0x802F1D64: main.sym("object_b_802F1D64", flag={"GLOBL"}),
	0x802F0D70: main.sym("object_b_802F1DC0"),
	0x802F0E0C: main.sym("object_b_802F1E5C"),
	#0x802F1F3C: main.sym("object_b_802F1F3C", flag={"GLOBL"}),
	#0x802F1FD0: main.sym("object_b_802F1FD0", flag={"GLOBL"}),
	0x802F0FE0: main.sym("object_b_802F2030"),
	#0x802F20AC: main.sym("object_b_802F20AC", flag={"GLOBL"}),
	#0x802F2140: main.sym("object_b_802F2140", flag={"GLOBL"}),
	0x802F1190: main.sym("object_b_802F21E0"),
	0x802F1234: main.sym("object_b_802F2284"),
	#0x802F23A8: main.sym("object_b_802F23A8", flag={"GLOBL"}),
	#0x802F2498: main.sym("object_b_802F2498", flag={"GLOBL"}),
	#0x802F24F4: main.sym("object_b_802F24F4", flag={"GLOBL"}),
	#0x802F25B0: main.sym("object_b_802F25B0", flag={"GLOBL"}),
	#0x802F2614: main.sym("object_b_802F2614", flag={"GLOBL"}),
	#0x802F2768: main.sym("object_b_802F2768", flag={"GLOBL"}),
	0x802F1A50: main.sym("object_b_802F2AA0"),
	0x802F1B38: main.sym("object_b_802F2B88", flag={"GLOBL"}),
	0x802F1B84: main.sym("object_b_802F2BD4"),
	0x802F1BD4: main.sym("object_b_802F2C24"),
	#0x802F2C84: main.sym("object_b_802F2C84", flag={"GLOBL"}),
	#0x802F2D8C: main.sym("object_b_802F2D8C", flag={"GLOBL"}),
	#0x802F2E6C: main.sym("RedCoin_Init", flag={"GLOBL"}),
	#0x802F2F2C: main.sym("RedCoin_Proc", flag={"GLOBL"}),
	#0x802F3014: main.sym("object_b_802F3014", flag={"GLOBL"}),
	#0x802F30F0: main.sym("object_b_802F30F0", flag={"GLOBL"}),
	#0x802F31BC: main.sym("object_b_802F31BC", flag={"GLOBL"}),
	#0x802F328C: main.sym("object_b_802F328C", flag={"GLOBL"}),
	#0x802F336C: main.sym("object_b_802F336C", flag={"GLOBL"}),
	0x802F238C: main.sym("object_b_802F341C"),
	#0x802F36A4: main.sym("object_b_802F36A4", flag={"GLOBL"}),
	0x802F2820: main.sym("object_b_802F38B0"),
	0x802F2924: main.sym("object_b_802F39B4"),
	#0x802F3A30: main.sym("object_b_802F3A30", flag={"GLOBL"}),
	#0x802F3B98: main.sym("object_b_802F3B98", flag={"GLOBL"}),
	0x802F2BC4: main.sym("object_b_802F3C54"),
	0x802F2C38: main.sym("object_b_802F3CC8", flag={"GLOBL"}),
	#0x802F3D30: main.sym("object_b_802F3D30", flag={"GLOBL"}),
	0x802F2D40: main.sym("object_b_802F3DD0"),
	0x802F2E18: main.sym("object_b_802F3EA8"),
	0x802F2F8C: main.sym("object_b_802F401C"),
	#0x802F40CC: main.sym("object_b_802F40CC", flag={"GLOBL"}),
	#0x802F4248: main.sym("object_b_802F4248", flag={"GLOBL"}),
	0x802F3328: main.sym("object_b_802F43B8"),
	#0x802F44C0: main.sym("object_b_802F44C0", flag={"GLOBL"}),
	#0x802F45B8: main.sym("object_b_802F45B8", flag={"GLOBL"}),
	#0x802F45F0: main.sym("object_b_802F45F0", flag={"GLOBL"}),
	#0x802F4710: main.sym("object_b_802F4710", flag={"GLOBL"}),
	#0x802F48F4: main.sym("object_b_802F48F4", flag={"GLOBL"}),
	#0x802F496C: main.sym("object_b_802F496C", flag={"GLOBL"}),
	#0x802F4B00: main.sym("object_b_802F4B00", flag={"GLOBL"}),
	#0x802F4B78: main.sym("object_b_802F4B78", flag={"GLOBL"}),
	0x802F3BD8: main.sym("object_b_802F4C68"),
	0x802F3C50: main.sym("object_b_802F4CE0"),
	#0x802F4D78: main.sym("object_b_802F4D78", flag={"GLOBL"}),
	#0x802F4EB4: main.sym("object_b_802F4EB4", flag={"GLOBL"}),
	0x802F3F80: main.sym("object_b_802F5010"),
	0x802F3FD8: main.sym("object_b_802F5068"),
	0x802F4230: main.sym("object_b_802F52C0"),
	0x802F43EC: main.sym("object_b_802F547C"),
	#0x802F55A4: main.sym("object_b_802F55A4", flag={"GLOBL"}),
	0x802F4588: main.sym("L802F5618", flag={"GLOBL","LOCAL"}),
	0x802F4610: main.sym("L802F56A0", flag={"GLOBL","LOCAL"}),
	0x802F4758: main.sym("L802F57E8", flag={"GLOBL","LOCAL"}),
	0x802F48A0: main.sym("L802F5930", flag={"GLOBL","LOCAL"}),
	0x802F49E8: main.sym("L802F5A78", flag={"GLOBL","LOCAL"}),
	0x802F4B30: main.sym("L802F5BC0", flag={"GLOBL","LOCAL"}),
	0x802F4B48: main.sym("L802F5BD8", flag={"GLOBL","LOCAL"}),
	#0x802F5CD4: main.sym("object_b_802F5CD4", flag={"GLOBL"}),
	0x802F4CE8: main.sym("object_b_802F5D78"),
	0x802F4DB4: main.sym("object_b_802F5E44"),
	0x802F4EB8: main.sym("object_b_802F5F48"),
	0x802F4F84: main.sym("object_b_802F6014"),
	0x802F5048: main.sym("object_b_802F60D8"),
	0x802F50C0: main.sym("object_b_802F6150"),
	#0x802F6228: main.sym("object_b_802F6228", flag={"GLOBL"}),
	#0x802F62E4: main.sym("object_b_802F62E4", flag={"GLOBL"}),
	#0x802F6448: main.sym("object_b_802F6448", flag={"GLOBL"}),
	0x802F54F8: main.sym("object_b_802F6588"),
	0x802F55CC: main.sym("object_b_802F665C"),
	#0x802F6984: main.sym("object_b_802F6984", flag={"GLOBL"}),
	0x802F59B4: main.sym("object_b_802F6A44"),
	0x802F5A9C: main.sym("object_b_802F6B2C"),
	#0x802F6C0C: main.sym("object_b_802F6C0C", flag={"GLOBL"}),
	#0x802F6D20: main.sym("object_b_802F6D20", flag={"GLOBL"}),
	#0x802F6D58: main.sym("object_b_802F6D58", flag={"GLOBL"}),
	#0x802F6E40: main.sym("object_b_802F6E40", flag={"GLOBL"}),
	0x802F5E20: main.sym("object_b_802F6EB0"),
	0x802F5FD8: main.sym("object_b_802F7068"),
	#0x802F7264: main.sym("object_b_802F7264", flag={"GLOBL"}),
	#0x802F7348: main.sym("object_b_802F7348", flag={"GLOBL"}),
	0x802F6308: main.sym("object_b_802F7398"),
	0x802F6388: main.sym("object_b_802F7418"),
	#0x802F74DC: main.sym("object_b_802F74DC", flag={"GLOBL"}),
	#0x802F7760: main.sym("object_b_802F7760", flag={"GLOBL"}),
	#0x802F7924: main.sym("object_b_802F7924", flag={"GLOBL"}),
	#0x802F7978: main.sym("object_b_802F7978", flag={"GLOBL"}),
	#0x802F79B0: main.sym("object_b_802F79B0", flag={"GLOBL"}),
	#0x802F7A58: main.sym("object_b_802F7A58", flag={"GLOBL"}),
	#0x802F7C9C: main.sym("object_b_802F7C9C", flag={"GLOBL"}),
	#0x802F7D04: main.sym("object_b_802F7D04", flag={"GLOBL"}),
	0x802F6E8C: main.sym("object_b_802F7F1C"),
	#0x802F7FA0: main.sym("object_b_802F7FA0", flag={"GLOBL"}),
	#0x802F8044: main.sym("object_b_802F8044", flag={"GLOBL"}),
	#0x802F8158: main.sym("object_b_802F8158", flag={"GLOBL"}),
	#0x802F8208: main.sym("object_b_802F8208", flag={"GLOBL"}),
	#0x802F82F8: main.sym("object_b_802F82F8", flag={"GLOBL"}),
	#0x802F83A4: main.sym("object_b_802F83A4", flag={"GLOBL"}),
	#0x802F8490: main.sym("object_b_802F8490", flag={"GLOBL"}),
	0x802F7528: main.sym("object_b_802F85E0"),
	0x802F76A8: main.sym("object_b_802F8760"),
	0x802F7750: main.sym("object_b_802F8808"),
	0x802F788C: main.sym("object_b_802F893C"),
	0x802F78D8: main.sym("object_b_802F8988"),
	0x802F7984: main.sym("object_b_802F8A34"),
	0x802F7A04: main.sym("object_b_802F8AB4"),
	0x802F7A3C: main.sym("L802F8AEC", flag={"GLOBL","LOCAL"}),
	0x802F7A4C: main.sym("L802F8AFC", flag={"GLOBL","LOCAL"}),
	0x802F7A5C: main.sym("L802F8B0C", flag={"GLOBL","LOCAL"}),
	0x802F7A6C: main.sym("L802F8B1C", flag={"GLOBL","LOCAL"}),
	0x802F7A7C: main.sym("L802F8B2C", flag={"GLOBL","LOCAL"}),
	0x802F7AA4: main.sym("object_b_802F8B54"),
	0x802F7BC4: main.sym("object_b_802F8C74"),
	0x802F7C48: main.sym("object_b_802F8CF8"),
	#0x802F8DAC: main.sym("object_b_802F8DAC", flag={"GLOBL"}),
	#0x802F8E54: main.sym("object_b_802F8E54", flag={"GLOBL"}),
	0x802F7E58: main.sym("object_b_802F8F08"),
	0x802F7FA4: main.sym("object_b_802F9054"),
	0x802F818C: main.sym("object_b_802F923C"),
	0x802F82F8: main.sym("object_b_802F93A8"),
	0x802F8450: main.sym("object_b_802F9500"),
	0x802F84FC: main.sym("object_b_802F95AC"),
	#0x802F965C: main.sym("object_b_802F965C", flag={"GLOBL"}),
	0x802F85E4: main.sym("L802F9694", flag={"GLOBL","LOCAL"}),
	0x802F85F4: main.sym("L802F96A4", flag={"GLOBL","LOCAL"}),
	0x802F8604: main.sym("L802F96B4", flag={"GLOBL","LOCAL"}),
	0x802F8614: main.sym("L802F96C4", flag={"GLOBL","LOCAL"}),
	0x802F8624: main.sym("L802F96D4", flag={"GLOBL","LOCAL"}),
	0x802F8634: main.sym("L802F96E4", flag={"GLOBL","LOCAL"}),
	0x802F8644: main.sym("L802F96F4", flag={"GLOBL","LOCAL"}),
	0x802F8654: main.sym("L802F9704", flag={"GLOBL","LOCAL"}),

	# src/object_c.c
	0x802F8680: main.sym("object_c_802F9730"),
	0x802F86C0: main.sym("object_c_802F9770"),
	0x802F870C: main.sym("object_c_802F97BC"),
	0x802F8770: main.sym("object_c_802F9820"),
	0x802F87E0: main.sym("object_c_802F9890"),
	0x802F8854: main.sym("object_c_802F9904"),
	0x802F8978: main.sym("object_c_802F9A28"),
	0x802F8D78: main.sym("object_c_802F9E28"),
	0x802F90A8: main.sym("object_c_802FA158"),
	0x802F9100: main.sym("object_c_802FA1B0"),
	0x802F9148: main.sym("object_c_802FA1F8"),
	0x802F91AC: main.sym("object_c_802FA25C"),
	0x802F920C: main.sym("object_c_802FA2BC"),
	0x802F927C: main.sym("object_c_802FA32C"),
	0x802F92B0: main.sym("object_c_802FA360"),
	0x802F92EC: main.sym("object_c_802FA39C"),
	0x802F932C: main.sym("object_c_802FA3DC"),
	0x802F9378: main.sym("object_c_802FA428"),
	0x802F9414: main.sym("object_c_802FA4C4"),
	0x802F9494: main.sym("object_c_802FA544"),
	0x802F9520: main.sym("object_c_802FA5D0"),
	0x802F9568: main.sym("object_c_802FA618"),
	0x802F95B0: main.sym("object_c_802FA660"),
	0x802F9624: main.sym("object_c_802FA6D4"),
	0x802F9698: main.sym("object_c_802FA748"),
	0x802F970C: main.sym("object_c_802FA7BC"),
	0x802F9780: main.sym("object_c_802FA830"),
	0x802F9850: main.sym("object_c_802FA900"),
	0x802F98B4: main.sym("object_c_802FA964"),
	0x802F9928: main.sym("object_c_802FA9D8"),
	0x802F99B4: main.sym("object_c_802FAA64"),
	0x802F9A18: main.sym("object_c_802FAAC8"),
	0x802F9B68: main.sym("object_c_802FAC18"),
	0x802F9C84: main.sym("object_c_802FAD34"),
	0x802F9D24: main.sym("object_c_802FADD4"),
	0x802F9F6C: main.sym("object_c_802FB01C"),
	0x802FA01C: main.sym("object_c_802FB0CC"),
	0x802FA078: main.sym("object_c_802FB128"),
	#0x802FB254: main.sym("object_c_802FB254"),
	0x802FA1D8: main.sym("object_c_802FB288"),
	0x802FA2F0: main.sym("object_c_802FB3A0"),
	0x802FA32C: main.sym("object_c_802FB3DC"),
	0x802FA468: main.sym("object_c_802FB518"),
	0x802FA560: main.sym("L802FB610", flag={"GLOBL","LOCAL"}),
	0x802FA568: main.sym("L802FB618", flag={"GLOBL","LOCAL"}),
	0x802FA578: main.sym("L802FB628", flag={"GLOBL","LOCAL"}),
	0x802FA588: main.sym("L802FB638", flag={"GLOBL","LOCAL"}),
	0x802FA598: main.sym("L802FB648", flag={"GLOBL","LOCAL"}),
	0x802FA5A8: main.sym("L802FB658", flag={"GLOBL","LOCAL"}),
	0x802FA5B8: main.sym("L802FB668", flag={"GLOBL","LOCAL"}),
	0x802FA5C8: main.sym("L802FB678", flag={"GLOBL","LOCAL"}),
	0x802FA5D8: main.sym("L802FB688", flag={"GLOBL","LOCAL"}),
	0x802FA638: main.sym("object_c_802FB6E8"),
	0x802FA6C8: main.sym("object_c_802FB778"),
	0x802FA7CC: main.sym("object_c_802FB87C"),
	0x802FA888: main.sym("object_c_802FB938"),
	0x802FA990: main.sym("object_c_802FBA40"),
	0x802FAA04: main.sym("object_c_802FBAB4"),
	#0x802FBC4C: main.sym("object_c_802FBC4C", flag={"GLOBL"}),
	0x802FACAC: main.sym("object_c_802FBD5C"),
	0x802FAD24: main.sym("object_c_802FBDD4"),
	0x802FADA0: main.sym("object_c_802FBE50"),
	0x802FAE1C: main.sym("object_c_802FBECC"),
	0x802FAEA8: main.sym("object_c_802FBF58"),
	0x802FAF2C: main.sym("object_c_802FBFDC"),
	0x802FAF8C: main.sym("object_c_802FC03C"),
	0x802FB0BC: main.sym("object_c_802FC16C"),
	0x802FB1D8: main.sym("object_c_802FC288"),
	0x802FB288: main.sym("object_c_802FC338"),
	0x802FB364: main.sym("object_c_802FC414"),
	0x802FB460: main.sym("object_c_802FC510"),
	0x802FB5C0: main.sym("object_c_802FC670"),
	0x802FB864: main.sym("object_c_802FC914"),
	0x802FBA44: main.sym("object_c_802FCAF4"),
	0x802FBA6C: main.sym("object_c_802FCB1C"),
	0x802FBB50: main.sym("object_c_802FCC00"),
	0x802FBC18: main.sym("object_c_802FCCC8"),
	0x802FBCB4: main.sym("object_c_802FCD64"),
	0x802FBDE4: main.sym("object_c_802FCE94"),
	0x802FBF64: main.sym("object_c_802FD014"),
	0x802FBFB8: main.sym("object_c_802FD068"),
	0x802FC334: main.sym("object_c_802FD3E4"),
	0x802FC3B4: main.sym("object_c_802FD464"),
	0x802FC400: main.sym("object_c_802FD4B0"),
	0x802FC5FC: main.sym("object_c_802FD6AC"),
	0x802FC658: main.sym("L802FD708", flag={"GLOBL","LOCAL"}),
	0x802FC668: main.sym("L802FD718", flag={"GLOBL","LOCAL"}),
	0x802FC678: main.sym("L802FD728", flag={"GLOBL","LOCAL"}),
	0x802FC688: main.sym("L802FD738", flag={"GLOBL","LOCAL"}),
	0x802FC698: main.sym("L802FD748", flag={"GLOBL","LOCAL"}),
	0x802FC6A8: main.sym("L802FD758", flag={"GLOBL","LOCAL"}),
	#0x802FD7F8: main.sym("object_c_802FD7F8", flag={"GLOBL"}),
	#0x802FD950: main.sym("object_c_802FD950", flag={"GLOBL"}),
	#0x802FDA28: main.sym("object_c_802FDA28", flag={"GLOBL"}),
	0x802FCDF8: main.sym("object_c_802FDEA8"),
	0x802FCF14: main.sym("object_c_802FDFC4"),
	0x802FD2CC: main.sym("object_c_802FE37C"),
	#0x802FE3B0: main.sym("object_c_802FE3B0", flag={"GLOBL"}),
	0x802FD3A0: main.sym("object_c_802FE450"),
	0x802FD470: main.sym("object_c_802FE520"),
	#0x802FE8B4: main.sym("object_c_802FE8B4", flag={"GLOBL"}),
	0x802FD8D8: main.sym("object_c_802FE988"),
	0x802FDA50: main.sym("object_c_802FEB00"),
	0x802FDCA0: main.sym("object_c_802FED50"),
	0x802FDE68: main.sym("object_c_802FEF18"),
	#0x802FF040: main.sym("object_c_802FF040", flag={"GLOBL"}),
	#0x802FF214: main.sym("object_c_802FF214", flag={"GLOBL"}),
	#0x802FF408: main.sym("object_c_802FF408", flag={"GLOBL"}),
	0x802FE468: main.sym("object_c_802FF518"),
	0x802FE4D4: main.sym("object_c_802FF584"),
	0x802FE550: main.sym("object_c_802FF600"),
	0x802FE7B8: main.sym("object_c_802FF868"),
	0x802FE838: main.sym("object_c_802FF8E8"),
	0x802FE89C: main.sym("object_c_802FF94C"),
	#0x802FF96C: main.sym("object_c_802FF96C", flag={"GLOBL"}),
	#0x802FFB38: main.sym("object_c_802FFB38", flag={"GLOBL"}),
	0x802FEBB0: main.sym("object_c_802FFC60"),
	0x802FECFC: main.sym("object_c_802FFDAC"),
	0x802FEFEC: main.sym("object_c_8030009C"),
	0x802FF034: main.sym("object_c_803000E4"),
	0x802FF244: main.sym("object_c_803002F4"),
	0x802FF440: main.sym("object_c_803004F0"),
	0x802FF4EC: main.sym("object_c_8030059C"),
	0x802FF6C8: main.sym("object_c_80300778"),
	0x802FF7F8: main.sym("object_c_803008A8"),
	0x802FF83C: main.sym("object_c_803008EC"),
	0x802FF890: main.sym("object_c_80300940"),
	0x802FF938: main.sym("L803009E8", flag={"GLOBL","LOCAL"}),
	0x802FF988: main.sym("L80300A38", flag={"GLOBL","LOCAL"}),
	0x802FF998: main.sym("L80300A48", flag={"GLOBL","LOCAL"}),
	0x802FF9A8: main.sym("L80300A58", flag={"GLOBL","LOCAL"}),
	0x802FF9B8: main.sym("L80300A68", flag={"GLOBL","LOCAL"}),
	0x802FF9C8: main.sym("L80300A78", flag={"GLOBL","LOCAL"}),
	0x802FFD24: main.sym("object_c_80300DD4"),
	#0x80300E40: main.sym("object_c_80300E40", flag={"GLOBL"}),
	#0x80300ECC: main.sym("object_c_80300ECC", flag={"GLOBL"}),
	#0x80301148: main.sym("object_c_80301148", flag={"GLOBL"}),
	#0x80301180: main.sym("object_c_80301180", flag={"GLOBL"}),
	#0x80301210: main.sym("object_c_80301210", flag={"GLOBL"}),
	0x8030041C: main.sym("object_c_803014CC"),
	0x80300630: main.sym("object_c_803016E0"),
	0x80300890: main.sym("object_c_80301940"),
	0x80300BD8: main.sym("object_c_80301C88"),
	0x80300DD4: main.sym("object_c_80301E84"),
	0x80300EC0: main.sym("object_c_80301F70"),
	0x80300F74: main.sym("object_c_80302024"),
	0x80301034: main.sym("object_c_803020E4"),
	#0x80302154: main.sym("object_c_80302154", flag={"GLOBL"}),
	0x803011C8: main.sym("L80302278", flag={"GLOBL","LOCAL"}),
	0x803011D8: main.sym("L80302288", flag={"GLOBL","LOCAL"}),
	0x803011E8: main.sym("L80302298", flag={"GLOBL","LOCAL"}),
	0x803011F8: main.sym("L803022A8", flag={"GLOBL","LOCAL"}),
	0x80301208: main.sym("L803022B8", flag={"GLOBL","LOCAL"}),
	0x803012A8: main.sym("object_c_80302358"),
	0x80301334: main.sym("object_c_803023E4"),
	0x803015CC: main.sym("object_c_8030267C"),
	0x803016FC: main.sym("object_c_803027AC"),
	#0x80302910: main.sym("object_c_80302910", flag={"GLOBL"}),
	0x80301908: main.sym("object_c_803029B8"),
	0x803019A4: main.sym("object_c_80302A54"),
	0x80301A70: main.sym("object_c_80302B20"),
	0x80301BD4: main.sym("object_c_80302C84"),
	0x80301D00: main.sym("object_c_80302DB0"),
	0x80301DD4: main.sym("object_c_80302E84"),
	0x80301E54: main.sym("object_c_80302F04"),
	#0x80303028: main.sym("object_c_80303028", flag={"GLOBL"}),
	0x80301FF8: main.sym("object_c_803030A8"),
	0x80302104: main.sym("object_c_803031B4"),
	0x8030215C: main.sym("object_c_8030320C"),
	0x803023E8: main.sym("object_c_80303498"),
	0x80302584: main.sym("object_c_80303634"),
	#0x8030369C: main.sym("object_c_8030369C", flag={"GLOBL"}),
	#0x80303744: main.sym("object_c_80303744", flag={"GLOBL"}),
	#0x80303984: main.sym("object_c_80303984", flag={"GLOBL"}),
	0x80302970: main.sym("object_c_80303A20"),
	0x80302A58: main.sym("object_c_80303B08"),
	0x80302B64: main.sym("object_c_80303C14"),
	#0x80303F64: main.sym("object_c_80303F64", flag={"GLOBL"}),
	0x803030BC: main.sym("object_c_803041A0"),
	0x80303190: main.sym("object_c_80304274"),
	#0x803043F8: main.sym("object_c_803043F8", flag={"GLOBL"}),
	0x80303390: main.sym("object_c_80304474"),
	#0x803044C0: main.sym("object_c_803044C0", flag={"GLOBL"}),
	0x803033F8: main.sym("object_c_803044DC"),
	0x8030362C: main.sym("object_c_80304710"),
	0x803036C8: main.sym("object_c_803047AC"),
	0x80303780: main.sym("object_c_80304864"),
	0x80303808: main.sym("object_c_803048EC"),
	0x80303874: main.sym("object_c_80304958"),
	0x80303930: main.sym("object_c_80304A14"),
	0x8030398C: main.sym("object_c_80304A70"),
	0x803039FC: main.sym("object_c_80304AE0"),
	#0x80304BA8: main.sym("object_c_80304BA8", flag={"GLOBL"}),
	0x80303B30: main.sym("L80304C14", flag={"GLOBL","LOCAL"}),
	0x80303B40: main.sym("L80304C24", flag={"GLOBL","LOCAL"}),
	0x80303B50: main.sym("L80304C34", flag={"GLOBL","LOCAL"}),
	0x80303B60: main.sym("L80304C44", flag={"GLOBL","LOCAL"}),
	0x80303B70: main.sym("L80304C54", flag={"GLOBL","LOCAL"}),
	0x80303B80: main.sym("L80304C64", flag={"GLOBL","LOCAL"}),
	0x80303B90: main.sym("L80304C74", flag={"GLOBL","LOCAL"}),
	0x80303BA0: main.sym("L80304C84", flag={"GLOBL","LOCAL"}),
	0x80303D44: main.sym("object_c_80304E28"),
	0x80303E90: main.sym("object_c_80304F74"),
	#0x80304FD4: main.sym("object_c_80304FD4", flag={"GLOBL"}),
	0x80303F78: main.sym("object_c_8030505C"),
	0x80303FA8: main.sym("object_c_8030508C"),
	#0x80305100: main.sym("object_c_80305100", flag={"GLOBL"}),
	0x80304148: main.sym("object_c_8030522C"),
	0x803042F8: main.sym("object_c_803053DC"),
	0x80304390: main.sym("object_c_80305474"),
	0x80304788: main.sym("object_c_8030586C"),
	0x803047C0: main.sym("object_c_803058A4"),
	0x80304820: main.sym("object_c_80305904"),
	#0x80305A58: main.sym("object_c_80305A58", flag={"GLOBL"}),
	0x803049AC: main.sym("L80305A90", flag={"GLOBL","LOCAL"}),
	0x803049BC: main.sym("L80305AA0", flag={"GLOBL","LOCAL"}),
	0x803049CC: main.sym("L80305AB0", flag={"GLOBL","LOCAL"}),
	0x803049DC: main.sym("L80305AC0", flag={"GLOBL","LOCAL"}),
	0x803049EC: main.sym("L80305AD0", flag={"GLOBL","LOCAL"}),
	#0x80305BB0: main.sym("object_c_80305BB0", flag={"GLOBL"}),
	#0x80305C14: main.sym("object_c_80305C14", flag={"GLOBL"}),
	#0x80305C90: main.sym("object_c_80305C90", flag={"GLOBL"}),
	#0x80305E2C: main.sym("object_c_80305E2C", flag={"GLOBL"}),
	#0x80305F24: main.sym("object_c_80305F24", flag={"GLOBL"}),
	#0x80306084: main.sym("object_c_80306084", flag={"GLOBL"}),
	0x803051C4: main.sym("object_c_803062A8"),
	0x80305220: main.sym("object_c_80306304"),
	0x80305280: main.sym("object_c_80306364"),
	0x803055A8: main.sym("object_c_8030668C"),
	0x803055F4: main.sym("object_c_803066D8"),
	#0x803067E8: main.sym("object_c_803067E8", flag={"GLOBL"}),
	#0x803068C0: main.sym("object_c_803068C0", flag={"GLOBL"}),
	#0x8030699C: main.sym("object_c_8030699C", flag={"GLOBL"}),
	#0x80306A38: main.sym("object_c_80306A38", flag={"GLOBL"}),
	#0x80306CC4: main.sym("object_c_80306CC4", flag={"GLOBL"}),
	#0x80306D38: main.sym("object_c_80306D38", flag={"GLOBL"}),
	#0x80306F48: main.sym("object_c_80306F48", flag={"GLOBL"}),
	#0x80307010: main.sym("object_c_80307010", flag={"GLOBL"}),
	#0x803071B8: main.sym("object_c_803071B8", flag={"GLOBL"}),
	0x8030615C: main.sym("object_c_80307240"),
	0x80306264: main.sym("object_c_80307348"),
	0x80306314: main.sym("object_c_803073F8"),
	0x80306350: main.sym("object_c_80307434"),
	0x80306514: main.sym("object_c_803075F8"),
	#0x80307670: main.sym("object_c_80307670", flag={"GLOBL"}),
	#0x80307760: main.sym("object_c_80307760", flag={"GLOBL"}),
	#0x803077E0: main.sym("object_c_803077E0", flag={"GLOBL"}),
	#0x80307930: main.sym("object_c_80307930", flag={"GLOBL"}),
	#0x803079C8: main.sym("object_c_803079C8", flag={"GLOBL"}),
	#0x80307AE4: main.sym("object_c_80307AE4", flag={"GLOBL"}),
	#0x80307B58: main.sym("object_c_80307B58", flag={"GLOBL"}),
	#0x80307C88: main.sym("object_c_80307C88", flag={"GLOBL"}),
	#0x80307CF8: main.sym("object_c_80307CF8", flag={"GLOBL"}),
	#0x80307EA4: main.sym("object_c_80307EA4", flag={"GLOBL"}),
	0x80306ED4: main.sym("object_c_80307FB8"),
	#0x8030803C: main.sym("object_c_8030803C", flag={"GLOBL"}),
	0x8030702C: main.sym("object_c_80308110"),
	0x80307144: main.sym("object_c_80308228"),
	0x80307208: main.sym("object_c_803082EC"),
	0x80307370: main.sym("object_c_80308454"),
	0x80307650: main.sym("object_c_80308734"),
	0x80307990: main.sym("object_c_80308A74"),
	0x80307A0C: main.sym("object_c_80308AF0"),
	0x80307AD4: main.sym("object_c_80308BB8"),
	#0x80308D6C: main.sym("object_c_80308D6C", flag={"GLOBL"}),
	0x80307CCC: main.sym("L80308DB0", flag={"GLOBL","LOCAL"}),
	0x80307CDC: main.sym("L80308DC0", flag={"GLOBL","LOCAL"}),
	0x80307CEC: main.sym("L80308DD0", flag={"GLOBL","LOCAL"}),
	0x80307CFC: main.sym("L80308DE0", flag={"GLOBL","LOCAL"}),
	0x80307D0C: main.sym("L80308DF0", flag={"GLOBL","LOCAL"}),
	0x80307D1C: main.sym("L80308E00", flag={"GLOBL","LOCAL"}),
	0x80307D2C: main.sym("L80308E10", flag={"GLOBL","LOCAL"}),
	0x80307D3C: main.sym("L80308E20", flag={"GLOBL","LOCAL"}),
	0x80307E24: main.sym("object_c_80308F08"),
	0x80307EB0: main.sym("object_c_80308F94"),
	0x80307FD4: main.sym("object_c_803090B8"),
	#0x80309154: main.sym("object_c_80309154", flag={"GLOBL"}),
	#0x803091E0: main.sym("object_c_803091E0", flag={"GLOBL"}),
	#0x80309354: main.sym("object_c_80309354", flag={"GLOBL"}),
	#0x80309454: main.sym("object_c_80309454", flag={"GLOBL"}),
	#0x803094D0: main.sym("object_c_803094D0", flag={"GLOBL"}),
	#0x803094F8: main.sym("object_c_803094F8", flag={"GLOBL"}),
	#0x80309530: main.sym("object_c_80309530", flag={"GLOBL"}),
	#0x803097A4: main.sym("object_c_803097A4", flag={"GLOBL"}),
	#0x803098C0: main.sym("object_c_803098C0", flag={"GLOBL"}),
	#0x80309B64: main.sym("object_c_80309B64", flag={"GLOBL"}),
	#0x80309CEC: main.sym("object_c_80309CEC", flag={"GLOBL"}),
	0x80308DF0: main.sym("object_c_80309ED4"),
	0x80308E84: main.sym("object_c_80309F68"),
	0x80309004: main.sym("object_c_8030A0E8"),
	#0x8030A11C: main.sym("object_c_8030A11C", flag={"GLOBL"}),
	#0x8030A1C0: main.sym("object_c_8030A1C0", flag={"GLOBL"}),
	0x803091C4: main.sym("object_c_8030A2A8"),
	0x803092AC: main.sym("object_c_8030A390"),
	0x80309430: main.sym("object_c_8030A514"),
	0x80309530: main.sym("object_c_8030A614"),
	#0x8030A93C: main.sym("object_c_8030A93C", flag={"GLOBL"}),
	0x80309970: main.sym("L8030AA54", flag={"GLOBL","LOCAL"}),
	0x80309980: main.sym("L8030AA64", flag={"GLOBL","LOCAL"}),
	0x80309998: main.sym("L8030AA7C", flag={"GLOBL","LOCAL"}),
	0x803099A0: main.sym("L8030AA84", flag={"GLOBL","LOCAL"}),
	0x803099B0: main.sym("L8030AA94", flag={"GLOBL","LOCAL"}),
	#0x8030AABC: main.sym("object_c_8030AABC", flag={"GLOBL"}),
	0x80309C20: main.sym("object_c_8030AD04"),
	0x80309DB8: main.sym("object_c_8030AE9C"),
	0x80309FD4: main.sym("object_c_8030B0B8"),
	0x8030A00C: main.sym("object_c_8030B0F0"),
	0x8030A120: main.sym("object_c_8030B220"),
	#0x8030B2F4: main.sym("object_c_8030B2F4", flag={"GLOBL"}),
	#0x8030B658: main.sym("object_c_8030B658", flag={"GLOBL"}),
	0x8030A5D8: main.sym("object_c_8030B6D8"),
	0x8030A968: main.sym("object_c_8030BA68"),
	#0x8030BC90: main.sym("object_c_8030BC90", flag={"GLOBL"}),
	0x8030AC2C: main.sym("object_c_8030BD2C"),
	0x8030ACF8: main.sym("object_c_8030BDF8"),
	#0x8030BFD0: main.sym("object_c_8030BFD0", flag={"GLOBL"}),
	0x8030AF6C: main.sym("object_c_8030C06C"),
	0x8030AFF0: main.sym("object_c_8030C0F0"),
	0x8030B110: main.sym("object_c_8030C210"),
	0x8030B1C8: main.sym("object_c_8030C2C8"),
	#0x8030C364: main.sym("object_c_8030C364", flag={"GLOBL"}),
	#0x8030C4B0: main.sym("object_c_8030C4B0", flag={"GLOBL"}),
	0x8030B464: main.sym("object_c_8030C564"),
	0x8030B50C: main.sym("object_c_8030C60C"),
	0x8030B5A4: main.sym("object_c_8030C6A4"),
	0x8030B728: main.sym("object_c_8030C828"),
	0x8030B794: main.sym("object_c_8030C894"),
	#0x8030C8EC: main.sym("object_c_8030C8EC", flag={"GLOBL"}),
	0x8030B824: main.sym("L8030C924", flag={"GLOBL","LOCAL"}),
	0x8030B834: main.sym("L8030C934", flag={"GLOBL","LOCAL"}),
	0x8030B844: main.sym("L8030C944", flag={"GLOBL","LOCAL"}),
	0x8030B854: main.sym("L8030C954", flag={"GLOBL","LOCAL"}),
	0x8030B864: main.sym("L8030C964", flag={"GLOBL","LOCAL"}),
	#0x8030C98C: main.sym("object_c_8030C98C", flag={"GLOBL"}),
	0x8030BC30: main.sym("object_c_8030CD30", flag={"GLOBL"}),
	#0x8030CDDC: main.sym("object_c_8030CDDC", flag={"GLOBL"}),
	0x8030BDC0: main.sym("object_c_8030CEC0"),
	0x8030C040: main.sym("object_c_8030D140"),
	#0x8030D2F0: main.sym("object_c_8030D2F0", flag={"GLOBL"}),
	0x8030C32C: main.sym("object_c_8030D42C"),
	0x8030C3D4: main.sym("object_c_8030D4D4"),
	#0x8030D598: main.sym("object_c_8030D598", flag={"GLOBL"}),
	#0x8030D640: main.sym("object_c_8030D640", flag={"GLOBL"}),
	#0x8030D8D4: main.sym("object_c_8030D8D4", flag={"GLOBL"}),
	#0x8030D93C: main.sym("Ctrl_object_c_8030D93C", flag={"GLOBL"}),
	#0x8030D9AC: main.sym("Ctrl_object_c_8030D9AC", flag={"GLOBL"}),
	0x8030C914: main.sym("object_c_8030DA14"),
	0x8030CA38: main.sym("object_c_8030DB38"),
	#0x8030DC70: main.sym("object_c_8030DC70", flag={"GLOBL"}),
	#0x8030DFC4: main.sym("object_c_8030DFC4", flag={"GLOBL"}),
	#0x8030E14C: main.sym("object_c_8030E14C", flag={"GLOBL"}),
	#0x8030E16C: main.sym("object_c_8030E16C", flag={"GLOBL"}),
	0x8030D284: main.sym("object_c_8030E384"),
	0x8030D2E0: main.sym("object_c_8030E3E0"),
	0x8030D388: main.sym("object_c_8030E488"),
	0x8030D42C: main.sym("object_c_8030E52C"),
	0x8030D588: main.sym("object_c_8030E688"),
	0x8030D5D4: main.sym("object_c_8030E6D4"),
	0x8030D8E0: main.sym("object_c_8030E9E0"),
	#0x8030EA9C: main.sym("object_c_8030EA9C", flag={"GLOBL"}),
	0x8030D9D4: main.sym("L8030EAD4", flag={"GLOBL","LOCAL"}),
	0x8030D9E4: main.sym("L8030EAE4", flag={"GLOBL","LOCAL"}),
	0x8030D9F4: main.sym("L8030EAF4", flag={"GLOBL","LOCAL"}),
	0x8030DA04: main.sym("L8030EB04", flag={"GLOBL","LOCAL"}),
	0x8030DA14: main.sym("L8030EB14", flag={"GLOBL","LOCAL"}),
	0x8030DA3C: main.sym("object_c_8030EB3C"),
	0x8030DBA8: main.sym("object_c_8030ECA8"),
	0x8030DBF8: main.sym("object_c_8030ECF8"),
	0x8030DE08: main.sym("object_c_8030EF08"),
	0x8030E018: main.sym("object_c_8030F118"),
	0x8030E11C: main.sym("object_c_8030F21C"),
	0x8030E340: main.sym("object_c_8030F440"),
	0x8030E408: main.sym("object_c_8030F508"),
	0x8030E48C: main.sym("object_c_8030F58C"),
	0x8030E4CC: main.sym("object_c_8030F5CC"),
	0x8030E528: main.sym("object_c_8030F628"),
	0x8030E5BC: main.sym("object_c_8030F6BC"),
	0x8030E740: main.sym("object_c_8030F840"),
	0x8030E8C0: main.sym("object_c_8030F9C0"),
	0x8030EA3C: main.sym("object_c_8030FB3C"),
	0x8030EB34: main.sym("object_c_8030FC34"),
	0x8030EBF4: main.sym("object_c_8030FCF4"),
	0x8030ED38: main.sym("object_c_8030FE38"),
	#0x8030FFF8: main.sym("object_c_8030FFF8", flag={"GLOBL"}),
	0x8030EF78: main.sym("L80310078", flag={"GLOBL","LOCAL"}),
	0x8030EF88: main.sym("L80310088", flag={"GLOBL","LOCAL"}),
	0x8030EF98: main.sym("L80310098", flag={"GLOBL","LOCAL"}),
	0x8030EFA8: main.sym("L803100A8", flag={"GLOBL","LOCAL"}),
	0x8030EFB8: main.sym("L803100B8", flag={"GLOBL","LOCAL"}),
	0x8030EFC8: main.sym("L803100C8", flag={"GLOBL","LOCAL"}),
	0x8030EFD8: main.sym("L803100D8", flag={"GLOBL","LOCAL"}),
	0x8030EFE8: main.sym("L803100E8", flag={"GLOBL","LOCAL"}),
	0x8030EFF8: main.sym("L803100F8", flag={"GLOBL","LOCAL"}),
	0x8030F008: main.sym("L80310108", flag={"GLOBL","LOCAL"}),
	0x8030F018: main.sym("L80310118", flag={"GLOBL","LOCAL"}),
	0x8030F028: main.sym("L80310128", flag={"GLOBL","LOCAL"}),
	0x8030F038: main.sym("L80310138", flag={"GLOBL","LOCAL"}),
	0x8030F048: main.sym("L80310148", flag={"GLOBL","LOCAL"}),
	0x8030F058: main.sym("L80310158", flag={"GLOBL","LOCAL"}),
	0x8030F0DC: main.sym("object_c_803101DC"),
	0x8030F158: main.sym("object_c_80310258"),
	0x8030F218: main.sym("object_c_80310318"),
	#0x80310498: main.sym("object_c_80310498", flag={"GLOBL"}),
	0x8030F44C: main.sym("object_c_8031054C"),
	0x8030F674: main.sym("object_c_80310774"),
	0x8030F87C: main.sym("object_c_8031097C"),
	0x8030F97C: main.sym("object_c_80310A7C"),
	0x8030FA2C: main.sym("object_c_80310B2C"),
	0x8030FB3C: main.sym("object_c_80310C3C"),
	0x8030FE04: main.sym("object_c_80310F04"),
	0x8030FF18: main.sym("object_c_80311018"),
	0x8031001C: main.sym("object_c_8031111C"),
	0x8031016C: main.sym("object_c_8031126C"),
	#0x8031129C: main.sym("object_c_8031129C", flag={"GLOBL"}),
	0x80310258: main.sym("L80311358", flag={"GLOBL","LOCAL"}),
	0x80310278: main.sym("L80311378", flag={"GLOBL","LOCAL"}),
	0x80310290: main.sym("L80311390", flag={"GLOBL","LOCAL"}),
	0x803102A0: main.sym("L803113A0", flag={"GLOBL","LOCAL"}),
	0x803102B0: main.sym("L803113B0", flag={"GLOBL","LOCAL"}),
	0x803102C0: main.sym("L803113C0", flag={"GLOBL","LOCAL"}),
	0x803102D0: main.sym("L803113D0", flag={"GLOBL","LOCAL"}),
	0x803102E0: main.sym("L803113E0", flag={"GLOBL","LOCAL"}),
	0x8031047C: main.sym("object_c_8031157C"),
	0x803105C0: main.sym("object_c_803116C0"),
	#0x80311874: main.sym("object_c_80311874", flag={"GLOBL"}),
	#0x803118E4: main.sym("object_c_803118E4", flag={"GLOBL"}),
	0x80310854: main.sym("object_c_80311954"),
	0x803108E4: main.sym("object_c_803119E4"),
	0x80310A18: main.sym("object_c_80311B18"),
	0x80310A7C: main.sym("object_c_80311B7C"),
	0x80310CD8: main.sym("object_c_80311DD8"),
	0x80310DA4: main.sym("object_c_80311EA4"),
	#0x80312070: main.sym("object_c_80312070", flag={"GLOBL"}),
	0x80310FA4: main.sym("L803120B0", flag={"GLOBL","LOCAL"}),
	0x80310FB4: main.sym("L803120C0", flag={"GLOBL","LOCAL"}),
	0x80310FC4: main.sym("L803120D0", flag={"GLOBL","LOCAL"}),
	0x80310FD4: main.sym("L803120E0", flag={"GLOBL","LOCAL"}),
	0x80310FE4: main.sym("L803120F0", flag={"GLOBL","LOCAL"}),
	0x80310FF4: main.sym("L80312100", flag={"GLOBL","LOCAL"}),
	#0x80312168: main.sym("object_c_80312168", flag={"GLOBL"}),
	#0x80312200: main.sym("object_c_80312200", flag={"GLOBL"}),
	#0x80312248: main.sym("object_c_80312248", flag={"GLOBL"}),
	0x80311264: main.sym("object_c_80312370"),
	0x80311520: main.sym("object_c_8031262C"),
	#0x8031274C: main.sym("object_c_8031274C", flag={"GLOBL"}),
	0x803116F8: main.sym("object_c_80312804"),
	0x803117F4: main.sym("object_c_80312900"),
	#0x80312A54: main.sym("object_c_80312A54", flag={"GLOBL"}),
	0x803119E8: main.sym("object_c_80312AF4"),
	0x80311A74: main.sym("object_c_80312B80"),
	0x80311C00: main.sym("object_c_80312D0C"),
	0x80311D9C: main.sym("object_c_80312EA8"),
	#0x80313110: main.sym("object_c_80313110", flag={"GLOBL"}),
	#0x803131E8: main.sym("object_c_803131E8", flag={"GLOBL"}),
	#0x8031326C: main.sym("object_c_8031326C", flag={"GLOBL"}),
	#0x80313294: main.sym("object_c_80313294", flag={"GLOBL"}),
	#0x80313354: main.sym("object_c_80313354", flag={"GLOBL"}),
	#0x80313530: main.sym("object_c_80313530", flag={"GLOBL"}),
	#0x803136CC: main.sym("object_c_803136CC", flag={"GLOBL"}),
	#0x80313754: main.sym("object_c_80313754", flag={"GLOBL"}),
	#0x803137F4: main.sym("object_c_803137F4", flag={"GLOBL"}),
	0x80312710: main.sym("object_c_8031381C"),
	0x803128E4: main.sym("object_c_803139F0"),
	0x80312AD8: main.sym("object_c_80313BE4"),
	0x80312D10: main.sym("object_c_80313E1C"),
	#0x80313FC0: main.sym("object_c_80313FC0", flag={"GLOBL"}),
	0x80312F8C: main.sym("object_c_80314098"),
	0x80313170: main.sym("object_c_8031427C"),
	#0x803145D4: main.sym("object_c_803145D4", flag={"GLOBL"}),

	# src/audio/driver.c
	0x80313920: main.sym("Na_driver_80314A30"),
	0x80313BB0: main.sym("Na_driver_80314CC0"),
	0x80313CD4: main.sym("Na_driver_80314DE4", flag={"GLOBL"}),
	0x80313E54: main.sym("Na_driver_80314F64"),
	0x80314480: main.sym("Na_driver_80315590"),
	0x80314F08: main.sym("Na_driver_80316010"),
	0x80314FD4: main.sym("Na_driver_803160DC"),
	0x80315030: main.sym("Na_driver_80316138"),
	0x80315094: main.sym("Na_driver_8031619C"),
	0x803155F4: main.sym("Na_driver_803166FC"),
	0x803159C0: main.sym("Na_driver_80316AC8", flag={"GLOBL"}),
	0x803159EC: main.sym("Na_driver_80316AF4", flag={"GLOBL"}),
	0x80315D88: main.sym("Na_driver_80316DA8", flag={"GLOBL"}),
	0x80315D94: main.sym("Na_driver_80316DB4", flag={"GLOBL"}),
	0x80315DE0: main.sym("Na_driver_80316E00", flag={"GLOBL"}),

	# src/audio/memory.c
	0x80315E60: main.sym("Na_memory_80316E80"),
	0x80315EA4: main.sym("Na_memory_80316EC4"),
	0x80315F94: main.sym("Na_memory_80316FB4"),
	0x80316020: main.sym("Na_memory_80317040", flag={"GLOBL"}),
	0x80316094: main.sym("Na_memory_803170B4"),
	0x803160B4: main.sym("Na_memory_803170D4"),
	0x803160C8: main.sym("Na_memory_803170E8"),
	0x803160F8: main.sym("Na_memory_80317118"),
	0x80316108: main.sym("Na_memory_80317128", flag={"GLOBL"}),
	0x80316164: main.sym("Na_memory_80317184"),
	0x803161E0: main.sym("Na_memory_80317200"),
	0x8031625C: main.sym("Na_memory_8031727C"),
	0x80316318: main.sym("Na_memory_80317338"),
	0x803163D4: main.sym("Na_memory_803173F4"),
	0x803163DC: main.sym("Na_memory_803173FC", flag={"GLOBL"}),
	0x8031680C: main.sym("Na_memory_8031782C", flag={"GLOBL"}),
	0x803168CC: main.sym("Na_memory_803178EC"),
	0x803168F4: main.sym("Na_memory_80317914"),
	0x80316928: main.sym("Na_memory_80317948", flag={"GLOBL"}),
	0x80316BD0: main.sym("L80317BF0", flag={"GLOBL","LOCAL"}),
	0x80316BDC: main.sym("L80317BFC", flag={"GLOBL","LOCAL"}),
	0x80316BEC: main.sym("L80317C0C", flag={"GLOBL","LOCAL"}),
	0x80316BFC: main.sym("L80317C1C", flag={"GLOBL","LOCAL"}),
	0x80316C0C: main.sym("L80317C2C", flag={"GLOBL","LOCAL"}),
	0x80316C1C: main.sym("L80317C3C", flag={"GLOBL","LOCAL"}),

	# src/audio/system.c
	0x80316FB0: main.sym("Na_system_80318040"),
	0x80317034: main.sym("Na_system_803180C4"),
	0x803170A0: main.sym("Na_system_80318130", flag={"GLOBL"}),
	0x8031715C: main.sym("Na_system_803181EC", flag={"GLOBL"}),
	0x80317270: main.sym("Na_system_80318300", flag={"GLOBL"}),
	0x8031758C: main.sym("Na_system_80318634", flag={"GLOBL"}),
	0x80317844: main.sym("Na_system_803188EC"),
	0x8031784C: main.sym("Na_system_803188F4", flag={"GLOBL"}),
	0x80317A88: main.sym("Na_system_80318B30"),
	0x80317BE4: main.sym("Na_system_80318C8C"),
	0x80317D1C: main.sym("Na_system_80318DC4"),
	0x80317DC8: main.sym("Na_system_80318E70"),
	0x80317F04: main.sym("Na_system_80318FAC"),
	0x8031804C: main.sym("Na_system_803190F4"),
	0x80318178: main.sym("Na_system_80319220", flag={"GLOBL"}),
	0x80318280: main.sym("Na_system_80319328", flag={"GLOBL"}),
	0x803182E0: main.sym("Na_system_80319388"),
	0x80318464: main.sym("Na_Load", flag={"GLOBL"}),

	# src/audio/voice.c
	0x80318870: main.sym("Na_voice_80319920"),
	0x803188E8: main.sym("Na_voice_80319998"),
	0x80318908: main.sym("Na_voice_803199B8", flag={"GLOBL"}),
	0x80318D18: main.sym("Na_voice_80319DB8"),
	0x80318EC4: main.sym("Na_voice_80319F64", flag={"GLOBL"}),
	0x80318EE4: main.sym("Na_voice_80319F84"),
	0x80318F04: main.sym("Na_voice_80319FA4"),
	0x80319164: main.sym("Na_voice_8031A1D0", flag={"GLOBL"}),
	0x803191E8: main.sym("Na_voice_8031A254"),
	0x803191F8: main.sym("Na_voice_8031A264", flag={"GLOBL"}),
	0x80319248: main.sym("Na_voice_8031A2B4", flag={"GLOBL"}),
	0x803192FC: main.sym("Na_voice_8031A368", flag={"GLOBL"}),
	0x80319428: main.sym("Na_voice_8031A494", flag={"GLOBL"}),
	0x80319564: main.sym("Na_voice_8031A5D0"),
	0x803195A4: main.sym("Na_voice_8031A610", flag={"GLOBL"}),
	0x803195D0: main.sym("Na_voice_8031A63C"),
	0x80319660: main.sym("Na_voice_8031A6CC"),
	0x80319728: main.sym("Na_voice_8031A794"),
	0x8031975C: main.sym("Na_voice_8031A7C8"),
	0x803197B4: main.sym("Na_voice_8031A820"),
	0x80319830: main.sym("Na_voice_8031A89C"),
	0x80319884: main.sym("Na_voice_8031A8F0"),
	0x803198E0: main.sym("Na_voice_8031A94C", flag={"GLOBL"}),
	0x80319BC8: main.sym("Na_voice_8031AC34", flag={"GLOBL"}),
	0x80319D40: main.sym("Na_voice_8031ADAC", flag={"GLOBL"}),

	# src/audio/effect.c
	0x80319E70: main.sym("Na_effect_8031AEE0"),
	0x80319E78: main.sym("Na_effect_8031AEE8", flag={"GLOBL"}),
	0x8031A078: main.sym("Na_effect_8031B0CC"),
	0x8031A17C: main.sym("Na_effect_8031B1C0"),
	0x8031A204: main.sym("Na_effect_8031B248"),
	0x8031A418: main.sym("Na_effect_8031B440", flag={"GLOBL"}),
	0x8031A478: main.sym("Na_effect_8031B4A0", flag={"GLOBL"}),
	0x8031A564: main.sym("Na_effect_8031B58C", flag={"GLOBL"}),
	0x8031A584: main.sym("Na_effect_8031B5AC", flag={"GLOBL"}),
	0x8031A5B0: main.sym("L8031B5D8", flag={"GLOBL","LOCAL"}),
	0x8031A5B8: main.sym("L8031B5E0", flag={"GLOBL","LOCAL"}),
	0x8031A5DC: main.sym("L8031B604", flag={"GLOBL","LOCAL"}),
	0x8031A5F4: main.sym("L8031B61C", flag={"GLOBL","LOCAL"}),
	0x8031A6D8: main.sym("L8031B700", flag={"GLOBL","LOCAL"}),
	0x8031A70C: main.sym("L8031B734", flag={"GLOBL","LOCAL"}),
	0x8031A714: main.sym("L8031B73C", flag={"GLOBL","LOCAL"}),
	0x8031A794: main.sym("L8031B7BC", flag={"GLOBL","LOCAL"}),

	# src/audio/sequence.c
	0x8031A810: main.sym("Na_sequence_8031B830"),
	0x8031A920: main.sym("Na_sequence_8031B940"),
	0x8031AA10: main.sym("Na_sequence_8031BA30", flag={"GLOBL"}),
	0x8031AA4C: main.sym("Na_sequence_8031BA6C"),
	0x8031AAD0: main.sym("Na_sequence_8031BAF0", flag={"GLOBL"}),
	0x8031AB3C: main.sym("Na_sequence_8031BB5C"),
	0x8031AB84: main.sym("Na_sequence_8031BBA4"),
	0x8031ACB0: main.sym("Na_sequence_8031BCD0"),
	0x8031AD80: main.sym("Na_sequence_8031BDA0"),
	0x8031AE24: main.sym("Na_sequence_8031BE44", flag={"GLOBL"}),
	0x8031AEF4: main.sym("Na_sequence_8031BF14", flag={"GLOBL"}),
	0x8031AF34: main.sym("Na_sequence_8031BF54", flag={"GLOBL"}),
	0x8031AF74: main.sym("Na_sequence_8031BF94"),
	0x8031B01C: main.sym("Na_sequence_8031C03C"),
	0x8031B030: main.sym("Na_sequence_8031C050"),
	0x8031B060: main.sym("Na_sequence_8031C080"),
	0x8031B0A4: main.sym("Na_sequence_8031C0C4"),
	0x8031B1E4: main.sym("L8031C200", flag={"GLOBL","LOCAL"}),
	0x8031B220: main.sym("L8031C23C", flag={"GLOBL","LOCAL"}),
	0x8031B27C: main.sym("L8031C298", flag={"GLOBL","LOCAL"}),
	0x8031B2C0: main.sym("L8031C2DC", flag={"GLOBL","LOCAL"}),
	0x8031B30C: main.sym("L8031C328", flag={"GLOBL","LOCAL"}),
	0x8031B350: main.sym("L8031C36C", flag={"GLOBL","LOCAL"}),
	0x8031B3A8: main.sym("L8031C3BC", flag={"GLOBL","LOCAL"}),
	0x8031B3D4: main.sym("L8031C3E8", flag={"GLOBL","LOCAL"}),
	0x8031B444: main.sym("L8031C454", flag={"GLOBL","LOCAL"}),
	0x8031B494: main.sym("L8031C4A4", flag={"GLOBL","LOCAL"}),
	0x8031B5B8: main.sym("L8031C5C8", flag={"GLOBL","LOCAL"}),
	0x8031B688: main.sym("L8031C698", flag={"GLOBL","LOCAL"}),
	0x8031B690: main.sym("L8031C6A0", flag={"GLOBL","LOCAL"}),
	0x8031BBE8: main.sym("L8031CBE0", flag={"GLOBL","LOCAL"}),
	0x8031BBF4: main.sym("L8031CBEC", flag={"GLOBL","LOCAL"}),
	0x8031BEB0: main.sym("Na_sequence_8031CE54"),
	0x8031C030: main.sym("Na_sequence_8031CFD4"),
	0x8031C0C4: main.sym("Na_sequence_8031D068"),
	0x8031C104: main.sym("Na_sequence_8031D08C"),
	0x8031C1CC: main.sym("L8031D144", flag={"GLOBL","LOCAL"}),
	0x8031C280: main.sym("L8031D1F8", flag={"GLOBL","LOCAL"}),
	0x8031C2BC: main.sym("L8031D234", flag={"GLOBL","LOCAL"}),
	0x8031C2F4: main.sym("L8031D26C", flag={"GLOBL","LOCAL"}),
	0x8031C33C: main.sym("L8031D2B4", flag={"GLOBL","LOCAL"}),
	0x8031C34C: main.sym("L8031D2C4", flag={"GLOBL","LOCAL"}),
	0x8031C3A4: main.sym("L8031D31C", flag={"GLOBL","LOCAL"}),
	0x8031C3CC: main.sym("L8031D344", flag={"GLOBL","LOCAL"}),
	0x8031C3DC: main.sym("L8031D354", flag={"GLOBL","LOCAL"}),
	0x8031C3F8: main.sym("L8031D370", flag={"GLOBL","LOCAL"}),
	0x8031C430: main.sym("L8031D3A8", flag={"GLOBL","LOCAL"}),
	0x8031C44C: main.sym("L8031D3C4", flag={"GLOBL","LOCAL"}),
	0x8031C45C: main.sym("L8031D3D4", flag={"GLOBL","LOCAL"}),
	0x8031C46C: main.sym("L8031D3E4", flag={"GLOBL","LOCAL"}),
	0x8031C488: main.sym("L8031D400", flag={"GLOBL","LOCAL"}),
	0x8031C4C0: main.sym("L8031D424", flag={"GLOBL","LOCAL"}),
	0x8031C508: main.sym("L8031D44C", flag={"GLOBL","LOCAL"}),
	0x8031C530: main.sym("L8031D474", flag={"GLOBL","LOCAL"}),
	0x8031C568: main.sym("L8031D498", flag={"GLOBL","LOCAL"}),
	0x8031C5A0: main.sym("L8031D4BC", flag={"GLOBL","LOCAL"}),
	0x8031C5B8: main.sym("L8031D4D4", flag={"GLOBL","LOCAL"}),
	0x8031C5D4: main.sym("L8031D4F0", flag={"GLOBL","LOCAL"}),
	0x8031C5E4: main.sym("L8031D500", flag={"GLOBL","LOCAL"}),
	0x8031C600: main.sym("L8031D51C", flag={"GLOBL","LOCAL"}),
	0x8031C61C: main.sym("L8031D538", flag={"GLOBL","LOCAL"}),
	0x8031C650: main.sym("L8031D56C", flag={"GLOBL","LOCAL"}),
	0x8031C684: main.sym("L8031D5A0", flag={"GLOBL","LOCAL"}),
	0x8031C698: main.sym("L8031D5B4", flag={"GLOBL","LOCAL"}),
	0x8031C6B8: main.sym("L8031D5D4", flag={"GLOBL","LOCAL"}),
	0x8031C6C8: main.sym("L8031D5E4", flag={"GLOBL","LOCAL"}),
	0x8031C724: main.sym("L8031D640", flag={"GLOBL","LOCAL"}),
	0x8031C75C: main.sym("L8031D678", flag={"GLOBL","LOCAL"}),
	0x8031C7A8: main.sym("L8031D6C4", flag={"GLOBL","LOCAL"}),
	0x8031C7B8: main.sym("L8031D6D4", flag={"GLOBL","LOCAL"}),
	0x8031C7D8: main.sym("L8031D6F4", flag={"GLOBL","LOCAL"}),
	0x8031C7FC: main.sym("L8031D718", flag={"GLOBL","LOCAL"}),
	0x8031C80C: main.sym("L8031D728", flag={"GLOBL","LOCAL"}),
	0x8031C820: main.sym("L8031D73C", flag={"GLOBL","LOCAL"}),
	0x8031C89C: main.sym("L8031D7B8", flag={"GLOBL","LOCAL"}),
	0x8031C8CC: main.sym("L8031D7E8", flag={"GLOBL","LOCAL"}),
	0x8031C8DC: main.sym("L8031D7F8", flag={"GLOBL","LOCAL"}),
	0x8031C8F8: main.sym("L8031D814", flag={"GLOBL","LOCAL"}),
	0x8031C914: main.sym("L8031D830", flag={"GLOBL","LOCAL"}),
	0x8031C960: main.sym("L8031D87C", flag={"GLOBL","LOCAL"}),
	0x8031C97C: main.sym("L8031D898", flag={"GLOBL","LOCAL"}),
	0x8031C9DC: main.sym("L8031D8F8", flag={"GLOBL","LOCAL"}),
	0x8031C9E4: main.sym("L8031D900", flag={"GLOBL","LOCAL"}),
	0x8031CA14: main.sym("L8031D930", flag={"GLOBL","LOCAL"}),
	0x8031CA30: main.sym("L8031D94C", flag={"GLOBL","LOCAL"}),
	0x8031CA58: main.sym("L8031D974", flag={"GLOBL","LOCAL"}),
	0x8031CAD4: main.sym("Na_sequence_8031D9EC"),
	0x8031CD54: main.sym("L8031DC6C", flag={"GLOBL","LOCAL"}),
	0x8031CDFC: main.sym("L8031DD14", flag={"GLOBL","LOCAL"}),
	0x8031CE38: main.sym("L8031DD50", flag={"GLOBL","LOCAL"}),
	0x8031CE70: main.sym("L8031DD88", flag={"GLOBL","LOCAL"}),
	0x8031CEB8: main.sym("L8031DDD0", flag={"GLOBL","LOCAL"}),
	0x8031CF18: main.sym("L8031DE30", flag={"GLOBL","LOCAL"}),
	0x8031CF40: main.sym("L8031DE58", flag={"GLOBL","LOCAL"}),
	0x8031CF50: main.sym("L8031DE68", flag={"GLOBL","LOCAL"}),
	0x8031CF54: main.sym("L8031DE6C", flag={"GLOBL","LOCAL"}),
	0x8031CF74: main.sym("L8031DE8C", flag={"GLOBL","LOCAL"}),
	0x8031CFE4: main.sym("L8031DF14", flag={"GLOBL","LOCAL"}),
	0x8031D0E0: main.sym("L8031DFB0", flag={"GLOBL","LOCAL"}),
	0x8031D118: main.sym("L8031DFDC", flag={"GLOBL","LOCAL"}),
	0x8031D134: main.sym("L8031DFF8", flag={"GLOBL","LOCAL"}),
	0x8031D150: main.sym("L8031E014", flag={"GLOBL","LOCAL"}),
	0x8031D180: main.sym("L8031E03C", flag={"GLOBL","LOCAL"}),
	0x8031D190: main.sym("L8031E04C", flag={"GLOBL","LOCAL"}),
	0x8031D1A0: main.sym("L8031E05C", flag={"GLOBL","LOCAL"}),
	0x8031D1D4: main.sym("L8031E090", flag={"GLOBL","LOCAL"}),
	0x8031D1E4: main.sym("L8031E0A0", flag={"GLOBL","LOCAL"}),
	0x8031D1F4: main.sym("L8031E0B0", flag={"GLOBL","LOCAL"}),
	0x8031D204: main.sym("L8031E0C0", flag={"GLOBL","LOCAL"}),
	0x8031D2D8: main.sym("L8031E194", flag={"GLOBL","LOCAL"}),
	0x8031D2E4: main.sym("L8031E1A0", flag={"GLOBL","LOCAL"}),
	0x8031D2EC: main.sym("L8031E1A8", flag={"GLOBL","LOCAL"}),
	0x8031D2F4: main.sym("L8031E1B0", flag={"GLOBL","LOCAL"}),
	0x8031D384: main.sym("Na_sequence_8031E240", flag={"GLOBL"}),
	0x8031D42C: main.sym("Na_sequence_8031E2E8", flag={"GLOBL"}),
	0x8031D4B8: main.sym("Na_sequence_8031E374", flag={"GLOBL"}),

	# src/audio/game.c
	#0x8031E4F0: main.sym("Na_game_8031E4F0"),
	#0x8031E568: main.sym("Na_game_8031E568"),
	0x8031D630: main.sym("Na_game_8031E578"),
	0x8031D690: main.sym("Na_game_8031E5C0"),
	0x8031D6E4: main.sym("Na_game_8031E60C"),
	0x8031D7B0: main.sym("Na_game_8031E6A4"),
	0x8031D838: main.sym("Na_game_8031E710"),
	0x8031D924: main.sym("Na_Main", flag={"GLOBL"}),
	0x8031DC78: main.sym("Na_SePlay", flag={"GLOBL"}),
	0x8031DCA8: main.sym("Na_game_8031EB30"),
	0x8031DF64: main.sym("Na_game_8031EDEC"),
	0x8031DFE8: main.sym("Na_game_8031EE70"),
	0x8031E0E4: main.sym("Na_game_8031EF6C"),
	0x8031E16C: main.sym("Na_game_8031EFF4"),
	0x8031E97C: main.sym("Na_game_8031F810"),
	0x8031EB24: main.sym("Na_game_8031F96C"),
	0x8031EC7C: main.sym("Na_game_8031FB20"),
	0x8031ED70: main.sym("Na_game_8031FBE8"),
	0x8031EEC8: main.sym("Na_game_8031FD7C"),
	0x8031EED0: main.sym("Na_Tick", flag={"GLOBL"}),
	0x8031EEF8: main.sym("Na_game_8031FDAC"),
	0x8031F0B4: main.sym("L8031FF5C", flag={"GLOBL","LOCAL"}),
	0x8031F220: main.sym("L803200B0", flag={"GLOBL","LOCAL"}),
	0x8031F244: main.sym("L803200D4", flag={"GLOBL","LOCAL"}),
	0x8031F2A8: main.sym("L80320138", flag={"GLOBL","LOCAL"}),
	0x8031F3A4: main.sym("L8032026C", flag={"GLOBL","LOCAL"}),
	0x8031F50C: main.sym("L803203BC", flag={"GLOBL","LOCAL"}),
	0x8031F52C: main.sym("L803203DC", flag={"GLOBL","LOCAL"}),
	0x8031F590: main.sym("L80320440", flag={"GLOBL","LOCAL"}),
	0x8031F690: main.sym("Na_game_80320544"),
	0x8031F7CC: main.sym("Na_SeqFadeout", flag={"GLOBL"}),
	0x8031F810: main.sym("Na_game_803206BC", flag={"GLOBL"}),
	0x8031F888: main.sym("Na_game_80320734"),
	0x8031F96C: main.sym("Na_game_8032080C"),
	0x8031FA4C: main.sym("Na_game_803208EC"),
	0x8031FBAC: main.sym("L80320A4C", flag={"GLOBL","LOCAL"}),
	0x8031FBEC: main.sym("L80320A8C", flag={"GLOBL","LOCAL"}),
	0x8031FC2C: main.sym("L80320ACC", flag={"GLOBL","LOCAL"}),
	0x8031FC6C: main.sym("L80320B0C", flag={"GLOBL","LOCAL"}),
	0x8031FCAC: main.sym("L80320B4C", flag={"GLOBL","LOCAL"}),
	0x8031FCEC: main.sym("L80320B8C", flag={"GLOBL","LOCAL"}),
	0x8031FD2C: main.sym("L80320BCC", flag={"GLOBL","LOCAL"}),
	0x8031FD54: main.sym("L80320BF4", flag={"GLOBL","LOCAL"}),
	#0x80320D70: main.sym("Na_game_80320D70"),
	0x8031FFB4: main.sym("Na_SeqMute", flag={"GLOBL"}),
	0x80320040: main.sym("Na_SeqUnmute", flag={"GLOBL"}),
	0x803200E4: main.sym("Na_game_80320F68"),
	0x80320248: main.sym("Na_Pause", flag={"GLOBL"}),
	0x803202A0: main.sym("Na_Init", flag={"GLOBL"}),
	#0x80321398: main.sym("Na_game_80321398"),
	0x803205E8: main.sym("Na_SeStop", flag={"GLOBL"}),
	0x803206F8: main.sym("Na_SeKill", flag={"GLOBL"}),
	0x803207DC: main.sym("Na_game_80321668"),
	0x80320890: main.sym("Na_SeClear", flag={"GLOBL"}),
	0x803208C0: main.sym("Na_PortLock", flag={"GLOBL"}),
	0x8032091C: main.sym("Na_game_803217A8"),
	0x80320980: main.sym("Na_PortUnlock", flag={"GLOBL"}),
	#0x80321864: main.sym("Na_game_80321864"),
	0x80320A4C: main.sym("Na_game_803218D8", flag={"GLOBL"}),
	0x80320A68: main.sym("Na_MessageSound", flag={"GLOBL"}),
	0x80320AE8: main.sym("Na_BgmPlay", flag={"GLOBL"}),
	0x80320CE8: main.sym("Na_BgmStop", flag={"GLOBL"}),
	0x80320E20: main.sym("Na_BgmFadeout", flag={"GLOBL"}),
	0x80320E74: main.sym("Na_game_80321D38", flag={"GLOBL"}),
	0x80320E98: main.sym("Na_BgmGet", flag={"GLOBL"}),
	0x80320ED8: main.sym("Na_game_80321D9C"),
	0x80320F84: main.sym("Na_SeqPush", flag={"GLOBL"}),
	0x80321080: main.sym("Na_SeqPull", flag={"GLOBL"}),
	0x803210D4: main.sym("Na_Fadeout", flag={"GLOBL"}),
	0x803211B0: main.sym("Na_StarCatch", flag={"GLOBL"}),
	0x803211EC: main.sym("Na_PeachMessage", flag={"GLOBL"}),
	0x80321228: main.sym("Na_Solution", flag={"GLOBL"}),
	0x80321264: main.sym("Na_HiScore", flag={"GLOBL"}),
	0x803212A0: main.sym("Na_StarAppear", flag={"GLOBL"}),
	0x803212F0: main.sym("Na_Fanfare", flag={"GLOBL"}),
	0x8032132C: main.sym("Na_ToadMessage", flag={"GLOBL"}),
	0x80321368: main.sym("Na_SetMode", flag={"GLOBL"}),
	0x80321434: main.sym("Na_SetOutput", flag={"GLOBL"}),
	#0x80322348: main.sym("Na_game_80322348"),
	#0x8032235C: main.sym("Na_game_8032235C"),

	0x80321480: main.sym("osSetTime", flag={"GLOBL"}),
	0x803214B0: main.sym("osMapTLB", flag={"GLOBL"}),
	0x80321570: main.sym("osUnmapTLBAll", flag={"GLOBL"}),
	0x803215C0: main.sym("sprintf", flag={"GLOBL"}),
	0x8032162C: main.sym("proutSprintf"),
	0x80321670: main.sym("osCreateMesgQueue", flag={"GLOBL"}),
	0x803216A0: main.sym("osSetEventMesg", flag={"GLOBL"}),
	0x80321710: main.sym("osViSetEvent", flag={"GLOBL"}),
	0x80321780: main.sym("osCreateThread", flag={"GLOBL"}),
	0x803218D0: main.sym("osRecvMesg", flag={"GLOBL"}),
	0x80321A10: main.sym("_VirtualToPhysicalTask"),
	0x80321B2C: main.sym("osSpTaskLoad", flag={"GLOBL"}),
	0x80321C8C: main.sym("osSpTaskStartGo", flag={"GLOBL"}),
	0x80321CD0: main.sym("osSpTaskYield", flag={"GLOBL"}),
	0x80321CF0: main.sym("osSendMesg", flag={"GLOBL"}),
	0x80321E40: main.sym("osSpTaskYielded", flag={"GLOBL"}),
	0x80321EC0: main.sym("osStartThread", flag={"GLOBL"}),
	0x80322010: main.sym("osWritebackDCacheAll", flag={"GLOBL"}),
	0x80322040: main.sym("osCreateViManager", flag={"GLOBL"}),
	0x803221C4: main.sym("viMgrMain"),
	0x803223A0: main.sym("osViSetMode", flag={"GLOBL"}),
	0x80322410: main.sym("osViBlack", flag={"GLOBL"}),
	0x80322480: main.sym("osViSetSpecialFeatures", flag={"GLOBL"}),
	0x80322640: main.sym("osCreatePiManager", flag={"GLOBL"}),
	0x803227C0: main.sym("osSetThreadPri", flag={"GLOBL"}),
	0x803228A0: main.sym("osInitialize", flag={"GLOBL"}),
	0x80322AD0: main.sym("osViSwapBuffer", flag={"GLOBL"}),
	0x80322B20: main.sym("sqrtf", flag={"GLOBL"}),
	0x80322B30: main.sym("osContStartReadData", flag={"GLOBL"}),
	0x80322BF4: main.sym("osContGetReadData", flag={"GLOBL"}),
	0x80322C9C: main.sym("__osPackReadData"),
	0x80322D90: main.sym("osContInit", flag={"GLOBL"}),
	0x80322F8C: main.sym("__osContGetInitData", flag={"GLOBL"}),
	0x8032305C: main.sym("__osPackRequestData", flag={"GLOBL"}),
	0x80323150: main.sym("osEepromProbe", flag={"GLOBL"}),
	0x803231C0: main.sym("__ull_rshift", flag={"GLOBL"}),
	0x803231EC: main.sym("__ull_rem", flag={"GLOBL"}),
	0x80323228: main.sym("__ull_div", flag={"GLOBL"}),
	0x80323264: main.sym("__ll_lshift", flag={"GLOBL"}),
	0x80323290: main.sym("__ll_rem", flag={"GLOBL"}),
	0x803232CC: main.sym("__ll_div", flag={"GLOBL"}),
	0x80323328: main.sym("__ll_mul", flag={"GLOBL"}),
	0x80323358: main.sym("__ull_divremi", flag={"GLOBL"}),
	0x803233B8: main.sym("__ll_mod", flag={"GLOBL"}),
	0x80323454: main.sym("__ll_rshift", flag={"GLOBL"}),
	0x80323480: main.sym("osInvalDCache", flag={"GLOBL"}),
	0x80323530: main.sym("osPiStartDma", flag={"GLOBL"}),
	0x80323640: main.sym("bzero", flag={"GLOBL"}),
	0x80323660: main.sym("blkzero", flag={"LOCAL"}),
	0x8032369C: main.sym("wordzero", flag={"LOCAL"}),
	0x803236BC: main.sym("bytezero", flag={"LOCAL"}),
	0x803236D4: main.sym("zerodone", flag={"LOCAL"}),
	0x803236E0: main.sym("osInvalICache", flag={"GLOBL"}),
	0x80323760: main.sym("osEepromLongRead", flag={"GLOBL"}),
	0x803238A0: main.sym("osEepromLongWrite", flag={"GLOBL"}),
	0x803239E0: main.sym("bcopy", flag={"GLOBL"}),
	0x80323A10: main.sym("goforwards", flag={"LOCAL"}),
	0x80323A14: main.sym("goforwards.L", flag={"LOCAL"}),
	0x80323A2C: main.sym("forwards_bytecopy", flag={"LOCAL"}),
	0x80323A4C: main.sym("ret", flag={"LOCAL"}),
	0x80323A54: main.sym("forwalignable", flag={"LOCAL"}),
	0x80323A84: main.sym("forw_copy2", flag={"LOCAL"}),
	0x80323A88: main.sym("forw_copy2.L", flag={"LOCAL"}),
	0x80323A9C: main.sym("forw_copy3", flag={"LOCAL"}),
	0x80323AB8: main.sym("forwards_32", flag={"LOCAL"}),
	0x80323B14: main.sym("forwards_16", flag={"LOCAL"}),
	0x80323B18: main.sym("forwards_16.L", flag={"LOCAL"}),
	0x80323B50: main.sym("forwards_4", flag={"LOCAL"}),
	0x80323B54: main.sym("forwards_4.L", flag={"LOCAL"}),
	0x80323B74: main.sym("gobackwards", flag={"LOCAL"}),
	0x80323B78: main.sym("gobackwards.L", flag={"LOCAL"}),
	0x80323B94: main.sym("backwards_bytecopy", flag={"LOCAL"}),
	0x80323BC4: main.sym("backalignable", flag={"LOCAL"}),
	0x80323BF4: main.sym("back_copy2", flag={"LOCAL"}),
	0x80323BF8: main.sym("back_copy2.L", flag={"LOCAL"}),
	0x80323C0C: main.sym("back_copy3", flag={"LOCAL"}),
	0x80323C28: main.sym("backwards_32", flag={"LOCAL"}),
	0x80323C84: main.sym("backwards_16", flag={"LOCAL"}),
	0x80323C88: main.sym("backwards_16.L", flag={"LOCAL"}),
	0x80323CC0: main.sym("backwards_4", flag={"LOCAL"}),
	0x80323CC4: main.sym("backwards_4.L", flag={"LOCAL"}),
	0x80323CF0: main.sym("guOrthoF", flag={"GLOBL"}),
	0x80323E44: main.sym("guOrtho", flag={"GLOBL"}),
	0x80323EB0: main.sym("guPerspectiveF", flag={"GLOBL"}),
	0x803240E0: main.sym("guPerspective", flag={"GLOBL"}),
	0x80324140: main.sym("osGetTime", flag={"GLOBL"}),
	0x803241D0: main.sym("__d_to_ll", flag={"GLOBL"}),
	0x803241EC: main.sym("__f_to_ll", flag={"GLOBL"}),
	0x80324208: main.sym("__d_to_ull", flag={"GLOBL"}),
	0x803242A8: main.sym("__f_to_ull", flag={"GLOBL"}),
	0x80324344: main.sym("__ll_to_d", flag={"GLOBL"}),
	0x8032435C: main.sym("__ll_to_f", flag={"GLOBL"}),
	0x80324374: main.sym("__ull_to_d", flag={"GLOBL"}),
	0x803243A8: main.sym("__ull_to_f", flag={"GLOBL"}),
	0x803243E0: main.sym("cosf", flag={"GLOBL"}),
	0x80324550: main.sym("sinf", flag={"GLOBL"}),
	0x80324710: main.sym("guTranslateF", flag={"GLOBL"}),
	0x80324758: main.sym("guTranslate", flag={"GLOBL"}),
	0x803247B0: main.sym("guRotateF", flag={"GLOBL"}),
	0x80324944: main.sym("guRotate", flag={"GLOBL"}),
	0x803249A0: main.sym("guScaleF", flag={"GLOBL"}),
	0x803249F4: main.sym("guScale", flag={"GLOBL"}),
	0x80324A40: main.sym("osAiSetFrequency", flag={"GLOBL"}),
	0x80324BA0: main.sym("_bnkfPatchWaveTable"),
	0x80324BA8: main.sym("_bnkfPatchSound"),
	0x80324BB0: main.sym("_bnkfPatchInst"),
	0x80324C9C: main.sym("_bnkfPatchBank"),
	0x80324CA4: main.sym("alBnkfNew", flag={"GLOBL"}),
	0x80324DA8: main.sym("alSeqFileNew", flag={"GLOBL"}),
	0x80324DF0: main.sym("osWritebackDCache", flag={"GLOBL"}),
	0x80324E70: main.sym("osAiGetLength", flag={"GLOBL"}),
	0x80324E80: main.sym("osAiSetNextBuffer", flag={"GLOBL"}),
	0x80324F30: main.sym("__osTimerServicesInit", flag={"GLOBL"}),
	0x80324FBC: main.sym("__osTimerInterrupt", flag={"GLOBL"}),
	0x80325134: main.sym("__osSetTimerIntr", flag={"GLOBL"}),
	0x803251A8: main.sym("__osInsertTimer", flag={"GLOBL"}),
	0x80325330: main.sym("_Printf", flag={"GLOBL"}),
	0x80325B5C: main.sym("_Putfld"),
	0x80325C10: main.sym("L80326B40", flag={"GLOBL","LOCAL"}),
	0x80325C60: main.sym("L80326B90", flag={"GLOBL","LOCAL"}),
	0x80325E60: main.sym("L80326D90", flag={"GLOBL","LOCAL"}),
	0x80326044: main.sym("L80326F74", flag={"GLOBL","LOCAL"}),
	0x8032624C: main.sym("L8032717C", flag={"GLOBL","LOCAL"}),
	0x80326374: main.sym("L803272A4", flag={"GLOBL","LOCAL"}),
	0x803263D8: main.sym("L80327308", flag={"GLOBL","LOCAL"}),
	0x80326470: main.sym("L803273A0", flag={"GLOBL","LOCAL"}),
	0x803264C0: main.sym("memcpy", flag={"GLOBL"}),
	0x803264EC: main.sym("strlen", flag={"GLOBL"}),
	0x80326514: main.sym("strchr", flag={"GLOBL"}),
	0x80326560: main.sym("__osDequeueThread", flag={"GLOBL"}),
	0x803265A0: main.sym("__osDisableInt", flag={"GLOBL"}),
	0x803265C0: main.sym("__osRestoreInt", flag={"GLOBL"}),
	0x803265E0: main.sym("__osViInit", flag={"GLOBL"}),
	0x803266C0: main.sym("__osExceptionPreamble", flag={"GLOBL"}),
	0x803266D0: main.sym("__osException", flag={"GLOBL"}),
	0x80326734: main.sym("notIP7", flag={"LOCAL"}),
	0x80326750: main.sym("savecontext", flag={"LOCAL"}),
	0x803268B4: main.sym("no_kdebug", flag={"LOCAL"}),
	0x80326900: main.sym("no_rdb_mesg", flag={"LOCAL"}),
	0x80326928: main.sym("handle_interrupt"),
	0x8032692C: main.sym("next_interrupt", flag={"LOCAL"}),
	0x80326964: main.sym("counter"),
	0x80326984: main.sym("cart"),
	0x803269B8: main.sym("rcp"),
	0x80326A08: main.sym("sp_other_break", flag={"LOCAL"}),
	0x80326A18: main.sym("vi", flag={"LOCAL"}),
	0x80326A3C: main.sym("ai", flag={"LOCAL"}),
	0x80326A68: main.sym("si", flag={"LOCAL"}),
	0x80326A8C: main.sym("pi", flag={"LOCAL"}),
	0x80326AB8: main.sym("dp", flag={"LOCAL"}),
	0x80326ADC: main.sym("NoMoreRcpInts", flag={"LOCAL"}),
	0x80326AE8: main.sym("prenmi"),
	0x80326B14: main.sym("firstnmi", flag={"LOCAL"}),
	0x80326B44: main.sym("sw2"),
	0x80326B64: main.sym("sw1"),
	0x80326B84: main.sym("handle_break"),
	0x80326B9C: main.sym("redispatch"),
	0x80326BD0: main.sym("enqueueRunning", flag={"LOCAL"}),
	0x80326BE8: main.sym("panic"),
	0x80326C18: main.sym("send_mesg", flag={"GLOBL"}),
	0x80326CC4: main.sym("send_done", flag={"LOCAL"}),
	0x80326CCC: main.sym("handle_CpU", flag={"GLOBL"}),
	0x80326D00: main.sym("__osEnqueueAndYield", flag={"GLOBL"}),
	0x80326D88: main.sym("noEnqueue", flag={"LOCAL"}),
	0x80326D90: main.sym("__osEnqueueThread", flag={"GLOBL"}),
	0x80326DD8: main.sym("__osPopThread", flag={"GLOBL"}),
	0x80326DE8: main.sym("__osDispatchThread", flag={"GLOBL"}),
	0x80326E08: main.sym("__osDispatchThreadSave", flag={"LOCAL"}),
	0x80326F28: main.sym("__osCleanupThread", flag={"GLOBL"}),
	0x80326F30: main.sym("osVirtualToPhysical", flag={"GLOBL"}),
	0x80326FB0: main.sym("__osSpSetStatus", flag={"GLOBL"}),
	0x80326FC0: main.sym("__osSpSetPc", flag={"GLOBL"}),
	0x80327000: main.sym("__osSpRawStartDma", flag={"GLOBL"}),
	0x80327090: main.sym("__osSpDeviceBusy", flag={"GLOBL"}),
	0x803270C0: main.sym("__osSpGetStatus", flag={"GLOBL"}),
	0x803270D0: main.sym("osGetThreadPri", flag={"GLOBL"}),
	0x803270F0: main.sym("__osViGetCurrentContext", flag={"GLOBL"}),
	0x80327100: main.sym("__osViSwapContext", flag={"GLOBL"}),
	0x80327460: main.sym("osGetCount", flag={"GLOBL"}),
	0x80327470: main.sym("__osPiCreateAccessQueue", flag={"GLOBL"}),
	0x803274C0: main.sym("__osPiGetAccess", flag={"GLOBL"}),
	0x80327504: main.sym("__osPiRelAccess", flag={"GLOBL"}),
	0x80327530: main.sym("osPiRawStartDma", flag={"GLOBL"}),
	0x80327610: main.sym("__osDevMgrMain", flag={"GLOBL"}),
	0x80327790: main.sym("__osSetSR", flag={"GLOBL"}),
	0x803277A0: main.sym("__osGetSR", flag={"GLOBL"}),
	0x803277B0: main.sym("__osSetFpcCsr", flag={"GLOBL"}),
	0x803277C0: main.sym("__osSiRawReadIo", flag={"GLOBL"}),
	0x80327810: main.sym("__osSiRawWriteIo", flag={"GLOBL"}),
	0x80327860: main.sym("osMapTLBRdb", flag={"GLOBL"}),
	0x803278C0: main.sym("osPiRawReadIo", flag={"GLOBL"}),
	0x80327960: main.sym("__osSiCreateAccessQueue", flag={"GLOBL"}),
	0x803279B0: main.sym("__osSiGetAccess", flag={"GLOBL"}),
	0x803279F4: main.sym("__osSiRelAccess", flag={"GLOBL"}),
	0x80327A20: main.sym("__osSiRawStartDma", flag={"GLOBL"}),
	0x80327AD0: main.sym("osSetTimer", flag={"GLOBL"}),
	0x80327BB0: main.sym("osEepromWrite", flag={"GLOBL"}),
	0x80327D60: main.sym("__osPackEepWriteData"),
	0x80327E6C: main.sym("__osEepStatus", flag={"GLOBL"}),
	0x80328090: main.sym("osJamMesg", flag={"GLOBL"}),
	0x803281E0: main.sym("osPiGetCmdQueue", flag={"GLOBL"}),
	0x80328210: main.sym("osEepromRead", flag={"GLOBL"}),
	0x80328400: main.sym("__osPackEepReadData"),
	0x80328510: main.sym("guMtxF2L", flag={"GLOBL"}),
	0x80328610: main.sym("guMtxIdentF", flag={"GLOBL"}),
	0x80328698: main.sym("guMtxIdent", flag={"GLOBL"}),
	0x803286C8: main.sym("guMtxL2F", flag={"GLOBL"}),
	0x80328780: main.sym("guNormalize", flag={"GLOBL"}),
	0x80328810: main.sym("__osAiDeviceBusy", flag={"GLOBL"}),
	0x80328840: main.sym("__osSetCompare", flag={"GLOBL"}),
	0x80328850: main.sym("_Litob", flag={"GLOBL"}),
	0x80328B50: main.sym("_Ldtob", flag={"GLOBL"}),
	0x80329150: main.sym("_Ldunscale"),
	0x80329230: main.sym("_Genld"),
	0x80329920: main.sym("u32_to_string"),
	0x80329950: main.sym("string_to_u32"),
	0x803299A8: main.sym("send_packet"),
	0x80329A68: main.sym("send"),
	0x80329B40: main.sym("process_command_memory"),
	0x80329B8C: main.sym("process_command_register"),
	0x80329BB8: main.sym("kdebugserver", flag={"GLOBL"}),
	0x80329DA0: main.sym("__osSyncPutChars", flag={"GLOBL"}),
	0x80329ED0: main.sym("osSetIntMask", flag={"GLOBL"}),
	0x80329F30: main.sym("osDestroyThread", flag={"GLOBL"}),
	0x8032A030: main.sym("__osProbeTLB", flag={"GLOBL"}),
	0x8032A0F0: main.sym("__osSiDeviceBusy", flag={"GLOBL"}),
	0x8032A120: main.sym("lldiv", flag={"GLOBL"}),
	0x8032A220: main.sym("ldiv", flag={"GLOBL"}),
	0x8032A2B0: main.sym("__osGetCause", flag={"GLOBL"}),
	0x8032A2C0: main.sym("__osAtomicDec", flag={"GLOBL"}),

	# ==========================================================================
	# data
	# ==========================================================================

	0x8032C6B8: main.sym("demo_rec+0x00"),
	0x8032C6B9: main.sym("demo_rec+0x01"),
	0x8032C6BA: main.sym("demo_rec+0x02"),
	0x8032C6BB: main.sym("demo_rec+0x03"),

	0x8032C9F0: main.sym("collisiontab+0x00"),
	0x8032C9F4: main.sym("collisiontab+0x04"),

	0x8032CB7B: main.sym("pl_unpresstab+1*15"),
	0x8032CB80: main.sym("pl_flash_pattern+0"),
	0x8032CB84: main.sym("pl_flash_pattern+4"),

	0x8032CC82: main.sym("pldemo_8032DC3C-1*90"),
	0x8032CCD6: main.sym("pldemo_8032DC34+2"),
	0x8032CCDA: main.sym("pldemo_8032DC38+2"),

	0x8032CE37: main.sym("coursetab-1"),

	#0x8032F4D4: main.sym("camdemo_8032F4D4+0x00"),
	#0x8032F4D8: main.sym("camdemo_8032F4D4+0x04"),
	#0x8032F534: main.sym("camdemo_8032F534+0x00"),
	#0x8032F538: main.sym("camdemo_8032F534+0x04"),
	#0x8032F544: main.sym("camdemo_8032F544+0x00"),
	#0x8032F548: main.sym("camdemo_8032F544+0x04"),
	#0x8032F554: main.sym("camdemo_8032F554+0x00"),
	#0x8032F558: main.sym("camdemo_8032F554+0x04"),
	#0x8032F564: main.sym("camdemo_8032F564+0x00"),
	#0x8032F568: main.sym("camdemo_8032F564+0x04"),
	#0x8032F56C: main.sym("camdemo_8032F56C+0x00"),
	#0x8032F570: main.sym("camdemo_8032F56C+0x04"),
	#0x8032F574: main.sym("camdemo_8032F574+0x00"),
	#0x8032F578: main.sym("camdemo_8032F574+0x04"),
	#0x8032F59C: main.sym("camdemo_8032F59C+0x00"),
	#0x8032F5A0: main.sym("camdemo_8032F59C+0x04"),
	#0x8032F5C4: main.sym("camdemo_8032F5C4+0x00"),
	#0x8032F5C8: main.sym("camdemo_8032F5C4+0x04"),
	#0x8032F5DC: main.sym("camdemo_8032F5DC+0x00"),
	#0x8032F5E0: main.sym("camdemo_8032F5DC+0x04"),
	#0x8032F5F4: main.sym("camdemo_8032F5F4+0x00"),
	#0x8032F5F8: main.sym("camdemo_8032F5F4+0x04"),
	#0x8032F60C: main.sym("camdemo_8032F60C+0x00"),
	#0x8032F610: main.sym("camdemo_8032F60C+0x04"),
	#0x8032F624: main.sym("camdemo_8032F624+0x00"),
	#0x8032F628: main.sym("camdemo_8032F624+0x04"),
	#0x8032F634: main.sym("camdemo_8032F634+0x00"),
	#0x8032F638: main.sym("camdemo_8032F634+0x04"),
	#0x8032F63C: main.sym("camdemo_8032F63C+0x00"),
	#0x8032F640: main.sym("camdemo_8032F63C+0x04"),
	#0x8032F64C: main.sym("camdemo_8032F64C+0x00"),
	#0x8032F650: main.sym("camdemo_8032F64C+0x04"),
	#0x8032F65C: main.sym("camdemo_8032F65C+0x00"),
	#0x8032F660: main.sym("camdemo_8032F65C+0x04"),
	#0x8032F674: main.sym("camdemo_8032F674+0x00"),
	#0x8032F678: main.sym("camdemo_8032F674+0x04"),
	#0x8032F69C: main.sym("camdemo_8032F69C+0x00"),
	#0x8032F6A0: main.sym("camdemo_8032F69C+0x04"),
	#0x8032F6AC: main.sym("camdemo_8032F6AC+0x00"),
	#0x8032F6B0: main.sym("camdemo_8032F6AC+0x04"),
	#0x8032F6BC: main.sym("camdemo_8032F6BC+0x00"),
	#0x8032F6C0: main.sym("camdemo_8032F6BC+0x04"),
	#0x8032F6CC: main.sym("camdemo_8032F6CC+0x00"),
	#0x8032F6D0: main.sym("camdemo_8032F6CC+0x04"),
	#0x8032F6DC: main.sym("camdemo_8032F6DC+0x00"),
	#0x8032F6E0: main.sym("camdemo_8032F6DC+0x04"),
	#0x8032F6F4: main.sym("camdemo_8032F6F4+0x00"),
	#0x8032F6F8: main.sym("camdemo_8032F6F4+0x04"),
	#0x8032F6FC: main.sym("camdemo_8032F6FC+0x00"),
	#0x8032F700: main.sym("camdemo_8032F6FC+0x04"),
	#0x8032F70C: main.sym("camdemo_8032F70C+0x00"),
	#0x8032F710: main.sym("camdemo_8032F70C+0x04"),
	#0x8032F714: main.sym("camdemo_8032F714+0x00"),
	#0x8032F718: main.sym("camdemo_8032F714+0x04"),
	#0x8032F71C: main.sym("camdemo_8032F71C+0x00"),
	#0x8032F720: main.sym("camdemo_8032F71C+0x04"),
	#0x8032F72C: main.sym("camdemo_8032F72C+0x00"),
	#0x8032F730: main.sym("camdemo_8032F72C+0x04"),
	#0x8032F734: main.sym("camdemo_8032F734+0x00"),
	#0x8032F738: main.sym("camdemo_8032F734+0x04"),
	#0x8032F74C: main.sym("camdemo_8032F74C+0x00"),
	#0x8032F750: main.sym("camdemo_8032F74C+0x04"),
	#0x8032F754: main.sym("camdemo_8032F754+0x00"),
	#0x8032F758: main.sym("camdemo_8032F754+0x04"),
	#0x8032F75C: main.sym("camdemo_8032F75C+0x00"),
	#0x8032F760: main.sym("camdemo_8032F75C+0x04"),
	#0x8032F764: main.sym("camdemo_8032F764+0x00"),
	#0x8032F768: main.sym("camdemo_8032F764+0x04"),
	#0x8032F76C: main.sym("camdemo_8032F76C+0x00"),
	#0x8032F770: main.sym("camdemo_8032F76C+0x04"),
	#0x8032F774: main.sym("camdemo_8032F774+0x00"),
	#0x8032F778: main.sym("camdemo_8032F774+0x04"),
	#0x8032F784: main.sym("camdemo_8032F784+0x00"),
	#0x8032F788: main.sym("camdemo_8032F784+0x04"),
	#0x8032F794: main.sym("camdemo_8032F794+0x00"),
	#0x8032F798: main.sym("camdemo_8032F794+0x04"),
	#0x8032F7A4: main.sym("camdemo_8032F7A4+0x00"),
	#0x8032F7A8: main.sym("camdemo_8032F7A4+0x04"),
	#0x8032F7B4: main.sym("camdemo_8032F7B4+0x00"),
	#0x8032F7B8: main.sym("camdemo_8032F7B4+0x04"),
	#0x8032F7C4: main.sym("camdemo_8032F7C4+0x00"),
	#0x8032F7C8: main.sym("camdemo_8032F7C4+0x04"),
	#0x8032F7D4: main.sym("camdemo_8032F7D4+0x00"),
	#0x8032F7D8: main.sym("camdemo_8032F7D4+0x04"),
	#0x8032F7EC: main.sym("camdemo_8032F7EC+0x00"),
	#0x8032F7F0: main.sym("camdemo_8032F7EC+0x04"),

	#0x803301AA: main.sym("object_a_803301A8+0x02"),
	#0x803301AC: main.sym("object_a_803301A8+0x04"),
	#0x803301B0: main.sym("object_a_803301A8+0x08"),
	#0x803301D0: main.sym("object_a_803301D0+0x00"),
	#0x803301D1: main.sym("object_a_803301D0+0x01"),
	#0x803301D3: main.sym("object_a_803301D0+0x03"),
	#0x803301DC: main.sym("object_a_803301D0+0x0C"),
	#0x803301E0: main.sym("object_a_803301D0+0x10"),
	#0x80330204: main.sym("object_a_80330204+2*0"),
	#0x80330206: main.sym("object_a_80330204+2*1"),
	#0x8033022C: main.sym("object_a_8033022C+2*0"),
	#0x8033022E: main.sym("object_a_8033022C+2*1"),
	#0x80330244: main.sym("object_a_80330244+2*0"),
	#0x80330246: main.sym("object_a_80330244+2*1"),
	#0x80330260: main.sym("object_a_80330260+4*0"),
	#0x80330264: main.sym("object_a_80330260+4*1"),
	#0x803302AC: main.sym("object_a_803302AC+0x00"),
	#0x803302B2: main.sym("object_a_803302AC+0x06"),
	#0x803302B4: main.sym("object_a_803302AC+0x08"),
	#0x803302EC: main.sym("object_a_803302EC+2*0"),
	#0x803302EE: main.sym("object_a_803302EC+2*1"),
	#0x803302F0: main.sym("object_a_803302EC+2*2"),
	#0x803303C0: main.sym("object_a_803303C0+2*0"),
	#0x803303C2: main.sym("object_a_803303C0+2*1"),
	#0x8033047E: main.sym("object_a_80330480+2*(3*-1+2)"),
	#0x80330480: main.sym("object_a_80330480+2*0"),
	#0x80330482: main.sym("object_a_80330480+2*1"),
	#0x80330484: main.sym("object_a_80330480+2*2"),
	#0x803305F8: main.sym("object_a_803305F8+0x00"),
	#0x803305FC: main.sym("object_a_803305F8+0x04"),
	#0x803305FE: main.sym("object_a_803305F8+0x06"),
	#0x80330600: main.sym("object_a_803305F8+0x08"),
	#0x803306B4: main.sym("object_a_803306B4+0x00"),
	#0x803306C4: main.sym("object_a_803306B4+0x10"),
	#0x80330C48: main.sym("object_a_80330C48+0x00"),
	#0x80330C4C: main.sym("object_a_80330C48+0x04"),
	#0x80330DAC: main.sym("object_a_80330DAC+0x00"),
	#0x80330DB4: main.sym("object_a_80330DAC+0x08"),

	0x8032FF80: main.sym("shadow_rect_table+0x00"),
	0x8032FF84: main.sym("shadow_rect_table+0x04"),
	0x8032FF88: main.sym("shadow_rect_table+0x08"),

	0x80330004: main.sym("fluidtab+0x00"),
	0x80330010: main.sym("fluidtab+0x0C"),
	0x80330024: main.sym("fluidtab+0x20"),

	0x80330244: main.sym("fluidtabL+0x00"),
	0x80330250: main.sym("fluidtabL+0x0C"),
	0x80330264: main.sym("fluidtabL+0x20"),

	0x8033031C: main.sym("fluidtabS+0x00"),
	0x80330328: main.sym("fluidtabS+0x0C"),
	0x8033033C: main.sym("fluidtabS+0x20"),

	0x803306D0: main.sym("tagobjtab+0x00"),
	0x803306D4: main.sym("tagobjtab+0x04"),
	0x803306D6: main.sym("tagobjtab+0x06"),

	0x80331240: main.sym("mapobjtab+0x00"),
	0x80331241: main.sym("mapobjtab+0x01"),
	0x80331242: main.sym("mapobjtab+0x02"),
	0x80331243: main.sym("mapobjtab+0x03"),
	0x80331244: main.sym("mapobjtab+0x04"),

	0x803314E0: main.sym("meter+0x00"),
	0x803314E2: main.sym("meter+0x02"),
	0x803314E4: main.sym("meter+0x04"),

	#0x8033282C: main.sym("object_b_8033282C+2*0"),
	#0x8033282E: main.sym("object_b_8033282C+2*1"),

	#0x80332860: main.sym("object_c_80332860+0x00"),
	#0x80332862: main.sym("object_c_80332860+0x02"),
	#0x80332864: main.sym("object_c_80332860+0x04"),
	#0x803328D0: main.sym("object_c_803328D0+0x00"),
	#0x803328D4: main.sym("object_c_803328D0+0x04"),
	#0x803328D8: main.sym("object_c_803328D0+0x08"),
	#0x803328DA: main.sym("object_c_803328D0+0x0A"),
	#0x80332934: main.sym("object_c_80332938+4*-1"),
	#0x80332984: main.sym("object_c_80332984+0x00"),
	#0x80332987: main.sym("object_c_80332984+0x03"),
	#0x8033298A: main.sym("object_c_80332984+0x06"),
	#0x80332A20: main.sym("object_c_80332A20+0x00"),
	#0x80332A24: main.sym("object_c_80332A20+0x04"),
	#0x80332A28: main.sym("object_c_80332A20+0x08"),
	#0x80332A48: main.sym("object_c_80332A48+0x00"),
	#0x80332A4B: main.sym("object_c_80332A48+0x03"),
	#0x80332A4D: main.sym("object_c_80332A48+0x05"),
	#0x80332A4E: main.sym("object_c_80332A48+0x06"),
	#0x80332AC0: main.sym("object_c_80332AC0+2*0"),
	#0x80332AC2: main.sym("object_c_80332AC0+2*1"),
	#0x80332B10: main.sym("object_c_80332B10+0x00"),
	#0x80332B11: main.sym("object_c_80332B10+0x01"),
	#0x80332B13: main.sym("object_c_80332B10+0x03"),
	#0x80332B14: main.sym("object_c_80332B10+0x04"),
	#0x80332B16: main.sym("object_c_80332B10+0x06"),
	#0x80332B1C: main.sym("object_c_80332B10+0x0C"),
	#0x80332B64: main.sym("object_c_80332B64+0x00"),
	#0x80332B68: main.sym("object_c_80332B64+0x04"),
	#0x80332CCC: main.sym("object_c_80332CCC+4*0"),
	#0x80332CD0: main.sym("object_c_80332CCC+4*1"),
	#0x80332CD4: main.sym("object_c_80332CCC+4*2"),
	#0x80332D10: main.sym("object_c_80332D10+2*0"),
	#0x80332D12: main.sym("object_c_80332D10+2*1"),
	#0x80332D58: main.sym("object_c_80332D58+2*0"),
	#0x80332D5A: main.sym("object_c_80332D58+2*1"),
	#0x80332D5C: main.sym("object_c_80332D58+2*2"),
	#0x80332E24: main.sym("object_c_80332E24+0x00"),
	#0x80332E28: main.sym("object_c_80332E24+0x04"),
	#0x80332E2C: main.sym("object_c_80332E24+0x08"),

	#0x80333794: main.sym("Na_data_80333598+4*127"),
	#0x80333DF2: main.sym("Na_data_80333DE0+2*9"),
	#0x80333FF0: main.sym("Na_PhonePan+4*127"),
	#0x803341F0: main.sym("Na_WidePan+4*127"),
	#0x803343F0: main.sym("Na_StereoPan+4*127"),

	0x803347C0: main.sym("__osViDevMgr+0x00"),
	0x803347C4: main.sym("__osViDevMgr+0x04"),
	0x803347C8: main.sym("__osViDevMgr+0x08"),
	0x803347CC: main.sym("__osViDevMgr+0x0C"),
	0x803347D0: main.sym("__osViDevMgr+0x10"),
	0x803347D4: main.sym("__osViDevMgr+0x14"),

	0x803347E0: main.sym("__osPiDevMgr+0x00"),
	0x803347E4: main.sym("__osPiDevMgr+0x04"),
	0x803347E8: main.sym("__osPiDevMgr+0x08"),
	0x803347EC: main.sym("__osPiDevMgr+0x0C"),
	0x803347F0: main.sym("__osPiDevMgr+0x10"),
	0x803347F4: main.sym("__osPiDevMgr+0x14"),

	0x80334800: main.sym("osClockRate+0"),
	0x80334804: main.sym("osClockRate+4"),

	# ==========================================================================
	# bss
	# ==========================================================================

	0x80339C34: main.sym("controller_data+0x14"),
	0x80339C38: main.sym("controller_data+0x18"),

	0x80339D28: main.sym("demo_bank+0x08"),

	0x80339E32: main.sym("player_data+0x32+2*0"),
	0x80339E34: main.sym("player_data+0x32+2*1"),
	0x80339E36: main.sym("player_data+0x32+2*2"),
	0x80339E3C: main.sym("player_data+0x3C+4*0"),
	0x80339E40: main.sym("player_data+0x3C+4*1"),
	0x80339E44: main.sym("player_data+0x3C+4*2"),
	0x80339E48: main.sym("player_data+0x48+4*0"),
	0x80339E4C: main.sym("player_data+0x48+4*1"),
	0x80339E50: main.sym("player_data+0x48+4*2"),

	0x80339ED8: main.sym("mario_entry+0x00"),
	0x80339ED9: main.sym("mario_entry+0x01"),
	0x80339EDA: main.sym("mario_entry+0x02"),
	0x80339EDB: main.sym("mario_entry+0x03"),
	0x80339EDC: main.sym("mario_entry+0x04"),

	0x80339EF0: main.sym("hud+0x00"),
	0x80339EF2: main.sym("hud+0x02"),
	0x80339EF4: main.sym("hud+0x04"),
	0x80339EF6: main.sym("hud+0x06"),
	0x80339EF8: main.sym("hud+0x08"),
	0x80339EFA: main.sym("hud+0x0A"),
	0x80339EFC: main.sym("hud+0x0C"),

	0x80339FF4: main.sym("mario_mirror+0x14"),
	0x80339FF8: main.sym("mario_mirror+0x18"),

	0x8033A047: main.sym("pl_shape_data+0x07"),

	0x8033A560: main.sym("scene_data+0x00"),
	0x8033A561: main.sym("scene_data+0x01"),
	0x8033A562: main.sym("scene_data+0x02"),
	0x8033A564: main.sym("scene_data+0x04"),
	0x8033A568: main.sym("scene_data+0x08"),
	0x8033A56C: main.sym("scene_data+0x0C"),
	0x8033A570: main.sym("scene_data+0x10"),
	0x8033A574: main.sym("scene_data+0x14"),
	0x8033A578: main.sym("scene_data+0x18"),
	0x8033A57C: main.sym("scene_data+0x1C"),
	0x8033A580: main.sym("scene_data+0x20"),
	0x8033A584: main.sym("scene_data+0x24"),
	0x8033A588: main.sym("scene_data+0x28"),
	0x8033A58C: main.sym("scene_data+0x2C+4*0"),
	0x8033A590: main.sym("scene_data+0x2C+4*1"),
	0x8033A594: main.sym("scene_data+0x34+0"),
	0x8033A595: main.sym("scene_data+0x35+1"),
	0x8033A596: main.sym("scene_data+0x36"),
	0x8033A598: main.sym("scene_data+0x38"),

	0x8033A740: main.sym("wipe+0x00"),
	0x8033A741: main.sym("wipe+0x01"),
	0x8033A742: main.sym("wipe+0x02"),
	0x8033A743: main.sym("wipe+0x03"),
	0x8033A744: main.sym("wipe+0x04"),
	0x8033A745: main.sym("wipe+0x05"),
	0x8033A746: main.sym("wipe+0x06"),
	0x8033A748: main.sym("wipe+0x08"),
	0x8033A74A: main.sym("wipe+0x0A"),
	0x8033A74C: main.sym("wipe+0x0C"),
	0x8033A74E: main.sym("wipe+0x0E"),
	0x8033A750: main.sym("wipe+0x10"),
	0x8033A752: main.sym("wipe+0x12"),
	0x8033A754: main.sym("wipe+0x14"),

	0x8033A7A8: main.sym("draw_mtxf+4*(4*3+0)"),
	0x8033A7AC: main.sym("draw_mtxf+4*(4*3+1)"),
	0x8033A7B0: main.sym("draw_mtxf+4*(4*3+2)"),

	0x8033B020: main.sym("time_data+0x00"),
	0x8033B022: main.sym("time_data+0x02"),
	0x8033B028: main.sym("time_data+0x08+0"),
	0x8033B02C: main.sym("time_data+0x08+4"),
	0x8033B050: main.sym("time_data+0x30+0"),
	0x8033B054: main.sym("time_data+0x30+4"),

	#0x8033C568: main.sym("_camera_bss_48-0x48+0x48"),
	#0x8033C578: main.sym("_camera_bss_48-0x48+0x58"),
	#0x8033C588: main.sym("_camera_bss_48-0x48+0x68"),
	#0x8033C594: main.sym("_camera_bss_48-0x48+0x74"),
	#0x8033C596: main.sym("_camera_bss_48-0x48+0x76"),
	#0x8033C598: main.sym("_camera_bss_48-0x48+0x78"),
	#0x8033C5A0: main.sym("_camera_bss_48-0x48+0x80"),
	#0x8033C5A4: main.sym("_camera_bss_48-0x48+0x84"),
	#0x8033C5A8: main.sym("_camera_bss_48-0x48+0x88"),
	#0x8033C5AC: main.sym("_camera_bss_48-0x48+0x8C"),
	#0x8033C5B0: main.sym("_camera_bss_48-0x48+0x90"),
	#0x8033C5B4: main.sym("_camera_bss_48-0x48+0x94"),
	#0x8033C5B6: main.sym("_camera_bss_48-0x48+0x96"),
	#0x8033C5B8: main.sym("_camera_bss_48-0x48+0x98"),
	#0x8033C5C0: main.sym("_camera_bss_48-0x48+0xA0"),
	#0x8033C5C2: main.sym("_camera_bss_48-0x48+0xA2"),
	#0x8033C5C4: main.sym("_camera_bss_48-0x48+0xA4"),
	#0x8033C5C8: main.sym("_camera_bss_48-0x48+0xA8"),
	#0x8033C5CA: main.sym("_camera_bss_48-0x48+0xAA"),
	#0x8033C5CC: main.sym("_camera_bss_48-0x48+0xAC"),
	#0x8033C5D0: main.sym("_camera_bss_48-0x48+0xB0"),
	#0x8033C5D2: main.sym("_camera_bss_48-0x48+0xB2"),
	#0x8033C5D4: main.sym("_camera_bss_48-0x48+0xB4"),
	#0x8033C5E8: main.sym("_camera_bss_48-0x48+0xC8"),
	#0x8033C5EC: main.sym("_camera_bss_48-0x48+0xCC"),
	#0x8033C5F0: main.sym("_camera_bss_48-0x48+0xD0"),
	#0x8033C5F4: main.sym("_camera_bss_48-0x48+0xD4"),
	#0x8033C5F8: main.sym("_camera_bss_48-0x48+0xD8"),
	#0x8033C5FC: main.sym("_camera_bss_48-0x48+0xDC"),
	#0x8033C600: main.sym("_camera_bss_48-0x48+0xE0"),
	#0x8033C604: main.sym("_camera_bss_48-0x48+0xE4"),
	#0x8033C608: main.sym("_camera_bss_48-0x48+0xE8"),
	#0x8033C60C: main.sym("_camera_bss_48-0x48+0xEC"),
	#0x8033C610: main.sym("_camera_bss_48-0x48+0xF0"),
	#0x8033C614: main.sym("_camera_bss_48-0x48+0xF4"),
	#0x8033C61C: main.sym("_camera_bss_48-0x48+0xFC"),
	#0x8033C61E: main.sym("_camera_bss_48-0x48+0xFE"),
	#0x8033C620: main.sym("_camera_bss_48-0x48+0x100"),
	#0x8033C622: main.sym("_camera_bss_48-0x48+0x102"),
	#0x8033C624: main.sym("_camera_bss_48-0x48+0x104"),
	#0x8033C628: main.sym("_camera_bss_48-0x48+0x108"),
	#0x8033C630: main.sym("_camera_bss_48-0x48+0x110"),
	#0x8033C632: main.sym("_camera_bss_48-0x48+0x112"),
	#0x8033C634: main.sym("_camera_bss_48-0x48+0x114"),
	#0x8033C668: main.sym("_camera_bss_48-0x48+0x148"),
	#0x8033C66C: main.sym("_camera_bss_48-0x48+0x14C"),
	#0x8033C670: main.sym("_camera_bss_48-0x48+0x150"),
	#0x8033C674: main.sym("_camera_bss_48-0x48+0x154"),
	#0x8033C676: main.sym("_camera_bss_48-0x48+0x156"),
	#0x8033C678: main.sym("_camera_bss_48-0x48+0x158"),
	#0x8033C67C: main.sym("_camera_bss_48-0x48+0x15C"),
	#0x8033C680: main.sym("_camera_bss_48-0x48+0x160"),
	#0x8033C684: main.sym("_camera_bss_48-0x48+0x164"),
	#0x8033C686: main.sym("_camera_bss_48-0x48+0x166"),
	#0x8033C688: main.sym("_camera_bss_48-0x48+0x168"),
	#0x8033C68A: main.sym("_camera_bss_48-0x48+0x16A"),
	#0x8033C68C: main.sym("_camera_bss_48-0x48+0x16C"),
	#0x8033C68E: main.sym("_camera_bss_48-0x48+0x16E"),
	#0x8033C690: main.sym("_camera_bss_48-0x48+0x170"),

	#0x8033C6D4: main.sym("camdata+0x3C"),
	#0x8033C6D5: main.sym("camdata+0x3D"),
	#0x8033C6F0: main.sym("camdata+0x58"),
	#0x8033C6F2: main.sym("camdata+0x5A"),
	#0x8033C6F4: main.sym("camdata+0x5C"),
	#0x8033C712: main.sym("camdata+0x7A"),
	#0x8033C714: main.sym("camdata+0x7C"),
	#0x8033C716: main.sym("camdata+0x7E"),
	#0x8033C730: main.sym("camdata+0x98"),
	#0x8033C732: main.sym("camdata+0x9A"),
	#0x8033C734: main.sym("camdata+0x9C"),
	#0x8033C736: main.sym("camdata+0x9E"),
	#0x8033C738: main.sym("camdata+0xA0"),
	#0x8033C73A: main.sym("camdata+0xA2"),
	#0x8033C73C: main.sym("camdata+0xA4"),
	#0x8033C740: main.sym("camdata+0xA8"),
	#0x8033C744: main.sym("camdata+0xAC"),
	#0x8033C748: main.sym("camdata+0xB0"),
	#0x8033C74C: main.sym("camdata+0xB4"),
	#0x8033C750: main.sym("camdata+0xB8"),
	#0x8033C754: main.sym("camdata+0xBC"),

	#0x8033C75A: main.sym("_camera_bss_238-0x238+0x23A"),
	#0x8033C75C: main.sym("_camera_bss_238-0x238+0x23C"),
	#0x8033C75E: main.sym("_camera_bss_238-0x238+0x23E"),
	#0x8033C760: main.sym("_camera_bss_238-0x238+0x240"),
	#0x8033C764: main.sym("_camera_bss_238-0x238+0x244"),
	#0x8033C768: main.sym("_camera_bss_238-0x238+0x248"),
	#0x8033C76A: main.sym("_camera_bss_238-0x238+0x24A"),
	#0x8033C76C: main.sym("_camera_bss_238-0x238+0x24C"),
	#0x8033C770: main.sym("_camera_bss_238-0x238+0x250"),
	#0x8033C772: main.sym("_camera_bss_238-0x238+0x252"),
	#0x8033C774: main.sym("_camera_bss_238-0x238+0x254"),
	#0x8033C776: main.sym("_camera_bss_238-0x238+0x256"),
	#0x8033C778: main.sym("_camera_bss_238-0x238+0x258"),
	#0x8033C77C: main.sym("_camera_bss_238-0x238+0x25C"),
	#0x8033C780: main.sym("_camera_bss_238-0x238+0x260"),
	#0x8033C788: main.sym("_camera_bss_238-0x238+0x268"),
	#0x8033C78A: main.sym("_camera_bss_238-0x238+0x26A"),
	#0x8033C78C: main.sym("_camera_bss_238-0x238+0x26C"),
	#0x8033C78E: main.sym("_camera_bss_238-0x238+0x26E"),
	#0x8033C7A8: main.sym("_camera_bss_238-0x238+0x288"),
	#0x8033C7AE: main.sym("_camera_bss_238-0x238+0x28E"),
	#0x8033C7D0: main.sym("_camera_bss_238-0x238+0x2B0"),
	#0x8033C7DC: main.sym("_camera_bss_238-0x238+0x2BC"),
	#0x8033C7E0: main.sym("_camera_bss_238-0x238+0x2C0"),
	#0x8033C7E8: main.sym("_camera_bss_238-0x238+0x2C8"),
	#0x8033C808: main.sym("_camera_bss_238-0x238+0x2E8"),
	#0x8033C828: main.sym("_camera_bss_238-0x238+0x308"),
	#0x8033C840: main.sym("_camera_bss_238-0x238+0x320"),
	#0x8033C844: main.sym("_camera_bss_238-0x238+0x324"),

	#0x8033C850: main.sym("_camera_bss_330-0x330+0x330"),
	#0x8033C950: main.sym("_camera_bss_330-0x330+0x430"),
	#0x8033CA50: main.sym("_camera_bss_330-0x330+0x530"),
	#0x8033CA54: main.sym("_camera_bss_330-0x330+0x534"),
	#0x8033CA58: main.sym("_camera_bss_330-0x330+0x538"),
	#0x8033CA5A: main.sym("_camera_bss_330-0x330+0x53A"),
	#0x8033CA5C: main.sym("_camera_bss_330-0x330+0x53C"),
	#0x8033CA60: main.sym("_camera_bss_330-0x330+0x540"),
	#0x8033CA82: main.sym("_camera_bss_330-0x330+0x562"),

	0x8033BF04: main.sym("bgdebug+0x00"),
	0x8033BF06: main.sym("bgdebug+0x02"),
	0x8033BF08: main.sym("bgdebug+0x04"),
	0x8033C18C: main.sym("object_data+0x74"),
	0x8035FB30: main.sym("object_dummy+0x0C"),
	0x8035FB31: main.sym("object_dummy+0x0D"),
	0x8035FDE0: main.sym("obj_freelist+0x60"),
	0x8035FE68: main.sym("area_table+0"),
	0x8035FE69: main.sym("area_table+1"),

	0x8035FF50: main.sym("backdata+0x00"),
	0x8035FF52: main.sym("backdata+0x02"),
	0x8035FF54: main.sym("backdata+0x04"),
	0x8035FF58: main.sym("backdata+0x08"),
	0x8035FF5C: main.sym("backdata+0x0C"),

	0x80360120: main.sym("_Na_game_bss+0x00"),
	0x80360128: main.sym("_Na_game_bss+0x08"),
	0x80360928: main.sym("_Na_game_bss+0x808"),
	0x80360C28: main.sym("_Na_game_bss+0xB08"),
	0x80360C38: main.sym("_Na_game_bss+0xB18"),
	0x80360C48: main.sym("_Na_game_bss+0xB28"),
	0x80360C5C: main.sym("_Na_game_bss+0xB3C"),
	0x80363808: main.sym("_Na_game_bss+0x36E8"),
	0x80363812: main.sym("_Na_game_bss+0x36F2"),
	0x80363813: main.sym("_Na_game_bss+0x36F3"),
	0x80363818: main.sym("_Na_game_bss+0x36F8"),

	0x80364AD0: main.sym("viRetraceMsg+0"),
	0x80364AD2: main.sym("viRetraceMsg+2"),
	0x80364AD4: main.sym("viRetraceMsg+4"),

	0x80364AE8: main.sym("viCounterMsg+0"),
	0x80364AEA: main.sym("viCounterMsg+2"),
	0x80364AEC: main.sym("viCounterMsg+4"),

	0x80365D1C: main.sym("__osContPifRam+0x3C"),

	0x80365DA0: main.sym("__osCurrentTime+0"),
	0x80365DA4: main.sym("__osCurrentTime+4"),

	0x80365E3C: main.sym("__osEepPifRam+0x3C"),

	# ==========================================================================

	0x001076D0: main.sym("_MainSegmentRomEnd"),
	0x004E9FA0: main.sym("_AnimeSegmentRomStart"),
	0x00577BC0: main.sym("_DemoSegmentRomStart"),
	0x00579140: main.sym("_AudioctlSegmentRomStart"),
	0x00590200: main.sym("_AudiotblSegmentRomStart"),
	0x00745F80: main.sym("_AudioseqSegmentRomStart"),
	0x00761B40: main.sym("_AudiobnkSegmentRomStart"),

	# ==========================================================================

	#0x80220D98: main.sym("Na_WorkStart-8"),
	#0x80220DB0: main.sym("_Na_work_bss_10-0x10+0x10"),
	#0x80220DB1: main.sym("_Na_work_bss_10-0x10+0x11"),
	#0x80220EA0: main.sym("_Na_work_bss_10-0x10+0x100"),
	#0x80220EA2: main.sym("_Na_work_bss_10-0x10+0x102"),
	#0x80220EA3: main.sym("_Na_work_bss_10-0x10+0x103"),
	#0x80220EA8: main.sym("_Na_work_bss_10-0x10+0x108"),
	#0x80220EB0: main.sym("_Na_work_bss_10-0x10+0x110"),
	#0x80220EB8: main.sym("_Na_work_bss_10-0x10+0x118"),
	#0x80220EC8: main.sym("_Na_work_bss_10-0x10+0x128"),
	#0x80220EF8: main.sym("_Na_work_bss_10-0x10+0x158"),
	#0x80220F08: main.sym("_Na_work_bss_10-0x10+0x168"),
	#0x80220F18: main.sym("_Na_work_bss_10-0x10+0x178"),
	#0x80220F28: main.sym("_Na_work_bss_10-0x10+0x188"),
	#0x80220F2C: main.sym("_Na_work_bss_10-0x10+0x18C"),
	#0x802210BC: main.sym("_Na_work_bss_10-0x10+0x31C"),
	#0x802210C0: main.sym("_Na_work_bss_10-0x10+0x320"),
	#0x802210F8: main.sym("_Na_work_bss_10-0x10+0x358"),
	#0x802210FC: main.sym("_Na_work_bss_10-0x10+0x35C"),
	#0x8022128C: main.sym("_Na_work_bss_10-0x10+0x4EC"),
	#0x80221290: main.sym("_Na_work_bss_10-0x10+0x4F0"),
	#0x802212C8: main.sym("_Na_work_bss_10-0x10+0x528"),
	#0x802212CC: main.sym("_Na_work_bss_10-0x10+0x52C"),
	#0x8022145C: main.sym("_Na_work_bss_10-0x10+0x6BC"),
	#0x80221460: main.sym("_Na_work_bss_10-0x10+0x6C0"),
	#0x80221498: main.sym("_Na_work_bss_10-0x10+0x6F8"),
	#0x802214A8: main.sym("_Na_work_bss_10-0x10+0x708"),
	#0x802214B0: main.sym("_Na_work_bss_10-0x10+0x710"),
	#0x802214C0: main.sym("_Na_work_bss_10-0x10+0x720"),
	#0x802214D0: main.sym("_Na_work_bss_10-0x10+0x730"),
	#0x80221510: main.sym("_Na_work_bss_10-0x10+0x770"),
	#0x80221610: main.sym("_Na_work_bss_10-0x10+0x870"),
	#0x80222610: main.sym("_Na_work_bss_10-0x10+0x1870"),
	#0x80222618: main.sym("_Na_work_bss_10-0x10+0x1878"),
	#0x80222619: main.sym("_Na_work_bss_10-0x10+0x1879"),
	#0x8022261A: main.sym("_Na_work_bss_10-0x10+0x187A"),
	#0x80222630: main.sym("_Na_work_bss_10-0x10+0x1890"),
	#0x80222644: main.sym("_Na_work_bss_10-0x10+0x18A4"),
	#0x802226A8: main.sym("_Na_work_bss_10-0x10+0x1908"),
	#0x802228C4: main.sym("_Na_work_bss_10-0x10+0x1B24"),
	#0x802229D8: main.sym("_Na_work_bss_10-0x10+0x1C38"),
	#0x802241D8: main.sym("_Na_work_bss_10-0x10+0x3438"),
	#0x80224248: main.sym("_Na_work_bss_10-0x10+0x34A8"),
	#0x80225BD8: main.sym("_Na_work_bss_10-0x10+0x4E38"),
	#0x80225C98: main.sym("_Na_work_bss_10-0x10+0x4EF8"),
	#0x80225CA8: main.sym("_Na_work_bss_10-0x10+0x4F08"),
	#0x80225CAC: main.sym("_Na_work_bss_10-0x10+0x4F0C"),
	#0x80225CB8: main.sym("_Na_work_bss_10-0x10+0x4F18"),
	#0x80225CC8: main.sym("_Na_work_bss_10-0x10+0x4F28"),
	#0x80225CD8: main.sym("_Na_work_bss_10-0x10+0x4F38"),
	#0x80225CE8: main.sym("_Na_work_bss_10-0x10+0x4F48"),
	#0x80225D00: main.sym("_Na_work_bss_10-0x10+0x4F60"),
	#0x80225E00: main.sym("_Na_work_bss_10-0x10+0x5060"),
	#0x80226300: main.sym("_Na_work_bss_10-0x10+0x5560"),
	#0x80226318: main.sym("_Na_work_bss_10-0x10+0x5578"),
	#0x80226320: main.sym("_Na_work_bss_10-0x10+0x5580"),
	#0x80226338: main.sym("_Na_work_bss_10-0x10+0x5598"),
	#0x80226938: main.sym("_Na_work_bss_10-0x10+0x5B98"),
	#0x8022693C: main.sym("_Na_work_bss_10-0x10+0x5B9C"),
	#0x80226940: main.sym("_Na_work_bss_10-0x10+0x5BA0"),
	#0x80226948: main.sym("_Na_work_bss_10-0x10+0x5BA8"),
	#0x80226A48: main.sym("_Na_work_bss_10-0x10+0x5CA8"),
	#0x80226B48: main.sym("_Na_work_bss_10-0x10+0x5DA8"),
	#0x80226B49: main.sym("_Na_work_bss_10-0x10+0x5DA9"),
	#0x80226B4A: main.sym("_Na_work_bss_10-0x10+0x5DAA"),
	#0x80226B4B: main.sym("_Na_work_bss_10-0x10+0x5DAB"),
	#0x80226B4C: main.sym("_Na_work_bss_10-0x10+0x5DAC"),
	#0x80226B50: main.sym("_Na_work_bss_10-0x10+0x5DB0"),
	#0x80226B54: main.sym("_Na_work_bss_10-0x10+0x5DB4"),
	#0x80226B58: main.sym("_Na_work_bss_10-0x10+0x5DB8"),
	#0x80226B5C: main.sym("_Na_work_bss_10-0x10+0x5DBC"),
	#0x80226B60: main.sym("_Na_work_bss_10-0x10+0x5DC0"),
	#0x80226B64: main.sym("_Na_work_bss_10-0x10+0x5DC4"),
	#0x80226B68: main.sym("_Na_work_bss_10-0x10+0x5DC8"),
	#0x80226B6C: main.sym("_Na_work_bss_10-0x10+0x5DCC"),
	#0x80226B70: main.sym("_Na_work_bss_10-0x10+0x5DD0"),
	#0x80226B74: main.sym("_Na_work_bss_10-0x10+0x5DD4"),
	#0x80226B78: main.sym("_Na_work_bss_10-0x10+0x5DD8"),
	#0x80226B7C: main.sym("_Na_work_bss_10-0x10+0x5DDC"),
	#0x80226B7E: main.sym("_Na_work_bss_10-0x10+0x5DDE"),
	#0x80226B7F: main.sym("_Na_work_bss_10-0x10+0x5DDF"),
	#0x80226B80: main.sym("_Na_work_bss_10-0x10+0x5DE0"),
	#0x80226B84: main.sym("_Na_work_bss_10-0x10+0x5DE4"),
	#0x80226B88: main.sym("_Na_work_bss_10-0x10+0x5DE8"),
	#0x80226B8C: main.sym("_Na_work_bss_10-0x10+0x5DEC"),
	#0x80226B90: main.sym("_Na_work_bss_10-0x10+0x5DF0"),
	#0x80226B98: main.sym("_Na_work_bss_10-0x10+0x5DF8"),
	#0x80226B9C: main.sym("_Na_work_bss_10-0x10+0x5DFC"),
	#0x80226BA0: main.sym("_Na_work_bss_10-0x10+0x5E00"),
	#0x80226C40: main.sym("_Na_work_bss_10-0x10+0x5EA0"),
	#0x80226C4C: main.sym("_Na_work_bss_10-0x10+0x5EAC"),
	#0x80226C52: main.sym("_Na_work_bss_10-0x10+0x5EB2"),
	#0x80226C58: main.sym("_Na_work_bss_10-0x10+0x5EB8"),
	#0x80226C98: main.sym("_Na_work_bss_10-0x10+0x5EF8"),

	0x80207A90: main.sym("backup-0x70"),
	0x80207A98: main.sym("backup-0x68"),
	0x80207A9C: main.sym("backup-0x64"),
	0x80207B08: main.sym("backup+0x08"),
	0x80207B0C: main.sym("backup+0x0C"),
	0x80207B25: main.sym("backup+0x25"),
	0x80207CC0: main.sym("backup+0x1C0"),

	0x030293E0: main.sym("txt_meter_n"),
	0x03029480: main.sym("gfx_meter_0"),
	0x03029570: main.sym("gfx_meter_n"),
	0x030295A0: main.sym("gfx_meter_end"),

	0x0700B3A0: main.sym("gfx_logo"),
	0x0700C6A0: main.sym("gfx_symbol"),
	0x0700C790: main.sym("logo_scale_a"),
	0x0700C880: main.sym("logo_scale_b"),
	0x0A000100: main.sym("gfx_titlebg_start"),
	0x0A000118: main.sym("gfx_titlebg_vtx"),
	0x0A000190: main.sym("gfx_titlebg_end"),

	0x0700D108: main.sym("gfx_smfont_start"),
	0x0700D160: main.sym("gfx_smfont_end"),
	0x0700F228: main.sym("gfx_course"),

	0x0702A880: main.sym("gfx_inside_0702A880"),
	0x07019248: main.sym("rr_07019080"),
	0x070192F0: main.sym("gfx_rr_07019128"),
	0x07019360: main.sym("gfx_rr_07019198"),
	0x070193C8: main.sym("gfx_rr_07019200"),
	0x07026400: main.sym("gfx_ending"),
}

seg_J0_code_text = {
	0x80247B7C: "J0.rspboot.text",
	0x80247B88: "J0.rspboot.text",
	0x80247BA8: "J0.gspFast3D_fifo.text",
	0x80247BAC: "J0.gspFast3D_fifo.text",

	0x80248A74: "J0.Main",
	0x80248A78: "J0.Main",
	0x80248A7C: "J0.Main",
	0x80248A80: "J0.Main",
	0x80248A90: "J0.Gfx",
	0x80248A94: "J0.Gfx",
	0x80248A98: "J0.Gfx",
	0x80248A9C: "J0.Gfx",

	0x802783E4: "J0.ulib.text",
	0x802783E8: "J0.ulib.text",
	0x802783EC: "J0.ulib.text",
	0x802783F0: "J0.ulib.text",
	0x8027841C: "J0.ulib.text",
	0x80278420: "J0.ulib.text",
	0x80278424: "J0.ulib.text",
	0x80278428: "J0.ulib.text",

	0x8031DB9C: "J0.rspboot.text",
	0x8031DBA4: "J0.aspMain.data",
	0x8031DBAC: "J0.rspboot.text",
	0x8031DBC4: "J0.aspMain.data",
	0x8031DBD4: "J0.aspMain.data",
	0x8031DBDC: "J0.aspMain.data",
}

sym_J0_code_data = {
	# ==========================================================================
	# data
	# ==========================================================================

	# src/main.c
	0x8032C620: main.sym("sc_audclient"),
	0x8032C624: main.sym("sc_gfxclient"),
	0x8032C628: main.sym("sc_task"),
	0x8032C62C: main.sym("sc_audtask"),
	0x8032C630: main.sym("sc_gfxtask"),
	0x8032C634: main.sym("sc_audtask_next"),
	0x8032C638: main.sym("sc_gfxtask_next"),
	0x8032C63C: main.sym("sc_aud"),
	0x8032C640: main.sym("sc_vi"),
	0x8032C644: main.sym("reset_timer"),
	0x8032C648: main.sym("reset_frame"),
	0x8032C64C: main.sym("debug_stage"),
	0x8032C650: main.sym("debug_thread"),
	0x8032C654: main.sym("debug_time"),
	0x8032C658: main.sym("debug_mem"),
	0x8032C65C: main.sym("debug_time_seq"),
	0x8032C66C: main.sym("debug_mem_seq"),
	0x8032C67C: main.sym("debug_time_idx"),
	0x8032C680: main.sym("debug_mem_idx"),

	# src/graphics.c
	0x8032C690: main.sym("gfx_8032D5D0"),
	0x8032C694: main.sym("gfx_frame", flag={"GLOBL"}),
	0x8032C698: main.sym("gfx_vi", flag={"GLOBL"}),
	0x8032C69C: main.sym("gfx_dp", flag={"GLOBL"}),
	0x8032C6A0: main.sym("gfx_callback", flag={"GLOBL"}),
	0x8032C6A4: main.sym("cont1", flag={"GLOBL"}),
	0x8032C6A8: main.sym("cont2", flag={"GLOBL"}),
	0x8032C6AC: main.sym("contp", flag={"GLOBL"}),
	0x8032C6B0: main.sym("demop", flag={"GLOBL"}),
	0x8032C6B4: main.sym("demo_index", flag={"GLOBL"}),
	0x8032C6B8: main.sym("demo_rec"),

	# src/audio.c
	0x8032C6C0: main.sym("aud_mute_flag"),
	0x8032C6C4: main.sym("aud_lock_flag"),
	0x8032C6C8: main.sym("bgm_stage"),
	0x8032C6CC: main.sym("bgm_shell"),
	0x8032C6D0: main.sym("bgm_special"),
	0x8032C6D4: main.sym("aud_endless_flag"),
	0x8032C6D8: main.sym("aud_8032D618"),
	0x8032C6DC: main.sym("aud_8032D61C"),
	0x8032C6E8: main.sym("aud_modetab"),
	0x8032C6F0: main.sym("aud_levelse_table"),
	0x8032C780: main.sym("aud_wave_flag"),

	# src/game.c
	0x8032C790: main.sym_var("staff_01", "static const char *", "[]"),
	0x8032C798: main.sym_var("staff_02", "static const char *", "[]"),
	0x8032C7A4: main.sym_var("staff_03", "static const char *", "[]"),
	0x8032C7B0: main.sym_var("staff_04", "static const char *", "[]"),
	0x8032C7C0: main.sym_var("staff_05", "static const char *", "[]"),
	0x8032C7C8: main.sym_var("staff_06", "static const char *", "[]"),
	0x8032C7D0: main.sym_var("staff_07", "static const char *", "[]"),
	0x8032C7DC: main.sym_var("staff_08", "static const char *", "[]"),
	0x8032C7E8: main.sym_var("staff_09", "static const char *", "[]"),
	0x8032C7F8: main.sym_var("staff_10", "static const char *", "[]"),
	0x8032C800: main.sym_var("staff_11", "static const char *", "[]"),
	0x8032C808: main.sym_var("staff_12", "static const char *", "[]"),
	0x8032C810: main.sym_var("staff_13", "static const char *", "[]"),
	0x8032C81C: main.sym_var("staff_14", "static const char *", "[]"),
	0x8032C824: main.sym_var("staff_15", "static const char *", "[]"),
	0x8032C834: main.sym_var("staff_16", "static const char *", "[]"),
	0x8032C83C: main.sym_var("staff_17", "static const char *", "[]"),
	0x8032C848: main.sym_var("staff_18", "static const char *", "[]"),
	0x8032C858: main.sym_var("staff_19", "static const char *", "[]"),
	0x8032C860: main.sym_var("staff_20", "static const char *", "[]"),
	0x8032C868: main.sym("staff_table"),
	0x8032C9D8: main.sym("mario", flag={"GLOBL"}),
	0x8032C9DC: main.sym("game_8032D940"),
	0x8032C9E0: main.sym("mid_flag"),

	# src/collision.c
	0x8032C9F0: main.sym("collisiontab"),
	0x8032CAE8: main.sym("fdamagetab"),
	0x8032CB0C: main.sym("bdamagetab"),
	0x8032CB30: main.sym("door_flag"),
	0x8032CB34: main.sym("pipe_flag"),
	0x8032CB38: main.sym("slider_flag"),

	# src/player.c
	0x8032CB40: main.sym("pl_surfacetab"),
	0x8032CB6C: main.sym("pl_unpresstab"),
	0x8032CB80: main.sym("pl_flash_pattern"),

	# src/physics.c
	0x8032CB90: main.sym("quicksand_speed", flag={"GLOBL"}),
	0x8032CB98: main.sym("water_ground", flag={"GLOBL"}),

	# src/pldemo.c
	0x8032CBD0: main.sym("pldemo_vp", flag={"GLOBL"}),
	0x8032CBE0: main.sym("pldemo_staff", flag={"GLOBL"}),
	0x8032CBE4: main.sym("pldemo_8032DB44", flag={"GLOBL"}),
	0x8032CBE8: main.sym("pldemo_8032DB48", flag={"GLOBL"}),
	0x8032CBEC: main.sym("pldemo_8032DB4C", flag={"GLOBL"}),
	0x8032CBF4: main.sym("pldemo_8032DB54", flag={"GLOBL"}),
	0x8032CBFC: main.sym("pldemo_8032DB5C", flag={"GLOBL"}),
	0x8032CCD4: main.sym("pldemo_8032DC34", flag={"GLOBL"}),
	0x8032CCD8: main.sym("pldemo_8032DC38", flag={"GLOBL"}),
	0x8032CCDC: main.sym("pldemo_8032DC3C", flag={"GLOBL"}),

	# src/plmove.c
	#0x8032DC50: main.sym("plmove_8032DC50", flag={"GLOBL"}),
	#0x8032DC68: main.sym("plmove_8032DC68", flag={"GLOBL"}),
	#0x8032DC80: main.sym("plmove_8032DC80", flag={"GLOBL"}),
	#0x8032DC98: main.sym("plmove_8032DC98", flag={"GLOBL"}),
	#0x8032DCB0: main.sym("plmove_8032DCB0", flag={"GLOBL"}),
	#0x8032DCC8: main.sym("plmove_8032DCC8", flag={"GLOBL"}),
	#0x8032DCE0: main.sym("plmove_8032DCE0", flag={"GLOBL"}),
	#0x8032DCF8: main.sym("plmove_8032DCF8", flag={"GLOBL"}),
	#0x8032DD10: main.sym("plmove_8032DD10", flag={"GLOBL"}),

	# src/plswim.c
	#0x8032DD30: main.sym("plswim_8032DD30", flag={"GLOBL"}),
	#0x8032DD34: main.sym("plswim_8032DD34", flag={"GLOBL"}),
	#0x8032DD38: main.sym("plswim_8032DD38", flag={"GLOBL"}),

	# src/pltake.c
	#0x8032DD40: main.sym("pltake_8032DD40", flag={"GLOBL"}),

	# src/callback.c
	0x8032CDF0: main.sym("pl_eyes_table"),
	0x8032CDF8: main.sym("pl_punch_table"),
	0x8032CE0C: main.sym("pl_punch_stamp"),

	# src/memory.c
	0x8032CE10: main.sym("mem_frame"),

	# src/backup.c
	0x8032CE20: main.sym("bu_course", flag={"GLOBL"}),
	0x8032CE24: main.sym("bu_level", flag={"GLOBL"}),
	0x8032CE28: main.sym("bu_hiscore", flag={"GLOBL"}),
	0x8032CE2C: main.sym("bu_myscore", flag={"GLOBL"}),
	0x8032CE30: main.sym("bu_star", flag={"GLOBL"}),
	0x8032CE34: main.sym("bu_jump", flag={"GLOBL"}),
	0x8032CE38: main.sym("coursetab", flag={"GLOBL"}),

	# src/scene.c
	0x8032CE60: main.sym("mario_actor", flag={"GLOBL"}),
	0x8032CE64: main.sym("shape_table", flag={"GLOBL"}),
	0x8032CE68: main.sym("scene_table", flag={"GLOBL"}),
	0x8032CE6C: main.sym("scenep", flag={"GLOBL"}),
	0x8032CE70: main.sym("staffp", flag={"GLOBL"}),
	0x8032CE74: main.sym("sn_viewport"),
	0x8032CE78: main.sym("sn_scissor"),
	0x8032CE7C: main.sym("wipe_delay"),
	0x8032CE80: main.sym("scene_fill"),
	0x8032CE84: main.sym("blank_fill"),
	0x8032CE88: main.sym("blank_r"),
	0x8032CE8C: main.sym("blank_g"),
	0x8032CE90: main.sym("blank_b"),
	0x8032CE94: main.sym("file_index", flag={"GLOBL"}),
	0x8032CE98: main.sym("stage_index", flag={"GLOBL"}),
	0x8032CE9C: main.sym("port_script"),
	0x8032CEEC: main.sym("port_type"),
	0x8032CF00: main.sym("default_vp"),

	# src/draw.c
	0x8032CF10: main.sym("draw_rendermode_1"),
	0x8032CF50: main.sym("draw_rendermode_2"),
	0x8032CF90: main.sym("draw_scene", flag={"GLOBL"}),
	0x8032CF94: main.sym("draw_layer", flag={"GLOBL"}),
	0x8032CF98: main.sym("draw_persp", flag={"GLOBL"}),
	0x8032CF9C: main.sym("draw_camera", flag={"GLOBL"}),
	0x8032CFA0: main.sym("draw_object", flag={"GLOBL"}),
	0x8032CFA4: main.sym("draw_hand", flag={"GLOBL"}),
	0x8032CFA8: main.sym("draw_timer", flag={"GLOBL"}),

	# src/time.c
	0x8032CFB0: main.sym("time_mode"),
	0x8032CFB4: main.sym("time_cpu"),
	0x8032CFB8: main.sym("time_rcp"),

	# src/camera.c
	#0x8032DF20: main.sym("camera_8032DF20", flag={"GLOBL"}),
	#0x8032DF24: main.sym("camera_8032DF24", flag={"GLOBL"}),
	#0x8032DF28: main.sym("camera_8032DF28", flag={"GLOBL"}),
	#0x8032DF2C: main.sym("camera_8032DF2C", flag={"GLOBL"}),
	#0x8032DF30: main.sym("camera_8032DF30", flag={"GLOBL"}),
	#0x8032DF34: main.sym("camera_8032DF34", flag={"GLOBL"}),
	#0x8032DF38: main.sym("camera_stagescene", flag={"GLOBL"}),
	#0x8032DF3C: main.sym("camera_prevstage", flag={"GLOBL"}),
	#0x8032DF40: main.sym("camera_8032DF40", flag={"GLOBL"}),
	#0x8032DF44: main.sym("camera_8032DF44", flag={"GLOBL"}),
	#0x8032DF48: main.sym("camera_8032DF48", flag={"GLOBL"}),
	#0x8032DF4C: main.sym("camera_8032DF4C", flag={"GLOBL"}),
	#0x8032DF50: main.sym("camera_8032DF50", flag={"GLOBL"}),
	#0x8032DF54: main.sym("camera_8032DF54", flag={"GLOBL"}),
	#0x8032DF58: main.sym("camera_8032DF58", flag={"GLOBL"}),
	#0x8032DF5C: main.sym("camera_8032DF5C", flag={"GLOBL"}),
	0x8032D000: main.sym("mario_cam", flag={"GLOBL"}),
	0x8032D004: main.sym("luigi_cam", flag={"GLOBL"}),
	0x8032D008: main.sym("camera_8032DF68", flag={"GLOBL"}),
	0x8032D00C: main.sym("camera_8032DF6C", flag={"GLOBL"}),
	#0x8032DF78: main.sym("camera_8032DF78", flag={"GLOBL"}),
	#0x8032DF84: main.sym("camera_8032DF84", flag={"GLOBL"}),
	#0x8032DF90: main.sym("camera_8032DF90", flag={"GLOBL"}),
	#0x8032DF9C: main.sym("camera_8032DF9C", flag={"GLOBL"}),
	#0x8032DFA8: main.sym("camera_8032DFA8", flag={"GLOBL"}),
	#0x8032DFF0: main.sym("camera_8032DFF0", flag={"GLOBL"}),
	#0x8032DFFC: main.sym("camera_8032DFFC", flag={"GLOBL"}),
	#0x8032E008: main.sym("camera_8032E008", flag={"GLOBL"}),
	#0x8032E018: main.sym("camera_8032E018", flag={"GLOBL"}),
	#0x8032E020: main.sym("campos_bbh_library_test", flag={"GLOBL"}),
	#0x8032E050: main.sym("campos_bbh_library", flag={"GLOBL"}),
	#0x8032E080: main.sym("camctl_null", flag={"GLOBL"}),
	#0x8032E098: main.sym("camctl_sl", flag={"GLOBL"}),
	#0x8032E0E0: main.sym("camctl_thi", flag={"GLOBL"}),
	#0x8032E128: main.sym("camctl_hmc", flag={"GLOBL"}),
	#0x8032E1D0: main.sym("camctl_ssl", flag={"GLOBL"}),
	#0x8032E248: main.sym("camctl_rr", flag={"GLOBL"}),
	#0x8032E338: main.sym("camctl_cotmc", flag={"GLOBL"}),
	#0x8032E368: main.sym("camctl_ccm", flag={"GLOBL"}),
	#0x8032E3B0: main.sym("camctl_inside", flag={"GLOBL"}),
	#0x8032E6F8: main.sym("camctl_bbh", flag={"GLOBL"}),
	#0x8032ECB0: main.sym("camctl_table", flag={"GLOBL"}),
	#0x8032ED50: main.sym("campath_8032ED50", flag={"GLOBL"}),
	#0x8032EE08: main.sym("campath_8032EE08", flag={"GLOBL"}),
	#0x8032EEC0: main.sym("campath_8032EEC0", flag={"GLOBL"}),
	#0x8032EF30: main.sym("campath_8032EF30", flag={"GLOBL"}),
	#0x8032EFA0: main.sym("campath_8032EFA0", flag={"GLOBL"}),
	#0x8032EFF0: main.sym("campath_8032EFF0", flag={"GLOBL"}),
	#0x8032F048: main.sym("campath_8032F048", flag={"GLOBL"}),
	#0x8032F0E8: main.sym("campath_8032F0E8", flag={"GLOBL"}),
	#0x8032F130: main.sym("campath_8032F130", flag={"GLOBL"}),
	#0x8032F178: main.sym("campath_8032F178", flag={"GLOBL"}),
	#0x8032F1B8: main.sym("campath_8032F1B8", flag={"GLOBL"}),
	#0x8032F1F0: main.sym("camera_8032F1F0", flag={"GLOBL"}),
	#0x8032F1FC: main.sym("camera_8032F1FC", flag={"GLOBL"}),
	#0x8032F208: main.sym("camera_8032F208", flag={"GLOBL"}),
	#0x8032F214: main.sym("campath_8032F214", flag={"GLOBL"}),
	#0x8032F32C: main.sym("campath_8032F32C", flag={"GLOBL"}),
	#0x8032F444: main.sym("campath_8032F444", flag={"GLOBL"}),
	#0x8032F48C: main.sym("campath_8032F48C", flag={"GLOBL"}),
	#0x8032F4D4: main.sym("camdemo_8032F4D4", flag={"GLOBL"}),
	#0x8032F534: main.sym("camdemo_8032F534", flag={"GLOBL"}),
	#0x8032F544: main.sym("camdemo_8032F544", flag={"GLOBL"}),
	#0x8032F554: main.sym("camdemo_8032F554", flag={"GLOBL"}),
	#0x8032F564: main.sym("camdemo_8032F564", flag={"GLOBL"}),
	#0x8032F56C: main.sym("camdemo_8032F56C", flag={"GLOBL"}),
	#0x8032F574: main.sym("camdemo_8032F574", flag={"GLOBL"}),
	#0x8032F59C: main.sym("camdemo_8032F59C", flag={"GLOBL"}),
	#0x8032F5C4: main.sym("camdemo_8032F5C4", flag={"GLOBL"}),
	#0x8032F5DC: main.sym("camdemo_8032F5DC", flag={"GLOBL"}),
	#0x8032F5F4: main.sym("camdemo_8032F5F4", flag={"GLOBL"}),
	#0x8032F60C: main.sym("camdemo_8032F60C", flag={"GLOBL"}),
	#0x8032F624: main.sym("camdemo_8032F624", flag={"GLOBL"}),
	#0x8032F634: main.sym("camdemo_8032F634", flag={"GLOBL"}),
	#0x8032F63C: main.sym("camdemo_8032F63C", flag={"GLOBL"}),
	#0x8032F64C: main.sym("camdemo_8032F64C", flag={"GLOBL"}),
	#0x8032F65C: main.sym("camdemo_8032F65C", flag={"GLOBL"}),
	#0x8032F674: main.sym("camdemo_8032F674", flag={"GLOBL"}),
	#0x8032F69C: main.sym("camdemo_8032F69C", flag={"GLOBL"}),
	#0x8032F6AC: main.sym("camdemo_8032F6AC", flag={"GLOBL"}),
	#0x8032F6BC: main.sym("camdemo_8032F6BC", flag={"GLOBL"}),
	#0x8032F6CC: main.sym("camdemo_8032F6CC", flag={"GLOBL"}),
	#0x8032F6DC: main.sym("camdemo_8032F6DC", flag={"GLOBL"}),
	#0x8032F6F4: main.sym("camdemo_8032F6F4", flag={"GLOBL"}),
	#0x8032F6FC: main.sym("camdemo_8032F6FC", flag={"GLOBL"}),
	#0x8032F70C: main.sym("camdemo_8032F70C", flag={"GLOBL"}),
	#0x8032F714: main.sym("camdemo_8032F714", flag={"GLOBL"}),
	#0x8032F71C: main.sym("camdemo_8032F71C", flag={"GLOBL"}),
	#0x8032F72C: main.sym("camdemo_8032F72C", flag={"GLOBL"}),
	#0x8032F734: main.sym("camdemo_8032F734", flag={"GLOBL"}),
	#0x8032F74C: main.sym("camdemo_8032F74C", flag={"GLOBL"}),
	#0x8032F754: main.sym("camdemo_8032F754", flag={"GLOBL"}),
	#0x8032F75C: main.sym("camdemo_8032F75C", flag={"GLOBL"}),
	#0x8032F764: main.sym("camdemo_8032F764", flag={"GLOBL"}),
	#0x8032F76C: main.sym("camdemo_8032F76C", flag={"GLOBL"}),
	#0x8032F774: main.sym("camdemo_8032F774", flag={"GLOBL"}),
	#0x8032F784: main.sym("camdemo_8032F784", flag={"GLOBL"}),
	#0x8032F794: main.sym("camdemo_8032F794", flag={"GLOBL"}),
	#0x8032F7A4: main.sym("camdemo_8032F7A4", flag={"GLOBL"}),
	#0x8032F7B4: main.sym("camdemo_8032F7B4", flag={"GLOBL"}),
	#0x8032F7C4: main.sym("camdemo_8032F7C4", flag={"GLOBL"}),
	#0x8032F7D4: main.sym("camdemo_8032F7D4", flag={"GLOBL"}),
	#0x8032F7EC: main.sym("camdemo_8032F7EC", flag={"GLOBL"}),
	#0x8032F804: main.sym("camera_windemo_table", flag={"GLOBL"}),
	#0x8032F870: main.sym("camera_pause_table", flag={"GLOBL"}),
	#0x8032F884: main.sym("campath_battlefield_eye", flag={"GLOBL"}),
	#0x8032F8AC: main.sym("campath_battlefield_look", flag={"GLOBL"}),
	#0x8032F8D4: main.sym("campath_wf1_eye", flag={"GLOBL"}),
	#0x8032F8FC: main.sym("campath_wf1_look", flag={"GLOBL"}),
	#0x8032F924: main.sym("campath_jrb1_eye", flag={"GLOBL"}),
	#0x8032F94C: main.sym("campath_jrb1_look", flag={"GLOBL"}),
	#0x8032F974: main.sym("campath_ccm2_eye", flag={"GLOBL"}),
	#0x8032F99C: main.sym("campath_ccm2_look", flag={"GLOBL"}),
	#0x8032F9C4: main.sym("campath_bbh1_eye", flag={"GLOBL"}),
	#0x8032F9E4: main.sym("campath_bbh1_look", flag={"GLOBL"}),
	#0x8032FA04: main.sym("campath_hmc1_eye", flag={"GLOBL"}),
	#0x8032FA2C: main.sym("campath_hmc1_look", flag={"GLOBL"}),
	#0x8032FA54: main.sym("campath_thi3_eye", flag={"GLOBL"}),
	#0x8032FA6C: main.sym("campath_thi3_look", flag={"GLOBL"}),
	#0x8032FA84: main.sym("campath_lll2_eye", flag={"GLOBL"}),
	#0x8032FAB4: main.sym("campath_lll2_look", flag={"GLOBL"}),
	#0x8032FAE4: main.sym("campath_ssl1_eye", flag={"GLOBL"}),
	#0x8032FB14: main.sym("campath_ssl1_look", flag={"GLOBL"}),
	#0x8032FB44: main.sym("campath_ddd1_eye", flag={"GLOBL"}),
	#0x8032FB7C: main.sym("campath_ddd1_look", flag={"GLOBL"}),
	#0x8032FBB4: main.sym("campath_sl1_eye", flag={"GLOBL"}),
	#0x8032FBD4: main.sym("campath_sl1_look", flag={"GLOBL"}),
	#0x8032FBF4: main.sym("campath_wdw1_eye", flag={"GLOBL"}),
	#0x8032FC14: main.sym("campath_wdw1_look", flag={"GLOBL"}),
	#0x8032FC34: main.sym("campath_ttm1_eye", flag={"GLOBL"}),
	#0x8032FC64: main.sym("campath_ttm1_look", flag={"GLOBL"}),
	#0x8032FC94: main.sym("campath_thi1_eye", flag={"GLOBL"}),
	#0x8032FCCC: main.sym("campath_thi1_look", flag={"GLOBL"}),
	#0x8032FD04: main.sym("campath_ttc1_eye", flag={"GLOBL"}),
	#0x8032FD24: main.sym("campath_ttc1_look", flag={"GLOBL"}),
	#0x8032FD44: main.sym("campath_rr1_eye", flag={"GLOBL"}),
	#0x8032FD64: main.sym("campath_rr1_look", flag={"GLOBL"}),
	#0x8032FD84: main.sym("campath_sa1_eye", flag={"GLOBL"}),
	#0x8032FDAC: main.sym("campath_sa1_look", flag={"GLOBL"}),
	#0x8032FDD4: main.sym("campath_cotmc1_eye", flag={"GLOBL"}),
	#0x8032FDFC: main.sym("campath_cotmc1_look", flag={"GLOBL"}),
	#0x8032FE24: main.sym("campath_ddd2_eye", flag={"GLOBL"}),
	#0x8032FE4C: main.sym("campath_ddd2_look", flag={"GLOBL"}),
	#0x8032FE74: main.sym("campath_ccm1_eye", flag={"GLOBL"}),
	#0x8032FE94: main.sym("campath_ccm1_look", flag={"GLOBL"}),

	# src/object.c
	0x8032EF60: main.sym("objproc_table"),
	0x8032EF6C: main.sym("pl_effecttab"),

	# src/objectlib.c
	#0x80330000: main.sym("objectlib_80330000", flag={"GLOBL"}),
	#0x80330004: main.sym("bittab", flag={"GLOBL"}),
	#0x80330014: main.sym("areastagetab", flag={"GLOBL"}),

	# src/object_a.c
	#0x80330020: main.sym("object_a_80330020", flag={"GLOBL"}),
	#0x8033002C: main.sym("object_a_8033002C", flag={"GLOBL"}),
	#0x8033006C: main.sym("object_a_8033006C", flag={"GLOBL"}),
	#0x80330074: main.sym("object_a_80330074", flag={"GLOBL"}),
	#0x80330084: main.sym("object_a_80330084", flag={"GLOBL"}),
	#0x80330094: main.sym("object_a_80330094", flag={"GLOBL"}),
	#0x803300A8: main.sym("object_a_803300A8", flag={"GLOBL"}),
	#0x803300AC: main.sym("object_a_803300AC", flag={"GLOBL"}),
	#0x803300BC: main.sym("object_a_803300BC", flag={"GLOBL"}),
	#0x803300E0: main.sym("object_a_803300E0", flag={"GLOBL"}),
	#0x80330140: main.sym("object_a_80330140", flag={"GLOBL"}),
	#0x8033015C: main.sym("object_a_8033015C", flag={"GLOBL"}),
	#0x80330198: main.sym("object_a_80330198", flag={"GLOBL"}),
	#0x803301A8: main.sym("object_a_803301A8", flag={"GLOBL"}),
	#0x803301C0: main.sym("object_a_803301C0", flag={"GLOBL"}),
	#0x803301D0: main.sym("object_a_803301D0", flag={"GLOBL"}),
	#0x803301E4: main.sym("object_a_803301E4", flag={"GLOBL"}),
	#0x803301F4: main.sym("object_a_803301F4", flag={"GLOBL"}),
	#0x80330204: main.sym("object_a_80330204", flag={"GLOBL"}),
	#0x80330224: main.sym("object_a_80330224", flag={"GLOBL"}),
	#0x8033022C: main.sym("object_a_8033022C", flag={"GLOBL"}),
	#0x80330244: main.sym("object_a_80330244", flag={"GLOBL"}),
	#0x80330260: main.sym("object_a_80330260", flag={"GLOBL"}),
	#0x80330288: main.sym("object_a_80330288", flag={"GLOBL"}),
	#0x80330290: main.sym("object_a_80330290", flag={"GLOBL"}),
	#0x80330298: main.sym("object_a_80330298", flag={"GLOBL"}),
	#0x803302AC: main.sym("object_a_803302AC", flag={"GLOBL"}),
	#0x803302DC: main.sym("object_a_803302DC", flag={"GLOBL"}),
	#0x803302EC: main.sym("object_a_803302EC", flag={"GLOBL"}),
	#0x80330318: main.sym("object_a_80330318", flag={"GLOBL"}),
	#0x8033032C: main.sym("object_a_8033032C", flag={"GLOBL"}),
	#0x80330340: main.sym("object_a_80330340", flag={"GLOBL"}),
	#0x80330354: main.sym("object_a_80330354", flag={"GLOBL"}),
	#0x8033035C: main.sym("object_a_8033035C", flag={"GLOBL"}),
	#0x80330370: main.sym("object_a_80330370", flag={"GLOBL"}),
	#0x80330380: main.sym("object_a_80330380", flag={"GLOBL"}),
	#0x80330390: main.sym("object_a_80330390", flag={"GLOBL"}),
	#0x803303A0: main.sym("object_a_803303A0", flag={"GLOBL"}),
	#0x803303B0: main.sym("object_a_803303B0", flag={"GLOBL"}),
	#0x803303C0: main.sym("object_a_803303C0", flag={"GLOBL"}),
	#0x803303E8: main.sym("object_a_803303E8", flag={"GLOBL"}),
	#0x803303F8: main.sym("object_a_803303F8", flag={"GLOBL"}),
	#0x80330408: main.sym("object_a_80330408", flag={"GLOBL"}),
	#0x80330410: main.sym("object_a_80330410", flag={"GLOBL"}),
	#0x80330420: main.sym("object_a_80330420", flag={"GLOBL"}),
	#0x8033042C: main.sym("object_a_8033042C", flag={"GLOBL"}),
	#0x8033043C: main.sym("object_a_8033043C", flag={"GLOBL"}),
	#0x80330450: main.sym("object_a_80330450", flag={"GLOBL"}),
	#0x8033045C: main.sym("object_a_8033045C", flag={"GLOBL"}),
	#0x8033046C: main.sym("object_a_8033046C", flag={"GLOBL"}),
	#0x80330470: main.sym("object_a_80330470", flag={"GLOBL"}),
	#0x80330474: main.sym("object_a_80330474", flag={"GLOBL"}),
	#0x80330478: main.sym("object_a_80330478", flag={"GLOBL"}),
	#0x80330480: main.sym("object_a_80330480", flag={"GLOBL"}),
	#0x803304C8: main.sym("object_a_803304C8", flag={"GLOBL"}),
	#0x80330518: main.sym("object_a_80330518", flag={"GLOBL"}),
	#0x803305F0: main.sym("object_a_803305F0", flag={"GLOBL"}),
	#0x803305F4: main.sym("object_a_803305F4", flag={"GLOBL"}),
	#0x803305F8: main.sym("object_a_803305F8", flag={"GLOBL"}),
	#0x8033067C: main.sym("object_a_8033067C", flag={"GLOBL"}),
	#0x80330688: main.sym("object_a_80330688", flag={"GLOBL"}),
	#0x80330698: main.sym("object_a_80330698", flag={"GLOBL"}),
	#0x803306A8: main.sym("object_a_803306A8", flag={"GLOBL"}),
	#0x803306B4: main.sym("object_a_803306B4", flag={"GLOBL"}),
	#0x803306DC: main.sym("object_a_803306DC", flag={"GLOBL"}),
	#0x80330738: main.sym("object_a_80330738", flag={"GLOBL"}),
	#0x803307A0: main.sym("object_a_803307A0", flag={"GLOBL"}),
	#0x803307C0: main.sym("object_a_803307C0"),
	#0x803307F4: main.sym("object_a_803307F4"),
	#0x80330828: main.sym("object_a_80330828", flag={"GLOBL"}),
	#0x80330830: main.sym("object_a_80330830", flag={"GLOBL"}),
	#0x80330840: main.sym("object_a_80330840", flag={"GLOBL"}),
	#0x80330850: main.sym("object_a_80330850"),
	#0x80330884: main.sym("object_a_80330884"),
	#0x803308A8: main.sym("object_a_803308A8"),
	#0x803308CC: main.sym("object_a_803308CC", flag={"GLOBL"}),
	#0x803308D8: main.sym("object_a_803308D8", flag={"GLOBL"}),
	#0x803308F8: main.sym("object_a_803308F8", flag={"GLOBL"}),
	#0x80330900: main.sym("object_a_80330900", flag={"GLOBL"}),
	#0x80330924: main.sym("object_a_80330924"),
	#0x80330940: main.sym("object_a_80330940"),
	#0x8033095C: main.sym("object_a_8033095C"),
	#0x80330978: main.sym("object_a_80330978"),
	#0x80330994: main.sym("object_a_80330994"),
	#0x803309B0: main.sym("object_a_803309B0"),
	#0x803309CC: main.sym("object_a_803309CC"),
	#0x803309E8: main.sym("object_a_803309E8"),
	#0x80330A04: main.sym("object_a_80330A04"),
	#0x80330A20: main.sym("object_a_80330A20"),
	#0x80330A3C: main.sym("object_a_80330A3C"),
	#0x80330A58: main.sym("object_a_80330A58"),
	#0x80330A74: main.sym("object_a_80330A74"),
	#0x80330A90: main.sym("object_a_80330A90"),
	#0x80330AAC: main.sym("object_a_80330AAC", flag={"GLOBL"}),
	#0x80330B1C: main.sym("object_a_80330B1C", flag={"GLOBL"}),
	#0x80330B38: main.sym("object_a_80330B38", flag={"GLOBL"}),
	#0x80330B44: main.sym("object_a_80330B44", flag={"GLOBL"}),
	#0x80330B5C: main.sym("object_a_80330B5C", flag={"GLOBL"}),
	#0x80330B68: main.sym("object_a_80330B68", flag={"GLOBL"}),
	#0x80330B74: main.sym("object_a_80330B74", flag={"GLOBL"}),
	#0x80330B84: main.sym("object_a_80330B84", flag={"GLOBL"}),
	#0x80330B90: main.sym("object_a_80330B90", flag={"GLOBL"}),
	#0x80330BA0: main.sym("object_a_80330BA0", flag={"GLOBL"}),
	#0x80330C20: main.sym("object_a_80330C20", flag={"GLOBL"}),
	#0x80330C38: main.sym("object_a_80330C38", flag={"GLOBL"}),
	#0x80330C48: main.sym("object_a_80330C48", flag={"GLOBL"}),
	#0x80330C58: main.sym("object_a_80330C58", flag={"GLOBL"}),
	#0x80330C68: main.sym("object_a_80330C68", flag={"GLOBL"}),
	#0x80330C74: main.sym("object_a_80330C74", flag={"GLOBL"}),
	#0x80330C84: main.sym("object_a_80330C84", flag={"GLOBL"}),
	#0x80330C98: main.sym("object_a_80330C98", flag={"GLOBL"}),
	#0x80330CB0: main.sym("object_a_80330CB0", flag={"GLOBL"}),
	#0x80330CC4: main.sym("object_a_80330CC4", flag={"GLOBL"}),
	#0x80330CD4: main.sym("object_a_80330CD4", flag={"GLOBL"}),
	#0x80330CE4: main.sym("object_a_80330CE4", flag={"GLOBL"}),
	#0x80330D0C: main.sym("object_a_80330D0C", flag={"GLOBL"}),
	#0x80330D30: main.sym("object_a_80330D30", flag={"GLOBL"}),
	#0x80330D54: main.sym("object_a_80330D54", flag={"GLOBL"}),
	#0x80330D78: main.sym("object_a_80330D78", flag={"GLOBL"}),
	#0x80330D9C: main.sym("object_a_80330D9C", flag={"GLOBL"}),
	#0x80330DAC: main.sym("object_a_80330DAC", flag={"GLOBL"}),

	# src/ride.c
	0x8032FEC0: main.sym("ride_80330E20"),
	0x8032FEC4: main.sym("ride_80330E24"),
	0x8032FED4: main.sym("ride_obj"),

	# src/debug.c
	0x8032FEE0: main.sym("db_edit_effectinfo"),
	0x8032FF04: main.sym("db_edit_enemyinfo"),
	0x8032FF28: main.sym("db_button"),
	0x8032FF2C: main.sym("db_repeat"),
	0x8032FF30: main.sym("db_init_flag"),
	0x8032FF34: main.sym("db_page"),
	0x8032FF38: main.sym("db_hideinfo"),
	0x8032FF3C: main.sym("db_edit_flag"),
	0x8032FF40: main.sym("db_line"),
	0x8032FF44: main.sym("db_info_idx"),
	0x8032FF48: main.sym("db_info_seq"),

	# src/wipe.c
	0x8032FF60: main.sym("wipe_timer"),
	0x8032FF64: main.sym("wipe_ang"),
	0x8032FF68: main.sym("txt_wipe"),

	# src/shadow.c
	0x8032FF80: main.sym("shadow_rect_table"),

	# src/background.c
	0x8032FFA0: main.sym("backtab"),
	0x8032FFC8: main.sym("back_shade"),

	# src/water.c
	0x8032FFD0: main.sym("water_timer"),
	0x8032FFD4: main.sym("water_stamp"),
	0x8032FFD8: main.sym("water_color"),
	0x8032FFDC: main.sym("pool_entry", flag={"GLOBL"}),
	0x8032FFE0: main.sym("pool_flag"),
	0x8032FFE4: main.sym("txt_water"),
	0x80330004: main.sym("fluidtab"),
	0x80330244: main.sym("fluidtabL"),
	0x8033031C: main.sym("fluidtabS"),
	0x80330388: main.sym("water_leveltab"),

	# src/objshape.c
	0x80330390: main.sym("objshape_803312F0"),
	0x80330394: main.sym("objshape_803312F4"),
	0x80330398: main.sym("objshape_803312F8"),

	# src/wave.c
	0x803303A0: main.sym("wavetab0"),
	0x803303A8: main.sym("wavetab1"),
	0x803303E4: main.sym("wavetab2"),
	0x803303EC: main.sym("wavetab"),
	0x803303F8: main.sym("wave_timer"),
	0x803303FC: main.sym("wave_stamp"),

	# src/dprint.c
	0x80330400: main.sym("dprint_index"),

	# src/message.c
	0x80330410: main.sym("msg_state"),
	0x80330414: main.sym("msg_angle"),
	0x80330418: main.sym("msg_scale"),
	0x8033041C: main.sym("msg_scroll"),
	0x80330420: main.sym("msg_type"),
	0x80330424: main.sym("msg_code"),
	0x80330428: main.sym("msg_next"),
	0x8033042C: main.sym("msg_index"),
	0x80330430: main.sym("msg_cursor"),
	0x80330434: main.sym("msg_cursor_flag"),
	0x80330438: main.sym("cursor_status"),
	0x8033043C: main.sym("cursor_timer"),
	0x80330440: main.sym("msg_answer", flag={"GLOBL"}),
	0x80330444: main.sym("str_803314B0"),
	0x80330448: main.sym("str_803314B4"),
	0x8033044C: main.sym("str_803314B8"),
	0x80330450: main.sym("str_803314BC"),
	0x80330454: main.sym("msg_battle"),
	0x80330460: main.sym("msg_fanfare"),
	0x80330468: main.sym("msg_se7_1e"),
	0x80330474: main.sym("msg_bgmstop"),
	0x8033047C: main.sym("menu_code"),
	0x803304F8: main.sym("captiontab"),
	0x80330520: main.sym("demo_alpha"),
	0x80330524: main.sym("caption"),
	0x80330528: main.sym("demo_frame"),
	0x8033052C: main.sym("demo_timer"),
	0x80330530: main.sym("camera_cursor"),
	0x80330534: main.sym("pausemenu_level", flag={"GLOBL"}),
	0x80330538: main.sym("str_80331624"),
	0x8033053C: main.sym("str_8033162C"),
	0x80330544: main.sym("str_80331638"),
	0x80330548: main.sym("str_8033163C"),
	0x8033054C: main.sym("str_80331640"),
	0x80330558: main.sym("str_80331650"),
	0x80330568: main.sym("str_80331660"),
	0x80330574: main.sym("str_80331674"),
	0x80330580: main.sym("str_80331684"),
	0x80330590: main.sym("str_80331690"),
	0x8033059C: main.sym("str_8033169C"),
	0x803305AC: main.sym("str_803316B4"),
	0x803305B4: main.sym("str_803316BC"),
	0x803305B8: main.sym("str_803316C0"),
	0x803305BC: main.sym("str_803316C4"),
	0x803305C0: main.sym("savedemo_end"),
	0x803305C4: main.sym("savedemo_timer"),
	0x803305C8: main.sym("savedemo_coin"),
	0x803305CC: main.sym("savemenu_code", flag={"GLOBL"}),
	0x803305D0: main.sym("str_803316D8"),
	0x803305D8: main.sym("str_803316E4"),
	0x803305E8: main.sym("str_803316F4"),
	0x803305EC: main.sym("str_803316F8"),
	0x803305F0: main.sym("str_803316FC"),
	0x803305F4: main.sym("str_80331704"),
	0x803305F8: main.sym("str_8033170C"),
	0x80330600: main.sym("str_80331714"),
	0x80330608: main.sym("str_80331718"),
	0x80330618: main.sym("str_80331728"),
	0x80330624: main.sym("str_80331734"),

	# src/weather.c
	0x80330640: main.sym("weather_code", flag={"GLOBL"}),
	0x80330648: main.sym("snow_template"),
	0x80330678: main.sym("snow_v0"),
	0x80330680: main.sym("snow_v1"),
	0x80330688: main.sym("snow_v2"),

	# src/lava.c
	0x80330690: main.sym("lava_803317A0"),
	0x80330698: main.sym("lava_template"),

	# src/tag.c
	0x803306D0: main.sym("tagobjtab"),
	0x80331240: main.sym("mapobjtab"),

	# src/hud.c
	0x803314E0: main.sym("meter"),
	0x803314EC: main.sym("hud_timer"),
	0x803314F0: main.sym("hud_80332600"),
	0x803314F4: main.sym("hud_80332604"),
	0x803314F8: main.sym("hud_camera"),

	# src/object_b.c
	#0x80332610: main.sym("object_b_80332610", flag={"GLOBL"}),
	#0x80332614: main.sym("object_b_80332614", flag={"GLOBL"}),
	#0x80332618: main.sym("object_b_80332618", flag={"GLOBL"}),
	#0x8033261C: main.sym("object_b_8033261C", flag={"GLOBL"}),
	#0x80332620: main.sym("object_b_80332620", flag={"GLOBL"}),
	#0x80332624: main.sym("object_b_80332624", flag={"GLOBL"}),
	#0x80332634: main.sym("object_b_80332634", flag={"GLOBL"}),
	#0x80332644: main.sym("object_b_80332644", flag={"GLOBL"}),
	#0x80332654: main.sym("object_b_80332654", flag={"GLOBL"}),
	#0x80332664: main.sym("object_b_80332664", flag={"GLOBL"}),
	#0x80332674: main.sym("object_b_80332674", flag={"GLOBL"}),
	#0x80332684: main.sym("object_b_80332684", flag={"GLOBL"}),
	#0x80332694: main.sym("object_b_80332694", flag={"GLOBL"}),
	#0x803326A4: main.sym("object_b_803326A4", flag={"GLOBL"}),
	#0x803326B4: main.sym("object_b_803326B4", flag={"GLOBL"}),
	#0x803326C4: main.sym("object_b_803326C4", flag={"GLOBL"}),
	#0x80332718: main.sym("object_b_80332718", flag={"GLOBL"}),
	#0x80332764: main.sym("object_b_80332764", flag={"GLOBL"}),
	#0x80332774: main.sym("object_b_80332774", flag={"GLOBL"}),
	#0x80332784: main.sym("object_b_80332784", flag={"GLOBL"}),
	#0x80332794: main.sym("redcoin_hit", flag={"GLOBL"}),
	#0x803327A4: main.sym("object_b_803327A4", flag={"GLOBL"}),
	#0x803327A8: main.sym("object_b_803327A8", flag={"GLOBL"}),
	#0x803327B8: main.sym("object_b_803327B8", flag={"GLOBL"}),
	#0x803327FC: main.sym("object_b_803327FC", flag={"GLOBL"}),
	#0x8033280C: main.sym("object_b_8033280C", flag={"GLOBL"}),
	#0x8033281C: main.sym("object_b_8033281C", flag={"GLOBL"}),
	#0x8033282C: main.sym("object_b_8033282C", flag={"GLOBL"}),

	# src/object_c.c
	#0x80332840: main.sym("object_c_80332840", flag={"GLOBL"}),
	#0x80332850: main.sym("object_c_80332850", flag={"GLOBL"}),
	#0x80332858: main.sym("object_c_80332858", flag={"GLOBL"}),
	#0x80332860: main.sym("object_c_80332860", flag={"GLOBL"}),
	#0x80332880: main.sym("object_c_80332880", flag={"GLOBL"}),
	#0x80332890: main.sym("object_c_80332890", flag={"GLOBL"}),
	#0x80332898: main.sym("object_c_80332898", flag={"GLOBL"}),
	#0x803328A8: main.sym("object_c_803328A8", flag={"GLOBL"}),
	#0x803328B8: main.sym("object_c_803328B8", flag={"GLOBL"}),
	#0x803328C0: main.sym("object_c_803328C0", flag={"GLOBL"}),
	#0x803328D0: main.sym("object_c_803328D0", flag={"GLOBL"}),
	#0x803328F4: main.sym("object_c_803328F4", flag={"GLOBL"}),
	#0x80332900: main.sym("object_c_80332900", flag={"GLOBL"}),
	#0x80332910: main.sym("object_c_80332910", flag={"GLOBL"}),
	#0x80332920: main.sym("object_c_80332920", flag={"GLOBL"}),
	#0x80332930: main.sym("object_c_80332930", flag={"GLOBL"}),
	#0x80332938: main.sym("object_c_80332938", flag={"GLOBL"}),
	#0x80332948: main.sym("object_c_80332948", flag={"GLOBL"}),
	#0x80332954: main.sym("object_c_80332954", flag={"GLOBL"}),
	#0x80332964: main.sym("object_c_80332964", flag={"GLOBL"}),
	#0x8033296C: main.sym("object_c_8033296C", flag={"GLOBL"}),
	#0x8033297C: main.sym("object_c_8033297C", flag={"GLOBL"}),
	#0x80332984: main.sym("object_c_80332984", flag={"GLOBL"}),
	#0x80332998: main.sym("object_c_80332998", flag={"GLOBL"}),
	#0x803329A8: main.sym("object_c_803329A8", flag={"GLOBL"}),
	#0x803329B8: main.sym("object_c_803329B8", flag={"GLOBL"}),
	#0x803329CC: main.sym("object_c_803329CC", flag={"GLOBL"}),
	#0x803329DC: main.sym("object_c_803329DC", flag={"GLOBL"}),
	#0x80332A00: main.sym("object_c_80332A00", flag={"GLOBL"}),
	#0x80332A20: main.sym("object_c_80332A20", flag={"GLOBL"}),
	#0x80332A38: main.sym("object_c_80332A38", flag={"GLOBL"}),
	#0x80332A48: main.sym("object_c_80332A48", flag={"GLOBL"}),
	#0x80332A5C: main.sym("object_c_80332A5C", flag={"GLOBL"}),
	#0x80332A70: main.sym("object_c_80332A70", flag={"GLOBL"}),
	#0x80332A78: main.sym("object_c_80332A78", flag={"GLOBL"}),
	#0x80332A7C: main.sym("object_c_80332A7C", flag={"GLOBL"}),
	#0x80332A8C: main.sym("object_c_80332A8C", flag={"GLOBL"}),
	#0x80332A94: main.sym("object_c_80332A94", flag={"GLOBL"}),
	#0x80332A9C: main.sym("object_c_80332A9C", flag={"GLOBL"}),
	#0x80332AA4: main.sym("object_c_80332AA4", flag={"GLOBL"}),
	#0x80332AA8: main.sym("object_c_80332AA8", flag={"GLOBL"}),
	#0x80332AB0: main.sym("object_c_80332AB0", flag={"GLOBL"}),
	#0x80332AB4: main.sym("object_c_80332AB4", flag={"GLOBL"}),
	#0x80332AB8: main.sym("object_c_80332AB8", flag={"GLOBL"}),
	#0x80332AC0: main.sym("object_c_80332AC0", flag={"GLOBL"}),
	#0x80332AE0: main.sym("object_c_80332AE0", flag={"GLOBL"}),
	#0x80332AE4: main.sym("object_c_80332AE4", flag={"GLOBL"}),
	#0x80332AE8: main.sym("object_c_80332AE8", flag={"GLOBL"}),
	#0x80332AF8: main.sym("object_c_80332AF8", flag={"GLOBL"}),
	#0x80332B00: main.sym("object_c_80332B00", flag={"GLOBL"}),
	#0x80332B10: main.sym("object_c_80332B10", flag={"GLOBL"}),
	#0x80332B24: main.sym("object_c_80332B24", flag={"GLOBL"}),
	#0x80332B34: main.sym("object_c_80332B34", flag={"GLOBL"}),
	#0x80332B54: main.sym("object_c_80332B54", flag={"GLOBL"}),
	#0x80332B5C: main.sym("object_c_80332B5C", flag={"GLOBL"}),
	#0x80332B64: main.sym("object_c_80332B64", flag={"GLOBL"}),
	#0x80332BDC: main.sym("object_c_80332BDC", flag={"GLOBL"}),
	#0x80332BE4: main.sym("object_c_80332BE4", flag={"GLOBL"}),
	#0x80332BF0: main.sym("object_c_80332BF0", flag={"GLOBL"}),
	#0x80332C00: main.sym("object_c_80332C00", flag={"GLOBL"}),
	#0x80332C10: main.sym("object_c_80332C10", flag={"GLOBL"}),
	#0x80332C20: main.sym("object_c_80332C20", flag={"GLOBL"}),
	#0x80332C30: main.sym("object_c_80332C30", flag={"GLOBL"}),
	#0x80332C40: main.sym("object_c_80332C40", flag={"GLOBL"}),
	#0x80332C4C: main.sym("object_c_80332C4C", flag={"GLOBL"}),
	#0x80332C5C: main.sym("object_c_80332C5C", flag={"GLOBL"}),
	#0x80332C6C: main.sym("object_c_80332C6C", flag={"GLOBL"}),
	#0x80332C74: main.sym("object_c_80332C74", flag={"GLOBL"}),
	#0x80332C84: main.sym("object_c_80332C84", flag={"GLOBL"}),
	#0x80332C94: main.sym("object_c_80332C94", flag={"GLOBL"}),
	#0x80332CA4: main.sym("object_c_80332CA4", flag={"GLOBL"}),
	#0x80332CB4: main.sym("object_c_80332CB4", flag={"GLOBL"}),
	#0x80332CBC: main.sym("object_c_80332CBC", flag={"GLOBL"}),
	#0x80332CCC: main.sym("object_c_80332CCC", flag={"GLOBL"}),
	#0x80332CF0: main.sym("object_c_80332CF0", flag={"GLOBL"}),
	#0x80332CF8: main.sym("object_c_80332CF8", flag={"GLOBL"}),
	#0x80332D10: main.sym("object_c_80332D10", flag={"GLOBL"}),
	#0x80332D28: main.sym("object_c_80332D28", flag={"GLOBL"}),
	#0x80332D38: main.sym("object_c_80332D38", flag={"GLOBL"}),
	#0x80332D48: main.sym("object_c_80332D48", flag={"GLOBL"}),
	#0x80332D58: main.sym("object_c_80332D58", flag={"GLOBL"}),
	#0x80332E14: main.sym("object_c_80332E14", flag={"GLOBL"}),
	#0x80332E24: main.sym("object_c_80332E24", flag={"GLOBL"}),
	#0x80332E3C: main.sym("object_c_80332E3C", flag={"GLOBL"}),

	# src/audio/game.c
	#0x80332E50: main.sym("Na_game_80332E50", flag={"GLOBL"}),
	#0x80332E54: main.sym("Na_game_80332E54", flag={"GLOBL"}),
	#0x80332E58: main.sym("Na_MsgSeTable", flag={"GLOBL"}),
	#0x80332F04: main.sym("Na_MsgSeData", flag={"GLOBL"}),
	#0x80332F40: main.sym("Na_game_80332F40", flag={"GLOBL"}),
	#0x80332F44: main.sym("Na_game_80332F44", flag={"GLOBL"}),
	#0x80332F48: main.sym("Na_BgmCtlBBH"),
	#0x80332F54: main.sym("Na_BgmCtlDDD"),
	#0x80332F6C: main.sym("Na_BgmCtlJRB"),
	#0x80332F84: main.sym("Na_BgmCtlSA"),
	#0x80332F88: main.sym("Na_BgmCtlWDW"),
	#0x80332F98: main.sym("Na_BgmCtlHMC"),
	#0x80332FA8: main.sym("Na_BgmCtl38"),
	#0x80332FB8: main.sym("Na_BgmCtlNULL"),
	#0x80332FBC: main.sym("Na_game_80332FBC", flag={"GLOBL"}),
	#0x80332FC0: main.sym("Na_game_80332FC0", flag={"GLOBL"}),
	#0x80332FC4: main.sym("Na_BgmCtlTable", flag={"GLOBL"}),
	#0x80333060: main.sym("Na_BgmCtlData", flag={"GLOBL"}),
	#0x803330C0: main.sym("Na_game_803330C0", flag={"GLOBL"}),
	#0x80333138: main.sym("Na_game_80333138", flag={"GLOBL"}),
	#0x80333188: main.sym("Na_BgmVolTable", flag={"GLOBL"}),
	#0x803331AC: main.sym("Na_game_803331AC", flag={"GLOBL"}),
	#0x803331B0: main.sym("Na_game_803331B0", flag={"GLOBL"}),
	#0x803331B4: main.sym("Na_game_803331B4", flag={"GLOBL"}),
	#0x803331C0: main.sym("Na_game_803331C0", flag={"GLOBL"}),
	#0x803331CC: main.sym("Na_game_803331CC", flag={"GLOBL"}),
	#0x803331D8: main.sym("Na_game_803331D8", flag={"GLOBL"}),
	#0x803331E4: main.sym("Na_game_803331E4", flag={"GLOBL"}),
	0x803320E0: main.sym("Na_0", flag={"GLOBL"}),
	0x803320EC: main.sym("Na_1", flag={"GLOBL"}),
	#0x80333208: main.sym("Na_PortStatus", flag={"GLOBL"}),
	#0x80333214: main.sym("Na_game_80333214", flag={"GLOBL"}),
	#0x80333218: main.sym("Na_game_80333218", flag={"GLOBL"}),
	#0x8033321C: main.sym("Na_game_8033321C", flag={"GLOBL"}),
	#0x80333220: main.sym("Na_game_80333220", flag={"GLOBL"}),
	#0x80333224: main.sym("Na_game_80333224", flag={"GLOBL"}),
	#0x80333228: main.sym("Na_game_80333228", flag={"GLOBL"}),
	#0x8033322C: main.sym("Na_game_8033322C", flag={"GLOBL"}),
	#0x80333230: main.sym("Na_game_80333230", flag={"GLOBL"}),
	#0x80333234: main.sym("Na_game_80333234", flag={"GLOBL"}),
	#0x80333238: main.sym("Na_game_80333238", flag={"GLOBL"}),
	#0x8033323C: main.sym("Na_game_8033323C", flag={"GLOBL"}),
	#0x80333240: main.sym("Na_game_80333240", flag={"GLOBL"}),
	#0x80333280: main.sym("Na_game_80333280", flag={"GLOBL"}),
	#0x80333290: main.sym("Na_game_80333290", flag={"GLOBL"}),

	# src/audio/data.c
	#0x803332A0: main.sym("Na_CfgTable", flag={"GLOBL"}),
	#0x80333498: main.sym("Na_data_80333498", flag={"GLOBL"}),
	#0x80333598: main.sym("Na_data_80333598", flag={"GLOBL"}),
	#0x80333994: main.sym("Na_FreqTable", flag={"GLOBL"}),
	#0x80333B94: main.sym("Na_data_80333B94", flag={"GLOBL"}),
	#0x80333BA4: main.sym("Na_data_80333BA4", flag={"GLOBL"}),
	#0x80333BB4: main.sym("Na_data_80333BB4", flag={"GLOBL"}),
	#0x80333BC4: main.sym("Na_DefaultEnv", flag={"GLOBL"}),
	#0x80333BD0: main.sym("Na_SineWave"),
	#0x80333C50: main.sym("Na_PulseWave"),
	#0x80333CD0: main.sym("Na_TriangleWave"),
	#0x80333D50: main.sym("Na_SawWave"),
	#0x80333DD0: main.sym("Na_WaveTable", flag={"GLOBL"}),
	#0x80333DE0: main.sym("Na_data_80333DE0", flag={"GLOBL"}),
	#0x80333DF4: main.sym("Na_PhonePan", flag={"GLOBL"}),
	#0x80333FF4: main.sym("Na_WidePan", flag={"GLOBL"}),
	#0x803341F4: main.sym("Na_StereoPan", flag={"GLOBL"}),
	#0x803343F4: main.sym("Na_rate_136A", flag={"GLOBL"}),
	#0x803345F4: main.sym("Na_rate_136B", flag={"GLOBL"}),
	#0x803347F4: main.sym("Na_rate_144A", flag={"GLOBL"}),
	#0x803349F4: main.sym("Na_rate_144B", flag={"GLOBL"}),
	#0x80334BF4: main.sym("Na_rate_128A", flag={"GLOBL"}),
	#0x80334DF4: main.sym("Na_rate_128B", flag={"GLOBL"}),
	#0x80334FF4: main.sym("Na_TickRate", flag={"GLOBL"}),
	#0x80334FF8: main.sym("Na_data_80334FF8", flag={"GLOBL"}),
	#0x80334FFC: main.sym("Na_HeapSize", flag={"GLOBL"}),
	#0x80335000: main.sym("Na_data_80335000", flag={"GLOBL"}),
	#0x80335004: main.sym("Na_data_80335004", flag={"GLOBL"}),
	#0x80335008: main.sym("Na_data_80335008", flag={"GLOBL"}),

	# libultra
	0x80333F00: main.sym("osViModeTable"),
	0x803347C0: main.sym("__osViDevMgr"),
	0x803347E0: main.sym("__osPiDevMgr"),
	0x80365DA0: main.sym("osClockRate"),
	0x80334808: main.sym("__osShutdown"),
	0x80334810: main.sym("__osContinitialized"),
	0x80334820: main.sym("hdwrBugFlag"),
	0x80334830: main.sym("__osTimerList"),
	0x80334840: main.sym("spaces"),
	0x80334864: main.sym("zeroes"),
	0x80334890: main.sym("__osThreadTail"),
	0x80334898: main.sym("__osRunQueue"),
	0x8033489C: main.sym("__osActiveQueue"),
	0x803348A0: main.sym("__osRunningThread"),
	0x803348A4: main.sym("__osFaultedThread"),
	0x803348B0: main.sym("vi"),
	0x80334910: main.sym("__osViCurr"),
	0x80334914: main.sym("__osViNext"),
	0x80334918: main.sym("osViNtscEnabled"),
	0x8033491C: main.sym("osViClock"),
	0x80334920: main.sym("__osHwIntTable"),
	0x80334934: main.sym("__osIsRdbWrite"),
	0x80334938: main.sym("__osIsRdbRead"),
	0x80334940: main.sym("__osPiAccessQueueEnabled"),
	0x80334950: main.sym("__osSiAccessQueueEnabled"),
	0x80334960: main.sym("ldigs"),
	0x80334974: main.sym("udigs"),
	0x80334990: main.sym("osViModeNtscLan1"),
	0x803349E0: main.sym("osViModePalLan1"),
	0x80334A30: main.sym("debug_state"),
	0x80334A34: main.sym("numChars"),
	0x80334A38: main.sym("numCharsToReceive"),
	0x80334A40: main.sym("__osRdbSendMessage"),
	0x80334A44: main.sym("__osRdbWriteOK"),

	# ==========================================================================
	# rodata
	# ==========================================================================

	# src/main.c
	0x80334A50: main.sym("main_80335B60"),

	# src/graphics.c
	0x80334A70: main.sym("str_gfx_buf"),

	# src/audio.c
	0x80334A80: main.sym("audio_80335B90"),

	# src/game.c
	#0x80335BA0: main.sym("str_01_0"),
	#0x80335BB0: main.sym("str_01_1"),
	#0x80335BC4: main.sym("str_02_0"),
	#0x80335BDC: main.sym("str_02_1"),
	#0x80335BF0: main.sym("str_02_2"),
	#0x80335C00: main.sym("str_03_0"),
	#0x80335C14: main.sym("str_03_1"),
	#0x80335C28: main.sym("str_03_2"),
	#0x80335C3C: main.sym("str_04_0"),
	#0x80335C4C: main.sym("str_04_1"),
	#0x80335C5C: main.sym("str_04_2"),
	#0x80335C6C: main.sym("str_04_3"),
	#0x80335C7C: main.sym("str_05_0"),
	#0x80335C90: main.sym("str_05_1"),
	#0x80335CA8: main.sym("str_05_2"),
	#0x80335CB8: main.sym("str_05_3"),
	#0x80335CC8: main.sym("str_06_0"),
	#0x80335CDC: main.sym("str_06_1"),
	#0x80335CEC: main.sym("str_06_2"),
	#0x80335D00: main.sym("str_07_0"),
	#0x80335D14: main.sym("str_07_1"),
	#0x80335D20: main.sym("str_07_2"),
	#0x80335D2C: main.sym("str_08_0"),
	#0x80335D40: main.sym("str_08_1"),
	#0x80335D54: main.sym("str_08_2"),
	#0x80335D64: main.sym("str_08_3"),
	#0x80335D74: main.sym("str_09_0"),
	#0x80335D84: main.sym("str_09_1"),
	#0x80335D90: main.sym("str_10_0"),
	#0x80335DA0: main.sym("str_10_1"),
	#0x80335DB4: main.sym("str_10_2"),
	#0x80335DC4: main.sym("str_10_3"),
	#0x80335DD4: main.sym("str_11_0"),
	#0x80335DE4: main.sym("str_11_1"),
	#0x80335DF8: main.sym("str_11_2"),
	#0x80335E08: main.sym("str_12_0"),
	#0x80335E20: main.sym("str_12_1"),
	#0x80335E30: main.sym("str_13_0"),
	#0x80335E44: main.sym("str_13_1"),
	#0x80335E54: main.sym("str_13_2"),
	#0x80335E68: main.sym("str_13_3"),
	#0x80335E74: main.sym("str_14_0"),
	#0x80335E88: main.sym("str_14_1"),
	#0x80335EA0: main.sym("str_15_0"),
	#0x80335EB8: main.sym("str_15_1"),
	#0x80335EC8: main.sym("str_15_2"),
	#0x80335ED4: main.sym("str_16_0"),
	#0x80335EE8: main.sym("str_16_1"),
	#0x80335EF4: main.sym("str_16_2"),
	#0x80335F00: main.sym("str_16_3"),
	#0x80335F0C: main.sym("str_16_4"),
	#0x80335F18: main.sym("str_17_0"),
	#0x80335F28: main.sym("str_17_1"),
	#0x80335F34: main.sym("str_17_2"),
	#0x80335F48: main.sym("str_17_3"),
	#0x80335F54: main.sym("str_18_0"),
	#0x80335F68: main.sym("str_18_1"),
	#0x80335F74: main.sym("str_18_2"),
	#0x80335F8C: main.sym("str_18_3"),
	#0x80335FA0: main.sym("str_19_0"),
	#0x80335FAC: main.sym("str_19_1"),
	#0x80335FC0: main.sym("str_20_0"),
	#0x80335FD4: main.sym("str_20_1"),
	0x80334E4C: main.sym("game_80335FE8"),
	0x80334EE0: main.sym("game_8033607C"),
	0x80334F7C: main.sym("game_80336118"),
	0x80334FE0: main.sym("game_8033617C"),
	0x80334FF4: main.sym("game_80336190"),

	# src/collision.c
	0x80335010: main.sym("collision_803361B0"),
	0x80335090: main.sym("collision_80336230"),
	0x80335158: main.sym("collision_803362F8"),
	0x80335270: main.sym("collision_80336410"),
	0x80335274: main.sym("collision_80336414"),
	0x80335278: main.sym("collision_80336418"),

	# src/player.c
	0x80335280: main.sym("str_player_ang"),
	0x80335288: main.sym("str_player_spd"),
	0x80335290: main.sym("str_player_sta"),
	0x80335298: main.sym("player_80336438"),
	0x803352B8: main.sym("player_80336458"),
	0x8033534C: main.sym("player_803364EC"),
	0x8033536C: main.sym("player_8033650C"),
	0x80335400: main.sym("player_803365A0"),
	0x80335404: main.sym("player_803365A4"),
	0x80335408: main.sym("player_803365A8"),
	0x8033540C: main.sym("player_803365AC"),
	0x80335410: main.sym("player_803365B0"),
	0x80335414: main.sym("player_803365B4"),
	0x80335418: main.sym("player_803365B8"),
	0x8033541C: main.sym("player_803365BC"),
	0x80335420: main.sym("player_803365C0"),
	0x80335424: main.sym("player_803365C4"),
	0x80335428: main.sym("player_803365C8"),
	0x8033542C: main.sym("player_803365CC"),
	0x80335430: main.sym("player_803365D0"),
	0x80335434: main.sym("player_803365D4"),
	0x803354B8: main.sym("player_80336658"),
	0x803354BC: main.sym("player_8033665C"),
	0x803354C0: main.sym("player_80336660"),
	0x803354C4: main.sym("player_80336664"),
	0x803354C8: main.sym("player_80336668"),

	# src/physics.c
	0x803354D0: main.sym("physics_80336670"),
	0x803354D4: main.sym("physics_80336674"),
	0x803354D8: main.sym("physics_80336678"),
	0x8033550C: main.sym("physics_803366AC"),
	0x80335510: main.sym("physics_803366B0"),
	0x80335514: main.sym("physics_803366B4"),
	0x80335518: main.sym("physics_803366B8"),
	0x8033551C: main.sym("physics_803366BC"),
	0x80335520: main.sym("physics_803366C0"),

	# src/pldemo.c
	0x80335530: main.sym("pldemo_803366D0"),
	#0x803366D4: main.sym("pldemo_803366D4"),
	#0x803366E8: main.sym("pldemo_803366E8"),
	#0x803366EC: main.sym("pldemo_803366EC"),
	#0x80336708: main.sym("pldemo_80336708"),
	#0x8033670C: main.sym("pldemo_8033670C"),
	#0x80336710: main.sym("pldemo_80336710"),
	#0x80336714: main.sym("pldemo_80336714"),
	#0x80336718: main.sym("pldemo_80336718"),
	#0x8033671C: main.sym("pldemo_8033671C"),
	#0x80336720: main.sym("pldemo_80336720"),
	#0x80336754: main.sym("pldemo_80336754"),
	#0x80336770: main.sym("pldemo_80336770"),
	#0x80336784: main.sym("pldemo_80336784"),
	#0x80336848: main.sym("pldemo_80336848"),

	# src/plspec.c
	#0x80336940: main.sym("plspec_80336940"),
	#0x80336944: main.sym("plspec_80336944"),
	#0x80336948: main.sym("plspec_80336948"),
	#0x8033694C: main.sym("plspec_8033694C"),
	#0x80336950: main.sym("plspec_80336950"),

	# src/plwait.c
	#0x80336970: main.sym("plwait_80336970"),
	#0x80336974: main.sym("plwait_80336974"),
	#0x80336978: main.sym("plwait_80336978"),
	#0x803369A4: main.sym("plwait_803369A4"),
	#0x803369B8: main.sym("plwait_803369B8"),
	#0x80336A18: main.sym("plwait_80336A18"),

	# src/plmove.c
	#0x80336A80: main.sym("plmove_80336A80"),
	#0x80336A84: main.sym("plmove_80336A84"),
	#0x80336A88: main.sym("plmove_80336A88"),
	#0x80336A8C: main.sym("plmove_80336A8C"),
	#0x80336A90: main.sym("plmove_80336A90"),
	#0x80336A94: main.sym("plmove_80336A94"),
	#0x80336A98: main.sym("plmove_80336A98"),
	#0x80336A9C: main.sym("plmove_80336A9C"),
	#0x80336AA0: main.sym("plmove_80336AA0"),
	#0x80336AA4: main.sym("plmove_80336AA4"),
	#0x80336AA8: main.sym("plmove_80336AA8"),
	#0x80336AAC: main.sym("plmove_80336AAC"),
	#0x80336AB0: main.sym("plmove_80336AB0"),
	#0x80336AB4: main.sym("plmove_80336AB4"),
	#0x80336AB8: main.sym("plmove_80336AB8"),
	#0x80336ABC: main.sym("plmove_80336ABC"),
	#0x80336AC0: main.sym("plmove_80336AC0"),
	#0x80336AC4: main.sym("plmove_80336AC4"),
	#0x80336AC8: main.sym("plmove_80336AC8"),
	#0x80336ACC: main.sym("plmove_80336ACC"),
	#0x80336AD0: main.sym("plmove_80336AD0"),
	#0x80336AD4: main.sym("plmove_80336AD4"),
	#0x80336AD8: main.sym("plmove_80336AD8"),
	#0x80336ADC: main.sym("plmove_80336ADC"),
	#0x80336AE0: main.sym("plmove_80336AE0"),
	#0x80336AE4: main.sym("plmove_80336AE4"),
	#0x80336AE8: main.sym("plmove_80336AE8"),
	#0x80336AEC: main.sym("plmove_80336AEC"),
	#0x80336AF0: main.sym("plmove_80336AF0"),
	#0x80336AF8: main.sym("plmove_80336AF8"),
	#0x80336B00: main.sym("plmove_80336B00"),
	#0x80336B04: main.sym("plmove_80336B04"),
	#0x80336B08: main.sym("plmove_80336B08"),
	#0x80336B0C: main.sym("plmove_80336B0C"),
	#0x80336B38: main.sym("plmove_80336B38"),
	#0x80336BB4: main.sym("plmove_80336BB4"),
	#0x80336BCC: main.sym("plmove_80336BCC"),

	# src/pljump.c
	#0x80336C00: main.sym("pljump_80336C00"),
	#0x80336C04: main.sym("pljump_80336C04"),
	#0x80336C08: main.sym("pljump_80336C08"),
	#0x80336C0C: main.sym("pljump_80336C0C"),
	#0x80336C10: main.sym("pljump_80336C10"),
	#0x80336C14: main.sym("pljump_80336C14"),
	#0x80336C18: main.sym("pljump_80336C18"),
	#0x80336C1C: main.sym("pljump_80336C1C"),
	#0x80336C38: main.sym("pljump_80336C38"),
	#0x80336C3C: main.sym("pljump_80336C3C"),
	#0x80336C40: main.sym("pljump_80336C40"),
	#0x80336C44: main.sym("pljump_80336C44"),
	#0x80336C48: main.sym("pljump_80336C48"),
	#0x80336C4C: main.sym("pljump_80336C4C"),
	#0x80336C50: main.sym("pljump_80336C50"),
	#0x80336C54: main.sym("pljump_80336C54"),
	#0x80336C58: main.sym("pljump_80336C58"),
	#0x80336C60: main.sym("pljump_80336C60"),
	#0x80336D20: main.sym("pljump_80336D20"),
	#0x80336D5C: main.sym("pljump_80336D5C"),

	# src/plswim.c
	#0x80336E10: main.sym("plswim_80336E10"),
	#0x80336E14: main.sym("plswim_80336E14"),
	#0x80336E2C: main.sym("plswim_80336E2C"),
	#0x80336E44: main.sym("plswim_80336E44"),
	#0x80336E48: main.sym("plswim_80336E48"),
	#0x80336E4C: main.sym("plswim_80336E4C"),
	#0x80336E50: main.sym("plswim_80336E50"),
	#0x80336E54: main.sym("plswim_80336E54"),
	#0x80336E58: main.sym("plswim_80336E58"),
	#0x80336E5C: main.sym("plswim_80336E5C"),
	#0x80336EA4: main.sym("plswim_80336EA4"),

	# src/pltake.c
	#0x80336ED0: main.sym("pltake_80336ED0"),
	#0x80336EF8: main.sym("pltake_80336EF8"),

	# src/callback.c
	0x80335DA0: main.sym("callback_80336F40"),
	0x80335DB4: main.sym("callback_80336F54"),
	0x80335DB8: main.sym("callback_80336F58"),
	0x80335DC0: main.sym("callback_80336F60"),
	0x80335DC8: main.sym("callback_80336F68"),

	# src/scene.c
	0x80335DD0: main.sym("str_scene_no_controller"),
	0x80335DE0: main.sym("str_scene_press"),
	0x80335DE8: main.sym("str_scene_start"),

	# src/draw.c
	0x80335DF0: main.sym("str_draw_mem"),
	0x80335DF8: main.sym("draw_80336F98"),
	0x80335DFC: main.sym("draw_80336F9C"),
	0x80335EAC: main.sym("draw_8033704C"),

	# src/camera.c
	#0x803370F0: main.sym("camera_803370F0"),
	#0x80337118: main.sym("camera_80337118"),
	#0x8033711C: main.sym("camera_8033711C"),
	#0x80337120: main.sym("camera_80337120"),
	#0x80337148: main.sym("camera_80337148"),
	#0x8033714C: main.sym("camera_8033714C"),
	#0x80337150: main.sym("camera_80337150"),
	#0x80337154: main.sym("camera_80337154"),
	#0x80337158: main.sym("camera_80337158"),
	#0x8033715C: main.sym("camera_8033715C"),
	#0x80337160: main.sym("camera_80337160"),
	#0x80337164: main.sym("camera_80337164"),
	#0x80337168: main.sym("camera_80337168"),
	#0x8033716C: main.sym("camera_8033716C"),
	#0x80337170: main.sym("camera_80337170"),
	#0x80337174: main.sym("camera_80337174"),
	#0x80337178: main.sym("camera_80337178"),
	#0x8033717C: main.sym("camera_8033717C"),
	#0x80337180: main.sym("camera_80337180"),
	#0x80337184: main.sym("camera_80337184"),
	#0x80337188: main.sym("camera_80337188"),
	#0x8033718C: main.sym("camera_8033718C"),
	#0x80337190: main.sym("camera_80337190"),
	#0x80337194: main.sym("camera_80337194"),
	#0x80337198: main.sym("camera_80337198"),
	#0x8033719C: main.sym("camera_8033719C"),
	#0x803371A0: main.sym("camera_803371A0"),
	#0x803371A4: main.sym("camera_803371A4"),
	#0x803371A8: main.sym("camera_803371A8"),
	#0x803371AC: main.sym("camera_803371AC"),
	#0x803371B0: main.sym("camera_803371B0"),
	#0x803371B4: main.sym("camera_803371B4"),
	#0x803371B8: main.sym("camera_803371B8"),
	#0x803371BC: main.sym("camera_803371BC"),
	#0x803371C0: main.sym("camera_803371C0"),
	#0x803371C4: main.sym("camera_803371C4"),
	#0x803371C8: main.sym("camera_803371C8"),
	#0x803371CC: main.sym("camera_803371CC"),
	#0x803371D0: main.sym("camera_803371D0"),
	#0x803371D4: main.sym("camera_803371D4"),
	#0x803371D8: main.sym("camera_803371D8"),
	#0x803371DC: main.sym("camera_803371DC"),
	#0x803371E0: main.sym("camera_803371E0"),
	#0x803371E4: main.sym("camera_803371E4"),
	#0x803371E8: main.sym("camera_803371E8"),
	#0x803371EC: main.sym("camera_803371EC"),
	#0x803371F0: main.sym("camera_803371F0"),
	#0x803371F4: main.sym("camera_803371F4"),
	#0x803371F8: main.sym("camera_803371F8"),
	#0x803371FC: main.sym("camera_803371FC"),
	#0x80337200: main.sym("camera_80337200"),
	#0x80337204: main.sym("camera_80337204"),
	#0x80337208: main.sym("camera_80337208"),
	#0x8033720C: main.sym("camera_8033720C"),
	#0x80337210: main.sym("camera_80337210"),
	#0x80337214: main.sym("camera_80337214"),
	#0x80337218: main.sym("camera_80337218"),
	#0x8033725C: main.sym("camera_8033725C"),
	#0x80337260: main.sym("camera_80337260"),
	#0x80337264: main.sym("camera_80337264"),
	#0x80337268: main.sym("camera_80337268"),
	#0x8033726C: main.sym("camera_8033726C"),
	#0x803372E0: main.sym("camera_803372E0"),
	#0x803372E4: main.sym("camera_803372E4"),
	#0x803372E8: main.sym("camera_803372E8"),
	#0x803372EC: main.sym("camera_803372EC"),
	#0x803372F0: main.sym("camera_803372F0"),
	#0x803372F4: main.sym("camera_803372F4"),
	#0x803372F8: main.sym("camera_803372F8"),
	#0x803372FC: main.sym("camera_803372FC"),
	#0x80337300: main.sym("camera_80337300"),
	#0x80337304: main.sym("camera_80337304"),
	#0x8033731C: main.sym("camera_8033731C"),
	#0x80337320: main.sym("camera_80337320"),
	#0x80337324: main.sym("camera_80337324"),
	#0x80337328: main.sym("camera_80337328"),
	#0x8033732C: main.sym("camera_8033732C"),
	#0x80337330: main.sym("camera_80337330"),
	#0x80337334: main.sym("camera_80337334"),
	#0x80337338: main.sym("camera_80337338"),
	#0x8033733C: main.sym("camera_8033733C"),
	#0x80337354: main.sym("camera_80337354"),
	#0x80337368: main.sym("camera_80337368"),
	#0x8033736C: main.sym("camera_8033736C"),
	#0x80337370: main.sym("camera_80337370"),
	#0x80337374: main.sym("camera_80337374"),
	#0x80337378: main.sym("camera_80337378"),
	#0x8033737C: main.sym("camera_8033737C"),
	#0x80337380: main.sym("camera_80337380"),
	#0x80337384: main.sym("camera_80337384"),
	#0x80337388: main.sym("camera_80337388"),
	#0x8033738C: main.sym("camera_8033738C"),
	#0x80337390: main.sym("camera_80337390"),
	#0x80337394: main.sym("camera_80337394"),
	#0x80337398: main.sym("camera_80337398"),
	#0x8033739C: main.sym("camera_8033739C"),
	#0x803373A0: main.sym("camera_803373A0"),
	#0x803373A4: main.sym("camera_803373A4"),
	#0x803373A8: main.sym("camera_803373A8"),
	#0x803373AC: main.sym("camera_803373AC"),
	#0x803373B0: main.sym("camera_803373B0"),
	#0x803373B4: main.sym("camera_803373B4"),
	#0x803373B8: main.sym("camera_803373B8"),
	#0x803373BC: main.sym("camera_803373BC"),
	#0x803373C0: main.sym("camera_803373C0"),
	#0x803373C4: main.sym("camera_803373C4"),
	#0x803373C8: main.sym("camera_803373C8"),
	#0x803373CC: main.sym("camera_803373CC"),
	#0x803373D0: main.sym("camera_803373D0"),
	#0x803373D4: main.sym("camera_803373D4"),
	#0x803373D8: main.sym("camera_803373D8"),
	#0x803373DC: main.sym("camera_803373DC"),
	#0x803373E0: main.sym("camera_803373E0"),
	#0x803373E4: main.sym("camera_803373E4"),
	#0x803373E8: main.sym("camera_803373E8"),
	#0x803373EC: main.sym("camera_803373EC"),
	#0x803373F0: main.sym("camera_803373F0"),
	#0x803373F4: main.sym("camera_803373F4"),
	#0x803373F8: main.sym("camera_803373F8"),
	#0x803373FC: main.sym("camera_803373FC"),
	#0x80337400: main.sym("camera_80337400"),
	#0x80337404: main.sym("camera_80337404"),
	#0x80337408: main.sym("camera_80337408"),
	#0x8033740C: main.sym("camera_8033740C"),
	#0x80337410: main.sym("camera_80337410"),
	#0x80337414: main.sym("camera_80337414"),
	#0x80337418: main.sym("camera_80337418"),
	#0x8033741C: main.sym("camera_8033741C"),
	#0x80337420: main.sym("camera_80337420"),
	#0x80337424: main.sym("camera_80337424"),
	#0x80337428: main.sym("camera_80337428"),
	#0x8033742C: main.sym("camera_8033742C"),
	#0x80337430: main.sym("camera_80337430"),
	#0x80337434: main.sym("camera_80337434"),
	#0x80337438: main.sym("camera_80337438"),
	#0x8033743C: main.sym("camera_8033743C"),
	#0x80337440: main.sym("camera_80337440"),
	#0x80337644: main.sym("camera_80337644"),
	#0x80337648: main.sym("camera_80337648"),
	#0x8033764C: main.sym("camera_8033764C"),
	#0x80337650: main.sym("camera_80337650"),
	#0x80337654: main.sym("camera_80337654"),
	#0x80337658: main.sym("camera_80337658"),
	#0x8033765C: main.sym("camera_8033765C"),
	#0x80337660: main.sym("camera_80337660"),
	#0x80337664: main.sym("camera_80337664"),
	#0x80337668: main.sym("camera_80337668"),
	#0x80337738: main.sym("camera_80337738"),
	#0x8033776C: main.sym("camera_8033776C"),
	#0x80337770: main.sym("camera_80337770"),
	#0x80337774: main.sym("camera_80337774"),
	#0x80337778: main.sym("camera_80337778"),
	#0x8033777C: main.sym("camera_8033777C"),
	#0x80337780: main.sym("camera_80337780"),

	# src/object.c
	0x80336600: main.sym("object_803377A0"),
	0x80336608: main.sym("object_803377A8"),

	# src/objectlib.c
	#0x803377B0: main.sym("str_objectlib_areainfo"),
	#0x803377BC: main.sym("objectlib_803377BC"),
	#0x803377C0: main.sym("objectlib_803377C0"),
	#0x803377C4: main.sym("objectlib_803377C4"),
	#0x803377C8: main.sym("objectlib_803377C8"),
	#0x803377CC: main.sym("objectlib_803377CC"),
	#0x803377D0: main.sym("objectlib_803377D0"),
	#0x803377D8: main.sym("objectlib_803377D8"),
	#0x803377E0: main.sym("objectlib_803377E0"),
	#0x803377E8: main.sym("objectlib_803377E8"),
	#0x803377F0: main.sym("objectlib_803377F0"),
	#0x803377F4: main.sym("objectlib_803377F4"),
	#0x803377F8: main.sym("objectlib_803377F8"),
	#0x80337800: main.sym("objectlib_80337800"),
	#0x80337808: main.sym("objectlib_80337808"),
	#0x80337810: main.sym("objectlib_80337810"),
	#0x80337814: main.sym("objectlib_80337814"),
	#0x80337818: main.sym("objectlib_80337818"),
	#0x8033781C: main.sym("objectlib_8033781C"),
	#0x80337820: main.sym("objectlib_80337820"),
	#0x80337824: main.sym("objectlib_80337824"),
	#0x80337828: main.sym("objectlib_80337828"),
	#0x8033782C: main.sym("objectlib_8033782C"),
	#0x80337830: main.sym("objectlib_80337830"),
	#0x80337834: main.sym("objectlib_80337834"),

	# src/object_a.c
	#0x80337850: main.sym("str_object_a_0_fmt"),
	#0x80337854: main.sym("str_object_a_0_fg"),
	#0x8033785C: main.sym("str_object_a_0_sp"),
	#0x80337864: main.sym("str_object_a_1_fmt"),
	#0x80337868: main.sym("str_object_a_1_md"),
	#0x80337870: main.sym("str_object_a_1_sp"),
	#0x80337878: main.sym("str_object_a_mode"),
	#0x80337884: main.sym("str_object_a_action"),
	#0x80337890: main.sym("str_object_a_number"),
	#0x8033789C: main.sym("str_object_a_off"),
	#0x803378A4: main.sym("str_object_a_x"),
	#0x803378AC: main.sym("str_object_a_z"),
	#0x803378B4: main.sym("object_a_803378B4"),
	#0x803378C8: main.sym("object_a_803378C8"),
	#0x803378D0: main.sym("object_a_803378D0"),
	#0x803378D8: main.sym("object_a_803378D8"),
	#0x803378E0: main.sym("object_a_803378E0"),
	#0x803378E8: main.sym("object_a_803378E8"),
	#0x803378F0: main.sym("object_a_803378F0"),
	#0x803378F4: main.sym("object_a_803378F4"),
	#0x803378F8: main.sym("object_a_803378F8"),
	#0x803378FC: main.sym("object_a_803378FC"),
	#0x80337900: main.sym("object_a_80337900"),
	#0x80337904: main.sym("object_a_80337904"),
	#0x80337918: main.sym("object_a_80337918"),
	#0x80337920: main.sym("object_a_80337920"),
	#0x80337928: main.sym("object_a_80337928"),
	#0x80337930: main.sym("object_a_80337930"),
	#0x80337938: main.sym("object_a_80337938"),
	#0x80337940: main.sym("object_a_80337940"),
	#0x80337944: main.sym("object_a_80337944"),
	#0x80337948: main.sym("object_a_80337948"),
	#0x8033794C: main.sym("object_a_8033794C"),
	#0x80337950: main.sym("object_a_80337950"),
	#0x80337958: main.sym("object_a_80337958"),
	#0x80337960: main.sym("object_a_80337960"),
	#0x80337968: main.sym("object_a_80337968"),
	#0x80337970: main.sym("object_a_80337970"),
	#0x80337974: main.sym("object_a_80337974"),
	#0x80337988: main.sym("object_a_80337988"),
	#0x80337990: main.sym("object_a_80337990"),
	#0x80337994: main.sym("object_a_80337994"),
	#0x80337998: main.sym("object_a_80337998"),
	#0x8033799C: main.sym("object_a_8033799C"),
	#0x803379A0: main.sym("object_a_803379A0"),
	#0x803379A4: main.sym("object_a_803379A4"),
	#0x803379A8: main.sym("object_a_803379A8"),
	#0x803379AC: main.sym("object_a_803379AC"),
	#0x803379B0: main.sym("object_a_803379B0"),
	#0x803379B4: main.sym("object_a_803379B4"),
	#0x803379C8: main.sym("object_a_803379C8"),
	#0x803379D0: main.sym("object_a_803379D0"),
	#0x803379D8: main.sym("object_a_803379D8"),
	#0x803379E0: main.sym("object_a_803379E0"),
	#0x803379E8: main.sym("object_a_803379E8"),
	#0x803379F0: main.sym("object_a_803379F0"),
	#0x803379F8: main.sym("object_a_803379F8"),
	#0x80337A20: main.sym("object_a_80337A20"),
	#0x80337A28: main.sym("object_a_80337A28"),
	#0x80337A30: main.sym("object_a_80337A30"),
	#0x80337A38: main.sym("object_a_80337A38"),
	#0x80337A40: main.sym("object_a_80337A40"),
	#0x80337A54: main.sym("object_a_80337A54"),
	#0x80337A68: main.sym("object_a_80337A68"),
	#0x80337A70: main.sym("object_a_80337A70"),
	#0x80337A78: main.sym("object_a_80337A78"),
	#0x80337A7C: main.sym("object_a_80337A7C"),
	#0x80337A80: main.sym("object_a_80337A80"),
	#0x80337A84: main.sym("object_a_80337A84"),
	#0x80337A88: main.sym("object_a_80337A88"),
	#0x80337A8C: main.sym("object_a_80337A8C"),
	#0x80337A90: main.sym("object_a_80337A90"),
	#0x80337A98: main.sym("object_a_80337A98"),
	#0x80337AAC: main.sym("object_a_80337AAC"),
	#0x80337AB0: main.sym("object_a_80337AB0"),
	#0x80337AB8: main.sym("object_a_80337AB8"),
	#0x80337AC0: main.sym("object_a_80337AC0"),
	#0x80337AC4: main.sym("object_a_80337AC4"),
	#0x80337AC8: main.sym("object_a_80337AC8"),
	#0x80337AD0: main.sym("object_a_80337AD0"),
	#0x80337AD8: main.sym("object_a_80337AD8"),
	#0x80337ADC: main.sym("object_a_80337ADC"),
	#0x80337AE0: main.sym("object_a_80337AE0"),
	#0x80337AE8: main.sym("object_a_80337AE8"),
	#0x80337AF0: main.sym("object_a_80337AF0"),
	#0x80337AF8: main.sym("object_a_80337AF8"),
	#0x80337B00: main.sym("object_a_80337B00"),
	#0x80337B08: main.sym("object_a_80337B08"),
	#0x80337B38: main.sym("object_a_80337B38"),
	#0x80337B40: main.sym("object_a_80337B40"),
	#0x80337B48: main.sym("object_a_80337B48"),
	#0x80337B4C: main.sym("object_a_80337B4C"),
	#0x80337B74: main.sym("object_a_80337B74"),
	#0x80337B78: main.sym("object_a_80337B78"),
	#0x80337B80: main.sym("object_a_80337B80"),
	#0x80337B88: main.sym("object_a_80337B88"),
	#0x80337B90: main.sym("object_a_80337B90"),
	#0x80337BA4: main.sym("object_a_80337BA4"),
	#0x80337BBC: main.sym("object_a_80337BBC"),
	#0x80337BC0: main.sym("object_a_80337BC0"),
	#0x80337BC4: main.sym("object_a_80337BC4"),
	#0x80337BC8: main.sym("object_a_80337BC8"),
	#0x80337BD0: main.sym("object_a_80337BD0"),
	#0x80337BD8: main.sym("object_a_80337BD8"),
	#0x80337BDC: main.sym("object_a_80337BDC"),
	#0x80337BE0: main.sym("object_a_80337BE0"),
	#0x80337BE4: main.sym("object_a_80337BE4"),
	#0x80337BE8: main.sym("object_a_80337BE8"),
	#0x80337BF0: main.sym("object_a_80337BF0"),
	#0x80337BF4: main.sym("object_a_80337BF4"),
	#0x80337BF8: main.sym("object_a_80337BF8"),
	#0x80337C00: main.sym("object_a_80337C00"),
	#0x80337C04: main.sym("object_a_80337C04"),
	#0x80337C08: main.sym("object_a_80337C08"),
	#0x80337C0C: main.sym("object_a_80337C0C"),
	#0x80337C10: main.sym("object_a_80337C10"),
	#0x80337C30: main.sym("object_a_80337C30"),
	#0x80337C34: main.sym("object_a_80337C34"),
	#0x80337C54: main.sym("object_a_80337C54"),
	#0x80337C58: main.sym("object_a_80337C58"),
	#0x80337C5C: main.sym("object_a_80337C5C"),
	#0x80337C60: main.sym("object_a_80337C60"),
	#0x80337C64: main.sym("object_a_80337C64"),
	#0x80337C68: main.sym("object_a_80337C68"),
	#0x80337C70: main.sym("object_a_80337C70"),
	#0x80337C84: main.sym("object_a_80337C84"),
	#0x80337C88: main.sym("object_a_80337C88"),
	#0x80337C90: main.sym("object_a_80337C90"),
	#0x80337C98: main.sym("object_a_80337C98"),
	#0x80337CA0: main.sym("object_a_80337CA0"),
	#0x80337CA8: main.sym("object_a_80337CA8"),
	#0x80337CB0: main.sym("object_a_80337CB0"),
	#0x80337CB8: main.sym("object_a_80337CB8"),
	#0x80337CBC: main.sym("object_a_80337CBC"),
	#0x80337CC0: main.sym("object_a_80337CC0"),
	#0x80337CC4: main.sym("object_a_80337CC4"),
	#0x80337CC8: main.sym("object_a_80337CC8"),
	#0x80337CCC: main.sym("object_a_80337CCC"),
	#0x80337CD0: main.sym("object_a_80337CD0"),
	#0x80337CD4: main.sym("object_a_80337CD4"),
	#0x80337CD8: main.sym("object_a_80337CD8"),
	#0x80337CE0: main.sym("object_a_80337CE0"),
	#0x80337CE8: main.sym("object_a_80337CE8"),
	#0x80337CF0: main.sym("object_a_80337CF0"),
	#0x80337CF4: main.sym("object_a_80337CF4"),
	#0x80337CF8: main.sym("object_a_80337CF8"),
	#0x80337D00: main.sym("object_a_80337D00"),
	#0x80337D04: main.sym("object_a_80337D04"),
	#0x80337D08: main.sym("object_a_80337D08"),
	#0x80337D10: main.sym("object_a_80337D10"),
	#0x80337D18: main.sym("object_a_80337D18"),
	#0x80337D20: main.sym("object_a_80337D20"),
	#0x80337D28: main.sym("object_a_80337D28"),
	#0x80337D30: main.sym("object_a_80337D30"),
	#0x80337D38: main.sym("object_a_80337D38"),
	#0x80337D3C: main.sym("object_a_80337D3C"),
	#0x80337D40: main.sym("object_a_80337D40"),
	#0x80337D44: main.sym("object_a_80337D44"),
	#0x80337D48: main.sym("object_a_80337D48"),
	#0x80337D50: main.sym("object_a_80337D50"),
	#0x80337D58: main.sym("object_a_80337D58"),
	#0x80337D60: main.sym("object_a_80337D60"),
	#0x80337D68: main.sym("object_a_80337D68"),
	#0x80337D70: main.sym("object_a_80337D70"),
	#0x80337D74: main.sym("object_a_80337D74"),
	#0x80337D78: main.sym("object_a_80337D78"),
	#0x80337D7C: main.sym("object_a_80337D7C"),
	#0x80337D80: main.sym("object_a_80337D80"),
	#0x80337D84: main.sym("object_a_80337D84"),
	#0x80337D88: main.sym("object_a_80337D88"),
	#0x80337D8C: main.sym("object_a_80337D8C"),
	#0x80337D90: main.sym("object_a_80337D90"),
	#0x80337D94: main.sym("object_a_80337D94"),
	#0x80337D98: main.sym("object_a_80337D98"),
	#0x80337DAC: main.sym("object_a_80337DAC"),
	#0x80337DC4: main.sym("object_a_80337DC4"),
	#0x80337DC8: main.sym("object_a_80337DC8"),
	#0x80337DCC: main.sym("object_a_80337DCC"),
	#0x80337DD0: main.sym("object_a_80337DD0"),
	#0x80337DD4: main.sym("object_a_80337DD4"),
	#0x80337DD8: main.sym("object_a_80337DD8"),
	#0x80337DE0: main.sym("object_a_80337DE0"),
	#0x80337DE8: main.sym("object_a_80337DE8"),
	#0x80337DEC: main.sym("object_a_80337DEC"),

	# src/hitcheck.c
	0x80336C50: main.sym("str_hitcheck_on"),

	# src/objlist.c
	0x80336C60: main.sym("objlist_80337E00"),
	0x80336C64: main.sym("objlist_80337E04"),
	0x80336C68: main.sym("objlist_80337E08"),
	0x80336C6C: main.sym("objlist_80337E0C"),

	# src/objsound.c
	0x80336C70: main.sym("objsound_80337E10"),
	0x80336C74: main.sym("objsound_80337E14"),
	0x80336C78: main.sym("objsound_80337E18"),

	# src/debug.c
	#0x80337E20: main.sym("str_debug_a0"),
	#0x80337E28: main.sym("str_debug_a1"),
	#0x80337E30: main.sym("str_debug_a2"),
	#0x80337E38: main.sym("str_debug_a3"),
	#0x80337E40: main.sym("str_debug_a4"),
	#0x80337E48: main.sym("str_debug_a5"),
	#0x80337E50: main.sym("str_debug_a6"),
	#0x80337E58: main.sym("str_debug_a7"),
	#0x80337E60: main.sym("str_debug_a"),
	#0x80337E64: main.sym("str_debug_b0"),
	#0x80337E6C: main.sym("str_debug_b1"),
	#0x80337E74: main.sym("str_debug_b2"),
	#0x80337E7C: main.sym("str_debug_b3"),
	#0x80337E84: main.sym("str_debug_b4"),
	#0x80337E8C: main.sym("str_debug_b5"),
	#0x80337E94: main.sym("str_debug_b6"),
	#0x80337E9C: main.sym("str_debug_b7"),
	#0x80337EA4: main.sym("str_debug_b"),
	0x80336D08: main.sym("str_debug_dprint_over"),
	0x80336D14: main.sym("str_debug_mapinfo"),
	0x80336D1C: main.sym("str_debug_area"),
	0x80336D24: main.sym("str_debug_wx"),
	0x80336D2C: main.sym("str_debug_wy"),
	0x80336D34: main.sym("str_debug_wz"),
	0x80336D3C: main.sym("str_debug_bgy"),
	0x80336D44: main.sym("str_debug_angy"),
	0x80336D4C: main.sym("str_debug_bgcode"),
	0x80336D58: main.sym("str_debug_bgstatus"),
	0x80336D64: main.sym("str_debug_bgarea"),
	0x80336D70: main.sym("str_debug_water"),
	0x80336D7C: main.sym("str_DebugCheckinfo"),
	0x80336D88: main.sym("str_debug_stageinfo"),
	0x80336D94: main.sym("str_debug_stage_param"),
	0x80336DA4: main.sym("str_debug_effectinfo"),
	0x80336DB0: main.sym("str_debug_enemyinfo"),
	0x80336DBC: main.sym("str_debug_obj"),
	0x80336DC4: main.sym("str_debug_nullbg"),
	0x80336DD0: main.sym("str_debug_wall"),
	0x80336DDC: main.sym("str_debug_bound"),
	0x80336DE8: main.sym("str_debug_touch"),
	0x80336DF4: main.sym("str_debug_takeoff"),
	0x80336E00: main.sym("str_debug_dive"),
	0x80336E0C: main.sym("str_debug_s_water"),
	0x80336E18: main.sym("str_debug_u_water"),
	0x80336E24: main.sym("str_debug_b_water"),
	0x80336E30: main.sym("str_debug_sky"),
	0x80336E3C: main.sym("str_debug_out_scope"),
	0x80336E50: main.sym("debug_80337FF0"),

	# src/wipe.c
	0x80336E60: main.sym("wipe_80338000"),
	0x80336E68: main.sym("wipe_80338008"),
	0x80336E70: main.sym("wipe_80338010"),

	# src/shadow.c
	0x80336EC0: main.sym("shadow_80338060"),
	0x80336EC8: main.sym("shadow_80338068"),
	0x80336ED0: main.sym("shadow_80338070"),
	0x80336ED8: main.sym("shadow_80338078"),
	0x80336EE0: main.sym("shadow_80338080"),
	0x80336EE8: main.sym("shadow_80338088"),
	0x80336EF0: main.sym("shadow_80338090"),
	0x80336EF8: main.sym("shadow_80338098"),
	0x80336F00: main.sym("shadow_803380A0"),
	0x80336F08: main.sym("shadow_803380A8"),
	0x80336F10: main.sym("shadow_803380B0"),
	0x80336F18: main.sym("shadow_803380B8"),
	0x80336F20: main.sym("shadow_803380C0"),
	0x80336F28: main.sym("shadow_803380C8"),
	0x80336F30: main.sym("shadow_803380D0"),
	0x80336F38: main.sym("shadow_803380D8"),
	0x80336F40: main.sym("shadow_803380E0"),
	0x80336F48: main.sym("shadow_803380E8"),
	0x80336F50: main.sym("shadow_803380F0"),
	0x80336F58: main.sym("shadow_803380F8"),
	0x80336F60: main.sym("shadow_80338100"),
	0x80336F68: main.sym("shadow_80338108"),

	# src/background.c
	0x80336FA0: main.sym("background_80338140"),
	0x80336FA8: main.sym("background_80338148"),
	0x80336FB0: main.sym("background_80338150"),
	0x80336FB8: main.sym("background_80338158"),

	# src/water.c
	0x80336FC0: main.sym("water_80338160"),

	# src/wave.c
	0x80336FD0: main.sym("wave_80338170"),
	0x80336FD8: main.sym("wave_80338178"),
	0x80336FE0: main.sym("wave_80338180"),
	0x80336FE8: main.sym("wave_80338188"),
	0x80336FF0: main.sym("wave_80338190"),

	# src/message.c
	0x80337000: main.sym("message_803381A0"),
	0x80337008: main.sym("message_803381A8"),
	0x80337010: main.sym("message_803381B0"),
	0x80337018: main.sym("message_803381B8"),

	# src/weather.c
	0x803370A0: main.sym("weather_80338280"),
	0x803370A8: main.sym("weather_80338288"),
	0x803370B0: main.sym("weather_80338290"),
	0x803370B8: main.sym("weather_80338298"),
	0x803370C0: main.sym("weather_803382A0"),
	0x803370C8: main.sym("weather_803382A8"),
	0x803370D0: main.sym("weather_803382B0"),

	# src/lava.c
	0x803370E0: main.sym("lava_803382C0"),
	0x803370E4: main.sym("lava_803382C4"),
	0x803370E8: main.sym("lava_803382C8"),
	0x803370EC: main.sym("lava_803382CC"),
	0x803370F0: main.sym("lava_803382D0"),
	0x803370F4: main.sym("lava_803382D4"),

	# src/tag.c
	0x80337130: main.sym("tag_80338310"),
	0x80337188: main.sym("tag_80338368"),

	# src/hud.c
	0x803371A0: main.sym("str_hud_life_icon"),
	0x803371A4: main.sym("str_hud_life_x"),
	0x803371A8: main.sym("str_hud_life_fmt"),
	0x803371AC: main.sym("str_hud_coin_icon"),
	0x803371B0: main.sym("str_hud_coin_x"),
	0x803371B4: main.sym("str_hud_coin_fmt"),
	0x803371B8: main.sym("str_hud_star_icon"),
	0x803371BC: main.sym("str_hud_star_x"),
	0x803371C0: main.sym("str_hud_star_fmt"),
	0x803371C4: main.sym("str_hud_key"),
	0x803371C8: main.sym("str_hud_time_text"),
	0x803371D0: main.sym("str_hud_time_min"),
	0x803371D4: main.sym("str_hud_time_sec"),
	0x803371DC: main.sym("str_hud_time_frc"),
	0x803371E0: main.sym("hud_803383C0"),
	0x803371E8: main.sym("hud_803383C8"),

	# src/object_b.c
	#0x803383D0: main.sym("object_b_803383D0"),
	#0x803383D8: main.sym("object_b_803383D8"),
	#0x803383E0: main.sym("object_b_803383E0"),
	#0x803383E8: main.sym("object_b_803383E8"),
	#0x803383F0: main.sym("object_b_803383F0"),
	#0x803383F8: main.sym("object_b_803383F8"),
	#0x80338400: main.sym("object_b_80338400"),
	#0x80338408: main.sym("object_b_80338408"),
	#0x80338410: main.sym("object_b_80338410"),
	#0x80338418: main.sym("object_b_80338418"),
	#0x80338420: main.sym("object_b_80338420"),
	#0x80338428: main.sym("object_b_80338428"),
	#0x80338430: main.sym("object_b_80338430"),
	#0x80338438: main.sym("object_b_80338438"),
	#0x80338440: main.sym("object_b_80338440"),
	#0x80338448: main.sym("object_b_80338448"),
	#0x80338450: main.sym("object_b_80338450"),
	#0x80338458: main.sym("object_b_80338458"),
	#0x80338460: main.sym("object_b_80338460"),
	#0x80338468: main.sym("object_b_80338468"),
	#0x80338470: main.sym("object_b_80338470"),
	#0x80338478: main.sym("object_b_80338478"),
	#0x80338480: main.sym("object_b_80338480"),
	#0x80338488: main.sym("object_b_80338488"),
	#0x80338490: main.sym("object_b_80338490"),
	#0x80338494: main.sym("object_b_80338494"),
	#0x803384A8: main.sym("object_b_803384A8"),
	#0x803384BC: main.sym("object_b_803384BC"),
	#0x803384C0: main.sym("object_b_803384C0"),
	#0x803384C4: main.sym("object_b_803384C4"),
	#0x803384C8: main.sym("object_b_803384C8"),
	#0x803384CC: main.sym("object_b_803384CC"),
	#0x803384D0: main.sym("object_b_803384D0"),
	#0x803384D4: main.sym("object_b_803384D4"),
	#0x803384D8: main.sym("object_b_803384D8"),
	#0x803384DC: main.sym("object_b_803384DC"),
	#0x803384E0: main.sym("object_b_803384E0"),
	#0x803384E4: main.sym("object_b_803384E4"),
	#0x803384E8: main.sym("object_b_803384E8"),
	#0x803384EC: main.sym("object_b_803384EC"),
	#0x803384F0: main.sym("object_b_803384F0"),
	#0x803384F4: main.sym("object_b_803384F4"),
	#0x803384F8: main.sym("object_b_803384F8"),
	#0x803384FC: main.sym("object_b_803384FC"),
	#0x80338500: main.sym("object_b_80338500"),
	#0x80338508: main.sym("object_b_80338508"),
	#0x80338510: main.sym("object_b_80338510"),
	#0x80338518: main.sym("object_b_80338518"),
	#0x80338530: main.sym("object_b_80338530"),
	#0x80338538: main.sym("object_b_80338538"),
	#0x80338540: main.sym("object_b_80338540"),
	#0x80338548: main.sym("object_b_80338548"),
	#0x80338550: main.sym("object_b_80338550"),
	#0x80338558: main.sym("object_b_80338558"),
	#0x80338560: main.sym("object_b_80338560"),
	#0x80338568: main.sym("object_b_80338568"),
	#0x80338570: main.sym("object_b_80338570"),
	#0x80338574: main.sym("object_b_80338574"),
	#0x80338578: main.sym("object_b_80338578"),
	#0x8033857C: main.sym("object_b_8033857C"),
	#0x80338580: main.sym("object_b_80338580"),
	#0x80338584: main.sym("object_b_80338584"),
	#0x80338588: main.sym("object_b_80338588"),
	#0x8033858C: main.sym("object_b_8033858C"),
	#0x80338590: main.sym("object_b_80338590"),
	#0x80338594: main.sym("object_b_80338594"),
	#0x80338598: main.sym("object_b_80338598"),
	#0x8033859C: main.sym("object_b_8033859C"),
	#0x803385B8: main.sym("object_b_803385B8"),
	#0x803385C0: main.sym("object_b_803385C0"),
	#0x803385C8: main.sym("object_b_803385C8"),
	#0x803385D0: main.sym("object_b_803385D0"),
	#0x803385D8: main.sym("object_b_803385D8"),
	#0x803385E0: main.sym("object_b_803385E0"),
	#0x803385E8: main.sym("object_b_803385E8"),
	#0x803385F0: main.sym("object_b_803385F0"),
	#0x803385F8: main.sym("object_b_803385F8"),
	#0x80338600: main.sym("object_b_80338600"),
	#0x80338604: main.sym("object_b_80338604"),
	#0x80338608: main.sym("object_b_80338608"),
	#0x8033860C: main.sym("object_b_8033860C"),
	#0x80338610: main.sym("object_b_80338610"),
	#0x80338614: main.sym("object_b_80338614"),
	#0x80338618: main.sym("object_b_80338618"),
	#0x8033861C: main.sym("object_b_8033861C"),
	#0x80338620: main.sym("object_b_80338620"),
	#0x80338624: main.sym("object_b_80338624"),
	#0x80338628: main.sym("object_b_80338628"),
	#0x8033862C: main.sym("object_b_8033862C"),
	#0x80338630: main.sym("object_b_80338630"),
	#0x80338634: main.sym("object_b_80338634"),
	#0x80338638: main.sym("object_b_80338638"),
	#0x8033863C: main.sym("object_b_8033863C"),
	#0x80338650: main.sym("object_b_80338650"),
	#0x80338668: main.sym("object_b_80338668"),
	#0x80338680: main.sym("object_b_80338680"),
	#0x80338688: main.sym("object_b_80338688"),
	#0x8033869C: main.sym("object_b_8033869C"),
	#0x803386A0: main.sym("object_b_803386A0"),
	#0x803386A4: main.sym("object_b_803386A4"),
	#0x803386A8: main.sym("object_b_803386A8"),
	#0x803386AC: main.sym("object_b_803386AC"),
	#0x803386B0: main.sym("object_b_803386B0"),
	#0x803386B4: main.sym("object_b_803386B4"),
	#0x803386B8: main.sym("object_b_803386B8"),
	#0x803386BC: main.sym("object_b_803386BC"),
	#0x803386C0: main.sym("object_b_803386C0"),
	#0x803386C8: main.sym("object_b_803386C8"),
	#0x803386D0: main.sym("object_b_803386D0"),
	#0x803386D8: main.sym("object_b_803386D8"),
	#0x803386E0: main.sym("object_b_803386E0"),
	#0x803386E4: main.sym("object_b_803386E4"),
	#0x803386E8: main.sym("object_b_803386E8"),
	#0x803386EC: main.sym("object_b_803386EC"),
	#0x803386F0: main.sym("object_b_803386F0"),
	#0x80338704: main.sym("object_b_80338704"),
	#0x80338708: main.sym("object_b_80338708"),
	#0x8033870C: main.sym("object_b_8033870C"),
	#0x80338710: main.sym("object_b_80338710"),
	#0x80338714: main.sym("object_b_80338714"),
	#0x80338718: main.sym("object_b_80338718"),
	#0x8033871C: main.sym("object_b_8033871C"),
	#0x80338730: main.sym("object_b_80338730"),
	#0x80338734: main.sym("object_b_80338734"),
	#0x80338738: main.sym("object_b_80338738"),
	#0x8033873C: main.sym("object_b_8033873C"),
	#0x80338740: main.sym("object_b_80338740"),
	#0x80338748: main.sym("object_b_80338748"),
	#0x803387D8: main.sym("object_b_803387D8"),
	#0x803387DC: main.sym("object_b_803387DC"),
	#0x803387E0: main.sym("object_b_803387E0"),
	#0x803387E8: main.sym("object_b_803387E8"),
	#0x803387F0: main.sym("object_b_803387F0"),
	#0x803387F8: main.sym("object_b_803387F8"),
	#0x803387FC: main.sym("object_b_803387FC"),
	#0x80338800: main.sym("object_b_80338800"),
	#0x80338804: main.sym("object_b_80338804"),
	#0x80338808: main.sym("object_b_80338808"),
	#0x8033880C: main.sym("object_b_8033880C"),
	#0x80338810: main.sym("object_b_80338810"),
	#0x80338814: main.sym("object_b_80338814"),
	#0x80338818: main.sym("object_b_80338818"),
	#0x8033881C: main.sym("object_b_8033881C"),
	#0x80338820: main.sym("object_b_80338820"),
	#0x80338828: main.sym("object_b_80338828"),
	#0x80338830: main.sym("object_b_80338830"),
	#0x80338838: main.sym("object_b_80338838"),
	#0x80338840: main.sym("object_b_80338840"),
	#0x80338860: main.sym("object_b_80338860"),
	#0x80338868: main.sym("object_b_80338868"),
	#0x80338870: main.sym("object_b_80338870"),
	#0x80338878: main.sym("object_b_80338878"),
	#0x80338880: main.sym("object_b_80338880"),
	#0x80338888: main.sym("object_b_80338888"),
	#0x80338890: main.sym("object_b_80338890"),
	#0x80338898: main.sym("object_b_80338898"),
	#0x803388A0: main.sym("object_b_803388A0"),
	#0x803388A8: main.sym("object_b_803388A8"),
	#0x803388B0: main.sym("object_b_803388B0"),
	#0x803388B8: main.sym("object_b_803388B8"),
	#0x803388C0: main.sym("object_b_803388C0"),
	#0x803388C8: main.sym("object_b_803388C8"),
	#0x803388D0: main.sym("object_b_803388D0"),
	#0x803388D8: main.sym("object_b_803388D8"),
	#0x803388E0: main.sym("object_b_803388E0"),
	#0x803388E8: main.sym("object_b_803388E8"),
	#0x803388F0: main.sym("object_b_803388F0"),
	#0x803388F8: main.sym("object_b_803388F8"),
	#0x80338900: main.sym("object_b_80338900"),
	#0x80338904: main.sym("object_b_80338904"),
	#0x80338908: main.sym("object_b_80338908"),
	#0x80338910: main.sym("object_b_80338910"),
	#0x80338918: main.sym("object_b_80338918"),
	#0x80338920: main.sym("object_b_80338920"),
	#0x80338924: main.sym("object_b_80338924"),
	#0x80338928: main.sym("object_b_80338928"),
	#0x8033892C: main.sym("object_b_8033892C"),
	#0x80338930: main.sym("object_b_80338930"),
	#0x80338934: main.sym("object_b_80338934"),
	#0x80338938: main.sym("object_b_80338938"),
	#0x8033893C: main.sym("object_b_8033893C"),
	#0x80338940: main.sym("object_b_80338940"),
	#0x80338954: main.sym("object_b_80338954"),
	#0x80338958: main.sym("object_b_80338958"),
	#0x8033895C: main.sym("object_b_8033895C"),
	#0x80338960: main.sym("object_b_80338960"),
	#0x80338968: main.sym("object_b_80338968"),
	#0x8033896C: main.sym("object_b_8033896C"),
	#0x80338970: main.sym("object_b_80338970"),
	#0x80338974: main.sym("object_b_80338974"),
	#0x80338978: main.sym("object_b_80338978"),

	# src/object_c.c
	#0x803389B0: main.sym("object_c_803389B0"),
	#0x803389B4: main.sym("object_c_803389B4"),
	#0x803389B8: main.sym("object_c_803389B8"),
	#0x803389DC: main.sym("object_c_803389DC"),
	#0x803389E0: main.sym("object_c_803389E0"),
	#0x803389E4: main.sym("object_c_803389E4"),
	#0x803389E8: main.sym("object_c_803389E8"),
	#0x803389EC: main.sym("object_c_803389EC"),
	#0x803389F0: main.sym("object_c_803389F0"),
	#0x803389F4: main.sym("object_c_803389F4"),
	#0x803389F8: main.sym("object_c_803389F8"),
	#0x803389FC: main.sym("object_c_803389FC"),
	#0x80338A00: main.sym("object_c_80338A00"),
	#0x80338A04: main.sym("object_c_80338A04"),
	#0x80338A08: main.sym("object_c_80338A08"),
	#0x80338A0C: main.sym("object_c_80338A0C"),
	#0x80338A10: main.sym("object_c_80338A10"),
	#0x80338A14: main.sym("object_c_80338A14"),
	#0x80338A18: main.sym("object_c_80338A18"),
	#0x80338A1C: main.sym("object_c_80338A1C"),
	#0x80338A20: main.sym("object_c_80338A20"),
	#0x80338A24: main.sym("object_c_80338A24"),
	#0x80338A28: main.sym("object_c_80338A28"),
	#0x80338A2C: main.sym("object_c_80338A2C"),
	#0x80338A30: main.sym("object_c_80338A30"),
	#0x80338A4C: main.sym("object_c_80338A4C"),
	#0x80338A50: main.sym("object_c_80338A50"),
	#0x80338A54: main.sym("object_c_80338A54"),
	#0x80338A58: main.sym("object_c_80338A58"),
	#0x80338A5C: main.sym("object_c_80338A5C"),
	#0x80338A60: main.sym("object_c_80338A60"),
	#0x80338A64: main.sym("object_c_80338A64"),
	#0x80338A68: main.sym("object_c_80338A68"),
	#0x80338A6C: main.sym("object_c_80338A6C"),
	#0x80338A70: main.sym("object_c_80338A70"),
	#0x80338A74: main.sym("object_c_80338A74"),
	#0x80338A78: main.sym("object_c_80338A78"),
	#0x80338A7C: main.sym("object_c_80338A7C"),
	#0x80338A80: main.sym("object_c_80338A80"),
	#0x80338A84: main.sym("object_c_80338A84"),
	#0x80338A88: main.sym("object_c_80338A88"),
	#0x80338A8C: main.sym("object_c_80338A8C"),
	#0x80338A90: main.sym("object_c_80338A90"),
	#0x80338A94: main.sym("object_c_80338A94"),
	#0x80338A98: main.sym("object_c_80338A98"),
	#0x80338A9C: main.sym("object_c_80338A9C"),
	#0x80338AA0: main.sym("object_c_80338AA0"),
	#0x80338AA4: main.sym("object_c_80338AA4"),
	#0x80338ABC: main.sym("object_c_80338ABC"),
	#0x80338AC0: main.sym("object_c_80338AC0"),
	#0x80338AC4: main.sym("object_c_80338AC4"),
	#0x80338AC8: main.sym("object_c_80338AC8"),
	#0x80338ACC: main.sym("object_c_80338ACC"),
	#0x80338AE0: main.sym("object_c_80338AE0"),
	#0x80338AE4: main.sym("object_c_80338AE4"),
	#0x80338AE8: main.sym("object_c_80338AE8"),
	#0x80338AEC: main.sym("object_c_80338AEC"),
	#0x80338AF0: main.sym("object_c_80338AF0"),
	#0x80338AF4: main.sym("object_c_80338AF4"),
	#0x80338AF8: main.sym("object_c_80338AF8"),
	#0x80338AFC: main.sym("object_c_80338AFC"),
	#0x80338B00: main.sym("object_c_80338B00"),
	#0x80338B04: main.sym("object_c_80338B04"),
	#0x80338B08: main.sym("object_c_80338B08"),
	#0x80338B0C: main.sym("object_c_80338B0C"),
	#0x80338B10: main.sym("object_c_80338B10"),
	#0x80338B14: main.sym("object_c_80338B14"),
	#0x80338B18: main.sym("object_c_80338B18"),
	#0x80338B1C: main.sym("object_c_80338B1C"),
	#0x80338B20: main.sym("object_c_80338B20"),
	#0x80338B24: main.sym("object_c_80338B24"),
	#0x80338B28: main.sym("object_c_80338B28"),
	#0x80338B2C: main.sym("object_c_80338B2C"),
	#0x80338B30: main.sym("object_c_80338B30"),
	#0x80338B34: main.sym("object_c_80338B34"),
	#0x80338B38: main.sym("object_c_80338B38"),
	#0x80338B3C: main.sym("object_c_80338B3C"),
	#0x80338B5C: main.sym("object_c_80338B5C"),
	#0x80338B60: main.sym("object_c_80338B60"),
	#0x80338B64: main.sym("object_c_80338B64"),
	#0x80338B68: main.sym("object_c_80338B68"),
	#0x80338B6C: main.sym("object_c_80338B6C"),
	#0x80338B80: main.sym("object_c_80338B80"),
	#0x80338B84: main.sym("object_c_80338B84"),
	#0x80338B88: main.sym("object_c_80338B88"),
	#0x80338B8C: main.sym("object_c_80338B8C"),
	#0x80338B90: main.sym("object_c_80338B90"),
	#0x80338B94: main.sym("object_c_80338B94"),
	#0x80338B98: main.sym("object_c_80338B98"),
	#0x80338B9C: main.sym("object_c_80338B9C"),
	#0x80338BA0: main.sym("object_c_80338BA0"),
	#0x80338BA4: main.sym("object_c_80338BA4"),
	#0x80338BA8: main.sym("object_c_80338BA8"),
	#0x80338BAC: main.sym("object_c_80338BAC"),
	#0x80338BB0: main.sym("object_c_80338BB0"),
	#0x80338BB4: main.sym("object_c_80338BB4"),
	#0x80338BB8: main.sym("object_c_80338BB8"),
	#0x80338BBC: main.sym("object_c_80338BBC"),
	#0x80338BC0: main.sym("object_c_80338BC0"),
	#0x80338BC4: main.sym("object_c_80338BC4"),
	#0x80338BC8: main.sym("object_c_80338BC8"),
	#0x80338BE8: main.sym("object_c_80338BE8"),
	#0x80338BEC: main.sym("object_c_80338BEC"),
	#0x80338BF0: main.sym("object_c_80338BF0"),
	#0x80338BF4: main.sym("object_c_80338BF4"),
	#0x80338BF8: main.sym("object_c_80338BF8"),
	#0x80338BFC: main.sym("object_c_80338BFC"),
	#0x80338C00: main.sym("object_c_80338C00"),
	#0x80338C04: main.sym("object_c_80338C04"),
	#0x80338C08: main.sym("object_c_80338C08"),
	#0x80338C1C: main.sym("object_c_80338C1C"),
	#0x80338C20: main.sym("object_c_80338C20"),
	#0x80338C24: main.sym("object_c_80338C24"),
	#0x80338C28: main.sym("object_c_80338C28"),
	#0x80338C2C: main.sym("object_c_80338C2C"),
	#0x80338C30: main.sym("object_c_80338C30"),
	#0x80338C34: main.sym("object_c_80338C34"),
	#0x80338C38: main.sym("object_c_80338C38"),
	#0x80338C4C: main.sym("object_c_80338C4C"),
	#0x80338C50: main.sym("object_c_80338C50"),
	#0x80338C54: main.sym("object_c_80338C54"),
	#0x80338C58: main.sym("object_c_80338C58"),
	#0x80338C5C: main.sym("object_c_80338C5C"),
	#0x80338C60: main.sym("object_c_80338C60"),
	#0x80338C64: main.sym("object_c_80338C64"),
	#0x80338C68: main.sym("object_c_80338C68"),
	#0x80338C6C: main.sym("object_c_80338C6C"),
	#0x80338C70: main.sym("object_c_80338C70"),
	#0x80338C74: main.sym("object_c_80338C74"),
	#0x80338C78: main.sym("object_c_80338C78"),
	#0x80338C7C: main.sym("object_c_80338C7C"),
	#0x80338C90: main.sym("object_c_80338C90"),
	#0x80338C94: main.sym("object_c_80338C94"),
	#0x80338C98: main.sym("object_c_80338C98"),
	#0x80338C9C: main.sym("object_c_80338C9C"),
	#0x80338CA0: main.sym("object_c_80338CA0"),
	#0x80338CDC: main.sym("object_c_80338CDC"),
	#0x80338CE0: main.sym("object_c_80338CE0"),
	#0x80338CE4: main.sym("object_c_80338CE4"),
	#0x80338CE8: main.sym("object_c_80338CE8"),
	#0x80338CEC: main.sym("object_c_80338CEC"),
	#0x80338CF0: main.sym("object_c_80338CF0"),
	#0x80338CF4: main.sym("object_c_80338CF4"),
	#0x80338D14: main.sym("object_c_80338D14"),
	#0x80338D18: main.sym("object_c_80338D18"),
	#0x80338D1C: main.sym("object_c_80338D1C"),
	#0x80338D20: main.sym("object_c_80338D20"),
	#0x80338D24: main.sym("object_c_80338D24"),
	#0x80338D28: main.sym("object_c_80338D28"),
	#0x80338D2C: main.sym("object_c_80338D2C"),
	#0x80338D30: main.sym("object_c_80338D30"),
	#0x80338D34: main.sym("object_c_80338D34"),
	#0x80338D4C: main.sym("object_c_80338D4C"),
	#0x80338D50: main.sym("object_c_80338D50"),
	#0x80338D54: main.sym("object_c_80338D54"),
	#0x80338D58: main.sym("object_c_80338D58"),
	#0x80338D5C: main.sym("object_c_80338D5C"),
	#0x80338D60: main.sym("object_c_80338D60"),
	#0x80338D64: main.sym("object_c_80338D64"),
	#0x80338D68: main.sym("object_c_80338D68"),
	#0x80338D6C: main.sym("object_c_80338D6C"),
	#0x80338D70: main.sym("object_c_80338D70"),
	#0x80338D74: main.sym("object_c_80338D74"),
	#0x80338D78: main.sym("object_c_80338D78"),
	#0x80338D7C: main.sym("object_c_80338D7C"),
	#0x80338D80: main.sym("object_c_80338D80"),
	#0x80338D84: main.sym("object_c_80338D84"),
	#0x80338D88: main.sym("object_c_80338D88"),
	#0x80338D8C: main.sym("object_c_80338D8C"),
	#0x80338D90: main.sym("object_c_80338D90"),

	# src/audio/driver.c
	#0x80338DA0: main.sym("Na_driver_80338DA0"),
	#0x80338DA4: main.sym("Na_driver_80338DA4"),
	#0x80338DA8: main.sym("Na_driver_80338DA8"),
	#0x80338DAC: main.sym("Na_driver_80338DAC"),
	#0x80338DB0: main.sym("Na_driver_80338DB0"),

	# src/audio/memory.c
	#0x80338DC0: main.sym("Na_memory_80338DC0"),
	#0x80338E00: main.sym("Na_memory_80338E00"),
	#0x80338E04: main.sym("Na_memory_80338E04"),

	# src/audio/voice.c
	#0x80338E10: main.sym("Na_voice_80338E10"),
	#0x80338E14: main.sym("Na_voice_80338E14"),
	#0x80338E18: main.sym("Na_voice_80338E18"),
	#0x80338E1C: main.sym("Na_voice_80338E1C"),
	#0x80338E20: main.sym("Na_voice_80338E20"),
	#0x80338E24: main.sym("Na_voice_80338E24"),

	# src/audio/effect.c
	#0x80338E30: main.sym("Na_effect_80338E30"),

	# src/audio/sequence.c
	#0x80338E60: main.sym("Na_sequence_80338E60"),
	#0x80338E84: main.sym("Na_sequence_80338E84"),
	#0x80338EAC: main.sym("Na_sequence_80338EAC"),
	#0x80338EC0: main.sym("Na_sequence_80338EC0"),
	#0x80338FBC: main.sym("Na_sequence_80338FBC"),
	#0x80339280: main.sym("Na_sequence_80339280"),
	#0x80339360: main.sym("Na_sequence_80339360"),

	# src/audio/game.c
	#0x803394F0: main.sym("str_Na_game_803394F0"),
	#0x803394FC: main.sym("str_Na_game_803394FC"),
	#0x80339518: main.sym("str_Na_game_80339518"),
	#0x80339524: main.sym("str_Na_game_80339524"),
	#0x80339540: main.sym("str_Na_game_80339540"),
	#0x8033954C: main.sym("str_Na_game_8033954C"),
	#0x80339560: main.sym("str_Na_game_80339560"),
	#0x80339568: main.sym("str_Na_game_80339568"),
	#0x8033956C: main.sym("str_Na_game_8033956C"),
	#0x80339578: main.sym("str_Na_game_80339578"),
	#0x8033958C: main.sym("str_Na_game_8033958C"),
	#0x80339594: main.sym("str_Na_game_80339594"),
	#0x80339598: main.sym("str_Na_game_80339598"),
	#0x803395C8: main.sym("str_Na_game_803395C8"),
	#0x803395F8: main.sym("str_Na_game_803395F8"),
	#0x80339600: main.sym("str_Na_game_80339600"),
	#0x80339604: main.sym("str_Na_game_80339604"),
	#0x80339608: main.sym("str_Na_game_80339608"),
	#0x80339610: main.sym("str_Na_game_80339610"),
	#0x80339614: main.sym("str_Na_game_80339614"),
	#0x80339618: main.sym("str_Na_game_80339618"),
	#0x80339624: main.sym("str_Na_game_80339624"),
	#0x80339630: main.sym("str_Na_game_80339630"),
	#0x8033963C: main.sym("str_Na_game_8033963C"),
	#0x80339648: main.sym("str_Na_game_80339648"),
	#0x80339660: main.sym("str_Na_game_80339660"),
	#0x8033967C: main.sym("str_Na_game_8033967C"),
	#0x8033968C: main.sym("str_Na_game_8033968C"),
	#0x8033969C: main.sym("str_Na_game_8033969C"),
	#0x803396AC: main.sym("str_Na_game_803396AC"),
	#0x803396BC: main.sym("str_Na_game_803396BC"),
	#0x803396CC: main.sym("str_Na_game_803396CC"),
	#0x803396D8: main.sym("str_Na_game_803396D8"),
	#0x803396EC: main.sym("str_Na_game_803396EC"),
	#0x80339710: main.sym("Na_game_80339710"),
	#0x80339718: main.sym("Na_game_80339718"),
	#0x80339720: main.sym("Na_game_80339720"),
	#0x80339724: main.sym("Na_game_80339724"),
	#0x80339728: main.sym("Na_game_80339728"),
	#0x8033972C: main.sym("Na_game_8033972C"),
	#0x80339730: main.sym("Na_game_80339730"),
	#0x80339734: main.sym("Na_game_80339734"),
	#0x80339738: main.sym("Na_game_80339738"),
	#0x8033973C: main.sym("Na_game_8033973C"),
	#0x80339764: main.sym("Na_game_80339764"),
	#0x8033978C: main.sym("Na_game_8033978C"),

	# libultra
	0x80338440: main.sym("guPerspectiveF__803397B0"),
	0x80338450: main.sym("__d_to_ull__803397C0"),
	0x80338458: main.sym("__f_to_ull__803397C8"),
	0x80338460: main.sym("cosf__P"),
	0x80338488: main.sym("cosf__rpi"),
	0x80338490: main.sym("cosf__pihi"),
	0x80338498: main.sym("cosf__pilo"),
	0x803384A0: main.sym("cosf__zero"),
	0x803384B0: main.sym("sinf__P"),
	0x803384D8: main.sym("sinf__rpi"),
	0x803384E0: main.sym("sinf__pihi"),
	0x803384E8: main.sym("sinf__pilo"),
	0x803384F0: main.sym("sinf__zero"),
	0x80338500: main.sym("guRotateF__80339870"),
	0x80338510: main.sym("_Printf__80339880"),
	0x80338514: main.sym("fchar"),
	0x8033851C: main.sym("fbit"),
	0x80338534: main.sym("_Putfld__803398A4"),
	0x80338610: main.sym("__osIntOffTable"),
	0x80338630: main.sym("__osIntTable"),
	0x80338660: main.sym("__libm_qnan_f", flag={"GLOBL"}),
	0x80338670: main.sym("pows"),
	0x803386B8: main.sym("_Ldtob__80339A28"),
	0x803386BC: main.sym("_Ldtob__80339A2C"),
	0x803386C0: main.sym("_Genld__80339A30"),
	0x803386C8: main.sym("_Ldtob__80339A38"),
	0x803386D0: main.sym("__osRcpImTable", flag={"GLOBL"}),

	# ==========================================================================
	# bss
	# ==========================================================================

	# src/main.c
	0x80339210: main.sym("rmon_thread"),
	0x803393C0: main.sym("idle_thread"),
	0x80339570: main.sym("sched_thread"),
	0x80339720: main.sym("gfx_thread"),
	0x803398D0: main.sym("aud_thread"),
	0x80339A80: main.sym("pi_mq"),
	0x80339A98: main.sym("sched_mq"),
	0x80339AB0: main.sym("sctask_mq"),
	0x80339AC8: main.sym("dma_mbox"),
	0x80339AD0: main.sym("pi_mbox"),
	0x80339B50: main.sym("si_mbox"),
	0x80339B58: main.sym("sched_mbox"),
	0x80339B98: main.sym("sctask_mbox"),
	0x80339BD8: main.sym("dma_mb"),
	0x80339BEC: main.sym("null_msg"),
	0x80339BF0: main.sym("dma_mq"),
	0x80339C08: main.sym("si_mq"),

	# src/graphics.c
	0x80339C20: main.sym("controller_data", flag={"GLOBL"}),
	0x80339C78: main.sym("cont_status"),
	0x80339C88: main.sym("cont_pad"),
	0x80339CA0: main.sym("gfx_vi_mq"),
	0x80339CB8: main.sym("gfx_dp_mq"),
	0x80339CD0: main.sym("gfx_vi_mbox"),
	0x80339CD4: main.sym("gfx_dp_mbox"),
	0x80339CD8: main.sym("gfx_client"),
	0x80339CE0: main.sym("gfx_cimg"),
	0x80339CEC: main.sym("gfx_zimg"),
	0x80339CF0: main.sym("mario_anime_buf"),
	0x80339CF4: main.sym("demo_buf"),
	0x80339CF8: main.sym("gfx_task", flag={"GLOBL"}),
	0x80339CFC: main.sym("glistp", flag={"GLOBL"}),
	0x80339D00: main.sym("gfx_mem", flag={"GLOBL"}),
	0x80339D04: main.sym("framep", flag={"GLOBL"}),
	0x80339D08: main.sym("cont_bitpattern", flag={"GLOBL"}),
	0x80339D09: main.sym("eeprom_status", flag={"GLOBL"}),
	0x80339D10: main.sym("mario_anime_bank", flag={"GLOBL"}),
	0x80339D20: main.sym("demo_bank", flag={"GLOBL"}),

	# src/audio.c
	0x80339D30: main.sym("aud_levelse_8033B0A0"),
	0x80339DC0: main.sym("aud_0"),
	0x80339DD0: main.sym("aud_vi_mq"),
	0x80339DE8: main.sym("aud_vi_mbox"),
	0x80339DF0: main.sym("aud_client"),

	# src/game.c
	0x80339E00: main.sym("player_data", flag={"GLOBL"}),
	0x80339EC8: main.sym("game_state"),
	0x80339ECA: main.sym("game_timer"),
	0x80339ECC: main.sym("freeze_timer"),
	0x80339ED0: main.sym("freeze_callback"),
	0x80339ED8: main.sym("mario_entry"),
	0x80339EE0: main.sym("game_result"),
	0x80339EE2: main.sym("fade_mode"),
	0x80339EE4: main.sym("fade_timer"),
	0x80339EE6: main.sym("fade_port"),
	0x80339EE8: main.sym("fade_code"),
	0x80339EEC: main.sym("game_8033B25C"),
	0x80339EEE: main.sym("time_flag"),
	0x80339EF0: main.sym("hud", flag={"GLOBL"}),
	0x80339EFE: main.sym("first_msg", flag={"GLOBL"}),

	# src/collision.c
	0x80339F00: main.sym("hit_enemy"),
	0x80339F02: main.sym("invincible"),

	# src/player.c
	0x80339F10: main.sym("player_8033B280"),

	# src/physics.c
	0x80339F20: main.sym("physics_8033B290", flag={"GLOBL"}),

	# src/pldemo.c
	0x80339F30: main.sym("pldemo_8033B2A0", flag={"GLOBL"}),
	0x80339F34: main.sym("pldemo_8033B2A4", flag={"GLOBL"}),
	0x80339F38: main.sym("pldemo_8033B2A8", flag={"GLOBL"}),
	0x80339F3C: main.sym("pldemo_8033B2AC", flag={"GLOBL"}),
	0x80339F40: main.sym("pldemo_8033B2B0", flag={"GLOBL"}),
	0x80339F44: main.sym("pldemo_8033B2B4", flag={"GLOBL"}),
	0x80339F48: main.sym("pldemo_8033B2B8", flag={"GLOBL"}),
	0x80339F4C: main.sym("pldemo_8033B2BC", flag={"GLOBL"}),

	# src/plmove.c
	0x80339F50: main.sym("plmove_8033B2C0", flag={"GLOBL"}),

	# src/plswim.c
	0x80339FD0: main.sym("plswim_8033B340", flag={"GLOBL"}),
	0x80339FD2: main.sym("plswim_8033B342", flag={"GLOBL"}),
	0x80339FD4: main.sym("plswim_8033B344", flag={"GLOBL"}),

	# src/callback.c
	0x80339FE0: main.sym("mario_mirror"),
	0x8033A040: main.sym("pl_shape_data", flag={"GLOBL"}),

	# src/memory.c
	0x8033A090: main.sym("segment_table"),
	0x8033A110: main.sym("mem_size"),
	0x8033A114: main.sym("mem_start"),
	0x8033A118: main.sym("mem_end"),
	0x8033A11C: main.sym("mem_blockl"),
	0x8033A120: main.sym("mem_blockr"),
	0x8033A124: main.sym("mem_heap", flag={"GLOBL"}),

	# src/backup.c
	0x8033A130: main.sym("mid_level"),
	0x8033A131: main.sym("mid_course"),
	0x8033A132: main.sym("mid_stage"),
	0x8033A133: main.sym("mid_scene"),
	0x8033A134: main.sym("mid_port"),
	0x8033A135: main.sym("bu_info_dirty"),
	0x8033A136: main.sym("bu_file_dirty"),

	# src/scene.c
	0x8033A140: main.sym("player_actor", flag={"GLOBL"}),
	0x8033A160: main.sym("shape_data", flag={"GLOBL"}),
	0x8033A560: main.sym("scene_data", flag={"GLOBL"}),
	0x8033A740: main.sym("wipe", flag={"GLOBL"}),
	0x8033A756: main.sym("course_index", flag={"GLOBL"}),
	0x8033A758: main.sym("level_index", flag={"GLOBL"}),
	0x8033A75A: main.sym("scene_index", flag={"GLOBL"}),
	0x8033A75C: main.sym("prev_course", flag={"GLOBL"}),
	0x8033A75E: main.sym("msg_status", flag={"GLOBL"}),
	0x8033A760: main.sym("msg_result", flag={"GLOBL"}),

	# src/draw.c
	0x8033A770: main.sym("draw_m"),
	0x8033A778: main.sym("draw_mtxf"),
	0x8033AF78: main.sym("draw_mtx"),
	0x8033AFF8: main.sym("joint_save_type"),
	0x8033AFF9: main.sym("joint_save_shadow"),
	0x8033AFFA: main.sym("joint_save_frame"),
	0x8033AFFC: main.sym("joint_save_scale"),
	0x8033B000: main.sym("joint_save_tbl"),
	0x8033B004: main.sym("joint_save_val"),
	0x8033B008: main.sym("joint_type"),
	0x8033B009: main.sym("joint_shadow"),
	0x8033B00A: main.sym("joint_frame"),
	0x8033B00C: main.sym("joint_scale"),
	0x8033B010: main.sym("joint_tbl"),
	0x8033B014: main.sym("joint_val"),
	0x8033B018: main.sym("draw_arena"),

	# src/time.c
	0x8033B020: main.sym("time_data"),

	# src/camera.c
	0x8033B1B0: main.sym("pl_camera_data", flag={"GLOBL"}),
	0x8033B1F8: main.sym("_camera_bss_48"),
	0x8033B328: main.sym("camdata", flag={"GLOBL"}),
	0x8033B3E8: main.sym("_camera_bss_238"),
	0x8033B4D8: main.sym("camera_8033C848", flag={"GLOBL"}),
	0x8033B4DA: main.sym("camera_8033C84A", flag={"GLOBL"}),
	0x8033B4E0: main.sym("_camera_bss_330"),
	0x8033B858: main.sym("camera_8033CBC8", flag={"GLOBL"}),
	0x8033B85C: main.sym("camera_8033CBCC", flag={"GLOBL"}),
	0x8033B860: main.sym("camerap", flag={"GLOBL"}),

	# src/object.c
	0x8033B870: main.sym("obj_rootdata"),
	0x8033BEF0: main.sym("debug_flag", flag={"GLOBL"}),
	0x8033BEF4: main.sym("nullbg_count", flag={"GLOBL"}),
	0x8033BEF8: main.sym("nullroof_count", flag={"GLOBL"}),
	0x8033BEFC: main.sym("wall_count", flag={"GLOBL"}),
	0x8033BF00: main.sym("obj_count", flag={"GLOBL"}),
	0x8033BF04: main.sym("bgdebug", flag={"GLOBL"}),
	0x8033BF10: main.sym("db_work", flag={"GLOBL"}),
	0x8033C010: main.sym("db_save", flag={"GLOBL"}),
	0x8033C110: main.sym("object_flag", flag={"GLOBL"}),
	0x8033C118: main.sym("object_data", flag={"GLOBL"}),
	0x8035FB18: main.sym("object_dummy", flag={"GLOBL"}),
	0x8035FD78: main.sym("obj_rootlist", flag={"GLOBL"}),
	0x8035FD80: main.sym("obj_freelist", flag={"GLOBL"}),
	0x8035FDE8: main.sym("mario_obj", flag={"GLOBL"}),
	0x8035FDEC: main.sym("luigi_obj", flag={"GLOBL"}),
	0x8035FDF0: main.sym("object", flag={"GLOBL"}),
	0x8035FDF4: main.sym("object_pc", flag={"GLOBL"}),
	0x8035FDF8: main.sym("obj_prevcount", flag={"GLOBL"}),
	0x8035FDFC: main.sym("bglist_count", flag={"GLOBL"}),
	0x8035FE00: main.sym("bgface_count", flag={"GLOBL"}),
	0x8035FE04: main.sym("bglist_static", flag={"GLOBL"}),
	0x8035FE08: main.sym("bgface_static", flag={"GLOBL"}),
	0x8035FE0C: main.sym("object_heap", flag={"GLOBL"}),
	0x8035FE10: main.sym("object_80361180", flag={"GLOBL"}),
	0x8035FE12: main.sym("object_80361182", flag={"GLOBL"}),
	0x8035FE14: main.sym("waterp", flag={"GLOBL"}),
	0x8035FE18: main.sym("water_table", flag={"GLOBL"}),
	0x8035FE68: main.sym("area_table", flag={"GLOBL"}),
	0x8035FEE0: main.sym("object_80361250", flag={"GLOBL"}),
	0x8035FEE2: main.sym("object_80361252", flag={"GLOBL"}),
	0x8035FEE4: main.sym("object_80361254", flag={"GLOBL"}),
	0x8035FEE6: main.sym("object_80361256", flag={"GLOBL"}),
	0x8035FEE8: main.sym("object_80361258", flag={"GLOBL"}),
	0x8035FEEA: main.sym("object_8036125A", flag={"GLOBL"}),
	0x8035FEEC: main.sym("object_8036125C", flag={"GLOBL"}),
	0x8035FEEE: main.sym("object_8036125E", flag={"GLOBL"}),
	0x8035FEF0: main.sym("object_80361260", flag={"GLOBL"}),
	0x8035FEF2: main.sym("object_80361262", flag={"GLOBL"}),
	0x8035FEF4: main.sym("object_80361264", flag={"GLOBL"}),

	# src/objectlib.c
	0x8035FF00: main.sym("objectlib_80361270", flag={"GLOBL"}),

	# src/object_a.c
	0x8035FF10: main.sym("object_a_80361280", flag={"GLOBL"}),

	# src/debug.c
	0x8035FF20: main.sym("db_out"),
	0x8035FF30: main.sym("db_err"),

	# src/shadow.c
	0x8035FF40: main.sym("shadow_offset"),
	0x8035FF42: main.sym("shadow_bgcode"),
	0x8035FF44: main.sym("shadow_onwater", flag={"GLOBL"}),
	0x8035FF45: main.sym("shadow_ondecal", flag={"GLOBL"}),

	# src/background.c
	0x8035FF50: main.sym("backdata"),

	# src/water.c
	0x8035FF70: main.sym("water_txt"),

	# src/objshape.c
	0x8035FF80: main.sym("objshape_803612F0", flag={"GLOBL"}),

	# src/wave.c
	0x8035FF90: main.sym("wave_bgcode"),
	0x8035FF94: main.sym("wave_posx"),
	0x8035FF98: main.sym("wave_posy"),
	0x8035FF9C: main.sym("wave_posz"),
	0x8035FFA0: main.sym("wavevtx"),
	0x8035FFA4: main.sym("wavenorm"),
	0x8035FFA8: main.sym("wavep", flag={"GLOBL"}),
	0x8035FFAC: main.sym("wave_8036131C", flag={"GLOBL"}),

	# src/dprint.c
	0x8035FFB0: main.sym("dprint_table"),

	# src/message.c
	0x80360080: main.sym("msg_theta"),
	0x80360082: main.sym("msg_cursor_line"),
	0x80360084: main.sym("msg_value"),
	0x80360088: main.sym("msg_alpha"),
	0x8036008A: main.sym("caption_x"),
	0x8036008C: main.sym("caption_y"),
	0x8036008E: main.sym("redcoin_count", flag={"GLOBL"}),

	# src/weather.c
	0x80360090: main.sym("weatherp", flag={"GLOBL"}),
	0x80360098: main.sym("snow_pos"),
	0x803600A4: main.sym("snow_len"),
	0x803600A6: main.sym("snow_max"),

	# src/lava.c
	0x803600B0: main.sym("lava_info", flag={"GLOBL"}),
	0x803600C4: main.sym("lava_glistp"),
	0x803600C8: main.sym("lava_max"),
	0x803600CC: main.sym("lava_len"),

	# src/hud.c
	0x803600D0: main.sym("meter_power"),

	# src/object_b.c
	0x803600E0: main.sym("object_b_80361450", flag={"GLOBL"}),

	# src/object_c.c
	0x803600F0: main.sym("object_c_80361460", flag={"GLOBL"}),
	0x803600F4: main.sym("object_c_80361464", flag={"GLOBL"}),
	0x803600F8: main.sym("object_c_80361468", flag={"GLOBL"}),
	0x803600FC: main.sym("object_c_8036146C", flag={"GLOBL"}),
	0x80360100: main.sym("object_c_80361470", flag={"GLOBL"}),
	0x80360104: main.sym("object_c_80361474", flag={"GLOBL"}),
	0x80360108: main.sym("object_c_80361478", flag={"GLOBL"}),
	0x8036010C: main.sym("object_c_8036147C", flag={"GLOBL"}),
	0x80360110: main.sym("object_c_80361480", flag={"GLOBL"}),
	0x80360114: main.sym("object_c_80361484", flag={"GLOBL"}),
	0x80360118: main.sym("object_c_80361488", flag={"GLOBL"}),

	# src/audio/game.c
	0x80360120: main.sym("_Na_game_bss"),

	# libultra
	0x80363830: main.sym("__osEventStateTab"),
	0x803638B0: main.sym("tmp_task"),
	0x803638F0: main.sym("viThread"),
	0x80363AA0: main.sym("viThreadStack"),
	0x80364AA0: main.sym("viEventQueue"),
	0x80364AB8: main.sym("viEventBuf"),
	0x80364AD0: main.sym("viRetraceMsg"),
	0x80364AE8: main.sym("viCounterMsg"),
	0x80364AFC: main.sym("viMgrMain__retrace"),
	0x80364B00: main.sym("piThread"),
	0x80364CB0: main.sym("piThreadStack"),
	0x80365CB0: main.sym("piEventQueue"),
	0x80365CC8: main.sym("piEventBuf"),
	0x80365CD0: main.sym("__osFinalrom"),
	0x80365CE0: main.sym("__osContPifRam"),
	0x80365D20: main.sym("__osContLastCmd"),
	0x80365D21: main.sym("__osMaxControllers"),
	0x80365D28: main.sym("__osEepromTimer"),
	0x80365D48: main.sym("__osEepromTimerQ"),
	0x80365D60: main.sym("__osEepromTimerMsg"),
	0x80365D70: main.sym("guRotateF__dtor"),
	0x80365D80: main.sym("__osBaseTimer"),
	0x80365DA0: main.sym("__osCurrentTime"),
	0x80365DA8: main.sym("__osBaseCounter"),
	0x80365DAC: main.sym("__osViIntrCount"),
	0x80365DB0: main.sym("__osTimerCounter"),
	0x80365DC0: main.sym("piAccessBuf"),
	0x80365DC8: main.sym("__osPiAccessQueue"),
	0x80365DE0: main.sym("siAccessBuf"),
	0x80365DE8: main.sym("__osSiAccessQueue"),
	0x80365E00: main.sym("__osEepPifRam"),
	0x80365E40: main.sym("kdebugserver__buffer"),
	0x80365F40: main.sym("__osThreadSave"),

	# ==========================================================================
	# buffer
	# ==========================================================================

	# src/zimg.c
	0x80000400: main.sym("z_image", flag={"GLOBL"}),

	# src/timg.c
	0x801C1000: main.sym("t_image", flag={"GLOBL"}),

	# src/audio/heap.c
	0x801CE000: main.sym("Na_Heap", flag={"GLOBL"}),
	0x801FF200: main.sym("Na_SpYield", flag={"GLOBL"}),
	0x801FF600: main.sym("Na_SpStack", flag={"GLOBL"}),

	# src/buffer.c
	0x80200600: main.sym("entry_stack", flag={"GLOBL"}),
	0x80200A00: main.sym("idle_stack", flag={"GLOBL"}),
	0x80201200: main.sym("sched_stack", flag={"GLOBL"}),
	0x80203200: main.sym("aud_stack", flag={"GLOBL"}),
	0x80205200: main.sym("gfx_stack", flag={"GLOBL"}),
	0x80207200: main.sym("gfx_sp_yield", flag={"GLOBL"}),
	0x80207B00: main.sym("backup", flag={"GLOBL"}),
	0x80207D00: main.sym("gfx_sp_stack", flag={"GLOBL"}),
	0x80208100: main.sym("frame_data", flag={"GLOBL"}),

	# src/audio/work.c
	#0x80220DA0: main.sym("Na_WorkStart"),
	#0x80220DB0: main.sym("_Na_work_bss_10"),
	0x80226EB8: main.sym("Na_Random"),
	#0x80226CC0: main.sym("_Na_work_80226CC0"),
	# 0x80220DA0 (max 0x6260)

	# src/fifo.c
	0x80227000: main.sym("gfx_fifo", flag={"GLOBL"}),

	# src/cimg.c
	0x8038F800: main.sym("c_image_a", flag={"GLOBL"}),
	0x803B5000: main.sym("c_image_b", flag={"GLOBL"}),
	0x803DA800: main.sym("c_image_c", flag={"GLOBL"}),

	# shape
	0x03007940: main.sym("gfx_redcoin_0"),
	0x03007968: main.sym("gfx_redcoin_1"),
	0x03007990: main.sym("gfx_redcoin_2"),
	0x030079B8: main.sym("gfx_redcoin_3"),
	0x03009AC8: main.sym("map_pipe"),

	# select
	0x0700ABD0: main.sym("txt_selfont"),
	0x0700CD08: main.sym("txt_smfont"),

	# stage
	# 4
	0x07026E24: main.sym("water_0400"),
	0x07026E34: main.sym("water_0401"),
	# 5
	0x07016708: main.sym("water_0501"),
	# 6
	0x070790F0: main.sym("water_0600"),
	0x07079100: main.sym("water_0612"),
	# 7
	0x0702B900: main.sym("water_0701"),
	0x0702B950: main.sym("water_0702"),
	# 8
	0x07004930: main.sym("fluid_0801S"),
	0x070049B4: main.sym("fluid_0802S"),
	0x07012778: main.sym("water_0801"),
	0x070127C8: main.sym("water_0851"),
	# 10
	0x0700FA70: main.sym("water_1001"),
	# 11
	0x07018748: main.sym("water_1101"),
	0x07018778: main.sym("water_1102"),
	# 12
	0x0700D2CC: main.sym("water_1201"),
	0x0700D304: main.sym("water_1205"),
	0x0701139C: main.sym("water_1202"),
	# 13
	0x0700E31C: main.sym("water_1301"),
	0x0700E39C: main.sym("water_1302"),
	# 14
	0x07016840: main.sym("fluid_1400L"),
	0x07016904: main.sym("fluid_1401L"),
	# 16
	0x0700EA58: main.sym("gfx_grounds_0700EA58"),
	0x07010E80: main.sym("water_1601"),
	# 22
	0x07028810: main.sym("water_2202"),
	# 23
	0x0700FCB4: main.sym("water_2301"),
	0x0700FD00: main.sym("water_2302"),
	# 24
	0x07011E08: main.sym("water_2401"),
	# 26
	0x07006E6C: main.sym("water_2601"),
	# 36
	0x07017124: main.sym("water_3601"),
}

seg_J0_code_data = {
	#0x80330F00: "J0.BackgroundA",
	#0x80330F04: "J0.BackgroundD",
	#0x80330F08: "J0.BackgroundE",
	#0x80330F0C: "J0.BackgroundF",
	#0x80330F10: "J0.BackgroundB",
	#0x80330F14: "J0.BackgroundG",
	#0x80330F18: "J0.BackgroundH",
	#0x80330F1C: "J0.BackgroundI",
	#0x80330F20: "J0.BackgroundC",
	#0x80330F24: "J0.BackgroundJ",
}

sym_E0_rspboot_text = {
	0x8032B260: main.sym("rspbootTextStart"),
	0x8032B330: main.sym("rspbootTextEnd"),
}

sym_E0_gspFast3D_fifo_text = {
	0x8032B330: main.sym("gspFast3D_fifoTextStart"),
	0x8032C738: main.sym("gspFast3D_fifoTextEnd"),
}

sym_E0_aspMain_text = {
	0x8032C740: main.sym("aspMainTextStart"),
	0x8032D560: main.sym("aspMainTextEnd"),
}

sym_E0_gspFast3D_fifo_data = {
	0x80339AC0: main.sym("gspFast3D_fifoDataStart"),
	0x8033A2C0: main.sym("gspFast3D_fifoDataEnd"),
}

sym_E0_aspMain_data = {
	0x8033A2C0: main.sym("aspMainDataStart"),
	0x8033A580: main.sym("aspMainDataEnd"),
}

sym_E0_crt0_text = {
	# ==========================================================================
	# text
	# ==========================================================================

	# src/crt0.s
	0x80246000: main.sym("_start", flag={"GLOBL"}),

	0x80200600: main.sym("entry_stack+1024"),
	0x8033A580: main.sym("_codeSegmentBssStart"),
}

sym_E0_code_text = {
	0x000F5580: main.sym("_ulibSegmentRomStart"),
	0x00108A10: main.sym("_ulibSegmentRomEnd"),
	0x0036F530: main.sym("_WeatherSegmentRomStart"),

	# ==========================================================================
	# text
	# ==========================================================================

	# src/main.c
	0x80246050: main.sym_fnc("DebugCheck", flag={"GLOBL"}), # unused
	0x80246170: main.sym_fnc("dummy"), # unused
	0x802461CC: main.sym_fnc("DebugEntry"),
	0x802461DC: main.sym_fnc("DebugSchedProc"),
	0x802461EC: main.sym_fnc("DebugSchedVI"),
	0x802461FC: main.sym_fnc("ScInit"),
	0x802462E0: main.sym_fnc("ScInitMem"),
	0x80246338: main.sym_fnc("CreateThread", arg=(
		"OSThread *t",
		"OSId id",
		"void (*entry)(void *)",
		"void *arg",
		"void *sp",
		"OSPri pri",
	)),
	0x8024639C: main.sym_fnc("ScEventPreNMI"),
	0x802463EC: main.sym_fnc("ScTaskFlush"),
	0x8024651C: main.sym_fnc("ScTaskStart", arg=(
		"int type",
	)),
	0x8024659C: main.sym_fnc("ScTaskYield"),
	0x802465EC: main.sym_fnc("ScEventGfxTask"),
	0x80246648: main.sym_fnc("ScSkipAudTask"),
	0x8024669C: main.sym_fnc("ScEventVI"),
	0x802467FC: main.sym_fnc("ScEventSP"),
	0x8024694C: main.sym_fnc("ScEventDP"),
	0x802469B8: main.sym_fnc("SchedProc", arg=(
		"void *arg",
	)),
	0x80246A9C: main.sym_fnc("L80246A9C", flag={"GLOBL","LOCAL"}),
	0x80246AAC: main.sym_fnc("L80246AAC", flag={"GLOBL","LOCAL"}),
	0x80246ABC: main.sym_fnc("L80246ABC", flag={"GLOBL","LOCAL"}),
	0x80246ACC: main.sym_fnc("L80246ACC", flag={"GLOBL","LOCAL"}),
	0x80246ADC: main.sym_fnc("L80246ADC", flag={"GLOBL","LOCAL"}),
	0x80246B14: main.sym_fnc("ScSetClient", arg=(
		"int i",
		"SCCLIENT *client",
		"OSMesgQueue *mq",
		"OSMesg msg",
	), flag={"GLOBL"}),
	0x80246B74: main.sym_fnc("ScQueueTask", arg=(
		"SCTASK *task",
	), flag={"GLOBL"}), # unused
	0x80246BB4: main.sym_fnc("ScQueueAudTask", arg=(
		"SCTASK *task",
	), flag={"GLOBL"}),
	0x80246C10: main.sym_fnc("ScQueueGfxTask", arg=(
		"SCTASK *task",
	), flag={"GLOBL"}),
	0x80246C9C: main.sym_fnc("ScAudEnable", flag={"GLOBL"}), # unused
	0x80246CB8: main.sym_fnc("ScAudDisable", flag={"GLOBL"}), # unused
	0x80246CF0: main.sym_fnc("IdleProc", arg=(
		"void *arg",
	)),
	0x80246DF8: main.sym_fnc("entry", flag={"GLOBL"}),

	# src/graphics.c
	0x80246E70: main.sym_fnc("GfxInitDP"),
	0x802471A4: main.sym_fnc("GfxInitSP"),
	0x80247284: main.sym_fnc("GfxInitZB"),
	0x802473C8: main.sym_fnc("GfxInitCB"),
	0x802474B8: main.sym_fnc("GfxClear", arg=(
		"u32 fill",
	), flag={"GLOBL"}),
	0x80247620: main.sym_fnc("GfxVpClear", arg=(
		"Vp *vp",
		"u32 fill",
	), flag={"GLOBL"}),
	0x8024784C: main.sym_fnc("GfxDrawBorder"),
	0x802479BC: main.sym_fnc("GfxVpScissor", arg=(
		"Vp *vp",
	), flag={"GLOBL"}),
	0x80247B3C: main.sym_fnc("GfxMakeTask"),
	0x80247CCC: main.sym_fnc("GfxStart", flag={"GLOBL"}),
	0x80247D14: main.sym_fnc("GfxEnd", flag={"GLOBL"}),
	0x80247DB4: main.sym_fnc("GfxReset"),
	0x80247F08: main.sym_fnc("FrameInit"),
	0x80247FDC: main.sym_fnc("FrameStart"),
	0x80248090: main.sym_fnc("FrameEnd"),
	0x802481E0: main.sym_fnc("DemoRecord"), # unused
	0x80248304: main.sym_fnc("ContProcStick", arg=(
		"CONTROLLER *cont",
	)),
	0x80248498: main.sym_fnc("DemoProc"),
	0x80248638: main.sym_fnc("ContProc"),
	0x80248824: main.sym_fnc("ContInit"),
	0x80248964: main.sym_fnc("GfxInit"),
	0x80248AF0: main.sym_fnc("GfxProc", arg=(
		"void *arg",
	), flag={"GLOBL"}),

	# src/audio.c
	0x80248C40: main.sym_fnc("AudResetMute", flag={"GLOBL"}),
	0x80248C58: main.sym_fnc("AudSetMute", arg=(
		"int flag",
	), flag={"GLOBL"}),
	0x80248CE8: main.sym_fnc("AudClrMute", arg=(
		"int flag",
	), flag={"GLOBL"}),
	0x80248D78: main.sym_fnc("AudLock", flag={"GLOBL"}),
	0x80248DC0: main.sym_fnc("AudUnlock", flag={"GLOBL"}),
	0x80248E08: main.sym_fnc("AudSetMode", arg=(
		"USHORT mode",
	), flag={"GLOBL"}),
	0x80248E54: main.sym_fnc("AudPlayFaceSound", arg=(
		"SHORT flag",
	), flag={"GLOBL"}),
	0x80248FEC: main.sym_fnc("AudProcWaveSound", flag={"GLOBL"}),
	0x80249070: main.sym_fnc("AudProcEndlessMusic", flag={"GLOBL"}),
	0x80249178: main.sym_fnc("AudPlayBGM", arg=(
		"USHORT mode",
		"USHORT bgm",
		"SHORT fadein",
	), flag={"GLOBL"}),
	0x8024922C: main.sym_fnc("AudFadeout", arg=(
		"SHORT fadeout",
	), flag={"GLOBL"}),
	0x8024927C: main.sym_fnc("AudFadeoutBGM", arg=(
		"SHORT fadeout",
	), flag={"GLOBL"}),
	0x802492D0: main.sym_fnc("AudPlayStageBGM", arg=(
		"USHORT bgm",
	), flag={"GLOBL"}),
	0x80249310: main.sym_fnc("AudPlayShellBGM", flag={"GLOBL"}),
	0x8024934C: main.sym_fnc("AudStopShellBGM", flag={"GLOBL"}),
	0x80249398: main.sym_fnc("AudPlaySpecialBGM", arg=(
		"USHORT bgm",
	), flag={"GLOBL"}),
	0x80249404: main.sym_fnc("AudFadeoutSpecialBGM", flag={"GLOBL"}),
	0x80249448: main.sym_fnc("AudStopSpecialBGM", flag={"GLOBL"}),
	0x80249494: main.sym_fnc("AudPlayLevelSe", arg=(
		"int se",
		"FVEC pos",
	), flag={"GLOBL"}),
	0x802494D8: main.sym_fnc("AudTick", flag={"GLOBL"}),
	0x80249500: main.sym_fnc("AudProc", arg=(
		"void *arg",
	), flag={"GLOBL"}),

	# src/game.c
	0x802495E0: main.sym_fnc("GmTimeCtrl", "int", arg=(
		"int code",
	), flag={"GLOBL"}),
	0x802496B8: main.sym_fnc("GmCheckPause", "int"),
	0x80249764: main.sym_fnc("GmSetState", arg=(
		"SHORT state",
	)),
	0x8024978C: main.sym_fnc("GmExit", arg=(
		"int code",
	)),
	0x802497B8: main.sym_fnc("GmFadeout", arg=(
		"int code",
		"int color",
	), flag={"GLOBL"}),
	0x8024982C: main.sym_fnc("game_8024982C"), # unused
	0x8024983C: main.sym_fnc("GmInitMessage", arg=(
		"int index",
	), flag={"GLOBL"}),
	0x8024995C: main.sym_fnc("PL_InitDoor", arg=(
		"ACTOR *actor",
		"u32 code",
	)),
	0x80249A10: main.sym_fnc("PL_InitCap", arg=(
		"PLAYER *pl",
	)),
	0x80249AB4: main.sym_fnc("PL_InitState", arg=(
		"PLAYER *pl",
		"int type",
		"u32 code",
	)),
	0x80249AF4: main.sym_fnc("L80249AF4", flag={"GLOBL","LOCAL"}),
	0x80249B0C: main.sym_fnc("L80249B0C", flag={"GLOBL","LOCAL"}),
	0x80249B28: main.sym_fnc("L80249B28", flag={"GLOBL","LOCAL"}),
	0x80249B40: main.sym_fnc("L80249B40", flag={"GLOBL","LOCAL"}),
	0x80249B58: main.sym_fnc("L80249B58", flag={"GLOBL","LOCAL"}),
	0x80249B74: main.sym_fnc("L80249B74", flag={"GLOBL","LOCAL"}),
	0x80249B8C: main.sym_fnc("L80249B8C", flag={"GLOBL","LOCAL"}),
	0x80249BA8: main.sym_fnc("L80249BA8", flag={"GLOBL","LOCAL"}),
	0x80249BC0: main.sym_fnc("L80249BC0", flag={"GLOBL","LOCAL"}),
	0x80249BD8: main.sym_fnc("L80249BD8", flag={"GLOBL","LOCAL"}),
	0x80249BF0: main.sym_fnc("L80249BF0", flag={"GLOBL","LOCAL"}),
	0x80249C0C: main.sym_fnc("L80249C0C", flag={"GLOBL","LOCAL"}),
	0x80249C28: main.sym_fnc("L80249C28", flag={"GLOBL","LOCAL"}),
	0x80249C40: main.sym_fnc("L80249C40", flag={"GLOBL","LOCAL"}),
	0x80249C58: main.sym_fnc("L80249C58", flag={"GLOBL","LOCAL"}),
	0x80249C70: main.sym_fnc("L80249C70", flag={"GLOBL","LOCAL"}),
	0x80249C88: main.sym_fnc("L80249C88", flag={"GLOBL","LOCAL"}),
	0x80249CA0: main.sym_fnc("L80249CA0", flag={"GLOBL","LOCAL"}),
	0x80249CB8: main.sym_fnc("L80249CB8", flag={"GLOBL","LOCAL"}),
	0x80249CD8: main.sym_fnc("GmInitPort"),
	0x80249EA4: main.sym_fnc("L80249EA4", flag={"GLOBL","LOCAL"}),
	0x80249EC4: main.sym_fnc("L80249EC4", flag={"GLOBL","LOCAL"}),
	0x80249EE4: main.sym_fnc("L80249EE4", flag={"GLOBL","LOCAL"}),
	0x80249F08: main.sym_fnc("L80249F08", flag={"GLOBL","LOCAL"}),
	0x80249F2C: main.sym_fnc("L80249F2C", flag={"GLOBL","LOCAL"}),
	0x80249F4C: main.sym_fnc("L80249F4C", flag={"GLOBL","LOCAL"}),
	0x80249F6C: main.sym_fnc("L80249F6C", flag={"GLOBL","LOCAL"}),
	0x8024A124: main.sym_fnc("GmProcEntry"),
	0x8024A18C: main.sym_fnc("GmInitStage"),
	0x8024A1D8: main.sym_fnc("GmInitStaff"),
	0x8024A374: main.sym_fnc("GmProcConnect"),
	0x8024A584: main.sym_fnc("GmIsSameBGM", "int", (
		"SHORT port",
	)),
	0x8024A700: main.sym_fnc("GmSetEntry", arg=(
		"SHORT stage",
		"SHORT scene",
		"SHORT port",
		"u32 code",
	)),
	0x8024A7B4: main.sym_fnc("GmGetBGPort", "BGPORT *"),
	0x8024A85C: main.sym_fnc("GmProcBGPort"),
	0x8024A9CC: main.sym_fnc("PL_Fade", "int", (
		"PLAYER *pl",
		"int mode",
	), flag={"GLOBL"}),
	0x8024AA44: main.sym_fnc("L8024AA44", flag={"GLOBL","LOCAL"}),
	0x8024AA88: main.sym_fnc("L8024AA88", flag={"GLOBL","LOCAL"}),
	0x8024AACC: main.sym_fnc("L8024AACC", flag={"GLOBL","LOCAL"}),
	0x8024AB0C: main.sym_fnc("L8024AB0C", flag={"GLOBL","LOCAL"}),
	0x8024AB74: main.sym_fnc("L8024AB74", flag={"GLOBL","LOCAL"}),
	0x8024ABEC: main.sym_fnc("L8024ABEC", flag={"GLOBL","LOCAL"}),
	0x8024AC3C: main.sym_fnc("L8024AC3C", flag={"GLOBL","LOCAL"}),
	0x8024AC8C: main.sym_fnc("L8024AC8C", flag={"GLOBL","LOCAL"}),
	0x8024ACF0: main.sym_fnc("L8024ACF0", flag={"GLOBL","LOCAL"}),
	0x8024AD60: main.sym_fnc("L8024AD60", flag={"GLOBL","LOCAL"}),
	0x8024ADC0: main.sym_fnc("L8024ADC0", flag={"GLOBL","LOCAL"}),
	0x8024ADEC: main.sym_fnc("L8024ADEC", flag={"GLOBL","LOCAL"}),
	0x8024AE60: main.sym_fnc("L8024AE60", flag={"GLOBL","LOCAL"}),
	0x8024AEDC: main.sym_fnc("GmProcFade"),
	0x8024AFC4: main.sym_fnc("L8024AFC4", flag={"GLOBL","LOCAL"}),
	0x8024AFDC: main.sym_fnc("L8024AFDC", flag={"GLOBL","LOCAL"}),
	0x8024AFF8: main.sym_fnc("L8024AFF8", flag={"GLOBL","LOCAL"}),
	0x8024B008: main.sym_fnc("L8024B008", flag={"GLOBL","LOCAL"}),
	0x8024B03C: main.sym_fnc("L8024B03C", flag={"GLOBL","LOCAL"}),
	0x8024B13C: main.sym_fnc("GmProcHUD"),
	0x8024B390: main.sym_fnc("GmSceneProc", arg=(
		"short *timer",
	)),
	0x8024B3E4: main.sym_fnc("GmProcNormal", "int"),
	0x8024B5D4: main.sym_fnc("GmProcPause", "int"),
	0x8024B6CC: main.sym_fnc("GmProcFrameAdv", "int"),
	0x8024B798: main.sym_fnc("GmFreeze", arg=(
		"SHORT timer",
		"FREEZECALL *callback",
	), flag={"GLOBL"}),
	0x8024B7C0: main.sym_fnc("GmProcFreeze", "int"),
	0x8024B880: main.sym_fnc("GmProcExit", "int"),
	0x8024B940: main.sym_fnc("GmProcExitOLD", "int"),
	0x8024B9B8: main.sym_fnc("GmProc", "int"),
	0x8024B9EC: main.sym_fnc("L8024B9EC", flag={"GLOBL","LOCAL"}),
	0x8024BA00: main.sym_fnc("L8024BA00", flag={"GLOBL","LOCAL"}),
	0x8024BA14: main.sym_fnc("L8024BA14", flag={"GLOBL","LOCAL"}),
	0x8024BA28: main.sym_fnc("L8024BA28", flag={"GLOBL","LOCAL"}),
	0x8024BA3C: main.sym_fnc("L8024BA3C", flag={"GLOBL","LOCAL"}),
	0x8024BA50: main.sym_fnc("L8024BA50", flag={"GLOBL","LOCAL"}),
	0x8024BA8C: main.sym_fnc("GmInit", "int"),
	0x8024BCD8: main.sym_fnc("GameProc", "long", (
		"SHORT code",
		"long status",
	), flag={"GLOBL"}), # prgcall
	0x8024BD5C: main.sym_fnc("GameInit", "long", (
		"SHORT code",
		"long status",
	), flag={"GLOBL"}), # prgcall
	0x8024BE14: main.sym_fnc("GameCheckSelect", "long", (
		"SHORT code",
		"long status",
	), flag={"GLOBL"}), # prgcall
	0x8024BFA0: main.sym_fnc("EndingSound", "long", (
		"SHORT code",
		"long status",
	), flag={"GLOBL"}), # prgcall

	# src/collision.c
	0x8024BFF0: main.sym_fnc("ObjGetCapFlag", "u32", (
		"OBJECT *obj",
	)),
	0x8024C0B8: main.sym_fnc("PL_IsFacingObj", "int", (
		"PLAYER *pl",
		"OBJECT *obj",
		"SHORT range",
	)),
	0x8024C16C: main.sym_fnc("PL_GetAngToObj", "SHORT", (
		"PLAYER *pl",
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x8024C1D8: main.sym_fnc("PL_CheckAttack", "int", (
		"PLAYER *pl",
		"OBJECT *obj",
	)),
	0x8024C51C: main.sym_fnc("ObjAttack", "int", (
		"OBJECT *obj",
		"int flag",
	)),
	0x8024C590: main.sym_fnc("L8024C590", flag={"GLOBL","LOCAL"}),
	0x8024C5A0: main.sym_fnc("L8024C5A0", flag={"GLOBL","LOCAL"}),
	0x8024C5B0: main.sym_fnc("L8024C5B0", flag={"GLOBL","LOCAL"}),
	0x8024C5C0: main.sym_fnc("L8024C5C0", flag={"GLOBL","LOCAL"}),
	0x8024C5F0: main.sym_fnc("L8024C5F0", flag={"GLOBL","LOCAL"}),
	0x8024C618: main.sym_fnc("PL_StopRide", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8024C66C: main.sym_fnc("PL_TakeObject", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8024C6C0: main.sym_fnc("PL_DropObject", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8024C780: main.sym_fnc("PL_ThrowObject", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8024C894: main.sym_fnc("PL_DropAll", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8024C8FC: main.sym_fnc("PL_IsWearingDefCap", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8024C928: main.sym_fnc("PL_BlowCap", arg=(
		"PLAYER *pl",
		"float speed",
	), flag={"GLOBL"}),
	0x8024CA68: main.sym_fnc("MarioStealCap", "int", (
		"int flag",
	), flag={"GLOBL"}),
	0x8024CAF8: main.sym_fnc("MarioReturnCap", flag={"GLOBL"}),
	0x8024CB58: main.sym_fnc("PL_IsTaking", "int", (
		"PLAYER *pl",
		"OBJECT *obj",
	)),
	0x8024CBFC: main.sym_fnc("PL_GetHitObj", "OBJECT *", (
		"PLAYER *pl",
		"int code",
	), flag={"GLOBL"}),
	0x8024CC7C: main.sym_fnc("PL_CheckTaking", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8024CE08: main.sym_fnc("PL_BumpObject", "u32", (
		"PLAYER *pl",
	)),
	0x8024D0B4: main.sym_fnc("PL_Stomp", arg=(
		"PLAYER *pl",
		"OBJECT *obj",
		"float vely",
	)),
	0x8024D130: main.sym_fnc("PL_HeadAttack", arg=(
		"PLAYER *pl",
		"OBJECT *obj",
	)),
	0x8024D16C: main.sym_fnc("PL_GetBlowState", "u32", (
		"PLAYER *pl",
	)), # unused
	0x8024D2BC: main.sym_fnc("PL_GetDamageState", "u32", (
		"PLAYER *pl",
		"int ap",
	)),
	0x8024D578: main.sym_fnc("PL_RepelFromObj", arg=(
		"PLAYER *pl",
		"OBJECT *obj",
		"float gap",
	)),
	0x8024D72C: main.sym_fnc("PL_PunchKickRecoil", arg=(
		"PLAYER *pl",
		"int flag",
	)),
	0x8024D804: main.sym_fnc("PL_GetDoorCode", "int", (
		"PLAYER *pl",
		"OBJECT *obj",
	)),
	0x8024D8B0: main.sym_fnc("PL_TakeDamage", "int", (
		"PLAYER *pl",
	)),
	0x8024D998: main.sym_fnc("PL_CheckDamage", "int", (
		"PLAYER *pl",
		"OBJECT *obj",
	)),
	0x8024DAAC: main.sym_fnc("collision_8024DAAC", arg=(
		"PLAYER *pl",
	)),
	0x8024DB2C: main.sym_fnc("PL_CollideCoin", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024DBF0: main.sym_fnc("PL_CollideRecover", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024DC28: main.sym_fnc("PL_CollideStar", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024DE4C: main.sym_fnc("PL_CollideCage", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024DF10: main.sym_fnc("PL_CollidePipe", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024E0C4: main.sym_fnc("PL_CollidePortDoor", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024E2FC: main.sym_fnc("PL_GetStarDoorFlag", "u32", (
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x8024E388: main.sym_fnc("L8024E388", flag={"GLOBL","LOCAL"}),
	0x8024E3B0: main.sym_fnc("L8024E3B0", flag={"GLOBL","LOCAL"}),
	0x8024E3D8: main.sym_fnc("L8024E3D8", flag={"GLOBL","LOCAL"}),
	0x8024E3E8: main.sym_fnc("L8024E3E8", flag={"GLOBL","LOCAL"}),
	0x8024E3F8: main.sym_fnc("L8024E3F8", flag={"GLOBL","LOCAL"}),
	0x8024E408: main.sym_fnc("L8024E408", flag={"GLOBL","LOCAL"}),
	0x8024E420: main.sym_fnc("PL_CollideDoor", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024E5A4: main.sym_fnc("L8024E5A4", flag={"GLOBL","LOCAL"}),
	0x8024E5B4: main.sym_fnc("L8024E5B4", flag={"GLOBL","LOCAL"}),
	0x8024E5C4: main.sym_fnc("L8024E5C4", flag={"GLOBL","LOCAL"}),
	0x8024E5D4: main.sym_fnc("L8024E5D4", flag={"GLOBL","LOCAL"}),
	0x8024E5E4: main.sym_fnc("L8024E5E4", flag={"GLOBL","LOCAL"}),
	0x8024E5F4: main.sym_fnc("L8024E5F4", flag={"GLOBL","LOCAL"}),
	0x8024E604: main.sym_fnc("L8024E604", flag={"GLOBL","LOCAL"}),
	0x8024E6EC: main.sym_fnc("PL_CollideCannon", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024E778: main.sym_fnc("PL_CollideIgloo", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024E7D4: main.sym_fnc("PL_CollideTornado", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024E8F0: main.sym_fnc("PL_CollideWhirlpool", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024E9D0: main.sym_fnc("PL_CollideWind", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024EAD8: main.sym_fnc("PL_CollideBurn", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024EC54: main.sym_fnc("PL_CollideBullet", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024ED84: main.sym_fnc("PL_CollideClam", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024EE44: main.sym_fnc("PL_CollideBump", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024EFF8: main.sym_fnc("PL_CollideElecShock", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024F134: main.sym_fnc("PL_CollideDummy", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # unused
	0x8024F170: main.sym_fnc("PL_CollideEnemy", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024F1E0: main.sym_fnc("PL_CollideFlyEnemy", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024F354: main.sym_fnc("PL_CollideBounce", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024F4AC: main.sym_fnc("PL_CollideSpiny", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024F55C: main.sym_fnc("PL_CollideDamage", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024F5CC: main.sym_fnc("PL_CollideItemBox", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024F6A4: main.sym_fnc("PL_CollideShell", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024F7A8: main.sym_fnc("PL_CheckTaken", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)),
	0x8024F8BC: main.sym_fnc("PL_CollidePole", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024FA60: main.sym_fnc("PL_CollideHang", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024FB30: main.sym_fnc("PL_CollideCap", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024FD2C: main.sym_fnc("PL_CollideTake", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x8024FE6C: main.sym_fnc("PL_CanOpenMessage", "int", (
		"PLAYER *pl",
		"int flag",
	)),
	0x8024FF04: main.sym_fnc("PL_CheckReading", "int", (
		"PLAYER *pl",
		"OBJECT *obj",
	)),
	0x80250098: main.sym_fnc("PL_CheckTalking", "int", (
		"PLAYER *pl",
		"OBJECT *obj",
	)),
	0x80250198: main.sym_fnc("PL_CollideMessage", "int", (
		"PLAYER *pl",
		"u32 flag",
		"OBJECT *obj",
	)), # data
	0x80250230: main.sym_fnc("PL_CheckPunchKickWall", arg=(
		"PLAYER *pl",
	)),
	0x802503F0: main.sym_fnc("PL_CheckCollision", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x802505C8: main.sym_fnc("PL_CheckFall", arg=(
		"PLAYER *pl",
	)),
	0x8025065C: main.sym_fnc("PL_GroundBurn", arg=(
		"PLAYER *pl",
	)),
	0x80250724: main.sym_fnc("PL_StartTimer", arg=(
		"PLAYER *pl",
	)),
	0x80250778: main.sym_fnc("PL_StopTimer", arg=(
		"PLAYER *pl",
	)),
	0x802507FC: main.sym_fnc("PL_CheckGroundCollision", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),

	# src/player.c
	0x80250940: main.sym_fnc("PL_IsAnimeLast1F", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8025097C: main.sym_fnc("PL_IsAnimeLast2F", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x802509B8: main.sym_fnc("PL_SetAnime", "int", (
		"PLAYER *pl",
		"int index",
	), flag={"GLOBL"}),
	0x80250B04: main.sym_fnc("PL_SetAnimeV", "int", (
		"PLAYER *pl",
		"int index",
		"int speed",
	), flag={"GLOBL"}),
	0x80250C7C: main.sym_fnc("PL_SetAnimeFrame", arg=(
		"PLAYER *pl",
		"SHORT frame",
	), flag={"GLOBL"}),
	0x80250D38: main.sym_fnc("PL_IsAnimeAtFrame", "int", (
		"PLAYER *pl",
		"SHORT frame",
	), flag={"GLOBL"}),
	0x80250E54: main.sym_fnc("PL_GetAnimePos", "int", (
		"OBJECT *obj",
		"SHORT angy",
		"SVEC pos",
	), flag={"GLOBL"}),
	0x80251020: main.sym_fnc("PL_UseAnimePos", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x802510DC: main.sym_fnc("PL_GetAnimeY", "SHORT", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80251120: main.sym_fnc("PL_TrigSound", arg=(
		"PLAYER *pl",
		"Na_Se se",
		"u32 flag",
	), flag={"GLOBL"}),
	0x8025118C: main.sym_fnc("PL_TrigJumpVoice", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80251274: main.sym_fnc("PL_SetSpeedEffect", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80251310: main.sym_fnc("PL_PlayEffect", arg=(
		"PLAYER *pl",
		"Na_Se se",
		"int flag",
	), flag={"GLOBL"}),
	0x80251444: main.sym_fnc("PL_TrigEffect", arg=(
		"PLAYER *pl",
		"Na_Se se",
		"int flag",
	), flag={"GLOBL"}),
	0x802514AC: main.sym_fnc("PL_PlayLandEffect", arg=(
		"PLAYER *pl",
		"Na_Se se",
	), flag={"GLOBL"}),
	0x80251510: main.sym_fnc("PL_TrigLandEffect", arg=(
		"PLAYER *pl",
		"Na_Se se",
	), flag={"GLOBL"}),
	0x80251574: main.sym_fnc("PL_PlayFallEffect", arg=(
		"PLAYER *pl",
		"Na_Se se",
	), flag={"GLOBL"}),
	0x802515D8: main.sym_fnc("PL_TrigFallEffect", arg=(
		"PLAYER *pl",
		"Na_Se se",
	), flag={"GLOBL"}),
	0x8025163C: main.sym_fnc("PL_TrigJumpEffect", arg=(
		"PLAYER *pl",
		"Na_Se se",
		"Na_Se voice",
	), flag={"GLOBL"}),
	0x80251708: main.sym_fnc("PL_SetSpeed", arg=(
		"PLAYER *pl",
		"float speed",
	), flag={"GLOBL"}),
	0x8025177C: main.sym_fnc("PL_GetSlip", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80251818: main.sym_fnc("L80251818", flag={"GLOBL","LOCAL"}),
	0x80251828: main.sym_fnc("L80251828", flag={"GLOBL","LOCAL"}),
	0x80251838: main.sym_fnc("L80251838", flag={"GLOBL","LOCAL"}),
	0x80251848: main.sym_fnc("L80251848", flag={"GLOBL","LOCAL"}),
	0x802518A8: main.sym_fnc("PL_GetSurface", "u32", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x802519A8: main.sym_fnc("L802519A8", flag={"GLOBL","LOCAL"}),
	0x802519B4: main.sym_fnc("L802519B4", flag={"GLOBL","LOCAL"}),
	0x802519C4: main.sym_fnc("L802519C4", flag={"GLOBL","LOCAL"}),
	0x802519D4: main.sym_fnc("L802519D4", flag={"GLOBL","LOCAL"}),
	0x802519E4: main.sym_fnc("L802519E4", flag={"GLOBL","LOCAL"}),
	0x802519F4: main.sym_fnc("L802519F4", flag={"GLOBL","LOCAL"}),
	0x80251A48: main.sym_fnc("PL_CheckWall", "BGFACE *", (
		"FVEC pos",
		"float offset",
		"float radius",
	), flag={"GLOBL"}),
	0x80251AFC: main.sym_fnc("PL_CheckRoof", "float", (
		"FVEC pos",
		"float y",
		"BGFACE **roof",
	), flag={"GLOBL"}),
	0x80251B54: main.sym_fnc("PL_IsFaceDownSlope", "int", (
		"PLAYER *pl",
		"int flag",
	), flag={"GLOBL"}),
	0x80251BD4: main.sym_fnc("PL_IsSlipMin", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80251CFC: main.sym_fnc("PL_IsSlipMax", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80251E24: main.sym_fnc("PL_IsSlipJump", "int", (
		"PLAYER *pl",
	)),
	0x80251F24: main.sym_fnc("PL_CheckGroundYNear", "float", (
		"PLAYER *pl",
		"SHORT angy",
		"float dist",
	), flag={"GLOBL"}),
	0x80252000: main.sym_fnc("PL_GetGroundAngX", "SHORT", (
		"PLAYER *pl",
		"SHORT angy",
	), flag={"GLOBL"}),
	0x802521A0: main.sym_fnc("player_802521A0", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8025229C: main.sym_fnc("PL_SetSlipJump", arg=(
		"PLAYER *pl",
	)),
	0x802523C8: main.sym_fnc("PL_SetJumpSpeed", arg=(
		"PLAYER *pl",
		"float speed",
		"float scale",
	)),
	0x80252460: main.sym_fnc("PL_SetJump", "u32", (
		"PLAYER *pl",
		"u32 state",
		"u32 code",
	)),
	0x8025260C: main.sym_fnc("L8025260C", flag={"GLOBL","LOCAL"}),
	0x802526A4: main.sym_fnc("L802526A4", flag={"GLOBL","LOCAL"}),
	0x80252720: main.sym_fnc("L80252720", flag={"GLOBL","LOCAL"}),
	0x80252760: main.sym_fnc("L80252760", flag={"GLOBL","LOCAL"}),
	0x802527E4: main.sym_fnc("L802527E4", flag={"GLOBL","LOCAL"}),
	0x80252898: main.sym_fnc("L80252898", flag={"GLOBL","LOCAL"}),
	0x802529A4: main.sym_fnc("L802529A4", flag={"GLOBL","LOCAL"}),
	0x802529E4: main.sym_fnc("PL_SetMove", "u32", (
		"PLAYER *pl",
		"u32 state",
		"u32 code",
	)),
	0x80252BD4: main.sym_fnc("PL_SetSwim", "u32", (
		"PLAYER *pl",
		"u32 state",
		"u32 code",
	)),
	0x80252C18: main.sym_fnc("PL_SetDemo", "u32", (
		"PLAYER *pl",
		"u32 state",
		"u32 code",
	)),
	0x80252CF4: main.sym_fnc("PL_SetState", "int", (
		"PLAYER *pl",
		"u32 state",
		"u32 code",
	), flag={"GLOBL"}),
	0x80252E5C: main.sym_fnc("PL_SetTripJump", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x802530A0: main.sym_fnc("PL_SetStateJump", "int", (
		"PLAYER *pl",
		"u32 state",
		"u32 code",
	), flag={"GLOBL"}),
	0x80253178: main.sym_fnc("PL_SetStateDrop", "int", (
		"PLAYER *pl",
		"u32 state",
		"u32 code",
	), flag={"GLOBL"}),
	0x802531C4: main.sym_fnc("PL_SetStateDamage", "int", (
		"PLAYER *pl",
		"u32 state",
		"u32 code",
		"SHORT damage",
	), flag={"GLOBL"}),
	0x80253218: main.sym_fnc("PL_CheckMotion", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80253300: main.sym_fnc("PL_CheckMotionTake", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x802533E4: main.sym_fnc("PL_EnterField", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80253488: main.sym_fnc("PL_EnterWater", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80253588: main.sym_fnc("PL_ProcPress", arg=(
		"PLAYER *pl",
	)),
	0x80253720: main.sym_fnc("PL_ProcDebug", arg=(
		"PLAYER *pl",
	)),
	0x80253838: main.sym_fnc("PL_ProcButton", arg=(
		"PLAYER *pl",
	)),
	0x8025395C: main.sym_fnc("PL_ProcStick", arg=(
		"PLAYER *pl",
	)),
	0x80253A60: main.sym_fnc("PL_ProcBG", arg=(
		"PLAYER *pl",
	)),
	0x80253D58: main.sym_fnc("PL_ProcStatus", arg=(
		"PLAYER *pl",
	)),
	0x80253EC0: main.sym_fnc("PL_ProcSwimCamera", arg=(
		"PLAYER *pl",
	)),
	0x80254060: main.sym_fnc("PL_ProcPower", arg=(
		"PLAYER *pl",
	)),
	0x802542B4: main.sym_fnc("PL_ProcInfo", arg=(
		"PLAYER *pl",
	)),
	0x80254338: main.sym_fnc("PL_InitShape", arg=(
		"PLAYER *pl",
	)),
	0x80254390: main.sym_fnc("PL_ProcSink", arg=(
		"PLAYER *pl",
	)),
	0x802543E8: main.sym_fnc("PL_ProcCap", "u32", (
		"PLAYER *pl",
	)),
	0x80254588: main.sym_fnc("PL_ProcShape", arg=(
		"PLAYER *pl",
	)),
	0x80254768: main.sym_fnc("DebugCap", arg=(
		"USHORT button",
		"u32 flag",
		"USHORT timer",
		"USHORT bgm",
	)), # unused
	0x80254830: main.sym_fnc("MarioExec", "u32", (
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x80254B20: main.sym_fnc("MarioEnter", flag={"GLOBL"}),
	0x80254F44: main.sym_fnc("MarioInit", flag={"GLOBL"}),

	# src/physics.c
	0x80255080: main.sym_fnc("PL_GetTrampolinePower", "float", flag={"GLOBL"}),
	0x8025509C: main.sym_fnc("PL_ProcTrampoline", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x802550B0: main.sym_fnc("TrampolineProc", flag={"GLOBL"}),
	0x802550C0: main.sym_fnc("BumpCollision", arg=(
		"BUMP *a",
		"BUMP *b",
	), flag={"GLOBL"}),
	0x80255238: main.sym_fnc("BumpInit", arg=(
		"BUMP *bump",
		"float posx",
		"float posz",
		"float speed",
		"SHORT angy",
		"float power",
		"float radius",
	), flag={"GLOBL"}),
	0x802552FC: main.sym_fnc("PL_Reflect", arg=(
		"PLAYER *pl",
		"int flag",
	), flag={"GLOBL"}),
	0x80255414: main.sym_fnc("PL_Sink", "int", (
		"PLAYER *pl",
		"float sink",
	), flag={"GLOBL"}),
	0x802554B0: main.sym_fnc("L802554B0", flag={"GLOBL","LOCAL"}),
	0x802554FC: main.sym_fnc("L802554FC", flag={"GLOBL","LOCAL"}),
	0x80255548: main.sym_fnc("L80255548", flag={"GLOBL","LOCAL"}),
	0x80255594: main.sym_fnc("L80255594", flag={"GLOBL","LOCAL"}),
	0x802555F4: main.sym_fnc("L802555F4", flag={"GLOBL","LOCAL"}),
	0x80255620: main.sym_fnc("L80255620", flag={"GLOBL","LOCAL"}),
	0x80255654: main.sym_fnc("PL_SteepFall", "int", (
		"PLAYER *pl",
		"u32 state",
		"u32 code",
	), flag={"GLOBL"}),
	0x8025570C: main.sym_fnc("PL_ProcQuicksand", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8025580C: main.sym_fnc("PL_ProcWind", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x802559B0: main.sym_fnc("PL_Stop", arg=(
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80255A34: main.sym_fnc("PL_ProcWait", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80255B04: main.sym_fnc("PL_CheckWalk", "int", (
		"PLAYER *pl",
		"FVEC pos",
	)),
	0x80255D88: main.sym_fnc("PL_ProcWalk", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80255EC4: main.sym_fnc("PL_CheckLedge", "int", (
		"PLAYER *pl",
		"BGFACE *wall",
		"FVEC oldpos",
		"FVEC newpos",
	)),
	0x802560AC: main.sym_fnc("PL_CheckJump", "int", (
		"PLAYER *pl",
		"FVEC pos",
		"int flag",
	)),
	0x802564E0: main.sym_fnc("PL_ProcSpinGravity", arg=(
		"PLAYER *pl",
	)),
	0x80256584: main.sym_fnc("PL_IsJumpCancel", "int", (
		"PLAYER *pl",
	)),
	0x8025661C: main.sym_fnc("PL_ProcGravity", arg=(
		"PLAYER *pl",
	)),
	0x802569F8: main.sym_fnc("PL_ProcUpWind", arg=(
		"PLAYER *pl",
	)),
	0x80256B24: main.sym_fnc("PL_ProcJump", "int", (
		"PLAYER *pl",
		"int flag",
	), flag={"GLOBL"}),
	0x80256CD8: main.sym_fnc("PL_SetSpeed3D", arg=(
		"PLAYER *pl",
	)), # unused
	0x80256D8C: main.sym_fnc("PL_SetSpeed2D", arg=(
		"PLAYER *pl",
	)), # unused

	# src/pldemo.c
	0x80256E00: main.sym("pldemo_80256E00"),
	0x80256E88: main.sym_fnc("StaffDraw", flag={"GLOBL"}),
	0x80257060: main.sym("pldemo_80257060", flag={"GLOBL"}), # objcall
	0x802570DC: main.sym("pldemo_802570DC", flag={"GLOBL"}), # objcall
	0x80257198: main.sym("Ctrl_pldemo_80257198", flag={"GLOBL"}), # shpcall
	0x80257270: main.sym("pldemo_80257270"), # unused
	0x802572B0: main.sym("pldemo_802572B0"),
	0x8025733C: main.sym("pldemo_8025733C"),
	0x80257450: main.sym("pldemo_80257450"),
	0x802574E8: main.sym("pldemo_802574E8"),
	0x80257548: main.sym("pldemo_80257548"),
	0x802575A8: main.sym_fnc("pldemo_802575A8", "int", flag={"GLOBL"}),
	0x80257640: main.sym_fnc("pldemo_80257640", "int", (
		"int",
	), flag={"GLOBL"}),
	0x80257748: main.sym("pldemo_80257748"),
	0x80257980: main.sym("pldemo_80257980"),
	0x80257A0C: main.sym("pldemo_80257A0C"),
	0x80257AB0: main.sym("pldemo_80257AB0"),
	0x80257CE4: main.sym("pldemo_80257CE4"),
	0x80257EAC: main.sym("pldemo_80257EAC"),
	0x80258184: main.sym("pldemo_80258184"),
	0x80258420: main.sym("pldemo_80258420"),
	0x802584DC: main.sym("pldemo_802584DC"),
	0x802585C0: main.sym("pldemo_802585C0"),
	0x802586CC: main.sym("pldemo_802586CC"),
	0x80258744: main.sym("pldemo_80258744"),
	0x802587EC: main.sym("pldemo_802587EC"),
	0x8025883C: main.sym("pldemo_8025883C"),
	0x8025888C: main.sym("pldemo_8025888C"),
	0x802588F8: main.sym("pldemo_802588F8"),
	0x80258964: main.sym("pldemo_80258964"),
	0x80258A7C: main.sym("pldemo_80258A7C"),
	0x80258B24: main.sym("pldemo_80258B24"),
	0x80258BA8: main.sym("pldemo_80258BA8"),
	0x80258DAC: main.sym("pldemo_80258DAC"),
	0x80258F94: main.sym("pldemo_80258F94"),
	0x80259264: main.sym("pldemo_80259264"),
	0x802593CC: main.sym("pldemo_802593CC"),
	0x802594D4: main.sym("pldemo_802594D4"),
	0x80259608: main.sym("pldemo_80259608"),
	0x80259740: main.sym("pldemo_80259740"),
	0x802597AC: main.sym("pldemo_802597AC"),
	0x80259854: main.sym("pldemo_80259854"),
	0x802598D0: main.sym("pldemo_802598D0"),
	0x80259C30: main.sym("pldemo_80259C30"),
	0x80259CE8: main.sym("pldemo_80259CE8"),
	0x80259D74: main.sym("pldemo_80259D74"),
	0x80259E00: main.sym("pldemo_80259E00"),
	0x80259EF8: main.sym("pldemo_80259EF8"),
	0x80259FCC: main.sym("pldemo_80259FCC"),
	0x8025A040: main.sym("pldemo_8025A040"),
	0x8025A0BC: main.sym("pldemo_8025A0BC"),
	0x8025A1AC: main.sym_fnc("L8025A1AC", flag={"GLOBL","LOCAL"}),
	0x8025A244: main.sym_fnc("L8025A244", flag={"GLOBL","LOCAL"}),
	0x8025A2E0: main.sym_fnc("L8025A2E0", flag={"GLOBL","LOCAL"}),
	0x8025A450: main.sym_fnc("L8025A450", flag={"GLOBL","LOCAL"}),
	0x8025A494: main.sym("pldemo_8025A494"),
	0x8025A610: main.sym("pldemo_8025A610"),
	0x8025A6FC: main.sym("pldemo_8025A6FC"),
	0x8025A858: main.sym("pldemo_8025A858"),
	0x8025A9AC: main.sym("pldemo_8025A9AC"),
	0x8025AE0C: main.sym("pldemo_8025AE0C"),
	0x8025AEA8: main.sym("pldemo_8025AEA8"),
	0x8025AFFC: main.sym("pldemo_8025AFFC"),
	0x8025B050: main.sym("pldemo_8025B050"),
	0x8025B0A4: main.sym("pldemo_8025B0A4"),
	0x8025B0F8: main.sym("pldemo_8025B0F8"),
	0x8025B11C: main.sym("pldemo_8025B11C"),
	0x8025B178: main.sym("pldemo_8025B178"),
	0x8025B234: main.sym("pldemo_8025B234"),
	0x8025B2EC: main.sym("pldemo_8025B2EC"),
	0x8025B404: main.sym("pldemo_8025B404"),
	0x8025B454: main.sym("pldemo_8025B454"),
	0x8025B520: main.sym("pldemo_8025B520"),
	0x8025B58C: main.sym("pldemo_8025B58C"),
	0x8025B5C4: main.sym_fnc("L8025B5C4", flag={"GLOBL","LOCAL"}),
	0x8025B5D4: main.sym_fnc("L8025B5D4", flag={"GLOBL","LOCAL"}),
	0x8025B5E4: main.sym_fnc("L8025B5E4", flag={"GLOBL","LOCAL"}),
	0x8025B5F4: main.sym_fnc("L8025B5F4", flag={"GLOBL","LOCAL"}),
	0x8025B604: main.sym_fnc("L8025B604", flag={"GLOBL","LOCAL"}),
	0x8025B614: main.sym_fnc("L8025B614", flag={"GLOBL","LOCAL"}),
	0x8025B624: main.sym_fnc("L8025B624", flag={"GLOBL","LOCAL"}),
	0x8025B654: main.sym("pldemo_8025B654"),
	0x8025B760: main.sym("pldemo_8025B760"),
	0x8025B9A8: main.sym("pldemo_8025B9A8"),
	0x8025BBEC: main.sym("pldemo_8025BBEC"),
	0x8025BC80: main.sym("pldemo_8025BC80"),
	0x8025BEB8: main.sym("pldemo_8025BEB8"),
	0x8025BF64: main.sym("pldemo_8025BF64"),
	0x8025C014: main.sym("pldemo_8025C014"),
	0x8025C0C4: main.sym("pldemo_8025C0C4"),
	0x8025C1C0: main.sym("pldemo_8025C1C0"),
	0x8025C498: main.sym("pldemo_8025C498"),
	0x8025C600: main.sym("pldemo_8025C600"),
	0x8025C6F8: main.sym("pldemo_8025C6F8"),
	0x8025C904: main.sym("pldemo_8025C904"),
	0x8025CA48: main.sym("pldemo_8025CA48"),
	0x8025CBDC: main.sym("pldemo_8025CBDC"),
	0x8025CD6C: main.sym("pldemo_8025CD6C"),
	0x8025CEF0: main.sym("pldemo_8025CEF0"),
	0x8025CFE4: main.sym("pldemo_8025CFE4"),
	0x8025D040: main.sym("pldemo_8025D040"),
	0x8025D078: main.sym_fnc("L8025D078", flag={"GLOBL","LOCAL"}),
	0x8025D088: main.sym_fnc("L8025D088", flag={"GLOBL","LOCAL"}),
	0x8025D098: main.sym_fnc("L8025D098", flag={"GLOBL","LOCAL"}),
	0x8025D0A8: main.sym_fnc("L8025D0A8", flag={"GLOBL","LOCAL"}),
	0x8025D0B8: main.sym_fnc("L8025D0B8", flag={"GLOBL","LOCAL"}),
	0x8025D0C8: main.sym_fnc("L8025D0C8", flag={"GLOBL","LOCAL"}),
	0x8025D0D8: main.sym_fnc("L8025D0D8", flag={"GLOBL","LOCAL"}),
	0x8025D0E8: main.sym_fnc("L8025D0E8", flag={"GLOBL","LOCAL"}),
	0x8025D0F8: main.sym_fnc("L8025D0F8", flag={"GLOBL","LOCAL"}),
	0x8025D108: main.sym_fnc("L8025D108", flag={"GLOBL","LOCAL"}),
	0x8025D118: main.sym_fnc("L8025D118", flag={"GLOBL","LOCAL"}),
	0x8025D128: main.sym_fnc("L8025D128", flag={"GLOBL","LOCAL"}),
	0x8025D138: main.sym_fnc("L8025D138", flag={"GLOBL","LOCAL"}),
	0x8025D1D4: main.sym("pldemo_8025D1D4"),
	0x8025D4F0: main.sym("pldemo_8025D4F0"),
	0x8025D70C: main.sym("pldemo_8025D70C"),
	0x8025D798: main.sym_fnc("PL_ExecDemo", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8025D92C: main.sym_fnc("L8025D92C", flag={"GLOBL","LOCAL"}),
	0x8025D954: main.sym_fnc("L8025D954", flag={"GLOBL","LOCAL"}),
	0x8025D968: main.sym_fnc("L8025D968", flag={"GLOBL","LOCAL"}),
	0x8025D97C: main.sym_fnc("L8025D97C", flag={"GLOBL","LOCAL"}),
	0x8025D990: main.sym_fnc("L8025D990", flag={"GLOBL","LOCAL"}),
	0x8025D9CC: main.sym_fnc("L8025D9CC", flag={"GLOBL","LOCAL"}),
	0x8025D9E0: main.sym_fnc("L8025D9E0", flag={"GLOBL","LOCAL"}),
	0x8025D9F4: main.sym_fnc("L8025D9F4", flag={"GLOBL","LOCAL"}),
	0x8025DA08: main.sym_fnc("L8025DA08", flag={"GLOBL","LOCAL"}),
	0x8025DA1C: main.sym_fnc("L8025DA1C", flag={"GLOBL","LOCAL"}),
	0x8025DA30: main.sym_fnc("L8025DA30", flag={"GLOBL","LOCAL"}),
	0x8025DA44: main.sym_fnc("L8025DA44", flag={"GLOBL","LOCAL"}),
	0x8025DA58: main.sym_fnc("L8025DA58", flag={"GLOBL","LOCAL"}),
	0x8025DA6C: main.sym_fnc("L8025DA6C", flag={"GLOBL","LOCAL"}),
	0x8025DA80: main.sym_fnc("L8025DA80", flag={"GLOBL","LOCAL"}),
	0x8025DA94: main.sym_fnc("L8025DA94", flag={"GLOBL","LOCAL"}),
	0x8025DAA8: main.sym_fnc("L8025DAA8", flag={"GLOBL","LOCAL"}),
	0x8025DABC: main.sym_fnc("L8025DABC", flag={"GLOBL","LOCAL"}),
	0x8025DAD0: main.sym_fnc("L8025DAD0", flag={"GLOBL","LOCAL"}),
	0x8025DAE4: main.sym_fnc("L8025DAE4", flag={"GLOBL","LOCAL"}),
	0x8025DAF8: main.sym_fnc("L8025DAF8", flag={"GLOBL","LOCAL"}),
	0x8025DB0C: main.sym_fnc("L8025DB0C", flag={"GLOBL","LOCAL"}),
	0x8025DB20: main.sym_fnc("L8025DB20", flag={"GLOBL","LOCAL"}),
	0x8025DB34: main.sym_fnc("L8025DB34", flag={"GLOBL","LOCAL"}),
	0x8025DB48: main.sym_fnc("L8025DB48", flag={"GLOBL","LOCAL"}),
	0x8025DB5C: main.sym_fnc("L8025DB5C", flag={"GLOBL","LOCAL"}),
	0x8025DB70: main.sym_fnc("L8025DB70", flag={"GLOBL","LOCAL"}),
	0x8025DB84: main.sym_fnc("L8025DB84", flag={"GLOBL","LOCAL"}),
	0x8025DB98: main.sym_fnc("L8025DB98", flag={"GLOBL","LOCAL"}),
	0x8025DBAC: main.sym_fnc("L8025DBAC", flag={"GLOBL","LOCAL"}),
	0x8025DBC0: main.sym_fnc("L8025DBC0", flag={"GLOBL","LOCAL"}),
	0x8025DBD4: main.sym_fnc("L8025DBD4", flag={"GLOBL","LOCAL"}),
	0x8025DBE8: main.sym_fnc("L8025DBE8", flag={"GLOBL","LOCAL"}),
	0x8025DBFC: main.sym_fnc("L8025DBFC", flag={"GLOBL","LOCAL"}),
	0x8025DC10: main.sym_fnc("L8025DC10", flag={"GLOBL","LOCAL"}),
	0x8025DC24: main.sym_fnc("L8025DC24", flag={"GLOBL","LOCAL"}),
	0x8025DC38: main.sym_fnc("L8025DC38", flag={"GLOBL","LOCAL"}),
	0x8025DC4C: main.sym_fnc("L8025DC4C", flag={"GLOBL","LOCAL"}),
	0x8025DC74: main.sym_fnc("L8025DC74", flag={"GLOBL","LOCAL"}),
	0x8025DC88: main.sym_fnc("L8025DC88", flag={"GLOBL","LOCAL"}),
	0x8025DC9C: main.sym_fnc("L8025DC9C", flag={"GLOBL","LOCAL"}),
	0x8025DCB0: main.sym_fnc("L8025DCB0", flag={"GLOBL","LOCAL"}),
	0x8025DCC4: main.sym_fnc("L8025DCC4", flag={"GLOBL","LOCAL"}),
	0x8025DCD8: main.sym_fnc("L8025DCD8", flag={"GLOBL","LOCAL"}),
	0x8025DCEC: main.sym_fnc("L8025DCEC", flag={"GLOBL","LOCAL"}),
	0x8025DD00: main.sym_fnc("L8025DD00", flag={"GLOBL","LOCAL"}),
	0x8025DD14: main.sym_fnc("L8025DD14", flag={"GLOBL","LOCAL"}),

	# src/plspec.c
	0x8025DD70: main.sym("plspec_8025DD70"),
	0x8025DE1C: main.sym("plspec_8025DE1C"),
	0x8025DF04: main.sym("plspec_8025DF04"),
	0x8025E21C: main.sym("plspec_8025E21C"),
	0x8025E5A8: main.sym("plspec_8025E5A8"),
	0x8025E7A4: main.sym("plspec_8025E7A4"),
	0x8025E830: main.sym("plspec_8025E830"),
	0x8025E930: main.sym("plspec_8025E930"),
	0x8025EA30: main.sym("plspec_8025EA30"),
	0x8025EB50: main.sym("plspec_8025EB50"),
	0x8025ECFC: main.sym("plspec_8025ECFC"),
	0x8025EED0: main.sym("plspec_8025EED0"),
	0x8025EF58: main.sym("plspec_8025EF58"),
	0x8025F0B4: main.sym("plspec_8025F0B4"),
	0x8025F1E4: main.sym("plspec_8025F1E4"),
	0x8025F384: main.sym("plspec_8025F384"),
	0x8025F4B4: main.sym("plspec_8025F4B4"),
	0x8025F560: main.sym("plspec_8025F560"),
	0x8025F644: main.sym("plspec_8025F644"),
	0x8025F6C0: main.sym("plspec_8025F6C0"),
	0x8025F970: main.sym("plspec_8025F970"),
	0x8025FA64: main.sym("plspec_8025FA64"),
	0x8025FAE8: main.sym("plspec_8025FAE8"),
	0x8025FB90: main.sym("plspec_8025FB90"),
	0x8025FC6C: main.sym("plspec_8025FC6C"),
	0x80260154: main.sym("plspec_80260154"),
	0x80260568: main.sym("plspec_80260568"),
	0x802605D0: main.sym_fnc("PL_ExecSpec", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80260748: main.sym_fnc("L80260748", flag={"GLOBL","LOCAL"}),
	0x8026075C: main.sym_fnc("L8026075C", flag={"GLOBL","LOCAL"}),
	0x80260770: main.sym_fnc("L80260770", flag={"GLOBL","LOCAL"}),
	0x80260784: main.sym_fnc("L80260784", flag={"GLOBL","LOCAL"}),
	0x80260798: main.sym_fnc("L80260798", flag={"GLOBL","LOCAL"}),

	# src/plwait.c
	0x802608B0: main.sym("plwait_802608B0"),
	0x80260AAC: main.sym("plwait_80260AAC"),
	0x80260CB4: main.sym("plwait_80260CB4"),
	0x80260F94: main.sym("plwait_80260F94"),
	0x80261000: main.sym("plwait_80261000"),
	0x80261268: main.sym("plwait_80261268"),
	0x802614FC: main.sym("plwait_802614FC"),
	0x8026168C: main.sym("plwait_8026168C"),
	0x802618D8: main.sym("plwait_802618D8"),
	0x802619D0: main.sym("plwait_802619D0"),
	0x80261AD0: main.sym("plwait_80261AD0"),
	0x80261BF8: main.sym("plwait_80261BF8"),
	0x80261CEC: main.sym("plwait_80261CEC"),
	0x80261DB4: main.sym("plwait_80261DB4"),
	0x80261F70: main.sym("plwait_80261F70"),
	0x80262080: main.sym("plwait_80262080"),
	0x8026217C: main.sym("plwait_8026217C"),
	0x802621DC: main.sym("plwait_802621DC"),
	0x802622DC: main.sym("plwait_802622DC"),
	0x80262398: main.sym("plwait_80262398"),
	0x80262490: main.sym("plwait_80262490"),
	0x80262530: main.sym("plwait_80262530"),
	0x80262650: main.sym("plwait_80262650"),
	0x80262770: main.sym("plwait_80262770"),
	0x80262890: main.sym("plwait_80262890"),
	0x80262980: main.sym("plwait_80262980"),
	0x80262BC4: main.sym("plwait_80262BC4"),
	0x80262C34: main.sym("plwait_80262C34"),
	0x80262D68: main.sym("plwait_80262D68"),
	0x80262DC4: main.sym("plwait_80262DC4"),
	0x80262E20: main.sym("plwait_80262E20"),
	0x80262E94: main.sym("plwait_80262E94"),
	0x80262EF0: main.sym("plwait_80262EF0"),
	0x80262F50: main.sym("plwait_80262F50"),
	0x80262FEC: main.sym("plwait_80262FEC"),
	0x8026305C: main.sym("plwait_8026305C"),
	0x802630F8: main.sym("plwait_802630F8"),
	0x802631F0: main.sym("plwait_802631F0"),
	0x802632E8: main.sym("plwait_802632E8"),
	0x802633B4: main.sym("plwait_802633B4"),
	0x8026350C: main.sym("plwait_8026350C"),
	0x802635E8: main.sym("plwait_802635E8"),
	0x80263784: main.sym("plwait_80263784"),
	0x80263898: main.sym_fnc("PL_ExecWait", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80263B38: main.sym_fnc("L80263B38", flag={"GLOBL","LOCAL"}),
	0x80263B4C: main.sym_fnc("L80263B4C", flag={"GLOBL","LOCAL"}),
	0x80263B88: main.sym_fnc("L80263B88", flag={"GLOBL","LOCAL"}),
	0x80263BEC: main.sym_fnc("L80263BEC", flag={"GLOBL","LOCAL"}),
	0x80263C00: main.sym_fnc("L80263C00", flag={"GLOBL","LOCAL"}),
	0x80263C14: main.sym_fnc("L80263C14", flag={"GLOBL","LOCAL"}),
	0x80263C28: main.sym_fnc("L80263C28", flag={"GLOBL","LOCAL"}),
	0x80263C3C: main.sym_fnc("L80263C3C", flag={"GLOBL","LOCAL"}),
	0x80263C50: main.sym_fnc("L80263C50", flag={"GLOBL","LOCAL"}),
	0x80263C64: main.sym_fnc("L80263C64", flag={"GLOBL","LOCAL"}),
	0x80263C78: main.sym_fnc("L80263C78", flag={"GLOBL","LOCAL"}),
	0x80263C8C: main.sym_fnc("L80263C8C", flag={"GLOBL","LOCAL"}),
	0x80263CB4: main.sym_fnc("L80263CB4", flag={"GLOBL","LOCAL"}),
	0x80263CC8: main.sym_fnc("L80263CC8", flag={"GLOBL","LOCAL"}),
	0x80263CDC: main.sym_fnc("L80263CDC", flag={"GLOBL","LOCAL"}),
	0x80263CF0: main.sym_fnc("L80263CF0", flag={"GLOBL","LOCAL"}),
	0x80263D04: main.sym_fnc("L80263D04", flag={"GLOBL","LOCAL"}),
	0x80263D18: main.sym_fnc("L80263D18", flag={"GLOBL","LOCAL"}),
	0x80263D2C: main.sym_fnc("L80263D2C", flag={"GLOBL","LOCAL"}),
	0x80263D54: main.sym_fnc("L80263D54", flag={"GLOBL","LOCAL"}),
	0x80263D7C: main.sym_fnc("L80263D7C", flag={"GLOBL","LOCAL"}),
	0x80263D90: main.sym_fnc("L80263D90", flag={"GLOBL","LOCAL"}),
	0x80263DA4: main.sym_fnc("L80263DA4", flag={"GLOBL","LOCAL"}),
	0x80263DCC: main.sym_fnc("L80263DCC", flag={"GLOBL","LOCAL"}),
	0x80263DE0: main.sym_fnc("L80263DE0", flag={"GLOBL","LOCAL"}),
	0x80263E08: main.sym_fnc("L80263E08", flag={"GLOBL","LOCAL"}),

	# src/plmove.c
	0x80263E60: main.sym("plmove_80263E60"),
	0x80263EE4: main.sym_fnc("plmove_80263EE4", arg=(
		"PLAYER *pl",
		"SHORT",
		"SHORT",
	), flag={"GLOBL"}),
	0x80264024: main.sym("plmove_80264024"),
	0x8026409C: main.sym("plmove_8026409C"),
	0x802640FC: main.sym("plmove_802640FC"),
	0x802642B4: main.sym("plmove_802642B4"),
	0x80264340: main.sym("plmove_80264340"),
	0x8026440C: main.sym("plmove_8026440C"),
	0x80264740: main.sym("plmove_80264740"),
	0x80264B54: main.sym("plmove_80264B54"),
	0x80264D80: main.sym("plmove_80264D80"),
	0x80264E18: main.sym("plmove_80264E18"),
	0x80265080: main.sym("plmove_80265080"),
	0x802651B0: main.sym("plmove_802651B0"),
	0x80265244: main.sym("plmove_80265244"),
	0x80265458: main.sym("plmove_80265458"),
	0x80265514: main.sym("plmove_80265514"),
	0x80265558: main.sym("plmove_80265558"),
	0x80265620: main.sym("plmove_80265620"),
	0x80265700: main.sym("plmove_80265700"),
	0x80265B1C: main.sym("plmove_80265B1C"),
	0x80265D90: main.sym("plmove_80265D90"),
	0x80265DF8: main.sym("plmove_80265DF8"),
	0x80266038: main.sym("plmove_80266038"),
	0x802661CC: main.sym("plmove_802661CC"),
	0x80266354: main.sym("plmove_80266354"),
	0x802665B4: main.sym("plmove_802665B4"),
	0x80266734: main.sym("plmove_80266734"),
	0x8026699C: main.sym("plmove_8026699C"),
	0x80266AF8: main.sym("plmove_80266AF8"),
	0x80266D4C: main.sym("plmove_80266D4C"),
	0x80266E48: main.sym("plmove_80266E48"),
	0x80266FC8: main.sym("plmove_80266FC8"),
	0x80267240: main.sym("plmove_80267240"),
	0x80267504: main.sym("plmove_80267504"),
	0x80267728: main.sym("plmove_80267728"),
	0x8026795C: main.sym("plmove_8026795C"),
	0x80267C24: main.sym("plmove_80267C24"),
	0x80267CE4: main.sym("plmove_80267CE4"),
	0x80267FA4: main.sym("plmove_80267FA4"),
	0x80268074: main.sym("plmove_80268074"),
	0x802680D4: main.sym("plmove_802680D4"),
	0x80268168: main.sym("plmove_80268168"),
	0x80268338: main.sym("plmove_80268338"),
	0x802684AC: main.sym("plmove_802684AC"),
	0x802685C0: main.sym("plmove_802685C0"),
	0x80268608: main.sym("plmove_80268608"),
	0x80268684: main.sym("plmove_80268684"),
	0x802687B8: main.sym("plmove_802687B8"),
	0x802689F8: main.sym("plmove_802689F8"),
	0x80268ADC: main.sym("plmove_80268ADC"),
	0x80268B64: main.sym("plmove_80268B64"),
	0x80268BB0: main.sym("plmove_80268BB0"),
	0x80268BFC: main.sym("plmove_80268BFC"),
	0x80268C48: main.sym("plmove_80268C48"),
	0x80268C94: main.sym("plmove_80268C94"),
	0x80268D04: main.sym("plmove_80268D04"),
	0x80268DCC: main.sym("plmove_80268DCC"),
	0x80268F78: main.sym("plmove_80268F78"),
	0x80269108: main.sym("plmove_80269108"),
	0x80269170: main.sym("plmove_80269170"),
	0x802691D8: main.sym("plmove_802691D8"),
	0x80269264: main.sym("plmove_80269264"),
	0x80269300: main.sym("plmove_80269300"),
	0x8026939C: main.sym("plmove_8026939C"),
	0x8026947C: main.sym("plmove_8026947C"),
	0x802694E4: main.sym("plmove_802694E4"),
	0x80269588: main.sym("plmove_80269588"),
	0x80269640: main.sym("plmove_80269640"),
	0x80269788: main.sym("plmove_80269788"),
	0x802697DC: main.sym("plmove_802697DC"),
	0x80269830: main.sym("plmove_80269830"),
	0x80269954: main.sym_fnc("PL_ExecMove", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80269BEC: main.sym_fnc("L80269BEC", flag={"GLOBL","LOCAL"}),
	0x80269C00: main.sym_fnc("L80269C00", flag={"GLOBL","LOCAL"}),
	0x80269C14: main.sym_fnc("L80269C14", flag={"GLOBL","LOCAL"}),
	0x80269C28: main.sym_fnc("L80269C28", flag={"GLOBL","LOCAL"}),
	0x80269C78: main.sym_fnc("L80269C78", flag={"GLOBL","LOCAL"}),
	0x80269CA0: main.sym_fnc("L80269CA0", flag={"GLOBL","LOCAL"}),
	0x80269D54: main.sym_fnc("L80269D54", flag={"GLOBL","LOCAL"}),
	0x80269D68: main.sym_fnc("L80269D68", flag={"GLOBL","LOCAL"}),
	0x80269D7C: main.sym_fnc("L80269D7C", flag={"GLOBL","LOCAL"}),
	0x80269D90: main.sym_fnc("L80269D90", flag={"GLOBL","LOCAL"}),
	0x80269DA4: main.sym_fnc("L80269DA4", flag={"GLOBL","LOCAL"}),
	0x80269DB8: main.sym_fnc("L80269DB8", flag={"GLOBL","LOCAL"}),
	0x80269DCC: main.sym_fnc("L80269DCC", flag={"GLOBL","LOCAL"}),
	0x80269DE0: main.sym_fnc("L80269DE0", flag={"GLOBL","LOCAL"}),
	0x80269DF4: main.sym_fnc("L80269DF4", flag={"GLOBL","LOCAL"}),
	0x80269E08: main.sym_fnc("L80269E08", flag={"GLOBL","LOCAL"}),
	0x80269E1C: main.sym_fnc("L80269E1C", flag={"GLOBL","LOCAL"}),
	0x80269E30: main.sym_fnc("L80269E30", flag={"GLOBL","LOCAL"}),
	0x80269E44: main.sym_fnc("L80269E44", flag={"GLOBL","LOCAL"}),
	0x80269E58: main.sym_fnc("L80269E58", flag={"GLOBL","LOCAL"}),
	0x80269E6C: main.sym_fnc("L80269E6C", flag={"GLOBL","LOCAL"}),
	0x80269E80: main.sym_fnc("L80269E80", flag={"GLOBL","LOCAL"}),
	0x80269E94: main.sym_fnc("L80269E94", flag={"GLOBL","LOCAL"}),
	0x80269EA8: main.sym_fnc("L80269EA8", flag={"GLOBL","LOCAL"}),
	0x80269EBC: main.sym_fnc("L80269EBC", flag={"GLOBL","LOCAL"}),
	0x80269ED0: main.sym_fnc("L80269ED0", flag={"GLOBL","LOCAL"}),

	# src/pljump.c
	0x80269F40: main.sym("pljump_80269F40"),
	0x80269FC0: main.sym("pljump_80269FC0"),
	0x8026A090: main.sym("pljump_8026A090"),
	0x8026A12C: main.sym("pljump_8026A12C"),
	0x8026A224: main.sym("pljump_8026A224"),
	0x8026A400: main.sym("pljump_8026A400"),
	0x8026A494: main.sym("pljump_8026A494"),
	0x8026A598: main.sym("pljump_8026A598"),
	0x8026A62C: main.sym("pljump_8026A62C"),
	0x8026A818: main.sym("pljump_8026A818"),
	0x8026AA48: main.sym("pljump_8026AA48"),
	0x8026ACD8: main.sym("pljump_8026ACD8"),
	0x8026AE5C: main.sym("pljump_8026AE5C"),
	0x8026B004: main.sym("pljump_8026B004"),
	0x8026B17C: main.sym("pljump_8026B17C"),
	0x8026B444: main.sym("pljump_8026B444"),
	0x8026B49C: main.sym_fnc("L8026B49C", flag={"GLOBL","LOCAL"}),
	0x8026B4B0: main.sym_fnc("L8026B4B0", flag={"GLOBL","LOCAL"}),
	0x8026B4E0: main.sym_fnc("L8026B4E0", flag={"GLOBL","LOCAL"}),
	0x8026B62C: main.sym_fnc("L8026B62C", flag={"GLOBL","LOCAL"}),
	0x8026B654: main.sym_fnc("L8026B654", flag={"GLOBL","LOCAL"}),
	0x8026B670: main.sym_fnc("L8026B670", flag={"GLOBL","LOCAL"}),
	0x8026B680: main.sym_fnc("L8026B680", flag={"GLOBL","LOCAL"}),
	0x8026B6A0: main.sym("pljump_8026B6A0"),
	0x8026B740: main.sym("pljump_8026B740"),
	0x8026B814: main.sym("pljump_8026B814"),
	0x8026B90C: main.sym("pljump_8026B90C"),
	0x8026B9AC: main.sym("pljump_8026B9AC"),
	0x8026BAB8: main.sym("pljump_8026BAB8"),
	0x8026BBB4: main.sym("pljump_8026BBB4"),
	0x8026BCC0: main.sym("pljump_8026BCC0"),
	0x8026BDCC: main.sym("pljump_8026BDCC"),
	0x8026BE78: main.sym("pljump_8026BE78"),
	0x8026BF40: main.sym("pljump_8026BF40"),
	0x8026C034: main.sym("pljump_8026C034"),
	0x8026C1E0: main.sym("pljump_8026C1E0"),
	0x8026C4B8: main.sym("pljump_8026C4B8"),
	0x8026C5D0: main.sym("pljump_8026C5D0"),
	0x8026C738: main.sym("pljump_8026C738"),
	0x8026C880: main.sym("pljump_8026C880"),
	0x8026C9FC: main.sym("pljump_8026C9FC"),
	0x8026CD0C: main.sym("pljump_8026CD0C"),
	0x8026CE50: main.sym("pljump_8026CE50"),
	0x8026CF28: main.sym("pljump_8026CF28"),
	0x8026D1B0: main.sym("pljump_8026D1B0"),
	0x8026D33C: main.sym("pljump_8026D33C"),
	0x8026D3C8: main.sym("pljump_8026D3C8"),
	0x8026D43C: main.sym("pljump_8026D43C"),
	0x8026D4B0: main.sym("pljump_8026D4B0"),
	0x8026D508: main.sym("pljump_8026D508"),
	0x8026D560: main.sym("pljump_8026D560"),
	0x8026D608: main.sym("pljump_8026D608"),
	0x8026D6FC: main.sym("pljump_8026D6FC"),
	0x8026D770: main.sym("pljump_8026D770"),
	0x8026D988: main.sym("pljump_8026D988"),
	0x8026DB54: main.sym("pljump_8026DB54"),
	0x8026DCF4: main.sym("pljump_8026DCF4"),
	0x8026DE98: main.sym("pljump_8026DE98"),
	0x8026E088: main.sym("pljump_8026E088"),
	0x8026E2B4: main.sym("pljump_8026E2B4"),
	0x8026E59C: main.sym("pljump_8026E59C"),
	0x8026E810: main.sym("pljump_8026E810"),
	0x8026E968: main.sym("pljump_8026E968"),
	0x8026EC00: main.sym("pljump_8026EC00"),
	0x8026F158: main.sym("pljump_8026F158"),
	0x8026F2EC: main.sym("pljump_8026F2EC"),
	0x8026F614: main.sym("pljump_8026F614"),
	0x8026F660: main.sym("pljump_8026F660"),
	0x8026F840: main.sym("pljump_8026F840"),
	0x8026FA18: main.sym("pljump_8026FA18"),
	0x8026FB04: main.sym_fnc("PL_ExecJump", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x8026FD70: main.sym_fnc("L8026FD70", flag={"GLOBL","LOCAL"}),
	0x8026FD84: main.sym_fnc("L8026FD84", flag={"GLOBL","LOCAL"}),
	0x8026FD98: main.sym_fnc("L8026FD98", flag={"GLOBL","LOCAL"}),
	0x8026FDAC: main.sym_fnc("L8026FDAC", flag={"GLOBL","LOCAL"}),
	0x8026FDC0: main.sym_fnc("L8026FDC0", flag={"GLOBL","LOCAL"}),
	0x8026FDD4: main.sym_fnc("L8026FDD4", flag={"GLOBL","LOCAL"}),
	0x8026FDE8: main.sym_fnc("L8026FDE8", flag={"GLOBL","LOCAL"}),
	0x8026FE10: main.sym_fnc("L8026FE10", flag={"GLOBL","LOCAL"}),
	0x8026FE24: main.sym_fnc("L8026FE24", flag={"GLOBL","LOCAL"}),
	0x8026FE38: main.sym_fnc("L8026FE38", flag={"GLOBL","LOCAL"}),
	0x8026FE4C: main.sym_fnc("L8026FE4C", flag={"GLOBL","LOCAL"}),
	0x8026FE60: main.sym_fnc("L8026FE60", flag={"GLOBL","LOCAL"}),
	0x8026FE74: main.sym_fnc("L8026FE74", flag={"GLOBL","LOCAL"}),
	0x8026FE88: main.sym_fnc("L8026FE88", flag={"GLOBL","LOCAL"}),
	0x8026FE9C: main.sym_fnc("L8026FE9C", flag={"GLOBL","LOCAL"}),
	0x8026FEEC: main.sym_fnc("L8026FEEC", flag={"GLOBL","LOCAL"}),
	0x8026FF00: main.sym_fnc("L8026FF00", flag={"GLOBL","LOCAL"}),
	0x8026FF14: main.sym_fnc("L8026FF14", flag={"GLOBL","LOCAL"}),
	0x8026FF28: main.sym_fnc("L8026FF28", flag={"GLOBL","LOCAL"}),
	0x8026FF3C: main.sym_fnc("L8026FF3C", flag={"GLOBL","LOCAL"}),
	0x8026FF64: main.sym_fnc("L8026FF64", flag={"GLOBL","LOCAL"}),
	0x8026FF8C: main.sym_fnc("L8026FF8C", flag={"GLOBL","LOCAL"}),
	0x8026FFA0: main.sym_fnc("L8026FFA0", flag={"GLOBL","LOCAL"}),
	0x8026FFB4: main.sym_fnc("L8026FFB4", flag={"GLOBL","LOCAL"}),
	0x8026FFC8: main.sym_fnc("L8026FFC8", flag={"GLOBL","LOCAL"}),
	0x8026FFDC: main.sym_fnc("L8026FFDC", flag={"GLOBL","LOCAL"}),
	0x80270004: main.sym_fnc("L80270004", flag={"GLOBL","LOCAL"}),
	0x8027002C: main.sym_fnc("L8027002C", flag={"GLOBL","LOCAL"}),
	0x80270040: main.sym_fnc("L80270040", flag={"GLOBL","LOCAL"}),
	0x80270054: main.sym_fnc("L80270054", flag={"GLOBL","LOCAL"}),
	0x802700B8: main.sym_fnc("L802700B8", flag={"GLOBL","LOCAL"}),
	0x802700E0: main.sym_fnc("L802700E0", flag={"GLOBL","LOCAL"}),

	# src/plswim.c
	0x80270110: main.sym("plswim_80270110"),
	0x802701CC: main.sym("plswim_802701CC"),
	0x80270234: main.sym("plswim_80270234"),
	0x80270304: main.sym("plswim_80270304"),
	0x80270500: main.sym("plswim_80270500"),
	0x80270918: main.sym("plswim_80270918"),
	0x80270A74: main.sym("plswim_80270A74"),
	0x80270B4C: main.sym("plswim_80270B4C"),
	0x80270C94: main.sym("plswim_80270C94"),
	0x80270E40: main.sym("plswim_80270E40"),
	0x80270FD8: main.sym("plswim_80270FD8"),
	0x802710C4: main.sym("plswim_802710C4"),
	0x802711D4: main.sym("plswim_802711D4"),
	0x802712C0: main.sym("plswim_802712C0"),
	0x802713BC: main.sym("plswim_802713BC"),
	0x802714A8: main.sym("plswim_802714A8"),
	0x802715EC: main.sym("plswim_802715EC"),
	0x8027163C: main.sym("plswim_8027163C"),
	0x80271704: main.sym("plswim_80271704"),
	0x80271918: main.sym("plswim_80271918"),
	0x8027197C: main.sym("plswim_8027197C"),
	0x80271AA0: main.sym("plswim_80271AA0"),
	0x80271D04: main.sym("plswim_80271D04"),
	0x80271EB4: main.sym("plswim_80271EB4"),
	0x8027202C: main.sym("plswim_8027202C"),
	0x8027226C: main.sym("plswim_8027226C"),
	0x802723F0: main.sym("plswim_802723F0"),
	0x80272548: main.sym("plswim_80272548"),
	0x8027267C: main.sym("plswim_8027267C"),
	0x80272778: main.sym("plswim_80272778"),
	0x80272870: main.sym("plswim_80272870"),
	0x80272A60: main.sym("plswim_80272A60"),
	0x80272B1C: main.sym("plswim_80272B1C"),
	0x80272B64: main.sym("plswim_80272B64"),
	0x80272BAC: main.sym("plswim_80272BAC"),
	0x80272CBC: main.sym("plswim_80272CBC"),
	0x80272DC0: main.sym("plswim_80272DC0"),
	0x80272E3C: main.sym("plswim_80272E3C"),
	0x80272FE8: main.sym_fnc("L80272FE8", flag={"GLOBL","LOCAL"}),
	0x80273004: main.sym_fnc("L80273004", flag={"GLOBL","LOCAL"}),
	0x80273020: main.sym_fnc("L80273020", flag={"GLOBL","LOCAL"}),
	0x8027303C: main.sym_fnc("L8027303C", flag={"GLOBL","LOCAL"}),
	0x80273058: main.sym_fnc("L80273058", flag={"GLOBL","LOCAL"}),
	0x80273070: main.sym_fnc("L80273070", flag={"GLOBL","LOCAL"}),
	0x802730B8: main.sym_fnc("L802730B8", flag={"GLOBL","LOCAL"}),
	0x802730CC: main.sym_fnc("L802730CC", flag={"GLOBL","LOCAL"}),
	0x802730E0: main.sym_fnc("L802730E0", flag={"GLOBL","LOCAL"}),
	0x802730F4: main.sym_fnc("L802730F4", flag={"GLOBL","LOCAL"}),
	0x80273108: main.sym_fnc("L80273108", flag={"GLOBL","LOCAL"}),
	0x8027311C: main.sym_fnc("L8027311C", flag={"GLOBL","LOCAL"}),
	0x80273160: main.sym("plswim_80273160"),
	0x80273518: main.sym("plswim_80273518"),
	0x802735A4: main.sym("plswim_802735A4"),
	0x80273618: main.sym("plswim_80273618"),
	0x802737F4: main.sym("plswim_802737F4"),
	0x80273A2C: main.sym("plswim_80273A2C"),
	0x80273BD4: main.sym("plswim_80273BD4"),
	0x80273CD0: main.sym("plswim_80273CD0"),
	0x80273E74: main.sym("plswim_80273E74"),
	0x80274030: main.sym("plswim_80274030"),
	0x80274134: main.sym("plswim_80274134"),
	0x80274268: main.sym("plswim_80274268"),
	0x80274384: main.sym("plswim_80274384"),
	0x802744AC: main.sym("plswim_802744AC"),
	0x80274580: main.sym("plswim_80274580"),
	0x80274688: main.sym("plswim_80274688"),
	0x8027475C: main.sym("plswim_8027475C"),
	0x80274864: main.sym("plswim_80274864"),
	0x8027499C: main.sym_fnc("PL_ExecSwim", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80274CBC: main.sym_fnc("L80274CBC", flag={"GLOBL","LOCAL"}),
	0x80274CD0: main.sym_fnc("L80274CD0", flag={"GLOBL","LOCAL"}),
	0x80274CE4: main.sym_fnc("L80274CE4", flag={"GLOBL","LOCAL"}),
	0x80274CF8: main.sym_fnc("L80274CF8", flag={"GLOBL","LOCAL"}),
	0x80274D0C: main.sym_fnc("L80274D0C", flag={"GLOBL","LOCAL"}),
	0x80274D20: main.sym_fnc("L80274D20", flag={"GLOBL","LOCAL"}),
	0x80274D34: main.sym_fnc("L80274D34", flag={"GLOBL","LOCAL"}),
	0x80274D48: main.sym_fnc("L80274D48", flag={"GLOBL","LOCAL"}),
	0x80274D5C: main.sym_fnc("L80274D5C", flag={"GLOBL","LOCAL"}),
	0x80274DAC: main.sym_fnc("L80274DAC", flag={"GLOBL","LOCAL"}),
	0x80274DE8: main.sym_fnc("L80274DE8", flag={"GLOBL","LOCAL"}),
	0x80274DFC: main.sym_fnc("L80274DFC", flag={"GLOBL","LOCAL"}),
	0x80274E24: main.sym_fnc("L80274E24", flag={"GLOBL","LOCAL"}),
	0x80274E60: main.sym_fnc("L80274E60", flag={"GLOBL","LOCAL"}),
	0x80274E74: main.sym_fnc("L80274E74", flag={"GLOBL","LOCAL"}),
	0x80274E88: main.sym_fnc("L80274E88", flag={"GLOBL","LOCAL"}),

	# src/pltake.c
	0x80274EB0: main.sym("pltake_80274EB0"),
	0x80274F10: main.sym_fnc("pltake_80274F10", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x80274F90: main.sym_fnc("L80274F90", flag={"GLOBL","LOCAL"}),
	0x80274FA8: main.sym_fnc("L80274FA8", flag={"GLOBL","LOCAL"}),
	0x80275050: main.sym_fnc("L80275050", flag={"GLOBL","LOCAL"}),
	0x802750CC: main.sym_fnc("L802750CC", flag={"GLOBL","LOCAL"}),
	0x802750E4: main.sym_fnc("L802750E4", flag={"GLOBL","LOCAL"}),
	0x80275170: main.sym_fnc("L80275170", flag={"GLOBL","LOCAL"}),
	0x802751EC: main.sym_fnc("L802751EC", flag={"GLOBL","LOCAL"}),
	0x80275280: main.sym_fnc("L80275280", flag={"GLOBL","LOCAL"}),
	0x80275308: main.sym_fnc("L80275308", flag={"GLOBL","LOCAL"}),
	0x80275328: main.sym("pltake_80275328"),
	0x8027546C: main.sym("pltake_8027546C"),
	0x802755FC: main.sym("pltake_802755FC"),
	0x802756C8: main.sym("pltake_802756C8"),
	0x80275794: main.sym("pltake_80275794"),
	0x802758C0: main.sym("pltake_802758C0"),
	0x802759B4: main.sym("pltake_802759B4"),
	0x80275A80: main.sym("pltake_80275A80"),
	0x80275B34: main.sym("pltake_80275B34"),
	0x80275E78: main.sym("pltake_80275E78"),
	0x80275F0C: main.sym("pltake_80275F0C"),
	0x80275FE0: main.sym_fnc("PL_ExecTake", "int", (
		"PLAYER *pl",
	), flag={"GLOBL"}),
	0x802760C8: main.sym_fnc("L802760C8", flag={"GLOBL","LOCAL"}),
	0x802760DC: main.sym_fnc("L802760DC", flag={"GLOBL","LOCAL"}),
	0x802760F0: main.sym_fnc("L802760F0", flag={"GLOBL","LOCAL"}),
	0x80276104: main.sym_fnc("L80276104", flag={"GLOBL","LOCAL"}),
	0x80276140: main.sym_fnc("L80276140", flag={"GLOBL","LOCAL"}),
	0x80276154: main.sym_fnc("L80276154", flag={"GLOBL","LOCAL"}),
	0x80276168: main.sym_fnc("L80276168", flag={"GLOBL","LOCAL"}),
	0x8027617C: main.sym_fnc("L8027617C", flag={"GLOBL","LOCAL"}),

	# src/callback.c
	0x802761D0: main.sym_fnc("CtrlWeather", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802763D4: main.sym_fnc("CtrlBackground", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802764B0: main.sym_fnc("CtrlFace", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x8027657C: main.sym_fnc("callback_8027657C"),
	0x802765FC: main.sym_fnc("callback_802765FC"),
	0x802766B4: main.sym_fnc("callback_802766B4"),
	0x802767B8: main.sym_fnc("callback_802767B8"),
	0x80276804: main.sym_fnc("callback_80276804"),
	0x8027684C: main.sym_fnc("callback_8027684C", flag={"GLOBL"}), # objcall
	0x802768A8: main.sym_fnc("L802768A8", flag={"GLOBL","LOCAL"}),
	0x802768B8: main.sym_fnc("L802768B8", flag={"GLOBL","LOCAL"}),
	0x802768C8: main.sym_fnc("L802768C8", flag={"GLOBL","LOCAL"}),
	0x802768D8: main.sym_fnc("L802768D8", flag={"GLOBL","LOCAL"}),
	0x802768E8: main.sym_fnc("L802768E8", flag={"GLOBL","LOCAL"}),
	0x80276910: main.sym_fnc("callback_80276910", flag={"GLOBL"}), # objcall
	0x80276AA0: main.sym_fnc("callback_80276AA0", arg=(
		"SHORT angy",
	)),
	0x80276BB8: main.sym_fnc("callback_80276BB8", flag={"GLOBL"}), # objcall
	0x80276CCC: main.sym_fnc("callback_80276CCC", flag={"GLOBL"}), # objcall
	0x80276F90: main.sym_fnc("callback_80276F90", "Gfx *", (
		"SCALLBACK *shp",
		"SHORT alpha",
	)),
	0x802770A4: main.sym_fnc("CtrlPlayerAlpha", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x80277150: main.sym_fnc("CtrlPlayerLOD", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802771BC: main.sym_fnc("CtrlPlayerEyes", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x80277294: main.sym_fnc("CtrlPlayerTorso", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802773A4: main.sym_fnc("CtrlPlayerNeck", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802774F4: main.sym_fnc("CtrlMarioHand", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802775CC: main.sym_fnc("CtrlMarioPunch", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802776D8: main.sym_fnc("CtrlPlayerCap", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x80277740: main.sym_fnc("CtrlPlayerHead", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x80277824: main.sym_fnc("CtrlPlayerWing", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x8027795C: main.sym_fnc("CtrlPlayerHand", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x80277B14: main.sym_fnc("CtrlInsideMirror", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x80277D6C: main.sym_fnc("CtrlMarioMirror", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall

	# src/memory.c
	0x80277EE0: main.sym_fnc("SegmentSet", "unsigned long", (
		"int number",
		"void *addr",
	), flag={"GLOBL"}),
	0x80277F20: main.sym_fnc("SegmentGet", "void *", (
		"int number",
	), flag={"GLOBL"}), # unused
	0x80277F50: main.sym_fnc("SegmentToVirtual", "void *", (
		"const void *addr",
	), flag={"GLOBL"}),
	0x80277FA8: main.sym_fnc("VirtualToSegment", "void *", (
		"int number",
		"const void *addr",
	), flag={"GLOBL"}),
	0x80277FF0: main.sym_fnc("SegmentWrite", flag={"GLOBL"}),
	0x80278074: main.sym_fnc("MemInit", arg=(
		"void *start",
		"void *end",
	), flag={"GLOBL"}),
	0x80278120: main.sym_fnc("MemAlloc", "void *", (
		"size_t size",
		"int mode",
	), flag={"GLOBL"}),
	0x80278238: main.sym_fnc("MemFree", "size_t", (
		"void *ptr",
	), flag={"GLOBL"}),
	0x80278358: main.sym_fnc("MemRealloc", "void *", (
		"void *ptr",
		"size_t size",
	), flag={"GLOBL"}), # static
	0x802783C8: main.sym_fnc("MemAvailable", "size_t", flag={"GLOBL"}),
	0x802783E8: main.sym_fnc("MemPush", "size_t", flag={"GLOBL"}),
	0x80278498: main.sym_fnc("MemPull", "size_t", flag={"GLOBL"}),
	0x80278504: main.sym_fnc("MemRead", arg=(
		"char *dst",
		"const char *start",
		"const char *end",
	), flag={"GLOBL"}), # static
	0x80278610: main.sym_fnc("MemLoad", "void *", (
		"const char *start",
		"const char *end",
		"int mode",
	), flag={"GLOBL"}), # static
	0x8027868C: main.sym_fnc("MemLoadData", "void *", (
		"int seg",
		"const char *start",
		"const char *end",
		"int mode",
	), flag={"GLOBL"}),
	0x802786F0: main.sym_fnc("MemLoadCode", "void *", (
		"char *addr",
		"const char *start",
		"const char *end",
	), flag={"GLOBL"}),
	0x802787D8: main.sym_fnc("MemLoadPres", "void *", (
		"int seg",
		"const char *start",
		"const char *end",
	), flag={"GLOBL"}),
	0x802788B4: main.sym_fnc("MemLoadText", "void *", (
		"int seg",
		"const char *start",
		"const char *end",
	), flag={"GLOBL"}),
	0x80278974: main.sym_fnc("MemLoadULib", flag={"GLOBL"}),
	0x80278A14: main.sym_fnc("ArenaCreate", "ARENA *", (
		"size_t size",
		"int mode",
	), flag={"GLOBL"}),
	0x80278AB8: main.sym_fnc("ArenaAlloc", "void *", (
		"ARENA *arena",
		"long size",
	), flag={"GLOBL"}),
	0x80278B28: main.sym_fnc("ArenaResize", "void *", (
		"ARENA *arena",
		"size_t size",
	), flag={"GLOBL"}),
	0x80278B98: main.sym_fnc("HeapCreate", "HEAP *", (
		"size_t size",
		"int mode",
	), flag={"GLOBL"}),
	0x80278C58: main.sym_fnc("HeapAlloc", "void *", (
		"HEAP *heap",
		"size_t size",
	), flag={"GLOBL"}),
	0x80278D74: main.sym_fnc("HeapFree", arg=(
		"HEAP *heap",
		"void *ptr",
	), flag={"GLOBL"}),
	0x80278F2C: main.sym_fnc("GfxAlloc", "void *", (
		"size_t size",
	), flag={"GLOBL"}),
	0x80278FA0: main.sym_fnc("BankLoadInfo", "BANKINFO *", (
		"const char *src",
	)),
	0x80279028: main.sym_fnc("BankInit", arg=(
		"BANK *bank",
		"const char *src",
		"void *buf",
	), flag={"GLOBL"}),
	0x80279084: main.sym_fnc("BankLoad", "int", (
		"BANK *bank",
		"unsigned int index",
	), flag={"GLOBL"}),

	# src/backup.c
	0x80279160: main.sym_fnc("BuInitDebug"),
	0x80279174: main.sym_fnc("BackupRead", "int", (
		"void *data",
		"int size",
	)),
	0x80279218: main.sym_fnc("BackupWrite", "int", (
		"const void *data",
		"int size",
	)),
	0x802792C0: main.sym_fnc("BuCheckSum", "USHORT", (
		"u8 *data",
		"int size",
	)),
	0x80279314: main.sym_fnc("BuCheck", "int", (
		"void *data",
		"int size",
		"USHORT key",
	)),
	0x8027939C: main.sym_fnc("BuCheckSet", arg=(
		"void *data",
		"int size",
		"USHORT key",
	)),
	0x802793FC: main.sym_fnc("BuInfoRecover", arg=(
		"int src",
	)),
	0x802794A0: main.sym_fnc("BuInfoWrite"),
	0x8027951C: main.sym_fnc("BuInfoErase"),
	0x802795A0: main.sym_fnc("BuGetTime", "int", (
		"int file",
		"int course",
	)),
	0x802795D4: main.sym_fnc("BuSetTime", arg=(
		"int file",
		"int course",
		"int time",
	)),
	0x80279650: main.sym_fnc("BuUpdateTime", arg=(
		"int file",
		"int course",
	)),
	0x80279700: main.sym_fnc("BuUpdateTimeAll", arg=(
		"int file",
	)),
	0x80279748: main.sym_fnc("BuFileRecover", arg=(
		"int file",
		"int src",
	)),
	0x80279840: main.sym_fnc("BuFileWrite", arg=(
		"int file",
	), flag={"GLOBL"}),
	0x802798FC: main.sym_fnc("BuFileErase", arg=(
		"int file",
	), flag={"GLOBL"}),
	0x80279960: main.sym_fnc("BuFileCopy", arg=(
		"int src",
		"int dst",
	), flag={"GLOBL"}),
	0x802799DC: main.sym_fnc("BackupInit", flag={"GLOBL"}),
	0x80279BC8: main.sym_fnc("BuReset", flag={"GLOBL"}),
	0x80279C44: main.sym_fnc("BuSet", arg=(
		"SHORT coin",
		"SHORT level",
	), flag={"GLOBL"}),
	0x80279E44: main.sym_fnc("BuFileIsActive", "int", (
		"int file",
	), flag={"GLOBL"}),
	0x80279E80: main.sym_fnc("BuGetHiScore", "u32", (
		"int course",
	), flag={"GLOBL"}),
	0x80279F80: main.sym_fnc("BuFileStarCount", "int", (
		"int file",
		"int course",
	), flag={"GLOBL"}),
	0x8027A010: main.sym_fnc("BuFileStarRange", "int", (
		"int file",
		"int min",
		"int max",
	), flag={"GLOBL"}),
	0x8027A0A8: main.sym_fnc("BuSetFlag", arg=(
		"unsigned int flag",
	), flag={"GLOBL"}),
	0x8027A0F4: main.sym_fnc("BuClrFlag", arg=(
		"unsigned int flag",
	), flag={"GLOBL"}),
	0x8027A16C: main.sym_fnc("BuGetFlag", "unsigned int", flag={"GLOBL"}),
	0x8027A1C8: main.sym_fnc("BuFileGetStar", "int", (
		"int file",
		"int course",
	), flag={"GLOBL"}),
	0x8027A23C: main.sym_fnc("BuFileSetStar", arg=(
		"int file",
		"int course",
		"int flag",
	), flag={"GLOBL"}), # static
	0x8027A310: main.sym_fnc("BuFileGetCoin", "int", (
		"int file",
		"int course",
	), flag={"GLOBL"}),
	0x8027A340: main.sym_fnc("BuGetCannon", "int", flag={"GLOBL"}),
	0x8027A390: main.sym_fnc("BuSetCannon", flag={"GLOBL"}),
	0x8027A418: main.sym_fnc("BuSetCap", arg=(
		"SHORT x",
		"SHORT y",
		"SHORT z",
	), flag={"GLOBL"}),
	0x8027A4AC: main.sym_fnc("BuGetCap", "int", (
		"SVEC pos",
	), flag={"GLOBL"}),
	0x8027A564: main.sym_fnc("BuSetSound", arg=(
		"USHORT sound",
	), flag={"GLOBL"}),
	0x8027A5B4: main.sym_fnc("BuGetSound", "USHORT", flag={"GLOBL"}),
	0x8027A5D4: main.sym_fnc("BuInitCap", flag={"GLOBL"}),
	0x8027A698: main.sym_fnc("BuClrMid", flag={"GLOBL"}),
	0x8027A6B0: main.sym_fnc("BuSetMid", arg=(
		"PORTINFO *p",
	), flag={"GLOBL"}),
	0x8027A718: main.sym_fnc("BuGetMid", "int", (
		"PORTINFO *p",
	), flag={"GLOBL"}),

	# src/scene.c
	0x8027A7D0: main.sym_fnc("SnSetVp", arg=(
		"Vp *viewport",
		"Vp *scissor",
		"UCHAR r",
		"UCHAR g",
		"UCHAR b",
	), flag={"GLOBL"}),
	0x8027A83C: main.sym_fnc("SnSetBlank", arg=(
		"UCHAR r",
		"UCHAR g",
		"UCHAR b",
	)),
	0x8027A8B0: main.sym_fnc("SceneDemo", flag={"GLOBL"}),
	0x8027A93C: main.sym_fnc("SnGetPortType", "int", (
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x8027A9C8: main.sym_fnc("SnGetPort", "PORT *", (
		"UCHAR index",
	), flag={"GLOBL"}),
	0x8027AA28: main.sym_fnc("ObjGetPort", "PORT *", (
		"OBJECT *obj",
	)),
	0x8027AA74: main.sym_fnc("SnInitPort"),
	0x8027AB04: main.sym_fnc("SceneInit", flag={"GLOBL"}),
	0x8027AD74: main.sym_fnc("SceneExit", flag={"GLOBL"}),
	0x8027AE44: main.sym_fnc("SceneOpen", arg=(
		"int index",
	), flag={"GLOBL"}),
	0x8027AF48: main.sym_fnc("SceneClose", flag={"GLOBL"}),
	0x8027AFBC: main.sym_fnc("SnOpenPlayer", flag={"GLOBL"}),
	0x8027B038: main.sym_fnc("SnClosePlayer", flag={"GLOBL"}),
	0x8027B0C0: main.sym_fnc("SceneSet", arg=(
		"int index",
	), flag={"GLOBL"}),
	0x8027B164: main.sym_fnc("SceneProc", flag={"GLOBL"}),
	0x8027B1A0: main.sym_fnc("SnWipe", arg=(
		"SHORT type",
		"SHORT frame",
		"UCHAR r",
		"UCHAR g",
		"UCHAR b",
	), flag={"GLOBL"}),
	0x8027B35C: main.sym_fnc("SnWipeDelay", arg=(
		"SHORT type",
		"SHORT frame",
		"UCHAR r",
		"UCHAR g",
		"UCHAR b",
		"SHORT delay",
	), flag={"GLOBL"}),
	0x8027B3B4: main.sym_fnc("SceneDraw", flag={"GLOBL"}),

	# src/draw.c
	0x8027B6C0: main.sym_fnc("DrawLayerList", arg=(
		"SLAYER *shp",
	)),
	0x8027B904: main.sym_fnc("DrawLayerGfx", arg=(
		"Gfx *gfx",
		"SHORT layer",
	)),
	0x8027BA00: main.sym_fnc("DrawLayer", arg=(
		"SLAYER *shp",
	)),
	0x8027BA98: main.sym_fnc("DrawOrtho", arg=(
		"SORTHO *shp",
	)),
	0x8027BC74: main.sym_fnc("DrawPersp", arg=(
		"SPERSP *shp",
	)),
	0x8027BDF0: main.sym_fnc("DrawLOD", arg=(
		"SLOD *shp",
	)),
	0x8027BE84: main.sym_fnc("DrawSelect", arg=(
		"SSELECT *shp",
	)),
	0x8027BF58: main.sym_fnc("DrawCamera", arg=(
		"SCAMERA *shp",
	)),
	0x8027C114: main.sym_fnc("DrawCoord", arg=(
		"SCOORD *shp",
	)),
	0x8027C238: main.sym_fnc("DrawPos", arg=(
		"SPOS *shp",
	)),
	0x8027C35C: main.sym_fnc("DrawAng", arg=(
		"SANG *shp",
	)),
	0x8027C474: main.sym_fnc("DrawScale", arg=(
		"SSCALE *shp",
	)),
	0x8027C594: main.sym_fnc("DrawBillboard", arg=(
		"SBILLBOARD *shp",
	)),
	0x8027C73C: main.sym_fnc("DrawGfx", arg=(
		"SGFX *shp",
	)),
	0x8027C7A4: main.sym_fnc("DrawCallback", arg=(
		"SCALLBACK *shp",
	)),
	0x8027C858: main.sym_fnc("DrawBack", arg=(
		"SBACK *shp",
	)),
	0x8027CA70: main.sym_fnc("DrawJoint", arg=(
		"SJOINT *shp",
	)),
	0x8027CF38: main.sym_fnc("DrawSkeleton", arg=(
		"SKELETON *skel",
		"int flag",
	)),
	0x8027D0B8: main.sym_fnc("DrawShadow", arg=(
		"SSHADOW *shp",
	)),
	0x8027D518: main.sym_fnc("SObjIsVisible", "int", (
		"SOBJECT *shp",
		"FMTX *m",
	)),
	0x8027D6FC: main.sym_fnc("DrawObject", arg=(
		"SOBJECT *shp",
	)),
	0x8027DA10: main.sym_fnc("DrawBranch", arg=(
		"SBRANCH *shp",
	)),
	0x8027DA84: main.sym_fnc("DrawHand", arg=(
		"SHAND *shp",
	)),
	0x8027DE68: main.sym_fnc("DrawChild", arg=(
		"SHAPE *shape",
	)),
	0x8027DEA8: main.sym_fnc("DrawShape", arg=(
		"SHAPE *shape",
	)),
	0x8027DF90: main.sym_fnc("L8027DF90", flag={"GLOBL","LOCAL"}),
	0x8027DFA0: main.sym_fnc("L8027DFA0", flag={"GLOBL","LOCAL"}),
	0x8027DFB0: main.sym_fnc("L8027DFB0", flag={"GLOBL","LOCAL"}),
	0x8027DFC0: main.sym_fnc("L8027DFC0", flag={"GLOBL","LOCAL"}),
	0x8027DFD0: main.sym_fnc("L8027DFD0", flag={"GLOBL","LOCAL"}),
	0x8027DFE0: main.sym_fnc("L8027DFE0", flag={"GLOBL","LOCAL"}),
	0x8027DFF0: main.sym_fnc("L8027DFF0", flag={"GLOBL","LOCAL"}),
	0x8027E000: main.sym_fnc("L8027E000", flag={"GLOBL","LOCAL"}),
	0x8027E010: main.sym_fnc("L8027E010", flag={"GLOBL","LOCAL"}),
	0x8027E020: main.sym_fnc("L8027E020", flag={"GLOBL","LOCAL"}),
	0x8027E030: main.sym_fnc("L8027E030", flag={"GLOBL","LOCAL"}),
	0x8027E040: main.sym_fnc("L8027E040", flag={"GLOBL","LOCAL"}),
	0x8027E050: main.sym_fnc("L8027E050", flag={"GLOBL","LOCAL"}),
	0x8027E060: main.sym_fnc("L8027E060", flag={"GLOBL","LOCAL"}),
	0x8027E070: main.sym_fnc("L8027E070", flag={"GLOBL","LOCAL"}),
	0x8027E080: main.sym_fnc("L8027E080", flag={"GLOBL","LOCAL"}),
	0x8027E090: main.sym_fnc("L8027E090", flag={"GLOBL","LOCAL"}),
	0x8027E0A0: main.sym_fnc("L8027E0A0", flag={"GLOBL","LOCAL"}),
	0x8027E0B0: main.sym_fnc("L8027E0B0", flag={"GLOBL","LOCAL"}),
	0x8027E0C0: main.sym_fnc("L8027E0C0", flag={"GLOBL","LOCAL"}),
	0x8027E130: main.sym_fnc("DrawScene", arg=(
		"SSCENE *shp",
		"Vp *viewport",
		"Vp *scissor",
		"u32 fill",
	), flag={"GLOBL"}),

	# src/time.c
	0x8027E3E0: main.sym_fnc("TimeGfxCPU", arg=(
		"int",
	), flag={"GLOBL"}),
	0x8027E490: main.sym_fnc("TimeAudCPU", flag={"GLOBL"}),
	0x8027E520: main.sym_fnc("TimeGfxRCP", arg=(
		"int",
	), flag={"GLOBL"}),
	0x8027E5CC: main.sym_fnc("TimeAudRCP", flag={"GLOBL"}),
	0x8027E65C: main.sym("TimeDrawD"),
	0x8027E958: main.sym("TimeDrawScale"),
	0x8027EBCC: main.sym("TimeDrawAbs"),
	0x8027EEAC: main.sym("TimeDrawRel"),
	0x8027F460: main.sym_fnc("TimeDraw", flag={"GLOBL"}),

	# src/slidec.s
	0x8027F4E0: main.sym_fnc("slidec", arg=(
		"const char *src",
		"char *dst",
	), flag={"GLOBL"}),

	# src/camera.c
	0x8027F590: main.sym_fnc("camera_8027F590", arg=(
		"SHORT",
	), flag={"GLOBL"}),
	0x8027F5CC: main.sym_fnc("L8027F5CC", flag={"GLOBL","LOCAL"}),
	0x8027F5EC: main.sym_fnc("L8027F5EC", flag={"GLOBL","LOCAL"}),
	0x8027F614: main.sym_fnc("L8027F614", flag={"GLOBL","LOCAL"}),
	0x8027F62C: main.sym_fnc("L8027F62C", flag={"GLOBL","LOCAL"}),
	0x8027F6CC: main.sym_fnc("L8027F6CC", flag={"GLOBL","LOCAL"}),
	0x8027F76C: main.sym_fnc("L8027F76C", flag={"GLOBL","LOCAL"}),
	0x8027F80C: main.sym_fnc("L8027F80C", flag={"GLOBL","LOCAL"}),
	0x8027F834: main.sym_fnc("L8027F834", flag={"GLOBL","LOCAL"}),
	0x8027F89C: main.sym_fnc("L8027F89C", flag={"GLOBL","LOCAL"}),
	0x8027F8B8: main.sym("camera_8027F8B8", flag={"GLOBL"}),
	0x8027F8F0: main.sym_fnc("L8027F8F0", flag={"GLOBL","LOCAL"}),
	0x8027F908: main.sym_fnc("L8027F908", flag={"GLOBL","LOCAL"}),
	0x8027F920: main.sym_fnc("L8027F920", flag={"GLOBL","LOCAL"}),
	0x8027F938: main.sym_fnc("L8027F938", flag={"GLOBL","LOCAL"}),
	0x8027F950: main.sym_fnc("L8027F950", flag={"GLOBL","LOCAL"}),
	0x8027F968: main.sym_fnc("L8027F968", flag={"GLOBL","LOCAL"}),
	0x8027F980: main.sym_fnc("L8027F980", flag={"GLOBL","LOCAL"}),
	0x8027F9A8: main.sym_fnc("L8027F9A8", flag={"GLOBL","LOCAL"}),
	0x8027F9C0: main.sym_fnc("L8027F9C0", flag={"GLOBL","LOCAL"}),
	0x8027F9D8: main.sym_fnc("L8027F9D8", flag={"GLOBL","LOCAL"}),
	0x8027F9F0: main.sym_fnc("camera_8027F9F0", arg=(
		"int",
		"float",
		"float",
		"float",
	), flag={"GLOBL"}),
	0x8027FB74: main.sym("camera_8027FB74"), # unused
	0x8027FC18: main.sym("camera_8027FC18"),
	0x8027FE20: main.sym("camera_8027FE20"),
	0x8027FF00: main.sym("camera_8027FF00"), # unused
	0x8027FFF8: main.sym("camera_8027FFF8"),
	0x80280368: main.sym("camera_80280368"),
	0x802804F4: main.sym("camera_802804F4"),
	0x802806A4: main.sym("camera_802806A4"),
	0x80280810: main.sym_fnc("camera_80280810", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x80280970: main.sym_fnc("camera_80280970", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x80280B00: main.sym("camera_80280B00"),
	0x80281188: main.sym("camera_80281188"),
	0x802813BC: main.sym("camera_802813BC"),
	0x802813EC: main.sym("camera_802813EC"),
	0x8028146C: main.sym("camera_8028146C"),
	0x80281588: main.sym("camera_80281588"),
	0x802816A0: main.sym_fnc("camera_802816A0", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x802817FC: main.sym("camera_802817FC"),
	0x80281904: main.sym_fnc("camera_80281904", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x80282280: main.sym_fnc("camera_80282280", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x802826A0: main.sym_fnc("camera_802826A0", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x80282C0C: main.sym_fnc("camera_80282C0C", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x80282C28: main.sym("camera_80282C28"), # unused
	0x80282C3C: main.sym("camera_80282C3C"),
	0x80282C7C: main.sym("camera_80282C7C"),
	0x80282CE0: main.sym("camera_80282CE0"),
	0x80282D78: main.sym_fnc("camera_80282D78", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x80283340: main.sym("camera_80283340"),
	0x80283578: main.sym("camera_80283578"),
	0x802839E4: main.sym("camera_802839E4"),
	0x80283A18: main.sym_fnc("camera_80283A18", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x80283A34: main.sym("camera_80283A34"),
	0x80283A68: main.sym_fnc("camera_80283A68", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x80283AF8: main.sym("camera_80283AF8"),
	0x80284CB8: main.sym("camera_80284CB8"),
	0x80284CFC: main.sym("camera_80284CFC"),
	0x80284D38: main.sym("camera_80284D38"),
	0x80284D74: main.sym_fnc("camera_80284D74", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x802850AC: main.sym("camera_802850AC"),
	0x802850EC: main.sym_fnc("camera_802850EC", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x8028517C: main.sym("camera_8028517C"), # unused
	0x802851DC: main.sym("camera_802851DC"),
	0x8028526C: main.sym("camera_8028526C"),
	0x802852F4: main.sym("camera_802852F4"),
	0x80285370: main.sym("camera_80285370"),
	0x80285808: main.sym_fnc("camera_80285808", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x802858A4: main.sym("camera_802858A4"),
	0x80285A2C: main.sym("camera_80285A2C"),
	0x80285D20: main.sym("camera_80285D20"),
	0x80285ED8: main.sym_fnc("camera_80285ED8", "int", (
		"CAMERA *cam",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}), # data / tbl
	0x80285F60: main.sym("camera_80285F60"),
	0x8028603C: main.sym("camera_8028603C"),
	0x80286088: main.sym("camera_80286088"),
	0x80286188: main.sym_fnc("camera_80286188", arg=(
		"CAMERA *cam",
		"SHORT",
		"SHORT",
	), flag={"GLOBL"}),
	0x80286420: main.sym("camera_80286420"),
	0x802868F8: main.sym_fnc("camera_802868F8", arg=(
		"CAMERA *",
	), flag={"GLOBL"}),
	0x80286C84: main.sym_fnc("L80286C84", flag={"GLOBL","LOCAL"}),
	0x80286C94: main.sym_fnc("L80286C94", flag={"GLOBL","LOCAL"}),
	0x80286CA4: main.sym_fnc("L80286CA4", flag={"GLOBL","LOCAL"}),
	0x80286CB4: main.sym_fnc("L80286CB4", flag={"GLOBL","LOCAL"}),
	0x80286CC4: main.sym_fnc("L80286CC4", flag={"GLOBL","LOCAL"}),
	0x80286CD4: main.sym_fnc("L80286CD4", flag={"GLOBL","LOCAL"}),
	0x80286CE4: main.sym_fnc("L80286CE4", flag={"GLOBL","LOCAL"}),
	0x80286CF4: main.sym_fnc("L80286CF4", flag={"GLOBL","LOCAL"}),
	0x80286D04: main.sym_fnc("L80286D04", flag={"GLOBL","LOCAL"}),
	0x80286D14: main.sym_fnc("L80286D14", flag={"GLOBL","LOCAL"}),
	0x80286D24: main.sym_fnc("L80286D24", flag={"GLOBL","LOCAL"}),
	0x80286D34: main.sym_fnc("L80286D34", flag={"GLOBL","LOCAL"}),
	0x80286D44: main.sym_fnc("L80286D44", flag={"GLOBL","LOCAL"}),
	0x80286D54: main.sym_fnc("L80286D54", flag={"GLOBL","LOCAL"}),
	0x80286D64: main.sym_fnc("L80286D64", flag={"GLOBL","LOCAL"}),
	0x80286F68: main.sym_fnc("camera_80286F68", arg=(
		"CAMERA *",
	), flag={"GLOBL"}),
	0x8028724C: main.sym("camera_8028724C"),
	0x8028752C: main.sym_fnc("L8028752C", flag={"GLOBL","LOCAL"}),
	0x80287578: main.sym_fnc("L80287578", flag={"GLOBL","LOCAL"}),
	0x8028758C: main.sym_fnc("L8028758C", flag={"GLOBL","LOCAL"}),
	0x802875A0: main.sym_fnc("L802875A0", flag={"GLOBL","LOCAL"}),
	0x80287664: main.sym_fnc("L80287664", flag={"GLOBL","LOCAL"}),
	0x8028767C: main.sym_fnc("L8028767C", flag={"GLOBL","LOCAL"}),
	0x80287694: main.sym_fnc("L80287694", flag={"GLOBL","LOCAL"}),
	0x802876B0: main.sym_fnc("L802876B0", flag={"GLOBL","LOCAL"}),
	0x802876C8: main.sym_fnc("L802876C8", flag={"GLOBL","LOCAL"}),
	0x802876EC: main.sym_fnc("L802876EC", flag={"GLOBL","LOCAL"}),
	0x802879EC: main.sym("camera_802879EC"),
	0x80287BC4: main.sym_fnc("camera_80287BC4", flag={"GLOBL"}),
	0x80287BE0: main.sym("camera_80287BE0"),
	0x80287CB8: main.sym("camera_80287CB8"),
	0x80287D30: main.sym("CtrlCamera", flag={"GLOBL"}), # shpcall
	0x80287DC0: main.sym("camera_80287DC0"),
	0x80287DD4: main.sym("camera_80287DD4"),
	0x80287DE8: main.sym("camera_80287DE8"),
	0x80287E28: main.sym("camera_80287E28"),
	0x80287E50: main.sym("camera_80287E50"),
	0x80287E78: main.sym("camera_80287E78"), # unused
	0x80287EA0: main.sym("camera_80287EA0"),
	0x802882E4: main.sym("camera_802882E4"),
	0x80288624: main.sym_fnc("camera_80288624", "int", (
		"int",
	), flag={"GLOBL"}),
	0x80288718: main.sym("camera_80288718"),
	0x80288888: main.sym("camera_80288888"),
	0x802888B4: main.sym_fnc("L802888B4", flag={"GLOBL","LOCAL"}),
	0x802888D8: main.sym_fnc("L802888D8", flag={"GLOBL","LOCAL"}),
	0x802888FC: main.sym_fnc("L802888FC", flag={"GLOBL","LOCAL"}),
	0x80288920: main.sym_fnc("L80288920", flag={"GLOBL","LOCAL"}),
	0x80288944: main.sym_fnc("L80288944", flag={"GLOBL","LOCAL"}),
	0x80288968: main.sym_fnc("L80288968", flag={"GLOBL","LOCAL"}),
	0x802889B0: main.sym("camera_802889B0"),
	0x80288CE4: main.sym("camera_80288CE4"),
	0x80288E68: main.sym("camera_80288E68"),
	0x80288F5C: main.sym("camera_80288F5C"),
	0x80289198: main.sym("camera_80289198"),
	0x80289214: main.sym("camera_80289214"),
	0x802892D8: main.sym("camera_802892D8"),
	0x8028935C: main.sym("camera_8028935C"),
	0x802893F4: main.sym("camera_802893F4"),
	0x80289488: main.sym("camera_80289488"),
	0x802894B4: main.sym("camera_802894B4"),
	0x8028956C: main.sym("camera_8028956C"),
	0x80289610: main.sym("camera_80289610"),
	0x80289684: main.sym("camera_80289684"),
	0x802896F8: main.sym("camera_802896F8"),
	0x8028976C: main.sym("camera_8028976C"),
	0x8028984C: main.sym("camera_8028984C"),
	0x8028993C: main.sym("camera_8028993C"),
	0x802899CC: main.sym("camera_802899CC"),
	0x80289B0C: main.sym("camera_80289B0C", flag={"GLOBL"}),
	0x80289C00: main.sym("camera_80289C00"),
	0x80289D20: main.sym("camera_80289D20"),
	0x80289F88: main.sym("camera_80289F88"),
	0x8028A080: main.sym("camera_8028A080"),
	0x8028A0F4: main.sym("camera_8028A0F4"),
	0x8028A4EC: main.sym("camera_8028A4EC"),
	0x8028A6BC: main.sym("camera_8028A6BC"),
	0x8028A7EC: main.sym("camera_8028A7EC"),
	0x8028A834: main.sym("camera_8028A834"),
	0x8028A8E8: main.sym("camera_8028A8E8"),
	0x8028AA28: main.sym("camera_8028AA28"),
	0x8028AAD8: main.sym("camera_8028AAD8"),
	0x8028AB60: main.sym("camera_8028AB60"),
	0x8028AC28: main.sym("camera_8028AC28"),
	0x8028ACCC: main.sym("camera_8028ACCC"),
	0x8028AD4C: main.sym("camera_8028AD4C"),
	0x8028AE1C: main.sym("camera_8028AE1C"),
	0x8028AEF0: main.sym("camera_8028AEF0"),
	0x8028AF4C: main.sym("camera_8028AF4C"),
	0x8028B00C: main.sym("camera_8028B00C"),
	0x8028B068: main.sym("camera_8028B068"),
	0x8028B11C: main.sym("camera_8028B11C"), # unused
	0x8028B1D0: main.sym("camera_8028B1D0"),
	0x8028B218: main.sym("camera_8028B218"),
	0x8028B32C: main.sym("camera_8028B32C"),
	0x8028B438: main.sym("camera_8028B438"),
	0x8028B50C: main.sym("camera_8028B50C"),
	0x8028B724: main.sym("camera_8028B724"),
	0x8028B754: main.sym("camera_8028B754"),
	0x8028B784: main.sym("camera_8028B784"),
	0x8028B7C4: main.sym("camera_8028B7C4"),
	0x8028B804: main.sym("camera_8028B804"),
	0x8028B850: main.sym("camera_8028B850"),
	0x8028B884: main.sym("camera_8028B884"),
	0x8028B8B8: main.sym("camera_8028B8B8"),
	0x8028B8EC: main.sym("camera_8028B8EC"),
	0x8028B920: main.sym("camera_8028B920"),
	0x8028B954: main.sym("camera_8028B954"),
	0x8028B9C4: main.sym("camera_8028B9C4"),
	0x8028BD34: main.sym_fnc("camera_8028BD34", arg=(
		"int",
	), flag={"GLOBL"}),
	0x8028BD98: main.sym("camera_8028BD98"),
	0x8028C038: main.sym("camera_8028C038"),
	0x8028C13C: main.sym("camera_8028C13C"),
	0x8028C18C: main.sym("camera_8028C18C"),
	0x8028C26C: main.sym("camera_8028C26C"),
	0x8028C2C8: main.sym("camera_8028C2C8"),
	0x8028C658: main.sym_fnc("L8028C658", flag={"GLOBL","LOCAL"}),
	0x8028C668: main.sym_fnc("L8028C668", flag={"GLOBL","LOCAL"}),
	0x8028C678: main.sym_fnc("L8028C678", flag={"GLOBL","LOCAL"}),
	0x8028C688: main.sym_fnc("L8028C688", flag={"GLOBL","LOCAL"}),
	0x8028C698: main.sym_fnc("L8028C698", flag={"GLOBL","LOCAL"}),
	0x8028C6A8: main.sym_fnc("L8028C6A8", flag={"GLOBL","LOCAL"}),
	0x8028C724: main.sym_fnc("L8028C724", flag={"GLOBL","LOCAL"}),
	0x8028C734: main.sym_fnc("L8028C734", flag={"GLOBL","LOCAL"}),
	0x8028C744: main.sym_fnc("L8028C744", flag={"GLOBL","LOCAL"}),
	0x8028C754: main.sym_fnc("L8028C754", flag={"GLOBL","LOCAL"}),
	0x8028C764: main.sym_fnc("L8028C764", flag={"GLOBL","LOCAL"}),
	0x8028C7A0: main.sym_fnc("camera_8028C7A0", arg=(
		"float",
		"float",
		"float",
	), flag={"GLOBL"}),
	0x8028C8F0: main.sym("camera_8028C8F0"),
	0x8028C9AC: main.sym("camera_8028C9AC"), # unused
	0x8028C9CC: main.sym("camera_8028C9CC"),
	0x8028CB08: main.sym("camera_8028CB08"), # unused
	0x8028CBF0: main.sym("camera_8028CBF0"),
	0x8028CD94: main.sym("camera_8028CD94"),
	0x8028CDEC: main.sym("camera_8028CDEC"),
	0x8028CE24: main.sym("camera_8028CE24"),
	0x8028D41C: main.sym("camera_8028D41C"), # unused
	0x8028D44C: main.sym("camera_8028D44C"),
	0x8028D5AC: main.sym("camera_8028D5AC"),
	0x8028D5FC: main.sym("camera_8028D5FC"),
	0x8028D658: main.sym("camera_8028D658"),
	0x8028D698: main.sym("camera_8028D698"),
	0x8028D79C: main.sym("camera_8028D79C"),
	0x8028D888: main.sym("camera_8028D888"),
	0x8028D92C: main.sym("camera_8028D92C"),
	0x8028DA18: main.sym_fnc("camera_8028DA18", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DA50: main.sym_fnc("camera_8028DA50", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DAEC: main.sym_fnc("camera_8028DAEC", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DB38: main.sym_fnc("camera_8028DB38", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DBB4: main.sym_fnc("camera_8028DBB4", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DBF4: main.sym_fnc("camera_8028DBF4", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DC1C: main.sym_fnc("camera_8028DC1C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DC70: main.sym_fnc("camera_8028DC70", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DCA4: main.sym("camera_8028DCA4"),
	0x8028DD48: main.sym_fnc("camera_8028DD48", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DE2C: main.sym_fnc("camera_8028DE2C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DE5C: main.sym_fnc("camera_8028DE5C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DE90: main.sym_fnc("camera_8028DE90", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DEC4: main.sym_fnc("camera_8028DEC4", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DEF8: main.sym_fnc("camera_8028DEF8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DF24: main.sym_fnc("camera_8028DF24", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DF6C: main.sym_fnc("camera_8028DF6C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DFB4: main.sym_fnc("camera_8028DFB4", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028DFE8: main.sym_fnc("camera_8028DFE8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E01C: main.sym_fnc("camera_8028E01C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E064: main.sym_fnc("camera_8028E064", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E098: main.sym_fnc("camera_8028E098", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E0EC: main.sym_fnc("camera_8028E0EC", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E164: main.sym_fnc("camera_8028E164", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E210: main.sym_fnc("camera_8028E210", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E298: main.sym_fnc("camera_8028E298", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E300: main.sym_fnc("camera_8028E300", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E334: main.sym("camera_8028E334"), # unused
	0x8028E38C: main.sym_fnc("camera_8028E38C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E3B8: main.sym_fnc("camera_8028E3B8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E3F0: main.sym_fnc("camera_8028E3F0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E41C: main.sym_fnc("camera_8028E41C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E450: main.sym_fnc("camera_8028E450", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E47C: main.sym_fnc("camera_8028E47C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E524: main.sym_fnc("camera_8028E524", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E55C: main.sym_fnc("camera_8028E55C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E594: main.sym_fnc("camera_8028E594", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E5CC: main.sym_fnc("camera_8028E5CC", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E604: main.sym_fnc("camera_8028E604", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E63C: main.sym_fnc("camera_8028E63C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E674: main.sym_fnc("camera_8028E674", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E6C4: main.sym_fnc("camera_8028E6C4", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E714: main.sym_fnc("camera_8028E714", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E758: main.sym_fnc("camera_8028E758", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E790: main.sym_fnc("camera_8028E790", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E7C8: main.sym_fnc("camera_8028E7C8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E818: main.sym_fnc("camera_8028E818", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E868: main.sym_fnc("camera_8028E868", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E8A0: main.sym_fnc("camera_8028E8A0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E8CC: main.sym_fnc("camera_8028E8CC", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E930: main.sym_fnc("camera_8028E930", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E974: main.sym_fnc("camera_8028E974", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E9A0: main.sym_fnc("camera_8028E9A0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028E9D8: main.sym_fnc("camera_8028E9D8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028EA28: main.sym_fnc("camera_8028EA28", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028EA60: main.sym_fnc("camera_8028EA60", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028EAB0: main.sym_fnc("camera_8028EAB0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028EAE8: main.sym_fnc("camera_8028EAE8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028EB38: main.sym_fnc("camera_8028EB38", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028EB88: main.sym_fnc("camera_8028EB88", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028EBC0: main.sym_fnc("camera_8028EBC0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028EC04: main.sym_fnc("camera_8028EC04", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028EC2C: main.sym_fnc("camera_8028EC2C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / ctl
	0x8028EC58: main.sym("camera_8028EC58"),
	0x8028ED30: main.sym("camera_8028ED30"),
	0x8028ED98: main.sym("camera_8028ED98"),
	0x8028EEB0: main.sym("camera_8028EEB0"),
	0x8028F670: main.sym("camera_8028F670"),
	0x8028F914: main.sym("camera_8028F914"),
	0x8028FC9C: main.sym("camera_8028FC9C"),
	0x8028FE24: main.sym("camera_8028FE24"),
	0x8028FE58: main.sym("camera_8028FE58"),
	0x8028FE84: main.sym("camera_8028FE84"), # unused
	0x8028FF04: main.sym_fnc("camera_8028FF04", "int", (
		"int",
		"OBJECT *",
		"int",
	), flag={"GLOBL"}),
	0x8028FFC8: main.sym_fnc("camera_8028FFC8", "int", (
		"int",
		"OBJECT *",
	), flag={"GLOBL"}),
	0x8029000C: main.sym("camera_8029000C", flag={"GLOBL"}),
	0x80290098: main.sym("camera_80290098"),
	0x802900E0: main.sym("camera_802900E0"),
	0x80290104: main.sym("camera_80290104"),
	0x80290168: main.sym("camera_80290168"),
	0x802901A4: main.sym("camera_802901A4"),
	0x802901FC: main.sym("camera_802901FC"),
	0x802903B8: main.sym("camera_802903B8"),
	0x8029040C: main.sym("camera_8029040C"), # unused
	0x80290440: main.sym_fnc("camera_80290440", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80290474: main.sym("camera_80290474"), # unused
	0x802904A8: main.sym("camera_802904A8"),
	0x802904E4: main.sym("camera_802904E4"),
	0x8029051C: main.sym("camera_8029051C"),
	0x8029053C: main.sym("camera_8029053C"),
	0x80290784: main.sym("camera_80290784"),
	0x802907F4: main.sym("camera_802907F4"),
	0x80290864: main.sym("camera_80290864"),
	0x802908E8: main.sym("camera_802908E8"),
	0x80290938: main.sym("camera_80290938"), # unused
	0x80290984: main.sym("camera_80290984"), # unused
	0x802909D0: main.sym("camera_802909D0"),
	0x80290A5C: main.sym("camera_80290A5C"),
	0x80290A90: main.sym("camera_80290A90"), # unused
	0x80290ABC: main.sym("camera_80290ABC"),
	0x80290B54: main.sym("camera_80290B54"),
	0x80290BA4: main.sym("camera_80290BA4"),
	0x80290BD8: main.sym("camera_80290BD8"),
	0x80290C08: main.sym("camera_80290C08"), # unused
	0x80290C1C: main.sym_fnc("camera_80290C1C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80290C30: main.sym_fnc("camera_80290C30", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80290C44: main.sym("camera_80290C44"),
	0x80290C9C: main.sym("camera_80290C9C"),
	0x80290D90: main.sym_fnc("camera_80290D90", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80290E00: main.sym_fnc("camera_80290E00", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80290E74: main.sym("camera_80290E74"),
	0x80290EB0: main.sym("camera_80290EB0"),
	0x80290F1C: main.sym_fnc("camera_80290F1C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80290F8C: main.sym_fnc("camera_80290F8C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80291074: main.sym("camera_80291074"),
	0x80291108: main.sym_fnc("camera_80291108", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802911C8: main.sym("camera_802911C8"),
	0x80291208: main.sym("camera_80291208"),
	0x8029127C: main.sym("camera_8029127C"),
	0x802912B8: main.sym("camera_802912B8"),
	0x80291354: main.sym_fnc("camera_80291354", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x8029142C: main.sym_fnc("camera_8029142C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802914CC: main.sym("camera_802914CC"),
	0x80291514: main.sym_fnc("camera_80291514", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802915D4: main.sym_fnc("camera_802915D4", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80291654: main.sym("camera_80291654"),
	0x802916B8: main.sym("camera_802916B8"),
	0x80291774: main.sym_fnc("camera_80291774", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802917E4: main.sym("camera_802917E4"),
	0x8029184C: main.sym("camera_8029184C"),
	0x80291870: main.sym_fnc("camera_80291870", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80291924: main.sym_fnc("camera_80291924", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80291964: main.sym("camera_80291964"),
	0x802919DC: main.sym("camera_802919DC"),
	0x80291AB4: main.sym("camera_80291AB4"),
	0x80291B18: main.sym("camera_80291B18"),
	0x80291B68: main.sym("camera_80291B68"),
	0x80291BF4: main.sym("camera_80291BF4"),
	0x80291C3C: main.sym("camera_80291C3C"),
	0x80291CD0: main.sym_fnc("camera_80291CD0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80291DB0: main.sym("camera_80291DB0"),
	0x80291E84: main.sym("camera_80291E84"),
	0x80291F18: main.sym("camera_80291F18"),
	0x80292038: main.sym("camera_80292038"),
	0x80292164: main.sym_fnc("camera_80292164", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802921FC: main.sym("camera_802921FC"),
	0x8029228C: main.sym("camera_8029228C"),
	0x80292324: main.sym("camera_80292324"),
	0x80292370: main.sym("camera_80292370"),
	0x802923B8: main.sym("camera_802923B8"),
	0x80292400: main.sym("camera_80292400"), # unused
	0x80292414: main.sym("camera_80292414"),
	0x8029244C: main.sym("camera_8029244C"),
	0x80292484: main.sym("camera_80292484"),
	0x802924B8: main.sym_fnc("camera_802924B8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80292628: main.sym("camera_80292628"),
	0x802926DC: main.sym("camera_802926DC"),
	0x802927D0: main.sym("camera_802927D0"),
	0x80292868: main.sym("camera_80292868"),
	0x80292974: main.sym("camera_80292974"),
	0x80292A20: main.sym("camera_80292A20"),
	0x80292A4C: main.sym("camera_80292A4C"),
	0x80292A80: main.sym_fnc("camera_80292A80", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80292C00: main.sym("camera_80292C00"),
	0x80292D80: main.sym("camera_80292D80"),
	0x80292E2C: main.sym("camera_80292E2C"),
	0x80292EC4: main.sym("camera_80292EC4"),
	0x80292F40: main.sym("camera_80292F40"),
	0x80292F98: main.sym("camera_80292F98"),
	0x80292FE4: main.sym("camera_80292FE4"),
	0x80293018: main.sym_fnc("camera_80293018", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802930F0: main.sym("camera_802930F0"),
	0x80293164: main.sym("camera_80293164"),
	0x802931C0: main.sym("camera_802931C0"),
	0x80293220: main.sym("camera_80293220"),
	0x8029328C: main.sym("camera_8029328C"),
	0x802932F4: main.sym("camera_802932F4"),
	0x80293328: main.sym("camera_80293328"),
	0x80293354: main.sym("camera_80293354"),
	0x8029338C: main.sym_fnc("camera_8029338C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80293488: main.sym("camera_80293488"),
	0x802934B4: main.sym("camera_802934B4"),
	0x802934D8: main.sym("camera_802934D8"),
	0x80293548: main.sym("camera_80293548"),
	0x802935E0: main.sym("camera_802935E0"),
	0x80293624: main.sym("camera_80293624"),
	0x8029369C: main.sym("camera_8029369C"),
	0x802936DC: main.sym("camera_802936DC"),
	0x80293708: main.sym("camera_80293708"),
	0x80293734: main.sym("camera_80293734"),
	0x802937E8: main.sym("camera_802937E8"),
	0x8029386C: main.sym_fnc("camera_8029386C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802938C8: main.sym_fnc("camera_802938C8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80293944: main.sym_fnc("camera_80293944", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80293ABC: main.sym("camera_80293ABC"),
	0x80293AE8: main.sym("camera_80293AE8"),
	0x80293B70: main.sym("camera_80293B70"),
	0x80293BF4: main.sym("camera_80293BF4"),
	0x80293C2C: main.sym_fnc("camera_80293C2C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80293CB0: main.sym_fnc("camera_80293CB0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80293D5C: main.sym_fnc("camera_80293D5C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80293D90: main.sym("camera_80293D90"),
	0x80293DD4: main.sym("camera_80293DD4"),
	0x80293E7C: main.sym_fnc("camera_80293E7C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80293ED8: main.sym_fnc("camera_80293ED8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80293F2C: main.sym("camera_80293F2C"),
	0x80293F70: main.sym_fnc("camera_80293F70", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80293FCC: main.sym("camera_80293FCC"),
	0x80294024: main.sym("camera_80294024"),
	0x80294088: main.sym("camera_80294088"),
	0x802940CC: main.sym("camera_802940CC"),
	0x8029410C: main.sym("camera_8029410C"),
	0x802942CC: main.sym("camera_802942CC"),
	0x802942F0: main.sym_fnc("camera_802942F0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802943D4: main.sym_fnc("camera_802943D4", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80294428: main.sym("camera_80294428"),
	0x80294718: main.sym("camera_80294718"),
	0x802947A4: main.sym("camera_802947A4"),
	0x8029480C: main.sym("camera_8029480C"),
	0x802948A0: main.sym("camera_802948A0"),
	0x80294A14: main.sym_fnc("camera_80294A14", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80294A94: main.sym_fnc("camera_80294A94", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80294AE8: main.sym("camera_80294AE8"),
	0x80294B78: main.sym("camera_80294B78"),
	0x80294BB4: main.sym("camera_80294BB4"),
	0x80294C28: main.sym("camera_80294C28"),
	0x80294C5C: main.sym_fnc("camera_80294C5C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80294CC4: main.sym("camera_80294CC4"),
	0x80294D48: main.sym("camera_80294D48"),
	0x80294D88: main.sym("camera_80294D88"), # unused
	0x80294DB4: main.sym_fnc("camera_80294DB4", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80294E24: main.sym("camera_80294E24"),
	0x80294EA8: main.sym("camera_80294EA8"),
	0x80294EE8: main.sym_fnc("camera_80294EE8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80294F58: main.sym("camera_80294F58"),
	0x80294F94: main.sym("camera_80294F94"),
	0x80294FEC: main.sym_fnc("camera_80294FEC", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802950B0: main.sym("camera_802950B0"),
	0x80295140: main.sym("camera_80295140"),
	0x802951F0: main.sym("camera_802951F0"),
	0x80295270: main.sym_fnc("camera_80295270", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80295310: main.sym("camera_80295310"),
	0x802953DC: main.sym("camera_802953DC"),
	0x80295418: main.sym_fnc("camera_80295418", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80295480: main.sym("camera_80295480"),
	0x802954EC: main.sym("camera_802954EC"),
	0x80295518: main.sym("camera_80295518"),
	0x80295580: main.sym("camera_80295580"),
	0x80295670: main.sym("camera_80295670"),
	0x80295740: main.sym("camera_80295740"),
	0x8029576C: main.sym("camera_8029576C"),
	0x802957C8: main.sym_fnc("camera_802957C8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80295894: main.sym_fnc("camera_80295894", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802958D4: main.sym("camera_802958D4"),
	0x80295930: main.sym_fnc("camera_80295930", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802959CC: main.sym("camera_802959CC"), # unused
	0x80295A58: main.sym("camera_80295A58"),
	0x80295BF0: main.sym("camera_80295BF0"),
	0x80295E24: main.sym("camera_80295E24"),
	0x80295E8C: main.sym_fnc("camera_80295E8C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80295FB0: main.sym_fnc("camera_80295FB0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80295FD8: main.sym_fnc("camera_80295FD8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80296020: main.sym("camera_80296020"),
	0x802960B0: main.sym("camera_802960B0"), # unused
	0x80296160: main.sym_fnc("camera_80296160", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802962C8: main.sym_fnc("camera_802962C8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802962F0: main.sym_fnc("camera_802962F0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80296318: main.sym("camera_80296318"),
	0x802963B8: main.sym("camera_802963B8"),
	0x8029652C: main.sym("camera_8029652C"),
	0x8029665C: main.sym("camera_8029665C"),
	0x8029669C: main.sym("camera_8029669C"),
	0x802966E4: main.sym("camera_802966E4"),
	0x80296710: main.sym_fnc("camera_80296710", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802967C4: main.sym_fnc("camera_802967C4", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x8029685C: main.sym("camera_8029685C"),
	0x802968A0: main.sym_fnc("camera_802968A0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x8029695C: main.sym("camera_8029695C"),
	0x802969F8: main.sym_fnc("camera_802969F8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80296A64: main.sym("camera_80296A64"),
	0x80296B30: main.sym_fnc("camera_80296B30", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80296BC8: main.sym("camera_80296BC8"),
	0x80296C4C: main.sym("camera_80296C4C"),
	0x80296D60: main.sym("camera_80296D60"),
	0x80296DA8: main.sym("camera_80296DA8"),
	0x80296EB4: main.sym("camera_80296EB4"),
	0x80296F38: main.sym("camera_80296F38"),
	0x80296F70: main.sym("camera_80296F70"), # unused
	0x80296FA8: main.sym_fnc("camera_80296FA8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80297148: main.sym("camera_80297148"),
	0x8029720C: main.sym("camera_8029720C"),
	0x80297290: main.sym("camera_80297290"),
	0x802972EC: main.sym("camera_802972EC"),
	0x80297300: main.sym("camera_80297300"),
	0x80297384: main.sym("camera_80297384"),
	0x802973B0: main.sym_fnc("camera_802973B0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80297464: main.sym("camera_80297464"),
	0x80297560: main.sym("camera_80297560"),
	0x8029758C: main.sym("camera_8029758C"),
	0x802975C4: main.sym("camera_802975C4"),
	0x8029762C: main.sym_fnc("camera_8029762C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802976BC: main.sym("camera_802976BC"),
	0x80297728: main.sym("camera_80297728"),
	0x80297748: main.sym("camera_80297748"),
	0x80297784: main.sym("camera_80297784"),
	0x802977C8: main.sym("camera_802977C8"),
	0x802977F4: main.sym("camera_802977F4"),
	0x80297820: main.sym("camera_80297820"),
	0x8029784C: main.sym_fnc("camera_8029784C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80297908: main.sym_fnc("camera_80297908", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80297A38: main.sym_fnc("camera_80297A38", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80297A64: main.sym_fnc("camera_80297A64", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80297B58: main.sym("camera_80297B58"),
	0x80297B84: main.sym_fnc("camera_80297B84", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80297C14: main.sym("camera_80297C14"),
	0x80297C40: main.sym_fnc("camera_80297C40", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80297D60: main.sym_fnc("L80297D60", flag={"GLOBL","LOCAL"}),
	0x80297DA0: main.sym_fnc("L80297DA0", flag={"GLOBL","LOCAL"}),
	0x80297E00: main.sym_fnc("L80297E00", flag={"GLOBL","LOCAL"}),
	0x80297E20: main.sym_fnc("L80297E20", flag={"GLOBL","LOCAL"}),
	0x80297E60: main.sym_fnc("L80297E60", flag={"GLOBL","LOCAL"}),
	0x80297EA0: main.sym_fnc("L80297EA0", flag={"GLOBL","LOCAL"}),
	0x80297EC0: main.sym_fnc("L80297EC0", flag={"GLOBL","LOCAL"}),
	0x80297F00: main.sym_fnc("L80297F00", flag={"GLOBL","LOCAL"}),
	0x80297F20: main.sym_fnc("L80297F20", flag={"GLOBL","LOCAL"}),
	0x80297F40: main.sym_fnc("L80297F40", flag={"GLOBL","LOCAL"}),
	0x80298024: main.sym_fnc("L80298024", flag={"GLOBL","LOCAL"}),
	0x802980DC: main.sym("camera_802980DC"),
	0x8029819C: main.sym("camera_8029819C"),
	0x80298218: main.sym("camera_80298218"),
	0x80298254: main.sym("camera_80298254"),
	0x80298290: main.sym("camera_80298290"),
	0x802983B4: main.sym_fnc("camera_802983B4", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80298458: main.sym_fnc("camera_80298458", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802984A0: main.sym("camera_802984A0"),
	0x802984B4: main.sym_fnc("camera_802984B4", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802987B0: main.sym("camera_802987B0"),
	0x8029894C: main.sym("camera_8029894C"),
	0x802989E8: main.sym("camera_802989E8"),
	0x80298AF8: main.sym_fnc("camera_80298AF8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80298BA0: main.sym_fnc("camera_80298BA0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80298C2C: main.sym_fnc("camera_80298C2C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80298CCC: main.sym_fnc("camera_80298CCC", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80298D44: main.sym_fnc("camera_80298D44", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80298D9C: main.sym_fnc("camera_80298D9C", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80298FE8: main.sym_fnc("camera_80298FE8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80299100: main.sym_fnc("camera_80299100", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80299154: main.sym_fnc("camera_80299154", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802991A8: main.sym_fnc("camera_802991A8", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802991F0: main.sym_fnc("camera_802991F0", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802992CC: main.sym_fnc("camera_802992CC", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80299360: main.sym_fnc("camera_80299360", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x80299404: main.sym_fnc("camera_80299404", arg=(
		"CAMERA *cam",
	), flag={"GLOBL"}), # data / demo
	0x802994E8: main.sym("camera_802994E8"),
	0x8029956C: main.sym_fnc("L8029956C", flag={"GLOBL","LOCAL"}),
	0x802995B4: main.sym_fnc("L802995B4", flag={"GLOBL","LOCAL"}),
	0x802995FC: main.sym_fnc("L802995FC", flag={"GLOBL","LOCAL"}),
	0x80299644: main.sym_fnc("L80299644", flag={"GLOBL","LOCAL"}),
	0x8029968C: main.sym_fnc("L8029968C", flag={"GLOBL","LOCAL"}),
	0x802996D4: main.sym_fnc("L802996D4", flag={"GLOBL","LOCAL"}),
	0x8029971C: main.sym_fnc("L8029971C", flag={"GLOBL","LOCAL"}),
	0x80299764: main.sym_fnc("L80299764", flag={"GLOBL","LOCAL"}),
	0x802997AC: main.sym_fnc("L802997AC", flag={"GLOBL","LOCAL"}),
	0x802997F4: main.sym_fnc("L802997F4", flag={"GLOBL","LOCAL"}),
	0x8029983C: main.sym_fnc("L8029983C", flag={"GLOBL","LOCAL"}),
	0x80299884: main.sym_fnc("L80299884", flag={"GLOBL","LOCAL"}),
	0x802998CC: main.sym_fnc("L802998CC", flag={"GLOBL","LOCAL"}),
	0x80299914: main.sym_fnc("L80299914", flag={"GLOBL","LOCAL"}),
	0x8029995C: main.sym_fnc("L8029995C", flag={"GLOBL","LOCAL"}),
	0x802999A4: main.sym_fnc("L802999A4", flag={"GLOBL","LOCAL"}),
	0x802999EC: main.sym_fnc("L802999EC", flag={"GLOBL","LOCAL"}),
	0x80299A34: main.sym_fnc("L80299A34", flag={"GLOBL","LOCAL"}),
	0x80299A7C: main.sym_fnc("L80299A7C", flag={"GLOBL","LOCAL"}),
	0x80299AC4: main.sym_fnc("L80299AC4", flag={"GLOBL","LOCAL"}),
	0x80299B0C: main.sym_fnc("L80299B0C", flag={"GLOBL","LOCAL"}),
	0x80299B54: main.sym_fnc("L80299B54", flag={"GLOBL","LOCAL"}),
	0x80299B9C: main.sym_fnc("L80299B9C", flag={"GLOBL","LOCAL"}),
	0x80299BE4: main.sym_fnc("L80299BE4", flag={"GLOBL","LOCAL"}),
	0x80299C2C: main.sym_fnc("L80299C2C", flag={"GLOBL","LOCAL"}),
	0x80299C74: main.sym_fnc("L80299C74", flag={"GLOBL","LOCAL"}),
	0x80299CBC: main.sym_fnc("L80299CBC", flag={"GLOBL","LOCAL"}),
	0x80299D04: main.sym_fnc("L80299D04", flag={"GLOBL","LOCAL"}),
	0x80299D4C: main.sym_fnc("L80299D4C", flag={"GLOBL","LOCAL"}),
	0x80299D94: main.sym_fnc("L80299D94", flag={"GLOBL","LOCAL"}),
	0x80299DDC: main.sym_fnc("L80299DDC", flag={"GLOBL","LOCAL"}),
	0x80299E24: main.sym_fnc("L80299E24", flag={"GLOBL","LOCAL"}),
	0x80299E6C: main.sym_fnc("L80299E6C", flag={"GLOBL","LOCAL"}),
	0x80299EB4: main.sym_fnc("L80299EB4", flag={"GLOBL","LOCAL"}),
	0x80299EFC: main.sym_fnc("L80299EFC", flag={"GLOBL","LOCAL"}),
	0x80299F44: main.sym_fnc("L80299F44", flag={"GLOBL","LOCAL"}),
	0x80299F8C: main.sym_fnc("L80299F8C", flag={"GLOBL","LOCAL"}),
	0x80299FD4: main.sym_fnc("L80299FD4", flag={"GLOBL","LOCAL"}),
	0x8029A01C: main.sym_fnc("L8029A01C", flag={"GLOBL","LOCAL"}),
	0x8029A064: main.sym_fnc("L8029A064", flag={"GLOBL","LOCAL"}),
	0x8029A0AC: main.sym_fnc("L8029A0AC", flag={"GLOBL","LOCAL"}),
	0x8029A0F4: main.sym_fnc("L8029A0F4", flag={"GLOBL","LOCAL"}),
	0x8029A13C: main.sym_fnc("L8029A13C", flag={"GLOBL","LOCAL"}),
	0x8029A184: main.sym_fnc("L8029A184", flag={"GLOBL","LOCAL"}),
	0x8029A1CC: main.sym_fnc("L8029A1CC", flag={"GLOBL","LOCAL"}),
	0x8029A214: main.sym_fnc("L8029A214", flag={"GLOBL","LOCAL"}),
	0x8029A2F8: main.sym("camera_8029A2F8"),
	0x8029A37C: main.sym("camera_8029A37C"),
	0x8029A3B4: main.sym("camera_8029A3B4"),
	0x8029A41C: main.sym("camera_8029A41C"),
	0x8029A4D0: main.sym("camera_8029A4D0"),
	0x8029A5BC: main.sym("camera_8029A5BC"), # unused
	0x8029A5E8: main.sym("camera_8029A5E8"),
	0x8029A60C: main.sym("camera_8029A60C"),
	0x8029A64C: main.sym("camera_8029A64C"),
	0x8029A670: main.sym("camera_8029A670"),
	0x8029A694: main.sym("camera_8029A694"),
	0x8029A6F4: main.sym("camera_8029A6F4"),
	0x8029A81C: main.sym("camera_8029A81C"), # unused
	0x8029A858: main.sym("camera_8029A858"),
	0x8029A894: main.sym("camera_8029A894"),
	0x8029A8D0: main.sym("camera_8029A8D0"),
	0x8029A968: main.sym("camera_8029A968"),
	0x8029A9A4: main.sym("camera_8029A9A4"),
	0x8029AA3C: main.sym("CtrlPerspective", flag={"GLOBL"}), # shpcall
	0x8029AAAC: main.sym_fnc("L8029AAAC", flag={"GLOBL","LOCAL"}),
	0x8029AABC: main.sym_fnc("L8029AABC", flag={"GLOBL","LOCAL"}),
	0x8029AACC: main.sym_fnc("L8029AACC", flag={"GLOBL","LOCAL"}),
	0x8029AADC: main.sym_fnc("L8029AADC", flag={"GLOBL","LOCAL"}),
	0x8029AAEC: main.sym_fnc("L8029AAEC", flag={"GLOBL","LOCAL"}),
	0x8029AAFC: main.sym_fnc("L8029AAFC", flag={"GLOBL","LOCAL"}),
	0x8029AB0C: main.sym_fnc("L8029AB0C", flag={"GLOBL","LOCAL"}),
	0x8029AB1C: main.sym_fnc("L8029AB1C", flag={"GLOBL","LOCAL"}),
	0x8029AB2C: main.sym_fnc("L8029AB2C", flag={"GLOBL","LOCAL"}),
	0x8029AB3C: main.sym_fnc("L8029AB3C", flag={"GLOBL","LOCAL"}),
	0x8029AB4C: main.sym_fnc("L8029AB4C", flag={"GLOBL","LOCAL"}),
	0x8029AB5C: main.sym_fnc("L8029AB5C", flag={"GLOBL","LOCAL"}),
	0x8029AB94: main.sym("camera_8029AB94"),
	0x8029ABB0: main.sym("camera_8029ABB0"),
	0x8029AC30: main.sym("camera_8029AC30"),
	0x8029AD80: main.sym("camera_8029AD80"), # unused
	0x8029AE40: main.sym("camera_8029AE40"), # unused
	0x8029AEF8: main.sym("camera_8029AEF8"),
	0x8029AF98: main.sym("camera_8029AF98"),
	0x8029B08C: main.sym("camera_8029B08C", flag={"GLOBL"}), # objcall
	0x8029B28C: main.sym("camera_8029B28C"),
	0x8029B358: main.sym("camera_8029B358"),
	0x8029B3C8: main.sym("camera_8029B3C8"),
	0x8029B49C: main.sym("camera_8029B49C", flag={"GLOBL"}), # objcall
	0x8029BDE4: main.sym("camera_8029BDE4", flag={"GLOBL"}), # objcall
	0x8029BF64: main.sym("camera_8029BF64", flag={"GLOBL"}), # objcall
	0x8029C0E4: main.sym("camera_8029C0E4"),
	0x8029C254: main.sym("camera_8029C254", flag={"GLOBL"}), # objcall
	0x8029C2FC: main.sym_fnc("L8029C2FC", flag={"GLOBL","LOCAL"}),
	0x8029C320: main.sym_fnc("L8029C320", flag={"GLOBL","LOCAL"}),
	0x8029C344: main.sym_fnc("L8029C344", flag={"GLOBL","LOCAL"}),
	0x8029C554: main.sym_fnc("L8029C554", flag={"GLOBL","LOCAL"}),
	0x8029C5EC: main.sym_fnc("L8029C5EC", flag={"GLOBL","LOCAL"}),

	# src/course.c
	0x8029C770: main.sym_fnc("CourseInit", flag={"GLOBL"}),

	# src/object.c
	0x8029C780: main.sym_fnc("Player_CopyInfo"),
	0x8029C9CC: main.sym_fnc("Player_SetEffect", arg=(
		"u32 flag",
		"SHORT shape",
		"OBJLANG *script",
	)),
	0x8029CA58: main.sym_fnc("Mario_Proc", flag={"GLOBL"}), # objcall
	0x8029CB34: main.sym_fnc("ObjListExecNormal", "int", (
		"OBJECT *root",
		"OBJECT *obj",
	)),
	0x8029CBC8: main.sym_fnc("ObjListExecFrozen", "int", (
		"OBJECT *root",
		"OBJECT *obj",
	)),
	0x8029CD28: main.sym_fnc("ObjListExec", "int", (
		"OBJECT *root",
	)),
	0x8029CD98: main.sym_fnc("ObjListCleanup", "int", (
		"OBJECT *root",
	)),
	0x8029CE58: main.sym_fnc("ObjSetActorFlag", arg=(
		"OBJECT *obj",
		"UCHAR flag",
	), flag={"GLOBL"}),
	0x8029CEDC: main.sym_fnc("ObjectClose", arg=(
		"int screen",
		"int group",
	), flag={"GLOBL"}),
	0x8029CFB0: main.sym_fnc("ObjectOpen", arg=(
		"int screen",
		"ACTOR *actor",
	), flag={"GLOBL"}),
	0x8029D1D8: main.sym_fnc("object_8029D1D8"),
	0x8029D1E8: main.sym_fnc("ObjectInit", flag={"GLOBL"}),
	0x8029D324: main.sym_fnc("ObjectExec1"),
	0x8029D374: main.sym_fnc("ObjectExec2"),
	0x8029D428: main.sym_fnc("ObjectCleanup"),
	0x8029D4D0: main.sym_fnc("object_8029D4D0", "USHORT", (
		"OSTime *t",
		"int i",
	)), # unused
	0x8029D690: main.sym_fnc("ObjectProc", arg=(
		"int screen",
	), flag={"GLOBL"}),

	# src/objectlib.c
	0x8029D890: main.sym_fnc("CtrlObjectHand", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL","LOCAL"}), # shpcall
	0x8029D924: main.sym_fnc("CtrlObjectAlpha", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL","LOCAL"}), # shpcall
	0x8029DB48: main.sym_fnc("CtrlObjectShape", "void *", (
		"int code",
		"SHAPE *shape",
	), flag={"GLOBL","LOCAL"}), # shpcall
	0x8029DBD4: main.sym_fnc("CtrlArea", "void *", (
		"int code",
		"SHAPE *shape",
	), flag={"GLOBL","LOCAL"}), # shpcall
	0x8029DCD4: main.sym_fnc("ObjSetPosRelXFM", arg=(
		"FMTX m",
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x8029DDA8: main.sym_fnc("ObjFMtxScaleCopy", arg=(
		"OBJECT *obj",
		"FMTX dst",
		"FMTX src",
	), flag={"GLOBL"}),
	0x8029DE80: main.sym_fnc("FMtxInvCatAffine", arg=(
		"FMTX dst",
		"FMTX src",
		"FMTX cam",
	), flag={"GLOBL"}),
	0x8029E1B0: main.sym_fnc("ObjectSetTake", arg=(
		"OBJECT *o",
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x8029E27C: main.sym_fnc("ObjCalcDist2D", "float", (
		"OBJECT *obj",
		"OBJECT *o",
	), flag={"GLOBL"}),
	0x8029E2F8: main.sym_fnc("ObjCalcDist3D", "float", (
		"OBJECT *obj",
		"OBJECT *o",
	), flag={"GLOBL"}),
	0x8029E398: main.sym_fnc("ObjectAccelerate", arg=(
		"float limit",
		"float accel",
	), flag={"GLOBL"}),
	0x8029E3E8: main.sym_fnc("Accelerate", "int", (
		"float *speed",
		"float limit",
		"float accel",
	), flag={"GLOBL"}),
	0x8029E494: main.sym_fnc("ApproachPos", "float", (
		"float x",
		"float target",
		"float speed",
	), flag={"GLOBL"}),
	0x8029E530: main.sym_fnc("ApproachAng", "short", (
		"short x",
		"short target",
		"short speed",
	), flag={"GLOBL"}),
	0x8029E5EC: main.sym_fnc("ObjectTurn", "int", (
		"SHORT target",
		"SHORT speed",
	), flag={"GLOBL"}),
	0x8029E694: main.sym_fnc("ObjCalcAngY", "SHORT", (
		"OBJECT *obj",
		"OBJECT *o",
	), flag={"GLOBL"}),
	0x8029E714: main.sym_fnc("ObjectTurnTo", "short", (
		"OBJECT *a",
		"OBJECT *b",
		"SHORT mem",
		"SHORT speed",
	), flag={"GLOBL"}),
	0x8029E8BC: main.sym_fnc("ObjSetRel", arg=(
		"OBJECT *obj",
		"SHORT offx",
		"SHORT offy",
		"SHORT offz",
	), flag={"GLOBL"}),
	0x8029E914: main.sym_fnc("ObjSetPos", arg=(
		"OBJECT *obj",
		"SHORT posx",
		"SHORT posy",
		"SHORT posz",
	), flag={"GLOBL"}),
	0x8029E96C: main.sym_fnc("ObjSetAng", arg=(
		"OBJECT *obj",
		"SHORT angx",
		"SHORT angy",
		"SHORT angz",
	), flag={"GLOBL"}),
	0x8029E9AC: main.sym_fnc("ObjMakeAt", "OBJECT *", (
		"OBJECT *parent",
		"SHORT arg",
		"int shape",
		"OBJLANG *script",
		"SHORT posx",
		"SHORT posy",
		"SHORT posz",
		"SHORT angx",
		"SHORT angy",
		"SHORT angz",
	), flag={"GLOBL"}),
	0x8029EA24: main.sym_fnc("ObjMakeRel", "OBJECT *", (
		"OBJECT *parent",
		"int shape",
		"OBJLANG *script",
		"SHORT relx",
		"SHORT rely",
		"SHORT relz",
		"SHORT angx",
		"SHORT angy",
		"SHORT angz",
	), flag={"GLOBL"}),
	0x8029EAAC: main.sym_fnc("ObjMakeHereMtx", "OBJECT *", (
		"OBJECT *parent",
		"int shape",
		"OBJLANG *script",
	)), # unused
	0x8029EB04: main.sym_fnc("ObjMakeSplash", "OBJECT *", (
		"OBJECT *parent",
		"SPLASH *splash",
	), flag={"GLOBL"}),
	0x8029ED20: main.sym_fnc("ObjMake", "OBJECT *", (
		"OBJECT *parent",
		"SHORT arg",
		"int shape",
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x8029EDCC: main.sym_fnc("ObjMakeHere", "OBJECT *", (
		"OBJECT *parent",
		"int shape",
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x8029EE24: main.sym_fnc("ObjMakeEffect", "OBJECT *", (
		"SHORT offy",
		"float scale",
		"OBJECT *parent",
		"int shape",
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x8029EEB8: main.sym_fnc("ObjMakeHereScale", "OBJECT *", (
		"OBJECT *parent",
		"int shape",
		"OBJLANG *script",
		"float scale",
	), flag={"GLOBL"}),
	0x8029EF20: main.sym_fnc("ObjAddRelPos", arg=(
		"OBJECT *obj",
	)), # static
	0x8029EF64: main.sym_fnc("ObjMakeOff", "OBJECT *", (
		"SHORT code",
		"SHORT offx",
		"SHORT offy",
		"SHORT offz",
		"OBJECT *parent",
		"int shape",
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x8029EFFC: main.sym_fnc("ObjMakeOffScale", "OBJECT *", (
		"SHORT code",
		"SHORT offx",
		"SHORT offy",
		"SHORT offz",
		"float scale",
		"OBJECT *parent",
		"int shape",
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x8029F070: main.sym_fnc("ObjectMove3D"), # unused
	0x8029F0C8: main.sym_fnc("ObjCopyShapeOff", arg=(
		"OBJECT *obj",
		"OBJECT *o",
	), flag={"GLOBL"}),
	0x8029F0E0: main.sym_fnc("ObjCopyCoord", arg=(
		"OBJECT *obj",
		"OBJECT *o",
	), flag={"GLOBL"}),
	0x8029F120: main.sym_fnc("ObjCopyPos", arg=(
		"OBJECT *obj",
		"OBJECT *o",
	), flag={"GLOBL"}),
	0x8029F148: main.sym_fnc("ObjCopyAng", arg=(
		"OBJECT *obj",
		"OBJECT *o",
	), flag={"GLOBL"}), # static
	0x8029F188: main.sym_fnc("ObjSetShapePos", arg=(
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x8029F1B0: main.sym_fnc("ObjStartAnime", arg=(
		"OBJECT *obj",
		"int anime",
	)), # unused
	0x8029F200: main.sym_fnc("MtxTransform3", arg=(
		"FMTX m",
		"FVEC dst",
		"FVEC src",
	), flag={"GLOBL"}),
	0x8029F274: main.sym_fnc("InvTransform3", arg=(
		"FMTX m",
		"FVEC dst",
		"FVEC src",
	), flag={"GLOBL"}),
	0x8029F2EC: main.sym_fnc("ObjScaleMtx", arg=(
		"OBJECT *obj",
	)),
	0x8029F3A8: main.sym_fnc("ObjCopyScale", arg=(
		"OBJECT *obj",
		"OBJECT *o",
	), flag={"GLOBL"}),
	0x8029F3D0: main.sym_fnc("ObjSetScaleXYZ", arg=(
		"OBJECT *obj",
		"float scalex",
		"float scaley",
		"float scalez",
	), flag={"GLOBL"}),
	0x8029F404: main.sym_fnc("ObjSetScale", arg=(
		"OBJECT *obj",
		"float scale",
	), flag={"GLOBL"}),
	0x8029F430: main.sym_fnc("ObjectSetScale", arg=(
		"float scale",
	), flag={"GLOBL"}),
	0x8029F464: main.sym_fnc("ObjectStartAnime", arg=(
		"int anime",
	), flag={"GLOBL"}),
	0x8029F4B4: main.sym_fnc("ObjectSetAnime", arg=(
		"int anime",
	), flag={"GLOBL"}),
	0x8029F514: main.sym_fnc("ObjectSetAnimeV", arg=(
		"int anime",
		"float speed",
	), flag={"GLOBL"}),
	0x8029F59C: main.sym_fnc("ObjInitAnime", arg=(
		"OBJECT *obj",
		"void *animep",
		"int anime",
	), flag={"GLOBL"}),
	0x8029F600: main.sym_fnc("ObjActivate", arg=(
		"OBJECT *obj",
	)), # unused
	0x8029F620: main.sym_fnc("ObjectSetActive", flag={"GLOBL"}),
	0x8029F644: main.sym_fnc("ObjDeactivate", arg=(
		"OBJECT *obj",
	)), # unused
	0x8029F66C: main.sym_fnc("ObjectClrActive", flag={"GLOBL"}),
	0x8029F694: main.sym_fnc("ObjectShow", flag={"GLOBL"}),
	0x8029F6BC: main.sym_fnc("ObjectHide", flag={"GLOBL"}),
	0x8029F6E0: main.sym_fnc("ObjectSetPosOff", arg=(
		"OBJECT *o",
		"float offx",
		"float offy",
		"float offz",
	), flag={"GLOBL"}),
	0x8029F7D8: main.sym_fnc("ObjectSetPosOffParent", arg=(
		"float offx",
		"float offy",
		"float offz",
	)),
	0x8029F820: main.sym_fnc("objectlib_8029F820", flag={"GLOBL"}),
	0x8029F848: main.sym_fnc("objectlib_8029F848"), # unused
	0x8029F8EC: main.sym_fnc("ObjSetShapeAng", arg=(
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x8029F914: main.sym_fnc("ObjGetScriptType", "int", (
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x8029F95C: main.sym_fnc("ObjectFindObj", "OBJECT *", (
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x8029F998: main.sym_fnc("ObjectFindDist", "float", (
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x8029F9EC: main.sym_fnc("ObjectFind", "OBJECT *", (
		"OBJLANG *script",
		"float *distp",
	), flag={"GLOBL"}),
	0x8029FB1C: main.sym_fnc("ObjGetEffect", "OBJECT *", flag={"GLOBL"}),
	0x8029FB68: main.sym_fnc("ObjCountEffect", "int"), # unused
	0x8029FBDC: main.sym_fnc("ObjCount", "int", (
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x8029FC9C: main.sym_fnc("ObjectFindTake", "OBJECT *", (
		"OBJLANG *script",
		"float dist",
	), flag={"GLOBL"}),
	0x8029FD8C: main.sym_fnc("ObjectResetState"),
	0x8029FDB4: main.sym_fnc("ObjectInitState", arg=(
		"int state",
	), flag={"GLOBL"}),
	0x8029FE00: main.sym_fnc("ObjectMatchP1Speed", arg=(
		"float min",
		"float scale",
	), flag={"GLOBL"}),
	0x8029FE6C: main.sym_fnc("ObjectAnimeHold", flag={"GLOBL"}),
	0x8029FEA4: main.sym_fnc("ObjectAnimeHoldEnd", flag={"GLOBL"}),
	0x8029FF04: main.sym_fnc("objectlib_8029FF04", "int", flag={"GLOBL"}),
	0x8029FFA4: main.sym_fnc("objectlib_8029FFA4", "int", flag={"GLOBL"}),
	0x802A0008: main.sym_fnc("ObjectIsAnimeFrame", "int", (
		"int frame",
	), flag={"GLOBL"}),
	0x802A0050: main.sym_fnc("ObjectIsAnimeFrameRange", "int", (
		"int start",
		"int count",
	), flag={"GLOBL"}),
	0x802A00AC: main.sym_fnc("ObjectIsAnimeFrameTable", "int", (
		"short *table",
	)), # unused
	0x802A0114: main.sym_fnc("Player1IsJump", "int", flag={"GLOBL"}),
	0x802A0154: main.sym_fnc("objectlib_802A0154", "int", flag={"GLOBL"}),
	0x802A0198: main.sym_fnc("ObjectSetAnimeJump", arg=(
		"float vely",
		"int anime",
	), flag={"GLOBL"}),
	0x802A01D8: main.sym_fnc("objectlib_802A01D8", arg=(
		"int anime",
		"int state",
	), flag={"GLOBL"}),
	0x802A0234: main.sym_fnc("objectlib_802A0234", arg=(
		"float velf",
		"float vely",
	)),
	0x802A0380: main.sym_fnc("objectlib_802A0380", arg=(
		"float velf",
		"float vely",
		"int state",
	), flag={"GLOBL"}),
	0x802A0474: main.sym_fnc("objectlib_802A0474", flag={"GLOBL"}),
	0x802A04C0: main.sym_fnc("ObjectSetShape", arg=(
		"int shape",
	), flag={"GLOBL"}),
	0x802A04F0: main.sym_fnc("Player1SetFlag", arg=(
		"u32 flag",
	)), # unused
	0x802A0514: main.sym_fnc("ObjectCheckHitResult", "int", (
		"int flag",
	), flag={"GLOBL"}),
	0x802A0568: main.sym_fnc("ObjKill", arg=(
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x802A057C: main.sym_fnc("objectlib_802A057C", flag={"GLOBL"}),
	0x802A05B4: main.sym_fnc("ObjectHitOFF", flag={"GLOBL"}),
	0x802A05D4: main.sym_fnc("ObjectHitON", flag={"GLOBL"}),
	0x802A05F0: main.sym_fnc("ObjHitON", arg=(
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x802A0604: main.sym_fnc("ObjectCheckGroundY", flag={"GLOBL"}),
	0x802A064C: main.sym_fnc("ObjectCheckGround", "BGFACE *", flag={"GLOBL"}),
	0x802A069C: main.sym_fnc("CalcDrag", arg=(
		"float *vel",
		"float drag",
	)),
	0x802A079C: main.sym_fnc("ObjectCalcDrag", arg=(
		"float drag",
	), flag={"GLOBL"}),
	0x802A07E8: main.sym_fnc("objectlib_802A07E8", "int", (
		"float ny",
		"int flag",
	)),
	0x802A0AB0: main.sym_fnc("objectlib_802A0AB0"),
	0x802A0BDC: main.sym_fnc("objectlib_802A0BDC", arg=(
		"float gravity",
		"float density",
	)),
	0x802A0D84: main.sym_fnc("objectlib_802A0D84", "float", (
		"float gravity",
		"float bounce",
	)),
	0x802A0E68: main.sym_fnc("objectlib_802A0E68", arg=(
		"float gravity",
		"float density",
		"float bounce",
	), flag={"GLOBL"}),
	0x802A10E0: main.sym_fnc("objectlib_802A10E0"), # unused
	0x802A10F0: main.sym_fnc("CheckFlag", "int", (
		"int *flag",
		"int mask",
	), flag={"GLOBL"}), # static
	0x802A113C: main.sym_fnc("ObjectHitWall", arg=(
		"float offset",
		"float radius",
	)), # unused
	0x802A11A8: main.sym_fnc("DeltaAng", "SHORT", (
		"SHORT a",
		"SHORT b",
	), flag={"GLOBL"}),
	0x802A120C: main.sym_fnc("ObjectMoveF", flag={"GLOBL"}),
	0x802A12A4: main.sym_fnc("ObjectMoveY", flag={"GLOBL"}),
	0x802A1308: main.sym_fnc("ObjectCalcVelF", flag={"GLOBL"}), # objcall
	0x802A1370: main.sym_fnc("objectlib_802A1370", "float", (
		"float x",
		"float target",
		"float limit",
		"float speed",
	), flag={"GLOBL"}),
	0x802A1424: main.sym_fnc("ObjIsObjHit", "int", (
		"OBJECT *obj",
		"OBJECT *o",
	), flag={"GLOBL"}),
	0x802A148C: main.sym_fnc("ObjectSetScript", arg=(
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x802A14C4: main.sym_fnc("ObjSetScript", arg=(
		"OBJECT *obj",
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x802A14FC: main.sym_fnc("ObjectHasScript", "int", arg=(
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x802A1554: main.sym_fnc("ObjHasScript", "int", arg=(
		"OBJECT *obj",
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x802A15AC: main.sym_fnc("ObjectDistMarioToSave", "float", flag={"GLOBL"}),
	0x802A1634: main.sym_fnc("ObjectDistToSave", "float", flag={"GLOBL"}),
	0x802A16AC: main.sym_fnc("ObjectInSaveSquare", "int", (
		"float size",
	)), # unused
	0x802A1774: main.sym_fnc("ObjectInSaveRect", "int", (
		"float xmin",
		"float xmax",
		"float zmin",
		"float zmax",
	)), # unused
	0x802A184C: main.sym_fnc("ObjectSavePos", flag={"GLOBL"}),
	0x802A188C: main.sym_fnc("ObjectSavePosStop", flag={"GLOBL"}),
	0x802A18DC: main.sym_fnc("ObjectShake", arg=(
		"float offy",
	), flag={"GLOBL"}),
	0x802A1930: main.sym_fnc("objectlib_802A1930", arg=(
		"OBJECT *obj",
		"int a1",
	), flag={"GLOBL"}),
	0x802A1960: main.sym_fnc("objectlib_802A1960", arg=(
		"OBJECT *obj",
		"int a1",
		"float dist",
	)), # unused
	0x802A19AC: main.sym_fnc("ObjSetBillboard", arg=(
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x802A19C8: main.sym_fnc("ObjectSetHitBox", arg=(
		"float radius",
		"float height",
	), flag={"GLOBL"}),
	0x802A19F0: main.sym_fnc("ObjectSetDmgBox", arg=(
		"float radius",
		"float height",
	), flag={"GLOBL"}),
	0x802A1A18: main.sym_fnc("ObjectMakeCoinCommon", arg=(
		"OBJECT *obj",
		"int max",
		"float f7",
		"OBJLANG *script",
		"SHORT range",
		"SHORT shape",
	)),
	0x802A1B34: main.sym_fnc("objectlib_802A1B34", arg=(
		"OBJECT *obj",
		"int max",
		"float f7",
		"SHORT range",
	)),
	0x802A1B8C: main.sym_fnc("ObjectMakeCoin", arg=(
		"OBJECT *obj",
		"int max",
		"float f7",
	), flag={"GLOBL"}),
	0x802A1BDC: main.sym_fnc("objectlib_802A1BDC", flag={"GLOBL"}),
	0x802A1C68: main.sym_fnc("ObjectDistToSaveY", "float"), # unused
	0x802A1CC4: main.sym_fnc("objectlib_802A1CC4", "int"), # unused
	0x802A1D7C: main.sym_fnc("objectlib_802A1D7C", "int", (
		"SHORT ang",
	)),
	0x802A1F3C: main.sym_fnc("ObjectCheckWall", "int", flag={"GLOBL"}),
	0x802A20F4: main.sym_fnc("objectlib_802A20F4"),
	0x802A21D4: main.sym_fnc("objectlib_802A21D4", arg=(
		"SHORT ang",
	)),
	0x802A2320: main.sym_fnc("objectlib_802A2320", flag={"GLOBL"}), # objcall
	0x802A2348: main.sym_fnc("objectlib_802A2348", arg=(
		"SHORT ang",
	), flag={"GLOBL"}),
	0x802A24D0: main.sym_fnc("objectlib_802A24D0", "int"),
	0x802A25B4: main.sym_fnc("ObjectProcMove", flag={"GLOBL"}),
	0x802A2644: main.sym_fnc("ObjectProcMoveF", flag={"GLOBL"}), # objcall
	0x802A2674: main.sym_fnc("ObjCopyCoordOff", arg=(
		"OBJECT *obj",
		"OBJECT *o",
		"float offx",
		"float offy",
		"float offz",
	)), # unused
	0x802A2748: main.sym_fnc("ObjectAngToSave", "SHORT", flag={"GLOBL"}),
	0x802A27B0: main.sym_fnc("ObjCopyCoordToShape", arg=(
		"OBJECT *obj",
		"OBJECT *o",
	), flag={"GLOBL"}),
	0x802A2804: main.sym_fnc("ObjAddTransform", arg=(
		"OBJECT *obj",
		"SHORT dst",
		"SHORT src",
	), flag={"GLOBL"}),
	0x802A2930: main.sym_fnc("ObjCalcMtx", arg=(
		"OBJECT *obj",
		"SHORT pos",
		"SHORT ang",
	), flag={"GLOBL"}),
	0x802A2A18: main.sym_fnc("ObjSetMtx", arg=(
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x802A2A84: main.sym_fnc("ObjCalcRel", arg=(
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x802A2B28: main.sym_fnc("ObjClrRel", arg=(
		"OBJECT *obj",
	)), # unused
	0x802A2B6C: main.sym_fnc("ObjectRotate"), # unused
	0x802A2BC4: main.sym_fnc("ObjectRotateShape", flag={"GLOBL"}), # objcall
	0x802A2C1C: main.sym_fnc("ObjectSyncAng"), # unused
	0x802A2C5C: main.sym_fnc("ObjectProcPath", "int", (
		"int status",
	), flag={"GLOBL"}),
	0x802A2ED4: main.sym_fnc("ChainInit", arg=(
		"CHAIN *chain",
	), flag={"GLOBL"}),
	0x802A2F14: main.sym_fnc("RandRange", "float", (
		"float range",
	), flag={"GLOBL"}),
	0x802A2F5C: main.sym_fnc("ObjRandScale", arg=(
		"OBJECT *obj",
		"float range",
		"float start",
	), flag={"GLOBL"}),
	0x802A2FC0: main.sym_fnc("ObjRandOff3D", arg=(
		"OBJECT *obj",
		"float range",
	), flag={"GLOBL"}),
	0x802A308C: main.sym_fnc("ObjRandOff2D", arg=(
		"OBJECT *obj",
		"float range",
	), flag={"GLOBL"}),
	0x802A3124: main.sym_fnc("ObjCalcVelULF", arg=(
		"OBJECT *obj",
	)),
	0x802A31E0: main.sym_fnc("ObjectMoveULF", flag={"GLOBL"}),
	0x802A3268: main.sym_fnc("objectlib_802A3268", "short", flag={"GLOBL"}),
	0x802A32AC: main.sym_fnc("ObjectMakeParticle", arg=(
		"PARTICLE *part",
	), flag={"GLOBL"}),
	0x802A34A4: main.sym_fnc("ObjSetHitInfo", arg=(
		"OBJECT *obj",
		"HITINFO *hit",
	), flag={"GLOBL"}),
	0x802A3604: main.sym_fnc("GetSign", "int", (
		"int x",
	), flag={"GLOBL"}),
	0x802A3634: main.sym_fnc("fabsf", "float", (
		"float x",
	), flag={"GLOBL"}),
	0x802A3674: main.sym_fnc("abs", "int", (
		"int i",
	), flag={"GLOBL"}),
	0x802A36A4: main.sym_fnc("ObjectFlash", "int", (
		"int start",
		"int count",
	), flag={"GLOBL"}),
	0x802A3754: main.sym_fnc("objectlib_802A3754", "int", flag={"GLOBL"}),
	0x802A37AC: main.sym_fnc("objectlib_802A37AC", flag={"GLOBL"}),
	0x802A37DC: main.sym_fnc("objectlib_802A37DC", arg=(
		"Na_Se se",
	), flag={"GLOBL"}),
	0x802A3818: main.sym_fnc("ObjectRepelMario2D", arg=(
		"float radius",
	), flag={"GLOBL"}),
	0x802A390C: main.sym_fnc("ObjectRepelMario3D", arg=(
		"float radius",
		"float height",
	), flag={"GLOBL"}),
	0x802A399C: main.sym_fnc("objectlib_802A399C", flag={"GLOBL"}), # objcall
	0x802A3A3C: main.sym_fnc("objectlib_802A3A3C"), # unused
	0x802A3A4C: main.sym_fnc("objectlib_802A3A4C", "CHAR", (
		"void *table",
	), flag={"GLOBL"}),
	0x802A3A88: main.sym_fnc("objectlib_802A3A88", "CHAR", flag={"GLOBL"}),
	0x802A3B28: main.sym_fnc("objectlib_802A3B28", arg=(
		"OBJECT *obj",
		"OBJECT *o",
	)), # unused
	0x802A3B40: main.sym_fnc("ObjectScaleTime", arg=(
		"int flag",
		"int time",
		"float min",
		"float max",
	), flag={"GLOBL"}),
	0x802A3C18: main.sym_fnc("ObjectDebugPos", flag={"GLOBL"}),
	0x802A3CEC: main.sym_fnc("objectlib_802A3CEC"), # unused
	0x802A3CFC: main.sym_fnc("ObjectIsMarioRide", "int", flag={"GLOBL"}),
	0x802A3D40: main.sym_fnc("objectlib_802A3D40", "int", (
		"int count",
		"int offy",
	)), # unused
	0x802A3DD4: main.sym_fnc("objectlib_802A3DD4", "int", (
		"int index",
	), flag={"GLOBL"}),
	0x802A3E30: main.sym_fnc("ObjectCallState", arg=(
		"OBJCALL **statetab",
	), flag={"GLOBL"}),
	0x802A3E80: main.sym_fnc("objectlib_802A3E80", "OBJECT *", (
		"int code",
		"int v9",
	)),
	0x802A3EF8: main.sym_fnc("objectlib_802A3EF8"), # unused
	0x802A3F24: main.sym_fnc("GetBit", "int", (
		"int index",
	), flag={"GLOBL"}),
	0x802A3F48: main.sym_fnc("objectlib_802A3F48", "int", flag={"GLOBL"}),
	0x802A404C: main.sym_fnc("objectlib_802A404C", "int", (
		"int speed",
	), flag={"GLOBL"}),
	0x802A40B8: main.sym_fnc("InTable", "int", (
		"CHAR value",
		"s8 *table",
	), flag={"GLOBL"}),
	0x802A4110: main.sym_fnc("objectlib_802A4110"), # unused
	0x802A4120: main.sym_fnc("ObjectInitArea", flag={"GLOBL"}), # objcall
	0x802A4210: main.sym_fnc("ObjectProcArea", flag={"GLOBL"}),
	0x802A4360: main.sym_fnc("objectlib_802A4360", "int", (
		"HITINFO *hit",
		"Na_Se se",
		"int nocoin",
	), flag={"GLOBL"}),
	0x802A4440: main.sym_fnc("objectlib_802A4440", arg=(
		"float a0",
		"int a1",
	), flag={"GLOBL"}),
	0x802A44F4: main.sym_fnc("ObjSetMap", arg=(
		"OBJECT *obj",
		"MAP *map",
	), flag={"GLOBL"}),
	0x802A452C: main.sym_fnc("objectlib_802A452C", flag={"GLOBL"}),
	0x802A4564: main.sym_fnc("objectlib_802A4564", "int", (
		"float height",
	), flag={"GLOBL"}),
	0x802A45E4: main.sym_fnc("Ctrl_objectlib_802A45E4", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL","LOCAL"}), # shpcall
	0x802A462C: main.sym_fnc("Ctrl_objectlib_802A462C", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	)), # unused
	0x802A46CC: main.sym_fnc("ObjIsHide", "int", (
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x802A4704: main.sym_fnc("objectlib_802A4704", flag={"GLOBL"}),
	0x802A4728: main.sym_fnc("objectlib_802A4728", flag={"GLOBL"}),
	0x802A4750: main.sym_fnc("objectlib_802A4750", arg=(
		"unsigned int flag",
	), flag={"GLOBL"}),
	0x802A4774: main.sym_fnc("objectlib_802A4774", arg=(
		"unsigned int flag",
	), flag={"GLOBL"}),
	0x802A47A0: main.sym_fnc("objectlib_802A47A0", "int", (
		"float radius",
		"float height",
		"SHORT range",
	), flag={"GLOBL"}),
	0x802A48BC: main.sym_fnc("objectlib_802A48BC", "int", (
		"float radius",
		"float height",
	), flag={"GLOBL"}),
	0x802A48FC: main.sym_fnc("objectlib_802A48FC", arg=(
		"int flag",
		"int code",
	)),
	0x802A4960: main.sym_fnc("objectlib_802A4960", "int", (
		"int a0",
		"int flag",
		"int msg",
		"int a3",
	), flag={"GLOBL"}),
	0x802A49B4: main.sym_fnc("L802A49B4", flag={"GLOBL","LOCAL"}),
	0x802A4A28: main.sym_fnc("L802A4A28", flag={"GLOBL","LOCAL"}),
	0x802A4A58: main.sym_fnc("L802A4A58", flag={"GLOBL","LOCAL"}),
	0x802A4AAC: main.sym_fnc("L802A4AAC", flag={"GLOBL","LOCAL"}),
	0x802A4B30: main.sym_fnc("L802A4B30", flag={"GLOBL","LOCAL"}),
	0x802A4BE4: main.sym_fnc("objectlib_802A4BE4", "int", (
		"int a0",
		"int flag",
		"int msg",
		"int a3",
	), flag={"GLOBL"}),
	0x802A4F04: main.sym_fnc("ObjectHasShapeID", "int", (
		"USHORT shape",
	), flag={"GLOBL"}),
	0x802A4F58: main.sym_fnc("ObjectStand", flag={"GLOBL"}),
	0x802A5034: main.sym_fnc("MarioInRect", "int", (
		"SHORT xmin",
		"SHORT xmax",
		"SHORT zmin",
		"SHORT zmax",
	)), # unused
	0x802A50FC: main.sym_fnc("objectlib_802A50FC", arg=(
		"int a0",
	), flag={"GLOBL"}),
	0x802A513C: main.sym_fnc("objectlib_802A513C", "int", (
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x802A51AC: main.sym_fnc("objectlib_802A51AC", "int", flag={"GLOBL"}),
	0x802A5228: main.sym_fnc("ObjCopyActorInfo", arg=(
		"OBJECT *obj",
		"OBJECT *o",
	), flag={"GLOBL"}),
	0x802A5248: main.sym_fnc("ObjectSetAnimeFrame", arg=(
		"int anime",
		"int frame",
	), flag={"GLOBL"}),
	0x802A5288: main.sym_fnc("objectlib_802A5288", "int", (
		"int anime",
	), flag={"GLOBL"}),
	0x802A52C4: main.sym_fnc("ObjectSetAnimeHoldEnd", arg=(
		"int anime",
	), flag={"GLOBL"}),
	0x802A52F8: main.sym_fnc("objectlib_802A52F8", "int", flag={"GLOBL"}),
	0x802A5358: main.sym_fnc("objectlib_802A5358", "int", flag={"GLOBL"}),
	0x802A540C: main.sym_fnc("objectlib_802A540C", arg=(
		"int l",
		"int r",
		"Na_Se se",
	)), # unused
	0x802A5460: main.sym_fnc("objectlib_802A5460"), # unused
	0x802A5498: main.sym_fnc("objectlib_802A5498", flag={"GLOBL"}),
	0x802A54D8: main.sym_fnc("objectlib_802A54D8", "int", flag={"GLOBL"}),
	0x802A5524: main.sym_fnc("objectlib_802A5524", flag={"GLOBL"}),
	0x802A5588: main.sym_fnc("objectlib_802A5588", arg=(
		"float x",
		"float y",
		"float z",
		"float offy",
	), flag={"GLOBL"}),

	# src/object_a.c
	0x802A5620: main.sym("object_a_802A5620"),
	0x802A56BC: main.sym("object_a_802A56BC", flag={"GLOBL"}), # objcall
	0x802A5704: main.sym_fnc("L802A5704", flag={"GLOBL","LOCAL"}),
	0x802A5768: main.sym_fnc("L802A5768", flag={"GLOBL","LOCAL"}),
	0x802A57F0: main.sym_fnc("L802A57F0", flag={"GLOBL","LOCAL"}),
	0x802A5824: main.sym_fnc("L802A5824", flag={"GLOBL","LOCAL"}),
	0x802A58A4: main.sym_fnc("L802A58A4", flag={"GLOBL","LOCAL"}),
	0x802A58DC: main.sym("object_a_802A58DC", flag={"GLOBL"}), # objcall
	0x802A597C: main.sym_fnc("object_a_802A597C", flag={"GLOBL"}), # data
	0x802A5A44: main.sym_fnc("object_a_802A5A44", flag={"GLOBL"}), # data
	0x802A5AA0: main.sym("object_a_802A5AA0", flag={"GLOBL"}), # objcall
	0x802A5ACC: main.sym("object_a_802A5ACC"),
	0x802A5BD4: main.sym("object_a_802A5BD4", flag={"GLOBL"}), # objcall
	0x802A5D4C: main.sym_fnc("object_a_802A5D4C", flag={"GLOBL"}), # data
	0x802A6518: main.sym_fnc("object_a_802A6518", flag={"GLOBL"}), # data
	0x802A68A0: main.sym_fnc("object_a_802A68A0", flag={"GLOBL"}), # data
	0x802A6AD8: main.sym_fnc("object_a_802A6AD8", flag={"GLOBL"}), # data
	0x802A6B7C: main.sym("object_a_802A6B7C", flag={"GLOBL"}), # objcall
	0x802A6C20: main.sym("object_a_802A6C20", flag={"GLOBL"}), # objcall
	0x802A6C74: main.sym("object_a_802A6C74", flag={"GLOBL"}), # objcall
	0x802A6CF4: main.sym("object_a_802A6CF4", flag={"GLOBL"}), # objcall
	0x802A6D64: main.sym("object_a_802A6D64", flag={"GLOBL"}), # objcall
	0x802A6EE4: main.sym_fnc("object_a_802A6EE4", flag={"GLOBL"}), # data
	0x802A7020: main.sym_fnc("object_a_802A7020", flag={"GLOBL"}), # data
	0x802A708C: main.sym_fnc("object_a_802A708C", flag={"GLOBL"}), # data
	0x802A7160: main.sym_fnc("object_a_802A7160", flag={"GLOBL"}), # data
	0x802A7170: main.sym("object_a_802A7170", flag={"GLOBL"}), # objcall
	0x802A719C: main.sym("Ctrl_object_a_802A719C", flag={"GLOBL"}), # shpcall
	0x802A7230: main.sym("object_a_802A7230", flag={"GLOBL"}), # objcall
	0x802A7264: main.sym_fnc("object_a_802A7264", flag={"GLOBL"}), # data
	0x802A7384: main.sym("object_a_802A7384"),
	0x802A73D8: main.sym_fnc("object_a_802A73D8", flag={"GLOBL"}), # data
	0x802A7598: main.sym_fnc("object_a_802A7598", flag={"GLOBL"}), # data
	0x802A7804: main.sym_fnc("object_a_802A7804", flag={"GLOBL"}), # data
	0x802A78D8: main.sym_fnc("object_a_802A78D8", flag={"GLOBL"}), # data
	0x802A7A60: main.sym_fnc("object_a_802A7A60", flag={"GLOBL"}), # data
	0x802A7B1C: main.sym_fnc("object_a_802A7B1C", flag={"GLOBL"}), # data
	0x802A7B5C: main.sym_fnc("object_a_802A7B5C", flag={"GLOBL"}), # data
	0x802A7D14: main.sym_fnc("object_a_802A7D14", flag={"GLOBL"}), # data
	0x802A7D4C: main.sym_fnc("L802A7D4C", flag={"GLOBL","LOCAL"}),
	0x802A7E08: main.sym_fnc("L802A7E08", flag={"GLOBL","LOCAL"}),
	0x802A7EDC: main.sym_fnc("L802A7EDC", flag={"GLOBL","LOCAL"}),
	0x802A7F08: main.sym_fnc("L802A7F08", flag={"GLOBL","LOCAL"}),
	0x802A7F70: main.sym_fnc("L802A7F70", flag={"GLOBL","LOCAL"}),
	0x802A7FBC: main.sym("object_a_802A7FBC"),
	0x802A8064: main.sym("object_a_802A8064", flag={"GLOBL"}), # objcall
	0x802A816C: main.sym("object_a_802A816C", flag={"GLOBL"}), # objcall
	0x802A81E8: main.sym("object_a_802A81E8", flag={"GLOBL"}), # objcall
	0x802A821C: main.sym("object_a_802A821C", flag={"GLOBL"}), # objcall
	0x802A8370: main.sym("object_a_802A8370", flag={"GLOBL"}), # objcall
	0x802A83A0: main.sym("object_a_802A83A0", flag={"GLOBL"}), # objcall
	0x802A8630: main.sym("object_a_802A8630", flag={"GLOBL"}), # objcall
	0x802A86BC: main.sym("object_a_802A86BC"), # unused
	0x802A870C: main.sym("object_a_802A870C", flag={"GLOBL"}), # objcall
	0x802A88A4: main.sym("object_a_802A88A4", flag={"GLOBL"}), # objcall
	0x802A8A38: main.sym("object_a_802A8A38"),
	0x802A8B18: main.sym("object_a_802A8B18", flag={"GLOBL"}), # objcall
	0x802A8BC0: main.sym("object_a_802A8BC0", flag={"GLOBL"}), # objcall
	0x802A8C88: main.sym("object_a_802A8C88", flag={"GLOBL"}), # objcall
	0x802A8CDC: main.sym("object_a_802A8CDC", flag={"GLOBL"}), # objcall
	0x802A8D48: main.sym("object_a_802A8D48", flag={"GLOBL"}), # objcall
	0x802A8D98: main.sym("object_a_802A8D98", flag={"GLOBL"}), # objcall
	0x802A8DC0: main.sym_fnc("object_a_802A8DC0", flag={"GLOBL"}), # data
	0x802A8F40: main.sym_fnc("object_a_802A8F40", flag={"GLOBL"}), # data
	0x802A9114: main.sym_fnc("object_a_802A9114", flag={"GLOBL"}), # data
	0x802A92FC: main.sym_fnc("object_a_802A92FC", flag={"GLOBL"}), # data
	0x802A93F8: main.sym_fnc("object_a_802A93F8", flag={"GLOBL"}), # data
	0x802A9440: main.sym_fnc("object_a_802A9440", flag={"GLOBL"}), # data
	0x802A9460: main.sym_fnc("object_a_802A9460", flag={"GLOBL"}), # data
	0x802A9498: main.sym("object_a_802A9498", flag={"GLOBL"}), # objcall
	0x802A94F8: main.sym("object_a_802A94F8", flag={"GLOBL"}), # objcall
	0x802A958C: main.sym("object_a_802A958C"),
	0x802A9708: main.sym("object_a_802A9708", flag={"GLOBL"}), # objcall
	0x802A973C: main.sym("object_a_802A973C"), # unused
	0x802A98C4: main.sym("object_a_802A98C4"),
	0x802A9994: main.sym_fnc("object_a_802A9994", flag={"GLOBL"}), # data
	0x802A9D08: main.sym_fnc("object_a_802A9D08", flag={"GLOBL"}), # data
	0x802A9F54: main.sym_fnc("object_a_802A9F54", flag={"GLOBL"}), # data
	0x802A9FC8: main.sym_fnc("object_a_802A9FC8", flag={"GLOBL"}), # data
	0x802AA02C: main.sym("object_a_802AA02C"),
	0x802AA0AC: main.sym("object_a_802AA0AC", flag={"GLOBL"}), # objcall
	0x802AA1B8: main.sym("object_a_802AA1B8", flag={"GLOBL"}), # objcall
	0x802AA280: main.sym("object_a_802AA280"),
	0x802AA3C8: main.sym("object_a_802AA3C8"),
	0x802AA3F4: main.sym("object_a_802AA3F4", flag={"GLOBL"}), # objcall
	0x802AA700: main.sym("object_a_802AA700", flag={"GLOBL"}), # objcall
	0x802AA774: main.sym("object_a_802AA774", flag={"GLOBL"}), # objcall
	0x802AA830: main.sym("object_a_802AA830", flag={"GLOBL"}), # objcall
	0x802AA948: main.sym("object_a_802AA948"),
	0x802AA97C: main.sym("object_a_802AA97C", flag={"GLOBL"}), # objcall
	0x802AAA60: main.sym("object_a_802AAA60", flag={"GLOBL"}), # objcall
	0x802AAB54: main.sym("object_a_802AAB54", flag={"GLOBL"}), # objcall
	0x802AAC48: main.sym("object_a_802AAC48", flag={"GLOBL"}), # objcall
	0x802AAE8C: main.sym_fnc("object_a_802AAE8C", arg=(
		"int",
		"int",
		"float",
	), flag={"GLOBL"}), # extern / make effect?
	0x802AAF48: main.sym("object_a_802AAF48", flag={"GLOBL"}), # objcall
	0x802AAFFC: main.sym("object_a_802AAFFC"),
	0x802AB060: main.sym("object_a_802AB060"),
	0x802AB158: main.sym("object_a_802AB158"),
	0x802AB18C: main.sym("object_a_802AB18C"),
	0x802AB1C8: main.sym("object_a_802AB1C8", flag={"GLOBL"}), # objcall
	0x802AB558: main.sym_fnc("object_a_802AB558", arg=(
		"int",
	), flag={"GLOBL"}), # extern / make selroom star
	0x802AB5C8: main.sym("object_a_802AB5C8"),
	0x802AB650: main.sym("object_a_802AB650", flag={"GLOBL"}), # objcall
	0x802AB70C: main.sym("object_a_802AB70C", flag={"GLOBL"}), # objcall
	0x802AB748: main.sym("object_a_802AB748", flag={"GLOBL"}), # objcall
	0x802AB7A4: main.sym("object_a_802AB7A4", flag={"GLOBL"}), # objcall
	0x802AB860: main.sym("object_a_802AB860", flag={"GLOBL"}), # objcall
	0x802ABA40: main.sym("object_a_802ABA40", flag={"GLOBL"}), # objcall
	0x802ABC04: main.sym("object_a_802ABC04"),
	0x802ABC70: main.sym_fnc("L802ABC70", flag={"GLOBL","LOCAL"}),
	0x802ABCA8: main.sym_fnc("L802ABCA8", flag={"GLOBL","LOCAL"}),
	0x802ABCF8: main.sym_fnc("L802ABCF8", flag={"GLOBL","LOCAL"}),
	0x802ABD88: main.sym_fnc("L802ABD88", flag={"GLOBL","LOCAL"}),
	0x802ABE20: main.sym_fnc("L802ABE20", flag={"GLOBL","LOCAL"}),
	0x802ABEE4: main.sym("object_a_802ABEE4", flag={"GLOBL"}), # objcall
	0x802ABF0C: main.sym("object_a_802ABF0C", flag={"GLOBL"}), # objcall
	0x802AC068: main.sym_fnc("object_a_802AC068", flag={"GLOBL"}), # data
	0x802AC15C: main.sym_fnc("object_a_802AC15C", flag={"GLOBL"}), # data
	0x802AC294: main.sym("object_a_802AC294", flag={"GLOBL"}), # objcall
	0x802AC2C0: main.sym("object_a_802AC2C0", flag={"GLOBL"}), # objcall
	0x802AC2EC: main.sym("object_a_802AC2EC", flag={"GLOBL"}), # objcall
	0x802AC3A8: main.sym("object_a_802AC3A8", flag={"GLOBL"}), # objcall
	0x802AC4A0: main.sym("object_a_802AC4A0", flag={"GLOBL"}), # objcall
	0x802AC5B4: main.sym("object_a_802AC5B4", flag={"GLOBL"}), # objcall
	0x802AC678: main.sym("object_a_802AC678", flag={"GLOBL"}), # objcall
	0x802AC78C: main.sym("object_a_802AC78C", flag={"GLOBL"}), # objcall
	0x802AC864: main.sym("object_a_802AC864", flag={"GLOBL"}), # objcall
	0x802AC910: main.sym("object_a_802AC910"),
	0x802AC958: main.sym("object_a_802AC958"),
	0x802AC9D0: main.sym("object_a_802AC9D0"),
	0x802ACA6C: main.sym("object_a_802ACA6C"),
	0x802ACAC8: main.sym("object_a_802ACAC8", flag={"GLOBL"}), # objcall
	0x802ACB90: main.sym_fnc("L802ACB90", flag={"GLOBL","LOCAL"}),
	0x802ACBA0: main.sym_fnc("L802ACBA0", flag={"GLOBL","LOCAL"}),
	0x802ACBB8: main.sym_fnc("L802ACBB8", flag={"GLOBL","LOCAL"}),
	0x802ACBD0: main.sym_fnc("L802ACBD0", flag={"GLOBL","LOCAL"}),
	0x802ACBE8: main.sym_fnc("L802ACBE8", flag={"GLOBL","LOCAL"}),
	0x802ACC3C: main.sym("object_a_802ACC3C", flag={"GLOBL"}), # objcall
	0x802ACE80: main.sym("object_a_802ACE80", flag={"GLOBL"}), # objcall
	0x802AD078: main.sym_fnc("object_a_802AD078", flag={"GLOBL"}), # data
	0x802AD10C: main.sym_fnc("object_a_802AD10C", flag={"GLOBL"}), # data
	0x802AD1A4: main.sym_fnc("object_a_802AD1A4", flag={"GLOBL"}), # data
	0x802AD238: main.sym_fnc("object_a_802AD238", flag={"GLOBL"}), # data
	0x802AD2D0: main.sym_fnc("object_a_802AD2D0", flag={"GLOBL"}), # data
	0x802AD34C: main.sym("object_a_802AD34C", flag={"GLOBL"}), # objcall
	0x802AD378: main.sym("object_a_802AD378", flag={"GLOBL"}), # objcall
	0x802AD580: main.sym_fnc("object_a_802AD580", flag={"GLOBL"}), # data
	0x802AD76C: main.sym_fnc("object_a_802AD76C", flag={"GLOBL"}), # data
	0x802AD7F4: main.sym_fnc("object_a_802AD7F4", flag={"GLOBL"}), # data
	0x802AD828: main.sym_fnc("object_a_802AD828", flag={"GLOBL"}), # data
	0x802AD890: main.sym("object_a_802AD890", flag={"GLOBL"}), # objcall
	0x802AD8BC: main.sym("object_a_802AD8BC"),
	0x802AD8F0: main.sym_fnc("object_a_802AD8F0", flag={"GLOBL"}), # data
	0x802ADA4C: main.sym_fnc("object_a_802ADA4C", flag={"GLOBL"}), # data
	0x802ADB88: main.sym_fnc("object_a_802ADB88", flag={"GLOBL"}), # data
	0x802ADCE4: main.sym_fnc("object_a_802ADCE4", flag={"GLOBL"}), # data
	0x802ADD70: main.sym_fnc("object_a_802ADD70", flag={"GLOBL"}), # data
	0x802ADDF8: main.sym("object_a_802ADDF8", flag={"GLOBL"}), # objcall
	0x802ADF6C: main.sym("object_a_802ADF6C", flag={"GLOBL"}), # objcall
	0x802ADF98: main.sym("object_a_802ADF98", flag={"GLOBL"}), # objcall
	0x802ADFD8: main.sym("object_a_802ADFD8", flag={"GLOBL"}), # objcall
	0x802AE0CC: main.sym_fnc("object_a_802AE0CC", arg=(
		"SHORT",
		"SHORT shape",
		"float",
		"SHORT",
	), flag={"GLOBL"}), # extern
	0x802AE238: main.sym("object_a_802AE238", flag={"GLOBL"}), # objcall
	0x802AE304: main.sym("object_a_802AE304", flag={"GLOBL"}), # objcall
	0x802AE334: main.sym("object_a_802AE334", flag={"GLOBL"}), # extern
	0x802AE360: main.sym("object_a_802AE360", flag={"GLOBL"}), # objcall
	0x802AE394: main.sym("object_a_802AE394"), # unused
	0x802AE45C: main.sym("object_a_802AE45C"),
	0x802AE48C: main.sym("object_a_802AE48C", flag={"GLOBL"}), # objcall
	0x802AE4C0: main.sym_fnc("object_a_802AE4C0", arg=(
		"SHORT",
		"SHORT",
	), flag={"GLOBL"}), # extern
	0x802AE534: main.sym("object_a_802AE534", flag={"GLOBL"}), # objcall
	0x802AE85C: main.sym("object_a_802AE85C", flag={"GLOBL"}), # objcall
	0x802AE908: main.sym("object_a_802AE908", flag={"GLOBL"}), # objcall
	0x802AEA6C: main.sym_fnc("object_a_802AEA6C", flag={"GLOBL"}), # data
	0x802AEAB8: main.sym_fnc("object_a_802AEAB8", flag={"GLOBL"}), # data
	0x802AEB1C: main.sym_fnc("object_a_802AEB1C", flag={"GLOBL"}), # data
	0x802AEB74: main.sym_fnc("object_a_802AEB74", flag={"GLOBL"}), # data
	0x802AEB9C: main.sym("object_a_802AEB9C", flag={"GLOBL"}), # objcall
	0x802AEBC8: main.sym("object_a_802AEBC8", flag={"GLOBL"}), # objcall
	0x802AEC40: main.sym("object_a_802AEC40", flag={"GLOBL"}), # objcall
	0x802AECA8: main.sym("object_a_802AECA8", flag={"GLOBL"}), # objcall
	0x802AECDC: main.sym("object_a_802AECDC", flag={"GLOBL"}), # objcall
	0x802AEDC0: main.sym("object_a_802AEDC0", flag={"GLOBL"}), # objcall
	0x802AEE34: main.sym_fnc("L802AEE34", flag={"GLOBL","LOCAL"}),
	0x802AEE68: main.sym_fnc("L802AEE68", flag={"GLOBL","LOCAL"}),
	0x802AEE70: main.sym_fnc("L802AEE70", flag={"GLOBL","LOCAL"}),
	0x802AEEA4: main.sym("object_a_802AEEA4", flag={"GLOBL"}), # objcall
	0x802AEF1C: main.sym("object_a_802AEF1C", flag={"GLOBL"}), # objcall
	0x802AF1E8: main.sym("object_a_802AF1E8", flag={"GLOBL"}), # objcall
	0x802AF3FC: main.sym("object_a_802AF3FC", flag={"GLOBL"}), # objcall
	0x802AF448: main.sym("object_a_802AF448", flag={"GLOBL"}), # objcall
	0x802AF5F8: main.sym("object_a_802AF5F8", flag={"GLOBL"}), # objcall
	0x802AF7C4: main.sym("object_a_802AF7C4", flag={"GLOBL"}), # objcall
	0x802AF9CC: main.sym("object_a_802AF9CC", flag={"GLOBL"}), # objcall
	0x802AFA0C: main.sym("object_a_802AFA0C", flag={"GLOBL"}), # objcall
	0x802AFAE4: main.sym("object_a_802AFAE4", flag={"GLOBL"}), # objcall
	0x802AFBF8: main.sym("object_a_802AFBF8", flag={"GLOBL"}), # objcall
	0x802AFCE4: main.sym("object_a_802AFCE4", flag={"GLOBL"}), # objcall
	0x802AFD1C: main.sym("object_a_802AFD1C", flag={"GLOBL"}), # objcall
	0x802AFEE8: main.sym("object_a_802AFEE8", flag={"GLOBL"}), # objcall
	0x802AFF30: main.sym("object_a_802AFF30", flag={"GLOBL"}), # objcall
	0x802B00E4: main.sym("object_a_802B00E4", flag={"GLOBL"}), # objcall
	0x802B0244: main.sym("object_a_802B0244"),
	0x802B039C: main.sym("object_a_802B039C"),
	0x802B04B4: main.sym("object_a_802B04B4", flag={"GLOBL"}), # objcall
	0x802B0614: main.sym("object_a_802B0614", flag={"GLOBL"}), # objcall
	0x802B0974: main.sym("object_a_802B0974", flag={"GLOBL"}), # objcall
	0x802B0B9C: main.sym("object_a_802B0B9C"),
	0x802B0BEC: main.sym("object_a_802B0BEC", flag={"GLOBL"}), # objcall
	0x802B0C3C: main.sym_fnc("L802B0C3C", flag={"GLOBL","LOCAL"}),
	0x802B0C5C: main.sym_fnc("L802B0C5C", flag={"GLOBL","LOCAL"}),
	0x802B0C8C: main.sym_fnc("L802B0C8C", flag={"GLOBL","LOCAL"}),
	0x802B0CBC: main.sym_fnc("L802B0CBC", flag={"GLOBL","LOCAL"}),
	0x802B0CEC: main.sym_fnc("L802B0CEC", flag={"GLOBL","LOCAL"}),
	0x802B0D48: main.sym("object_a_802B0D48", flag={"GLOBL"}), # objcall
	0x802B0DF0: main.sym("object_a_802B0DF0", flag={"GLOBL"}), # objcall
	0x802B1278: main.sym("object_a_802B1278", flag={"GLOBL"}), # objcall
	0x802B12B0: main.sym_fnc("L802B12B0", flag={"GLOBL","LOCAL"}),
	0x802B1344: main.sym_fnc("L802B1344", flag={"GLOBL","LOCAL"}),
	0x802B13A0: main.sym_fnc("L802B13A0", flag={"GLOBL","LOCAL"}),
	0x802B1470: main.sym_fnc("L802B1470", flag={"GLOBL","LOCAL"}),
	0x802B14B4: main.sym_fnc("L802B14B4", flag={"GLOBL","LOCAL"}),
	0x802B14F4: main.sym("object_a_802B14F4"),
	0x802B15E8: main.sym("object_a_802B15E8", flag={"GLOBL"}), # objcall
	0x802B1714: main.sym("object_a_802B1714"),
	0x802B17F4: main.sym("object_a_802B17F4"),
	0x802B19D8: main.sym("object_a_802B19D8"),
	0x802B1AE0: main.sym("object_a_802B1AE0", flag={"GLOBL"}), # objcall
	0x802B1B2C: main.sym("object_a_802B1B2C", flag={"GLOBL"}), # objcall
	0x802B1BB0: main.sym_fnc("CtrlMarioCopyParentPos", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802B1C54: main.sym("object_a_802B1C54", flag={"GLOBL"}), # objcall
	0x802B1D7C: main.sym_fnc("object_a_802B1D7C", flag={"GLOBL"}), # data
	0x802B1E6C: main.sym_fnc("object_a_802B1E6C", flag={"GLOBL"}), # data
	0x802B1FF4: main.sym_fnc("object_a_802B1FF4", flag={"GLOBL"}), # data
	0x802B20A0: main.sym_fnc("object_a_802B20A0", flag={"GLOBL"}), # data
	0x802B2154: main.sym("object_a_802B2154"),
	0x802B2278: main.sym("object_a_802B2278", flag={"GLOBL"}), # objcall
	0x802B2340: main.sym("object_a_802B2340", flag={"GLOBL"}), # objcall
	0x802B23E0: main.sym("object_a_802B23E0", flag={"GLOBL"}), # objcall
	0x802B2494: main.sym("object_a_802B2494", flag={"GLOBL"}), # objcall
	0x802B25AC: main.sym("object_a_802B25AC", flag={"GLOBL"}), # objcall
	0x802B26A4: main.sym_fnc("object_a_802B26A4", flag={"GLOBL"}), # data
	0x802B27D8: main.sym_fnc("object_a_802B27D8", flag={"GLOBL"}), # data
	0x802B2824: main.sym("object_a_802B2824"),
	0x802B288C: main.sym("object_a_802B288C", flag={"GLOBL"}), # objcall
	0x802B29B8: main.sym("object_a_802B29B8", flag={"GLOBL"}), # objcall
	0x802B2A04: main.sym_fnc("L802B2A04", flag={"GLOBL","LOCAL"}),
	0x802B2A8C: main.sym_fnc("L802B2A8C", flag={"GLOBL","LOCAL"}),
	0x802B2B24: main.sym_fnc("L802B2B24", flag={"GLOBL","LOCAL"}),
	0x802B2B74: main.sym_fnc("L802B2B74", flag={"GLOBL","LOCAL"}),
	0x802B2BA8: main.sym_fnc("L802B2BA8", flag={"GLOBL","LOCAL"}),
	0x802B2BC8: main.sym("object_a_802B2BC8"),
	0x802B2D10: main.sym("object_a_802B2D10", flag={"GLOBL"}), # objcall
	0x802B2DAC: main.sym_fnc("object_a_802B2DAC", flag={"GLOBL"}), # data
	0x802B2F34: main.sym_fnc("object_a_802B2F34", flag={"GLOBL"}), # data
	0x802B3064: main.sym_fnc("object_a_802B3064", flag={"GLOBL"}), # data
	0x802B3108: main.sym("object_a_802B3108", flag={"GLOBL"}), # objcall
	0x802B3134: main.sym("object_a_802B3134"),
	0x802B3250: main.sym("object_a_802B3250"),
	0x802B329C: main.sym("object_a_802B329C", flag={"GLOBL"}), # objcall
	0x802B3600: main.sym("object_a_802B3600", flag={"GLOBL"}), # objcall
	0x802B37B8: main.sym("object_a_802B37B8", flag={"GLOBL"}), # objcall
	0x802B3810: main.sym("object_a_802B3810", flag={"GLOBL"}), # objcall
	0x802B3830: main.sym_fnc("object_a_802B3830", flag={"GLOBL"}), # data
	0x802B38B8: main.sym_fnc("object_a_802B38B8", flag={"GLOBL"}), # data
	0x802B394C: main.sym_fnc("object_a_802B394C", flag={"GLOBL"}), # data
	0x802B3B08: main.sym_fnc("object_a_802B3B08", flag={"GLOBL"}), # data
	0x802B3B24: main.sym_fnc("object_a_802B3B24", flag={"GLOBL"}), # data
	0x802B3BE0: main.sym("object_a_802B3BE0", flag={"GLOBL"}), # objcall
	0x802B3C2C: main.sym_fnc("object_a_802B3C2C", flag={"GLOBL"}), # data
	0x802B3CDC: main.sym_fnc("object_a_802B3CDC", flag={"GLOBL"}), # data
	0x802B3D10: main.sym_fnc("object_a_802B3D10", flag={"GLOBL"}), # data
	0x802B3D74: main.sym("object_a_802B3D74", flag={"GLOBL"}), # objcall
	0x802B3DF4: main.sym("object_a_802B3DF4", flag={"GLOBL"}), # objcall
	0x802B4080: main.sym("object_a_802B4080", flag={"GLOBL"}), # objcall
	0x802B4184: main.sym("object_a_802B4184"),
	0x802B41FC: main.sym("object_a_802B41FC"),
	0x802B4288: main.sym("object_a_802B4288"),
	0x802B4300: main.sym("object_a_802B4300"),
	0x802B4368: main.sym("object_a_802B4368"),
	0x802B43DC: main.sym("object_a_802B43DC"),
	0x802B4478: main.sym_fnc("object_a_802B4478", flag={"GLOBL"}), # data
	0x802B44BC: main.sym_fnc("object_a_802B44BC", flag={"GLOBL"}), # data
	0x802B459C: main.sym("object_a_802B459C"), # unused
	0x802B45F4: main.sym("object_a_802B45F4"),
	0x802B473C: main.sym("object_a_802B473C"),
	0x802B48D4: main.sym("object_a_802B48D4"),
	0x802B4A1C: main.sym("object_a_802B4A1C"),
	0x802B4A3C: main.sym("object_a_802B4A3C"),
	0x802B4AF4: main.sym("object_a_802B4AF4"),
	0x802B4BAC: main.sym_fnc("object_a_802B4BAC", flag={"GLOBL"}), # data
	0x802B4BE8: main.sym_fnc("object_a_802B4BE8", flag={"GLOBL"}), # data
	0x802B4CA4: main.sym_fnc("object_a_802B4CA4", flag={"GLOBL"}), # data
	0x802B4D14: main.sym_fnc("object_a_802B4D14", flag={"GLOBL"}), # data
	0x802B4F00: main.sym_fnc("object_a_802B4F00", flag={"GLOBL"}), # data
	0x802B5104: main.sym_fnc("object_a_802B5104", flag={"GLOBL"}), # data
	0x802B5218: main.sym_fnc("object_a_802B5218", flag={"GLOBL"}), # data
	0x802B53F4: main.sym("object_a_802B53F4"),
	0x802B5444: main.sym("object_a_802B5444"),
	0x802B5554: main.sym("object_a_802B5554"),
	0x802B55CC: main.sym_fnc("object_a_802B55CC", flag={"GLOBL"}), # data
	0x802B5798: main.sym_fnc("object_a_802B5798", flag={"GLOBL"}), # data
	0x802B58BC: main.sym_fnc("object_a_802B58BC", flag={"GLOBL"}), # data
	0x802B59CC: main.sym_fnc("object_a_802B59CC", flag={"GLOBL"}), # data
	0x802B5AEC: main.sym("object_a_802B5AEC"),
	0x802B5C00: main.sym_fnc("object_a_802B5C00", flag={"GLOBL"}), # data
	0x802B5C40: main.sym_fnc("object_a_802B5C40", flag={"GLOBL"}), # data
	0x802B5F6C: main.sym("object_a_802B5F6C"),
	0x802B5FEC: main.sym_fnc("object_a_802B5FEC", flag={"GLOBL"}), # data
	0x802B611C: main.sym("object_a_802B611C"),
	0x802B6190: main.sym_fnc("object_a_802B6190", flag={"GLOBL"}), # data
	0x802B6568: main.sym_fnc("object_a_802B6568", flag={"GLOBL"}), # data
	0x802B65D0: main.sym("object_a_802B65D0"),
	0x802B6670: main.sym("object_a_802B6670"),
	0x802B6730: main.sym("object_a_802B6730"),
	0x802B67D4: main.sym("object_a_802B67D4"),
	0x802B6878: main.sym("object_a_802B6878"),
	0x802B6A10: main.sym("object_a_802B6A10"),
	0x802B6A78: main.sym("object_a_802B6A78"),
	0x802B6BAC: main.sym("object_a_802B6BAC"),
	0x802B6CF0: main.sym_fnc("object_a_802B6CF0", flag={"GLOBL"}), # data
	0x802B6D28: main.sym_fnc("L802B6D28", flag={"GLOBL","LOCAL"}),
	0x802B6D38: main.sym_fnc("L802B6D38", flag={"GLOBL","LOCAL"}),
	0x802B6D48: main.sym_fnc("L802B6D48", flag={"GLOBL","LOCAL"}),
	0x802B6DC0: main.sym_fnc("L802B6DC0", flag={"GLOBL","LOCAL"}),
	0x802B6DEC: main.sym_fnc("L802B6DEC", flag={"GLOBL","LOCAL"}),
	0x802B6DF4: main.sym_fnc("L802B6DF4", flag={"GLOBL","LOCAL"}),
	0x802B6E20: main.sym_fnc("L802B6E20", flag={"GLOBL","LOCAL"}),
	0x802B6E28: main.sym_fnc("L802B6E28", flag={"GLOBL","LOCAL"}),
	0x802B6E40: main.sym("object_a_802B6E40"),
	0x802B6EE0: main.sym_fnc("object_a_802B6EE0", flag={"GLOBL"}), # data
	0x802B711C: main.sym("object_a_802B711C"),
	0x802B71E4: main.sym("object_a_802B71E4"),
	0x802B72D4: main.sym("object_a_802B72D4"),
	0x802B7418: main.sym("object_a_802B7418"),
	0x802B75A4: main.sym("object_a_802B75A4", flag={"GLOBL"}), # objcall
	0x802B7878: main.sym("object_a_802B7878", flag={"GLOBL"}), # objcall
	0x802B798C: main.sym("Ctrl_object_a_802B798C", flag={"GLOBL"}), # shpcall
	0x802B7A20: main.sym("object_a_802B7A20"),
	0x802B7A78: main.sym_fnc("L802B7A78", flag={"GLOBL","LOCAL"}),
	0x802B7AE8: main.sym_fnc("L802B7AE8", flag={"GLOBL","LOCAL"}),
	0x802B7B10: main.sym_fnc("L802B7B10", flag={"GLOBL","LOCAL"}),
	0x802B7B38: main.sym_fnc("L802B7B38", flag={"GLOBL","LOCAL"}),
	0x802B7B5C: main.sym_fnc("L802B7B5C", flag={"GLOBL","LOCAL"}),
	0x802B7B9C: main.sym_fnc("L802B7B9C", flag={"GLOBL","LOCAL"}),
	0x802B7BC0: main.sym_fnc("L802B7BC0", flag={"GLOBL","LOCAL"}),
	0x802B7C00: main.sym_fnc("L802B7C00", flag={"GLOBL","LOCAL"}),
	0x802B7C24: main.sym_fnc("L802B7C24", flag={"GLOBL","LOCAL"}),
	0x802B7C64: main.sym("Ctrl_object_a_802B7C64", flag={"GLOBL"}), # shpcall
	0x802B7D44: main.sym("Ctrl_object_a_802B7D44", flag={"GLOBL"}), # shpcall
	0x802B7E68: main.sym_fnc("object_a_802B7E68", flag={"GLOBL"}), # data
	0x802B7EF0: main.sym_fnc("object_a_802B7EF0", flag={"GLOBL"}), # data
	0x802B8024: main.sym_fnc("object_a_802B8024", flag={"GLOBL"}), # data
	0x802B8384: main.sym("object_a_802B8384", flag={"GLOBL"}), # objcall
	0x802B83B0: main.sym("object_a_802B83B0"),
	0x802B8434: main.sym("object_a_802B8434"),
	0x802B84AC: main.sym("object_a_802B84AC", flag={"GLOBL"}), # objcall
	0x802B85B0: main.sym("object_a_802B85B0", flag={"GLOBL"}), # objcall
	0x802B8654: main.sym("object_a_802B8654"),
	0x802B8734: main.sym("object_a_802B8734", flag={"GLOBL"}), # objcall
	0x802B8960: main.sym("object_a_802B8960", flag={"GLOBL"}), # objcall
	0x802B89EC: main.sym("object_a_802B89EC", flag={"GLOBL"}), # objcall
	0x802B8B1C: main.sym("object_a_802B8B1C", flag={"GLOBL"}), # objcall
	0x802B8C38: main.sym("object_a_802B8C38", flag={"GLOBL"}), # objcall
	0x802B8D68: main.sym("object_a_802B8D68", flag={"GLOBL"}), # objcall
	0x802B8E7C: main.sym("object_a_802B8E7C", flag={"GLOBL"}), # objcall
	0x802B9034: main.sym("object_a_802B9034", flag={"GLOBL"}), # objcall
	0x802B90EC: main.sym("object_a_802B90EC", flag={"GLOBL"}), # objcall
	0x802B921C: main.sym("object_a_802B921C", flag={"GLOBL"}), # objcall
	0x802B935C: main.sym("object_a_802B935C", flag={"GLOBL"}), # objcall
	0x802B9790: main.sym("object_a_802B9790", flag={"GLOBL"}), # objcall
	0x802B98D4: main.sym("object_a_802B98D4"),
	0x802B98FC: main.sym("object_a_802B98FC", flag={"GLOBL"}), # objcall
	0x802B9A78: main.sym("object_a_802B9A78"),
	0x802B9AF8: main.sym("object_a_802B9AF8"),
	0x802B9BB4: main.sym("object_a_802B9BB4", flag={"GLOBL"}), # objcall
	0x802B9BD8: main.sym("object_a_802B9BD8", flag={"GLOBL"}), # objcall
	0x802B9C60: main.sym_fnc("L802B9C60", flag={"GLOBL","LOCAL"}),
	0x802B9CA0: main.sym_fnc("L802B9CA0", flag={"GLOBL","LOCAL"}),
	0x802B9CC0: main.sym_fnc("L802B9CC0", flag={"GLOBL","LOCAL"}),
	0x802B9CD4: main.sym_fnc("L802B9CD4", flag={"GLOBL","LOCAL"}),
	0x802B9CF4: main.sym_fnc("L802B9CF4", flag={"GLOBL","LOCAL"}),
	0x802B9E94: main.sym("object_a_802B9E94", flag={"GLOBL"}), # objcall
	0x802B9EFC: main.sym("object_a_802B9EFC"),
	0x802B9F34: main.sym_fnc("L802B9F34", flag={"GLOBL","LOCAL"}),
	0x802B9F68: main.sym_fnc("L802B9F68", flag={"GLOBL","LOCAL"}),
	0x802B9FBC: main.sym_fnc("L802B9FBC", flag={"GLOBL","LOCAL"}),
	0x802BA008: main.sym_fnc("L802BA008", flag={"GLOBL","LOCAL"}),
	0x802BA064: main.sym_fnc("L802BA064", flag={"GLOBL","LOCAL"}),
	0x802BA11C: main.sym_fnc("L802BA11C", flag={"GLOBL","LOCAL"}),
	0x802BA13C: main.sym("object_a_802BA13C"),
	0x802BA19C: main.sym("object_a_802BA19C", flag={"GLOBL"}), # objcall
	0x802BA1E0: main.sym("object_a_802BA1E0", flag={"GLOBL"}), # objcall
	0x802BA25C: main.sym("object_a_802BA25C", flag={"GLOBL"}), # objcall
	0x802BA2B0: main.sym("Ctrl_object_a_802BA2B0", flag={"GLOBL"}), # shpcall
	0x802BA2F8: main.sym("object_a_802BA2F8", flag={"GLOBL"}), # objcall
	0x802BA458: main.sym("object_a_802BA458", flag={"GLOBL"}), # objcall
	0x802BA5BC: main.sym("object_a_802BA5BC", flag={"GLOBL"}), # objcall
	0x802BA608: main.sym("object_a_802BA608", flag={"GLOBL"}), # objcall
	0x802BA7E0: main.sym("object_a_802BA7E0"),
	0x802BA868: main.sym("object_a_802BA868"),
	0x802BA8C4: main.sym("object_a_802BA8C4"), # unused
	0x802BA958: main.sym("object_a_802BA958"),
	0x802BAB7C: main.sym_fnc("object_a_802BAB7C", flag={"GLOBL"}), # data
	0x802BAE40: main.sym_fnc("object_a_802BAE40", flag={"GLOBL"}), # data
	0x802BAEC4: main.sym_fnc("object_a_802BAEC4", flag={"GLOBL"}), # data
	0x802BAF10: main.sym_fnc("object_a_802BAF10", flag={"GLOBL"}), # data
	0x802BAF64: main.sym_fnc("object_a_802BAF64", flag={"GLOBL"}), # data
	0x802BB07C: main.sym_fnc("object_a_802BB07C", flag={"GLOBL"}), # data
	0x802BB288: main.sym_fnc("object_a_802BB288", flag={"GLOBL"}), # data
	0x802BB3B8: main.sym_fnc("object_a_802BB3B8", flag={"GLOBL"}), # data
	0x802BB468: main.sym_fnc("L802BB468", flag={"GLOBL","LOCAL"}),
	0x802BB508: main.sym_fnc("L802BB508", flag={"GLOBL","LOCAL"}),
	0x802BB564: main.sym_fnc("L802BB564", flag={"GLOBL","LOCAL"}),
	0x802BB5A4: main.sym_fnc("L802BB5A4", flag={"GLOBL","LOCAL"}),
	0x802BB5F4: main.sym_fnc("L802BB5F4", flag={"GLOBL","LOCAL"}),
	0x802BB638: main.sym_fnc("L802BB638", flag={"GLOBL","LOCAL"}),
	0x802BB6E0: main.sym_fnc("L802BB6E0", flag={"GLOBL","LOCAL"}),
	0x802BB748: main.sym_fnc("L802BB748", flag={"GLOBL","LOCAL"}),
	0x802BB798: main.sym("object_a_802BB798"),
	0x802BB838: main.sym("object_a_802BB838"), # unused
	0x802BB888: main.sym("object_a_802BB888"),
	0x802BBA3C: main.sym("object_a_802BBA3C"),
	0x802BBA74: main.sym_fnc("L802BBA74", flag={"GLOBL","LOCAL"}),
	0x802BBAB4: main.sym_fnc("L802BBAB4", flag={"GLOBL","LOCAL"}),
	0x802BBAFC: main.sym_fnc("L802BBAFC", flag={"GLOBL","LOCAL"}),
	0x802BBB04: main.sym_fnc("L802BBB04", flag={"GLOBL","LOCAL"}),
	0x802BBB60: main.sym_fnc("L802BBB60", flag={"GLOBL","LOCAL"}),
	0x802BBB80: main.sym_fnc("L802BBB80", flag={"GLOBL","LOCAL"}),
	0x802BBB98: main.sym("object_a_802BBB98", flag={"GLOBL"}), # objcall
	0x802BBC0C: main.sym("object_a_802BBC0C", flag={"GLOBL"}), # objcall
	0x802BBD6C: main.sym("object_a_802BBD6C"),
	0x802BBFD8: main.sym("object_a_802BBFD8"),
	0x802BC0F0: main.sym("object_a_802BC0F0", flag={"GLOBL"}), # objcall
	0x802BC22C: main.sym("object_a_802BC22C", flag={"GLOBL"}), # objcall
	0x802BC294: main.sym("object_a_802BC294", flag={"GLOBL"}), # objcall
	0x802BC348: main.sym("object_a_802BC348"),
	0x802BC4F4: main.sym_fnc("object_a_802BC4F4", flag={"GLOBL"}), # data
	0x802BC538: main.sym_fnc("object_a_802BC538", flag={"GLOBL"}), # data
	0x802BC590: main.sym_fnc("object_a_802BC590", flag={"GLOBL"}), # data
	0x802BC5FC: main.sym_fnc("object_a_802BC5FC", flag={"GLOBL"}), # data
	0x802BC618: main.sym("object_a_802BC618", flag={"GLOBL"}), # objcall
	0x802BC660: main.sym("object_a_802BC660", flag={"GLOBL"}), # objcall
	0x802BC728: main.sym("object_a_802BC728", flag={"GLOBL"}), # objcall
	0x802BC898: main.sym("object_a_802BC898", flag={"GLOBL"}), # objcall
	0x802BC934: main.sym("object_a_802BC934"),
	0x802BCA74: main.sym("object_a_802BCA74", flag={"GLOBL"}), # objcall
	0x802BCADC: main.sym_fnc("L802BCADC", flag={"GLOBL","LOCAL"}),
	0x802BCB24: main.sym_fnc("L802BCB24", flag={"GLOBL","LOCAL"}),
	0x802BCBA4: main.sym_fnc("L802BCBA4", flag={"GLOBL","LOCAL"}),
	0x802BCC1C: main.sym_fnc("L802BCC1C", flag={"GLOBL","LOCAL"}),
	0x802BCC90: main.sym_fnc("L802BCC90", flag={"GLOBL","LOCAL"}),
	0x802BCCE8: main.sym("object_a_802BCCE8"),
	0x802BCDA8: main.sym("object_a_802BCDA8", flag={"GLOBL"}), # objcall
	0x802BCE58: main.sym("object_a_802BCE58", flag={"GLOBL"}), # objcall
	0x802BCE9C: main.sym("object_a_802BCE9C"),
	0x802BCF40: main.sym("object_a_802BCF40", flag={"GLOBL"}), # objcall
	0x802BCFC4: main.sym("object_a_802BCFC4"),
	0x802BD058: main.sym("object_a_802BD058", flag={"GLOBL"}), # objcall
	0x802BD3E4: main.sym("object_a_802BD3E4"),
	0x802BD488: main.sym("object_a_802BD488", flag={"GLOBL"}), # objcall
	0x802BD5DC: main.sym("object_a_802BD5DC"),
	0x802BD62C: main.sym("object_a_802BD62C"),
	0x802BD680: main.sym("object_a_802BD680", flag={"GLOBL"}), # objcall
	0x802BD8D0: main.sym("object_a_802BD8D0"),
	0x802BD91C: main.sym("object_a_802BD91C"),
	0x802BDB04: main.sym_fnc("object_a_802BDB04", flag={"GLOBL"}), # data
	0x802BDB3C: main.sym_fnc("object_a_802BDB3C", flag={"GLOBL"}), # data
	0x802BDB74: main.sym_fnc("object_a_802BDB74", flag={"GLOBL"}), # data
	0x802BDBAC: main.sym_fnc("object_a_802BDBAC", flag={"GLOBL"}), # data
	0x802BDBE4: main.sym_fnc("object_a_802BDBE4", flag={"GLOBL"}), # data
	0x802BDC7C: main.sym_fnc("object_a_802BDC7C", flag={"GLOBL"}), # data
	0x802BDCC8: main.sym_fnc("object_a_802BDCC8", flag={"GLOBL"}), # data
	0x802BDD14: main.sym_fnc("object_a_802BDD14", flag={"GLOBL"}), # data
	0x802BDD68: main.sym("object_a_802BDD68", flag={"GLOBL"}), # objcall
	0x802BDD9C: main.sym_fnc("object_a_802BDD9C", flag={"GLOBL"}), # data
	0x802BDE10: main.sym("object_a_802BDE10"),
	0x802BDEEC: main.sym_fnc("object_a_802BDEEC", flag={"GLOBL"}), # data
	0x802BE034: main.sym_fnc("object_a_802BE034", flag={"GLOBL"}), # data
	0x802BE0B8: main.sym("object_a_802BE0B8"),
	0x802BE0EC: main.sym_fnc("object_a_802BE0EC", flag={"GLOBL"}), # data
	0x802BE150: main.sym_fnc("object_a_802BE150", flag={"GLOBL"}), # data
	0x802BE234: main.sym_fnc("object_a_802BE234", flag={"GLOBL"}), # data
	0x802BE278: main.sym_fnc("object_a_802BE278", flag={"GLOBL"}), # data
	0x802BE350: main.sym_fnc("object_a_802BE350", flag={"GLOBL"}), # data
	0x802BE49C: main.sym("object_a_802BE49C"),
	0x802BE50C: main.sym_fnc("object_a_802BE50C", flag={"GLOBL"}), # data
	0x802BE5A0: main.sym("object_a_802BE5A0", flag={"GLOBL"}), # objcall
	0x802BE628: main.sym("object_a_802BE628"),
	0x802BE6D4: main.sym("object_a_802BE6D4"),
	0x802BE79C: main.sym("object_a_802BE79C", flag={"GLOBL"}), # objcall
	0x802BE8A8: main.sym_fnc("object_a_802BE8A8", flag={"GLOBL"}), # data
	0x802BE8B8: main.sym_fnc("object_a_802BE8B8", flag={"GLOBL"}), # data
	0x802BE8F4: main.sym("object_a_802BE8F4"),
	0x802BE9DC: main.sym("object_a_802BE9DC"),
	0x802BEB14: main.sym_fnc("object_a_802BEB14", flag={"GLOBL"}), # data
	0x802BEB54: main.sym_fnc("object_a_802BEB54", flag={"GLOBL"}), # data
	0x802BEB8C: main.sym_fnc("object_a_802BEB8C", flag={"GLOBL"}), # data
	0x802BEBC4: main.sym_fnc("object_a_802BEBC4", flag={"GLOBL"}), # data
	0x802BEBFC: main.sym_fnc("object_a_802BEBFC", flag={"GLOBL"}), # data
	0x802BEC34: main.sym("object_a_802BEC34", flag={"GLOBL"}), # objcall
	0x802BECB0: main.sym("object_a_802BECB0"),
	0x802BED7C: main.sym("object_a_802BED7C", flag={"GLOBL"}), # extern
	0x802BEDEC: main.sym_fnc("object_a_802BEDEC", flag={"GLOBL"}), # data
	0x802BEF8C: main.sym_fnc("object_a_802BEF8C", flag={"GLOBL"}), # data
	0x802BF1D8: main.sym_fnc("object_a_802BF1D8", flag={"GLOBL"}), # data
	0x802BF3C0: main.sym("object_a_802BF3C0", flag={"GLOBL"}), # objcall
	0x802BF424: main.sym("object_a_802BF424"),
	0x802BF474: main.sym_fnc("object_a_802BF474", flag={"GLOBL"}), # data
	0x802BF57C: main.sym_fnc("object_a_802BF57C", flag={"GLOBL"}), # data
	0x802BF648: main.sym_fnc("object_a_802BF648", flag={"GLOBL"}), # data
	0x802BF6E4: main.sym_fnc("object_a_802BF6E4", flag={"GLOBL"}), # data
	0x802BF760: main.sym_fnc("object_a_802BF760", flag={"GLOBL"}), # data
	0x802BF90C: main.sym_fnc("object_a_802BF90C", flag={"GLOBL"}), # data
	0x802BFA14: main.sym("object_a_802BFA14"),
	0x802BFA88: main.sym("object_a_802BFA88", flag={"GLOBL"}), # objcall
	0x802BFBAC: main.sym("Ctrl_object_a_802BFBAC", flag={"GLOBL"}), # shpcall
	0x802BFCD8: main.sym_fnc("object_a_802BFCD8", flag={"GLOBL"}), # data
	0x802BFEB8: main.sym_fnc("object_a_802BFEB8", flag={"GLOBL"}), # data
	0x802BFF20: main.sym_fnc("object_a_802BFF20", flag={"GLOBL"}), # data
	0x802BFF3C: main.sym("object_a_802BFF3C", flag={"GLOBL"}), # objcall
	0x802BFF68: main.sym("object_a_802BFF68"),
	0x802C00B4: main.sym_fnc("object_a_802C00B4", flag={"GLOBL"}), # data
	0x802C0348: main.sym_fnc("object_a_802C0348", flag={"GLOBL"}), # data
	0x802C06A8: main.sym_fnc("object_a_802C06A8", flag={"GLOBL"}), # data
	0x802C0768: main.sym("object_a_802C0768", flag={"GLOBL"}), # objcall
	0x802C08A8: main.sym("object_a_802C08A8", flag={"GLOBL"}), # objcall
	0x802C0AAC: main.sym_fnc("object_a_802C0AAC", flag={"GLOBL"}), # data
	0x802C0B50: main.sym_fnc("object_a_802C0B50", flag={"GLOBL"}), # data
	0x802C0BA4: main.sym_fnc("object_a_802C0BA4", flag={"GLOBL"}), # data
	0x802C0BC4: main.sym_fnc("object_a_802C0BC4", flag={"GLOBL"}), # data
	0x802C0BE0: main.sym("object_a_802C0BE0", flag={"GLOBL"}), # objcall
	0x802C0C0C: main.sym("object_a_802C0C0C"),
	0x802C0CD4: main.sym_fnc("object_a_802C0CD4", flag={"GLOBL"}), # data
	0x802C0D44: main.sym_fnc("object_a_802C0D44", flag={"GLOBL"}), # data
	0x802C0F90: main.sym_fnc("object_a_802C0F90", flag={"GLOBL"}), # data
	0x802C1204: main.sym("object_a_802C1204", flag={"GLOBL"}), # objcall
	0x802C12C0: main.sym("object_a_802C12C0", flag={"GLOBL"}), # objcall
	0x802C1308: main.sym_fnc("object_a_802C1308", flag={"GLOBL"}), # data
	0x802C13EC: main.sym_fnc("object_a_802C13EC", flag={"GLOBL"}), # data
	0x802C14B0: main.sym_fnc("object_a_802C14B0", flag={"GLOBL"}), # data
	0x802C15B8: main.sym_fnc("object_a_802C15B8", flag={"GLOBL"}), # data
	0x802C17BC: main.sym("object_a_802C17BC"),
	0x802C18D0: main.sym_fnc("object_a_802C18D0", flag={"GLOBL"}), # data
	0x802C1988: main.sym_fnc("object_a_802C1988", flag={"GLOBL"}), # data
	0x802C19C0: main.sym("object_a_802C19C0", flag={"GLOBL"}), # objcall
	0x802C19FC: main.sym("object_a_802C19FC", flag={"GLOBL"}), # objcall
	0x802C1A40: main.sym("object_a_802C1A40", flag={"GLOBL"}), # objcall
	0x802C1A80: main.sym("object_a_802C1A80", flag={"GLOBL"}), # objcall
	0x802C1A90: main.sym("object_a_802C1A90", flag={"GLOBL"}), # objcall
	0x802C1C44: main.sym("object_a_802C1C44", flag={"GLOBL"}), # objcall
	0x802C1CD4: main.sym("object_a_802C1CD4", flag={"GLOBL"}), # objcall
	0x802C1E10: main.sym("object_a_802C1E10", flag={"GLOBL"}), # objcall
	0x802C2190: main.sym("object_a_802C2190", flag={"GLOBL"}), # objcall
	0x802C2274: main.sym("object_a_802C2274", flag={"GLOBL"}), # objcall
	0x802C22B8: main.sym("object_a_802C22B8", flag={"GLOBL"}), # objcall
	0x802C242C: main.sym("object_a_802C242C", flag={"GLOBL"}), # objcall
	0x802C263C: main.sym("object_a_802C263C", flag={"GLOBL"}), # objcall
	0x802C26F8: main.sym("object_a_802C26F8", flag={"GLOBL"}), # objcall
	0x802C2930: main.sym("object_a_802C2930", flag={"GLOBL"}), # objcall
	0x802C2A24: main.sym("object_a_802C2A24", flag={"GLOBL"}), # objcall
	0x802C2CE8: main.sym("object_a_802C2CE8"),
	0x802C2EBC: main.sym_fnc("object_a_802C2EBC", flag={"GLOBL"}), # data
	0x802C2FBC: main.sym_fnc("object_a_802C2FBC", flag={"GLOBL"}), # data
	0x802C31C4: main.sym_fnc("object_a_802C31C4", flag={"GLOBL"}), # data
	0x802C329C: main.sym("object_a_802C329C", flag={"GLOBL"}), # objcall
	0x802C32E8: main.sym("object_a_802C32E8", flag={"GLOBL"}), # objcall
	0x802C33F4: main.sym("object_a_802C33F4"),
	0x802C3440: main.sym("object_a_802C3440", flag={"GLOBL"}), # objcall
	0x802C3460: main.sym("object_a_802C3460"),
	0x802C3534: main.sym("object_a_802C3534"),
	0x802C3684: main.sym("object_a_802C3684", flag={"GLOBL"}), # objcall
	0x802C3748: main.sym("object_a_802C3748"),
	0x802C3884: main.sym("object_a_802C3884"),
	0x802C39D4: main.sym("object_a_802C39D4"),
	0x802C3B08: main.sym("object_a_802C3B08"),
	0x802C3C04: main.sym("object_a_802C3C04"),
	0x802C3CD0: main.sym("object_a_802C3CD0"),
	0x802C3D50: main.sym("object_a_802C3D50"),
	0x802C3D9C: main.sym("object_a_802C3D9C"),
	0x802C3E80: main.sym("object_a_802C3E80"),
	0x802C3F8C: main.sym("object_a_802C3F8C"),
	0x802C4118: main.sym("object_a_802C4118"),
	0x802C4158: main.sym("object_a_802C4158"),
	0x802C4210: main.sym("object_a_802C4210"),
	0x802C43F4: main.sym_fnc("object_a_802C43F4", flag={"GLOBL"}), # data
	0x802C4508: main.sym_fnc("object_a_802C4508", flag={"GLOBL"}), # data
	0x802C45B0: main.sym_fnc("object_a_802C45B0", flag={"GLOBL"}), # data
	0x802C46D8: main.sym_fnc("object_a_802C46D8", flag={"GLOBL"}), # data
	0x802C4720: main.sym_fnc("object_a_802C4720", flag={"GLOBL"}), # data
	0x802C4790: main.sym_fnc("object_a_802C4790", flag={"GLOBL"}), # data
	0x802C4824: main.sym("object_a_802C4824", flag={"GLOBL"}), # objcall
	0x802C48C0: main.sym_fnc("object_a_802C48C0", flag={"GLOBL"}), # data
	0x802C49F0: main.sym_fnc("object_a_802C49F0", flag={"GLOBL"}), # data
	0x802C4B54: main.sym_fnc("object_a_802C4B54", flag={"GLOBL"}), # data
	0x802C4B9C: main.sym("object_a_802C4B9C"),
	0x802C4BD4: main.sym("object_a_802C4BD4"),
	0x802C4C10: main.sym("object_a_802C4C10"),
	0x802C4C70: main.sym_fnc("object_a_802C4C70", flag={"GLOBL"}), # data
	0x802C4DD4: main.sym_fnc("object_a_802C4DD4", flag={"GLOBL"}), # data
	0x802C4F30: main.sym("object_a_802C4F30", flag={"GLOBL"}), # objcall
	0x802C4FB0: main.sym_fnc("object_a_802C4FB0", flag={"GLOBL"}), # data
	0x802C503C: main.sym_fnc("object_a_802C503C", flag={"GLOBL"}), # data
	0x802C50D8: main.sym_fnc("object_a_802C50D8", flag={"GLOBL"}), # data
	0x802C5120: main.sym_fnc("object_a_802C5120", flag={"GLOBL"}), # data
	0x802C515C: main.sym("object_a_802C515C", flag={"GLOBL"}), # objcall
	0x802C51D4: main.sym("object_a_802C51D4", flag={"GLOBL"}), # objcall
	0x802C5224: main.sym("object_a_802C5224", flag={"GLOBL"}), # objcall
	0x802C53CC: main.sym("object_a_802C53CC"),
	0x802C53EC: main.sym("object_a_802C53EC", flag={"GLOBL"}), # objcall
	0x802C5414: main.sym("object_a_802C5414", flag={"GLOBL"}), # objcall
	0x802C5688: main.sym("object_a_802C5688", flag={"GLOBL"}), # objcall
	0x802C5890: main.sym("object_a_802C5890", flag={"GLOBL"}), # objcall
	0x802C5A38: main.sym("object_a_802C5A38", flag={"GLOBL"}), # objcall
	0x802C5B54: main.sym("object_a_802C5B54"),
	0x802C5CA8: main.sym("object_a_802C5CA8", flag={"GLOBL"}), # objcall
	0x802C5DC0: main.sym("object_a_802C5DC0", flag={"GLOBL"}), # objcall
	0x802C5F48: main.sym("object_a_802C5F48", flag={"GLOBL"}), # objcall
	0x802C5FDC: main.sym("object_a_802C5FDC", flag={"GLOBL"}), # objcall
	0x802C6050: main.sym("object_a_802C6050", flag={"GLOBL"}), # objcall
	0x802C60AC: main.sym("object_a_802C60AC", flag={"GLOBL"}), # objcall
	0x802C6150: main.sym("object_a_802C6150"),
	0x802C61D4: main.sym("object_a_802C61D4"),
	0x802C6278: main.sym("object_a_802C6278"),
	0x802C62BC: main.sym("object_a_802C62BC"),
	0x802C6328: main.sym("object_a_802C6328"),
	0x802C6348: main.sym("object_a_802C6348", flag={"GLOBL"}), # objcall
	0x802C6380: main.sym_fnc("L802C6380", flag={"GLOBL","LOCAL"}),
	0x802C6390: main.sym_fnc("L802C6390", flag={"GLOBL","LOCAL"}),
	0x802C63A0: main.sym_fnc("L802C63A0", flag={"GLOBL","LOCAL"}),
	0x802C63B0: main.sym_fnc("L802C63B0", flag={"GLOBL","LOCAL"}),
	0x802C63C0: main.sym_fnc("L802C63C0", flag={"GLOBL","LOCAL"}),
	0x802C63E8: main.sym("object_a_802C63E8", flag={"GLOBL"}), # objcall
	0x802C64A4: main.sym("object_a_802C64A4", flag={"GLOBL"}), # objcall
	0x802C6538: main.sym("object_a_802C6538"),
	0x802C65C0: main.sym("object_a_802C65C0", flag={"GLOBL"}), # objcall
	0x802C6668: main.sym_fnc("L802C6668", flag={"GLOBL","LOCAL"}),
	0x802C66F0: main.sym_fnc("L802C66F0", flag={"GLOBL","LOCAL"}),
	0x802C688C: main.sym_fnc("L802C688C", flag={"GLOBL","LOCAL"}),
	0x802C6920: main.sym_fnc("L802C6920", flag={"GLOBL","LOCAL"}),
	0x802C6990: main.sym_fnc("L802C6990", flag={"GLOBL","LOCAL"}),
	0x802C6A1C: main.sym_fnc("L802C6A1C", flag={"GLOBL","LOCAL"}),
	0x802C6B6C: main.sym("object_a_802C6B6C", flag={"GLOBL"}), # objcall
	0x802C6CA0: main.sym("object_a_802C6CA0"),
	0x802C6D6C: main.sym_fnc("object_a_802C6D6C", flag={"GLOBL"}), # data
	0x802C6EC8: main.sym_fnc("object_a_802C6EC8", flag={"GLOBL"}), # data
	0x802C6FB0: main.sym_fnc("object_a_802C6FB0", flag={"GLOBL"}), # data
	0x802C710C: main.sym_fnc("object_a_802C710C", flag={"GLOBL"}), # data
	0x802C7254: main.sym_fnc("object_a_802C7254", flag={"GLOBL"}), # data
	0x802C72B4: main.sym_fnc("object_a_802C72B4", flag={"GLOBL"}), # data
	0x802C7380: main.sym_fnc("object_a_802C7380", flag={"GLOBL"}), # data
	0x802C7428: main.sym("object_a_802C7428"),
	0x802C75FC: main.sym("object_a_802C75FC"),
	0x802C76D4: main.sym_fnc("object_a_802C76D4", flag={"GLOBL"}), # data
	0x802C7858: main.sym_fnc("object_a_802C7858", flag={"GLOBL"}), # data
	0x802C7998: main.sym_fnc("object_a_802C7998", flag={"GLOBL"}), # data
	0x802C79D8: main.sym("object_a_802C79D8", flag={"GLOBL"}), # objcall
	0x802C7A70: main.sym("object_a_802C7A70", flag={"GLOBL"}), # objcall
	0x802C7B14: main.sym("object_a_802C7B14", flag={"GLOBL"}), # objcall
	0x802C7CAC: main.sym("object_a_802C7CAC", flag={"GLOBL"}), # objcall
	0x802C7D40: main.sym("object_a_802C7D40", flag={"GLOBL"}), # objcall
	0x802C7D90: main.sym("object_a_802C7D90", flag={"GLOBL"}), # objcall
	0x802C7DFC: main.sym("object_a_802C7DFC", flag={"GLOBL"}), # objcall
	0x802C7E5C: main.sym("object_a_802C7E5C", flag={"GLOBL"}), # objcall
	0x802C7F98: main.sym("object_a_802C7F98", flag={"GLOBL"}), # objcall
	0x802C81B4: main.sym("object_a_802C81B4", flag={"GLOBL"}), # extern
	0x802C834C: main.sym("object_a_802C834C", flag={"GLOBL"}), # objcall
	0x802C85A4: main.sym("object_a_802C85A4"),
	0x802C863C: main.sym("object_a_802C863C", flag={"GLOBL"}), # objcall

	# src/ride.c
	0x802C89F0: main.sym_fnc("PLRideFind", flag={"GLOBL"}),
	0x802C8B4C: main.sym_fnc("MarioGetPos", arg=(
		"float *x",
		"float *y",
		"float *z",
	), flag={"GLOBL"}),
	0x802C8B8C: main.sym_fnc("MarioSetPos", arg=(
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}),
	0x802C8BC8: main.sym_fnc("RideProc", arg=(
		"int ismario",
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x802C8EC0: main.sym_fnc("PLRideProc", flag={"GLOBL"}),
	0x802C8F28: main.sym_fnc("PLRideClear", flag={"GLOBL"}),

	# src/hitcheck.c
	0x802C8F40: main.sym_fnc("ObjDebugHit", "OBJECT *", (
		"OBJECT *obj",
	)), # unused
	0x802C8FE4: main.sym_fnc("ObjCheckHit", "int", (
		"OBJECT *a",
		"OBJECT *b",
	)),
	0x802C91EC: main.sym_fnc("ObjCheckDmg", "int", (
		"OBJECT *a",
		"OBJECT *b",
	)),
	0x802C9388: main.sym_fnc("HitClear", arg=(
		"OBJLIST *root",
	)),
	0x802C93F8: main.sym_fnc("HitCheckList", arg=(
		"OBJECT *obj",
		"OBJECT *o",
		"OBJLIST *root",
	)),
	0x802C94AC: main.sym_fnc("HitCheckPlayer"),
	0x802C95B4: main.sym_fnc("HitCheckEnemyB"),
	0x802C9630: main.sym_fnc("HitCheckAttack"),
	0x802C9724: main.sym_fnc("HitCheck", flag={"GLOBL"}),

	# src/objlist.c
	0x802C97D0: main.sym_fnc("ListInit", arg=(
		"LIST *root",
		"LIST *free",
		"LIST *data",
		"size_t size",
		"int count",
	)), # unused
	0x802C9840: main.sym_fnc("ListAlloc", "LIST *", (
		"LIST *root",
		"LIST *free",
	)), # unused
	0x802C98A4: main.sym_fnc("ObjListAlloc", "OBJECT *", (
		"OBJLIST *root",
		"OBJLIST *free",
	)),
	0x802C9950: main.sym_fnc("ListFree", arg=(
		"LIST *free",
		"LIST *item",
	)), # unused
	0x802C9984: main.sym_fnc("ObjListFree", arg=(
		"OBJLIST *free",
		"OBJECT *obj",
	)),
	0x802C99B8: main.sym_fnc("ObjFreeListInit", flag={"GLOBL"}),
	0x802C9A3C: main.sym_fnc("ObjRootListInit", arg=(
		"OBJLIST *root",
	), flag={"GLOBL"}),
	0x802C9AD8: main.sym_fnc("objlist_802C9AD8", arg=(
		"SHAPE *shape",
	)), # unused
	0x802C9B68: main.sym_fnc("ObjFree", arg=(
		"OBJECT *obj",
	), flag={"GLOBL"}),
	0x802C9C00: main.sym_fnc("ObjAlloc", "OBJECT *", (
		"OBJLIST *root",
	)),
	0x802C9E5C: main.sym_fnc("ObjInitGround", arg=(
		"OBJECT *obj",
	)),
	0x802C9F04: main.sym_fnc("ObjCreate", "OBJECT *", (
		"OBJLANG *script",
	), flag={"GLOBL"}),
	0x802CA028: main.sym_fnc("ObjDestroy", arg=(
		"OBJECT *obj",
	), flag={"GLOBL"}),

	# src/objsound.c
	0x802CA040: main.sym_fnc("ObjectStepSound", arg=(
		"STEPSOUND *ss",
	), flag={"GLOBL"}),
	0x802CA144: main.sym_fnc("ObjectMakeSound", arg=(
		"Na_Se se",
	), flag={"GLOBL"}),
	0x802CA190: main.sym_fnc("ObjectLevelSound", arg=(
		"Na_Se se",
	), flag={"GLOBL"}),
	0x802CA1E0: main.sym_fnc("ObjectPlaySound", arg=(
		"Na_Se se",
	), flag={"GLOBL"}),
	0x802CA230: main.sym_fnc("CalcSeVol1", "int", (
		"float x",
	)), # unused
	0x802CA2D4: main.sym_fnc("CalcSeVol2", "int", (
		"float x",
	)), # unused

	0x802CA370: main.sym_fnc("_802CA370"), # unused
	0x802CA380: main.sym_fnc("_802CA380"), # unused
	0x802CA390: main.sym_fnc("_802CA390"), # unused
	0x802CA3A0: main.sym_fnc("_802CA3A0"), # unused

	# src/debug.c
	0x802CA3B0: main.sym_fnc("DbTimeStart", "OSTime", flag={"GLOBL"}),
	0x802CA3E0: main.sym_fnc("DbTimeCount", "OSTime", (
		"OSTime start",
	), flag={"GLOBL"}),
	0x802CA418: main.sym_fnc("DbPrintInit", arg=(
		"DBPRINT *dp",
		"SHORT x",
		"SHORT y",
		"SHORT min_y",
		"SHORT max_y",
		"SHORT height",
	)),
	0x802CA460: main.sym_fnc("DbPrintEntry", arg=(
		"DBPRINT *dp",
		"const char *fmt",
		"int value",
	)),
	0x802CA51C: main.sym_fnc("DbPrintOffset", arg=(
		"int off_x",
		"int off_ln",
	), flag={"GLOBL"}),
	0x802CA568: main.sym_fnc("DbPrintErr", arg=(
		"const char *fmt",
		"int value",
	), flag={"GLOBL"}),
	0x802CA5B8: main.sym_fnc("DbPrint", arg=(
		"const char *fmt",
		"int value",
	), flag={"GLOBL"}),
	0x802CA618: main.sym_fnc("DbPrintInfo", arg=(
		"const char *fmt",
		"int value",
	), flag={"GLOBL"}),
	0x802CA680: main.sym_fnc("DbPrintTitle", arg=(
		"const char *fmt",
		"int value",
	), flag={"GLOBL"}), # static
	0x802CA6D0: main.sym_fnc("DbPlayerMapInfo"),
	0x802CA8E8: main.sym_fnc("DbPlayerCheckInfo"),
	0x802CA918: main.sym_fnc("DbResultCheckInfo"),
	0x802CA94C: main.sym_fnc("DbPlayerStageInfo"),
	0x802CA990: main.sym_fnc("DbPrintEdit", arg=(
		"const char *fmt[]",
	)),
	0x802CAA6C: main.sym_fnc("DbResultEffectInfo"),
	0x802CAAA8: main.sym_fnc("DbResultEnemyInfo"),
	0x802CAAE4: main.sym_fnc("DbProcButton"),
	0x802CABAC: main.sym_fnc("DebugInit", flag={"GLOBL"}),
	0x802CAC20: main.sym_fnc("DebugClear", flag={"GLOBL"}),
	0x802CACC8: main.sym_fnc("DebugProcSeq"), # unused
	0x802CADC8: main.sym_fnc("DebugProcPage"), # unused
	0x802CAE9C: main.sym_fnc("DebugProcEdit"), # unused
	0x802CB0B0: main.sym_fnc("DebugExec", flag={"GLOBL"}),
	0x802CB0C0: main.sym_fnc("DebugResult", flag={"GLOBL"}),
	0x802CB1C0: main.sym_fnc("DebugPlayer", flag={"GLOBL"}), # objcall
	0x802CB264: main.sym_fnc("DebugProc", flag={"GLOBL"}), # objcall
	0x802CB394: main.sym_fnc("DebugPrintMoveStatus"), # unused
	0x802CB564: main.sym_fnc("DebugSetHit", arg=(
		"HITINFO *hit",
	)), # unused

	# src/wipe.c
	0x802CB5C0: main.sym_fnc("WpStep", "int", (
		"CHAR screen",
		"UCHAR frame",
	)),
	0x802CB640: main.sym_fnc("WpFadeAlpha", "UCHAR", (
		"CHAR code",
		"CHAR screen",
		"UCHAR frame",
	)),
	0x802CB894: main.sym_fnc("WpFadeVtx", "Vtx *", (
		"WIPE_FADE *fade",
		"UCHAR alpha",
	)),
	0x802CBA18: main.sym_fnc("WpFadeGfx", "int", (
		"CHAR screen",
		"UCHAR frame",
		"WIPE_FADE *fade",
		"UCHAR alpha",
	)),
	0x802CBBC4: main.sym_fnc("WpFadeIn", "int", (
		"CHAR screen",
		"UCHAR frame",
		"WIPE_FADE *fade",
	)),
	0x802CBC20: main.sym_fnc("WpFadeOut", "int", (
		"CHAR screen",
		"UCHAR frame",
		"WIPE_FADE *fade",
	)),
	0x802CBC7C: main.sym_fnc("WpWindowSize", "SHORT", (
		"CHAR screen",
		"UCHAR frame",
		"WIPE_WINDOW *win",
	)),
	0x802CBD54: main.sym_fnc("WpWindowDist", "float", (
		"CHAR screen",
		"UCHAR frame",
		"WIPE_WINDOW *win",
	)),
	0x802CBE64: main.sym_fnc("WpWindowAng", "u16", (
		"WIPE_WINDOW *win",
	)),
	0x802CBEE0: main.sym_fnc("WpWindowX", "SHORT", (
		"WIPE_WINDOW *win",
		"float dist",
		"USHORT ang",
	)),
	0x802CBF64: main.sym_fnc("WpWindowY", "SHORT", (
		"WIPE_WINDOW *win",
		"float dist",
		"USHORT ang",
	)),
	0x802CBFE8: main.sym_fnc("WpWindowVtxSet", arg=(
		"Vtx *vtx",
		"int i",
		"CHAR screen",
		"WIPE_WINDOW *win",
		"SHORT x",
		"SHORT y",
		"SHORT dx",
		"SHORT dy",
		"SHORT s",
		"SHORT t",
	)),
	0x802CC180: main.sym_fnc("WpWindowVtx", arg=(
		"Vtx *vtx",
		"CHAR screen",
		"WIPE_WINDOW *win",
		"SHORT x",
		"SHORT y",
		"SHORT size",
		"CHAR code",
	)),
	0x802CC4D8: main.sym_fnc("WpWindow", "int", (
		"CHAR screen",
		"CHAR frame",
		"WIPE_WINDOW *win",
		"CHAR txt",
		"CHAR code",
	)),
	0x802CCBE8: main.sym_fnc("WipeDraw", "int", (
		"CHAR screen",
		"CHAR type",
		"UCHAR frame",
		"WIPE_DATA *data",
	), flag={"GLOBL"}),
	0x802CCC28: main.sym_fnc("L802CCC28", flag={"GLOBL","LOCAL"}),
	0x802CCC48: main.sym_fnc("L802CCC48", flag={"GLOBL","LOCAL"}),
	0x802CCC68: main.sym_fnc("L802CCC68", flag={"GLOBL","LOCAL"}),
	0x802CCC90: main.sym_fnc("L802CCC90", flag={"GLOBL","LOCAL"}),
	0x802CCCB8: main.sym_fnc("L802CCCB8", flag={"GLOBL","LOCAL"}),
	0x802CCCE0: main.sym_fnc("L802CCCE0", flag={"GLOBL","LOCAL"}),
	0x802CCD08: main.sym_fnc("L802CCD08", flag={"GLOBL","LOCAL"}),
	0x802CCD34: main.sym_fnc("L802CCD34", flag={"GLOBL","LOCAL"}),
	0x802CCD60: main.sym_fnc("L802CCD60", flag={"GLOBL","LOCAL"}),
	0x802CCD88: main.sym_fnc("L802CCD88", flag={"GLOBL","LOCAL"}),
	0x802CCDB0: main.sym_fnc("L802CCDB0", flag={"GLOBL","LOCAL"}),
	0x802CCDC8: main.sym_fnc("CannonOverlayGfx", "Gfx *"),
	0x802CD1E8: main.sym_fnc("CtrlCannonOverlay", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall

	# src/shadow.c
	0x802CD280: main.sym_fnc("ShRotate", arg=(
		"float *posz",
		"float *posx",
		"float z",
		"float x",
	)),
	0x802CD328: main.sym_fnc("ShAtan2", "float", (
		"float y",
		"float x",
	)),
	0x802CD388: main.sym_fnc("ShScaleSize", "float", (
		"float size",
		"float height",
	)),
	0x802CD444: main.sym_fnc("ShCutSize", "float", (
		"float size",
		"float height",
	)),
	0x802CD48C: main.sym_fnc("ShScaleAlpha", "UCHAR", (
		"UCHAR alpha",
		"float height",
	)),
	0x802CD614: main.sym_fnc("ShCheckWater", "float", (
		"SHADOW *shadow",
	)),
	0x802CD6C4: main.sym_fnc("ShInit", "int", (
		"SHADOW *shadow",
		"float x",
		"float y",
		"float z",
		"SHORT size",
		"UCHAR alpha",
	)),
	0x802CD938: main.sym_fnc("ShVtxST9", arg=(
		"CHAR i",
		"short *s",
		"short *t",
	)),
	0x802CD988: main.sym_fnc("ShVtxST4", arg=(
		"CHAR i",
		"short *s",
		"short *t",
	)),
	0x802CD9EC: main.sym_fnc("ShSetVtx", arg=(
		"Vtx *vtx",
		"CHAR i",
		"float vx",
		"float vy",
		"float vz",
		"UCHAR alpha",
		"CHAR vcode",
	)),
	0x802CDB20: main.sym_fnc("ShProject", "float", (
		"SHADOW shadow",
		"float x",
		"float z",
	)),
	0x802CDB74: main.sym_fnc("ShCalcVtxOff", arg=(
		"CHAR i",
		"CHAR vcode",
		"s8 *x",
		"s8 *z",
	)),
	0x802CDC40: main.sym_fnc("ShCalcVtxPos", arg=(
		"CHAR i",
		"SHADOW shadow",
		"float *x",
		"float *y",
		"float *z",
		"CHAR vcode",
	)),
	0x802CDE94: main.sym_fnc("ShPlaneCalc", "SHORT", (
		"SHADOW shadow",
		"float x",
		"float y",
		"float z",
	)),
	0x802CDF3C: main.sym_fnc("ShCalcVtx", arg=(
		"Vtx *vtx",
		"CHAR i",
		"SHADOW shadow",
		"CHAR vcode",
	)),
	0x802CE128: main.sym_fnc("ShGfx", arg=(
		"Gfx *gfx",
		"Vtx *vtx",
		"CHAR vcode",
		"CHAR tcode",
	)),
	0x802CE2BC: main.sym_fnc("ShFadeIn", arg=(
		"SHADOW *shadow",
		"UCHAR alpha",
		"SHORT frame",
		"SHORT min",
		"SHORT max",
	)),
	0x802CE3EC: main.sym_fnc("ShFadeOut", arg=(
		"SHADOW *shadow",
		"UCHAR alpha",
		"SHORT frame",
		"SHORT min",
		"SHORT max",
	)),
	0x802CE524: main.sym_fnc("ShFadePlayer", "int", (
		"int code",
		"UCHAR alpha",
		"SHADOW *shadow",
	)),
	0x802CE690: main.sym_fnc("ShCheckPlayer", arg=(
		"SHADOW *shadow",
	)),
	0x802CE79C: main.sym_fnc("ShDrawPlayer", "Gfx *", (
		"float x",
		"float y",
		"float z",
		"SHORT size",
		"UCHAR alpha",
		"int code",
	)),
	0x802CE9D0: main.sym_fnc("ShDrawCircle9", "Gfx *", (
		"float x",
		"float y",
		"float z",
		"SHORT size",
		"UCHAR alpha",
	)),
	0x802CEAE8: main.sym_fnc("ShDrawCircle4", "Gfx *", (
		"float x",
		"float y",
		"float z",
		"SHORT size",
		"UCHAR alpha",
	)),
	0x802CEC04: main.sym_fnc("ShDrawCircle4Flat", "Gfx *", (
		"float x",
		"float y",
		"float z",
		"SHORT size",
		"UCHAR alpha",
	)),
	0x802CEDC0: main.sym_fnc("ShGfxSquare", "Gfx *", (
		"float x",
		"float z",
		"float y",
		"UCHAR alpha",
	)),
	0x802CEF6C: main.sym_fnc("ShInitSquare", "int", (
		"float x",
		"float y",
		"float z",
		"float *level",
		"u8 *alpha",
	)),
	0x802CF080: main.sym_fnc("ShDrawSquare", "Gfx *", (
		"float x",
		"float y",
		"float z",
		"SHORT size",
		"u8 alpha",
		"CHAR type",
	)),
	0x802CF1F0: main.sym_fnc("ShDrawRect", "Gfx *", (
		"float x",
		"float y",
		"float z",
		"SHORT size",
		"u8 alpha",
		"CHAR type",
	)),
	0x802CF34C: main.sym_fnc("ShadowDraw", "Gfx *", (
		"float x",
		"float y",
		"float z",
		"SHORT size",
		"UCHAR alpha",
		"CHAR type",
	), flag={"GLOBL"}),
	0x802CF41C: main.sym_fnc("L802CF41C", flag={"GLOBL","LOCAL"}),
	0x802CF444: main.sym_fnc("L802CF444", flag={"GLOBL","LOCAL"}),
	0x802CF46C: main.sym_fnc("L802CF46C", flag={"GLOBL","LOCAL"}),
	0x802CF494: main.sym_fnc("L802CF494", flag={"GLOBL","LOCAL"}),
	0x802CF4C4: main.sym_fnc("L802CF4C4", flag={"GLOBL","LOCAL"}),
	0x802CF4F4: main.sym_fnc("L802CF4F4", flag={"GLOBL","LOCAL"}),
	0x802CF550: main.sym_fnc("L802CF550", flag={"GLOBL","LOCAL"}),

	# src/background.c
	0x802CF5B0: main.sym_fnc("BackPosX", "int", (
		"CHAR screen",
		"float fovy",
	)),
	0x802CF69C: main.sym_fnc("BackPosY", "int", (
		"CHAR screen",
		"float fovy",
	)),
	0x802CF77C: main.sym_fnc("BackIndex", "int", (
		"CHAR screen",
	)),
	0x802CF804: main.sym_fnc("BackVtx", "Vtx *", (
		"int index",
		"CHAR shade",
	)),
	0x802CFA2C: main.sym_fnc("BackTile", arg=(
		"Gfx **g",
		"CHAR type",
		"CHAR screen",
		"CHAR shade",
	)),
	0x802CFC68: main.sym_fnc("BackMtx", "Mtx *", (
		"CHAR screen",
	)),
	0x802CFD88: main.sym_fnc("BackGfx", "Gfx *", (
		"CHAR screen",
		"CHAR type",
		"CHAR shade",
	)),
	0x802CFEF4: main.sym_fnc("BackgroundDraw", "Gfx *", (
		"CHAR screen",
		"CHAR type",
		"float fovy",
		"float eye_x",
		"float eye_y",
		"float eye_z",
		"float look_x",
		"float look_y",
		"float look_z",
	), flag={"GLOBL"}),

	# src/water.c
	0x802D0080: main.sym_fnc("CtrlPoolLevel", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802D01E0: main.sym_fnc("CtrlWaterProc", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802D0254: main.sym_fnc("WaterSetVtx", arg=(
		"Vtx *vtx",
		"int i",
		"SHORT x",
		"SHORT y",
		"SHORT z",
		"SHORT ang",
		"SHORT off",
		"float scale",
		"UCHAR alpha",
	)),
	0x802D0484: main.sym_fnc("WaterDrawPlane", "Gfx *", (
		"SHORT y",
		"short *plane",
	)),
	0x802D0A84: main.sym_fnc("WaterDraw", "Gfx *", (
		"SHORT y",
		"short *data",
	)),
	0x802D0BB0: main.sym_fnc("WaterGfx", "Gfx *", (
		"SHORT code",
		"SHORT y",
		"WATERINFO *info",
	)),
	0x802D0C84: main.sym_fnc("WaterGetInfo", "WATERINFO *", (
		"unsigned int code",
	)),
	0x802D0F28: main.sym_fnc("WaterGfxStart", arg=(
		"unsigned int code",
		"Gfx **g",
	)),
	0x802D104C: main.sym_fnc("CtrlWaterDraw", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802D1330: main.sym_fnc("FluidProc", arg=(
		"short *data",
		"int i",
	)),
	0x802D13CC: main.sym_fnc("FluidSetVtx0", arg=(
		"Vtx *vtx",
		"short *data",
		"FLUIDINFO *info",
		"CHAR type",
	)),
	0x802D1574: main.sym_fnc("FluidSetVtxN", arg=(
		"Vtx *vtx",
		"int i",
		"short *data",
		"FLUIDINFO *info",
		"CHAR type",
	)),
	0x802D18B4: main.sym_fnc("FluidGfx", "Gfx *", (
		"short *data",
		"FLUIDINFO *info",
		"CHAR type",
	)),
	0x802D1B70: main.sym_fnc("CtrlFluid", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802D1CDC: main.sym_fnc("CtrlFluidL", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802D1E48: main.sym_fnc("CtrlFluidDrawL", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802D1FA8: main.sym_fnc("CtrlFluidDrawS", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802D2108: main.sym_fnc("CtrlFluidProc", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall

	# src/objshape.c
	0x802D2210: main.sym_fnc("VtxSet", arg=(
		"Vtx *vtx",
		"int i",
		"SHORT x",
		"SHORT y",
		"SHORT z",
		"SHORT s",
		"SHORT t",
		"UCHAR r",
		"UCHAR g",
		"UCHAR b",
		"UCHAR a",
	), flag={"GLOBL"}),
	0x802D22C4: main.sym_fnc("RoundFtoS", "SHORT", (
		"float x",
	), flag={"GLOBL"}),
	0x802D2360: main.sym_fnc("Ctrl_objshape_802D2360", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802D2470: main.sym_fnc("Ctrl_objshape_802D2470", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802D2520: main.sym_fnc("Ctrl_objshape_802D2520", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802D28CC: main.sym_fnc("EndingDraw", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall

	# src/wave.c
	0x802D29C0: main.sym_fnc("WaveStopAll", arg=(
		"WAVE *wave",
		"WAVE **table",
	)),
	0x802D2A74: main.sym_fnc("WaveYPosY", "float", (
		"WAVE *wave",
	)),
	0x802D2B08: main.sym_fnc("WaveYPosZ", "float", (
		"WAVE *wave",
	)),
	0x802D2B84: main.sym_fnc("WaveGetCenterY", "float", (
		"WAVE *wave",
		"CHAR code",
	)),
	0x802D2C40: main.sym_fnc("WaveXStep", "float", (
		"WAVE *wave",
	)),
	0x802D2D80: main.sym_fnc("WaveXPosX", "float", (
		"WAVE *wave",
	)),
	0x802D2DFC: main.sym_fnc("WaveGetCenterX", "float", (
		"WAVE *wave",
		"CHAR code",
	)),
	0x802D2EB8: main.sym_fnc("WaveStart", arg=(
		"CHAR state",
		"WAVE *wave",
		"WAVE **table",
		"CHAR xcode",
		"CHAR ycode",
		"CHAR tcode",
	)),
	0x802D2FFC: main.sym_fnc("WaveProcV10Still", arg=(
		"WAVE *wave",
		"WAVE **table",
	)),
	0x802D319C: main.sym_fnc("WaveProcV10Touch", arg=(
		"WAVE *wave",
		"WAVE **table",
	)),
	0x802D327C: main.sym_fnc("WaveProcV20Still", arg=(
		"WAVE *wave",
		"WAVE **table",
	)),
	0x802D341C: main.sym_fnc("WaveProcV20Touch", arg=(
		"WAVE *wave",
		"WAVE **table",
	)),
	0x802D34FC: main.sym_fnc("WaveProcH10Still", arg=(
		"WAVE *wave",
		"WAVE **table",
	)),
	0x802D36AC: main.sym_fnc("WaveProcH10Touch", arg=(
		"WAVE *wave",
		"WAVE **table",
	)),
	0x802D379C: main.sym_fnc("WaveProcH20Still", arg=(
		"WAVE *wave",
		"WAVE **table",
	)),
	0x802D393C: main.sym_fnc("WaveProcH20Touch", arg=(
		"WAVE *wave",
		"WAVE **table",
	)),
	0x802D3A2C: main.sym_fnc("WaveProcFlag", arg=(
		"WAVE *wave",
	)),
	0x802D3BEC: main.sym_fnc("WaveProcMove", arg=(
		"WAVE *wave",
	)),
	0x802D3CEC: main.sym_fnc("WaveCalcZ", "SHORT", (
		"WAVE *wave",
		"float x",
		"float y",
	)),
	0x802D3E6C: main.sym_fnc("WaveGetZ", "SHORT", (
		"WAVE *wave",
		"SHORT flag",
		"SHORT x",
		"SHORT y",
	)),
	0x802D3EE4: main.sym_fnc("WaveMakeVtx", arg=(
		"WAVE *wave",
		"short *mesh",
		"SHORT nvtx",
	)),
	0x802D404C: main.sym_fnc("WaveMakeTri", arg=(
		"short *mesh",
		"SHORT nvtx",
		"SHORT ntri",
	)),
	0x802D43F8: main.sym_fnc("WaveScaleNormal", "CHAR", (
		"float x",
	)),
	0x802D44BC: main.sym_fnc("WaveCalcNormal", arg=(
		"short *norm",
		"SHORT nvtx",
	)),
	0x802D47D0: main.sym_fnc("WaveDrawMesh", "Gfx *", (
		"u16 *txt",
		"SHORT wd",
		"SHORT ht",
		"short *mesh",
		"SHORT nvtx",
		"SHORT ntri",
		"UCHAR alpha",
	)),
	0x802D4EDC: main.sym_fnc("WaveTransform", "Gfx *", (
		"WAVE *wave",
	)),
	0x802D50DC: main.sym_fnc("WaveGfxShade", "Gfx *", (
		"WAVE *wave",
	)),
	0x802D5354: main.sym_fnc("WaveGfxEnvMap", "Gfx *", (
		"WAVE *wave",
	)),
	0x802D556C: main.sym_fnc("WaveGfxMove", "Gfx *", (
		"WAVE *wave",
	)),
	0x802D568C: main.sym_fnc("WaveGfxStat", "Gfx *", (
		"WAVE *wave",
	)),
	0x802D5778: main.sym_fnc("WaveExit", arg=(
		"WAVE *wave",
	)),
	0x802D57A8: main.sym_fnc("WaveMoveDemo", arg=(
		"WAVE *wave",
		"float start",
		"float end",
		"float speed",
	)),
	0x802D58E4: main.sym_fnc("WaveSetLayer", arg=(
		"SCALLBACK *shp",
		"WAVE *wave",
	)),
	0x802D593C: main.sym_fnc("WaveGfx", "Gfx *", (
		"WAVE *wave",
	)),
	0x802D59A8: main.sym_fnc("WaveProcV", arg=(
		"WAVE *wave",
		"WAVE **table",
	)),
	0x802D5AA0: main.sym_fnc("WaveProcH", arg=(
		"WAVE *wave",
		"WAVE **table",
	)),
	0x802D5B98: main.sym_fnc("CtrlWaveDraw", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall
	0x802D5D0C: main.sym_fnc("CtrlWaveProc", "void *", (
		"int code",
		"SHAPE *shape",
		"void *data",
	), flag={"GLOBL"}), # shpcall

	# src/dprint.c
	0x802D5E00: main.sym_fnc("Powi", "unsigned int", (
		"int base",
		"int exponent",
	)),
	0x802D5E54: main.sym_fnc("dprintFormat", arg=(
		"int value",
		"int base",
		"char *buf",
		"int *index",
		"UCHAR digit",
		"CHAR zero",
	)),
	0x802D6144: main.sym_fnc("dprintGetFmt", arg=(
		"const char *fmt",
		"int *index",
		"u8 *digit",
		"char *zero",
	)),
	0x802D62D8: main.sym_fnc("dprintf", arg=(
		"int x",
		"int y",
		"const char *fmt",
		"int value",
	), flag={"GLOBL"}),
	0x802D6554: main.sym_fnc("dprint", arg=(
		"int x",
		"int y",
		"const char *str",
	), flag={"GLOBL"}),
	0x802D66C0: main.sym_fnc("dprintc", arg=(
		"int x",
		"int y",
		"const char *str",
	), flag={"GLOBL"}),
	0x802D6858: main.sym_fnc("dprintCvt", "CHAR", (
		"CHAR c",
	)),
	0x802D69F8: main.sym_fnc("dprintDrawTxt", arg=(
		"CHAR c",
	)),
	0x802D6ACC: main.sym_fnc("dprintClamp", arg=(
		"int *x",
		"int *y",
	)),
	0x802D6B3C: main.sym_fnc("dprintDrawChar", arg=(
		"int x",
		"int y",
		"int n",
	)),
	0x802D6C88: main.sym_fnc("dprintDraw", flag={"GLOBL"}),

	# src/message.c
	0x802D6F20: main.sym_fnc("GfxLoadIdent"),
	0x802D7070: main.sym_fnc("GfxTranslate", arg=(
		"CHAR flag",
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}),
	0x802D7174: main.sym_fnc("GfxRotate", arg=(
		"CHAR flag",
		"float a",
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}), # static
	0x802D7280: main.sym_fnc("GfxScale", arg=(
		"CHAR flag",
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}), # static
	0x802D7384: main.sym_fnc("GfxScreenProj", flag={"GLOBL"}),
	0x802D7480: main.sym_fnc("UnpackI1", "u8 *", (
		"u16 *src",
		"SHORT w",
		"SHORT h",
	)), # unused
	0x802D75DC: main.sym_fnc("PrintLgChar", arg=(
		"UCHAR c",
	)),
	0x802D76C8: main.sym_fnc("PrintLgMulti", arg=(
		"CHAR code",
	)),
	0x802D77DC: main.sym_fnc("PrintLg", arg=(
		"SHORT x",
		"SHORT y",
		"const unsigned char *str",
	), flag={"GLOBL"}),
	0x802D7B84: main.sym_fnc("Print16", arg=(
		"CHAR font",
		"SHORT x",
		"SHORT y",
		"const unsigned char *str",
	), flag={"GLOBL"}),
	0x802D7E88: main.sym_fnc("PrintSm", arg=(
		"SHORT x",
		"SHORT y",
		"const unsigned char *str",
	), flag={"GLOBL"}),
	0x802D82D4: main.sym_fnc("Print8", arg=(
		"SHORT x",
		"SHORT y",
		"const unsigned char *str",
	), flag={"GLOBL"}), # static
	0x802D862C: main.sym_fnc("CursorProc", arg=(
		"CHAR code",
		"s8 *cursor",
		"CHAR min",
		"CHAR max",
	), flag={"GLOBL"}),
	0x802D8844: main.sym_fnc("StrCenterX", "SHORT", (
		"SHORT x",
		"const unsigned char *str",
		"float kerning",
	), flag={"GLOBL"}),
	0x802D8934: main.sym_fnc("StrWidth", "SHORT", (
		"const unsigned char *str",
	), flag={"GLOBL"}), # static
	0x802D89B8: main.sym_fnc("PrintCoin", arg=(
		"int code",
		"CHAR file",
		"CHAR course",
		"SHORT x",
		"SHORT y",
	), flag={"GLOBL"}),
	0x802D8A80: main.sym_fnc("PrintStar", arg=(
		"CHAR file",
		"CHAR course",
		"SHORT x",
		"SHORT y",
	), flag={"GLOBL"}), # static
	0x802D8B34: main.sym_fnc("itostr", arg=(
		"int value",
		"unsigned char *str",
	), flag={"GLOBL"}),
	0x802D8C6C: main.sym_fnc("MsgGet", "SHORT", flag={"GLOBL"}),
	0x802D8C88: main.sym_fnc("MsgOpen", arg=(
		"SHORT code",
	), flag={"GLOBL"}),
	0x802D8CC4: main.sym_fnc("MsgOpenInt", arg=(
		"SHORT code",
		"int value",
	), flag={"GLOBL"}),
	0x802D8D08: main.sym_fnc("MsgOpenSignpost", arg=(
		"SHORT code",
	), flag={"GLOBL"}),
	0x802D8D48: main.sym_fnc("MsgOpenPrompt", arg=(
		"SHORT code",
	), flag={"GLOBL"}),
	0x802D8D90: main.sym_fnc("MsgClose", flag={"GLOBL"}),
	0x802D8E2C: main.sym_fnc("MsgDrawBack", arg=(
		"MESSAGE *msg",
		"CHAR line",
	)),
	0x802D9148: main.sym_fnc("MsgSetColor", arg=(
		"CHAR code",
		"CHAR line",
	)),
	0x802D9388: main.sym_fnc("MsgNewline", arg=(
		"CHAR line",
		"CHAR end",
		"char *state",
		"char *space",
		"short *count",
	)),
	0x802D944C: main.sym_fnc("MsgFmtInt", arg=(
		"char *space",
		"short *count",
	)),
	0x802D9634: main.sym_fnc("MsgMulti", arg=(
		"CHAR code",
		"CHAR line",
		"short *count",
		"CHAR page",
		"CHAR space",
		"CHAR start",
	)),
	0x802D9800: main.sym_fnc("MsgClamp", "unsigned int", (
		"SHORT x",
	)),
	0x802D982C: main.sym_fnc("MsgDraw", arg=(
		"CHAR code",
		"MESSAGE *msg",
		"CHAR start",
	)),
	0x802D99D4: main.sym_fnc("L802D99D4", flag={"GLOBL","LOCAL"}),
	0x802D9A10: main.sym_fnc("L802D9A10", flag={"GLOBL","LOCAL"}),
	0x802D9A40: main.sym_fnc("L802D9A40", flag={"GLOBL","LOCAL"}),
	0x802D9A50: main.sym_fnc("L802D9A50", flag={"GLOBL","LOCAL"}),
	0x802D9A80: main.sym_fnc("L802D9A80", flag={"GLOBL","LOCAL"}),
	0x802D9AA0: main.sym_fnc("L802D9AA0", flag={"GLOBL","LOCAL"}),
	0x802D9AD4: main.sym_fnc("L802D9AD4", flag={"GLOBL","LOCAL"}),
	0x802D9B08: main.sym_fnc("L802D9B08", flag={"GLOBL","LOCAL"}),
	0x802D9B1C: main.sym_fnc("L802D9B1C", flag={"GLOBL","LOCAL"}),
	0x802D9CB0: main.sym_fnc("MsgDrawCursor"),
	0x802D9DFC: main.sym_fnc("MsgDrawNextPage", arg=(
		"CHAR line",
	)),
	0x802D9F84: main.sym_fnc("MsgProcEndSound", arg=(
		"SHORT msg",
	)),
	0x802DA1AC: main.sym_fnc("MsgProc"),
	0x802DA810: main.sym_fnc("MenuOpen", arg=(
		"SHORT code",
	), flag={"GLOBL"}),
	0x802DA844: main.sym_fnc("StaffClear", flag={"GLOBL"}),
	0x802DA85C: main.sym_fnc("StaffDrawStart", flag={"GLOBL"}),
	0x802DA8E4: main.sym_fnc("StaffDrawEnd", flag={"GLOBL"}),
	0x802DA964: main.sym_fnc("StaffCvt", "UCHAR", (
		"UCHAR c",
	)),
	0x802DAA34: main.sym_fnc("StaffPrint", arg=(
		"SHORT x",
		"SHORT y",
		"const char *str",
	), flag={"GLOBL"}),
	0x802DAAE4: main.sym_fnc("CaptionOpen", arg=(
		"SHORT x",
		"SHORT y",
		"SHORT code",
		"SHORT frame",
	), flag={"GLOBL"}),
	0x802DAB58: main.sym_fnc("CaptionDraw", flag={"GLOBL"}),
	0x802DAD54: main.sym_fnc("OpeningDraw"),
	0x802DB08C: main.sym_fnc("DrawCannonReticle", flag={"GLOBL"}),
	0x802DB350: main.sym_fnc("PauseMenu_Init", flag={"GLOBL"}),
	0x802DB368: main.sym_fnc("PauseMenu_InitCourse"),
	0x802DB3B8: main.sym_fnc("MenuDrawBack"),
	0x802DB498: main.sym_fnc("PauseMenu_PutRedCoin", arg=(
		"SHORT x",
		"SHORT y",
	)),
	0x802DB6E8: main.sym_fnc("PauseMenu_DrawRedCoin"),
	0x802DB760: main.sym_fnc("PauseMenu_DrawCourse"),
	0x802DBB24: main.sym_fnc("PauseMenu_ProcCamera", arg=(
		"SHORT x",
		"SHORT y",
		"s8 *cursor",
		"SHORT space",
	)),
	0x802DBE68: main.sym_fnc("PauseMenu_ProcCourse", arg=(
		"SHORT x",
		"SHORT y",
		"s8 *cursor",
		"SHORT space",
	)),
	0x802DC15C: main.sym_fnc("PauseMenu_DrawScoreBox", arg=(
		"SHORT x",
		"SHORT y",
	)),
	0x802DC418: main.sym_fnc("PauseMenu_InitSelect"),
	0x802DC478: main.sym_fnc("PauseMenu_DrawSelect"),
	0x802DC570: main.sym_fnc("PauseMenu_DrawStar", arg=(
		"SHORT x",
		"SHORT y",
		"SHORT file",
		"SHORT course",
	)),
	0x802DC718: main.sym_fnc("PauseMenu_ProcScore", arg=(
		"SHORT x",
		"SHORT y",
	)),
	0x802DCA88: main.sym_fnc("PauseMenu_Proc", "SHORT"),
	0x802DCD04: main.sym_fnc("SaveMenu_DrawBanner", arg=(
		"CHAR code",
	)),
	0x802DCF30: main.sym_fnc("SaveMenu_ProcDemo", arg=(
		"SHORT x",
		"SHORT y",
	)),
	0x802DD194: main.sym_fnc("SaveMenu_ProcStar", arg=(
		"int code",
		"UCHAR star",
	)),
	0x802DD210: main.sym_fnc("SaveMenu_Draw"),
	0x802DD838: main.sym_fnc("SaveMenu_ProcSave", arg=(
		"SHORT x",
		"SHORT y",
		"s8 *cursor",
		"SHORT space",
	)),
	0x802DDAE0: main.sym_fnc("SaveMenu_Proc", "SHORT"),
	0x802DDCA4: main.sym_fnc("MessageProc", "SHORT", flag={"GLOBL"}),

	# src/weather.c
	0x802DDDF0: main.sym_fnc("SnowInit", "int", (
		"int code",
	)),
	0x802DDF38: main.sym_fnc("SnowProc", arg=(
		"int code",
		"SVEC pos",
	)),
	0x802DE0BC: main.sym_fnc("WeatherFree", arg=(
		"WEATHER *ptr",
	)),
	0x802DE114: main.sym_fnc("WeatherGetCoord", arg=(
		"SVEC look",
		"SVEC eye",
		"short *dist",
		"short *angx",
		"short *angy",
	), flag={"GLOBL"}),
	0x802DE23C: main.sym_fnc("WeatherSetCoord", arg=(
		"SVEC look",
		"SVEC eye",
		"SHORT dist",
		"SHORT angx",
		"SHORT angy",
	)),
	0x802DE360: main.sym_fnc("SnowIsVisible", "int", (
		"int i",
		"int x",
		"int y",
		"int z",
	)),
	0x802DE458: main.sym_fnc("SnowMakeSnow", arg=(
		"int x",
		"int y",
		"int z",
	)),
	0x802DE888: main.sym_fnc("SnowMakeBlizzard", arg=(
		"int x",
		"int y",
		"int z",
	)),
	0x802DECD4: main.sym_fnc("BubbleIsVisible", "int", (
		"int x",
		"int y",
		"int z",
	)), # unused
	0x802DED38: main.sym_fnc("SnowMakeBubble", arg=(
		"int x",
		"int y",
		"int z",
	)),
	0x802DEF2C: main.sym_fnc("WeatherXfm", arg=(
		"SVEC v0",
		"SVEC v1",
		"SVEC v2",
		"SHORT angx",
		"SHORT angy",
	), flag={"GLOBL"}),
	0x802DF334: main.sym_fnc("SnowVtx", arg=(
		"Gfx *g",
		"int i",
		"SVEC v0",
		"SVEC v1",
		"SVEC v2",
	)),
	0x802DF748: main.sym_fnc("SnowGfx", "Gfx *", (
		"int code",
		"SVEC pos",
		"SVEC eye",
		"SVEC look",
	)),
	0x802DFBC8: main.sym_fnc("WeatherDraw", "Gfx *", (
		"int code",
		"SVEC pos",
		"SVEC look",
		"SVEC eye",
	), flag={"GLOBL"}),

	# src/lava.c
	0x802DFD50: main.sym_fnc("LavaIsVisible", "int", (
		"int i",
		"int x",
		"int z",
		"int radius",
	)),
	0x802DFE00: main.sym_fnc("FlowerRand", "int"),
	0x802DFE80: main.sym_fnc("LavaMakeFlower", arg=(
		"SVEC pos",
	)),
	0x802E0120: main.sym_fnc("LavaNew", arg=(
		"int i",
		"SVEC pos",
	)),
	0x802E048C: main.sym_fnc("LavaMakeLava", arg=(
		"SVEC pos",
	)),
	0x802E065C: main.sym_fnc("WhirpoolMove", arg=(
		"int *x",
		"int *y",
		"int *z",
	)),
	0x802E08A8: main.sym_fnc("WhirpoolIsVisible", "int", (
		"int i",
	)),
	0x802E0934: main.sym_fnc("LavaMakeWhirlpool"),
	0x802E0E24: main.sym_fnc("JetIsVisible", "int", (
		"int i",
	)),
	0x802E0EB8: main.sym_fnc("LavaMakeJet"),
	0x802E1238: main.sym_fnc("LavaInit", "int", (
		"int code",
	)),
	0x802E126C: main.sym_fnc("L802E126C", flag={"GLOBL","LOCAL"}),
	0x802E1274: main.sym_fnc("L802E1274", flag={"GLOBL","LOCAL"}),
	0x802E1294: main.sym_fnc("L802E1294", flag={"GLOBL","LOCAL"}),
	0x802E12B4: main.sym_fnc("L802E12B4", flag={"GLOBL","LOCAL"}),
	0x802E12C8: main.sym_fnc("L802E12C8", flag={"GLOBL","LOCAL"}),
	0x802E12DC: main.sym_fnc("L802E12DC", flag={"GLOBL","LOCAL"}),
	0x802E1414: main.sym_fnc("LavaMake", arg=(
		"int code",
		"SVEC pos",
		"SVEC v0",
		"SVEC v1",
		"SVEC v2",
	)),
	0x802E1618: main.sym_fnc("LavaVtx", arg=(
		"Gfx *g",
		"int i",
		"SVEC v0",
		"SVEC v1",
		"SVEC v2",
		"Vtx *template",
	)),
	0x802E1A20: main.sym_fnc("LavaTxt", arg=(
		"int code",
		"SHORT i",
	)),
	0x802E1BB8: main.sym_fnc("LavaGfx", "Gfx *", (
		"int code",
		"SVEC pos",
		"SVEC eye",
		"SVEC look",
	)),
	0x802E1ED8: main.sym_fnc("LavaProc", arg=(
		"int code",
	)),
	0x802E1F48: main.sym_fnc("LavaDraw", "Gfx *", (
		"int code",
		"SVEC pos",
		"SVEC look",
		"SVEC eye",
	), flag={"GLOBL"}),

	# src/tag.c
	0x802E20A0: main.sym_fnc("TagAng", "SHORT", (
		"SHORT x",
	)),
	0x802E2134: main.sym_fnc("TagEnterCode", arg=(
		"int shape",
		"OBJLANG *script",
		"SHORT posx",
		"SHORT posy",
		"SHORT posz",
		"SHORT angy",
		"SHORT code",
	)),
	0x802E21DC: main.sym_fnc("TagEnterArg", arg=(
		"int shape",
		"OBJLANG *script",
		"SHORT posx",
		"SHORT posy",
		"SHORT posz",
		"SHORT angy",
		"SHORT arg",
	)),
	0x802E2284: main.sym_fnc("TagEnterXYZ", arg=(
		"int shape",
		"OBJLANG *script",
		"SHORT posx",
		"SHORT posy",
		"SHORT posz",
		"SHORT x",
		"SHORT y",
		"SHORT z",
	)),
	0x802E233C: main.sym_fnc("TagEnterOLD", arg=(
		"OBJLANG *script",
		"TAG *tag",
	)), # unused
	0x802E2414: main.sym_fnc("TagObjLoad", arg=(
		"SHORT scene",
		"TAG *tag",
	), flag={"GLOBL"}),
	0x802E2690: main.sym_fnc("TagLoad", arg=(
		"SHORT scene",
		"TAG *tag",
	), flag={"GLOBL"}),
	0x802E2758: main.sym_fnc("L802E2758", flag={"GLOBL","LOCAL"}),
	0x802E278C: main.sym_fnc("L802E278C", flag={"GLOBL","LOCAL"}),
	0x802E27C0: main.sym_fnc("L802E27C0", flag={"GLOBL","LOCAL"}),
	0x802E27F4: main.sym_fnc("L802E27F4", flag={"GLOBL","LOCAL"}),
	0x802E2828: main.sym_fnc("L802E2828", flag={"GLOBL","LOCAL"}),
	0x802E285C: main.sym_fnc("L802E285C", flag={"GLOBL","LOCAL"}),
	0x802E2890: main.sym_fnc("L802E2890", flag={"GLOBL","LOCAL"}),
	0x802E28C4: main.sym_fnc("L802E28C4", flag={"GLOBL","LOCAL"}),
	0x802E28EC: main.sym_fnc("MapObjLoad", arg=(
		"SHORT scene",
		"MAP **map",
	), flag={"GLOBL"}),
	0x802E2AAC: main.sym_fnc("L802E2AAC", flag={"GLOBL","LOCAL"}),
	0x802E2AD8: main.sym_fnc("L802E2AD8", flag={"GLOBL","LOCAL"}),
	0x802E2B30: main.sym_fnc("L802E2B30", flag={"GLOBL","LOCAL"}),
	0x802E2BB0: main.sym_fnc("L802E2BB0", flag={"GLOBL","LOCAL"}),
	0x802E2C5C: main.sym_fnc("L802E2C5C", flag={"GLOBL","LOCAL"}),

	# src/hud.c
	0x802E2CF0: main.sym_fnc("HUD_DrawChar", arg=(
		"unsigned int x",
		"unsigned int y",
		"u16 *txt",
	)),
	0x802E2E58: main.sym_fnc("HUD_Draw8x8", arg=(
		"unsigned int x",
		"unsigned int y",
		"u16 *txt",
	)),
	0x802E30B4: main.sym_fnc("MeterDrawN", arg=(
		"int power",
	)),
	0x802E3214: main.sym_fnc("MeterDraw", arg=(
		"int power",
	)),
	0x802E33B8: main.sym_fnc("MeterAlert"),
	0x802E3430: main.sym_fnc("MeterShow"),
	0x802E34E4: main.sym_fnc("MeterHide"),
	0x802E352C: main.sym_fnc("MeterProc", arg=(
		"SHORT power",
	)),
	0x802E3654: main.sym_fnc("HUD_DrawPower"),
	0x802E3744: main.sym_fnc("HUD_DrawLife"),
	0x802E37A8: main.sym_fnc("HUD_DrawCoin"),
	0x802E380C: main.sym_fnc("HUD_DrawStar"),
	0x802E38E4: main.sym_fnc("HUD_DrawKey"),
	0x802E395C: main.sym_fnc("HUD_DrawTime"),
	0x802E3B1C: main.sym_fnc("HUD_SetCamera", arg=(
		"SHORT flag",
	), flag={"GLOBL"}),
	0x802E3B3C: main.sym_fnc("HUD_DrawCamera"),
	0x802E3D2C: main.sym_fnc("HUD_Draw", flag={"GLOBL"}),

	# src/object_b.c
	0x802E3E50: main.sym_fnc("object_b_802E3E50", flag={"GLOBL"}), # extern
	0x802E3E68: main.sym("object_b_802E3E68"), # unused
	0x802E3F68: main.sym("object_b_802E3F68"),
	0x802E3FAC: main.sym("object_b_802E3FAC"),
	0x802E405C: main.sym("object_b_802E405C"),
	0x802E41A4: main.sym("object_b_802E41A4"),
	0x802E42E0: main.sym("object_b_802E42E0"),
	0x802E43E4: main.sym("object_b_802E43E4"),
	0x802E445C: main.sym("object_b_802E445C"),
	0x802E4814: main.sym("object_b_802E4814"),
	0x802E4CEC: main.sym("object_b_802E4CEC"),
	0x802E4D88: main.sym("object_b_802E4D88"),
	0x802E4E90: main.sym("object_b_802E4E90"),
	0x802E5114: main.sym("object_b_802E5114"),
	0x802E5160: main.sym("object_b_802E5160"),
	0x802E5208: main.sym("object_b_802E5208"),
	0x802E52B8: main.sym("object_b_802E52B8"),
	0x802E5360: main.sym("object_b_802E5360"),
	0x802E53F4: main.sym("object_b_802E53F4"),
	0x802E54B0: main.sym("object_b_802E54B0"),
	0x802E55D0: main.sym("object_b_802E55D0"),
	0x802E569C: main.sym("object_b_802E569C"),
	0x802E5760: main.sym("object_b_802E5760"),
	0x802E5824: main.sym("object_b_802E5824"),
	0x802E58B4: main.sym("object_b_802E58B4"),
	0x802E5948: main.sym("object_b_802E5948"),
	0x802E5A80: main.sym("object_b_802E5A80"),
	0x802E5B18: main.sym("object_b_802E5B18"),
	0x802E5C6C: main.sym("object_b_802E5C6C"),
	0x802E5D04: main.sym("object_b_802E5D04"), # unused
	0x802E5DE8: main.sym("object_b_802E5DE8"),
	0x802E5E6C: main.sym("object_b_802E5E6C"),
	0x802E5EA4: main.sym("object_b_802E5EA4"),
	0x802E5EE8: main.sym("object_b_802E5EE8", flag={"GLOBL"}), # objcall
	0x802E5F64: main.sym("object_b_802E5F64", flag={"GLOBL"}), # objcall
	0x802E6098: main.sym("object_b_802E6098", flag={"GLOBL"}), # objcall
	0x802E6114: main.sym("object_b_802E6114", flag={"GLOBL"}), # objcall
	0x802E62A4: main.sym("object_b_802E62A4", flag={"GLOBL"}), # objcall
	0x802E631C: main.sym("object_b_802E631C"),
	0x802E63EC: main.sym("object_b_802E63EC"),
	0x802E6474: main.sym("object_b_802E6474", flag={"GLOBL"}), # objcall
	0x802E64F0: main.sym_fnc("L802E64F0", flag={"GLOBL","LOCAL"}),
	0x802E6540: main.sym_fnc("L802E6540", flag={"GLOBL","LOCAL"}),
	0x802E6550: main.sym_fnc("L802E6550", flag={"GLOBL","LOCAL"}),
	0x802E6570: main.sym_fnc("L802E6570", flag={"GLOBL","LOCAL"}),
	0x802E65A8: main.sym_fnc("L802E65A8", flag={"GLOBL","LOCAL"}),
	0x802E6628: main.sym("object_b_802E6628", flag={"GLOBL"}), # objcall
	0x802E6660: main.sym_fnc("L802E6660", flag={"GLOBL","LOCAL"}),
	0x802E66D4: main.sym_fnc("L802E66D4", flag={"GLOBL","LOCAL"}),
	0x802E66E4: main.sym_fnc("L802E66E4", flag={"GLOBL","LOCAL"}),
	0x802E6704: main.sym_fnc("L802E6704", flag={"GLOBL","LOCAL"}),
	0x802E673C: main.sym_fnc("L802E673C", flag={"GLOBL","LOCAL"}),
	0x802E6790: main.sym("object_b_802E6790", flag={"GLOBL"}), # objcall
	0x802E67DC: main.sym("object_b_802E67DC", flag={"GLOBL"}), # objcall
	0x802E6A2C: main.sym("object_b_802E6A2C", flag={"GLOBL"}), # objcall
	0x802E6A8C: main.sym("object_b_802E6A8C"),
	0x802E6AF8: main.sym("object_b_802E6AF8"),
	0x802E6BD4: main.sym("object_b_802E6BD4"),
	0x802E6CF0: main.sym("object_b_802E6CF0"),
	0x802E6DC8: main.sym("object_b_802E6DC8"),
	0x802E6E84: main.sym("object_b_802E6E84"),
	0x802E6ED8: main.sym("object_b_802E6ED8"),
	0x802E7020: main.sym("object_b_802E7020"),
	0x802E7134: main.sym("object_b_802E7134"),
	0x802E7180: main.sym("object_b_802E7180"),
	0x802E7220: main.sym("object_b_802E7220"),
	0x802E7280: main.sym("object_b_802E7280"),
	0x802E7324: main.sym("object_b_802E7324"),
	0x802E742C: main.sym("object_b_802E742C", flag={"GLOBL"}), # objcall
	0x802E75A0: main.sym("object_b_802E75A0", flag={"GLOBL"}), # objcall
	0x802E76AC: main.sym("object_b_802E76AC", flag={"GLOBL"}), # objcall
	0x802E770C: main.sym("object_b_802E770C"),
	0x802E7814: main.sym("object_b_802E7814"),
	0x802E79DC: main.sym("object_b_802E79DC"),
	0x802E7B00: main.sym("object_b_802E7B00"),
	0x802E7BB0: main.sym("object_b_802E7BB0"),
	0x802E7C4C: main.sym("object_b_802E7C4C", flag={"GLOBL"}), # objcall
	0x802E7C90: main.sym("object_b_802E7C90", flag={"GLOBL"}), # objcall
	0x802E7D4C: main.sym("object_b_802E7D4C"),
	0x802E7E54: main.sym("object_b_802E7E54", flag={"GLOBL"}), # objcall
	0x802E7F70: main.sym("object_b_802E7F70", flag={"GLOBL"}), # objcall
	0x802E7FB8: main.sym("object_b_802E7FB8"),
	0x802E7FEC: main.sym("object_b_802E7FEC"),
	0x802E80DC: main.sym("object_b_802E80DC", flag={"GLOBL"}), # objcall
	0x802E82B0: main.sym("object_b_802E82B0", flag={"GLOBL"}), # objcall
	0x802E8388: main.sym("object_b_802E8388", flag={"GLOBL"}), # objcall
	0x802E844C: main.sym("object_b_802E844C"),
	0x802E84CC: main.sym("object_b_802E84CC"),
	0x802E8618: main.sym("object_b_802E8618"),
	0x802E885C: main.sym("object_b_802E885C"),
	0x802E8920: main.sym("object_b_802E8920"),
	0x802E89D4: main.sym("object_b_802E89D4", flag={"GLOBL"}), # objcall
	0x802E8A0C: main.sym_fnc("L802E8A0C", flag={"GLOBL","LOCAL"}),
	0x802E8A64: main.sym_fnc("L802E8A64", flag={"GLOBL","LOCAL"}),
	0x802E8A74: main.sym_fnc("L802E8A74", flag={"GLOBL","LOCAL"}),
	0x802E8A90: main.sym_fnc("L802E8A90", flag={"GLOBL","LOCAL"}),
	0x802E8AA0: main.sym_fnc("L802E8AA0", flag={"GLOBL","LOCAL"}),
	0x802E8AE4: main.sym("object_b_802E8AE4", flag={"GLOBL"}), # objcall
	0x802E8C18: main.sym("object_b_802E8C18"),
	0x802E8D98: main.sym("object_b_802E8D98"),
	0x802E8ECC: main.sym("object_b_802E8ECC", flag={"GLOBL"}), # objcall
	0x802E8F68: main.sym("object_b_802E8F68", flag={"GLOBL"}), # objcall
	0x802E9018: main.sym("object_b_802E9018"),
	0x802E9278: main.sym("object_b_802E9278"),
	0x802E9470: main.sym("object_b_802E9470"),
	0x802E94E4: main.sym("object_b_802E94E4"),
	0x802E9548: main.sym("object_b_802E9548"),
	0x802E96C8: main.sym("object_b_802E96C8", flag={"GLOBL"}), # objcall
	0x802E9764: main.sym("object_b_802E9764", flag={"GLOBL"}), # objcall
	0x802E97FC: main.sym("object_b_802E97FC"),
	0x802E98C0: main.sym("object_b_802E98C0"),
	0x802E9A4C: main.sym("object_b_802E9A4C"),
	0x802E9CF4: main.sym("object_b_802E9CF4"),
	0x802E9D98: main.sym("object_b_802E9D98"),
	0x802E9F60: main.sym("object_b_802E9F60"),
	0x802EA144: main.sym("object_b_802EA144"),
	0x802EA258: main.sym("object_b_802EA258"),
	0x802EA3F0: main.sym("object_b_802EA3F0"),
	0x802EA4EC: main.sym("object_b_802EA4EC"),
	0x802EA588: main.sym("object_b_802EA588", flag={"GLOBL"}), # objcall
	0x802EA6A8: main.sym("object_b_802EA6A8", flag={"GLOBL"}), # objcall
	0x802EA6F8: main.sym("object_b_802EA6F8"),
	0x802EA75C: main.sym("object_b_802EA75C"),
	0x802EA7E0: main.sym("object_b_802EA7E0", flag={"GLOBL"}), # objcall
	0x802EA888: main.sym("object_b_802EA888", flag={"GLOBL"}), # objcall
	0x802EA934: main.sym("object_b_802EA934", flag={"GLOBL"}), # objcall
	0x802EAA10: main.sym("object_b_802EAA10", flag={"GLOBL"}), # objcall
	0x802EAA50: main.sym("object_b_802EAA50", flag={"GLOBL"}), # objcall
	0x802EAA8C: main.sym("object_b_802EAA8C", flag={"GLOBL"}), # objcall
	0x802EAAD0: main.sym("object_b_802EAAD0", flag={"GLOBL"}), # objcall
	0x802EABF0: main.sym("object_b_802EABF0", flag={"GLOBL"}), # objcall
	0x802EAC3C: main.sym("object_b_802EAC3C", flag={"GLOBL"}), # objcall
	0x802EAD3C: main.sym("object_b_802EAD3C", flag={"GLOBL"}), # objcall
	0x802EAEF8: main.sym("object_b_802EAEF8", flag={"GLOBL"}), # objcall
	0x802EAF84: main.sym("object_b_802EAF84"),
	0x802EB05C: main.sym("object_b_802EB05C", flag={"GLOBL"}), # objcall
	0x802EB104: main.sym("object_b_802EB104", flag={"GLOBL"}), # objcall
	0x802EB1C0: main.sym("object_b_802EB1C0"),
	0x802EB288: main.sym("object_b_802EB288"),
	0x802EB3F0: main.sym("object_b_802EB3F0"),
	0x802EB510: main.sym("object_b_802EB510"),
	0x802EB5C4: main.sym("object_b_802EB5C4"),
	0x802EB630: main.sym("object_b_802EB630"),
	0x802EB744: main.sym("object_b_802EB744"),
	0x802EB7E0: main.sym("object_b_802EB7E0"),
	0x802EB8B0: main.sym("object_b_802EB8B0"),
	0x802EB9D0: main.sym("object_b_802EB9D0", flag={"GLOBL"}), # objcall
	0x802EBB74: main.sym("object_b_802EBB74"),
	0x802EBC00: main.sym("object_b_802EBC00", flag={"GLOBL"}), # objcall
	0x802EBC88: main.sym("object_b_802EBC88"),
	0x802EBCE0: main.sym("object_b_802EBCE0", flag={"GLOBL"}), # objcall
	0x802EBD94: main.sym_fnc("L802EBD94", flag={"GLOBL","LOCAL"}),
	0x802EBE04: main.sym_fnc("L802EBE04", flag={"GLOBL","LOCAL"}),
	0x802EBE1C: main.sym_fnc("L802EBE1C", flag={"GLOBL","LOCAL"}),
	0x802EBE34: main.sym_fnc("L802EBE34", flag={"GLOBL","LOCAL"}),
	0x802EBE4C: main.sym_fnc("L802EBE4C", flag={"GLOBL","LOCAL"}),
	0x802EBE9C: main.sym_fnc("L802EBE9C", flag={"GLOBL","LOCAL"}),
	0x802EBF70: main.sym("object_b_802EBF70"),
	0x802EC030: main.sym("object_b_802EC030"),
	0x802EC1B0: main.sym("object_b_802EC1B0", flag={"GLOBL"}), # objcall
	0x802EC200: main.sym("object_b_802EC200"),
	0x802EC3D0: main.sym("object_b_802EC3D0"),
	0x802EC4E0: main.sym("object_b_802EC4E0"),
	0x802EC59C: main.sym("object_b_802EC59C"),
	0x802EC75C: main.sym("object_b_802EC75C", flag={"GLOBL"}), # objcall
	0x802EC7CC: main.sym("object_b_802EC7CC"), # unused
	0x802EC818: main.sym("object_b_802EC818"),
	0x802EC908: main.sym("object_b_802EC908", flag={"GLOBL"}), # objcall
	0x802EC9B8: main.sym("object_b_802EC9B8", flag={"GLOBL"}), # objcall
	0x802EC9F0: main.sym("object_b_802EC9F0"),
	0x802ECBA4: main.sym("object_b_802ECBA4", flag={"GLOBL"}), # objcall
	0x802ECC14: main.sym("object_b_802ECC14", flag={"GLOBL"}), # objcall
	0x802ECD0C: main.sym("object_b_802ECD0C", flag={"GLOBL"}), # objcall
	0x802ECEA0: main.sym("object_b_802ECEA0", flag={"GLOBL"}), # objcall
	0x802ECFAC: main.sym("object_b_802ECFAC", flag={"GLOBL"}), # objcall
	0x802ED10C: main.sym("object_b_802ED10C"),
	0x802ED28C: main.sym("object_b_802ED28C"),
	0x802ED39C: main.sym("object_b_802ED39C", flag={"GLOBL"}), # objcall
	0x802ED40C: main.sym("object_b_802ED40C", flag={"GLOBL"}), # objcall
	0x802ED45C: main.sym("object_b_802ED45C", flag={"GLOBL"}), # objcall
	0x802ED498: main.sym("object_b_802ED498", flag={"GLOBL"}), # objcall
	0x802ED62C: main.sym("object_b_802ED62C", flag={"GLOBL"}), # objcall
	0x802ED78C: main.sym("object_b_802ED78C", flag={"GLOBL"}), # objcall
	0x802ED7FC: main.sym("object_b_802ED7FC", flag={"GLOBL"}), # objcall
	0x802EDACC: main.sym("object_b_802EDACC", flag={"GLOBL"}), # objcall
	0x802EDB2C: main.sym("object_b_802EDB2C", flag={"GLOBL"}), # objcall
	0x802EDDFC: main.sym("object_b_802EDDFC", flag={"GLOBL"}), # objcall
	0x802EDF28: main.sym("object_b_802EDF28", flag={"GLOBL"}), # objcall
	0x802EE124: main.sym("object_b_802EE124", flag={"GLOBL"}), # objcall
	0x802EE1A0: main.sym("object_b_802EE1A0"),
	0x802EE268: main.sym("object_b_802EE268"),
	0x802EE2B8: main.sym_fnc("L802EE2B8", flag={"GLOBL","LOCAL"}),
	0x802EE338: main.sym_fnc("L802EE338", flag={"GLOBL","LOCAL"}),
	0x802EE390: main.sym_fnc("L802EE390", flag={"GLOBL","LOCAL"}),
	0x802EE3C0: main.sym_fnc("L802EE3C0", flag={"GLOBL","LOCAL"}),
	0x802EE42C: main.sym_fnc("L802EE42C", flag={"GLOBL","LOCAL"}),
	0x802EE46C: main.sym("object_b_802EE46C"),
	0x802EE598: main.sym("object_b_802EE598"),
	0x802EE728: main.sym("object_b_802EE728"),
	0x802EE778: main.sym("object_b_802EE778"),
	0x802EE7E0: main.sym("object_b_802EE7E0", flag={"GLOBL"}), # objcall
	0x802EE818: main.sym_fnc("L802EE818", flag={"GLOBL","LOCAL"}),
	0x802EE87C: main.sym_fnc("L802EE87C", flag={"GLOBL","LOCAL"}),
	0x802EE8AC: main.sym_fnc("L802EE8AC", flag={"GLOBL","LOCAL"}),
	0x802EE8BC: main.sym_fnc("L802EE8BC", flag={"GLOBL","LOCAL"}),
	0x802EE8CC: main.sym_fnc("L802EE8CC", flag={"GLOBL","LOCAL"}),
	0x802EE8F4: main.sym("object_b_802EE8F4", flag={"GLOBL"}), # objcall
	0x802EE9CC: main.sym("object_b_802EE9CC", flag={"GLOBL"}), # objcall
	0x802EEA24: main.sym("object_b_802EEA24"),
	0x802EEA7C: main.sym("object_b_802EEA7C"),
	0x802EEAB4: main.sym_fnc("L802EEAB4", flag={"GLOBL","LOCAL"}),
	0x802EEAD4: main.sym_fnc("L802EEAD4", flag={"GLOBL","LOCAL"}),
	0x802EEAF4: main.sym_fnc("L802EEAF4", flag={"GLOBL","LOCAL"}),
	0x802EEB14: main.sym_fnc("L802EEB14", flag={"GLOBL","LOCAL"}),
	0x802EEB30: main.sym_fnc("L802EEB30", flag={"GLOBL","LOCAL"}),
	0x802EEB64: main.sym("object_b_802EEB64"),
	0x802EECB8: main.sym("object_b_802EECB8"),
	0x802EED14: main.sym_fnc("L802EED14", flag={"GLOBL","LOCAL"}),
	0x802EED34: main.sym_fnc("L802EED34", flag={"GLOBL","LOCAL"}),
	0x802EED54: main.sym_fnc("L802EED54", flag={"GLOBL","LOCAL"}),
	0x802EED74: main.sym_fnc("L802EED74", flag={"GLOBL","LOCAL"}),
	0x802EED94: main.sym_fnc("L802EED94", flag={"GLOBL","LOCAL"}),
	0x802EEDF0: main.sym("object_b_802EEDF0", flag={"GLOBL"}), # objcall
	0x802EEEB4: main.sym("object_b_802EEEB4", flag={"GLOBL"}), # objcall
	0x802EEF9C: main.sym("object_b_802EEF9C", flag={"GLOBL"}), # objcall
	0x802EF0E8: main.sym("object_b_802EF0E8", flag={"GLOBL"}), # objcall
	0x802EF21C: main.sym("object_b_802EF21C", flag={"GLOBL"}), # objcall
	0x802EF274: main.sym("object_b_802EF274", flag={"GLOBL"}), # objcall
	0x802EF34C: main.sym("object_b_802EF34C", flag={"GLOBL"}), # objcall
	0x802EF3F4: main.sym("object_b_802EF3F4"),
	0x802EF524: main.sym("object_b_802EF524", flag={"GLOBL"}), # objcall
	0x802EF63C: main.sym("object_b_802EF63C", flag={"GLOBL"}), # objcall
	0x802EF66C: main.sym("object_b_802EF66C", flag={"GLOBL"}), # objcall
	0x802EF820: main.sym("object_b_802EF820", flag={"GLOBL"}), # objcall
	0x802EF858: main.sym("object_b_802EF858", flag={"GLOBL"}), # objcall
	0x802EFCD0: main.sym("object_b_802EFCD0", flag={"GLOBL"}), # objcall
	0x802EFD8C: main.sym("object_b_802EFD8C", flag={"GLOBL"}), # objcall
	0x802EFE64: main.sym("object_b_802EFE64", flag={"GLOBL"}), # objcall
	0x802EFEF4: main.sym("object_b_802EFEF4", flag={"GLOBL"}), # objcall
	0x802F0104: main.sym("object_b_802F0104", flag={"GLOBL"}), # objcall
	0x802F0168: main.sym("object_b_802F0168", flag={"GLOBL"}), # objcall
	0x802F0288: main.sym("object_b_802F0288"),
	0x802F04A0: main.sym("object_b_802F04A0"),
	0x802F05B4: main.sym("object_b_802F05B4", flag={"GLOBL"}), # objcall
	0x802F06A8: main.sym("object_b_802F06A8", flag={"GLOBL"}), # objcall
	0x802F0714: main.sym("object_b_802F0714", flag={"GLOBL"}), # objcall
	0x802F0788: main.sym("object_b_802F0788", flag={"GLOBL"}), # objcall
	0x802F07F4: main.sym("object_b_802F07F4", flag={"GLOBL"}), # objcall
	0x802F0820: main.sym("object_b_802F0820", flag={"GLOBL"}), # objcall
	0x802F084C: main.sym("object_b_802F084C", flag={"GLOBL"}), # objcall
	0x802F0898: main.sym("object_b_802F0898", flag={"GLOBL"}), # objcall
	0x802F0950: main.sym("object_b_802F0950", flag={"GLOBL"}), # objcall
	0x802F09A4: main.sym("object_b_802F09A4", flag={"GLOBL"}), # objcall
	0x802F09F0: main.sym("object_b_802F09F0", flag={"GLOBL"}), # objcall
	0x802F0A40: main.sym("object_b_802F0A40", flag={"GLOBL"}), # objcall
	0x802F0B7C: main.sym("object_b_802F0B7C"),
	0x802F0BD4: main.sym("object_b_802F0BD4"),
	0x802F0C94: main.sym("object_b_802F0C94"),
	0x802F0DF0: main.sym("object_b_802F0DF0"),
	0x802F0FA8: main.sym("object_b_802F0FA8"),
	0x802F105C: main.sym("object_b_802F105C", flag={"GLOBL"}), # objcall
	0x802F1094: main.sym_fnc("L802F1094", flag={"GLOBL","LOCAL"}),
	0x802F112C: main.sym_fnc("L802F112C", flag={"GLOBL","LOCAL"}),
	0x802F1158: main.sym_fnc("L802F1158", flag={"GLOBL","LOCAL"}),
	0x802F1184: main.sym_fnc("L802F1184", flag={"GLOBL","LOCAL"}),
	0x802F1194: main.sym_fnc("L802F1194", flag={"GLOBL","LOCAL"}),
	0x802F120C: main.sym("object_b_802F120C", flag={"GLOBL"}), # objcall
	0x802F1370: main.sym("object_b_802F1370", flag={"GLOBL"}), # objcall
	0x802F13A8: main.sym_fnc("L802F13A8", flag={"GLOBL","LOCAL"}),
	0x802F13E4: main.sym_fnc("L802F13E4", flag={"GLOBL","LOCAL"}),
	0x802F13EC: main.sym_fnc("L802F13EC", flag={"GLOBL","LOCAL"}),
	0x802F1420: main.sym_fnc("L802F1420", flag={"GLOBL","LOCAL"}),
	0x802F148C: main.sym_fnc("L802F148C", flag={"GLOBL","LOCAL"}),
	0x802F151C: main.sym("object_b_802F151C", flag={"GLOBL"}), # objcall
	0x802F15A8: main.sym("object_b_802F15A8", flag={"GLOBL"}), # objcall
	0x802F162C: main.sym("object_b_802F162C"),
	0x802F1714: main.sym("object_b_802F1714", flag={"GLOBL"}), # objcall
	0x802F17F0: main.sym("object_b_802F17F0", flag={"GLOBL"}), # objcall
	0x802F1954: main.sym("object_b_802F1954"),
	0x802F19C8: main.sym("object_b_802F19C8"),
	0x802F1A10: main.sym("object_b_802F1A10"),
	0x802F1A5C: main.sym_fnc("L802F1A5C", flag={"GLOBL","LOCAL"}),
	0x802F1A70: main.sym_fnc("L802F1A70", flag={"GLOBL","LOCAL"}),
	0x802F1A9C: main.sym_fnc("L802F1A9C", flag={"GLOBL","LOCAL"}),
	0x802F1B0C: main.sym_fnc("L802F1B0C", flag={"GLOBL","LOCAL"}),
	0x802F1B38: main.sym_fnc("L802F1B38", flag={"GLOBL","LOCAL"}),
	0x802F1BA8: main.sym_fnc("L802F1BA8", flag={"GLOBL","LOCAL"}),
	0x802F1BB8: main.sym("object_b_802F1BB8"),
	0x802F1D64: main.sym("object_b_802F1D64", flag={"GLOBL"}), # objcall
	0x802F1DC0: main.sym("object_b_802F1DC0"),
	0x802F1E5C: main.sym("object_b_802F1E5C"),
	0x802F1F3C: main.sym("object_b_802F1F3C", flag={"GLOBL"}), # objcall
	0x802F1FD0: main.sym("object_b_802F1FD0", flag={"GLOBL"}), # objcall
	0x802F2030: main.sym("object_b_802F2030"),
	0x802F20AC: main.sym("object_b_802F20AC", flag={"GLOBL"}), # objcall
	0x802F2140: main.sym("object_b_802F2140", flag={"GLOBL"}), # objcall
	0x802F21E0: main.sym("object_b_802F21E0"),
	0x802F2284: main.sym("object_b_802F2284"),
	0x802F23A8: main.sym("object_b_802F23A8", flag={"GLOBL"}), # objcall
	0x802F2498: main.sym("object_b_802F2498", flag={"GLOBL"}), # objcall
	0x802F24F4: main.sym("object_b_802F24F4", flag={"GLOBL"}), # objcall
	0x802F25B0: main.sym("object_b_802F25B0", flag={"GLOBL"}), # objcall
	0x802F2614: main.sym("object_b_802F2614", flag={"GLOBL"}), # objcall
	0x802F2768: main.sym("object_b_802F2768", flag={"GLOBL"}), # objcall
	0x802F2AA0: main.sym("object_b_802F2AA0"),
	0x802F2B88: main.sym_fnc("object_b_802F2B88", arg=(
		"float",
		"float",
		"float",
	), flag={"GLOBL"}), # extern
	0x802F2BD4: main.sym("object_b_802F2BD4"),
	0x802F2C24: main.sym("object_b_802F2C24"),
	0x802F2C84: main.sym("object_b_802F2C84", flag={"GLOBL"}), # objcall
	0x802F2D8C: main.sym("object_b_802F2D8C", flag={"GLOBL"}), # objcall
	0x802F2E6C: main.sym("RedCoin_Init", flag={"GLOBL"}), # objcall
	0x802F2F2C: main.sym("RedCoin_Proc", flag={"GLOBL"}), # objcall
	0x802F3014: main.sym("object_b_802F3014", flag={"GLOBL"}), # objcall
	0x802F30F0: main.sym("object_b_802F30F0", flag={"GLOBL"}), # objcall
	0x802F31BC: main.sym("object_b_802F31BC", flag={"GLOBL"}), # objcall
	0x802F328C: main.sym("object_b_802F328C", flag={"GLOBL"}), # objcall
	0x802F336C: main.sym("object_b_802F336C", flag={"GLOBL"}), # objcall
	0x802F341C: main.sym("object_b_802F341C"),
	0x802F36A4: main.sym("object_b_802F36A4", flag={"GLOBL"}), # objcall
	0x802F38B0: main.sym("object_b_802F38B0"),
	0x802F39B4: main.sym("object_b_802F39B4"),
	0x802F3A30: main.sym("object_b_802F3A30", flag={"GLOBL"}), # objcall
	0x802F3B98: main.sym("object_b_802F3B98", flag={"GLOBL"}), # objcall
	0x802F3C54: main.sym("object_b_802F3C54"),
	0x802F3CC8: main.sym("object_b_802F3CC8", flag={"GLOBL"}), # objcall
	0x802F3D30: main.sym("object_b_802F3D30", flag={"GLOBL"}), # objcall
	0x802F3DD0: main.sym("object_b_802F3DD0"),
	0x802F3EA8: main.sym("object_b_802F3EA8"),
	0x802F401C: main.sym("object_b_802F401C"),
	0x802F40CC: main.sym("object_b_802F40CC", flag={"GLOBL"}), # objcall
	0x802F4248: main.sym("object_b_802F4248", flag={"GLOBL"}), # objcall
	0x802F43B8: main.sym("object_b_802F43B8"),
	0x802F44C0: main.sym("object_b_802F44C0", flag={"GLOBL"}), # objcall
	0x802F45B8: main.sym("object_b_802F45B8", flag={"GLOBL"}), # objcall
	0x802F45F0: main.sym("object_b_802F45F0", flag={"GLOBL"}), # objcall
	0x802F4710: main.sym("object_b_802F4710", flag={"GLOBL"}), # objcall
	0x802F48F4: main.sym("object_b_802F48F4", flag={"GLOBL"}), # objcall
	0x802F496C: main.sym("object_b_802F496C", flag={"GLOBL"}), # objcall
	0x802F4B00: main.sym("object_b_802F4B00", flag={"GLOBL"}), # objcall
	0x802F4B78: main.sym("object_b_802F4B78", flag={"GLOBL"}), # objcall
	0x802F4C68: main.sym("object_b_802F4C68"),
	0x802F4CE0: main.sym("object_b_802F4CE0"),
	0x802F4D78: main.sym("object_b_802F4D78", flag={"GLOBL"}), # objcall
	0x802F4EB4: main.sym("object_b_802F4EB4", flag={"GLOBL"}), # objcall
	0x802F5010: main.sym("object_b_802F5010"),
	0x802F5068: main.sym("object_b_802F5068"),
	0x802F52C0: main.sym("object_b_802F52C0"),
	0x802F547C: main.sym("object_b_802F547C"),
	0x802F55A4: main.sym("object_b_802F55A4", flag={"GLOBL"}), # objcall
	0x802F5618: main.sym_fnc("L802F5618", flag={"GLOBL","LOCAL"}),
	0x802F56A0: main.sym_fnc("L802F56A0", flag={"GLOBL","LOCAL"}),
	0x802F57E8: main.sym_fnc("L802F57E8", flag={"GLOBL","LOCAL"}),
	0x802F5930: main.sym_fnc("L802F5930", flag={"GLOBL","LOCAL"}),
	0x802F5A78: main.sym_fnc("L802F5A78", flag={"GLOBL","LOCAL"}),
	0x802F5BC0: main.sym_fnc("L802F5BC0", flag={"GLOBL","LOCAL"}),
	0x802F5BD8: main.sym_fnc("L802F5BD8", flag={"GLOBL","LOCAL"}),
	0x802F5CD4: main.sym("object_b_802F5CD4", flag={"GLOBL"}), # objcall
	0x802F5D78: main.sym("object_b_802F5D78"),
	0x802F5E44: main.sym("object_b_802F5E44"),
	0x802F5F48: main.sym("object_b_802F5F48"),
	0x802F6014: main.sym("object_b_802F6014"),
	0x802F60D8: main.sym("object_b_802F60D8"),
	0x802F6150: main.sym("object_b_802F6150"),
	0x802F6228: main.sym("object_b_802F6228", flag={"GLOBL"}), # objcall
	0x802F62E4: main.sym("object_b_802F62E4", flag={"GLOBL"}), # objcall
	0x802F6448: main.sym("object_b_802F6448", flag={"GLOBL"}), # objcall
	0x802F6588: main.sym("object_b_802F6588"),
	0x802F665C: main.sym("object_b_802F665C"),
	0x802F6984: main.sym("object_b_802F6984", flag={"GLOBL"}), # objcall
	0x802F6A44: main.sym("object_b_802F6A44"),
	0x802F6B2C: main.sym("object_b_802F6B2C"),
	0x802F6C0C: main.sym("object_b_802F6C0C", flag={"GLOBL"}), # objcall
	0x802F6D20: main.sym("object_b_802F6D20", flag={"GLOBL"}), # objcall
	0x802F6D58: main.sym("object_b_802F6D58", flag={"GLOBL"}), # objcall
	0x802F6E40: main.sym("object_b_802F6E40", flag={"GLOBL"}), # objcall
	0x802F6EB0: main.sym("object_b_802F6EB0"),
	0x802F7068: main.sym("object_b_802F7068"),
	0x802F7264: main.sym("object_b_802F7264", flag={"GLOBL"}), # objcall
	0x802F7348: main.sym("object_b_802F7348", flag={"GLOBL"}), # objcall
	0x802F7398: main.sym("object_b_802F7398"),
	0x802F7418: main.sym("object_b_802F7418"),
	0x802F74DC: main.sym("object_b_802F74DC", flag={"GLOBL"}), # objcall
	0x802F7760: main.sym("object_b_802F7760", flag={"GLOBL"}), # objcall
	0x802F7924: main.sym("object_b_802F7924", flag={"GLOBL"}), # objcall
	0x802F7978: main.sym("object_b_802F7978", flag={"GLOBL"}), # objcall
	0x802F79B0: main.sym("object_b_802F79B0", flag={"GLOBL"}), # objcall
	0x802F7A58: main.sym("object_b_802F7A58", flag={"GLOBL"}), # objcall
	0x802F7C9C: main.sym("object_b_802F7C9C", flag={"GLOBL"}), # objcall
	0x802F7D04: main.sym("object_b_802F7D04", flag={"GLOBL"}), # objcall
	0x802F7F1C: main.sym("object_b_802F7F1C"),
	0x802F7FA0: main.sym("object_b_802F7FA0", flag={"GLOBL"}), # objcall
	0x802F8044: main.sym("object_b_802F8044", flag={"GLOBL"}), # objcall
	0x802F8158: main.sym("object_b_802F8158", flag={"GLOBL"}), # objcall
	0x802F8208: main.sym("object_b_802F8208", flag={"GLOBL"}), # objcall
	0x802F82F8: main.sym("object_b_802F82F8", flag={"GLOBL"}), # objcall
	0x802F83A4: main.sym("object_b_802F83A4", flag={"GLOBL"}), # objcall
	0x802F8490: main.sym("object_b_802F8490", flag={"GLOBL"}), # objcall
	0x802F85E0: main.sym("object_b_802F85E0"),
	0x802F8760: main.sym("object_b_802F8760"),
	0x802F8808: main.sym("object_b_802F8808"),
	0x802F893C: main.sym("object_b_802F893C"),
	0x802F8988: main.sym("object_b_802F8988"),
	0x802F8A34: main.sym("object_b_802F8A34"),
	0x802F8AB4: main.sym("object_b_802F8AB4"),
	0x802F8AEC: main.sym_fnc("L802F8AEC", flag={"GLOBL","LOCAL"}),
	0x802F8AFC: main.sym_fnc("L802F8AFC", flag={"GLOBL","LOCAL"}),
	0x802F8B0C: main.sym_fnc("L802F8B0C", flag={"GLOBL","LOCAL"}),
	0x802F8B1C: main.sym_fnc("L802F8B1C", flag={"GLOBL","LOCAL"}),
	0x802F8B2C: main.sym_fnc("L802F8B2C", flag={"GLOBL","LOCAL"}),
	0x802F8B54: main.sym("object_b_802F8B54"),
	0x802F8C74: main.sym("object_b_802F8C74"),
	0x802F8CF8: main.sym("object_b_802F8CF8"),
	0x802F8DAC: main.sym("object_b_802F8DAC", flag={"GLOBL"}), # objcall
	0x802F8E54: main.sym("object_b_802F8E54", flag={"GLOBL"}), # objcall
	0x802F8F08: main.sym("object_b_802F8F08"),
	0x802F9054: main.sym("object_b_802F9054"),
	0x802F923C: main.sym("object_b_802F923C"),
	0x802F93A8: main.sym("object_b_802F93A8"),
	0x802F9500: main.sym("object_b_802F9500"),
	0x802F95AC: main.sym("object_b_802F95AC"),
	0x802F965C: main.sym("object_b_802F965C", flag={"GLOBL"}), # objcall
	0x802F9694: main.sym_fnc("L802F9694", flag={"GLOBL","LOCAL"}),
	0x802F96A4: main.sym_fnc("L802F96A4", flag={"GLOBL","LOCAL"}),
	0x802F96B4: main.sym_fnc("L802F96B4", flag={"GLOBL","LOCAL"}),
	0x802F96C4: main.sym_fnc("L802F96C4", flag={"GLOBL","LOCAL"}),
	0x802F96D4: main.sym_fnc("L802F96D4", flag={"GLOBL","LOCAL"}),
	0x802F96E4: main.sym_fnc("L802F96E4", flag={"GLOBL","LOCAL"}),
	0x802F96F4: main.sym_fnc("L802F96F4", flag={"GLOBL","LOCAL"}),
	0x802F9704: main.sym_fnc("L802F9704", flag={"GLOBL","LOCAL"}),

	# src/object_c.c
	0x802F9730: main.sym("object_c_802F9730"),
	0x802F9770: main.sym("object_c_802F9770"),
	0x802F97BC: main.sym("object_c_802F97BC"),
	0x802F9820: main.sym("object_c_802F9820"),
	0x802F9890: main.sym("object_c_802F9890"),
	0x802F9904: main.sym("object_c_802F9904"),
	0x802F9A28: main.sym("object_c_802F9A28"),
	0x802F9E28: main.sym("object_c_802F9E28"),
	0x802FA158: main.sym("object_c_802FA158"),
	0x802FA1B0: main.sym("object_c_802FA1B0"),
	0x802FA1F8: main.sym("object_c_802FA1F8"),
	0x802FA25C: main.sym("object_c_802FA25C"),
	0x802FA2BC: main.sym("object_c_802FA2BC"),
	0x802FA32C: main.sym("object_c_802FA32C"),
	0x802FA360: main.sym("object_c_802FA360"),
	0x802FA39C: main.sym("object_c_802FA39C"),
	0x802FA3DC: main.sym("object_c_802FA3DC"),
	0x802FA428: main.sym("object_c_802FA428"),
	0x802FA4C4: main.sym("object_c_802FA4C4"),
	0x802FA544: main.sym("object_c_802FA544"),
	0x802FA5D0: main.sym("object_c_802FA5D0"),
	0x802FA618: main.sym("object_c_802FA618"),
	0x802FA660: main.sym("object_c_802FA660"),
	0x802FA6D4: main.sym("object_c_802FA6D4"),
	0x802FA748: main.sym("object_c_802FA748"),
	0x802FA7BC: main.sym("object_c_802FA7BC"),
	0x802FA830: main.sym("object_c_802FA830"),
	0x802FA900: main.sym("object_c_802FA900"),
	0x802FA964: main.sym("object_c_802FA964"),
	0x802FA9D8: main.sym("object_c_802FA9D8"),
	0x802FAA64: main.sym("object_c_802FAA64"),
	0x802FAAC8: main.sym("object_c_802FAAC8"),
	0x802FAC18: main.sym("object_c_802FAC18"),
	0x802FAD34: main.sym("object_c_802FAD34"),
	0x802FADD4: main.sym("object_c_802FADD4"),
	0x802FB01C: main.sym("object_c_802FB01C"),
	0x802FB0CC: main.sym("object_c_802FB0CC"),
	0x802FB128: main.sym("object_c_802FB128"),
	0x802FB254: main.sym("object_c_802FB254"), # unused
	0x802FB288: main.sym("object_c_802FB288"),
	0x802FB3A0: main.sym("object_c_802FB3A0"),
	0x802FB3DC: main.sym("object_c_802FB3DC"),
	0x802FB518: main.sym("object_c_802FB518"),
	0x802FB610: main.sym_fnc("L802FB610", flag={"GLOBL","LOCAL"}),
	0x802FB618: main.sym_fnc("L802FB618", flag={"GLOBL","LOCAL"}),
	0x802FB628: main.sym_fnc("L802FB628", flag={"GLOBL","LOCAL"}),
	0x802FB638: main.sym_fnc("L802FB638", flag={"GLOBL","LOCAL"}),
	0x802FB648: main.sym_fnc("L802FB648", flag={"GLOBL","LOCAL"}),
	0x802FB658: main.sym_fnc("L802FB658", flag={"GLOBL","LOCAL"}),
	0x802FB668: main.sym_fnc("L802FB668", flag={"GLOBL","LOCAL"}),
	0x802FB678: main.sym_fnc("L802FB678", flag={"GLOBL","LOCAL"}),
	0x802FB688: main.sym_fnc("L802FB688", flag={"GLOBL","LOCAL"}),
	0x802FB6E8: main.sym("object_c_802FB6E8"),
	0x802FB778: main.sym("object_c_802FB778"),
	0x802FB87C: main.sym("object_c_802FB87C"),
	0x802FB938: main.sym("object_c_802FB938"),
	0x802FBA40: main.sym("object_c_802FBA40"),
	0x802FBAB4: main.sym("object_c_802FBAB4"),
	0x802FBC4C: main.sym("object_c_802FBC4C", flag={"GLOBL"}), # objcall
	0x802FBD5C: main.sym("object_c_802FBD5C"),
	0x802FBDD4: main.sym("object_c_802FBDD4"),
	0x802FBE50: main.sym("object_c_802FBE50"),
	0x802FBECC: main.sym("object_c_802FBECC"),
	0x802FBF58: main.sym("object_c_802FBF58"),
	0x802FBFDC: main.sym("object_c_802FBFDC"),
	0x802FC03C: main.sym("object_c_802FC03C"),
	0x802FC16C: main.sym("object_c_802FC16C"),
	0x802FC288: main.sym("object_c_802FC288"),
	0x802FC338: main.sym("object_c_802FC338"),
	0x802FC414: main.sym("object_c_802FC414"),
	0x802FC510: main.sym("object_c_802FC510"),
	0x802FC670: main.sym("object_c_802FC670"),
	0x802FC914: main.sym("object_c_802FC914"),
	0x802FCAF4: main.sym("object_c_802FCAF4"),
	0x802FCB1C: main.sym("object_c_802FCB1C"),
	0x802FCC00: main.sym("object_c_802FCC00"),
	0x802FCCC8: main.sym("object_c_802FCCC8"),
	0x802FCD64: main.sym("object_c_802FCD64"),
	0x802FCE94: main.sym("object_c_802FCE94"),
	0x802FD014: main.sym("object_c_802FD014"),
	0x802FD068: main.sym("object_c_802FD068"),
	0x802FD3E4: main.sym("object_c_802FD3E4"),
	0x802FD464: main.sym("object_c_802FD464"),
	0x802FD4B0: main.sym("object_c_802FD4B0"),
	0x802FD6AC: main.sym("object_c_802FD6AC"),
	0x802FD708: main.sym_fnc("L802FD708", flag={"GLOBL","LOCAL"}),
	0x802FD718: main.sym_fnc("L802FD718", flag={"GLOBL","LOCAL"}),
	0x802FD728: main.sym_fnc("L802FD728", flag={"GLOBL","LOCAL"}),
	0x802FD738: main.sym_fnc("L802FD738", flag={"GLOBL","LOCAL"}),
	0x802FD748: main.sym_fnc("L802FD748", flag={"GLOBL","LOCAL"}),
	0x802FD758: main.sym_fnc("L802FD758", flag={"GLOBL","LOCAL"}),
	0x802FD7F8: main.sym("object_c_802FD7F8", flag={"GLOBL"}), # objcall
	0x802FD950: main.sym("object_c_802FD950", flag={"GLOBL"}), # objcall
	0x802FDA28: main.sym("object_c_802FDA28", flag={"GLOBL"}), # objcall
	0x802FDEA8: main.sym("object_c_802FDEA8"),
	0x802FDFC4: main.sym("object_c_802FDFC4"),
	0x802FE37C: main.sym("object_c_802FE37C"),
	0x802FE3B0: main.sym("object_c_802FE3B0", flag={"GLOBL"}), # objcall
	0x802FE450: main.sym("object_c_802FE450"),
	0x802FE520: main.sym("object_c_802FE520"),
	0x802FE8B4: main.sym("object_c_802FE8B4", flag={"GLOBL"}), # objcall
	0x802FE988: main.sym("object_c_802FE988"),
	0x802FEB00: main.sym("object_c_802FEB00"),
	0x802FED50: main.sym("object_c_802FED50"),
	0x802FEF18: main.sym("object_c_802FEF18"),
	0x802FF040: main.sym("object_c_802FF040", flag={"GLOBL"}), # objcall
	0x802FF214: main.sym("object_c_802FF214", flag={"GLOBL"}), # objcall
	0x802FF408: main.sym("object_c_802FF408", flag={"GLOBL"}), # objcall
	0x802FF518: main.sym("object_c_802FF518"),
	0x802FF584: main.sym("object_c_802FF584"),
	0x802FF600: main.sym("object_c_802FF600"),
	0x802FF868: main.sym("object_c_802FF868"),
	0x802FF8E8: main.sym("object_c_802FF8E8"),
	0x802FF94C: main.sym("object_c_802FF94C"),
	0x802FF96C: main.sym("object_c_802FF96C", flag={"GLOBL"}), # objcall
	0x802FFB38: main.sym("object_c_802FFB38", flag={"GLOBL"}), # objcall
	0x802FFC60: main.sym("object_c_802FFC60"),
	0x802FFDAC: main.sym("object_c_802FFDAC"),
	0x8030009C: main.sym("object_c_8030009C"),
	0x803000E4: main.sym("object_c_803000E4"),
	0x803002F4: main.sym("object_c_803002F4"),
	0x803004F0: main.sym("object_c_803004F0"),
	0x8030059C: main.sym("object_c_8030059C"),
	0x80300778: main.sym("object_c_80300778"),
	0x803008A8: main.sym("object_c_803008A8"),
	0x803008EC: main.sym("object_c_803008EC"),
	0x80300940: main.sym("object_c_80300940"),
	0x803009E8: main.sym_fnc("L803009E8", flag={"GLOBL","LOCAL"}),
	0x80300A38: main.sym_fnc("L80300A38", flag={"GLOBL","LOCAL"}),
	0x80300A48: main.sym_fnc("L80300A48", flag={"GLOBL","LOCAL"}),
	0x80300A58: main.sym_fnc("L80300A58", flag={"GLOBL","LOCAL"}),
	0x80300A68: main.sym_fnc("L80300A68", flag={"GLOBL","LOCAL"}),
	0x80300A78: main.sym_fnc("L80300A78", flag={"GLOBL","LOCAL"}),
	0x80300DD4: main.sym("object_c_80300DD4"),
	0x80300E40: main.sym("object_c_80300E40", flag={"GLOBL"}), # objcall
	0x80300ECC: main.sym("object_c_80300ECC", flag={"GLOBL"}), # objcall
	0x80301148: main.sym("object_c_80301148", flag={"GLOBL"}), # objcall
	0x80301180: main.sym("object_c_80301180", flag={"GLOBL"}), # objcall
	0x80301210: main.sym("object_c_80301210", flag={"GLOBL"}), # objcall
	0x803014CC: main.sym("object_c_803014CC"),
	0x803016E0: main.sym("object_c_803016E0"),
	0x80301940: main.sym("object_c_80301940"),
	0x80301C88: main.sym("object_c_80301C88"),
	0x80301E84: main.sym("object_c_80301E84"),
	0x80301F70: main.sym("object_c_80301F70"),
	0x80302024: main.sym("object_c_80302024"),
	0x803020E4: main.sym("object_c_803020E4"),
	0x80302154: main.sym("object_c_80302154", flag={"GLOBL"}), # objcall
	0x80302278: main.sym_fnc("L80302278", flag={"GLOBL","LOCAL"}),
	0x80302288: main.sym_fnc("L80302288", flag={"GLOBL","LOCAL"}),
	0x80302298: main.sym_fnc("L80302298", flag={"GLOBL","LOCAL"}),
	0x803022A8: main.sym_fnc("L803022A8", flag={"GLOBL","LOCAL"}),
	0x803022B8: main.sym_fnc("L803022B8", flag={"GLOBL","LOCAL"}),
	0x80302358: main.sym("object_c_80302358"),
	0x803023E4: main.sym("object_c_803023E4"),
	0x8030267C: main.sym("object_c_8030267C"),
	0x803027AC: main.sym("object_c_803027AC"),
	0x80302910: main.sym("object_c_80302910", flag={"GLOBL"}), # objcall
	0x803029B8: main.sym("object_c_803029B8"),
	0x80302A54: main.sym("object_c_80302A54"),
	0x80302B20: main.sym("object_c_80302B20"),
	0x80302C84: main.sym("object_c_80302C84"),
	0x80302DB0: main.sym("object_c_80302DB0"),
	0x80302E84: main.sym("object_c_80302E84"),
	0x80302F04: main.sym("object_c_80302F04"),
	0x80303028: main.sym("object_c_80303028", flag={"GLOBL"}), # objcall
	0x803030A8: main.sym("object_c_803030A8"),
	0x803031B4: main.sym("object_c_803031B4"),
	0x8030320C: main.sym("object_c_8030320C"),
	0x80303498: main.sym("object_c_80303498"),
	0x80303634: main.sym("object_c_80303634"),
	0x8030369C: main.sym("object_c_8030369C", flag={"GLOBL"}), # objcall
	0x80303744: main.sym("object_c_80303744", flag={"GLOBL"}), # objcall
	0x80303984: main.sym("object_c_80303984", flag={"GLOBL"}), # objcall
	0x80303A20: main.sym("object_c_80303A20"),
	0x80303B08: main.sym("object_c_80303B08"),
	0x80303C14: main.sym("object_c_80303C14"),
	0x80303F64: main.sym("object_c_80303F64", flag={"GLOBL"}), # objcall
	0x803041A0: main.sym("object_c_803041A0"),
	0x80304274: main.sym("object_c_80304274"),
	0x803043F8: main.sym("object_c_803043F8", flag={"GLOBL"}), # objcall
	0x80304474: main.sym("object_c_80304474"),
	0x803044C0: main.sym("object_c_803044C0", flag={"GLOBL"}), # objcall
	0x803044DC: main.sym("object_c_803044DC"),
	0x80304710: main.sym("object_c_80304710"),
	0x803047AC: main.sym("object_c_803047AC"),
	0x80304864: main.sym("object_c_80304864"),
	0x803048EC: main.sym("object_c_803048EC"),
	0x80304958: main.sym("object_c_80304958"),
	0x80304A14: main.sym("object_c_80304A14"),
	0x80304A70: main.sym("object_c_80304A70"),
	0x80304AE0: main.sym("object_c_80304AE0"),
	0x80304BA8: main.sym("object_c_80304BA8", flag={"GLOBL"}), # objcall
	0x80304C14: main.sym_fnc("L80304C14", flag={"GLOBL","LOCAL"}),
	0x80304C24: main.sym_fnc("L80304C24", flag={"GLOBL","LOCAL"}),
	0x80304C34: main.sym_fnc("L80304C34", flag={"GLOBL","LOCAL"}),
	0x80304C44: main.sym_fnc("L80304C44", flag={"GLOBL","LOCAL"}),
	0x80304C54: main.sym_fnc("L80304C54", flag={"GLOBL","LOCAL"}),
	0x80304C64: main.sym_fnc("L80304C64", flag={"GLOBL","LOCAL"}),
	0x80304C74: main.sym_fnc("L80304C74", flag={"GLOBL","LOCAL"}),
	0x80304C84: main.sym_fnc("L80304C84", flag={"GLOBL","LOCAL"}),
	0x80304E28: main.sym("object_c_80304E28"),
	0x80304F74: main.sym("object_c_80304F74"),
	0x80304FD4: main.sym("object_c_80304FD4", flag={"GLOBL"}), # objcall
	0x8030505C: main.sym("object_c_8030505C"),
	0x8030508C: main.sym("object_c_8030508C"),
	0x80305100: main.sym("object_c_80305100", flag={"GLOBL"}), # objcall
	0x8030522C: main.sym("object_c_8030522C"),
	0x803053DC: main.sym("object_c_803053DC"),
	0x80305474: main.sym("object_c_80305474"),
	0x8030586C: main.sym("object_c_8030586C"),
	0x803058A4: main.sym("object_c_803058A4"),
	0x80305904: main.sym("object_c_80305904"),
	0x80305A58: main.sym("object_c_80305A58", flag={"GLOBL"}), # objcall
	0x80305A90: main.sym_fnc("L80305A90", flag={"GLOBL","LOCAL"}),
	0x80305AA0: main.sym_fnc("L80305AA0", flag={"GLOBL","LOCAL"}),
	0x80305AB0: main.sym_fnc("L80305AB0", flag={"GLOBL","LOCAL"}),
	0x80305AC0: main.sym_fnc("L80305AC0", flag={"GLOBL","LOCAL"}),
	0x80305AD0: main.sym_fnc("L80305AD0", flag={"GLOBL","LOCAL"}),
	0x80305BB0: main.sym("object_c_80305BB0", flag={"GLOBL"}), # objcall
	0x80305C14: main.sym("object_c_80305C14", flag={"GLOBL"}), # objcall
	0x80305C90: main.sym("object_c_80305C90", flag={"GLOBL"}), # objcall
	0x80305E2C: main.sym("object_c_80305E2C", flag={"GLOBL"}), # objcall
	0x80305F24: main.sym("object_c_80305F24", flag={"GLOBL"}), # objcall
	0x80306084: main.sym("object_c_80306084", flag={"GLOBL"}), # objcall
	0x803062A8: main.sym("object_c_803062A8"),
	0x80306304: main.sym("object_c_80306304"),
	0x80306364: main.sym("object_c_80306364"),
	0x8030668C: main.sym("object_c_8030668C"),
	0x803066D8: main.sym("object_c_803066D8"),
	0x803067E8: main.sym("object_c_803067E8", flag={"GLOBL"}), # objcall
	0x803068C0: main.sym("object_c_803068C0", flag={"GLOBL"}), # objcall
	0x8030699C: main.sym("object_c_8030699C", flag={"GLOBL"}), # objcall
	0x80306A38: main.sym("object_c_80306A38", flag={"GLOBL"}), # objcall
	0x80306CC4: main.sym("object_c_80306CC4", flag={"GLOBL"}), # objcall
	0x80306D38: main.sym("object_c_80306D38", flag={"GLOBL"}), # objcall
	0x80306F48: main.sym("object_c_80306F48", flag={"GLOBL"}), # objcall
	0x80307010: main.sym("object_c_80307010", flag={"GLOBL"}), # objcall
	0x803071B8: main.sym("object_c_803071B8", flag={"GLOBL"}), # objcall
	0x80307240: main.sym("object_c_80307240"),
	0x80307348: main.sym("object_c_80307348"),
	0x803073F8: main.sym("object_c_803073F8"),
	0x80307434: main.sym("object_c_80307434"),
	0x803075F8: main.sym("object_c_803075F8"),
	0x80307670: main.sym("object_c_80307670", flag={"GLOBL"}), # objcall
	0x80307760: main.sym("object_c_80307760", flag={"GLOBL"}), # objcall
	0x803077E0: main.sym("object_c_803077E0", flag={"GLOBL"}), # objcall
	0x80307930: main.sym("object_c_80307930", flag={"GLOBL"}), # objcall
	0x803079C8: main.sym("object_c_803079C8", flag={"GLOBL"}), # objcall
	0x80307AE4: main.sym("object_c_80307AE4", flag={"GLOBL"}), # objcall
	0x80307B58: main.sym("object_c_80307B58", flag={"GLOBL"}), # objcall
	0x80307C88: main.sym("object_c_80307C88", flag={"GLOBL"}), # objcall
	0x80307CF8: main.sym("object_c_80307CF8", flag={"GLOBL"}), # objcall
	0x80307EA4: main.sym("object_c_80307EA4", flag={"GLOBL"}), # objcall
	0x80307FB8: main.sym("object_c_80307FB8"),
	0x8030803C: main.sym("object_c_8030803C", flag={"GLOBL"}), # objcall
	0x80308110: main.sym("object_c_80308110"),
	0x80308228: main.sym("object_c_80308228"),
	0x803082EC: main.sym("object_c_803082EC"),
	0x80308454: main.sym("object_c_80308454"),
	0x80308734: main.sym("object_c_80308734"),
	0x80308A74: main.sym("object_c_80308A74"),
	0x80308AF0: main.sym("object_c_80308AF0"),
	0x80308BB8: main.sym("object_c_80308BB8"),
	0x80308D6C: main.sym("object_c_80308D6C", flag={"GLOBL"}), # objcall
	0x80308DB0: main.sym_fnc("L80308DB0", flag={"GLOBL","LOCAL"}),
	0x80308DC0: main.sym_fnc("L80308DC0", flag={"GLOBL","LOCAL"}),
	0x80308DD0: main.sym_fnc("L80308DD0", flag={"GLOBL","LOCAL"}),
	0x80308DE0: main.sym_fnc("L80308DE0", flag={"GLOBL","LOCAL"}),
	0x80308DF0: main.sym_fnc("L80308DF0", flag={"GLOBL","LOCAL"}),
	0x80308E00: main.sym_fnc("L80308E00", flag={"GLOBL","LOCAL"}),
	0x80308E10: main.sym_fnc("L80308E10", flag={"GLOBL","LOCAL"}),
	0x80308E20: main.sym_fnc("L80308E20", flag={"GLOBL","LOCAL"}),
	0x80308F08: main.sym("object_c_80308F08"),
	0x80308F94: main.sym("object_c_80308F94"),
	0x803090B8: main.sym("object_c_803090B8"),
	0x80309154: main.sym("object_c_80309154", flag={"GLOBL"}), # objcall
	0x803091E0: main.sym("object_c_803091E0", flag={"GLOBL"}), # objcall
	0x80309354: main.sym("object_c_80309354", flag={"GLOBL"}), # objcall
	0x80309454: main.sym("object_c_80309454", flag={"GLOBL"}), # objcall
	0x803094D0: main.sym("object_c_803094D0", flag={"GLOBL"}), # objcall
	0x803094F8: main.sym("object_c_803094F8", flag={"GLOBL"}), # objcall
	0x80309530: main.sym("object_c_80309530", flag={"GLOBL"}), # objcall
	0x803097A4: main.sym("object_c_803097A4", flag={"GLOBL"}), # objcall
	0x803098C0: main.sym("object_c_803098C0", flag={"GLOBL"}), # objcall
	0x80309B64: main.sym("object_c_80309B64", flag={"GLOBL"}), # objcall
	0x80309CEC: main.sym("object_c_80309CEC", flag={"GLOBL"}), # objcall
	0x80309ED4: main.sym("object_c_80309ED4"),
	0x80309F68: main.sym("object_c_80309F68"),
	0x8030A0E8: main.sym("object_c_8030A0E8"),
	0x8030A11C: main.sym("object_c_8030A11C", flag={"GLOBL"}), # objcall
	0x8030A1C0: main.sym("object_c_8030A1C0", flag={"GLOBL"}), # objcall
	0x8030A2A8: main.sym("object_c_8030A2A8"),
	0x8030A390: main.sym("object_c_8030A390"),
	0x8030A514: main.sym("object_c_8030A514"),
	0x8030A614: main.sym("object_c_8030A614"),
	0x8030A93C: main.sym("object_c_8030A93C", flag={"GLOBL"}), # objcall
	0x8030AA54: main.sym_fnc("L8030AA54", flag={"GLOBL","LOCAL"}),
	0x8030AA64: main.sym_fnc("L8030AA64", flag={"GLOBL","LOCAL"}),
	0x8030AA7C: main.sym_fnc("L8030AA7C", flag={"GLOBL","LOCAL"}),
	0x8030AA84: main.sym_fnc("L8030AA84", flag={"GLOBL","LOCAL"}),
	0x8030AA94: main.sym_fnc("L8030AA94", flag={"GLOBL","LOCAL"}),
	0x8030AABC: main.sym("object_c_8030AABC", flag={"GLOBL"}), # objcall
	0x8030AD04: main.sym("object_c_8030AD04"),
	0x8030AE9C: main.sym("object_c_8030AE9C"),
	0x8030B0B8: main.sym("object_c_8030B0B8"),
	0x8030B0F0: main.sym("object_c_8030B0F0"),
	0x8030B220: main.sym("object_c_8030B220"),
	0x8030B2F4: main.sym("object_c_8030B2F4", flag={"GLOBL"}), # objcall
	0x8030B658: main.sym("object_c_8030B658", flag={"GLOBL"}), # objcall
	0x8030B6D8: main.sym("object_c_8030B6D8"),
	0x8030BA68: main.sym("object_c_8030BA68"),
	0x8030BC90: main.sym("object_c_8030BC90", flag={"GLOBL"}), # objcall
	0x8030BD2C: main.sym("object_c_8030BD2C"),
	0x8030BDF8: main.sym("object_c_8030BDF8"),
	0x8030BFD0: main.sym("object_c_8030BFD0", flag={"GLOBL"}), # objcall
	0x8030C06C: main.sym("object_c_8030C06C"),
	0x8030C0F0: main.sym("object_c_8030C0F0"),
	0x8030C210: main.sym("object_c_8030C210"),
	0x8030C2C8: main.sym("object_c_8030C2C8"),
	0x8030C364: main.sym("object_c_8030C364", flag={"GLOBL"}), # objcall
	0x8030C4B0: main.sym("object_c_8030C4B0", flag={"GLOBL"}), # objcall
	0x8030C564: main.sym("object_c_8030C564"),
	0x8030C60C: main.sym("object_c_8030C60C"),
	0x8030C6A4: main.sym("object_c_8030C6A4"),
	0x8030C828: main.sym("object_c_8030C828"),
	0x8030C894: main.sym("object_c_8030C894"),
	0x8030C8EC: main.sym("object_c_8030C8EC", flag={"GLOBL"}), # objcall
	0x8030C924: main.sym_fnc("L8030C924", flag={"GLOBL","LOCAL"}),
	0x8030C934: main.sym_fnc("L8030C934", flag={"GLOBL","LOCAL"}),
	0x8030C944: main.sym_fnc("L8030C944", flag={"GLOBL","LOCAL"}),
	0x8030C954: main.sym_fnc("L8030C954", flag={"GLOBL","LOCAL"}),
	0x8030C964: main.sym_fnc("L8030C964", flag={"GLOBL","LOCAL"}),
	0x8030C98C: main.sym("object_c_8030C98C", flag={"GLOBL"}), # objcall
	0x8030CD30: main.sym("object_c_8030CD30", flag={"GLOBL"}), # extern
	0x8030CDDC: main.sym("object_c_8030CDDC", flag={"GLOBL"}), # objcall
	0x8030CEC0: main.sym("object_c_8030CEC0"),
	0x8030D140: main.sym("object_c_8030D140"),
	0x8030D2F0: main.sym("object_c_8030D2F0", flag={"GLOBL"}), # objcall
	0x8030D42C: main.sym("object_c_8030D42C"),
	0x8030D4D4: main.sym("object_c_8030D4D4"),
	0x8030D598: main.sym("object_c_8030D598", flag={"GLOBL"}), # objcall
	0x8030D640: main.sym("object_c_8030D640", flag={"GLOBL"}), # objcall
	0x8030D8D4: main.sym("object_c_8030D8D4", flag={"GLOBL"}), # objcall
	0x8030D93C: main.sym("Ctrl_object_c_8030D93C", flag={"GLOBL"}), # shpcall
	0x8030D9AC: main.sym("Ctrl_object_c_8030D9AC", flag={"GLOBL"}), # shpcall
	0x8030DA14: main.sym("object_c_8030DA14"),
	0x8030DB38: main.sym("object_c_8030DB38"),
	0x8030DC70: main.sym("object_c_8030DC70", flag={"GLOBL"}), # objcall
	0x8030DFC4: main.sym("object_c_8030DFC4", flag={"GLOBL"}), # objcall
	0x8030E14C: main.sym("object_c_8030E14C", flag={"GLOBL"}), # objcall
	0x8030E16C: main.sym("object_c_8030E16C", flag={"GLOBL"}), # objcall
	0x8030E384: main.sym("object_c_8030E384"),
	0x8030E3E0: main.sym("object_c_8030E3E0"),
	0x8030E488: main.sym("object_c_8030E488"),
	0x8030E52C: main.sym("object_c_8030E52C"),
	0x8030E688: main.sym("object_c_8030E688"),
	0x8030E6D4: main.sym("object_c_8030E6D4"),
	0x8030E9E0: main.sym("object_c_8030E9E0"),
	0x8030EA9C: main.sym("object_c_8030EA9C", flag={"GLOBL"}), # objcall
	0x8030EAD4: main.sym_fnc("L8030EAD4", flag={"GLOBL","LOCAL"}),
	0x8030EAE4: main.sym_fnc("L8030EAE4", flag={"GLOBL","LOCAL"}),
	0x8030EAF4: main.sym_fnc("L8030EAF4", flag={"GLOBL","LOCAL"}),
	0x8030EB04: main.sym_fnc("L8030EB04", flag={"GLOBL","LOCAL"}),
	0x8030EB14: main.sym_fnc("L8030EB14", flag={"GLOBL","LOCAL"}),
	0x8030EB3C: main.sym("object_c_8030EB3C"),
	0x8030ECA8: main.sym("object_c_8030ECA8"),
	0x8030ECF8: main.sym("object_c_8030ECF8"),
	0x8030EF08: main.sym("object_c_8030EF08"),
	0x8030F118: main.sym("object_c_8030F118"),
	0x8030F21C: main.sym("object_c_8030F21C"),
	0x8030F440: main.sym("object_c_8030F440"),
	0x8030F508: main.sym("object_c_8030F508"),
	0x8030F58C: main.sym("object_c_8030F58C"),
	0x8030F5CC: main.sym("object_c_8030F5CC"),
	0x8030F628: main.sym("object_c_8030F628"),
	0x8030F6BC: main.sym("object_c_8030F6BC"),
	0x8030F840: main.sym("object_c_8030F840"),
	0x8030F9C0: main.sym("object_c_8030F9C0"),
	0x8030FB3C: main.sym("object_c_8030FB3C"),
	0x8030FC34: main.sym("object_c_8030FC34"),
	0x8030FCF4: main.sym("object_c_8030FCF4"),
	0x8030FE38: main.sym("object_c_8030FE38"),
	0x8030FFF8: main.sym("object_c_8030FFF8", flag={"GLOBL"}), # objcall
	0x80310078: main.sym_fnc("L80310078", flag={"GLOBL","LOCAL"}),
	0x80310088: main.sym_fnc("L80310088", flag={"GLOBL","LOCAL"}),
	0x80310098: main.sym_fnc("L80310098", flag={"GLOBL","LOCAL"}),
	0x803100A8: main.sym_fnc("L803100A8", flag={"GLOBL","LOCAL"}),
	0x803100B8: main.sym_fnc("L803100B8", flag={"GLOBL","LOCAL"}),
	0x803100C8: main.sym_fnc("L803100C8", flag={"GLOBL","LOCAL"}),
	0x803100D8: main.sym_fnc("L803100D8", flag={"GLOBL","LOCAL"}),
	0x803100E8: main.sym_fnc("L803100E8", flag={"GLOBL","LOCAL"}),
	0x803100F8: main.sym_fnc("L803100F8", flag={"GLOBL","LOCAL"}),
	0x80310108: main.sym_fnc("L80310108", flag={"GLOBL","LOCAL"}),
	0x80310118: main.sym_fnc("L80310118", flag={"GLOBL","LOCAL"}),
	0x80310128: main.sym_fnc("L80310128", flag={"GLOBL","LOCAL"}),
	0x80310138: main.sym_fnc("L80310138", flag={"GLOBL","LOCAL"}),
	0x80310148: main.sym_fnc("L80310148", flag={"GLOBL","LOCAL"}),
	0x80310158: main.sym_fnc("L80310158", flag={"GLOBL","LOCAL"}),
	0x803101DC: main.sym("object_c_803101DC"),
	0x80310258: main.sym("object_c_80310258"),
	0x80310318: main.sym("object_c_80310318"),
	0x80310498: main.sym("object_c_80310498", flag={"GLOBL"}), # objcall
	0x8031054C: main.sym("object_c_8031054C"),
	0x80310774: main.sym("object_c_80310774"),
	0x8031097C: main.sym("object_c_8031097C"),
	0x80310A7C: main.sym("object_c_80310A7C"),
	0x80310B2C: main.sym("object_c_80310B2C"),
	0x80310C3C: main.sym("object_c_80310C3C"),
	0x80310F04: main.sym("object_c_80310F04"),
	0x80311018: main.sym("object_c_80311018"),
	0x8031111C: main.sym("object_c_8031111C"),
	0x8031126C: main.sym("object_c_8031126C"),
	0x8031129C: main.sym("object_c_8031129C", flag={"GLOBL"}), # objcall
	0x80311358: main.sym_fnc("L80311358", flag={"GLOBL","LOCAL"}),
	0x80311378: main.sym_fnc("L80311378", flag={"GLOBL","LOCAL"}),
	0x80311390: main.sym_fnc("L80311390", flag={"GLOBL","LOCAL"}),
	0x803113A0: main.sym_fnc("L803113A0", flag={"GLOBL","LOCAL"}),
	0x803113B0: main.sym_fnc("L803113B0", flag={"GLOBL","LOCAL"}),
	0x803113C0: main.sym_fnc("L803113C0", flag={"GLOBL","LOCAL"}),
	0x803113D0: main.sym_fnc("L803113D0", flag={"GLOBL","LOCAL"}),
	0x803113E0: main.sym_fnc("L803113E0", flag={"GLOBL","LOCAL"}),
	0x8031157C: main.sym("object_c_8031157C"),
	0x803116C0: main.sym("object_c_803116C0"),
	0x80311874: main.sym("object_c_80311874", flag={"GLOBL"}), # objcall
	0x803118E4: main.sym("object_c_803118E4", flag={"GLOBL"}), # objcall
	0x80311954: main.sym("object_c_80311954"),
	0x803119E4: main.sym("object_c_803119E4"),
	0x80311B18: main.sym("object_c_80311B18"),
	0x80311B7C: main.sym("object_c_80311B7C"),
	0x80311DD8: main.sym("object_c_80311DD8"),
	0x80311EA4: main.sym("object_c_80311EA4"),
	0x80312070: main.sym("object_c_80312070", flag={"GLOBL"}), # objcall
	0x803120B0: main.sym_fnc("L803120B0", flag={"GLOBL","LOCAL"}),
	0x803120C0: main.sym_fnc("L803120C0", flag={"GLOBL","LOCAL"}),
	0x803120D0: main.sym_fnc("L803120D0", flag={"GLOBL","LOCAL"}),
	0x803120E0: main.sym_fnc("L803120E0", flag={"GLOBL","LOCAL"}),
	0x803120F0: main.sym_fnc("L803120F0", flag={"GLOBL","LOCAL"}),
	0x80312100: main.sym_fnc("L80312100", flag={"GLOBL","LOCAL"}),
	0x80312168: main.sym("object_c_80312168", flag={"GLOBL"}), # objcall
	0x80312200: main.sym("object_c_80312200", flag={"GLOBL"}), # objcall
	0x80312248: main.sym("object_c_80312248", flag={"GLOBL"}), # objcall
	0x80312370: main.sym("object_c_80312370"),
	0x8031262C: main.sym("object_c_8031262C"),
	0x8031274C: main.sym("object_c_8031274C", flag={"GLOBL"}), # objcall
	0x80312804: main.sym("object_c_80312804"),
	0x80312900: main.sym("object_c_80312900"),
	0x80312A54: main.sym("object_c_80312A54", flag={"GLOBL"}), # objcall
	0x80312AF4: main.sym("object_c_80312AF4"),
	0x80312B80: main.sym("object_c_80312B80"),
	0x80312D0C: main.sym("object_c_80312D0C"),
	0x80312EA8: main.sym("object_c_80312EA8"),
	0x80313110: main.sym("object_c_80313110", flag={"GLOBL"}), # objcall
	0x803131E8: main.sym("object_c_803131E8", flag={"GLOBL"}), # objcall
	0x8031326C: main.sym("object_c_8031326C", flag={"GLOBL"}), # objcall
	0x80313294: main.sym("object_c_80313294", flag={"GLOBL"}), # objcall
	0x80313354: main.sym("object_c_80313354", flag={"GLOBL"}), # objcall
	0x80313530: main.sym("object_c_80313530", flag={"GLOBL"}), # objcall
	0x803136CC: main.sym("object_c_803136CC", flag={"GLOBL"}), # objcall
	0x80313754: main.sym("object_c_80313754", flag={"GLOBL"}), # objcall
	0x803137F4: main.sym("object_c_803137F4", flag={"GLOBL"}), # objcall
	0x8031381C: main.sym("object_c_8031381C"),
	0x803139F0: main.sym("object_c_803139F0"),
	0x80313BE4: main.sym("object_c_80313BE4"),
	0x80313E1C: main.sym("object_c_80313E1C"),
	0x80313FC0: main.sym("object_c_80313FC0", flag={"GLOBL"}), # objcall
	0x80314098: main.sym("object_c_80314098"),
	0x8031427C: main.sym("object_c_8031427C"),
	0x803145D4: main.sym("object_c_803145D4", flag={"GLOBL"}), # objcall

	# src/audio/driver.c
	0x80314A30: main.sym("Na_driver_80314A30"),
	0x80314CC0: main.sym("Na_driver_80314CC0"),
	0x80314DE4: main.sym("Na_driver_80314DE4", flag={"GLOBL"}),
	0x80314F64: main.sym("Na_driver_80314F64"),
	0x80315590: main.sym("Na_driver_80315590"),
	0x80316010: main.sym("Na_driver_80316010"),
	0x803160DC: main.sym("Na_driver_803160DC"),
	0x80316138: main.sym("Na_driver_80316138"),
	0x8031619C: main.sym("Na_driver_8031619C"),
	0x803166FC: main.sym("Na_driver_803166FC"),
	0x80316AC8: main.sym("Na_driver_80316AC8", flag={"GLOBL"}),
	0x80316AF4: main.sym("Na_driver_80316AF4", flag={"GLOBL"}),
	0x80316DA8: main.sym("Na_driver_80316DA8", flag={"GLOBL"}),
	0x80316DB4: main.sym("Na_driver_80316DB4", flag={"GLOBL"}),
	0x80316E00: main.sym("Na_driver_80316E00", flag={"GLOBL"}),

	# src/audio/memory.c
	0x80316E80: main.sym("Na_memory_80316E80"),
	0x80316EC4: main.sym("Na_memory_80316EC4"),
	0x80316FB4: main.sym("Na_memory_80316FB4"),
	0x80317040: main.sym("Na_memory_80317040", flag={"GLOBL"}),
	0x803170B4: main.sym("Na_memory_803170B4"),
	0x803170D4: main.sym("Na_memory_803170D4"),
	0x803170E8: main.sym("Na_memory_803170E8"),
	0x80317118: main.sym("Na_memory_80317118"), # unused
	0x80317128: main.sym("Na_memory_80317128", flag={"GLOBL"}),
	0x80317184: main.sym("Na_memory_80317184"),
	0x80317200: main.sym("Na_memory_80317200"),
	0x8031727C: main.sym("Na_memory_8031727C"),
	0x80317338: main.sym("Na_memory_80317338"),
	0x803173F4: main.sym("Na_memory_803173F4"), # unused
	0x803173FC: main.sym("Na_memory_803173FC", flag={"GLOBL"}),
	0x8031782C: main.sym("Na_memory_8031782C", flag={"GLOBL"}),
	0x803178EC: main.sym("Na_memory_803178EC"),
	0x80317914: main.sym("Na_memory_80317914"),
	0x80317948: main.sym("Na_memory_80317948", flag={"GLOBL"}),
	0x80317BF0: main.sym_fnc("L80317BF0", flag={"GLOBL","LOCAL"}),
	0x80317BFC: main.sym_fnc("L80317BFC", flag={"GLOBL","LOCAL"}),
	0x80317C0C: main.sym_fnc("L80317C0C", flag={"GLOBL","LOCAL"}),
	0x80317C1C: main.sym_fnc("L80317C1C", flag={"GLOBL","LOCAL"}),
	0x80317C2C: main.sym_fnc("L80317C2C", flag={"GLOBL","LOCAL"}),
	0x80317C3C: main.sym_fnc("L80317C3C", flag={"GLOBL","LOCAL"}),

	# src/audio/system.c
	0x80318040: main.sym("Na_system_80318040"),
	0x803180C4: main.sym("Na_system_803180C4"),
	0x80318130: main.sym("Na_system_80318130", flag={"GLOBL"}),
	0x803181EC: main.sym("Na_system_803181EC", flag={"GLOBL"}),
	0x80318300: main.sym("Na_system_80318300", flag={"GLOBL"}),
	0x80318634: main.sym("Na_system_80318634", flag={"GLOBL"}),
	0x803188EC: main.sym("Na_system_803188EC"), # unused
	0x803188F4: main.sym("Na_system_803188F4", flag={"GLOBL"}),
	0x80318B30: main.sym("Na_system_80318B30"),
	0x80318C8C: main.sym("Na_system_80318C8C"),
	0x80318DC4: main.sym("Na_system_80318DC4"),
	0x80318E70: main.sym("Na_system_80318E70"),
	0x80318FAC: main.sym("Na_system_80318FAC"),
	0x803190F4: main.sym("Na_system_803190F4"),
	0x80319220: main.sym("Na_system_80319220", flag={"GLOBL"}),
	0x80319328: main.sym("Na_system_80319328", flag={"GLOBL"}),
	0x80319388: main.sym("Na_system_80319388"),
	0x8031950C: main.sym_fnc("Na_Load", flag={"GLOBL"}), # ext

	# src/audio/voice.c
	0x80319920: main.sym("Na_voice_80319920"),
	0x80319998: main.sym("Na_voice_80319998"),
	0x803199B8: main.sym("Na_voice_803199B8", flag={"GLOBL"}),
	0x80319DB8: main.sym("Na_voice_80319DB8"),
	0x80319F64: main.sym("Na_voice_80319F64", flag={"GLOBL"}),
	0x80319F84: main.sym("Na_voice_80319F84"),
	0x80319FA4: main.sym("Na_voice_80319FA4"),
	0x8031A1D0: main.sym("Na_voice_8031A1D0", flag={"GLOBL"}),
	0x8031A254: main.sym("Na_voice_8031A254"),
	0x8031A264: main.sym("Na_voice_8031A264", flag={"GLOBL"}),
	0x8031A2B4: main.sym("Na_voice_8031A2B4", flag={"GLOBL"}),
	0x8031A368: main.sym("Na_voice_8031A368", flag={"GLOBL"}),
	0x8031A494: main.sym("Na_voice_8031A494", flag={"GLOBL"}),
	0x8031A5D0: main.sym("Na_voice_8031A5D0"),
	0x8031A610: main.sym("Na_voice_8031A610", flag={"GLOBL"}),
	0x8031A63C: main.sym("Na_voice_8031A63C"),
	0x8031A6CC: main.sym("Na_voice_8031A6CC"),
	0x8031A794: main.sym("Na_voice_8031A794"),
	0x8031A7C8: main.sym("Na_voice_8031A7C8"),
	0x8031A820: main.sym("Na_voice_8031A820"),
	0x8031A89C: main.sym("Na_voice_8031A89C"),
	0x8031A8F0: main.sym("Na_voice_8031A8F0"),
	0x8031A94C: main.sym("Na_voice_8031A94C", flag={"GLOBL"}),
	0x8031AC34: main.sym("Na_voice_8031AC34", flag={"GLOBL"}),
	0x8031ADAC: main.sym("Na_voice_8031ADAC", flag={"GLOBL"}),

	# src/audio/effect.c
	0x8031AEE0: main.sym("Na_effect_8031AEE0"), # unused
	0x8031AEE8: main.sym("Na_effect_8031AEE8", flag={"GLOBL"}),
	0x8031B0CC: main.sym("Na_effect_8031B0CC"),
	0x8031B1C0: main.sym("Na_effect_8031B1C0"),
	0x8031B248: main.sym("Na_effect_8031B248"),
	0x8031B440: main.sym("Na_effect_8031B440", flag={"GLOBL"}),
	0x8031B4A0: main.sym("Na_effect_8031B4A0", flag={"GLOBL"}),
	0x8031B58C: main.sym("Na_effect_8031B58C", flag={"GLOBL"}),
	0x8031B5AC: main.sym("Na_effect_8031B5AC", flag={"GLOBL"}),
	0x8031B5D8: main.sym_fnc("L8031B5D8", flag={"GLOBL","LOCAL"}),
	0x8031B5E0: main.sym_fnc("L8031B5E0", flag={"GLOBL","LOCAL"}),
	0x8031B604: main.sym_fnc("L8031B604", flag={"GLOBL","LOCAL"}),
	0x8031B61C: main.sym_fnc("L8031B61C", flag={"GLOBL","LOCAL"}),
	0x8031B700: main.sym_fnc("L8031B700", flag={"GLOBL","LOCAL"}),
	0x8031B734: main.sym_fnc("L8031B734", flag={"GLOBL","LOCAL"}),
	0x8031B73C: main.sym_fnc("L8031B73C", flag={"GLOBL","LOCAL"}),
	0x8031B7BC: main.sym_fnc("L8031B7BC", flag={"GLOBL","LOCAL"}),

	# src/audio/sequence.c
	0x8031B830: main.sym("Na_sequence_8031B830"),
	0x8031B940: main.sym("Na_sequence_8031B940"),
	0x8031BA30: main.sym("Na_sequence_8031BA30", flag={"GLOBL"}),
	0x8031BA6C: main.sym("Na_sequence_8031BA6C"),
	0x8031BAF0: main.sym("Na_sequence_8031BAF0", flag={"GLOBL"}),
	0x8031BB5C: main.sym("Na_sequence_8031BB5C"),
	0x8031BBA4: main.sym("Na_sequence_8031BBA4"),
	0x8031BCD0: main.sym("Na_sequence_8031BCD0"),
	0x8031BDA0: main.sym("Na_sequence_8031BDA0"),
	0x8031BE44: main.sym("Na_sequence_8031BE44", flag={"GLOBL"}),
	0x8031BF14: main.sym("Na_sequence_8031BF14", flag={"GLOBL"}),
	0x8031BF54: main.sym("Na_sequence_8031BF54", flag={"GLOBL"}),
	0x8031BF94: main.sym("Na_sequence_8031BF94"),
	0x8031C03C: main.sym("Na_sequence_8031C03C"),
	0x8031C050: main.sym("Na_sequence_8031C050"),
	0x8031C080: main.sym("Na_sequence_8031C080"),
	0x8031C0C4: main.sym("Na_sequence_8031C0C4"),
	0x8031C194: main.sym(".L8031C194", flag={"LOCAL"}),
	0x8031C198: main.sym(".L8031C198", flag={"LOCAL"}),
	0x8031C200: main.sym_fnc("L8031C200", flag={"GLOBL","LOCAL"}),
	0x8031C23C: main.sym_fnc("L8031C23C", flag={"GLOBL","LOCAL"}),
	0x8031C298: main.sym_fnc("L8031C298", flag={"GLOBL","LOCAL"}),
	0x8031C2DC: main.sym_fnc("L8031C2DC", flag={"GLOBL","LOCAL"}),
	0x8031C328: main.sym_fnc("L8031C328", flag={"GLOBL","LOCAL"}),
	0x8031C36C: main.sym_fnc("L8031C36C", flag={"GLOBL","LOCAL"}),
	0x8031C3BC: main.sym_fnc("L8031C3BC", flag={"GLOBL","LOCAL"}),
	0x8031C3E8: main.sym_fnc("L8031C3E8", flag={"GLOBL","LOCAL"}),
	0x8031C454: main.sym_fnc("L8031C454", flag={"GLOBL","LOCAL"}),
	0x8031C4A4: main.sym_fnc("L8031C4A4", flag={"GLOBL","LOCAL"}),
	0x8031C5C8: main.sym_fnc("L8031C5C8", flag={"GLOBL","LOCAL"}),
	0x8031C698: main.sym_fnc("L8031C698", flag={"GLOBL","LOCAL"}),
	0x8031C6A0: main.sym_fnc("L8031C6A0", flag={"GLOBL","LOCAL"}),
	0x8031CBE0: main.sym_fnc("L8031CBE0", flag={"GLOBL","LOCAL"}),
	0x8031CBEC: main.sym_fnc("L8031CBEC", flag={"GLOBL","LOCAL"}),
	0x8031CE54: main.sym("Na_sequence_8031CE54"),
	0x8031CFD4: main.sym("Na_sequence_8031CFD4"),
	0x8031D068: main.sym("Na_sequence_8031D068"),
	0x8031D08C: main.sym("Na_sequence_8031D08C"),
	0x8031D144: main.sym_fnc("L8031D144", flag={"GLOBL","LOCAL"}),
	0x8031D1F8: main.sym_fnc("L8031D1F8", flag={"GLOBL","LOCAL"}),
	0x8031D234: main.sym_fnc("L8031D234", flag={"GLOBL","LOCAL"}),
	0x8031D26C: main.sym_fnc("L8031D26C", flag={"GLOBL","LOCAL"}),
	0x8031D2B4: main.sym_fnc("L8031D2B4", flag={"GLOBL","LOCAL"}),
	0x8031D2C4: main.sym_fnc("L8031D2C4", flag={"GLOBL","LOCAL"}),
	0x8031D31C: main.sym_fnc("L8031D31C", flag={"GLOBL","LOCAL"}),
	0x8031D344: main.sym_fnc("L8031D344", flag={"GLOBL","LOCAL"}),
	0x8031D354: main.sym_fnc("L8031D354", flag={"GLOBL","LOCAL"}),
	0x8031D370: main.sym_fnc("L8031D370", flag={"GLOBL","LOCAL"}),
	0x8031D3A8: main.sym_fnc("L8031D3A8", flag={"GLOBL","LOCAL"}),
	0x8031D3C4: main.sym_fnc("L8031D3C4", flag={"GLOBL","LOCAL"}),
	0x8031D3D4: main.sym_fnc("L8031D3D4", flag={"GLOBL","LOCAL"}),
	0x8031D3E4: main.sym_fnc("L8031D3E4", flag={"GLOBL","LOCAL"}),
	0x8031D400: main.sym_fnc("L8031D400", flag={"GLOBL","LOCAL"}),
	0x8031D424: main.sym_fnc("L8031D424", flag={"GLOBL","LOCAL"}),
	0x8031D44C: main.sym_fnc("L8031D44C", flag={"GLOBL","LOCAL"}),
	0x8031D474: main.sym_fnc("L8031D474", flag={"GLOBL","LOCAL"}),
	0x8031D498: main.sym_fnc("L8031D498", flag={"GLOBL","LOCAL"}),
	0x8031D4BC: main.sym_fnc("L8031D4BC", flag={"GLOBL","LOCAL"}),
	0x8031D4D4: main.sym_fnc("L8031D4D4", flag={"GLOBL","LOCAL"}),
	0x8031D4F0: main.sym_fnc("L8031D4F0", flag={"GLOBL","LOCAL"}),
	0x8031D500: main.sym_fnc("L8031D500", flag={"GLOBL","LOCAL"}),
	0x8031D51C: main.sym_fnc("L8031D51C", flag={"GLOBL","LOCAL"}),
	0x8031D538: main.sym_fnc("L8031D538", flag={"GLOBL","LOCAL"}),
	0x8031D56C: main.sym_fnc("L8031D56C", flag={"GLOBL","LOCAL"}),
	0x8031D5A0: main.sym_fnc("L8031D5A0", flag={"GLOBL","LOCAL"}),
	0x8031D5B4: main.sym_fnc("L8031D5B4", flag={"GLOBL","LOCAL"}),
	0x8031D5D4: main.sym_fnc("L8031D5D4", flag={"GLOBL","LOCAL"}),
	0x8031D5E4: main.sym_fnc("L8031D5E4", flag={"GLOBL","LOCAL"}),
	0x8031D640: main.sym_fnc("L8031D640", flag={"GLOBL","LOCAL"}),
	0x8031D678: main.sym_fnc("L8031D678", flag={"GLOBL","LOCAL"}),
	0x8031D6C4: main.sym_fnc("L8031D6C4", flag={"GLOBL","LOCAL"}),
	0x8031D6D4: main.sym_fnc("L8031D6D4", flag={"GLOBL","LOCAL"}),
	0x8031D6F4: main.sym_fnc("L8031D6F4", flag={"GLOBL","LOCAL"}),
	0x8031D718: main.sym_fnc("L8031D718", flag={"GLOBL","LOCAL"}),
	0x8031D728: main.sym_fnc("L8031D728", flag={"GLOBL","LOCAL"}),
	0x8031D73C: main.sym_fnc("L8031D73C", flag={"GLOBL","LOCAL"}),
	0x8031D7B8: main.sym_fnc("L8031D7B8", flag={"GLOBL","LOCAL"}),
	0x8031D7E8: main.sym_fnc("L8031D7E8", flag={"GLOBL","LOCAL"}),
	0x8031D7F8: main.sym_fnc("L8031D7F8", flag={"GLOBL","LOCAL"}),
	0x8031D814: main.sym_fnc("L8031D814", flag={"GLOBL","LOCAL"}),
	0x8031D830: main.sym_fnc("L8031D830", flag={"GLOBL","LOCAL"}),
	0x8031D87C: main.sym_fnc("L8031D87C", flag={"GLOBL","LOCAL"}),
	0x8031D898: main.sym_fnc("L8031D898", flag={"GLOBL","LOCAL"}),
	0x8031D8F8: main.sym_fnc("L8031D8F8", flag={"GLOBL","LOCAL"}),
	0x8031D900: main.sym_fnc("L8031D900", flag={"GLOBL","LOCAL"}),
	0x8031D930: main.sym_fnc("L8031D930", flag={"GLOBL","LOCAL"}),
	0x8031D94C: main.sym_fnc("L8031D94C", flag={"GLOBL","LOCAL"}),
	0x8031D974: main.sym_fnc("L8031D974", flag={"GLOBL","LOCAL"}),
	0x8031D9EC: main.sym("Na_sequence_8031D9EC"),
	0x8031DC6C: main.sym_fnc("L8031DC6C", flag={"GLOBL","LOCAL"}),
	0x8031DD14: main.sym_fnc("L8031DD14", flag={"GLOBL","LOCAL"}),
	0x8031DD50: main.sym_fnc("L8031DD50", flag={"GLOBL","LOCAL"}),
	0x8031DD88: main.sym_fnc("L8031DD88", flag={"GLOBL","LOCAL"}),
	0x8031DDD0: main.sym_fnc("L8031DDD0", flag={"GLOBL","LOCAL"}),
	0x8031DE30: main.sym_fnc("L8031DE30", flag={"GLOBL","LOCAL"}),
	0x8031DE58: main.sym_fnc("L8031DE58", flag={"GLOBL","LOCAL"}),
	0x8031DE68: main.sym_fnc("L8031DE68", flag={"GLOBL","LOCAL"}),
	0x8031DE6C: main.sym_fnc("L8031DE6C", flag={"GLOBL","LOCAL"}),
	0x8031DE8C: main.sym_fnc("L8031DE8C", flag={"GLOBL","LOCAL"}),
	0x8031DF14: main.sym_fnc("L8031DF14", flag={"GLOBL","LOCAL"}),
	0x8031DFB0: main.sym_fnc("L8031DFB0", flag={"GLOBL","LOCAL"}),
	0x8031DFDC: main.sym_fnc("L8031DFDC", flag={"GLOBL","LOCAL"}),
	0x8031DFF8: main.sym_fnc("L8031DFF8", flag={"GLOBL","LOCAL"}),
	0x8031E014: main.sym_fnc("L8031E014", flag={"GLOBL","LOCAL"}),
	0x8031E03C: main.sym_fnc("L8031E03C", flag={"GLOBL","LOCAL"}),
	0x8031E04C: main.sym_fnc("L8031E04C", flag={"GLOBL","LOCAL"}),
	0x8031E05C: main.sym_fnc("L8031E05C", flag={"GLOBL","LOCAL"}),
	0x8031E090: main.sym_fnc("L8031E090", flag={"GLOBL","LOCAL"}),
	0x8031E0A0: main.sym_fnc("L8031E0A0", flag={"GLOBL","LOCAL"}),
	0x8031E0B0: main.sym_fnc("L8031E0B0", flag={"GLOBL","LOCAL"}),
	0x8031E0C0: main.sym_fnc("L8031E0C0", flag={"GLOBL","LOCAL"}),
	0x8031E194: main.sym_fnc("L8031E194", flag={"GLOBL","LOCAL"}),
	0x8031E1A0: main.sym_fnc("L8031E1A0", flag={"GLOBL","LOCAL"}),
	0x8031E1A8: main.sym_fnc("L8031E1A8", flag={"GLOBL","LOCAL"}),
	0x8031E1B0: main.sym_fnc("L8031E1B0", flag={"GLOBL","LOCAL"}),
	0x8031E240: main.sym("Na_sequence_8031E240", flag={"GLOBL"}),
	0x8031E2E8: main.sym("Na_sequence_8031E2E8", flag={"GLOBL"}),
	0x8031E374: main.sym("Na_sequence_8031E374", flag={"GLOBL"}),

	# src/audio/game.c
	0x8031E4F0: main.sym_fnc("Na_game_8031E4F0"), # unused
	0x8031E568: main.sym_fnc("Na_game_8031E568"), # unused
	0x8031E578: main.sym_fnc("Na_game_8031E578", arg=(
		"int",
		"int", #
	)),
	0x8031E5C0: main.sym_fnc("Na_game_8031E5C0", arg=(
		"int",
		"int", #
	)),
	0x8031E60C: main.sym_fnc("Na_game_8031E60C", arg=(
		"int",
		"int", #
		"u8",
	)),
	0x8031E6A4: main.sym_fnc("Na_game_8031E6A4", arg=(
		"int",
		"int", #
	)),
	0x8031E710: main.sym_fnc("Na_game_8031E710", arg=(
		"int",
		"int", #
		"u8",
	)),
	0x8031E7B8: main.sym_fnc("Na_Main", "SCTASK *", flag={"GLOBL"}), # ext
	0x8031EB00: main.sym_fnc("Na_SePlay", arg=(
		"Na_Se se",
		"f32 *pos",
	), flag={"GLOBL"}), # ext
	0x8031EB30: main.sym_fnc("Na_game_8031EB30", arg=(
		"Na_Se",
		"f32 *",
	)),
	0x8031EDEC: main.sym_fnc("Na_game_8031EDEC"),
	0x8031EE70: main.sym_fnc("Na_game_8031EE70", arg=(
		"u8",
		"u8",
	)),
	0x8031EF6C: main.sym_fnc("Na_game_8031EF6C", arg=(
		"u8",
		"u8",
	)),
	0x8031EFF4: main.sym_fnc("Na_game_8031EFF4", arg=(
		"u8",
	)),
	0x8031F810: main.sym_fnc("Na_game_8031F810", "float", (
		"float",
		"float",
	)),
	0x8031F96C: main.sym_fnc("Na_game_8031F96C", "float", (
		"u8",
		"u8",
		"float",
	)),
	0x8031FB20: main.sym_fnc("Na_game_8031FB20", "float", (
		"u8",
		"u8",
	)),
	0x8031FBE8: main.sym_fnc("Na_game_8031FBE8", "u8", (
		"u8",
		"u8",
		"u8",
	)),
	0x8031FD7C: main.sym_fnc("Na_game_8031FD7C"),
	0x8031FD84: main.sym_fnc("Na_Tick", flag={"GLOBL"}), # ext
	0x8031FDAC: main.sym_fnc("Na_game_8031FDAC"),
	0x8031FE4C: main.sym(".L8031FE4C", flag={"LOCAL"}),
	0x8031FE68: main.sym(".L8031FE68", flag={"LOCAL"}),
	0x8031FF5C: main.sym_fnc("L8031FF5C", flag={"GLOBL","LOCAL"}),
	0x803200B0: main.sym_fnc("L803200B0", flag={"GLOBL","LOCAL"}),
	0x803200D4: main.sym_fnc("L803200D4", flag={"GLOBL","LOCAL"}),
	0x80320138: main.sym_fnc("L80320138", flag={"GLOBL","LOCAL"}),
	0x8032026C: main.sym_fnc("L8032026C", flag={"GLOBL","LOCAL"}),
	0x803203BC: main.sym_fnc("L803203BC", flag={"GLOBL","LOCAL"}),
	0x803203DC: main.sym_fnc("L803203DC", flag={"GLOBL","LOCAL"}),
	0x80320440: main.sym_fnc("L80320440", flag={"GLOBL","LOCAL"}),
	0x80320544: main.sym_fnc("Na_game_80320544", arg=(
		"u8",
		"u8",
		"u16",
	)),
	0x80320678: main.sym_fnc("Na_SeqFadeout", arg=(
		"u8",
		"u16",
	), flag={"GLOBL"}), # ext
	0x803206BC: main.sym_fnc("Na_game_803206BC", arg=(
		"u8",
		"u8",
		"u16",
	), flag={"GLOBL"}), # ext
	0x80320734: main.sym_fnc("Na_game_80320734", arg=(
		"u8",
		"u8",
		"u8",
		"u16",
	)),
	0x8032080C: main.sym_fnc("Na_game_8032080C", arg=(
		"u8",
	)),
	0x803208EC: main.sym_fnc("Na_game_803208EC"),
	0x803209A8: main.sym(".L803209A8", flag={"LOCAL"}),
	0x80320A24: main.sym(".L80320A24", flag={"LOCAL"}),
	0x80320A4C: main.sym_fnc("L80320A4C", flag={"GLOBL","LOCAL"}),
	0x80320A8C: main.sym_fnc("L80320A8C", flag={"GLOBL","LOCAL"}),
	0x80320ACC: main.sym_fnc("L80320ACC", flag={"GLOBL","LOCAL"}),
	0x80320B0C: main.sym_fnc("L80320B0C", flag={"GLOBL","LOCAL"}),
	0x80320B4C: main.sym_fnc("L80320B4C", flag={"GLOBL","LOCAL"}),
	0x80320B8C: main.sym_fnc("L80320B8C", flag={"GLOBL","LOCAL"}),
	0x80320BCC: main.sym_fnc("L80320BCC", flag={"GLOBL","LOCAL"}),
	0x80320BF4: main.sym_fnc("L80320BF4", flag={"GLOBL","LOCAL"}),
	0x80320D70: main.sym_fnc("Na_game_80320D70", arg=(
		"u8",
		"u32",
		"s8",
	)), # unused
	0x80320E3C: main.sym_fnc("Na_SeqMute", arg=(
		"u8",
		"u16",
		"u8",
	), flag={"GLOBL"}), # ext
	0x80320EC4: main.sym_fnc("Na_SeqUnmute", arg=(
		"u8",
		"u16",
	), flag={"GLOBL"}), # ext
	0x80320F68: main.sym_fnc("Na_game_80320F68", "u8", (
		"u16",
	)),
	0x803210D4: main.sym_fnc("Na_Pause", arg=(
		"u8",
	), flag={"GLOBL"}), # ext
	0x8032112C: main.sym_fnc("Na_Init", flag={"GLOBL"}), # ext
	0x80321398: main.sym_fnc("Na_game_80321398", arg=(
		"u8",
		"u8 *",
		"u8 *",
		"u8 *",
	)), # unused
	0x80321474: main.sym_fnc("Na_SeStop", arg=(
		"u32",
		"f32 *",
	), flag={"GLOBL"}), # ext
	0x80321584: main.sym_fnc("Na_SeKill", arg=(
		"f32 *",
	), flag={"GLOBL"}), # ext
	0x80321668: main.sym_fnc("Na_game_80321668", arg=(
		"u8",
	)),
	0x8032171C: main.sym_fnc("Na_SeClear", flag={"GLOBL"}), # ext
	0x8032174C: main.sym_fnc("Na_PortLock", arg=(
		"u8",
		"u16",
	), flag={"GLOBL"}), # ext
	0x803217A8: main.sym_fnc("Na_game_803217A8"),
	0x8032180C: main.sym_fnc("Na_PortUnlock", arg=(
		"u8",
		"u16",
	), flag={"GLOBL"}), # ext
	0x80321864: main.sym_fnc("Na_game_80321864", "u8", (
		"u8",
		"u8",
		"u8",
	)), # unused
	0x803218D8: main.sym_fnc("Na_game_803218D8", arg=(
		"u8",
		"u8",
	), flag={"GLOBL"}), # ext
	0x803218F4: main.sym_fnc("Na_MessageSound", arg=(
		"u8",
	), flag={"GLOBL"}), # ext
	0x803219AC: main.sym_fnc("Na_BgmPlay", arg=(
		"u8",
		"u16",
		"u16",
	), flag={"GLOBL"}), # ext
	0x80321BAC: main.sym_fnc("Na_BgmStop", arg=(
		"u16",
	), flag={"GLOBL"}), # ext
	0x80321CE4: main.sym_fnc("Na_BgmFadeout", arg=(
		"u16",
		"u16",
	), flag={"GLOBL"}), # ext
	0x80321D38: main.sym_fnc("Na_game_80321D38", flag={"GLOBL"}), # ext
	0x80321D5C: main.sym_fnc("Na_BgmGet", "u16", flag={"GLOBL"}), # ext
	0x80321D9C: main.sym_fnc("Na_game_80321D9C"),
	0x80321E48: main.sym_fnc("Na_SeqPush", arg=(
		"u8",
		"u8",
		"u8",
		"u16",
	), flag={"GLOBL"}), # ext
	0x80321F48: main.sym_fnc("Na_SeqPull", arg=(
		"u16",
	), flag={"GLOBL"}), # ext
	0x80321F9C: main.sym_fnc("Na_Fadeout", arg=(
		"u16",
	), flag={"GLOBL"}), # ext
	0x80322078: main.sym_fnc("Na_StarCatch", flag={"GLOBL"}), # ext
	0x803220B4: main.sym_fnc("Na_PeachMessage", flag={"GLOBL"}), # ext
	0x803220F0: main.sym_fnc("Na_Solution", flag={"GLOBL"}), # ext
	0x8032212C: main.sym_fnc("Na_HiScore", flag={"GLOBL"}), # ext
	0x80322168: main.sym_fnc("Na_StarAppear", arg=(
		"u8",
	), flag={"GLOBL"}), # ext
	0x803221B8: main.sym_fnc("Na_Fanfare", flag={"GLOBL"}), # ext
	0x803221F4: main.sym_fnc("Na_ToadMessage", flag={"GLOBL"}), # ext
	0x80322230: main.sym_fnc("Na_SetMode", arg=(
		"u8",
	), flag={"GLOBL"}), # ext
	0x8032231C: main.sym_fnc("Na_SetOutput", arg=(
		"int",
	), flag={"GLOBL"}), # ext
	0x80322348: main.sym_fnc("Na_game_80322348", arg=(
		"int",
		"int",
		"int",
		"int",
	)), # unused
	0x8032235C: main.sym_fnc("Na_game_8032235C", arg=(
		"int",
	)), # unused

	# os/settime.c
	0x803223B0: main.sym_fnc("osSetTime", arg=(
		"OSTime ticks",
	), flag={"GLOBL"}),

	# os/maptlb.s
	0x803223E0: main.sym_fnc("osMapTLB", arg=(
		"s32",
		"OSPageMask",
		"void *",
		"u32",
		"u32",
		"s32",
	), flag={"GLOBL"}),

	# os/unmaptlball.s
	0x803224A0: main.sym_fnc("osUnmapTLBAll", flag={"GLOBL"}),

	# rmon/sprintf.c
	0x803224F0: main.sym_fnc("sprintf", "int", (
		"char *s",
		"const char *fmt",
		"...",
	), flag={"GLOBL"}),
	0x8032255C: main.sym_fnc("proutSprintf", "void *", (
		"void *s",
		"const char *buf",
		"size_t n",
	)),

	# os/createmesgqueue.c
	0x803225A0: main.sym_fnc("osCreateMesgQueue", arg=(
		"OSMesgQueue *mq",
		"OSMesg *msg",
		"s32 msgCount",
	), flag={"GLOBL"}),

	# os/seteventmesg.c
	0x803225D0: main.sym_fnc("osSetEventMesg", arg=(
		"OSEvent e",
		"OSMesgQueue *mq",
		"OSMesg m",
	), flag={"GLOBL"}),

	# io/visetevent.c
	0x80322640: main.sym_fnc("osViSetEvent", arg=(
		"OSMesgQueue *mq",
		"OSMesg msg",
		"u32 retraceCount",
	), flag={"GLOBL"}),

	# os/createthread.c
	0x803226B0: main.sym_fnc("osCreateThread", arg=(
		"OSThread *t",
		"OSId id",
		"void (*entry)(void *)",
		"void *arg",
		"void *sp",
		"OSPri p",
	), flag={"GLOBL"}),

	# os/recvmesg.c
	0x80322800: main.sym_fnc("osRecvMesg", "s32", (
		"OSMesgQueue *mq",
		"OSMesg *msg",
		"s32 flags",
	), flag={"GLOBL"}),

	# io/sptask.c
	0x80322940: main.sym_fnc("_VirtualToPhysicalTask", "OSTask *", (
		"OSTask *intp",
	)),
	0x80322A5C: main.sym_fnc("osSpTaskLoad", arg=(
		"OSTask *intp",
	), flag={"GLOBL"}),
	0x80322BBC: main.sym_fnc("osSpTaskStartGo", arg=(
		"OSTask *tp",
	), flag={"GLOBL"}),

	# io/sptaskyield.c
	0x80322C00: main.sym_fnc("osSpTaskYield", flag={"GLOBL"}),

	# os/sendmesg.c
	0x80322C20: main.sym_fnc("osSendMesg", arg=(
		"OSMesgQueue *mq",
		"OSMesg msg",
		"s32 flags",
	), flag={"GLOBL"}),

	# io/sptaskyielded.c
	0x80322D70: main.sym_fnc("osSpTaskYielded", "OSYieldResult", (
		"OSTask *tp",
	), flag={"GLOBL"}),

	# os/startthread.c
	0x80322DF0: main.sym_fnc("osStartThread", arg=(
		"OSThread *t",
	), flag={"GLOBL"}),

	# os/writebackdcacheall.s
	0x80322F40: main.sym_fnc("osWritebackDCacheAll", flag={"GLOBL"}),

	# io/vimgr.c
	0x80322F70: main.sym_fnc("osCreateViManager", arg=(
		"OSPri pri",
	), flag={"GLOBL"}),
	0x803230F4: main.sym("viMgrMain"),

	# io/visetmode.c
	0x803232D0: main.sym_fnc("osViSetMode", arg=(
		"OSViMode *modep",
	), flag={"GLOBL"}),

	# io/viblack.c
	0x80323340: main.sym_fnc("osViBlack", arg=(
		"u8 active",
	), flag={"GLOBL"}),

	# io/visetspecial.c
	0x803233B0: main.sym_fnc("osViSetSpecialFeatures", arg=(
		"u32 func",
	), flag={"GLOBL"}),

	# io/pimgr.c
	0x80323570: main.sym_fnc("osCreatePiManager", arg=(
		"OSPri pri",
		"OSMesgQueue *cmdQ",
		"OSMesg *cmdBuf",
		"s32 cmdMsgCnt",
	), flag={"GLOBL"}),

	# os/setthreadpri.c
	0x803236F0: main.sym_fnc("osSetThreadPri", arg=(
		"OSThread *t",
		"OSPri p",
	), flag={"GLOBL"}),

	# os/initialize.c
	0x803237D0: main.sym_fnc("osInitialize", flag={"GLOBL"}),

	# io/viswapbuf.c
	0x80323A00: main.sym_fnc("osViSwapBuffer", arg=(
		"void *frameBufPtr",
	), flag={"GLOBL"}),

	# gu/sqrtf.s
	0x80323A50: main.sym_fnc("sqrtf", "float", arg=(
		"float",
	), flag={"GLOBL"}),

	# io/contreaddata.c
	0x80323A60: main.sym_fnc("osContStartReadData", "s32", (
		"OSMesgQueue *mq",
	), flag={"GLOBL"}),
	0x80323B24: main.sym_fnc("osContGetReadData", arg=(
		"OSContPad *data",
	), flag={"GLOBL"}),
	0x80323BCC: main.sym_fnc("__osPackReadData"),

	# io/controller.c
	0x80323CC0: main.sym_fnc("osContInit", "s32", (
		"OSMesgQueue *mq",
		"u8 *bitpattern",
		"OSContStatus *data",
	), flag={"GLOBL"}),
	0x80323EBC: main.sym_fnc("__osContGetInitData", arg=(
		"u8 *pattern",
		"OSContStatus *data",
	), flag={"GLOBL"}), # static
	0x80323F8C: main.sym_fnc("__osPackRequestData", arg=(
		"u8 cmd",
	), flag={"GLOBL"}), # static

	# io/conteepprobe.c
	0x80324080: main.sym_fnc("osEepromProbe", "s32", (
		"OSMesgQueue *mq",
	), flag={"GLOBL"}),

	# libc/ll.c
	0x803240F0: main.sym("__ull_rshift", flag={"GLOBL"}), # unused
	0x8032411C: main.sym("__ull_rem", flag={"GLOBL"}),
	0x80324158: main.sym("__ull_div", flag={"GLOBL"}),
	0x80324194: main.sym("__ll_lshift", flag={"GLOBL"}),
	0x803241C0: main.sym("__ll_rem", flag={"GLOBL"}), # unused
	0x803241FC: main.sym("__ll_div", flag={"GLOBL"}),
	0x80324258: main.sym("__ll_mul", flag={"GLOBL"}),
	0x80324288: main.sym("__ull_divremi", flag={"GLOBL"}), # unused
	0x803242E8: main.sym("__ll_mod", flag={"GLOBL"}), # unused
	0x80324384: main.sym("__ll_rshift", flag={"GLOBL"}), # unused

	# os/invaldcache.s
	0x803243B0: main.sym_fnc("osInvalDCache", arg=(
		"void *",
		"s32",
	), flag={"GLOBL"}),

	# io/pidma.c
	0x80324460: main.sym_fnc("osPiStartDma", arg=(
		"OSIoMesg *mb",
		"s32 priority",
		"s32 direction",
		"u32 devAddr",
		"void *dramAddr",
		"u32 size",
		"OSMesgQueue *mq",
	), flag={"GLOBL"}),

	# libc/bzero.s
	0x80324570: main.sym_fnc("bzero", arg=(
		"void *",
		"int",
	), flag={"GLOBL"}),
	0x80324590: main.sym("blkzero", flag={"LOCAL"}),
	0x803245CC: main.sym("wordzero", flag={"LOCAL"}),
	0x803245EC: main.sym("bytezero", flag={"LOCAL"}),
	0x80324604: main.sym("zerodone", flag={"LOCAL"}),

	# os/invalicache.s
	0x80324610: main.sym_fnc("osInvalICache", arg=(
		"void *",
		"s32",
	), flag={"GLOBL"}),

	# io/conteeplongread.c
	0x80324690: main.sym_fnc("osEepromLongRead", arg=(
		"OSMesgQueue *mq",
		"u8 address",
		"u8 *buffer",
		"int length",
	), flag={"GLOBL"}),

	# io/conteeplongwrite.c
	0x803247D0: main.sym_fnc("osEepromLongWrite", arg=(
		"OSMesgQueue *mq",
		"u8 address",
		"u8 *buffer",
		"int length",
	), flag={"GLOBL"}),

	# libc/bcopy.s
	0x80324910: main.sym_fnc("bcopy", arg=(
		"const void *",
		"void *",
		"int",
	), flag={"GLOBL"}),
	0x80324940: main.sym("goforwards", flag={"LOCAL"}),
	0x80324944: main.sym("goforwards.L", flag={"LOCAL"}),
	0x8032495C: main.sym("forwards_bytecopy", flag={"LOCAL"}),
	0x8032497C: main.sym("ret", flag={"LOCAL"}),
	0x80324984: main.sym("forwalignable", flag={"LOCAL"}),
	0x803249B4: main.sym("forw_copy2", flag={"LOCAL"}),
	0x803249B8: main.sym("forw_copy2.L", flag={"LOCAL"}),
	0x803249CC: main.sym("forw_copy3", flag={"LOCAL"}),
	0x803249E8: main.sym("forwards_32", flag={"LOCAL"}),
	0x80324A44: main.sym("forwards_16", flag={"LOCAL"}),
	0x80324A48: main.sym("forwards_16.L", flag={"LOCAL"}),
	0x80324A80: main.sym("forwards_4", flag={"LOCAL"}),
	0x80324A84: main.sym("forwards_4.L", flag={"LOCAL"}),
	0x80324AA4: main.sym("gobackwards", flag={"LOCAL"}),
	0x80324AA8: main.sym("gobackwards.L", flag={"LOCAL"}),
	0x80324AC4: main.sym("backwards_bytecopy", flag={"LOCAL"}),
	0x80324AF4: main.sym("backalignable", flag={"LOCAL"}),
	0x80324B24: main.sym("back_copy2", flag={"LOCAL"}),
	0x80324B28: main.sym("back_copy2.L", flag={"LOCAL"}),
	0x80324B3C: main.sym("back_copy3", flag={"LOCAL"}),
	0x80324B58: main.sym("backwards_32", flag={"LOCAL"}),
	0x80324BB4: main.sym("backwards_16", flag={"LOCAL"}),
	0x80324BB8: main.sym("backwards_16.L", flag={"LOCAL"}),
	0x80324BF0: main.sym("backwards_4", flag={"LOCAL"}),
	0x80324BF4: main.sym("backwards_4.L", flag={"LOCAL"}),

	# gu/ortho.c
	0x80324C20: main.sym_fnc("guOrthoF", arg=(
		"float mf[4][4]",
		"float l",
		"float r",
		"float b",
		"float t",
		"float n",
		"float f",
		"float scale",
	), flag={"GLOBL"}),
	0x80324D74: main.sym_fnc("guOrtho", arg=(
		"Mtx *m",
		"float l",
		"float r",
		"float b",
		"float t",
		"float n",
		"float f",
		"float scale",
	), flag={"GLOBL"}),

	# gu/perspective.c
	0x80324DE0: main.sym_fnc("guPerspectiveF", arg=(
		"float mf[4][4]",
		"u16 *perspNorm",
		"float fovy",
		"float aspect",
		"float near",
		"float far",
		"float scale",
	), flag={"GLOBL"}),
	0x80325010: main.sym_fnc("guPerspective", arg=(
		"Mtx *m",
		"u16 *perspNorm",
		"float fovy",
		"float aspect",
		"float near",
		"float far",
		"float scale",
	), flag={"GLOBL"}),

	# os/gettime.c
	0x80325070: main.sym_fnc("osGetTime", "OSTime", flag={"GLOBL"}),

	# libc/llcvt.c
	0x80325100: main.sym("__d_to_ll", flag={"GLOBL"}), # unused
	0x8032511C: main.sym("__f_to_ll", flag={"GLOBL"}), # unused
	0x80325138: main.sym("__d_to_ull", flag={"GLOBL"}),
	0x803251D8: main.sym("__f_to_ull", flag={"GLOBL"}), # unused
	0x80325274: main.sym("__ll_to_d", flag={"GLOBL"}), # unused
	0x8032528C: main.sym("__ll_to_f", flag={"GLOBL"}), # unused
	0x803252A4: main.sym("__ull_to_d", flag={"GLOBL"}),
	0x803252D8: main.sym("__ull_to_f", flag={"GLOBL"}), # unused

	# gu/cosf.c
	0x80325310: main.sym_fnc("cosf", "float", (
		"float x",
	), flag={"GLOBL"}),

	# gu/sinf.c
	0x80325480: main.sym_fnc("sinf", "float", (
		"float x",
	), flag={"GLOBL"}),

	# gu/translate.c
	0x80325640: main.sym_fnc("guTranslateF", arg=(
		"float mf[4][4]",
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}), # unused
	0x80325688: main.sym_fnc("guTranslate", arg=(
		"Mtx *m",
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}),

	# gu/rotate.c
	0x803256E0: main.sym_fnc("guRotateF", arg=(
		"float mf[4][4]",
		"float a",
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}),
	0x80325874: main.sym_fnc("guRotate", arg=(
		"Mtx *m",
		"float a",
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}),

	# gu/scale.c
	0x803258D0: main.sym_fnc("guScaleF", arg=(
		"float mf[4][4]",
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}),
	0x80325924: main.sym_fnc("guScale", arg=(
		"Mtx *m",
		"float x",
		"float y",
		"float z",
	), flag={"GLOBL"}),

	# io/aisetfreq.c
	0x80325970: main.sym_fnc("osAiSetFrequency", arg=(
		"u32 frequency",
	), flag={"GLOBL"}),

	# audio/bnkf.c
	0x80325AD0: main.sym("_bnkfPatchWaveTable"), # unused
	0x80325AD8: main.sym("_bnkfPatchSound"), # unused
	0x80325AE0: main.sym("_bnkfPatchInst"),
	0x80325BD4: main.sym_fnc("alBnkfNew", arg=(
		"ALBankFile *file",
		"u8 *table",
	), flag={"GLOBL"}), # unused
	0x80325BCC: main.sym("_bnkfPatchBank"), # unused
	0x80325CD8: main.sym_fnc("alSeqFileNew", arg=(
		"ALSeqFile *file",
		"u8 *base",
	), flag={"GLOBL"}),

	# os/writebackdcache.s
	0x80325D20: main.sym_fnc("osWritebackDCache", arg=(
		"void *",
		"s32",
	), flag={"GLOBL"}),

	# io/aigetlen.c
	0x80325DA0: main.sym_fnc("osAiGetLength", "u32", flag={"GLOBL"}),

	# io/aisetnextbuf.c
	0x80325DB0: main.sym_fnc("osAiSetNextBuffer", "s32", (
		"void *bufPtr",
		"u32 size",
	), flag={"GLOBL"}),

	# os/timerintr.c
	0x80325E60: main.sym("__osTimerServicesInit", flag={"GLOBL"}),
	0x80325EEC: main.sym("__osTimerInterrupt", flag={"GLOBL"}),
	0x80326064: main.sym("__osSetTimerIntr", flag={"GLOBL"}),
	0x803260D8: main.sym("__osInsertTimer", flag={"GLOBL"}),

	# rmon/xprintf.c
	0x80326260: main.sym_fnc("_Printf", "int", (
		"void *(*pfn)(void *, const char *, size_t)",
		"void *arg",
		"const char *fmt",
		"va_list ap",
	), flag={"GLOBL"}),
	0x80326A8C: main.sym("_Putfld"),
	0x80326B40: main.sym_fnc("L80326B40", flag={"GLOBL","LOCAL"}),
	0x80326B90: main.sym_fnc("L80326B90", flag={"GLOBL","LOCAL"}),
	0x80326D90: main.sym_fnc("L80326D90", flag={"GLOBL","LOCAL"}),
	0x80326F74: main.sym_fnc("L80326F74", flag={"GLOBL","LOCAL"}),
	0x8032717C: main.sym_fnc("L8032717C", flag={"GLOBL","LOCAL"}),
	0x803272A4: main.sym_fnc("L803272A4", flag={"GLOBL","LOCAL"}),
	0x80327308: main.sym_fnc("L80327308", flag={"GLOBL","LOCAL"}),
	0x803273A0: main.sym_fnc("L803273A0", flag={"GLOBL","LOCAL"}),

	# libc/string.c
	0x803273F0: main.sym_fnc("memcpy", "void *", (
		"void *s1",
		"const void *s2",
		"size_t n",
	), flag={"GLOBL"}),
	0x8032741C: main.sym_fnc("strlen", "size_t", (
		"const char *s",
	), flag={"GLOBL"}),
	0x80327444: main.sym_fnc("strchr", "const char *", (
		"const char *s",
		"int c",
	), flag={"GLOBL"}),

	# os/thread.c
	0x80327490: main.sym("__osDequeueThread", flag={"GLOBL"}),

	# os/interrupt.s
	0x803274D0: main.sym("__osDisableInt", flag={"GLOBL"}),
	0x803274F0: main.sym("__osRestoreInt", flag={"GLOBL"}),

	# io/vi.c
	0x80327510: main.sym("__osViInit", flag={"GLOBL"}),

	# os/exceptasm.s
	0x80327640: main.sym("__osExceptionPreamble", flag={"GLOBL"}),
	0x80327650: main.sym("__osException", flag={"GLOBL"}),
	0x803276B4: main.sym("notIP7", flag={"LOCAL"}),
	0x803276D0: main.sym("savecontext", flag={"LOCAL"}),
	0x80327834: main.sym("no_kdebug", flag={"LOCAL"}),
	0x80327880: main.sym("no_rdb_mesg", flag={"LOCAL"}),
	0x803278A8: main.sym("handle_interrupt"),
	0x803278AC: main.sym("next_interrupt", flag={"LOCAL"}),
	0x803278E4: main.sym("counter"),
	0x80327904: main.sym("cart"),
	0x80327938: main.sym("rcp"),
	0x80327988: main.sym("sp_other_break", flag={"LOCAL"}),
	0x80327998: main.sym("vi", flag={"LOCAL"}),
	0x803279BC: main.sym("ai", flag={"LOCAL"}),
	0x803279E8: main.sym("si", flag={"LOCAL"}),
	0x80327A0C: main.sym("pi", flag={"LOCAL"}),
	0x80327A38: main.sym("dp", flag={"LOCAL"}),
	0x80327A5C: main.sym("NoMoreRcpInts", flag={"LOCAL"}),
	0x80327A68: main.sym("prenmi"),
	0x80327A94: main.sym("firstnmi", flag={"LOCAL"}),
	0x80327AC4: main.sym("sw2"),
	0x80327AE4: main.sym("sw1"),
	0x80327B04: main.sym("handle_break"),
	0x80327B1C: main.sym("redispatch"),
	0x80327B50: main.sym("enqueueRunning", flag={"LOCAL"}),
	0x80327B68: main.sym("panic"),
	0x80327B98: main.sym("send_mesg", flag={"GLOBL"}),
	0x80327C44: main.sym("send_done", flag={"LOCAL"}),
	0x80327C4C: main.sym("handle_CpU", flag={"GLOBL"}),
	0x80327C80: main.sym("__osEnqueueAndYield", flag={"GLOBL"}),
	0x80327D08: main.sym("noEnqueue", flag={"LOCAL"}),
	0x80327D10: main.sym("__osEnqueueThread", flag={"GLOBL"}),
	0x80327D58: main.sym("__osPopThread", flag={"GLOBL"}),
	0x80327D68: main.sym("__osDispatchThread", flag={"GLOBL"}),
	0x80327D88: main.sym("__osDispatchThreadSave", flag={"LOCAL"}),
	0x80327EA8: main.sym("__osCleanupThread", flag={"GLOBL"}),

	# os/virtualtophysical.c
	0x80327EB0: main.sym_fnc("osVirtualToPhysical", "u32", (
		"void *virtualAddress",
	), flag={"GLOBL"}),

	# io/spsetstat.c
	0x80327F30: main.sym("__osSpSetStatus", flag={"GLOBL"}),

	# io/spsetpc.c
	0x80327F40: main.sym("__osSpSetPc", flag={"GLOBL"}),

	# io/sprawdma.c
	0x80327F80: main.sym("__osSpRawStartDma", flag={"GLOBL"}),

	# io/sp.c
	0x80328010: main.sym("__osSpDeviceBusy", flag={"GLOBL"}),

	# io/spgetstat.c
	0x80328040: main.sym("__osSpGetStatus", flag={"GLOBL"}),

	# os/getthreadpri.c
	0x80328050: main.sym_fnc("osGetThreadPri", "OSPri", (
		"OSThread *t",
	), flag={"GLOBL"}),

	# io/vigetcurrcontext.c
	0x80328070: main.sym("__osViGetCurrentContext", flag={"GLOBL"}),

	# io/viswapcontext.c
	0x80328080: main.sym("__osViSwapContext", flag={"GLOBL"}),

	# os/getcount.s
	0x803283E0: main.sym_fnc("osGetCount", "u32", flag={"GLOBL"}),

	# io/piacs.c
	0x803283F0: main.sym("__osPiCreateAccessQueue", flag={"GLOBL"}),
	0x80328440: main.sym("__osPiGetAccess", flag={"GLOBL"}), # unused
	0x80328484: main.sym("__osPiRelAccess", flag={"GLOBL"}), # unused

	# io/pirawdma.c
	0x803284B0: main.sym("osPiRawStartDma", flag={"GLOBL"}),

	# io/devmgr.c
	0x80328590: main.sym("__osDevMgrMain", flag={"GLOBL"}),

	# os/setsr.s
	0x80328710: main.sym_fnc("__osSetSR", arg=(
		"u32",
	), flag={"GLOBL"}),

	# os/getsr.s
	0x80328720: main.sym_fnc("__osGetSR", "u32", flag={"GLOBL"}),

	# os/setfpccsr.s
	0x80328730: main.sym_fnc("__osSetFpcCsr", "u32", (
		"u32",
	), flag={"GLOBL"}),

	# io/sirawread.c
	0x80328740: main.sym("__osSiRawReadIo", flag={"GLOBL"}),

	# io/sirawwrite.c
	0x80328790: main.sym("__osSiRawWriteIo", flag={"GLOBL"}),

	# os/maptlbrdb.s
	0x803287E0: main.sym_fnc("osMapTLBRdb", flag={"GLOBL"}),

	# io/pirawread.c
	0x80328840: main.sym_fnc("osPiRawReadIo", "s32", (
		"u32 devAddr",
		"u32 *data",
	), flag={"GLOBL"}),

	# io/siacs.c
	0x803288A0: main.sym("__osSiCreateAccessQueue", flag={"GLOBL"}),
	0x803288F0: main.sym("__osSiGetAccess", flag={"GLOBL"}),
	0x80328934: main.sym("__osSiRelAccess", flag={"GLOBL"}),

	# io/sirawdma.c
	0x80328960: main.sym("__osSiRawStartDma", flag={"GLOBL"}),

	# os/settimer.c
	0x80328A10: main.sym_fnc("osSetTimer", arg=(
		"OSTimer *timer",
		"OSTime value",
		"OSTime interval",
		"OSMesgQueue *mq",
		"OSMesg msg",
	), flag={"GLOBL"}),

	# io/conteepwrite.c
	0x80328AF0: main.sym_fnc("osEepromWrite", arg=(
		"OSMesgQueue *mq",
		"u8 address",
		"u8 *buffer",
	), flag={"GLOBL"}),
	0x80328CA0: main.sym_fnc("__osPackEepWriteData", arg=(
		"u8 address",
		"u8 *buffer",
	)),
	0x80328DAC: main.sym_fnc("__osEepStatus", "s32", (
		"OSMesgQueue *mq",
		"OSContStatus *data",
	), flag={"GLOBL"}),

	# os/jammesg.c
	0x80328FD0: main.sym_fnc("osJamMesg", arg=(
		"OSMesgQueue *mq",
		"OSMesg msg",
		"s32 flags",
	), flag={"GLOBL"}),

	# io/pigetcmdq.c
	0x80329120: main.sym_fnc("osPiGetCmdQueue", "OSMesgQueue *", flag={"GLOBL"}),

	# io/conteepread.c
	0x80329150: main.sym_fnc("osEepromRead", arg=(
		"OSMesgQueue *mq",
		"u8 address",
		"u8 *buffer",
	), flag={"GLOBL"}),
	0x80329340: main.sym_fnc("__osPackEepReadData", arg=(
		"u8 address",
	)),

	# gu/mtxutil.c
	0x80329450: main.sym_fnc("guMtxF2L", arg=(
		"float mf[4][4]",
		"Mtx *m",
	), flag={"GLOBL"}),
	0x80329550: main.sym_fnc("guMtxIdentF", arg=(
		"float mf[4][4]",
	), flag={"GLOBL"}),
	0x803295D8: main.sym_fnc("guMtxIdent", arg=(
		"Mtx *m",
	), flag={"GLOBL"}), # unused
	0x80329608: main.sym_fnc("guMtxL2F", arg=(
		"float mf[4][4]",
		"Mtx *m",
	), flag={"GLOBL"}), # unused

	# gu/normalize.c
	0x803296C0: main.sym_fnc("guNormalize", arg=(
		"float *x",
		"float *y",
		"float *z",
	), flag={"GLOBL"}),

	# io/ai.c
	0x80329750: main.sym("__osAiDeviceBusy", flag={"GLOBL"}),

	# os/setcompare.s
	0x80329780: main.sym_fnc("__osSetCompare", arg=(
		"u32",
	), flag={"GLOBL"}),

	# rmon/xlitob.c
	0x80329790: main.sym("_Litob", flag={"GLOBL"}),

	# rmon/xldtob.c
	0x80329A90: main.sym("_Ldtob", flag={"GLOBL"}),
	0x8032A090: main.sym("_Ldunscale"),
	0x8032A170: main.sym("_Genld"),

	# os/kdebugserver.c
	0x8032A860: main.sym("u32_to_string"), # unused
	0x8032A890: main.sym("string_to_u32"),
	0x8032A8E8: main.sym("send_packet"),
	0x8032A9A8: main.sym("send"),
	0x8032AA80: main.sym("process_command_memory"),
	0x8032AACC: main.sym("process_command_register"),
	0x8032AAF8: main.sym("kdebugserver", flag={"GLOBL"}),

	# os/syncputchars.c
	0x8032ACE0: main.sym("__osSyncPutChars", flag={"GLOBL"}), # unused

	# os/setintmask.s
	0x8032AE10: main.sym_fnc("osSetIntMask", "OSIntMask", (
		"OSIntMask",
	), flag={"GLOBL"}), # unused

	# os/destroythread.c
	0x8032AE70: main.sym_fnc("osDestroyThread", arg=(
		"OSThread *t",
	), flag={"GLOBL"}),

	# os/probetlb.s
	0x8032AF70: main.sym("__osProbeTLB", flag={"GLOBL"}),

	# io/si.c
	0x8032B030: main.sym("__osSiDeviceBusy", flag={"GLOBL"}),

	# libc/ldiv.c
	0x8032B060: main.sym("lldiv", flag={"GLOBL"}),
	0x8032B160: main.sym("ldiv", flag={"GLOBL"}),

	# os/getcause.s
	0x8032B1F0: main.sym_fnc("__osGetCause", "u32", flag={"GLOBL"}),

	# os/atomic.c
	0x8032B200: main.sym("__osAtomicDec", flag={"GLOBL"}),

	# ==========================================================================
	# data
	# ==========================================================================

	0x8032D5F8: main.sym("demo_rec+0x00"), # count
	0x8032D5F9: main.sym("demo_rec+0x01"), # stick_x
	0x8032D5FA: main.sym("demo_rec+0x02"), # stick_y
	0x8032D5FB: main.sym("demo_rec+0x03"), # button

	0x8032D950: main.sym("collisiontab+0x00"), # type
	0x8032D954: main.sym("collisiontab+0x04"), # proc

	0x8032DADB: main.sym("pl_unpresstab+1*15"),
	0x8032DAE0: main.sym("pl_flash_pattern+0"),
	0x8032DAE4: main.sym("pl_flash_pattern+4"),

	0x8032DBE2: main.sym("pldemo_8032DC3C-1*90"),
	0x8032DC36: main.sym("pldemo_8032DC34+2"),
	0x8032DC3A: main.sym("pldemo_8032DC38+2"),

	0x8032DD97: main.sym("coursetab-1"),

	0x8032F4D4: main.sym("camdemo_8032F4D4+0x00"), # callback
	0x8032F4D8: main.sym("camdemo_8032F4D4+0x04"), # time
	0x8032F534: main.sym("camdemo_8032F534+0x00"), # callback
	0x8032F538: main.sym("camdemo_8032F534+0x04"), # time
	0x8032F544: main.sym("camdemo_8032F544+0x00"), # callback
	0x8032F548: main.sym("camdemo_8032F544+0x04"), # time
	0x8032F554: main.sym("camdemo_8032F554+0x00"), # callback
	0x8032F558: main.sym("camdemo_8032F554+0x04"), # time
	0x8032F564: main.sym("camdemo_8032F564+0x00"), # callback
	0x8032F568: main.sym("camdemo_8032F564+0x04"), # time
	0x8032F56C: main.sym("camdemo_8032F56C+0x00"), # callback
	0x8032F570: main.sym("camdemo_8032F56C+0x04"), # time
	0x8032F574: main.sym("camdemo_8032F574+0x00"), # callback
	0x8032F578: main.sym("camdemo_8032F574+0x04"), # time
	0x8032F59C: main.sym("camdemo_8032F59C+0x00"), # callback
	0x8032F5A0: main.sym("camdemo_8032F59C+0x04"), # time
	0x8032F5C4: main.sym("camdemo_8032F5C4+0x00"), # callback
	0x8032F5C8: main.sym("camdemo_8032F5C4+0x04"), # time
	0x8032F5DC: main.sym("camdemo_8032F5DC+0x00"), # callback
	0x8032F5E0: main.sym("camdemo_8032F5DC+0x04"), # time
	0x8032F5F4: main.sym("camdemo_8032F5F4+0x00"), # callback
	0x8032F5F8: main.sym("camdemo_8032F5F4+0x04"), # time
	0x8032F60C: main.sym("camdemo_8032F60C+0x00"), # callback
	0x8032F610: main.sym("camdemo_8032F60C+0x04"), # time
	0x8032F624: main.sym("camdemo_8032F624+0x00"), # callback
	0x8032F628: main.sym("camdemo_8032F624+0x04"), # time
	0x8032F634: main.sym("camdemo_8032F634+0x00"), # callback
	0x8032F638: main.sym("camdemo_8032F634+0x04"), # time
	0x8032F63C: main.sym("camdemo_8032F63C+0x00"), # callback
	0x8032F640: main.sym("camdemo_8032F63C+0x04"), # time
	0x8032F64C: main.sym("camdemo_8032F64C+0x00"), # callback
	0x8032F650: main.sym("camdemo_8032F64C+0x04"), # time
	0x8032F65C: main.sym("camdemo_8032F65C+0x00"), # callback
	0x8032F660: main.sym("camdemo_8032F65C+0x04"), # time
	0x8032F674: main.sym("camdemo_8032F674+0x00"), # callback
	0x8032F678: main.sym("camdemo_8032F674+0x04"), # time
	0x8032F69C: main.sym("camdemo_8032F69C+0x00"), # callback
	0x8032F6A0: main.sym("camdemo_8032F69C+0x04"), # time
	0x8032F6AC: main.sym("camdemo_8032F6AC+0x00"), # callback
	0x8032F6B0: main.sym("camdemo_8032F6AC+0x04"), # time
	0x8032F6BC: main.sym("camdemo_8032F6BC+0x00"), # callback
	0x8032F6C0: main.sym("camdemo_8032F6BC+0x04"), # time
	0x8032F6CC: main.sym("camdemo_8032F6CC+0x00"), # callback
	0x8032F6D0: main.sym("camdemo_8032F6CC+0x04"), # time
	0x8032F6DC: main.sym("camdemo_8032F6DC+0x00"), # callback
	0x8032F6E0: main.sym("camdemo_8032F6DC+0x04"), # time
	0x8032F6F4: main.sym("camdemo_8032F6F4+0x00"), # callback
	0x8032F6F8: main.sym("camdemo_8032F6F4+0x04"), # time
	0x8032F6FC: main.sym("camdemo_8032F6FC+0x00"), # callback
	0x8032F700: main.sym("camdemo_8032F6FC+0x04"), # time
	0x8032F70C: main.sym("camdemo_8032F70C+0x00"), # callback
	0x8032F710: main.sym("camdemo_8032F70C+0x04"), # time
	0x8032F714: main.sym("camdemo_8032F714+0x00"), # callback
	0x8032F718: main.sym("camdemo_8032F714+0x04"), # time
	0x8032F71C: main.sym("camdemo_8032F71C+0x00"), # callback
	0x8032F720: main.sym("camdemo_8032F71C+0x04"), # time
	0x8032F72C: main.sym("camdemo_8032F72C+0x00"), # callback
	0x8032F730: main.sym("camdemo_8032F72C+0x04"), # time
	0x8032F734: main.sym("camdemo_8032F734+0x00"), # callback
	0x8032F738: main.sym("camdemo_8032F734+0x04"), # time
	0x8032F74C: main.sym("camdemo_8032F74C+0x00"), # callback
	0x8032F750: main.sym("camdemo_8032F74C+0x04"), # time
	0x8032F754: main.sym("camdemo_8032F754+0x00"), # callback
	0x8032F758: main.sym("camdemo_8032F754+0x04"), # time
	0x8032F75C: main.sym("camdemo_8032F75C+0x00"), # callback
	0x8032F760: main.sym("camdemo_8032F75C+0x04"), # time
	0x8032F764: main.sym("camdemo_8032F764+0x00"), # callback
	0x8032F768: main.sym("camdemo_8032F764+0x04"), # time
	0x8032F76C: main.sym("camdemo_8032F76C+0x00"), # callback
	0x8032F770: main.sym("camdemo_8032F76C+0x04"), # time
	0x8032F774: main.sym("camdemo_8032F774+0x00"), # callback
	0x8032F778: main.sym("camdemo_8032F774+0x04"), # time
	0x8032F784: main.sym("camdemo_8032F784+0x00"), # callback
	0x8032F788: main.sym("camdemo_8032F784+0x04"), # time
	0x8032F794: main.sym("camdemo_8032F794+0x00"), # callback
	0x8032F798: main.sym("camdemo_8032F794+0x04"), # time
	0x8032F7A4: main.sym("camdemo_8032F7A4+0x00"), # callback
	0x8032F7A8: main.sym("camdemo_8032F7A4+0x04"), # time
	0x8032F7B4: main.sym("camdemo_8032F7B4+0x00"), # callback
	0x8032F7B8: main.sym("camdemo_8032F7B4+0x04"), # time
	0x8032F7C4: main.sym("camdemo_8032F7C4+0x00"), # callback
	0x8032F7C8: main.sym("camdemo_8032F7C4+0x04"), # time
	0x8032F7D4: main.sym("camdemo_8032F7D4+0x00"), # callback
	0x8032F7D8: main.sym("camdemo_8032F7D4+0x04"), # time
	0x8032F7EC: main.sym("camdemo_8032F7EC+0x00"), # callback
	0x8032F7F0: main.sym("camdemo_8032F7EC+0x04"), # time

	0x803301AA: main.sym("object_a_803301A8+0x02"), # scale
	0x803301AC: main.sym("object_a_803301A8+0x04"), # map
	0x803301B0: main.sym("object_a_803301A8+0x08"), # dist
	0x803301D0: main.sym("object_a_803301D0+0x00"), # arg
	0x803301D1: main.sym("object_a_803301D0+0x01"), # count
	0x803301D3: main.sym("object_a_803301D0+0x03"), # offset
	0x803301DC: main.sym("object_a_803301D0+0x0C"), # s_add
	0x803301E0: main.sym("object_a_803301D0+0x10"), # s_mul
	0x80330204: main.sym("object_a_80330204+2*0"),
	0x80330206: main.sym("object_a_80330204+2*1"),
	0x8033022C: main.sym("object_a_8033022C+2*0"),
	0x8033022E: main.sym("object_a_8033022C+2*1"),
	0x80330244: main.sym("object_a_80330244+2*0"),
	0x80330246: main.sym("object_a_80330244+2*1"),
	0x80330260: main.sym("object_a_80330260+4*0"),
	0x80330264: main.sym("object_a_80330260+4*1"),
	0x803302AC: main.sym("object_a_803302AC+0x00"), # count
	0x803302B2: main.sym("object_a_803302AC+0x06"), # shape
	0x803302B4: main.sym("object_a_803302AC+0x08"), # map
	0x803302EC: main.sym("object_a_803302EC+2*0"),
	0x803302EE: main.sym("object_a_803302EC+2*1"),
	0x803302F0: main.sym("object_a_803302EC+2*2"),
	0x803303C0: main.sym("object_a_803303C0+2*0"),
	0x803303C2: main.sym("object_a_803303C0+2*1"),
	0x8033047E: main.sym("object_a_80330480+2*(3*-1+2)"),
	0x80330480: main.sym("object_a_80330480+2*0"),
	0x80330482: main.sym("object_a_80330480+2*1"),
	0x80330484: main.sym("object_a_80330480+2*2"),
	0x803305F8: main.sym("object_a_803305F8+0x00"), # map
	0x803305FC: main.sym("object_a_803305F8+0x04"), # posx
	0x803305FE: main.sym("object_a_803305F8+0x06"), # posz
	0x80330600: main.sym("object_a_803305F8+0x08"), # angy
	0x803306B4: main.sym("object_a_803306B4+0x00"), # offset
	0x803306C4: main.sym("object_a_803306B4+0x10"), # vel
	0x80330C48: main.sym("object_a_80330C48+0x00"), # offset
	0x80330C4C: main.sym("object_a_80330C48+0x04"), # map
	0x80330DAC: main.sym("object_a_80330DAC+0x00"), # time
	0x80330DB4: main.sym("object_a_80330DAC+0x08"), # vel

	0x80330EE0: main.sym("shadow_rect_table+0x00"), # sizex
	0x80330EE4: main.sym("shadow_rect_table+0x04"), # sizez
	0x80330EE8: main.sym("shadow_rect_table+0x08"), # flag

	0x80330F64: main.sym("fluidtab+0x00"), # code
	0x80330F70: main.sym("fluidtab+0x0C"), # data
	0x80330F84: main.sym("fluidtab+0x20"), # layer

	0x803311A4: main.sym("fluidtabL+0x00"), # code
	0x803311B0: main.sym("fluidtabL+0x0C"), # data
	0x803311C4: main.sym("fluidtabL+0x20"), # layer

	0x8033127C: main.sym("fluidtabS+0x00"), # code
	0x80331288: main.sym("fluidtabS+0x0C"), # data
	0x8033129C: main.sym("fluidtabS+0x20"), # layer

	0x803317E0: main.sym("tagobjtab+0x00"), # script
	0x803317E4: main.sym("tagobjtab+0x04"), # shape
	0x803317E6: main.sym("tagobjtab+0x06"), # arg

	0x80332350: main.sym("mapobjtab+0x00"), # index
	0x80332351: main.sym("mapobjtab+0x01"), # type
	0x80332352: main.sym("mapobjtab+0x02"), # arg
	0x80332353: main.sym("mapobjtab+0x03"), # shape
	0x80332354: main.sym("mapobjtab+0x04"), # script

	0x803325F0: main.sym("meter+0x00"), # state
	0x803325F2: main.sym("meter+0x02"), # x
	0x803325F4: main.sym("meter+0x04"), # y

	0x8033282C: main.sym("object_b_8033282C+2*0"),
	0x8033282E: main.sym("object_b_8033282C+2*1"),

	0x80332860: main.sym("object_c_80332860+0x00"), # msg_start
	0x80332862: main.sym("object_c_80332860+0x02"), # msg_win
	0x80332864: main.sym("object_c_80332860+0x04"), # path
	0x803328D0: main.sym("object_c_803328D0+0x00"), # scale
	0x803328D4: main.sym("object_c_803328D0+0x04"), # se
	0x803328D8: main.sym("object_c_803328D0+0x08"), # dist
	0x803328DA: main.sym("object_c_803328D0+0x0A"), # damage
	0x80332934: main.sym("object_c_80332938+4*-1"),
	0x80332984: main.sym("object_c_80332984+0x00"), # arg
	0x80332987: main.sym("object_c_80332984+0x03"), # offset
	0x8033298A: main.sym("object_c_80332984+0x06"), # vy_add
	0x80332A20: main.sym("object_c_80332A20+0x00"), # map
	0x80332A24: main.sym("object_c_80332A20+0x04"), # p_map
	0x80332A28: main.sym("object_c_80332A20+0x08"), # p_shape
	0x80332A48: main.sym("object_c_80332A48+0x00"), # arg
	0x80332A4B: main.sym("object_c_80332A48+0x03"), # offset
	0x80332A4D: main.sym("object_c_80332A48+0x05"), # vf_mul
	0x80332A4E: main.sym("object_c_80332A48+0x06"), # vy_add
	0x80332AC0: main.sym("object_c_80332AC0+2*0"),
	0x80332AC2: main.sym("object_c_80332AC0+2*1"),
	0x80332B10: main.sym("object_c_80332B10+0x00"), # arg
	0x80332B11: main.sym("object_c_80332B10+0x01"), # count
	0x80332B13: main.sym("object_c_80332B10+0x03"), # offset
	0x80332B14: main.sym("object_c_80332B10+0x04"), # vf_add
	0x80332B16: main.sym("object_c_80332B10+0x06"), # vy_add
	0x80332B1C: main.sym("object_c_80332B10+0x0C"), # s_add
	0x80332B64: main.sym("object_c_80332B64+0x00"), # map
	0x80332B68: main.sym("object_c_80332B64+0x04"), # shape
	0x80332CCC: main.sym("object_c_80332CCC+4*0"),
	0x80332CD0: main.sym("object_c_80332CCC+4*1"),
	0x80332CD4: main.sym("object_c_80332CCC+4*2"),
	0x80332D10: main.sym("object_c_80332D10+2*0"),
	0x80332D12: main.sym("object_c_80332D10+2*1"),
	0x80332D58: main.sym("object_c_80332D58+2*0"),
	0x80332D5A: main.sym("object_c_80332D58+2*1"),
	0x80332D5C: main.sym("object_c_80332D58+2*2"),
	0x80332E24: main.sym("object_c_80332E24+0x00"), # shape
	0x80332E28: main.sym("object_c_80332E24+0x04"), # script
	0x80332E2C: main.sym("object_c_80332E24+0x08"), # scale

	0x80333794: main.sym("Na_data_80333598+4*127"),
	0x80333DF2: main.sym("Na_data_80333DE0+2*9"),
	0x80333FF0: main.sym("Na_PhonePan+4*127"),
	0x803341F0: main.sym("Na_WidePan+4*127"),
	0x803343F0: main.sym("Na_StereoPan+4*127"),

	0x803358D0: main.sym("__osViDevMgr+0x00"),
	0x803358D4: main.sym("__osViDevMgr+0x04"),
	0x803358D8: main.sym("__osViDevMgr+0x08"),
	0x803358DC: main.sym("__osViDevMgr+0x0C"),
	0x803358E0: main.sym("__osViDevMgr+0x10"),
	0x803358E4: main.sym("__osViDevMgr+0x14"),

	0x803358F0: main.sym("__osPiDevMgr+0x00"),
	0x803358F4: main.sym("__osPiDevMgr+0x04"),
	0x803358F8: main.sym("__osPiDevMgr+0x08"),
	0x803358FC: main.sym("__osPiDevMgr+0x0C"),
	0x80335900: main.sym("__osPiDevMgr+0x10"),
	0x80335904: main.sym("__osPiDevMgr+0x14"),

	0x80335910: main.sym("osClockRate+0"),
	0x80335914: main.sym("osClockRate+4"),

	# ==========================================================================
	# bss
	# ==========================================================================

	0x8033AFA4: main.sym("controller_data+0x14"), # status
	0x8033AFA8: main.sym("controller_data+0x18"), # pad

	0x8033B098: main.sym("demo_bank+0x08"), # buf

	0x8033B1A2: main.sym("player_data+0x32+2*0"), # rot[0]
	0x8033B1A4: main.sym("player_data+0x32+2*1"), # rot[1]
	0x8033B1A6: main.sym("player_data+0x32+2*2"), # rot[2]
	0x8033B1AC: main.sym("player_data+0x3C+4*0"), # pos[0]
	0x8033B1B0: main.sym("player_data+0x3C+4*1"), # pos[1]
	0x8033B1B4: main.sym("player_data+0x3C+4*2"), # pos[2]
	0x8033B1B8: main.sym("player_data+0x48+4*0"), # vel[0]
	0x8033B1BC: main.sym("player_data+0x48+4*1"), # vel[1]
	0x8033B1C0: main.sym("player_data+0x48+4*2"), # vel[2]

	0x8033B248: main.sym("mario_entry+0x00"),
	0x8033B249: main.sym("mario_entry+0x01"),
	0x8033B24A: main.sym("mario_entry+0x02"),
	0x8033B24B: main.sym("mario_entry+0x03"),
	0x8033B24C: main.sym("mario_entry+0x04"),

	0x8033B260: main.sym("hud+0x00"), # life
	0x8033B262: main.sym("hud+0x02"), # coin
	0x8033B264: main.sym("hud+0x04"), # star
	0x8033B266: main.sym("hud+0x06"), # power
	0x8033B268: main.sym("hud+0x08"), # key
	0x8033B26A: main.sym("hud+0x0A"), # flag
	0x8033B26C: main.sym("hud+0x0C"), # time

	0x8033B364: main.sym("mario_mirror+0x14"), # shape
	0x8033B368: main.sym("mario_mirror+0x18"), # scene

	0x8033B3B7: main.sym("pl_shape_data+0x07"), # wing

	0x8033B8D0: main.sym("scene_data+0x00"), # index
	0x8033B8D1: main.sym("scene_data+0x01"), # flag
	0x8033B8D2: main.sym("scene_data+0x02"), # env
	0x8033B8D4: main.sym("scene_data+0x04"), # s
	0x8033B8D8: main.sym("scene_data+0x08"), # map
	0x8033B8DC: main.sym("scene_data+0x0C"), # area
	0x8033B8E0: main.sym("scene_data+0x10"), # obj
	0x8033B8E4: main.sym("scene_data+0x14"), # port
	0x8033B8E8: main.sym("scene_data+0x18"), # bgport
	0x8033B8EC: main.sym("scene_data+0x1C"), # connect
	0x8033B8F0: main.sym("scene_data+0x20"), # actor
	0x8033B8F4: main.sym("scene_data+0x24"), # cam
	0x8033B8F8: main.sym("scene_data+0x28"), # wind
	0x8033B8FC: main.sym("scene_data+0x2C+4*0"), # jet[0]
	0x8033B900: main.sym("scene_data+0x2C+4*1"), # jet[1]
	0x8033B904: main.sym("scene_data+0x34+0"), # msg[0]
	0x8033B905: main.sym("scene_data+0x35+1"), # msg[1]
	0x8033B906: main.sym("scene_data+0x36"), # bgm_mode
	0x8033B908: main.sym("scene_data+0x38"), # bgm

	0x8033BAB0: main.sym("wipe+0x00"), # active
	0x8033BAB1: main.sym("wipe+0x01"), # type
	0x8033BAB2: main.sym("wipe+0x02"), # frame
	0x8033BAB3: main.sym("wipe+0x03"), # blank
	0x8033BAB4: main.sym("wipe+0x04"), # data.fade.r
	0x8033BAB5: main.sym("wipe+0x05"), # data.fade.g
	0x8033BAB6: main.sym("wipe+0x06"), # data.fade.b
	0x8033BAB8: main.sym("wipe+0x08"), # data.window.ssize
	0x8033BABA: main.sym("wipe+0x0A"), # data.window.esize
	0x8033BABC: main.sym("wipe+0x0C"), # data.window.sx
	0x8033BABE: main.sym("wipe+0x0E"), # data.window.sy
	0x8033BAC0: main.sym("wipe+0x10"), # data.window.ex
	0x8033BAC2: main.sym("wipe+0x12"), # data.window.ey
	0x8033BAC4: main.sym("wipe+0x14"), # data.window.rot

	0x8033BB18: main.sym("draw_mtxf+4*(4*3+0)"),
	0x8033BB1C: main.sym("draw_mtxf+4*(4*3+1)"),
	0x8033BB20: main.sym("draw_mtxf+4*(4*3+2)"),

	0x8033C390: main.sym("time_data+0x00"), # audcpu_i
	0x8033C392: main.sym("time_data+0x02"), # audrcp_i
	0x8033C398: main.sym("time_data+0x08+0"), # gfxcpu
	0x8033C39C: main.sym("time_data+0x08+4"), # gfxcpu
	0x8033C3C0: main.sym("time_data+0x30+0"), # gfxrcp
	0x8033C3C4: main.sym("time_data+0x30+4"), # gfxrcp

	0x8033C568: main.sym("_camera_bss_48-0x48+0x48"), # la
	0x8033C578: main.sym("_camera_bss_48-0x48+0x58"), # la
	0x8033C588: main.sym("_camera_bss_48-0x48+0x68"), # la
	0x8033C594: main.sym("_camera_bss_48-0x48+0x74"),
	0x8033C596: main.sym("_camera_bss_48-0x48+0x76"),
	0x8033C598: main.sym("_camera_bss_48-0x48+0x78"),
	0x8033C5A0: main.sym("_camera_bss_48-0x48+0x80"),
	0x8033C5A4: main.sym("_camera_bss_48-0x48+0x84"),
	0x8033C5A8: main.sym("_camera_bss_48-0x48+0x88"),
	0x8033C5AC: main.sym("_camera_bss_48-0x48+0x8C"),
	0x8033C5B0: main.sym("_camera_bss_48-0x48+0x90"),
	0x8033C5B4: main.sym("_camera_bss_48-0x48+0x94"),
	0x8033C5B6: main.sym("_camera_bss_48-0x48+0x96"),
	0x8033C5B8: main.sym("_camera_bss_48-0x48+0x98"),
	0x8033C5C0: main.sym("_camera_bss_48-0x48+0xA0"),
	0x8033C5C2: main.sym("_camera_bss_48-0x48+0xA2"),
	0x8033C5C4: main.sym("_camera_bss_48-0x48+0xA4"),
	0x8033C5C8: main.sym("_camera_bss_48-0x48+0xA8"),
	0x8033C5CA: main.sym("_camera_bss_48-0x48+0xAA"),
	0x8033C5CC: main.sym("_camera_bss_48-0x48+0xAC"),
	0x8033C5D0: main.sym("_camera_bss_48-0x48+0xB0"),
	0x8033C5D2: main.sym("_camera_bss_48-0x48+0xB2"),
	0x8033C5D4: main.sym("_camera_bss_48-0x48+0xB4"),
	0x8033C5E8: main.sym("_camera_bss_48-0x48+0xC8"),
	0x8033C5EC: main.sym("_camera_bss_48-0x48+0xCC"),
	0x8033C5F0: main.sym("_camera_bss_48-0x48+0xD0"),
	0x8033C5F4: main.sym("_camera_bss_48-0x48+0xD4"),
	0x8033C5F8: main.sym("_camera_bss_48-0x48+0xD8"),
	0x8033C5FC: main.sym("_camera_bss_48-0x48+0xDC"),
	0x8033C600: main.sym("_camera_bss_48-0x48+0xE0"),
	0x8033C604: main.sym("_camera_bss_48-0x48+0xE4"),
	0x8033C608: main.sym("_camera_bss_48-0x48+0xE8"),
	0x8033C60C: main.sym("_camera_bss_48-0x48+0xEC"),
	0x8033C610: main.sym("_camera_bss_48-0x48+0xF0"),
	0x8033C614: main.sym("_camera_bss_48-0x48+0xF4"),
	0x8033C61C: main.sym("_camera_bss_48-0x48+0xFC"),
	0x8033C61E: main.sym("_camera_bss_48-0x48+0xFE"),
	0x8033C620: main.sym("_camera_bss_48-0x48+0x100"),
	0x8033C622: main.sym("_camera_bss_48-0x48+0x102"),
	0x8033C624: main.sym("_camera_bss_48-0x48+0x104"),
	0x8033C628: main.sym("_camera_bss_48-0x48+0x108"),
	0x8033C630: main.sym("_camera_bss_48-0x48+0x110"),
	0x8033C632: main.sym("_camera_bss_48-0x48+0x112"),
	0x8033C634: main.sym("_camera_bss_48-0x48+0x114"),
	0x8033C668: main.sym("_camera_bss_48-0x48+0x148"),
	0x8033C66C: main.sym("_camera_bss_48-0x48+0x14C"),
	0x8033C670: main.sym("_camera_bss_48-0x48+0x150"),
	0x8033C674: main.sym("_camera_bss_48-0x48+0x154"),
	0x8033C676: main.sym("_camera_bss_48-0x48+0x156"),
	0x8033C678: main.sym("_camera_bss_48-0x48+0x158"),
	0x8033C67C: main.sym("_camera_bss_48-0x48+0x15C"),
	0x8033C680: main.sym("_camera_bss_48-0x48+0x160"),
	0x8033C684: main.sym("_camera_bss_48-0x48+0x164"),
	0x8033C686: main.sym("_camera_bss_48-0x48+0x166"),
	0x8033C688: main.sym("_camera_bss_48-0x48+0x168"),
	0x8033C68A: main.sym("_camera_bss_48-0x48+0x16A"),
	0x8033C68C: main.sym("_camera_bss_48-0x48+0x16C"),
	0x8033C68E: main.sym("_camera_bss_48-0x48+0x16E"),
	0x8033C690: main.sym("_camera_bss_48-0x48+0x170"),

	0x8033C6D4: main.sym("camdata+0x3C"),
	0x8033C6D5: main.sym("camdata+0x3D"),
	0x8033C6F0: main.sym("camdata+0x58"),
	0x8033C6F2: main.sym("camdata+0x5A"),
	0x8033C6F4: main.sym("camdata+0x5C"),
	0x8033C712: main.sym("camdata+0x7A"),
	0x8033C714: main.sym("camdata+0x7C"),
	0x8033C716: main.sym("camdata+0x7E"),
	0x8033C730: main.sym("camdata+0x98"),
	0x8033C732: main.sym("camdata+0x9A"),
	0x8033C734: main.sym("camdata+0x9C"),
	0x8033C736: main.sym("camdata+0x9E"),
	0x8033C738: main.sym("camdata+0xA0"),
	0x8033C73A: main.sym("camdata+0xA2"),
	0x8033C73C: main.sym("camdata+0xA4"),
	0x8033C740: main.sym("camdata+0xA8"),
	0x8033C744: main.sym("camdata+0xAC"),
	0x8033C748: main.sym("camdata+0xB0"),
	0x8033C74C: main.sym("camdata+0xB4"),
	0x8033C750: main.sym("camdata+0xB8"),
	0x8033C754: main.sym("camdata+0xBC"),

	0x8033C75A: main.sym("_camera_bss_238-0x238+0x23A"),
	0x8033C75C: main.sym("_camera_bss_238-0x238+0x23C"),
	0x8033C75E: main.sym("_camera_bss_238-0x238+0x23E"),
	0x8033C760: main.sym("_camera_bss_238-0x238+0x240"),
	0x8033C764: main.sym("_camera_bss_238-0x238+0x244"),
	0x8033C768: main.sym("_camera_bss_238-0x238+0x248"),
	0x8033C76A: main.sym("_camera_bss_238-0x238+0x24A"),
	0x8033C76C: main.sym("_camera_bss_238-0x238+0x24C"),
	0x8033C770: main.sym("_camera_bss_238-0x238+0x250"),
	0x8033C772: main.sym("_camera_bss_238-0x238+0x252"),
	0x8033C774: main.sym("_camera_bss_238-0x238+0x254"),
	0x8033C776: main.sym("_camera_bss_238-0x238+0x256"),
	0x8033C778: main.sym("_camera_bss_238-0x238+0x258"),
	0x8033C77C: main.sym("_camera_bss_238-0x238+0x25C"),
	0x8033C780: main.sym("_camera_bss_238-0x238+0x260"),
	0x8033C788: main.sym("_camera_bss_238-0x238+0x268"),
	0x8033C78A: main.sym("_camera_bss_238-0x238+0x26A"),
	0x8033C78C: main.sym("_camera_bss_238-0x238+0x26C"),
	0x8033C78E: main.sym("_camera_bss_238-0x238+0x26E"),
	0x8033C7A8: main.sym("_camera_bss_238-0x238+0x288"),
	0x8033C7AE: main.sym("_camera_bss_238-0x238+0x28E"),
	0x8033C7D0: main.sym("_camera_bss_238-0x238+0x2B0"), # la
	0x8033C7DC: main.sym("_camera_bss_238-0x238+0x2BC"),
	0x8033C7E0: main.sym("_camera_bss_238-0x238+0x2C0"),
	0x8033C7E8: main.sym("_camera_bss_238-0x238+0x2C8"), # la
	0x8033C808: main.sym("_camera_bss_238-0x238+0x2E8"), # la
	0x8033C828: main.sym("_camera_bss_238-0x238+0x308"), # la
	0x8033C840: main.sym("_camera_bss_238-0x238+0x320"),
	0x8033C844: main.sym("_camera_bss_238-0x238+0x324"),

	0x8033C850: main.sym("_camera_bss_330-0x330+0x330"),
	0x8033C950: main.sym("_camera_bss_330-0x330+0x430"),
	0x8033CA50: main.sym("_camera_bss_330-0x330+0x530"),
	0x8033CA54: main.sym("_camera_bss_330-0x330+0x534"),
	0x8033CA58: main.sym("_camera_bss_330-0x330+0x538"),
	0x8033CA5A: main.sym("_camera_bss_330-0x330+0x53A"),
	0x8033CA5C: main.sym("_camera_bss_330-0x330+0x53C"),
	0x8033CA60: main.sym("_camera_bss_330-0x330+0x540"),
	0x8033CA82: main.sym("_camera_bss_330-0x330+0x562"),

	0x8033D274: main.sym("bgdebug+0x00"), # ground
	0x8033D276: main.sym("bgdebug+0x02"), # roof
	0x8033D278: main.sym("bgdebug+0x04"), # wall
	0x8033D4FC: main.sym("object_data+0x74"), # flag
	0x80360EA0: main.sym("object_dummy+0x0C"), # s.scene
	0x80360EA1: main.sym("object_dummy+0x0D"), # s.group
	0x80361150: main.sym("obj_freelist+0x60"), # next
	0x803611D8: main.sym("area_table+0"),
	0x803611D9: main.sym("area_table+1"),

	0x803612C0: main.sym("backdata+0x00"),
	0x803612C2: main.sym("backdata+0x02"),
	0x803612C4: main.sym("backdata+0x04"),
	0x803612C8: main.sym("backdata+0x08"),
	0x803612CC: main.sym("backdata+0x0C"),

	0x80361490: main.sym("_Na_game_bss+0x00"),
	0x80361498: main.sym("_Na_game_bss+0x08"), # la
	0x80361C98: main.sym("_Na_game_bss+0x808"), # la
	0x80361F98: main.sym("_Na_game_bss+0xB08"),
	0x80361FA8: main.sym("_Na_game_bss+0xB18"),
	0x80361FB8: main.sym("_Na_game_bss+0xB28"), # la
	0x80361FCC: main.sym("_Na_game_bss+0xB3C"),
	0x80364B78: main.sym("_Na_game_bss+0x36E8"),
	0x80364B82: main.sym("_Na_game_bss+0x36F2"),
	0x80364B83: main.sym("_Na_game_bss+0x36F3"),
	0x80364B88: main.sym("_Na_game_bss+0x36F8"),

	0x80365E40: main.sym("viRetraceMsg+0"),
	0x80365E42: main.sym("viRetraceMsg+2"),
	0x80365E44: main.sym("viRetraceMsg+4"),

	0x80365E58: main.sym("viCounterMsg+0"),
	0x80365E5A: main.sym("viCounterMsg+2"),
	0x80365E5C: main.sym("viCounterMsg+4"),

	0x8036708C: main.sym("__osContPifRam+0x3C"),

	0x80367110: main.sym("__osCurrentTime+0"),
	0x80367114: main.sym("__osCurrentTime+4"),

	0x803671AC: main.sym("__osEepPifRam+0x3C"),

	# ==========================================================================

	0x00108A40: main.sym("_MainSegmentRomEnd"),
	0x004EC000: main.sym("_AnimeSegmentRomStart"),
	0x00579C20: main.sym("_DemoSegmentRomStart"),
	0x0057B720: main.sym("_AudioctlSegmentRomStart"),
	0x00593560: main.sym("_AudiotblSegmentRomStart"),
	0x007B0860: main.sym("_AudioseqSegmentRomStart"),
	0x007CC620: main.sym("_AudiobnkSegmentRomStart"),

	# ==========================================================================

	0x80220D98: main.sym("Na_WorkStart-8"), # la

	0x80220DB0: main.sym("_Na_work_bss_10-0x10+0x10"), # la
	0x80220DB1: main.sym("_Na_work_bss_10-0x10+0x11"),
	0x80220EA0: main.sym("_Na_work_bss_10-0x10+0x100"),
	0x80220EA2: main.sym("_Na_work_bss_10-0x10+0x102"),
	0x80220EA3: main.sym("_Na_work_bss_10-0x10+0x103"),
	0x80220EA8: main.sym("_Na_work_bss_10-0x10+0x108"), # la
	0x80220EB0: main.sym("_Na_work_bss_10-0x10+0x110"),
	0x80220EB8: main.sym("_Na_work_bss_10-0x10+0x118"), # la
	0x80220EC8: main.sym("_Na_work_bss_10-0x10+0x128"), # la
	0x80220EF8: main.sym("_Na_work_bss_10-0x10+0x158"), # la
	0x80220F08: main.sym("_Na_work_bss_10-0x10+0x168"), # la
	0x80220F18: main.sym("_Na_work_bss_10-0x10+0x178"), # la
	0x80220F28: main.sym("_Na_work_bss_10-0x10+0x188"),
	0x80220F2C: main.sym("_Na_work_bss_10-0x10+0x18C"), # la
	0x802210BC: main.sym("_Na_work_bss_10-0x10+0x31C"), # la
	0x802210C0: main.sym("_Na_work_bss_10-0x10+0x320"), # la
	0x802210F8: main.sym("_Na_work_bss_10-0x10+0x358"),
	0x802210FC: main.sym("_Na_work_bss_10-0x10+0x35C"), # la
	0x8022128C: main.sym("_Na_work_bss_10-0x10+0x4EC"), # la
	0x80221290: main.sym("_Na_work_bss_10-0x10+0x4F0"), # la
	0x802212C8: main.sym("_Na_work_bss_10-0x10+0x528"), # la
	0x802212CC: main.sym("_Na_work_bss_10-0x10+0x52C"), # la
	0x8022145C: main.sym("_Na_work_bss_10-0x10+0x6BC"), # la
	0x80221460: main.sym("_Na_work_bss_10-0x10+0x6C0"), # la
	0x80221498: main.sym("_Na_work_bss_10-0x10+0x6F8"), # la
	0x802214A8: main.sym("_Na_work_bss_10-0x10+0x708"), # la
	0x802214B0: main.sym("_Na_work_bss_10-0x10+0x710"), # la
	0x802214C0: main.sym("_Na_work_bss_10-0x10+0x720"), # la
	0x802214D0: main.sym("_Na_work_bss_10-0x10+0x730"),
	0x80221510: main.sym("_Na_work_bss_10-0x10+0x770"),
	0x80221610: main.sym("_Na_work_bss_10-0x10+0x870"), # la
	0x80222610: main.sym("_Na_work_bss_10-0x10+0x1870"),
	0x80222618: main.sym("_Na_work_bss_10-0x10+0x1878"),
	0x80222619: main.sym("_Na_work_bss_10-0x10+0x1879"),
	0x8022261A: main.sym("_Na_work_bss_10-0x10+0x187A"),
	0x80222630: main.sym("_Na_work_bss_10-0x10+0x1890"),
	0x80222644: main.sym("_Na_work_bss_10-0x10+0x18A4"),
	0x802226A8: main.sym("_Na_work_bss_10-0x10+0x1908"), # la
	0x802228C4: main.sym("_Na_work_bss_10-0x10+0x1B24"),
	0x802229D8: main.sym("_Na_work_bss_10-0x10+0x1C38"), # la
	0x802241D8: main.sym("_Na_work_bss_10-0x10+0x3438"), # la
	0x80224248: main.sym("_Na_work_bss_10-0x10+0x34A8"), # la
	0x80225BD8: main.sym("_Na_work_bss_10-0x10+0x4E38"), # la
	0x80225C98: main.sym("_Na_work_bss_10-0x10+0x4EF8"),
	0x80225CA8: main.sym("_Na_work_bss_10-0x10+0x4F08"), # la
	0x80225CAC: main.sym("_Na_work_bss_10-0x10+0x4F0C"),
	0x80225CB8: main.sym("_Na_work_bss_10-0x10+0x4F18"), # la
	0x80225CC8: main.sym("_Na_work_bss_10-0x10+0x4F28"), # la
	0x80225CD8: main.sym("_Na_work_bss_10-0x10+0x4F38"), # la
	0x80225CE8: main.sym("_Na_work_bss_10-0x10+0x4F48"), # la
	0x80225D00: main.sym("_Na_work_bss_10-0x10+0x4F60"), # la
	0x80225E00: main.sym("_Na_work_bss_10-0x10+0x5060"), # la
	0x80226300: main.sym("_Na_work_bss_10-0x10+0x5560"), # la
	0x80226318: main.sym("_Na_work_bss_10-0x10+0x5578"), # la
	0x80226320: main.sym("_Na_work_bss_10-0x10+0x5580"), # la
	0x80226338: main.sym("_Na_work_bss_10-0x10+0x5598"), # la
	0x80226938: main.sym("_Na_work_bss_10-0x10+0x5B98"),
	0x8022693C: main.sym("_Na_work_bss_10-0x10+0x5B9C"),
	0x80226940: main.sym("_Na_work_bss_10-0x10+0x5BA0"),
	0x80226948: main.sym("_Na_work_bss_10-0x10+0x5BA8"), # la
	0x80226A48: main.sym("_Na_work_bss_10-0x10+0x5CA8"), # la
	0x80226B48: main.sym("_Na_work_bss_10-0x10+0x5DA8"),
	0x80226B49: main.sym("_Na_work_bss_10-0x10+0x5DA9"),
	0x80226B4A: main.sym("_Na_work_bss_10-0x10+0x5DAA"),
	0x80226B4B: main.sym("_Na_work_bss_10-0x10+0x5DAB"),
	0x80226B4C: main.sym("_Na_work_bss_10-0x10+0x5DAC"),
	0x80226B50: main.sym("_Na_work_bss_10-0x10+0x5DB0"),
	0x80226B54: main.sym("_Na_work_bss_10-0x10+0x5DB4"),
	0x80226B58: main.sym("_Na_work_bss_10-0x10+0x5DB8"),
	0x80226B5C: main.sym("_Na_work_bss_10-0x10+0x5DBC"),
	0x80226B60: main.sym("_Na_work_bss_10-0x10+0x5DC0"),
	0x80226B64: main.sym("_Na_work_bss_10-0x10+0x5DC4"),
	0x80226B68: main.sym("_Na_work_bss_10-0x10+0x5DC8"), # la
	0x80226B6C: main.sym("_Na_work_bss_10-0x10+0x5DCC"), # la
	0x80226B70: main.sym("_Na_work_bss_10-0x10+0x5DD0"),
	0x80226B74: main.sym("_Na_work_bss_10-0x10+0x5DD4"),
	0x80226B78: main.sym("_Na_work_bss_10-0x10+0x5DD8"),
	0x80226B7C: main.sym("_Na_work_bss_10-0x10+0x5DDC"),
	0x80226B7E: main.sym("_Na_work_bss_10-0x10+0x5DDE"),
	0x80226B7F: main.sym("_Na_work_bss_10-0x10+0x5DDF"),
	0x80226B80: main.sym("_Na_work_bss_10-0x10+0x5DE0"), # la
	0x80226B84: main.sym("_Na_work_bss_10-0x10+0x5DE4"), # la
	0x80226B88: main.sym("_Na_work_bss_10-0x10+0x5DE8"),
	0x80226B8C: main.sym("_Na_work_bss_10-0x10+0x5DEC"),
	0x80226B90: main.sym("_Na_work_bss_10-0x10+0x5DF0"),
	0x80226B98: main.sym("_Na_work_bss_10-0x10+0x5DF8"),
	0x80226B9C: main.sym("_Na_work_bss_10-0x10+0x5DFC"),
	0x80226BA0: main.sym("_Na_work_bss_10-0x10+0x5E00"), # la
	0x80226C40: main.sym("_Na_work_bss_10-0x10+0x5EA0"),
	0x80226C4C: main.sym("_Na_work_bss_10-0x10+0x5EAC"),
	0x80226C52: main.sym("_Na_work_bss_10-0x10+0x5EB2"), # la
	0x80226C58: main.sym("_Na_work_bss_10-0x10+0x5EB8"), # la
	0x80226C98: main.sym("_Na_work_bss_10-0x10+0x5EF8"), # la

	0x80207690: main.sym("backup-0x70"),
	0x80207698: main.sym("backup-0x68"),
	0x8020769C: main.sym("backup-0x64"),
	0x80207708: main.sym("backup+0x08"),
	0x8020770C: main.sym("backup+0x0C"),
	0x80207725: main.sym("backup+0x25"),
	0x802078C0: main.sym("backup+0x1C0"),
}

seg_E0_code_text = {
	0x80247BAC: "E0.rspboot.text",
	0x80247BB8: "E0.rspboot.text",
	0x80247BD8: "E0.gspFast3D_fifo.text",
	0x80247BDC: "E0.gspFast3D_fifo.text",

	0x80248AA4: "E0.Main",
	# 0x80248AA8: "E0.Main",
	# 0x80248AAC: "E0.Main",
	0x80248AB0: "E0.Main",
	0x80248AC0: "E0.Gfx",
	0x80248AC4: "E0.Gfx",
	0x80248AC8: "E0.Gfx",
	0x80248ACC: "E0.Gfx",

	0x80278994: "E0.ulib.text",
	0x80278998: "E0.ulib.text",
	0x8027899C: "E0.ulib.text",
	0x802789A0: "E0.ulib.text",
	0x802789CC: "E0.ulib.text",
	0x802789D0: "E0.ulib.text",
	0x802789D4: "E0.ulib.text",
	0x802789D8: "E0.ulib.text",

	0x8031EA30: "E0.rspboot.text",
	0x8031EA38: "E0.aspMain.data",
	0x8031EA40: "E0.rspboot.text",
	0x8031EA58: "E0.aspMain.data",
	0x8031EA68: "E0.aspMain.data",
	0x8031EA70: "E0.aspMain.data",
}

imm_E0_code_text = {
	# src/memory.s
	# 0x80278074: (fmt_mask,),
	# 0x80278078: (fmt_mask,),
	# 0x8027808C: (fmt_mask,),
	# 0x80278128: (fmt_mask,),
	# 0x8027812C: (fmt_mask,),
	# 0x802783A0: (fmt_mem_alloc,),
	# 0x80278428: (fmt_mem_alloc,),
	# 0x80278520: (fmt_mask,),
	# 0x80278528: (fmt_mask,),
	# 0x8027858C: (ultra.fmt_os_mesg_pri,),
	# 0x80278590: (ultra.fmt_os_readwrite,),
	# 0x802785B8: (ultra.fmt_os_mesg_flag,),
	# 0x8027862C: (fmt_mask,),
	# 0x80278634: (fmt_mask,),
	# 0x80278710: (fmt_mask,),
	# 0x80278718: (fmt_mask,),
	# 0x80278730: (fmt_mask,),
	# 0x80278738: (fmt_mask,),
	# 0x80278760: (fmt_mem_alloc,),
	# 0x802787F8: (fmt_mask,),
	# 0x80278800: (fmt_mask,),
	# 0x80278814: (fmt_mem_alloc,),
	# 0x80278848: (fmt_mem_alloc,),
	# 0x802788D4: (fmt_mask,),
	# 0x802788DC: (fmt_mask,),
	# 0x802788F0: (fmt_mem_alloc,),
	# 0x80278980: ("ADDRESS_ULIB",),
	# 0x8027898C: ("ADDRESS_CIMG - ADDRESS_ULIB",),
	# 0x802789A8: (fmt_mask,),
	# 0x802789AC: (fmt_mask,),
	# 0x80278A2C: (fmt_mask,),
	# 0x80278A30: (fmt_mask,),
	# 0x80278AC0: (fmt_mask,),
	# 0x80278AC4: (fmt_mask,),
	# 0x80278B3C: (fmt_mask,),
	# 0x80278B40: (fmt_mask,),
	# 0x80278BB0: (fmt_mask,),
	# 0x80278BB4: (fmt_mask,),
	# 0x80278C68: (fmt_mask,),
	# 0x80278C6C: (fmt_mask,),
	# 0x80278F34: (fmt_mask,),
	# 0x80278F38: (fmt_mask,),
	# 0x80278FB0: (fmt_mem_alloc,),
	# 0x80278FE8: (fmt_mem_alloc,),
}

sym_E0_code_data = {
	# ==========================================================================
	# data
	# ==========================================================================

	# src/main.c
	0x8032D560: main.sym_var("sc_audclient", "SCCLIENT *", flag={"DALIGN"}),
	0x8032D564: main.sym_var("sc_gfxclient", "SCCLIENT *", flag={"DALIGN"}),
	0x8032D568: main.sym_var("sc_task", "SCTASK *", flag={"DALIGN"}),
	0x8032D56C: main.sym_var("sc_audtask", "SCTASK *", flag={"DALIGN"}),
	0x8032D570: main.sym_var("sc_gfxtask", "SCTASK *", flag={"DALIGN"}),
	0x8032D574: main.sym_var("sc_audtask_next", "SCTASK *", flag={"DALIGN"}),
	0x8032D578: main.sym_var("sc_gfxtask_next", "SCTASK *", flag={"DALIGN"}),
	0x8032D57C: main.sym_var("sc_aud", "char", flag={"DALIGN"}),
	0x8032D580: main.sym_var("sc_vi", "u32", flag={"DALIGN"}),
	0x8032D584: main.sym_var("reset_timer", "s8", flag={"GLOBL","DALIGN"}),
	0x8032D588: main.sym_var("reset_frame", "s8", flag={"GLOBL","DALIGN"}),
	0x8032D58C: main.sym_var("debug_stage", "char", flag={"GLOBL","DALIGN"}),
	0x8032D590: main.sym_var("debug_thread", "char", flag={"GLOBL","DALIGN"}),
	0x8032D594: main.sym_var("debug_time", "char", flag={"GLOBL","DALIGN"}),
	0x8032D598: main.sym_var("debug_mem", "char", flag={"GLOBL","DALIGN"}),
	0x8032D59C: main.sym_var("debug_time_seq", "u16", "[]"),
	0x8032D5AC: main.sym_var("debug_mem_seq", "u16", "[]"),
	0x8032D5BC: main.sym_var("debug_time_idx", "s16", flag={"DALIGN"}),
	0x8032D5C0: main.sym_var("debug_mem_idx", "s16", flag={"DALIGN"}),

	# src/graphics.c
	0x8032D5D0: main.sym_var("gfx_8032D5D0", "char", flag={"DALIGN"}), # unused
	0x8032D5D4: main.sym_var("gfx_frame", "u32", flag={"GLOBL","DALIGN"}),
	0x8032D5D8: main.sym_var("gfx_vi", "u16", flag={"GLOBL","DALIGN"}),
	0x8032D5DC: main.sym_var("gfx_dp", "u16", flag={"GLOBL","DALIGN"}),
	0x8032D5E0: main.sym_var_fnc("gfx_callback", flag={"GLOBL","DALIGN"}),
	0x8032D5E4: main.sym_var("cont1", "CONTROLLER *", flag={"GLOBL","DALIGN"}),
	0x8032D5E8: main.sym_var("cont2", "CONTROLLER *", flag={"GLOBL","DALIGN"}),
	0x8032D5EC: main.sym_var("contp", "CONTROLLER *", flag={"GLOBL","DALIGN"}),
	0x8032D5F0: main.sym_var("demop", "DEMO *", flag={"GLOBL","DALIGN"}),
	0x8032D5F4: main.sym_var("demo_index", "u16", flag={"GLOBL","DALIGN"}),
	0x8032D5F8: main.sym_var("demo_rec", "DEMO"),

	# src/audio.c
	0x8032D600: main.sym_var("aud_mute_flag", "u8", flag={"DALIGN"}),
	0x8032D604: main.sym_var("aud_lock_flag", "u8", flag={"DALIGN"}),
	0x8032D608: main.sym_var("bgm_stage", "u16", flag={"DALIGN"}),
	0x8032D60C: main.sym_var("bgm_shell", "u16", flag={"DALIGN"}),
	0x8032D610: main.sym_var("bgm_special", "u16", flag={"DALIGN"}),
	0x8032D614: main.sym_var("aud_endless_flag", "unsigned char", flag={"DALIGN"}),
	0x8032D618: main.sym_var("aud_8032D618", "char"), # unused
	0x8032D61C: main.sym_var("aud_8032D61C", "FVEC"), # unused
	0x8032D628: main.sym_var("aud_modetab", "s16", "[]"),
	0x8032D630: main.sym_var("aud_levelse_table", "Na_Se", "[]"),
	0x8032D6C0: main.sym_var("aud_wave_flag", "char", flag={"DALIGN"}),

	# src/game.c
	0x8032D6D0: main.sym_var("staff_01", "static const char *", "[]"),
	0x8032D6D8: main.sym_var("staff_02", "static const char *", "[]"),
	0x8032D6E4: main.sym_var("staff_03", "static const char *", "[]"),
	0x8032D6F0: main.sym_var("staff_04", "static const char *", "[]"),
	0x8032D700: main.sym_var("staff_05", "static const char *", "[]"),
	0x8032D710: main.sym_var("staff_06", "static const char *", "[]"),
	0x8032D71C: main.sym_var("staff_07", "static const char *", "[]"),
	0x8032D728: main.sym_var("staff_08", "static const char *", "[]"),
	0x8032D738: main.sym_var("staff_09", "static const char *", "[]"),
	0x8032D740: main.sym_var("staff_10", "static const char *", "[]"),
	0x8032D750: main.sym_var("staff_11", "static const char *", "[]"),
	0x8032D75C: main.sym_var("staff_12", "static const char *", "[]"),
	0x8032D764: main.sym_var("staff_13", "static const char *", "[]"),
	0x8032D774: main.sym_var("staff_14", "static const char *", "[]"),
	0x8032D77C: main.sym_var("staff_15", "static const char *", "[]"),
	0x8032D788: main.sym_var("staff_16", "static const char *", "[]"),
	0x8032D79C: main.sym_var("staff_17", "static const char *", "[]"),
	0x8032D7AC: main.sym_var("staff_18", "static const char *", "[]"),
	0x8032D7BC: main.sym_var("staff_19", "static const char *", "[]"),
	0x8032D7C4: main.sym_var("staff_20", "static const char *", "[]"),
	0x8032D7CC: main.sym_var("staff_table", "static STAFF", "[]"),
	0x8032D93C: main.sym_var("mario", "PLAYER *", flag={"GLOBL","DALIGN"}),
	0x8032D940: main.sym_var("game_8032D940", "s16", flag={"DALIGN"}), # unused
	0x8032D944: main.sym_var("mid_flag", "char", flag={"DALIGN"}),

	# src/collision.c
	0x8032D950: main.sym_var("collisiontab", "COLLISION", "[]"),
	0x8032DA48: main.sym_var("fdamagetab", "u32", "[3][3]"),
	0x8032DA6C: main.sym_var("bdamagetab", "u32", "[3][3]"),
	0x8032DA90: main.sym_var("door_flag", "u8", flag={"DALIGN"}),
	0x8032DA94: main.sym_var("pipe_flag", "u8", flag={"DALIGN"}),
	0x8032DA98: main.sym_var("slider_flag", "u8", flag={"DALIGN"}),

	# src/player.c
	0x8032DAA0: main.sym_var("pl_surfacetab", "char", "[][6]"),
	0x8032DACC: main.sym_var("pl_unpresstab", "u8", "[]"),
	0x8032DAE0: main.sym_var("pl_flash_pattern", "u64"),

	# src/physics.c
	0x8032DAF0: main.sym_var("quicksand_speed", "s16", "[]"),
	0x8032DAF8: main.sym_var("water_ground", "BGFACE", flag={"GLOBL"}),

	# src/pldemo.c
	0x8032DB30: main.sym_var("pldemo_vp", "Vp", flag={"GLOBL"}),
	0x8032DB40: main.sym_var("pldemo_staff", "STAFF *", flag={"GLOBL","DALIGN"}),
	0x8032DB44: main.sym_var("pldemo_8032DB44", "s8", flag={"GLOBL","DALIGN"}),
	0x8032DB48: main.sym_var("pldemo_8032DB48", "s8", flag={"GLOBL","DALIGN"}),
	0x8032DB4C: main.sym_var("pldemo_8032DB4C", "s8", "[]", flag={"GLOBL"}),
	0x8032DB54: main.sym_var("pldemo_8032DB54", "u8", "[]", flag={"GLOBL"}),
	0x8032DB5C: main.sym_var("pldemo_8032DB5C", "BSPLINE", "[]", flag={"GLOBL"}),
	0x8032DC34: main.sym_var("pldemo_8032DC34", "s32", flag={"GLOBL","DALIGN"}),
	0x8032DC38: main.sym_var("pldemo_8032DC38", "s32", flag={"GLOBL","DALIGN"}),
	0x8032DC3C: main.sym_var("pldemo_8032DC3C", "u8", "[]", flag={"GLOBL"}),

	# src/plmove.c
	0x8032DC50: main.sym_var("plmove_8032DC50", "PL_MOVE", flag={"GLOBL"}),
	0x8032DC68: main.sym_var("plmove_8032DC68", "PL_MOVE", flag={"GLOBL"}),
	0x8032DC80: main.sym_var("plmove_8032DC80", "PL_MOVE", flag={"GLOBL"}),
	0x8032DC98: main.sym_var("plmove_8032DC98", "PL_MOVE", flag={"GLOBL"}),
	0x8032DCB0: main.sym_var("plmove_8032DCB0", "PL_MOVE", flag={"GLOBL"}),
	0x8032DCC8: main.sym_var("plmove_8032DCC8", "PL_MOVE", flag={"GLOBL"}),
	0x8032DCE0: main.sym_var("plmove_8032DCE0", "PL_MOVE", flag={"GLOBL"}),
	0x8032DCF8: main.sym_var("plmove_8032DCF8", "PL_MOVE", flag={"GLOBL"}),
	0x8032DD10: main.sym_var("plmove_8032DD10", "PL_MOVE", flag={"GLOBL"}),

	# src/plswim.c
	0x8032DD30: main.sym_var("plswim_8032DD30", "s16", flag={"GLOBL","DALIGN"}),
	0x8032DD34: main.sym_var("plswim_8032DD34", "s16", flag={"GLOBL","DALIGN"}),
	0x8032DD38: main.sym_var("plswim_8032DD38", "s16", "[]", flag={"GLOBL"}),

	# src/pltake.c
	0x8032DD40: main.sym_var("pltake_8032DD40", "s8", "[]", flag={"GLOBL"}),

	# src/callback.c
	0x8032DD50: main.sym_var("pl_eyes_table", "s8", "[]"),
	0x8032DD58: main.sym_var("pl_punch_table", "s8", "[]"),
	0x8032DD6C: main.sym_var("pl_punch_stamp", "short", flag={"DALIGN"}),

	# src/memory.c
	0x8032DD70: main.sym_var("mem_frame", "MEM_FRAME *", flag={"DALIGN"}),

	# src/backup.c
	0x8032DD80: main.sym_var("bu_course", "u8", flag={"GLOBL","DALIGN"}),
	0x8032DD84: main.sym_var("bu_level", "u8", flag={"GLOBL","DALIGN"}),
	0x8032DD88: main.sym_var("bu_hiscore", "u8", flag={"GLOBL","DALIGN"}),
	0x8032DD8C: main.sym_var("bu_myscore", "u8", flag={"GLOBL","DALIGN"}),
	0x8032DD90: main.sym_var("bu_star", "u8", flag={"GLOBL","DALIGN"}),
	0x8032DD94: main.sym_var("bu_jump", "u8", flag={"GLOBL","DALIGN"}),
	0x8032DD98: main.sym_var("coursetab", "s8", "[]", flag={"GLOBL"}),

	# src/scene.c
	0x8032DDC0: main.sym_var("mario_actor", "ACTOR *", flag={"GLOBL","DALIGN"}),
	0x8032DDC4: main.sym_var("shape_table", "SHAPE **", flag={"GLOBL","DALIGN"}),
	0x8032DDC8: main.sym_var("scene_table", "SCENE *", flag={"GLOBL","DALIGN"}),
	0x8032DDCC: main.sym_var("scenep", "SCENE *", flag={"GLOBL","DALIGN"}),
	0x8032DDD0: main.sym_var("staffp", "STAFF *", flag={"GLOBL","DALIGN"}),
	0x8032DDD4: main.sym_var("sn_viewport", "Vp *", flag={"DALIGN"}),
	0x8032DDD8: main.sym_var("sn_scissor", "Vp *", flag={"DALIGN"}),
	0x8032DDDC: main.sym_var("wipe_delay", "s16", flag={"DALIGN"}),
	0x8032DDE0: main.sym_var("scene_fill", "u32", flag={"DALIGN"}),
	0x8032DDE4: main.sym_var("blank_fill", "u32", flag={"DALIGN"}),
	0x8032DDE8: main.sym_var("blank_r", "u8", flag={"DALIGN"}),
	0x8032DDEC: main.sym_var("blank_g", "u8", flag={"DALIGN"}),
	0x8032DDF0: main.sym_var("blank_b", "u8", flag={"DALIGN"}),
	0x8032DDF4: main.sym_var("file_index", "s16", flag={"GLOBL","DALIGN"}),
	0x8032DDF8: main.sym_var("stage_index", "s16", flag={"GLOBL","DALIGN"}),
	0x8032DDFC: main.sym_var("port_script", "OBJLANG *", "[]"),
	0x8032DE4C: main.sym_var("port_type", "u8", "[]"),
	0x8032DE60: main.sym_var("default_vp", "Vp"),

	# src/draw.c
	0x8032DE70: main.sym_var("draw_rendermode_1", "u32", "[2][8]"),
	0x8032DEB0: main.sym_var("draw_rendermode_2", "u32", "[2][8]"),
	0x8032DEF0: main.sym_var("draw_scene", "SSCENE *", flag={"GLOBL","DALIGN"}),
	0x8032DEF4: main.sym_var("draw_layer", "SLAYER *", flag={"GLOBL","DALIGN"}),
	0x8032DEF8: main.sym_var("draw_persp", "SPERSP *", flag={"GLOBL","DALIGN"}),
	0x8032DEFC: main.sym_var("draw_camera", "SCAMERA *", flag={"GLOBL","DALIGN"}),
	0x8032DF00: main.sym_var("draw_object", "SOBJECT *", flag={"GLOBL","DALIGN"}),
	0x8032DF04: main.sym_var("draw_hand", "SHAND *", flag={"GLOBL","DALIGN"}),
	0x8032DF08: main.sym_var("draw_timer", "u16", flag={"GLOBL","DALIGN"}),

	# src/time.c
	0x8032DF10: main.sym_var("time_mode", "s16", flag={"DALIGN"}),
	0x8032DF14: main.sym_var("time_cpu", "s16", flag={"DALIGN"}),
	0x8032DF18: main.sym_var("time_rcp", "s16", flag={"DALIGN"}),

	# src/camera.c
	0x8032DF20: main.sym_var("camera_8032DF20", "s32", flag={"GLOBL","DALIGN"}), # unused
	0x8032DF24: main.sym_var("camera_8032DF24", "OBJECT *", flag={"GLOBL","DALIGN"}),
	0x8032DF28: main.sym_var("camera_8032DF28", "s32", flag={"GLOBL","DALIGN"}),
	0x8032DF2C: main.sym_var("camera_8032DF2C", "s32", flag={"GLOBL","DALIGN"}),
	0x8032DF30: main.sym_var("camera_8032DF30", "OBJECT *", flag={"GLOBL","DALIGN"}),
	0x8032DF34: main.sym_var("camera_8032DF34", "s16", flag={"GLOBL","DALIGN"}),
	0x8032DF38: main.sym_var("camera_stagescene", "s32", flag={"GLOBL","DALIGN"}),
	0x8032DF3C: main.sym_var("camera_prevstage", "s32", flag={"GLOBL","DALIGN"}),
	0x8032DF40: main.sym_var("camera_8032DF40", "f32", flag={"GLOBL","DALIGN"}), # unused
	0x8032DF44: main.sym_var("camera_8032DF44", "f32", flag={"GLOBL","DALIGN"}), # unused
	0x8032DF48: main.sym_var("camera_8032DF48", "f32", flag={"GLOBL","DALIGN"}), # unused
	0x8032DF4C: main.sym_var("camera_8032DF4C", "f32", flag={"GLOBL","DALIGN"}),
	0x8032DF50: main.sym_var("camera_8032DF50", "u8", flag={"GLOBL","DALIGN"}),
	0x8032DF54: main.sym_var("camera_8032DF54", "u8", flag={"GLOBL","DALIGN"}),
	0x8032DF58: main.sym_var("camera_8032DF58", "u8", flag={"GLOBL","DALIGN"}),
	0x8032DF5C: main.sym_var("camera_8032DF5C", "u8", flag={"GLOBL","DALIGN"}),
	0x8032DF60: main.sym_var("mario_cam", "PL_CAMERA *", flag={"GLOBL","DALIGN"}),
	0x8032DF64: main.sym_var("luigi_cam", "PL_CAMERA *", flag={"GLOBL","DALIGN"}),
	0x8032DF68: main.sym_var("camera_8032DF68", "s32", flag={"GLOBL","DALIGN"}), # unused
	0x8032DF6C: main.sym_var("camera_8032DF6C", "FVEC", flag={"GLOBL"}),
	0x8032DF78: main.sym_var("camera_8032DF78", "FVEC", flag={"GLOBL"}), # unused
	0x8032DF84: main.sym_var("camera_8032DF84", "FVEC", flag={"GLOBL"}), # unused
	0x8032DF90: main.sym_var("camera_8032DF90", "FVEC", flag={"GLOBL"}), # unused
	0x8032DF9C: main.sym_var("camera_8032DF9C", "FVEC", flag={"GLOBL"}), # unused
	0x8032DFA8: main.sym_var_fnc("camera_8032DFA8", lst="[]", val="int", arg=(
		"CAMERA *",
		"FVEC",
		"FVEC",
	), flag={"GLOBL"}),
	0x8032DFF0: main.sym_var("camera_8032DFF0", "FVEC", flag={"GLOBL"}),
	0x8032DFFC: main.sym_var("camera_8032DFFC", "FVEC", flag={"GLOBL"}),
	0x8032E008: main.sym_var("camera_8032E008", "u16", "[]", flag={"GLOBL"}), # unused
	0x8032E018: main.sym_var("camera_8032E018", "u8", "[]", flag={"GLOBL"}),
	0x8032E020: main.sym_var("campos_bbh_library_test", "CAMPOS", "[]", flag={"GLOBL"}), # unused
	0x8032E050: main.sym_var("campos_bbh_library", "CAMPOS", "[]", flag={"GLOBL"}),
	0x8032E080: main.sym_var("camctl_null", "CAMCTL", "[]", flag={"GLOBL"}), # unused
	0x8032E098: main.sym_var("camctl_sl", "CAMCTL", "[]", flag={"GLOBL"}),
	0x8032E0E0: main.sym_var("camctl_thi", "CAMCTL", "[]", flag={"GLOBL"}),
	0x8032E128: main.sym_var("camctl_hmc", "CAMCTL", "[]", flag={"GLOBL"}),
	0x8032E1D0: main.sym_var("camctl_ssl", "CAMCTL", "[]", flag={"GLOBL"}),
	0x8032E248: main.sym_var("camctl_rr", "CAMCTL", "[]", flag={"GLOBL"}),
	0x8032E338: main.sym_var("camctl_cotmc", "CAMCTL", "[]", flag={"GLOBL"}),
	0x8032E368: main.sym_var("camctl_ccm", "CAMCTL", "[]", flag={"GLOBL"}),
	0x8032E3B0: main.sym_var("camctl_inside", "CAMCTL", "[]", flag={"GLOBL"}),
	0x8032E6F8: main.sym_var("camctl_bbh", "CAMCTL", "[]", flag={"GLOBL"}),
	0x8032ECB0: main.sym_var("camctl_table", "CAMCTL *", "[]", flag={"GLOBL"}),
	0x8032ED50: main.sym_var("campath_8032ED50", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032EE08: main.sym_var("campath_8032EE08", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032EEC0: main.sym_var("campath_8032EEC0", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032EF30: main.sym_var("campath_8032EF30", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032EFA0: main.sym_var("campath_8032EFA0", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032EFF0: main.sym_var("campath_8032EFF0", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F048: main.sym_var("campath_8032F048", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F0E8: main.sym_var("campath_8032F0E8", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F130: main.sym_var("campath_8032F130", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F178: main.sym_var("campath_8032F178", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F1B8: main.sym_var("campath_8032F1B8", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F1F0: main.sym_var("camera_8032F1F0", "FVEC", flag={"GLOBL"}),
	0x8032F1FC: main.sym_var("camera_8032F1FC", "FVEC", flag={"GLOBL"}),
	0x8032F208: main.sym_var("camera_8032F208", "FVEC", flag={"GLOBL"}),
	0x8032F214: main.sym_var("campath_8032F214", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F32C: main.sym_var("campath_8032F32C", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F444: main.sym_var("campath_8032F444", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F48C: main.sym_var("campath_8032F48C", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F4D4: main.sym_var("camdemo_8032F4D4", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F534: main.sym_var("camdemo_8032F534", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F544: main.sym_var("camdemo_8032F544", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F554: main.sym_var("camdemo_8032F554", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F564: main.sym_var("camdemo_8032F564", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F56C: main.sym_var("camdemo_8032F56C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F574: main.sym_var("camdemo_8032F574", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F59C: main.sym_var("camdemo_8032F59C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F5C4: main.sym_var("camdemo_8032F5C4", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F5DC: main.sym_var("camdemo_8032F5DC", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F5F4: main.sym_var("camdemo_8032F5F4", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F60C: main.sym_var("camdemo_8032F60C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F624: main.sym_var("camdemo_8032F624", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F634: main.sym_var("camdemo_8032F634", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F63C: main.sym_var("camdemo_8032F63C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F64C: main.sym_var("camdemo_8032F64C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F65C: main.sym_var("camdemo_8032F65C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F674: main.sym_var("camdemo_8032F674", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F69C: main.sym_var("camdemo_8032F69C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F6AC: main.sym_var("camdemo_8032F6AC", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F6BC: main.sym_var("camdemo_8032F6BC", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F6CC: main.sym_var("camdemo_8032F6CC", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F6DC: main.sym_var("camdemo_8032F6DC", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F6F4: main.sym_var("camdemo_8032F6F4", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F6FC: main.sym_var("camdemo_8032F6FC", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F70C: main.sym_var("camdemo_8032F70C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F714: main.sym_var("camdemo_8032F714", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F71C: main.sym_var("camdemo_8032F71C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F72C: main.sym_var("camdemo_8032F72C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F734: main.sym_var("camdemo_8032F734", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F74C: main.sym_var("camdemo_8032F74C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F754: main.sym_var("camdemo_8032F754", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F75C: main.sym_var("camdemo_8032F75C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F764: main.sym_var("camdemo_8032F764", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F76C: main.sym_var("camdemo_8032F76C", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F774: main.sym_var("camdemo_8032F774", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F784: main.sym_var("camdemo_8032F784", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F794: main.sym_var("camdemo_8032F794", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F7A4: main.sym_var("camdemo_8032F7A4", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F7B4: main.sym_var("camdemo_8032F7B4", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F7C4: main.sym_var("camdemo_8032F7C4", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F7D4: main.sym_var("camdemo_8032F7D4", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F7EC: main.sym_var("camdemo_8032F7EC", "CAMDEMO", "[]", flag={"GLOBL"}),
	0x8032F804: main.sym_var("camera_windemo_table", "u8", "[][4]", flag={"GLOBL"}),
	0x8032F870: main.sym_var("camera_pause_table", "u8", "[]", flag={"GLOBL"}),
	0x8032F884: main.sym_var("campath_battlefield_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F8AC: main.sym_var("campath_battlefield_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F8D4: main.sym_var("campath_wf1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F8FC: main.sym_var("campath_wf1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F924: main.sym_var("campath_jrb1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F94C: main.sym_var("campath_jrb1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F974: main.sym_var("campath_ccm2_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F99C: main.sym_var("campath_ccm2_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F9C4: main.sym_var("campath_bbh1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032F9E4: main.sym_var("campath_bbh1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FA04: main.sym_var("campath_hmc1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FA2C: main.sym_var("campath_hmc1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FA54: main.sym_var("campath_thi3_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FA6C: main.sym_var("campath_thi3_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FA84: main.sym_var("campath_lll2_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FAB4: main.sym_var("campath_lll2_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FAE4: main.sym_var("campath_ssl1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FB14: main.sym_var("campath_ssl1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FB44: main.sym_var("campath_ddd1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FB7C: main.sym_var("campath_ddd1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FBB4: main.sym_var("campath_sl1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FBD4: main.sym_var("campath_sl1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FBF4: main.sym_var("campath_wdw1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FC14: main.sym_var("campath_wdw1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FC34: main.sym_var("campath_ttm1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FC64: main.sym_var("campath_ttm1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FC94: main.sym_var("campath_thi1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FCCC: main.sym_var("campath_thi1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FD04: main.sym_var("campath_ttc1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FD24: main.sym_var("campath_ttc1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FD44: main.sym_var("campath_rr1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FD64: main.sym_var("campath_rr1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FD84: main.sym_var("campath_sa1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FDAC: main.sym_var("campath_sa1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FDD4: main.sym_var("campath_cotmc1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FDFC: main.sym_var("campath_cotmc1_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FE24: main.sym_var("campath_ddd2_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FE4C: main.sym_var("campath_ddd2_look", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FE74: main.sym_var("campath_ccm1_eye", "CAMPATH", "[]", flag={"GLOBL"}),
	0x8032FE94: main.sym_var("campath_ccm1_look", "CAMPATH", "[]", flag={"GLOBL"}),

	# src/object.c
	0x8032FEC0: main.sym_var("objproc_table", "s8", "[]"),
	0x8032FECC: main.sym_var("pl_effecttab", "PL_EFFECT", "[]"),

	# src/objectlib.c
	0x80330000: main.sym_var("objectlib_80330000", "signed char", "[]", flag={"GLOBL"}),
	0x80330004: main.sym_var("bittab", "short", "[]", flag={"GLOBL"}),
	0x80330014: main.sym_var("areastagetab", "s8", "[]", flag={"GLOBL"}),

	# src/object_a.c
	0x80330020: main.sym_var("object_a_80330020", "u32", "[]", flag={"GLOBL"}),
	0x8033002C: main.sym_var("object_a_8033002C", "s16", "[]", flag={"GLOBL"}),
	0x8033006C: main.sym_var("object_a_8033006C", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330074: main.sym_var("object_a_80330074", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330084: main.sym_var("object_a_80330084", "HITINFO", flag={"GLOBL"}),
	0x80330094: main.sym_var("object_a_80330094", "PARTICLE", flag={"GLOBL"}),
	0x803300A8: main.sym_var("object_a_803300A8", "u8", "[]", flag={"GLOBL"}), # unused
	0x803300AC: main.sym_var("object_a_803300AC", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x803300BC: main.sym_var("object_a_803300BC", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x803300E0: main.sym_var("object_a_803300E0", "STEPSOUND", "[]", flag={"GLOBL"}),
	0x80330140: main.sym_var("object_a_80330140", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x8033015C: main.sym_var("object_a_8033015C", "struct object_a_0", "[]", flag={"GLOBL"}), # unused
	0x80330198: main.sym_var("object_a_80330198", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x803301A8: main.sym_var("object_a_803301A8", "struct object_a_1", "[]", flag={"GLOBL"}),
	0x803301C0: main.sym_var("object_a_803301C0", "HITINFO", flag={"GLOBL"}),
	0x803301D0: main.sym_var("object_a_803301D0", "PARTICLE", flag={"GLOBL"}),
	0x803301E4: main.sym_var("object_a_803301E4", "HITINFO", flag={"GLOBL"}),
	0x803301F4: main.sym_var("object_a_803301F4", "HITINFO", flag={"GLOBL"}),
	0x80330204: main.sym_var("object_a_80330204", "s16", "[][2]", flag={"GLOBL"}),
	0x80330224: main.sym_var("object_a_80330224", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x8033022C: main.sym_var("object_a_8033022C", "s16", "[][2]", flag={"GLOBL"}),
	0x80330244: main.sym_var("object_a_80330244", "s16", "[][2]", flag={"GLOBL"}),
	0x80330260: main.sym_var("object_a_80330260", "s32", "[][2]", flag={"GLOBL"}),
	0x80330288: main.sym_var("object_a_80330288", "Na_Se", "[]", flag={"GLOBL"}),
	0x80330290: main.sym_var("object_a_80330290", "Na_Se", "[]", flag={"GLOBL"}),
	0x80330298: main.sym_var("object_a_80330298", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x803302AC: main.sym_var("object_a_803302AC", "struct object_a_2", "[]", flag={"GLOBL"}),
	0x803302DC: main.sym_var("object_a_803302DC", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x803302EC: main.sym_var("object_a_803302EC", "s16", "[][3]", flag={"GLOBL"}),
	0x80330318: main.sym_var("object_a_80330318", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x8033032C: main.sym_var("object_a_8033032C", "PARTICLE", flag={"GLOBL"}),
	0x80330340: main.sym_var("object_a_80330340", "PARTICLE", flag={"GLOBL"}),
	0x80330354: main.sym_var("object_a_80330354", "s16", "[]", flag={"GLOBL"}),
	0x8033035C: main.sym_var("object_a_8033035C", "PARTICLE", flag={"GLOBL"}),
	0x80330370: main.sym_var("object_a_80330370", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330380: main.sym_var("object_a_80330380", "f32", "[]", flag={"GLOBL"}),
	0x80330390: main.sym_var("object_a_80330390", "HITINFO", flag={"GLOBL"}),
	0x803303A0: main.sym_var("object_a_803303A0", "HITINFO", flag={"GLOBL"}),
	0x803303B0: main.sym_var("object_a_803303B0", "HITINFO", flag={"GLOBL"}),
	0x803303C0: main.sym_var("object_a_803303C0", "s16", "[][2]", flag={"GLOBL"}),
	0x803303E8: main.sym_var("object_a_803303E8", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x803303F8: main.sym_var("object_a_803303F8", "HITINFO", flag={"GLOBL"}),
	0x80330408: main.sym_var("object_a_80330408", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330410: main.sym_var("object_a_80330410", "HITINFO", flag={"GLOBL"}),
	0x80330420: main.sym_var("object_a_80330420", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x8033042C: main.sym_var("object_a_8033042C", "HITINFO", flag={"GLOBL"}),
	0x8033043C: main.sym_var("object_a_8033043C", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330450: main.sym_var("object_a_80330450", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x8033045C: main.sym_var("object_a_8033045C", "s8", "[]", flag={"GLOBL"}),
	0x8033046C: main.sym_var("object_a_8033046C", "s16", "[]", flag={"GLOBL"}),
	0x80330470: main.sym_var("object_a_80330470", "s16", "[]", flag={"GLOBL"}),
	0x80330474: main.sym_var("object_a_80330474", "s8", "[]", flag={"GLOBL"}),
	0x80330478: main.sym_var("object_a_80330478", "s16", "[]", flag={"GLOBL"}),
	0x80330480: main.sym_var("object_a_80330480", "s16", "[][3]", flag={"GLOBL"}),
	0x803304C8: main.sym_var("object_a_803304C8", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330518: main.sym_var("object_a_80330518", "STEPSOUND", "[]", flag={"GLOBL"}),
	0x803305F0: main.sym_var("object_a_803305F0", "s8", "[]", flag={"GLOBL"}),
	0x803305F4: main.sym_var("object_a_803305F4", "s8", "[]", flag={"GLOBL"}),
	0x803305F8: main.sym_var("object_a_803305F8", "struct object_a_3", "[]", flag={"GLOBL"}),
	0x8033067C: main.sym_var("object_a_8033067C", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330688: main.sym_var("object_a_80330688", "HITINFO", flag={"GLOBL"}),
	0x80330698: main.sym_var("object_a_80330698", "HITINFO", flag={"GLOBL"}),
	0x803306A8: main.sym_var("object_a_803306A8", "f32", "[]", flag={"GLOBL"}),
	0x803306B4: main.sym_var("object_a_803306B4", "struct object_a_4", "[]", flag={"GLOBL"}),
	0x803306DC: main.sym_var("object_a_803306DC", "PATH", "[]", flag={"GLOBL"}),
	0x80330738: main.sym_var("object_a_80330738", "STEPSOUND", "[]", flag={"GLOBL"}),
	0x803307A0: main.sym_var("object_a_803307A0", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x803307C0: main.sym_var("object_a_803307C0", "static s16", "[]"),
	0x803307F4: main.sym_var("object_a_803307F4", "static s16", "[]"),
	0x80330828: main.sym_var("object_a_80330828", "s16 *", "[]", flag={"GLOBL"}),
	0x80330830: main.sym_var("object_a_80330830", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330840: main.sym_var("object_a_80330840", "HITINFO", flag={"GLOBL"}),
	0x80330850: main.sym_var("object_a_80330850", "static s8", "[]"),
	0x80330884: main.sym_var("object_a_80330884", "static s8", "[]"),
	0x803308A8: main.sym_var("object_a_803308A8", "static s8", "[]"),
	0x803308CC: main.sym_var("object_a_803308CC", "s8 *", "[]", flag={"GLOBL"}),
	0x803308D8: main.sym_var("object_a_803308D8", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x803308F8: main.sym_var("object_a_803308F8", "s8", "[]", flag={"GLOBL"}),
	0x80330900: main.sym_var("object_a_80330900", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330924: main.sym_var("object_a_80330924", "static s8", "[]"),
	0x80330940: main.sym_var("object_a_80330940", "static s8", "[]"),
	0x8033095C: main.sym_var("object_a_8033095C", "static s8", "[]"),
	0x80330978: main.sym_var("object_a_80330978", "static s8", "[]"),
	0x80330994: main.sym_var("object_a_80330994", "static s8", "[]"),
	0x803309B0: main.sym_var("object_a_803309B0", "static s8", "[]"),
	0x803309CC: main.sym_var("object_a_803309CC", "static s8", "[]"),
	0x803309E8: main.sym_var("object_a_803309E8", "static s8", "[]"),
	0x80330A04: main.sym_var("object_a_80330A04", "static s8", "[]"),
	0x80330A20: main.sym_var("object_a_80330A20", "static s8", "[]"),
	0x80330A3C: main.sym_var("object_a_80330A3C", "static s8", "[]"),
	0x80330A58: main.sym_var("object_a_80330A58", "static s8", "[]"),
	0x80330A74: main.sym_var("object_a_80330A74", "static s8", "[]"),
	0x80330A90: main.sym_var("object_a_80330A90", "static s8", "[]"),
	0x80330AAC: main.sym_var("object_a_80330AAC", "struct object_a_5", "[]", flag={"GLOBL"}),
	0x80330B1C: main.sym_var("object_a_80330B1C", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330B38: main.sym_var("object_a_80330B38", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330B44: main.sym_var("object_a_80330B44", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330B5C: main.sym_var("object_a_80330B5C", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330B68: main.sym_var("object_a_80330B68", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330B74: main.sym_var("object_a_80330B74", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330B84: main.sym_var("object_a_80330B84", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330B90: main.sym_var("object_a_80330B90", "HITINFO", flag={"GLOBL"}),
	0x80330BA0: main.sym_var("object_a_80330BA0", "struct object_a_6", "[]", flag={"GLOBL"}),
	0x80330C20: main.sym_var("object_a_80330C20", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330C38: main.sym_var("object_a_80330C38", "HITINFO", flag={"GLOBL"}),
	0x80330C48: main.sym_var("object_a_80330C48", "struct object_a_7", "[]", flag={"GLOBL"}),
	0x80330C58: main.sym_var("object_a_80330C58", "HITINFO", flag={"GLOBL"}),
	0x80330C68: main.sym_var("object_a_80330C68", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330C74: main.sym_var("object_a_80330C74", "HITINFO", flag={"GLOBL"}),
	0x80330C84: main.sym_var("object_a_80330C84", "s16", "[][3]", flag={"GLOBL"}),
	0x80330C98: main.sym_var("object_a_80330C98", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330CB0: main.sym_var("object_a_80330CB0", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330CC4: main.sym_var("object_a_80330CC4", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330CD4: main.sym_var("object_a_80330CD4", "HITINFO", flag={"GLOBL"}),
	0x80330CE4: main.sym_var("object_a_80330CE4", "OBJCALL *", "[]", flag={"GLOBL"}),
	0x80330D0C: main.sym_var("object_a_80330D0C", "SPLASH", flag={"GLOBL"}),
	0x80330D30: main.sym_var("object_a_80330D30", "SPLASH", flag={"GLOBL"}),
	0x80330D54: main.sym_var("object_a_80330D54", "SPLASH", flag={"GLOBL"}),
	0x80330D78: main.sym_var("object_a_80330D78", "SPLASH", flag={"GLOBL"}),
	0x80330D9C: main.sym_var("object_a_80330D9C", "HITINFO", flag={"GLOBL"}),
	0x80330DAC: main.sym_var("object_a_80330DAC", "struct object_a_8", "[]", flag={"GLOBL"}),

	# src/ride.c
	0x80330E20: main.sym_var("ride_80330E20", "s16", flag={"DALIGN"}),
	0x80330E24: main.sym_var("ride_80330E24", "int", "[4]"), # unused
	0x80330E34: main.sym_var("ride_obj", "OBJECT *", flag={"DALIGN"}),

	# src/debug.c
	0x80330E40: main.sym_var("db_edit_effectinfo", "const char *", "[]"),
	0x80330E64: main.sym_var("db_edit_enemyinfo", "const char *", "[]"),
	0x80330E88: main.sym_var("db_button", "int", flag={"DALIGN"}),
	0x80330E8C: main.sym_var("db_repeat", "int", flag={"DALIGN"}),
	0x80330E90: main.sym_var("db_init_flag", "char", flag={"DALIGN"}),
	0x80330E94: main.sym_var("db_page", "s8", flag={"DALIGN"}),
	0x80330E98: main.sym_var("db_hideinfo", "char", flag={"DALIGN"}),
	0x80330E9C: main.sym_var("db_edit_flag", "char", flag={"DALIGN"}),
	0x80330EA0: main.sym_var("db_line", "s8", flag={"DALIGN"}),
	0x80330EA4: main.sym_var("db_info_idx", "s8", flag={"DALIGN"}),
	0x80330EA8: main.sym_var("db_info_seq", "s16", "[]"),

	# src/wipe.c
	0x80330EC0: main.sym_var("wipe_timer", "u8", "[2]"),
	0x80330EC4: main.sym_var("wipe_ang", "u16", "[2]"),
	0x80330EC8: main.sym_var("txt_wipe", "u8 *", "[]"),

	# src/shadow.c
	0x80330EE0: main.sym_var("shadow_rect_table", "SHADOW_RECT", "[]"),

	# src/background.c
	0x80330F00: main.sym_var("backtab", "BACKGROUND *", "[]"),
	0x80330F28: main.sym_var("back_shade", "u8", "[][3]"),

	# src/water.c
	0x80330F30: main.sym_var("water_timer", "s16", flag={"DALIGN"}),
	0x80330F34: main.sym_var("water_stamp", "s16", flag={"DALIGN"}),
	0x80330F38: main.sym_var("water_color", "s8", flag={"DALIGN"}),
	0x80330F3C: main.sym_var("pool_entry", "float", flag={"GLOBL","DALIGN"}),
	0x80330F40: main.sym_var("pool_flag", "int", flag={"DALIGN"}),
	0x80330F44: main.sym_var("txt_water", "u16 *", "[]"),
	0x80330F64: main.sym_var("fluidtab", "FLUID", "[]"),
	0x803311A4: main.sym_var("fluidtabL", "FLUID", "[]"),
	0x8033127C: main.sym_var("fluidtabS", "FLUID", "[]"),
	0x803312E8: main.sym_var("water_leveltab", "short", "[]"), # unused

	# src/objshape.c
	0x803312F0: main.sym_var("objshape_803312F0", "s16", flag={"DALIGN"}),
	0x803312F4: main.sym_var("objshape_803312F4", "s16", flag={"DALIGN"}),
	0x803312F8: main.sym_var("objshape_803312F8", "s16", flag={"DALIGN"}),

	# src/wave.c
	0x80331300: main.sym_var("wavetab0", "WAVE *", "[]"),
	0x80331308: main.sym_var("wavetab1", "WAVE *", "[]"),
	0x80331344: main.sym_var("wavetab2", "WAVE *", "[]"),
	0x8033134C: main.sym_var("wavetab", "WAVE **", "[]"),
	0x80331358: main.sym_var("wave_timer", "s16", flag={"DALIGN"}),
	0x8033135C: main.sym_var("wave_stamp", "s16", flag={"DALIGN"}),

	# src/dprint.c
	0x80331360: main.sym_var("dprint_index", "s16", flag={"DALIGN"}),

	# src/message.c
	0x80331370: main.sym_var("kerningtab", "u8", "[256]"),
	0x80331470: main.sym_var("msg_state", "s8", flag={"DALIGN"}),
	0x80331474: main.sym_var("msg_angle", "float", flag={"DALIGN"}),
	0x80331478: main.sym_var("msg_scale", "float", flag={"DALIGN"}),
	0x8033147C: main.sym_var("msg_scroll", "short", flag={"DALIGN"}),
	0x80331480: main.sym_var("msg_type", "s8", flag={"DALIGN"}),
	0x80331484: main.sym_var("msg_code", "s16", flag={"DALIGN"}),
	0x80331488: main.sym_var("msg_next", "s16", flag={"DALIGN"}),
	0x8033148C: main.sym_var("msg_index", "s16", flag={"DALIGN"}),
	0x80331490: main.sym_var("msg_cursor", "s8", flag={"DALIGN"}),
	0x80331494: main.sym_var("msg_cursor_flag", "char", flag={"DALIGN"}),
	0x80331498: main.sym_var("cursor_status", "u8", flag={"DALIGN"}),
	0x8033149C: main.sym_var("cursor_timer", "u8", flag={"DALIGN"}),
	0x803314A0: main.sym_var("msg_answer", "int", flag={"GLOBL","DALIGN"}),
	0x803314A4: main.sym_var("str_803314A4", "unsigned char", "[][5]"), # the / you
	0x803314B0: main.sym_var("str_803314B0", "unsigned char", "[]"), # [+]
	0x803314B4: main.sym_var("str_803314B4", "unsigned char", "[]"), # [x]
	0x803314B8: main.sym_var("str_803314B8", "unsigned char", "[]"), # [*]
	0x803314BC: main.sym_var("str_803314BC", "unsigned char", "[]"), # [x]
	0x803314C0: main.sym_var("str_803314C0", "unsigned char", "[][5]"), # the / you
	0x803314CC: main.sym_var("msg_battle", "s16", "[]"),
	0x803314D8: main.sym_var("msg_fanfare", "s16", "[]"),
	0x803314E0: main.sym_var("msg_se7_1e", "s16", "[]"),
	0x803314EC: main.sym_var("msg_bgmstop", "s16", "[]"),
	0x803314F8: main.sym_var("menu_code", "s16", flag={"DALIGN"}),
	0x803315E4: main.sym_var("captiontab", "unsigned char *", "[]"),
	0x8033160C: main.sym_var("demo_alpha", "u16", flag={"DALIGN"}),
	0x80331610: main.sym_var("caption", "s16", flag={"DALIGN"}),
	0x80331614: main.sym_var("demo_frame", "s16", flag={"DALIGN"}),
	0x80331618: main.sym_var("demo_timer", "s16", flag={"DALIGN"}),
	0x8033161C: main.sym_var("camera_cursor", "s8", flag={"DALIGN"}),
	0x80331620: main.sym_var("pausemenu_level", "s8", flag={"GLOBL","DALIGN"}),
	0x80331624: main.sym_var("str_80331624", "unsigned char", "[]"), # COURSE
	0x8033162C: main.sym_var("str_8033162C", "unsigned char", "[]"), # MY SCORE
	0x80331638: main.sym_var("str_80331638", "unsigned char", "[]"), # [*]
	0x8033163C: main.sym_var("str_8033163C", "unsigned char", "[]"), # [.]
	0x80331640: main.sym_var("str_80331640", "unsigned char", "[]"), # LAKITU <-> MARIO
	0x80331650: main.sym_var("str_80331650", "unsigned char", "[]"), # LAKITU <-> STOP
	0x80331660: main.sym_var("str_80331660", "unsigned char", "[]"), # (NORMAL)(UP-CLOSE)
	0x80331674: main.sym_var("str_80331674", "unsigned char", "[]"), # (NORMAL)(FIXED)
	0x80331684: main.sym_var("str_80331684", "unsigned char", "[]"), # CONTINUE
	0x80331690: main.sym_var("str_80331690", "unsigned char", "[]"), # EXIT COURSE
	0x8033169C: main.sym_var("str_8033169C", "unsigned char", "[]"), # SET CAMERA ANGLE WITH R
	0x803316B4: main.sym_var("str_803316B4", "unsigned char", "[]"), # PAUSE
	0x803316BC: main.sym_var("str_803316BC", "unsigned char", "[]"), # [*]
	0x803316C0: main.sym_var("str_803316C0", "unsigned char", "[]"), # [+][x]
	0x803316C4: main.sym_var("str_803316C4", "unsigned char", "[]"), # [*][x]
	0x803316C8: main.sym_var("savedemo_end", "char", flag={"DALIGN"}),
	0x803316CC: main.sym_var("savedemo_timer", "int", flag={"DALIGN"}),
	0x803316D0: main.sym_var("savedemo_coin", "int", flag={"DALIGN"}),
	0x803316D4: main.sym_var("savemenu_code", "s8", flag={"GLOBL","DALIGN"}),
	0x803316D8: main.sym_var("str_803316D8", "unsigned char", "[]"), # HI SCORE
	0x803316E4: main.sym_var("str_803316E4", "unsigned char", "[]"), # CONGRATULATIONS
	0x803316F4: main.sym_var("str_803316F4", "unsigned char", "[]"), # [+]
	0x803316F8: main.sym_var("str_803316F8", "unsigned char", "[]"), # [x]
	0x803316FC: main.sym_var("str_803316FC", "unsigned char", "[]"), # COURSE
	0x80331704: main.sym_var("str_80331704", "unsigned char", "[]"), # CATCH
	0x8033170C: main.sym_var("str_8033170C", "unsigned char", "[]"), # CLEAR
	0x80331714: main.sym_var("str_80331714", "unsigned char", "[]"), # [*]
	0x80331718: main.sym_var("str_80331718", "unsigned char", "[]"), # SAVE & CONTINUE
	0x80331728: main.sym_var("str_80331728", "unsigned char", "[]"), # SAVE & QUIT
	0x80331734: main.sym_var("str_80331734", "unsigned char", "[]"), # CONTINUE, DON'T SAVE

	# src/weather.c
	0x80331750: main.sym_var("weather_code", "s8", flag={"GLOBL","DALIGN"}),
	0x80331758: main.sym_var("snow_template", "Vtx", "[]"),
	0x80331788: main.sym_var("snow_v0", "SVEC"),
	0x80331790: main.sym_var("snow_v1", "SVEC"),
	0x80331798: main.sym_var("snow_v2", "SVEC"),

	# src/lava.c
	0x803317A0: main.sym_var("lava_803317A0", "char", flag={"DALIGN"}), # unused
	0x803317A8: main.sym_var("lava_template", "Vtx", "[]"),

	# src/tag.c
	0x803317E0: main.sym_var("tagobjtab", "static TAGOBJ", "[]"),
	0x80332350: main.sym_var("mapobjtab", "static MAPOBJ", "[]"),

	# src/hud.c
	0x803325F0: main.sym_var("meter", "METER"),
	0x803325FC: main.sym_var("hud_timer", "int", flag={"DALIGN"}),
	0x80332600: main.sym_var("hud_80332600", "short", flag={"DALIGN"}), # unused
	0x80332604: main.sym_var("hud_80332604", "short", flag={"DALIGN"}), # unused
	0x80332608: main.sym_var("hud_camera", "s16", flag={"DALIGN"}),

	# src/object_b.c
	0x80332610: main.sym_var("object_b_80332610", "s8", flag={"GLOBL","DALIGN"}),
	0x80332614: main.sym_var("object_b_80332614", "s16", flag={"GLOBL","DALIGN"}),
	0x80332618: main.sym_var("object_b_80332618", "s8", flag={"GLOBL","DALIGN"}),
	0x8033261C: main.sym_var("object_b_8033261C", "s8", flag={"GLOBL","DALIGN"}),
	0x80332620: main.sym_var("object_b_80332620", "s8", flag={"GLOBL","DALIGN"}),
	0x80332624: main.sym_var("object_b_80332624", "HITINFO", flag={"GLOBL"}),
	0x80332634: main.sym_var("object_b_80332634", "HITINFO", flag={"GLOBL"}),
	0x80332644: main.sym_var("object_b_80332644", "HITINFO", flag={"GLOBL"}),
	0x80332654: main.sym_var("object_b_80332654", "HITINFO", flag={"GLOBL"}),
	0x80332664: main.sym_var("object_b_80332664", "HITINFO", flag={"GLOBL"}),
	0x80332674: main.sym_var("object_b_80332674", "HITINFO", flag={"GLOBL"}),
	0x80332684: main.sym_var("object_b_80332684", "HITINFO", flag={"GLOBL"}),
	0x80332694: main.sym_var("object_b_80332694", "HITINFO", flag={"GLOBL"}),
	0x803326A4: main.sym_var("object_b_803326A4", "HITINFO", flag={"GLOBL"}),
	0x803326B4: main.sym_var("object_b_803326B4", "HITINFO", flag={"GLOBL"}),
	0x803326C4: main.sym_var("object_b_803326C4", "PATH", "[]", flag={"GLOBL"}),
	0x80332718: main.sym_var("object_b_80332718", "PATH", "[]", flag={"GLOBL"}),
	0x80332764: main.sym_var("object_b_80332764", "HITINFO", flag={"GLOBL"}),
	0x80332774: main.sym_var("object_b_80332774", "HITINFO", flag={"GLOBL"}),
	0x80332784: main.sym_var("object_b_80332784", "HITINFO", flag={"GLOBL"}),
	0x80332794: main.sym_var("redcoin_hit", "HITINFO", flag={"GLOBL"}),
	0x803327A4: main.sym_var("object_b_803327A4", "s8", flag={"GLOBL","DALIGN"}),
	0x803327A8: main.sym_var("object_b_803327A8", "HITINFO", flag={"GLOBL"}),
	0x803327B8: main.sym_var("object_b_803327B8", "PATH", "[]", flag={"GLOBL"}),
	0x803327FC: main.sym_var("object_b_803327FC", "HITINFO", flag={"GLOBL"}),
	0x8033280C: main.sym_var("object_b_8033280C", "HITINFO", flag={"GLOBL"}),
	0x8033281C: main.sym_var("object_b_8033281C", "HITINFO", flag={"GLOBL"}),
	0x8033282C: main.sym_var("object_b_8033282C", "s16", "[][2]", flag={"GLOBL"}),

	# src/object_c.c
	0x80332840: main.sym_var("object_c_80332840", "HITINFO", flag={"GLOBL"}),
	0x80332850: main.sym_var("object_c_80332850", "u8", "[6]", flag={"GLOBL"}), # template
	0x80332858: main.sym_var("object_c_80332858", "u8", "[6]", flag={"GLOBL"}), # template
	0x80332860: main.sym_var("object_c_80332860", "struct object_c_0", "[]", flag={"GLOBL"}),
	0x80332880: main.sym_var("object_c_80332880", "HITINFO", flag={"GLOBL"}),
	0x80332890: main.sym_var("object_c_80332890", "u8", "[6]", flag={"GLOBL"}), # template
	0x80332898: main.sym_var("object_c_80332898", "HITINFO", flag={"GLOBL"}),
	0x803328A8: main.sym_var("object_c_803328A8", "HITINFO", flag={"GLOBL"}),
	0x803328B8: main.sym_var("object_c_803328B8", "s16", "[]", flag={"GLOBL"}),
	0x803328C0: main.sym_var("object_c_803328C0", "HITINFO", flag={"GLOBL"}),
	0x803328D0: main.sym_var("object_c_803328D0", "struct object_c_1", "[]", flag={"GLOBL"}),
	0x803328F4: main.sym_var("object_c_803328F4", "u8", "[][6]", flag={"GLOBL"}), # template
	0x80332900: main.sym_var("object_c_80332900", "HITINFO", flag={"GLOBL"}),
	0x80332910: main.sym_var("object_c_80332910", "HITINFO", flag={"GLOBL"}),
	0x80332920: main.sym_var("object_c_80332920", "HITINFO", flag={"GLOBL"}),
	0x80332930: main.sym_var("object_c_80332930", "u8", "[6]", flag={"GLOBL"}), # template
	0x80332938: main.sym_var("object_c_80332938", "f32", "[]", flag={"GLOBL"}),
	0x80332948: main.sym_var("object_c_80332948", "int", "[]", flag={"GLOBL"}),
	0x80332954: main.sym_var("object_c_80332954", "HITINFO", flag={"GLOBL"}),
	0x80332964: main.sym_var("object_c_80332964", "u8", "[6]", flag={"GLOBL"}), # template
	0x8033296C: main.sym_var("object_c_8033296C", "HITINFO", flag={"GLOBL"}),
	0x8033297C: main.sym_var("object_c_8033297C", "s8", "[]", flag={"GLOBL"}),
	0x80332984: main.sym_var("object_c_80332984", "PARTICLE", flag={"GLOBL"}),
	0x80332998: main.sym_var("object_c_80332998", "HITINFO", flag={"GLOBL"}),
	0x803329A8: main.sym_var("object_c_803329A8", "HITINFO", flag={"GLOBL"}),
	0x803329B8: main.sym_var("object_c_803329B8", "PARTICLE", flag={"GLOBL"}),
	0x803329CC: main.sym_var("object_c_803329CC", "MAP *", "[]", flag={"GLOBL"}),
	0x803329DC: main.sym_var("object_c_803329DC", "PATH *", "[]", flag={"GLOBL"}),
	0x80332A00: main.sym_var("object_c_80332A00", "MAP *", "[]", flag={"GLOBL"}),
	0x80332A20: main.sym_var("object_c_80332A20", "struct object_c_2", "[]", flag={"GLOBL"}),
	0x80332A38: main.sym_var("object_c_80332A38", "HITINFO", flag={"GLOBL"}),
	0x80332A48: main.sym_var("object_c_80332A48", "PARTICLE", flag={"GLOBL"}),
	0x80332A5C: main.sym_var("object_c_80332A5C", "PARTICLE", flag={"GLOBL"}),
	0x80332A70: main.sym_var("object_c_80332A70", "MAP *", "[]", flag={"GLOBL"}),
	0x80332A78: main.sym_var("object_c_80332A78", "u8", "[]", flag={"GLOBL"}),
	0x80332A7C: main.sym_var("object_c_80332A7C", "f32", "[]", flag={"GLOBL"}),
	0x80332A8C: main.sym_var("object_c_80332A8C", "MAP *", "[]", flag={"GLOBL"}),
	0x80332A94: main.sym_var("object_c_80332A94", "s16", "[]", flag={"GLOBL"}),
	0x80332A9C: main.sym_var("object_c_80332A9C", "s16", "[]", flag={"GLOBL"}),
	0x80332AA4: main.sym_var("object_c_80332AA4", "s8", "[]", flag={"GLOBL"}),
	0x80332AA8: main.sym_var("object_c_80332AA8", "MAP *", "[]", flag={"GLOBL"}),
	0x80332AB0: main.sym_var("object_c_80332AB0", "s8", "[]", flag={"GLOBL"}),
	0x80332AB4: main.sym_var("object_c_80332AB4", "s16", "[]", flag={"GLOBL"}),
	0x80332AB8: main.sym_var("object_c_80332AB8", "MAP *", "[]", flag={"GLOBL"}),
	0x80332AC0: main.sym_var("object_c_80332AC0", "s16", "[][2][2]", flag={"GLOBL"}),
	0x80332AE0: main.sym_var("object_c_80332AE0", "s8", "[]", flag={"GLOBL"}),
	0x80332AE4: main.sym_var("object_c_80332AE4", "s16", "[]", flag={"GLOBL"}),
	0x80332AE8: main.sym_var("object_c_80332AE8", "s16", "[][4]", flag={"GLOBL"}),
	0x80332AF8: main.sym_var("object_c_80332AF8", "s16", "[]", flag={"GLOBL"}),
	0x80332B00: main.sym_var("object_c_80332B00", "HITINFO", flag={"GLOBL"}),
	0x80332B10: main.sym_var("object_c_80332B10", "PARTICLE", flag={"GLOBL"}),
	0x80332B24: main.sym_var("object_c_80332B24", "HITINFO", flag={"GLOBL"}),
	0x80332B34: main.sym_var("object_c_80332B34", "MAP *", "[]", flag={"GLOBL"}),
	0x80332B54: main.sym_var("object_c_80332B54", "MAP *", "[]", flag={"GLOBL"}),
	0x80332B5C: main.sym_var("object_c_80332B5C", "s16", "[]", flag={"GLOBL"}),
	0x80332B64: main.sym_var("object_c_80332B64", "struct object_c_3", "[][5]", flag={"GLOBL"}),
	0x80332BDC: main.sym_var("object_c_80332BDC", "s16", "[]", flag={"GLOBL"}),
	0x80332BE4: main.sym_var("object_c_80332BE4", "MAP *", "[]", flag={"GLOBL"}),
	0x80332BF0: main.sym_var("object_c_80332BF0", "HITINFO", flag={"GLOBL"}),
	0x80332C00: main.sym_var("object_c_80332C00", "HITINFO", flag={"GLOBL"}),
	0x80332C10: main.sym_var("object_c_80332C10", "HITINFO", flag={"GLOBL"}),
	0x80332C20: main.sym_var("object_c_80332C20", "HITINFO", flag={"GLOBL"}),
	0x80332C30: main.sym_var("object_c_80332C30", "HITINFO", flag={"GLOBL"}),
	0x80332C40: main.sym_var("object_c_80332C40", "s16", "[][2]", flag={"GLOBL"}),
	0x80332C4C: main.sym_var("object_c_80332C4C", "HITINFO", flag={"GLOBL"}),
	0x80332C5C: main.sym_var("object_c_80332C5C", "HITINFO", flag={"GLOBL"}),
	0x80332C6C: main.sym_var("object_c_80332C6C", "f32", "[]", flag={"GLOBL"}),
	0x80332C74: main.sym_var("object_c_80332C74", "HITINFO", flag={"GLOBL"}),
	0x80332C84: main.sym_var("object_c_80332C84", "HITINFO", flag={"GLOBL"}),
	0x80332C94: main.sym_var("object_c_80332C94", "HITINFO", flag={"GLOBL"}),
	0x80332CA4: main.sym_var("object_c_80332CA4", "HITINFO", flag={"GLOBL"}),
	0x80332CB4: main.sym_var("object_c_80332CB4", "s8", "[]", flag={"GLOBL"}),
	0x80332CBC: main.sym_var("object_c_80332CBC", "HITINFO", flag={"GLOBL"}),
	0x80332CCC: main.sym_var("object_c_80332CCC", "FVEC", "[]", flag={"GLOBL"}),
	0x80332CF0: main.sym_var("object_c_80332CF0", "u8", "[6]", flag={"GLOBL"}), # template
	0x80332CF8: main.sym_var("object_c_80332CF8", "struct object_c_4", "[]", flag={"GLOBL"}),
	0x80332D10: main.sym_var("object_c_80332D10", "s16", "[][2]", flag={"GLOBL"}),
	0x80332D28: main.sym_var("object_c_80332D28", "HITINFO", flag={"GLOBL"}),
	0x80332D38: main.sym_var("object_c_80332D38", "HITINFO", flag={"GLOBL"}),
	0x80332D48: main.sym_var("object_c_80332D48", "s16", "[][2]", flag={"GLOBL"}),
	0x80332D58: main.sym_var("object_c_80332D58", "SVEC", "[]", flag={"GLOBL"}),
	0x80332E14: main.sym_var("object_c_80332E14", "HITINFO", flag={"GLOBL"}),
	0x80332E24: main.sym_var("object_c_80332E24", "struct object_c_5", "[]", flag={"GLOBL"}),
	0x80332E3C: main.sym_var("object_c_80332E3C", "HITINFO", flag={"GLOBL"}),

	# src/audio/game.c
	0x80332E50: main.sym_var("Na_game_80332E50", "s32", flag={"GLOBL","DALIGN"}), # rng?
	0x80332E54: main.sym_var("Na_game_80332E54", "s32", flag={"GLOBL","DALIGN"}), # tick
	0x80332E58: main.sym_var("Na_MsgSeTable", "u8", "[]", flag={"GLOBL"}), # (msg len)
	0x80332F04: main.sym_var("Na_MsgSeData", "Na_Se", "[15]", flag={"GLOBL"}),
	0x80332F40: main.sym_var("Na_game_80332F40", "u8", flag={"GLOBL","DALIGN"}),
	0x80332F44: main.sym_var("Na_game_80332F44", "u8", flag={"GLOBL","DALIGN"}),
	0x80332F48: main.sym_var("Na_BgmCtlBBH", "static s16", "[]"),
	0x80332F54: main.sym_var("Na_BgmCtlDDD", "static s16", "[]"),
	0x80332F6C: main.sym_var("Na_BgmCtlJRB", "static s16", "[]"),
	0x80332F84: main.sym_var("Na_BgmCtlSA", "UNUSED static s16", "[]"), # unused
	0x80332F88: main.sym_var("Na_BgmCtlWDW", "static s16", "[]"),
	0x80332F98: main.sym_var("Na_BgmCtlHMC", "static s16", "[]"),
	0x80332FA8: main.sym_var("Na_BgmCtl38", "static s16", "[]"),
	0x80332FB8: main.sym_var("Na_BgmCtlNULL", "static s16", "[]"),
	0x80332FBC: main.sym_var("Na_game_80332FBC", "u8", flag={"GLOBL","DALIGN"}),
	0x80332FC0: main.sym_var("Na_game_80332FC0", "u8", flag={"GLOBL","DALIGN"}),
	0x80332FC4: main.sym_var("Na_BgmCtlTable", "s16 *", "[]", flag={"GLOBL"}), # (stage len)
	0x80333060: main.sym_var("Na_BgmCtlData", "Na_BgmCtl", "[]", flag={"GLOBL"}),
	0x803330C0: main.sym_var("Na_game_803330C0", "u8", "[][3]", flag={"GLOBL"}), # (stage len)
	0x80333138: main.sym_var("Na_game_80333138", "u16", "[]", flag={"GLOBL"}), # (stage len)
	0x80333188: main.sym_var("Na_BgmVolTable", "u8", "[]", flag={"GLOBL"}),
	0x803331AC: main.sym_var("Na_game_803331AC", "u8", flag={"GLOBL","DALIGN"}),
	0x803331B0: main.sym_var("Na_game_803331B0", "u8", flag={"GLOBL","DALIGN"}),
	0x803331B4: main.sym_var("Na_game_803331B4", "u8", "[]", flag={"GLOBL"}),
	0x803331C0: main.sym_var("Na_game_803331C0", "u8", "[]", flag={"GLOBL"}),
	0x803331CC: main.sym_var("Na_game_803331CC", "u8", "[]", flag={"GLOBL"}),
	0x803331D8: main.sym_var("Na_game_803331D8", "u8", "[]", flag={"GLOBL"}),
	0x803331E4: main.sym_var("Na_game_803331E4", "u8", "[]", flag={"GLOBL"}),
	0x803331F0: main.sym_var("Na_0", "FVEC", flag={"GLOBL"}),
	0x803331FC: main.sym_var("Na_1", "FVEC", flag={"GLOBL"}), # unused
	0x80333208: main.sym_var("Na_PortStatus", "u8", "[]", flag={"GLOBL"}),
	0x80333214: main.sym_var("Na_game_80333214", "u8", flag={"GLOBL","DALIGN"}), # unused
	0x80333218: main.sym_var("Na_game_80333218", "u8", flag={"GLOBL","DALIGN"}),
	0x8033321C: main.sym_var("Na_game_8033321C", "u8", flag={"GLOBL","DALIGN"}),
	0x80333220: main.sym_var("Na_game_80333220", "u16", flag={"GLOBL","DALIGN"}),
	0x80333224: main.sym_var("Na_game_80333224", "u8", flag={"GLOBL","DALIGN"}),
	0x80333228: main.sym_var("Na_game_80333228", "u16", flag={"GLOBL","DALIGN"}),
	0x8033322C: main.sym_var("Na_game_8033322C", "u8", flag={"GLOBL","DALIGN"}),
	0x80333230: main.sym_var("Na_game_80333230", "u8", flag={"GLOBL","DALIGN"}),
	0x80333234: main.sym_var("Na_game_80333234", "u8", flag={"GLOBL","DALIGN"}),
	0x80333238: main.sym_var("Na_game_80333238", "u8", flag={"GLOBL","DALIGN"}),
	0x8033323C: main.sym_var("Na_game_8033323C", "u8", flag={"GLOBL","DALIGN"}),
	0x80333240: main.sym_var("Na_game_80333240", "Na_Se", "[]", flag={"GLOBL"}),
	0x80333280: main.sym_var("Na_game_80333280", "u8", "[]", flag={"GLOBL"}),
	0x80333290: main.sym_var("Na_game_80333290", "u8", "[]", flag={"GLOBL"}),

	# src/audio/data.c
	0x803332A0: main.sym_var("Na_CfgTable", "Na_Cfg", "[]", flag={"GLOBL"}), # 18
	0x80333498: main.sym_var("Na_data_80333498", "s16", "[]", flag={"GLOBL"}), # unused
	0x80333598: main.sym_var("Na_data_80333598", "f32", "[]", flag={"GLOBL"}),
	0x80333994: main.sym_var("Na_FreqTable", "f32", "[]", flag={"GLOBL"}),
	0x80333B94: main.sym_var("Na_data_80333B94", "u8", "[]", flag={"GLOBL"}),
	0x80333BA4: main.sym_var("Na_data_80333BA4", "u8", "[]", flag={"GLOBL"}),
	0x80333BB4: main.sym_var("Na_data_80333BB4", "s8", "[]", flag={"GLOBL"}),
	0x80333BC4: main.sym_var("Na_DefaultEnv", "s16", "[]", flag={"GLOBL"}),
	0x80333BD0: main.sym_var("Na_SineWave", "static s16", "[]"),
	0x80333C50: main.sym_var("Na_PulseWave", "static s16", "[]"),
	0x80333CD0: main.sym_var("Na_TriangleWave", "static s16", "[]"),
	0x80333D50: main.sym_var("Na_SawWave", "static s16", "[]"),
	0x80333DD0: main.sym_var("Na_WaveTable", "s16 *", "[]", flag={"GLOBL"}),
	0x80333DE0: main.sym_var("Na_data_80333DE0", "u16", "[]", flag={"GLOBL"}),
	0x80333DF4: main.sym_var("Na_PhonePan", "f32", "[]", flag={"GLOBL"}),
	0x80333FF4: main.sym_var("Na_WidePan", "f32", "[]", flag={"GLOBL"}),
	0x803341F4: main.sym_var("Na_StereoPan", "f32", "[]", flag={"GLOBL"}),
	0x803343F4: main.sym_var("Na_rate_136A", "f32", "[]", flag={"GLOBL"}),
	0x803345F4: main.sym_var("Na_rate_136B", "f32", "[]", flag={"GLOBL"}),
	0x803347F4: main.sym_var("Na_rate_144A", "f32", "[]", flag={"GLOBL"}),
	0x803349F4: main.sym_var("Na_rate_144B", "f32", "[]", flag={"GLOBL"}),
	0x80334BF4: main.sym_var("Na_rate_128A", "f32", "[]", flag={"GLOBL"}),
	0x80334DF4: main.sym_var("Na_rate_128B", "f32", "[]", flag={"GLOBL"}),
	0x80334FF4: main.sym_var("Na_TickRate", "s16", flag={"GLOBL","DALIGN"}),
	0x80334FF8: main.sym_var("Na_data_80334FF8", "s8", flag={"GLOBL","DALIGN"}),
	0x80334FFC: main.sym_var("Na_HeapSize", "size_t", flag={"GLOBL","DALIGN"}),
	0x80335000: main.sym_var("Na_data_80335000", "size_t", flag={"GLOBL","DALIGN"}), # fix size
	0x80335004: main.sym_var("Na_data_80335004", "volatile u32", flag={"GLOBL","DALIGN"}),
	0x80335008: main.sym_var("Na_data_80335008", "s8", flag={"GLOBL","DALIGN"}), # unused

	# io/vitbl.c
	0x80335010: main.sym_var("osViModeTable", "OSViMode", "[]"),

	# io/vimgr.c
	0x803358D0: main.sym_var("__osViDevMgr", "OSDevMgr"),

	# io/pimgr.c
	0x803358F0: main.sym_var("__osPiDevMgr", "OSDevMgr"),

	# os/initialize.c
	0x80335910: main.sym_var("osClockRate", "u64"),
	0x80335918: main.sym_var("__osShutdown", "s32", flag={"DALIGN"}),

	# io/controller.c
	0x80335920: main.sym_var("__osContinitialized", "int", flag={"DALIGN"}),

	# io/aisetnextbuf.c
	0x80335930: main.sym_var("hdwrBugFlag", "u8", flag={"DALIGN"}),

	# os/timerintr.c
	0x80335940: main.sym_var("__osTimerList", "OSTimer *", flag={"DALIGN"}),

	# rmon/xprintf.c
	0x80335950: main.sym_var("spaces", "char", "[]"),
	0x80335974: main.sym_var("zeroes", "char", "[]"),

	# os/thread.c
	0x803359A0: main.sym_var("__osThreadTail", "__OSThreadTail"),
	0x803359A8: main.sym_var("__osRunQueue", "OSThread *", flag={"DALIGN"}),
	0x803359AC: main.sym_var("__osActiveQueue", "OSThread *", flag={"DALIGN"}),
	0x803359B0: main.sym_var("__osRunningThread", "OSThread *", flag={"DALIGN"}),
	0x803359B4: main.sym_var("__osFaultedThread", "OSThread *", flag={"DALIGN"}),

	# io/vi.c
	0x803359C0: main.sym_var("vi", "__OSViContext", "[2]"),
	0x80335A20: main.sym_var("__osViCurr", "__OSViContext *", flag={"DALIGN"}),
	0x80335A24: main.sym_var("__osViNext", "__OSViContext *", flag={"DALIGN"}),
	0x80335A28: main.sym_var("osViNtscEnabled", "u32", flag={"DALIGN"}),
	0x80335A2C: main.sym_var("osViClock", "u32", flag={"DALIGN"}),

	# os/exceptasm.s
	0x80335A30: main.sym("__osHwIntTable"),
	0x80335A44: main.sym("__osIsRdbWrite"),
	0x80335A48: main.sym("__osIsRdbRead"),

	# io/piacs.c
	0x80335A50: main.sym_var("__osPiAccessQueueEnabled", "int", flag={"DALIGN"}),

	# io/siacs.c
	0x80335A60: main.sym_var("__osSiAccessQueueEnabled", "int", flag={"DALIGN"}),

	# rmon/xlitob.c
	0x80335A70: main.sym_var("ldigs", "char", "[]"),
	0x80335A84: main.sym_var("udigs", "char", "[]"),

	# vimodentsclan1.c
	0x80335AA0: main.sym_var("osViModeNtscLan1", "OSViMode"),

	# vimodepallan1.c
	0x80335AF0: main.sym_var("osViModePalLan1", "OSViMode"),

	# os/kdebugserver.c
	0x80335B40: main.sym_var("debug_state", "u32", flag={"DALIGN"}),
	0x80335B44: main.sym_var("numChars", "u32", flag={"DALIGN"}),
	0x80335B48: main.sym_var("numCharsToReceive", "u32", flag={"DALIGN"}),

	# os/syncputchars.c
	0x80335B50: main.sym_var("__osRdbSendMessage", "unsigned int", flag={"DALIGN"}),
	0x80335B54: main.sym_var("__osRdbWriteOK", "unsigned int", flag={"DALIGN"}),

	# ==========================================================================
	# rodata
	# ==========================================================================

	# src/main.c
	0x80335B60: main.sym_var_fnc("main_80335B60", "const", "[]"),

	# src/graphics.c
	0x80335B80: main.sym_var("str_gfx_buf", "const char", "[]"),

	# src/audio.c
	0x80335B90: main.sym_var("audio_80335B90", "const float"),

	# src/game.c
	0x80335BA0: main.sym_var("str_01_0", "static const char", "[]"),
	0x80335BB0: main.sym_var("str_01_1", "static const char", "[]"),
	0x80335BC4: main.sym_var("str_02_0", "static const char", "[]"),
	0x80335BDC: main.sym_var("str_02_1", "static const char", "[]"),
	0x80335BF0: main.sym_var("str_02_2", "static const char", "[]"),
	0x80335C00: main.sym_var("str_03_0", "static const char", "[]"),
	0x80335C14: main.sym_var("str_03_1", "static const char", "[]"),
	0x80335C28: main.sym_var("str_03_2", "static const char", "[]"),
	0x80335C3C: main.sym_var("str_04_0", "static const char", "[]"),
	0x80335C4C: main.sym_var("str_04_1", "static const char", "[]"),
	0x80335C5C: main.sym_var("str_04_2", "static const char", "[]"),
	0x80335C6C: main.sym_var("str_04_3", "static const char", "[]"),
	0x80335C7C: main.sym_var("str_05_0", "static const char", "[]"),
	0x80335C90: main.sym_var("str_05_1", "static const char", "[]"),
	0x80335CA8: main.sym_var("str_05_2", "static const char", "[]"),
	0x80335CB8: main.sym_var("str_05_3", "static const char", "[]"),
	0x80335CC8: main.sym_var("str_06_0", "static const char", "[]"),
	0x80335CDC: main.sym_var("str_06_1", "static const char", "[]"),
	0x80335CEC: main.sym_var("str_06_2", "static const char", "[]"),
	0x80335D00: main.sym_var("str_07_0", "static const char", "[]"),
	0x80335D14: main.sym_var("str_07_1", "static const char", "[]"),
	0x80335D20: main.sym_var("str_07_2", "static const char", "[]"),
	0x80335D2C: main.sym_var("str_08_0", "static const char", "[]"),
	0x80335D40: main.sym_var("str_08_1", "static const char", "[]"),
	0x80335D54: main.sym_var("str_08_2", "static const char", "[]"),
	0x80335D64: main.sym_var("str_08_3", "static const char", "[]"),
	0x80335D74: main.sym_var("str_09_0", "static const char", "[]"),
	0x80335D84: main.sym_var("str_09_1", "static const char", "[]"),
	0x80335D90: main.sym_var("str_10_0", "static const char", "[]"),
	0x80335DA0: main.sym_var("str_10_1", "static const char", "[]"),
	0x80335DB4: main.sym_var("str_10_2", "static const char", "[]"),
	0x80335DC4: main.sym_var("str_10_3", "static const char", "[]"),
	0x80335DD4: main.sym_var("str_11_0", "static const char", "[]"),
	0x80335DE4: main.sym_var("str_11_1", "static const char", "[]"),
	0x80335DF8: main.sym_var("str_11_2", "static const char", "[]"),
	0x80335E08: main.sym_var("str_12_0", "static const char", "[]"),
	0x80335E20: main.sym_var("str_12_1", "static const char", "[]"),
	0x80335E30: main.sym_var("str_13_0", "static const char", "[]"),
	0x80335E44: main.sym_var("str_13_1", "static const char", "[]"),
	0x80335E54: main.sym_var("str_13_2", "static const char", "[]"),
	0x80335E68: main.sym_var("str_13_3", "static const char", "[]"),
	0x80335E74: main.sym_var("str_14_0", "static const char", "[]"),
	0x80335E88: main.sym_var("str_14_1", "static const char", "[]"),
	0x80335EA0: main.sym_var("str_15_0", "static const char", "[]"),
	0x80335EB8: main.sym_var("str_15_1", "static const char", "[]"),
	0x80335EC8: main.sym_var("str_15_2", "static const char", "[]"),
	0x80335ED4: main.sym_var("str_16_0", "static const char", "[]"),
	0x80335EE8: main.sym_var("str_16_1", "static const char", "[]"),
	0x80335EF4: main.sym_var("str_16_2", "static const char", "[]"),
	0x80335F00: main.sym_var("str_16_3", "static const char", "[]"),
	0x80335F0C: main.sym_var("str_16_4", "static const char", "[]"),
	0x80335F18: main.sym_var("str_17_0", "static const char", "[]"),
	0x80335F28: main.sym_var("str_17_1", "static const char", "[]"),
	0x80335F34: main.sym_var("str_17_2", "static const char", "[]"),
	0x80335F48: main.sym_var("str_17_3", "static const char", "[]"),
	0x80335F54: main.sym_var("str_18_0", "static const char", "[]"),
	0x80335F68: main.sym_var("str_18_1", "static const char", "[]"),
	0x80335F74: main.sym_var("str_18_2", "static const char", "[]"),
	0x80335F8C: main.sym_var("str_18_3", "static const char", "[]"),
	0x80335FA0: main.sym_var("str_19_0", "static const char", "[]"),
	0x80335FAC: main.sym_var("str_19_1", "static const char", "[]"),
	0x80335FC0: main.sym_var("str_20_0", "static const char", "[]"),
	0x80335FD4: main.sym_var("str_20_1", "static const char", "[]"),
	0x80335FE8: main.sym_var_fnc("game_80335FE8", "const", "[]"),
	0x8033607C: main.sym_var_fnc("game_8033607C", "const", "[]"),
	0x80336118: main.sym_var_fnc("game_80336118", "const", "[]"),
	0x8033617C: main.sym_var_fnc("game_8033617C", "const", "[]"),
	0x80336190: main.sym_var_fnc("game_80336190", "const", "[]"),

	# src/collision.c
	0x803361B0: main.sym_var_fnc("collision_803361B0", "const", "[]"),
	0x80336230: main.sym_var_fnc("collision_80336230", "const", "[]"),
	0x803362F8: main.sym_var_fnc("collision_803362F8", "const", "[]"),
	0x80336410: main.sym_var("collision_80336410", "const float"),
	0x80336414: main.sym_var("collision_80336414", "const float"),
	0x80336418: main.sym_var("collision_80336418", "const float"),

	# src/player.c
	0x80336420: main.sym_var("str_player_ang", "const char", "[]"),
	0x80336428: main.sym_var("str_player_spd", "const char", "[]"),
	0x80336430: main.sym_var("str_player_sta", "const char", "[]"),
	0x80336438: main.sym_var_fnc("player_80336438", "const", "[]"),
	0x80336458: main.sym_var_fnc("player_80336458", "const", "[]"),
	0x803364EC: main.sym_var_fnc("player_803364EC", "const", "[]"),
	0x8033650C: main.sym_var_fnc("player_8033650C", "const", "[]"),
	0x803365A0: main.sym_var("player_803365A0", "const float"),
	0x803365A4: main.sym_var("player_803365A4", "const float"),
	0x803365A8: main.sym_var("player_803365A8", "const float"),
	0x803365AC: main.sym_var("player_803365AC", "const float"),
	0x803365B0: main.sym_var("player_803365B0", "const float"),
	0x803365B4: main.sym_var("player_803365B4", "const float"),
	0x803365B8: main.sym_var("player_803365B8", "const float"),
	0x803365BC: main.sym_var("player_803365BC", "const float"),
	0x803365C0: main.sym_var("player_803365C0", "const float"),
	0x803365C4: main.sym_var("player_803365C4", "const float"),
	0x803365C8: main.sym_var("player_803365C8", "const float"),
	0x803365CC: main.sym_var("player_803365CC", "const float"),
	0x803365D0: main.sym_var("player_803365D0", "const float"),
	0x803365D4: main.sym_var_fnc("player_803365D4", "const", "[]"),
	0x80336658: main.sym_var("player_80336658", "const float"),
	0x8033665C: main.sym_var("player_8033665C", "const float"),
	0x80336660: main.sym_var("player_80336660", "const float"),
	0x80336664: main.sym_var("player_80336664", "const float"),
	0x80336668: main.sym_var("player_80336668", "const float"),

	# src/physics.c
	0x80336670: main.sym_var("physics_80336670", "const float"),
	0x80336674: main.sym_var("physics_80336674", "const float"),
	0x80336678: main.sym_var_fnc("physics_80336678", "const", "[]"),
	0x803366AC: main.sym_var("physics_803366AC", "const float"),
	0x803366B0: main.sym_var("physics_803366B0", "const float"),
	0x803366B4: main.sym_var("physics_803366B4", "const float"),
	0x803366B8: main.sym_var("physics_803366B8", "const float"),
	0x803366BC: main.sym_var("physics_803366BC", "const float"),
	0x803366C0: main.sym_var("physics_803366C0", "const float"),

	# src/pldemo.c
	0x803366D0: main.sym_var("pldemo_803366D0", "const float"),
	0x803366D4: main.sym_var_fnc("pldemo_803366D4", "const", "[]"),
	0x803366E8: main.sym_var("pldemo_803366E8", "const float"),
	0x803366EC: main.sym_var_fnc("pldemo_803366EC", "const", "[]"),
	0x80336708: main.sym_var("pldemo_80336708", "const float"),
	0x8033670C: main.sym_var("pldemo_8033670C", "const float"),
	0x80336710: main.sym_var("pldemo_80336710", "const float"),
	0x80336714: main.sym_var("pldemo_80336714", "const float"),
	0x80336718: main.sym_var("pldemo_80336718", "const float"),
	0x8033671C: main.sym_var("pldemo_8033671C", "const float"),
	0x80336720: main.sym_var_fnc("pldemo_80336720", "const", "[]"),
	0x80336754: main.sym_var_fnc("pldemo_80336754", "const", "[]"),
	0x80336770: main.sym_var_fnc("pldemo_80336770", "const", "[]"),
	0x80336784: main.sym_var_fnc("pldemo_80336784", "const", "[]"),
	0x80336848: main.sym_var_fnc("pldemo_80336848", "const", "[]"),

	# src/plspec.c
	0x80336940: main.sym_var("plspec_80336940", "const float"),
	0x80336944: main.sym_var("plspec_80336944", "const float"),
	0x80336948: main.sym_var("plspec_80336948", "const float"),
	0x8033694C: main.sym_var("plspec_8033694C", "const float"),
	0x80336950: main.sym_var_fnc("plspec_80336950", "const", "[]"),

	# src/plwait.c
	0x80336970: main.sym_var("plwait_80336970", "const float"),
	0x80336974: main.sym_var("plwait_80336974", "const float"),
	0x80336978: main.sym_var_fnc("plwait_80336978", "const", "[]"),
	0x803369A4: main.sym_var_fnc("plwait_803369A4", "const", "[]"),
	0x803369B8: main.sym_var_fnc("plwait_803369B8", "const", "[]"),
	0x80336A18: main.sym_var_fnc("plwait_80336A18", "const", "[]"),

	# src/plmove.c
	0x80336A80: main.sym_var("plmove_80336A80", "const float"),
	0x80336A84: main.sym_var("plmove_80336A84", "const float"),
	0x80336A88: main.sym_var("plmove_80336A88", "const float"),
	0x80336A8C: main.sym_var("plmove_80336A8C", "const float"),
	0x80336A90: main.sym_var("plmove_80336A90", "const float"),
	0x80336A94: main.sym_var("plmove_80336A94", "const float"),
	0x80336A98: main.sym_var("plmove_80336A98", "const float"),
	0x80336A9C: main.sym_var("plmove_80336A9C", "const float"),
	0x80336AA0: main.sym_var("plmove_80336AA0", "const float"),
	0x80336AA4: main.sym_var("plmove_80336AA4", "const float"),
	0x80336AA8: main.sym_var("plmove_80336AA8", "const float"),
	0x80336AAC: main.sym_var("plmove_80336AAC", "const float"),
	0x80336AB0: main.sym_var("plmove_80336AB0", "const float"),
	0x80336AB4: main.sym_var("plmove_80336AB4", "const float"),
	0x80336AB8: main.sym_var("plmove_80336AB8", "const float"),
	0x80336ABC: main.sym_var("plmove_80336ABC", "const float"),
	0x80336AC0: main.sym_var("plmove_80336AC0", "const float"),
	0x80336AC4: main.sym_var("plmove_80336AC4", "const float"),
	0x80336AC8: main.sym_var("plmove_80336AC8", "const float"),
	0x80336ACC: main.sym_var("plmove_80336ACC", "const float"),
	0x80336AD0: main.sym_var("plmove_80336AD0", "const float"),
	0x80336AD4: main.sym_var("plmove_80336AD4", "const float"),
	0x80336AD8: main.sym_var("plmove_80336AD8", "const float"),
	0x80336ADC: main.sym_var("plmove_80336ADC", "const float"),
	0x80336AE0: main.sym_var("plmove_80336AE0", "const float"),
	0x80336AE4: main.sym_var("plmove_80336AE4", "const float"),
	0x80336AE8: main.sym_var("plmove_80336AE8", "const float"),
	0x80336AEC: main.sym_var("plmove_80336AEC", "const float"),
	0x80336AF0: main.sym_var("plmove_80336AF0", "const float"),
	0x80336AF8: main.sym_var("plmove_80336AF8", "const double"),
	0x80336B00: main.sym_var("plmove_80336B00", "const float"),
	0x80336B04: main.sym_var("plmove_80336B04", "const float"),
	0x80336B08: main.sym_var("plmove_80336B08", "const float"),
	0x80336B0C: main.sym_var_fnc("plmove_80336B0C", "const", "[]"),
	0x80336B38: main.sym_var_fnc("plmove_80336B38", "const", "[]"),
	0x80336BB4: main.sym_var_fnc("plmove_80336BB4", "const", "[]"),
	0x80336BCC: main.sym_var_fnc("plmove_80336BCC", "const", "[]"),

	# src/pljump.c
	0x80336C00: main.sym_var("pljump_80336C00", "const float"),
	0x80336C04: main.sym_var("pljump_80336C04", "const float"),
	0x80336C08: main.sym_var("pljump_80336C08", "const float"),
	0x80336C0C: main.sym_var("pljump_80336C0C", "const float"),
	0x80336C10: main.sym_var("pljump_80336C10", "const float"),
	0x80336C14: main.sym_var("pljump_80336C14", "const float"),
	0x80336C18: main.sym_var("pljump_80336C18", "const float"),
	0x80336C1C: main.sym_var_fnc("pljump_80336C1C", "const", "[]"),
	0x80336C38: main.sym_var("pljump_80336C38", "const float"),
	0x80336C3C: main.sym_var("pljump_80336C3C", "const float"),
	0x80336C40: main.sym_var("pljump_80336C40", "const float"),
	0x80336C44: main.sym_var("pljump_80336C44", "const float"),
	0x80336C48: main.sym_var("pljump_80336C48", "const float"),
	0x80336C4C: main.sym_var("pljump_80336C4C", "const float"),
	0x80336C50: main.sym_var("pljump_80336C50", "const float"),
	0x80336C54: main.sym_var("pljump_80336C54", "const float"),
	0x80336C58: main.sym_var("pljump_80336C58", "const double"),
	0x80336C60: main.sym_var_fnc("pljump_80336C60", "const", "[]"),
	0x80336D20: main.sym_var_fnc("pljump_80336D20", "const", "[]"),
	0x80336D5C: main.sym_var_fnc("pljump_80336D5C", "const", "[]"),

	# src/plswim.c
	0x80336E10: main.sym_var("plswim_80336E10", "const float"),
	0x80336E14: main.sym_var_fnc("plswim_80336E14", "const", "[]"),
	0x80336E2C: main.sym_var_fnc("plswim_80336E2C", "const", "[]"),
	0x80336E44: main.sym_var("plswim_80336E44", "const float"),
	0x80336E48: main.sym_var("plswim_80336E48", "const float"),
	0x80336E4C: main.sym_var("plswim_80336E4C", "const float"),
	0x80336E50: main.sym_var("plswim_80336E50", "const float"),
	0x80336E54: main.sym_var("plswim_80336E54", "const float"),
	0x80336E58: main.sym_var("plswim_80336E58", "const float"),
	0x80336E5C: main.sym_var_fnc("plswim_80336E5C", "const", "[]"),
	0x80336EA4: main.sym_var_fnc("plswim_80336EA4", "const", "[]"),

	# src/pltake.c
	0x80336ED0: main.sym_var_fnc("pltake_80336ED0", "const", "[]"),
	0x80336EF8: main.sym_var_fnc("pltake_80336EF8", "const", "[]"),

	# src/callback.c
	0x80336F40: main.sym_var_fnc("callback_80336F40", "const", "[]"),
	0x80336F54: main.sym_var("callback_80336F54", "const float"),
	0x80336F58: main.sym_var("callback_80336F58", "const float"),
	0x80336F60: main.sym_var("callback_80336F60", "const double"),
	0x80336F68: main.sym_var("callback_80336F68", "const double"),

	# src/scene.c
	0x80336F70: main.sym_var("str_scene_no_controller", "const char", "[]"),
	0x80336F80: main.sym_var("str_scene_press", "const char", "[]"),
	0x80336F88: main.sym_var("str_scene_start", "const char", "[]"),

	# src/draw.c
	0x80336F90: main.sym_var("str_draw_mem", "const char", "[]"),
	0x80336F98: main.sym_var("draw_80336F98", "const float"),
	0x80336F9C: main.sym_var_fnc("draw_80336F9C", "const", "[]"),
	0x8033704C: main.sym_var_fnc("draw_8033704C", "const", "[]"),

	# src/camera.c
	0x803370F0: main.sym_var_fnc("camera_803370F0", "const", "[]"),
	0x80337118: main.sym_var("camera_80337118", "const float"),
	0x8033711C: main.sym_var("camera_8033711C", "const float"),
	0x80337120: main.sym_var_fnc("camera_80337120", "const", "[]"),
	0x80337148: main.sym_var("camera_80337148", "const float"),
	0x8033714C: main.sym_var("camera_8033714C", "const float"),
	0x80337150: main.sym_var("camera_80337150", "const float"),
	0x80337154: main.sym_var("camera_80337154", "const float"),
	0x80337158: main.sym_var("camera_80337158", "const float"),
	0x8033715C: main.sym_var("camera_8033715C", "const float"),
	0x80337160: main.sym_var("camera_80337160", "const float"),
	0x80337164: main.sym_var("camera_80337164", "const float"),
	0x80337168: main.sym_var("camera_80337168", "const float"),
	0x8033716C: main.sym_var("camera_8033716C", "const float"),
	0x80337170: main.sym_var("camera_80337170", "const float"),
	0x80337174: main.sym_var("camera_80337174", "const float"),
	0x80337178: main.sym_var("camera_80337178", "const float"),
	0x8033717C: main.sym_var("camera_8033717C", "const float"),
	0x80337180: main.sym_var("camera_80337180", "const float"),
	0x80337184: main.sym_var("camera_80337184", "const float"),
	0x80337188: main.sym_var("camera_80337188", "const float"),
	0x8033718C: main.sym_var("camera_8033718C", "const float"),
	0x80337190: main.sym_var("camera_80337190", "const float"),
	0x80337194: main.sym_var("camera_80337194", "const float"),
	0x80337198: main.sym_var("camera_80337198", "const float"),
	0x8033719C: main.sym_var("camera_8033719C", "const float"),
	0x803371A0: main.sym_var("camera_803371A0", "const float"),
	0x803371A4: main.sym_var("camera_803371A4", "const float"),
	0x803371A8: main.sym_var("camera_803371A8", "const float"),
	0x803371AC: main.sym_var("camera_803371AC", "const float"),
	0x803371B0: main.sym_var("camera_803371B0", "const float"),
	0x803371B4: main.sym_var("camera_803371B4", "const float"),
	0x803371B8: main.sym_var("camera_803371B8", "const float"),
	0x803371BC: main.sym_var("camera_803371BC", "const float"),
	0x803371C0: main.sym_var("camera_803371C0", "const float"),
	0x803371C4: main.sym_var("camera_803371C4", "const float"),
	0x803371C8: main.sym_var("camera_803371C8", "const float"),
	0x803371CC: main.sym_var("camera_803371CC", "const float"),
	0x803371D0: main.sym_var("camera_803371D0", "const float"),
	0x803371D4: main.sym_var("camera_803371D4", "const float"),
	0x803371D8: main.sym_var("camera_803371D8", "const float"),
	0x803371DC: main.sym_var("camera_803371DC", "const float"),
	0x803371E0: main.sym_var("camera_803371E0", "const float"),
	0x803371E4: main.sym_var("camera_803371E4", "const float"),
	0x803371E8: main.sym_var("camera_803371E8", "const float"),
	0x803371EC: main.sym_var("camera_803371EC", "const float"),
	0x803371F0: main.sym_var("camera_803371F0", "const float"),
	0x803371F4: main.sym_var("camera_803371F4", "const float"),
	0x803371F8: main.sym_var("camera_803371F8", "const float"),
	0x803371FC: main.sym_var("camera_803371FC", "const float"),
	0x80337200: main.sym_var("camera_80337200", "const float"),
	0x80337204: main.sym_var("camera_80337204", "const float"),
	0x80337208: main.sym_var("camera_80337208", "const float"),
	0x8033720C: main.sym_var("camera_8033720C", "const float"),
	0x80337210: main.sym_var("camera_80337210", "const float"),
	0x80337214: main.sym_var("camera_80337214", "const float"),
	0x80337218: main.sym_var_fnc("camera_80337218", "const", "[]"),
	0x8033725C: main.sym_var("camera_8033725C", "const float"),
	0x80337260: main.sym_var("camera_80337260", "const float"),
	0x80337264: main.sym_var("camera_80337264", "const float"),
	0x80337268: main.sym_var("camera_80337268", "const float"),
	0x8033726C: main.sym_var_fnc("camera_8033726C", "const", "[]"),
	0x803372E0: main.sym_var("camera_803372E0", "const float"),
	0x803372E4: main.sym_var("camera_803372E4", "const float"),
	0x803372E8: main.sym_var("camera_803372E8", "const float"),
	0x803372EC: main.sym_var("camera_803372EC", "const float"),
	0x803372F0: main.sym_var("camera_803372F0", "const float"),
	0x803372F4: main.sym_var("camera_803372F4", "const float"),
	0x803372F8: main.sym_var("camera_803372F8", "const float"),
	0x803372FC: main.sym_var("camera_803372FC", "const float"),
	0x80337300: main.sym_var("camera_80337300", "const float"),
	0x80337304: main.sym_var_fnc("camera_80337304", "const", "[]"),
	0x8033731C: main.sym_var("camera_8033731C", "const float"),
	0x80337320: main.sym_var("camera_80337320", "const float"),
	0x80337324: main.sym_var("camera_80337324", "const float"),
	0x80337328: main.sym_var("camera_80337328", "const float"),
	0x8033732C: main.sym_var("camera_8033732C", "const float"),
	0x80337330: main.sym_var("camera_80337330", "const float"),
	0x80337334: main.sym_var("camera_80337334", "const float"),
	0x80337338: main.sym_var("camera_80337338", "const float"),
	0x8033733C: main.sym_var_fnc("camera_8033733C", "const", "[]"),
	0x80337354: main.sym_var_fnc("camera_80337354", "const", "[]"),
	0x80337368: main.sym_var("camera_80337368", "const float"),
	0x8033736C: main.sym_var("camera_8033736C", "const float"),
	0x80337370: main.sym_var("camera_80337370", "const float"),
	0x80337374: main.sym_var("camera_80337374", "const float"),
	0x80337378: main.sym_var("camera_80337378", "const float"),
	0x8033737C: main.sym_var("camera_8033737C", "const float"),
	0x80337380: main.sym_var("camera_80337380", "const float"),
	0x80337384: main.sym_var("camera_80337384", "const float"),
	0x80337388: main.sym_var("camera_80337388", "const float"),
	0x8033738C: main.sym_var("camera_8033738C", "const float"),
	0x80337390: main.sym_var("camera_80337390", "const float"),
	0x80337394: main.sym_var("camera_80337394", "const float"),
	0x80337398: main.sym_var("camera_80337398", "const float"),
	0x8033739C: main.sym_var("camera_8033739C", "const float"),
	0x803373A0: main.sym_var("camera_803373A0", "const float"),
	0x803373A4: main.sym_var("camera_803373A4", "const float"),
	0x803373A8: main.sym_var("camera_803373A8", "const float"),
	0x803373AC: main.sym_var("camera_803373AC", "const float"),
	0x803373B0: main.sym_var("camera_803373B0", "const float"),
	0x803373B4: main.sym_var("camera_803373B4", "const float"),
	0x803373B8: main.sym_var("camera_803373B8", "const float"),
	0x803373BC: main.sym_var("camera_803373BC", "const float"),
	0x803373C0: main.sym_var("camera_803373C0", "const float"),
	0x803373C4: main.sym_var("camera_803373C4", "const float"),
	0x803373C8: main.sym_var("camera_803373C8", "const float"),
	0x803373CC: main.sym_var("camera_803373CC", "const float"),
	0x803373D0: main.sym_var("camera_803373D0", "const float"),
	0x803373D4: main.sym_var("camera_803373D4", "const float"),
	0x803373D8: main.sym_var("camera_803373D8", "const float"),
	0x803373DC: main.sym_var("camera_803373DC", "const float"),
	0x803373E0: main.sym_var("camera_803373E0", "const float"),
	0x803373E4: main.sym_var("camera_803373E4", "const float"),
	0x803373E8: main.sym_var("camera_803373E8", "const float"),
	0x803373EC: main.sym_var("camera_803373EC", "const float"),
	0x803373F0: main.sym_var("camera_803373F0", "const float"),
	0x803373F4: main.sym_var("camera_803373F4", "const float"),
	0x803373F8: main.sym_var("camera_803373F8", "const float"),
	0x803373FC: main.sym_var("camera_803373FC", "const float"),
	0x80337400: main.sym_var("camera_80337400", "const float"),
	0x80337404: main.sym_var("camera_80337404", "const float"),
	0x80337408: main.sym_var("camera_80337408", "const float"),
	0x8033740C: main.sym_var("camera_8033740C", "const float"),
	0x80337410: main.sym_var("camera_80337410", "const float"),
	0x80337414: main.sym_var("camera_80337414", "const float"),
	0x80337418: main.sym_var("camera_80337418", "const float"),
	0x8033741C: main.sym_var("camera_8033741C", "const float"),
	0x80337420: main.sym_var("camera_80337420", "const float"),
	0x80337424: main.sym_var("camera_80337424", "const float"),
	0x80337428: main.sym_var("camera_80337428", "const float"),
	0x8033742C: main.sym_var("camera_8033742C", "const float"),
	0x80337430: main.sym_var("camera_80337430", "const float"),
	0x80337434: main.sym_var("camera_80337434", "const float"),
	0x80337438: main.sym_var("camera_80337438", "const float"),
	0x8033743C: main.sym_var("camera_8033743C", "const float"),
	0x80337440: main.sym_var_fnc("camera_80337440", "const", "[]"),
	0x80337644: main.sym_var("camera_80337644", "const float"),
	0x80337648: main.sym_var("camera_80337648", "const float"),
	0x8033764C: main.sym_var("camera_8033764C", "const float"),
	0x80337650: main.sym_var("camera_80337650", "const float"),
	0x80337654: main.sym_var("camera_80337654", "const float"),
	0x80337658: main.sym_var("camera_80337658", "const float"),
	0x8033765C: main.sym_var("camera_8033765C", "const float"),
	0x80337660: main.sym_var("camera_80337660", "const float"),
	0x80337664: main.sym_var("camera_80337664", "const float"),
	0x80337668: main.sym_var_fnc("camera_80337668", "const", "[]"),
	0x80337738: main.sym_var_fnc("camera_80337738", "const", "[]"),
	0x8033776C: main.sym_var("camera_8033776C", "const float"),
	0x80337770: main.sym_var("camera_80337770", "const float"),
	0x80337774: main.sym_var("camera_80337774", "const float"),
	0x80337778: main.sym_var("camera_80337778", "const float"),
	0x8033777C: main.sym_var("camera_8033777C", "const float"),
	0x80337780: main.sym_var_fnc("camera_80337780", "const", "[]"),

	# src/object.c
	0x803377A0: main.sym_var("object_803377A0", "const double"),
	0x803377A8: main.sym_var("object_803377A8", "const double"),

	# src/objectlib.c
	0x803377B0: main.sym_var("str_objectlib_areainfo", "const char", "[]"),
	0x803377BC: main.sym_var("objectlib_803377BC", "const float"),
	0x803377C0: main.sym_var("objectlib_803377C0", "const float"),
	0x803377C4: main.sym_var("objectlib_803377C4", "const float"),
	0x803377C8: main.sym_var("objectlib_803377C8", "const float"),
	0x803377CC: main.sym_var("objectlib_803377CC", "const float"),
	0x803377D0: main.sym_var("objectlib_803377D0", "const float"),
	0x803377D8: main.sym_var("objectlib_803377D8", "const double"),
	0x803377E0: main.sym_var("objectlib_803377E0", "const double"),
	0x803377E8: main.sym_var("objectlib_803377E8", "const double"),
	0x803377F0: main.sym_var("objectlib_803377F0", "const float"),
	0x803377F4: main.sym_var("objectlib_803377F4", "const float"),
	0x803377F8: main.sym_var("objectlib_803377F8", "const double"),
	0x80337800: main.sym_var("objectlib_80337800", "const float"),
	0x80337808: main.sym_var("objectlib_80337808", "const double"),
	0x80337810: main.sym_var("objectlib_80337810", "const float"),
	0x80337814: main.sym_var("objectlib_80337814", "const float"),
	0x80337818: main.sym_var("objectlib_80337818", "const float"),
	0x8033781C: main.sym_var("objectlib_8033781C", "const float"),
	0x80337820: main.sym_var("objectlib_80337820", "const float"),
	0x80337824: main.sym_var("objectlib_80337824", "const float"),
	0x80337828: main.sym_var("objectlib_80337828", "const float"),
	0x8033782C: main.sym_var("objectlib_8033782C", "const float"),
	0x80337830: main.sym_var("objectlib_80337830", "const float"),
	0x80337834: main.sym_var_fnc("objectlib_80337834", "const", "[]"),

	# src/object_a.c
	0x80337850: main.sym_var("str_object_a_0_fmt", "const char", "[]"),
	0x80337854: main.sym_var("str_object_a_0_fg", "const char", "[]"),
	0x8033785C: main.sym_var("str_object_a_0_sp", "const char", "[]"),
	0x80337864: main.sym_var("str_object_a_1_fmt", "const char", "[]"),
	0x80337868: main.sym_var("str_object_a_1_md", "const char", "[]"),
	0x80337870: main.sym_var("str_object_a_1_sp", "const char", "[]"),
	0x80337878: main.sym_var("str_object_a_mode", "const char", "[]"),
	0x80337884: main.sym_var("str_object_a_action", "const char", "[]"),
	0x80337890: main.sym_var("str_object_a_number", "const char", "[]"),
	0x8033789C: main.sym_var("str_object_a_off", "const char", "[]"),
	0x803378A4: main.sym_var("str_object_a_x", "const char", "[]"),
	0x803378AC: main.sym_var("str_object_a_z", "const char", "[]"),
	0x803378B4: main.sym_var_fnc("object_a_803378B4", "const", "[]"),
	0x803378C8: main.sym_var("object_a_803378C8", "const double"),
	0x803378D0: main.sym_var("object_a_803378D0", "const double"),
	0x803378D8: main.sym_var("object_a_803378D8", "const double"),
	0x803378E0: main.sym_var("object_a_803378E0", "const float"),
	0x803378E8: main.sym_var("object_a_803378E8", "const double"),
	0x803378F0: main.sym_var("object_a_803378F0", "const float"),
	0x803378F4: main.sym_var("object_a_803378F4", "const float"),
	0x803378F8: main.sym_var("object_a_803378F8", "const float"),
	0x803378FC: main.sym_var("object_a_803378FC", "const float"),
	0x80337900: main.sym_var("object_a_80337900", "const float"),
	0x80337904: main.sym_var_fnc("object_a_80337904", "const", "[]"),
	0x80337918: main.sym_var("object_a_80337918", "const float"),
	0x80337920: main.sym_var("object_a_80337920", "const double"),
	0x80337928: main.sym_var("object_a_80337928", "const double"),
	0x80337930: main.sym_var("object_a_80337930", "const double"),
	0x80337938: main.sym_var("object_a_80337938", "const double"),
	0x80337940: main.sym_var("object_a_80337940", "const float"),
	0x80337944: main.sym_var("object_a_80337944", "const float"),
	0x80337948: main.sym_var("object_a_80337948", "const float"),
	0x8033794C: main.sym_var("object_a_8033794C", "const float"),
	0x80337950: main.sym_var("object_a_80337950", "const double"),
	0x80337958: main.sym_var("object_a_80337958", "const double"),
	0x80337960: main.sym_var("object_a_80337960", "const float"),
	0x80337968: main.sym_var("object_a_80337968", "const double"),
	0x80337970: main.sym_var("object_a_80337970", "const float"),
	0x80337974: main.sym_var_fnc("object_a_80337974", "const", "[]"),
	0x80337988: main.sym_var("object_a_80337988", "const double"),
	0x80337990: main.sym_var("object_a_80337990", "const float"),
	0x80337994: main.sym_var("object_a_80337994", "const float"),
	0x80337998: main.sym_var("object_a_80337998", "const float"),
	0x8033799C: main.sym_var("object_a_8033799C", "const float"),
	0x803379A0: main.sym_var("object_a_803379A0", "const float"),
	0x803379A4: main.sym_var("object_a_803379A4", "const float"),
	0x803379A8: main.sym_var("object_a_803379A8", "const float"),
	0x803379AC: main.sym_var("object_a_803379AC", "const float"),
	0x803379B0: main.sym_var("object_a_803379B0", "const float"),
	0x803379B4: main.sym_var_fnc("object_a_803379B4", "const", "[]"),
	0x803379C8: main.sym_var("object_a_803379C8", "const float"),
	0x803379D0: main.sym_var("object_a_803379D0", "const double"),
	0x803379D8: main.sym_var("object_a_803379D8", "const float"),
	0x803379E0: main.sym_var("object_a_803379E0", "const double"),
	0x803379E8: main.sym_var("object_a_803379E8", "const double"),
	0x803379F0: main.sym_var("object_a_803379F0", "const double"),
	0x803379F8: main.sym_var_fnc("object_a_803379F8", "const", "[]"),
	0x80337A20: main.sym_var("object_a_80337A20", "const double"),
	0x80337A28: main.sym_var("object_a_80337A28", "const float"),
	0x80337A30: main.sym_var("object_a_80337A30", "const double"),
	0x80337A38: main.sym_var("object_a_80337A38", "const double"),
	0x80337A40: main.sym_var_fnc("object_a_80337A40", "const", "[]"),
	0x80337A54: main.sym_var_fnc("object_a_80337A54", "const", "[]"),
	0x80337A68: main.sym_var("object_a_80337A68", "const double"),
	0x80337A70: main.sym_var("object_a_80337A70", "const double"),
	0x80337A78: main.sym_var("object_a_80337A78", "const float"),
	0x80337A7C: main.sym_var("object_a_80337A7C", "const float"),
	0x80337A80: main.sym_var("object_a_80337A80", "const float"),
	0x80337A84: main.sym_var("object_a_80337A84", "const float"),
	0x80337A88: main.sym_var("object_a_80337A88", "const float"),
	0x80337A8C: main.sym_var("object_a_80337A8C", "const float"),
	0x80337A90: main.sym_var("object_a_80337A90", "const double"),
	0x80337A98: main.sym_var_fnc("object_a_80337A98", "const", "[]"),
	0x80337AAC: main.sym_var("object_a_80337AAC", "const float"),
	0x80337AB0: main.sym_var("object_a_80337AB0", "const float"),
	0x80337AB8: main.sym_var("object_a_80337AB8", "const double"),
	0x80337AC0: main.sym_var("object_a_80337AC0", "const float"),
	0x80337AC4: main.sym_var("object_a_80337AC4", "const float"),
	0x80337AC8: main.sym_var("object_a_80337AC8", "const double"),
	0x80337AD0: main.sym_var("object_a_80337AD0", "const double"),
	0x80337AD8: main.sym_var("object_a_80337AD8", "const float"),
	0x80337ADC: main.sym_var("object_a_80337ADC", "const float"),
	0x80337AE0: main.sym_var("object_a_80337AE0", "const double"),
	0x80337AE8: main.sym_var("object_a_80337AE8", "const double"),
	0x80337AF0: main.sym_var("object_a_80337AF0", "const double"),
	0x80337AF8: main.sym_var("object_a_80337AF8", "const double"),
	0x80337B00: main.sym_var("object_a_80337B00", "const double"),
	0x80337B08: main.sym_var_fnc("object_a_80337B08", "const", "[]"),
	0x80337B38: main.sym_var("object_a_80337B38", "const double"),
	0x80337B40: main.sym_var("object_a_80337B40", "const double"),
	0x80337B48: main.sym_var("object_a_80337B48", "const float"),
	0x80337B4C: main.sym_var_fnc("object_a_80337B4C", "const", "[]"),
	0x80337B74: main.sym_var("object_a_80337B74", "const float"),
	0x80337B78: main.sym_var("object_a_80337B78", "const double"),
	0x80337B80: main.sym_var("object_a_80337B80", "const double"),
	0x80337B88: main.sym_var("object_a_80337B88", "const double"),
	0x80337B90: main.sym_var_fnc("object_a_80337B90", "const", "[]"),
	0x80337BA4: main.sym_var_fnc("object_a_80337BA4", "const", "[]"),
	0x80337BBC: main.sym_var("object_a_80337BBC", "const float"),
	0x80337BC0: main.sym_var("object_a_80337BC0", "const float"),
	0x80337BC4: main.sym_var("object_a_80337BC4", "const float"),
	0x80337BC8: main.sym_var("object_a_80337BC8", "const float"),
	0x80337BD0: main.sym_var("object_a_80337BD0", "const double"),
	0x80337BD8: main.sym_var("object_a_80337BD8", "const float"),
	0x80337BDC: main.sym_var("object_a_80337BDC", "const float"),
	0x80337BE0: main.sym_var("object_a_80337BE0", "const float"),
	0x80337BE4: main.sym_var("object_a_80337BE4", "const float"),
	0x80337BE8: main.sym_var("object_a_80337BE8", "const double"),
	0x80337BF0: main.sym_var("object_a_80337BF0", "const float"),
	0x80337BF4: main.sym_var("object_a_80337BF4", "const float"),
	0x80337BF8: main.sym_var("object_a_80337BF8", "const double"),
	0x80337C00: main.sym_var("object_a_80337C00", "const float"),
	0x80337C04: main.sym_var("object_a_80337C04", "const float"),
	0x80337C08: main.sym_var("object_a_80337C08", "const float"),
	0x80337C0C: main.sym_var("object_a_80337C0C", "const float"),
	0x80337C10: main.sym_var_fnc("object_a_80337C10", "const", "[]"),
	0x80337C30: main.sym_var("object_a_80337C30", "const float"),
	0x80337C34: main.sym_var_fnc("object_a_80337C34", "const", "[]"),
	0x80337C54: main.sym_var("object_a_80337C54", "const float"),
	0x80337C58: main.sym_var("object_a_80337C58", "const float"),
	0x80337C5C: main.sym_var("object_a_80337C5C", "const float"),
	0x80337C60: main.sym_var("object_a_80337C60", "const float"),
	0x80337C64: main.sym_var("object_a_80337C64", "const float"),
	0x80337C68: main.sym_var("object_a_80337C68", "const double"),
	0x80337C70: main.sym_var_fnc("object_a_80337C70", "const", "[]"),
	0x80337C84: main.sym_var("object_a_80337C84", "const float"),
	0x80337C88: main.sym_var("object_a_80337C88", "const double"),
	0x80337C90: main.sym_var("object_a_80337C90", "const float"),
	0x80337C98: main.sym_var("object_a_80337C98", "const double"),
	0x80337CA0: main.sym_var("object_a_80337CA0", "const double"),
	0x80337CA8: main.sym_var("object_a_80337CA8", "const float"),
	0x80337CB0: main.sym_var("object_a_80337CB0", "const double"),
	0x80337CB8: main.sym_var("object_a_80337CB8", "const float"),
	0x80337CBC: main.sym_var("object_a_80337CBC", "const float"),
	0x80337CC0: main.sym_var("object_a_80337CC0", "const float"),
	0x80337CC4: main.sym_var("object_a_80337CC4", "const float"),
	0x80337CC8: main.sym_var("object_a_80337CC8", "const float"),
	0x80337CCC: main.sym_var("object_a_80337CCC", "const float"),
	0x80337CD0: main.sym_var("object_a_80337CD0", "const float"),
	0x80337CD4: main.sym_var("object_a_80337CD4", "const float"),
	0x80337CD8: main.sym_var("object_a_80337CD8", "const double"),
	0x80337CE0: main.sym_var("object_a_80337CE0", "const double"),
	0x80337CE8: main.sym_var("object_a_80337CE8", "const double"),
	0x80337CF0: main.sym_var("object_a_80337CF0", "const float"),
	0x80337CF4: main.sym_var("object_a_80337CF4", "const float"),
	0x80337CF8: main.sym_var("object_a_80337CF8", "const double"),
	0x80337D00: main.sym_var("object_a_80337D00", "const float"),
	0x80337D04: main.sym_var("object_a_80337D04", "const float"),
	0x80337D08: main.sym_var("object_a_80337D08", "const float"),
	0x80337D10: main.sym_var("object_a_80337D10", "const double"),
	0x80337D18: main.sym_var("object_a_80337D18", "const float"),
	0x80337D20: main.sym_var("object_a_80337D20", "const double"),
	0x80337D28: main.sym_var("object_a_80337D28", "const double"),
	0x80337D30: main.sym_var("object_a_80337D30", "const double"),
	0x80337D38: main.sym_var("object_a_80337D38", "const float"),
	0x80337D3C: main.sym_var("object_a_80337D3C", "const float"),
	0x80337D40: main.sym_var("object_a_80337D40", "const float"),
	0x80337D44: main.sym_var("object_a_80337D44", "const float"),
	0x80337D48: main.sym_var("object_a_80337D48", "const float"),
	0x80337D50: main.sym_var("object_a_80337D50", "const double"),
	0x80337D58: main.sym_var("object_a_80337D58", "const double"),
	0x80337D60: main.sym_var("object_a_80337D60", "const double"),
	0x80337D68: main.sym_var("object_a_80337D68", "const double"),
	0x80337D70: main.sym_var("object_a_80337D70", "const float"),
	0x80337D74: main.sym_var("object_a_80337D74", "const float"),
	0x80337D78: main.sym_var("object_a_80337D78", "const float"),
	0x80337D7C: main.sym_var("object_a_80337D7C", "const float"),
	0x80337D80: main.sym_var("object_a_80337D80", "const float"),
	0x80337D84: main.sym_var("object_a_80337D84", "const float"),
	0x80337D88: main.sym_var("object_a_80337D88", "const float"),
	0x80337D8C: main.sym_var("object_a_80337D8C", "const float"),
	0x80337D90: main.sym_var("object_a_80337D90", "const float"),
	0x80337D94: main.sym_var("object_a_80337D94", "const float"),
	0x80337D98: main.sym_var_fnc("object_a_80337D98", "const", "[]"),
	0x80337DAC: main.sym_var_fnc("object_a_80337DAC", "const", "[]"),
	0x80337DC4: main.sym_var("object_a_80337DC4", "const float"),
	0x80337DC8: main.sym_var("object_a_80337DC8", "const float"),
	0x80337DCC: main.sym_var("object_a_80337DCC", "const float"),
	0x80337DD0: main.sym_var("object_a_80337DD0", "const float"),
	0x80337DD4: main.sym_var("object_a_80337DD4", "const float"),
	0x80337DD8: main.sym_var("object_a_80337DD8", "const float"),
	0x80337DE0: main.sym_var("object_a_80337DE0", "const double"),
	0x80337DE8: main.sym_var("object_a_80337DE8", "const float"),
	0x80337DEC: main.sym_var("object_a_80337DEC", "const float"),

	# src/hitcheck.c
	0x80337DF0: main.sym_var("str_hitcheck_on", "const char", "[]"),

	# src/objlist.c
	0x80337E00: main.sym_var("objlist_80337E00", "const float"),
	0x80337E04: main.sym_var("objlist_80337E04", "const float"),
	0x80337E08: main.sym_var("objlist_80337E08", "const float"),
	0x80337E0C: main.sym_var("objlist_80337E0C", "const float"),

	# src/objsound.c
	0x80337E10: main.sym_var("objsound_80337E10", "const float"),
	0x80337E14: main.sym_var("objsound_80337E14", "const float"),
	0x80337E18: main.sym_var("objsound_80337E18", "const float"),

	# src/debug.c
	0x80337E20: main.sym_var("str_debug_a0", "const char", "[]"),
	0x80337E28: main.sym_var("str_debug_a1", "const char", "[]"),
	0x80337E30: main.sym_var("str_debug_a2", "const char", "[]"),
	0x80337E38: main.sym_var("str_debug_a3", "const char", "[]"),
	0x80337E40: main.sym_var("str_debug_a4", "const char", "[]"),
	0x80337E48: main.sym_var("str_debug_a5", "const char", "[]"),
	0x80337E50: main.sym_var("str_debug_a6", "const char", "[]"),
	0x80337E58: main.sym_var("str_debug_a7", "const char", "[]"),
	0x80337E60: main.sym_var("str_debug_a", "const char", "[]"),
	0x80337E64: main.sym_var("str_debug_b0", "const char", "[]"),
	0x80337E6C: main.sym_var("str_debug_b1", "const char", "[]"),
	0x80337E74: main.sym_var("str_debug_b2", "const char", "[]"),
	0x80337E7C: main.sym_var("str_debug_b3", "const char", "[]"),
	0x80337E84: main.sym_var("str_debug_b4", "const char", "[]"),
	0x80337E8C: main.sym_var("str_debug_b5", "const char", "[]"),
	0x80337E94: main.sym_var("str_debug_b6", "const char", "[]"),
	0x80337E9C: main.sym_var("str_debug_b7", "const char", "[]"),
	0x80337EA4: main.sym_var("str_debug_b", "const char", "[]"),
	0x80337EA8: main.sym_var("str_debug_dprint_over", "const char", "[]"),
	0x80337EB4: main.sym_var("str_debug_mapinfo", "const char", "[]"),
	0x80337EBC: main.sym_var("str_debug_area", "const char", "[]"),
	0x80337EC4: main.sym_var("str_debug_wx", "const char", "[]"),
	0x80337ECC: main.sym_var("str_debug_wy", "const char", "[]"),
	0x80337ED4: main.sym_var("str_debug_wz", "const char", "[]"),
	0x80337EDC: main.sym_var("str_debug_bgy", "const char", "[]"),
	0x80337EE4: main.sym_var("str_debug_angy", "const char", "[]"),
	0x80337EEC: main.sym_var("str_debug_bgcode", "const char", "[]"),
	0x80337EF8: main.sym_var("str_debug_bgstatus", "const char", "[]"),
	0x80337F04: main.sym_var("str_debug_bgarea", "const char", "[]"),
	0x80337F10: main.sym_var("str_debug_water", "const char", "[]"),
	0x80337F1C: main.sym_var("str_DebugCheckinfo", "const char", "[]"),
	0x80337F28: main.sym_var("str_debug_stageinfo", "const char", "[]"),
	0x80337F34: main.sym_var("str_debug_stage_param", "const char", "[]"),
	0x80337F44: main.sym_var("str_debug_effectinfo", "const char", "[]"),
	0x80337F50: main.sym_var("str_debug_enemyinfo", "const char", "[]"),
	0x80337F5C: main.sym_var("str_debug_obj", "const char", "[]"),
	0x80337F64: main.sym_var("str_debug_nullbg", "const char", "[]"),
	0x80337F70: main.sym_var("str_debug_wall", "const char", "[]"),
	0x80337F7C: main.sym_var("str_debug_bound", "const char", "[]"),
	0x80337F88: main.sym_var("str_debug_touch", "const char", "[]"),
	0x80337F94: main.sym_var("str_debug_takeoff", "const char", "[]"),
	0x80337FA0: main.sym_var("str_debug_dive", "const char", "[]"),
	0x80337FAC: main.sym_var("str_debug_s_water", "const char", "[]"),
	0x80337FB8: main.sym_var("str_debug_u_water", "const char", "[]"),
	0x80337FC4: main.sym_var("str_debug_b_water", "const char", "[]"),
	0x80337FD0: main.sym_var("str_debug_sky", "const char", "[]"),
	0x80337FDC: main.sym_var("str_debug_out_scope", "const char", "[]"),
	0x80337FF0: main.sym_var("debug_80337FF0", "const double"),

	# src/wipe.c
	0x80338000: main.sym_var("wipe_80338000", "const double"),
	0x80338008: main.sym_var("wipe_80338008", "const double"),
	0x80338010: main.sym_var_fnc("wipe_80338010", "const", "[]"),

	# src/shadow.c
	0x80338060: main.sym_var("shadow_80338060", "const double"),
	0x80338068: main.sym_var("shadow_80338068", "const double"),
	0x80338070: main.sym_var("shadow_80338070", "const double"),
	0x80338078: main.sym_var("shadow_80338078", "const double"),
	0x80338080: main.sym_var("shadow_80338080", "const double"),
	0x80338088: main.sym_var("shadow_80338088", "const double"),
	0x80338090: main.sym_var("shadow_80338090", "const double"),
	0x80338098: main.sym_var("shadow_80338098", "const double"),
	0x803380A0: main.sym_var("shadow_803380A0", "const double"),
	0x803380A8: main.sym_var("shadow_803380A8", "const double"),
	0x803380B0: main.sym_var("shadow_803380B0", "const double"),
	0x803380B8: main.sym_var("shadow_803380B8", "const double"),
	0x803380C0: main.sym_var("shadow_803380C0", "const double"),
	0x803380C8: main.sym_var("shadow_803380C8", "const double"),
	0x803380D0: main.sym_var("shadow_803380D0", "const double"),
	0x803380D8: main.sym_var("shadow_803380D8", "const float"),
	0x803380E0: main.sym_var("shadow_803380E0", "const double"),
	0x803380E8: main.sym_var("shadow_803380E8", "const float"),
	0x803380F0: main.sym_var("shadow_803380F0", "const double"),
	0x803380F8: main.sym_var("shadow_803380F8", "const double"),
	0x80338100: main.sym_var("shadow_80338100", "const double"),
	0x80338108: main.sym_var_fnc("shadow_80338108", "const", "[]"),

	# src/background.c
	0x80338140: main.sym_var("background_80338140", "const double"),
	0x80338148: main.sym_var("background_80338148", "const double"),
	0x80338150: main.sym_var("background_80338150", "const double"),
	0x80338158: main.sym_var("background_80338158", "const double"),

	# src/water.c
	0x80338160: main.sym_var("water_80338160", "const double"),

	# src/wave.c
	0x80338170: main.sym_var("wave_80338170", "const double"),
	0x80338178: main.sym_var("wave_80338178", "const double"),
	0x80338180: main.sym_var("wave_80338180", "const double"),
	0x80338188: main.sym_var("wave_80338188", "const double"),
	0x80338190: main.sym_var("wave_80338190", "const double"),

	# src/message.c
	0x803381A0: main.sym_var("message_803381A0", "const double"),
	0x803381A8: main.sym_var("message_803381A8", "const double"),
	0x803381B0: main.sym_var("message_803381B0", "const double"),
	0x803381B8: main.sym_var_fnc("message_803381B8", "const", "[]"),

	# src/weather.c
	0x80338280: main.sym_var("weather_80338280", "const double"),
	0x80338288: main.sym_var("weather_80338288", "const double"),
	0x80338290: main.sym_var("weather_80338290", "const double"),
	0x80338298: main.sym_var("weather_80338298", "const double"),
	0x803382A0: main.sym_var("weather_803382A0", "const double"),
	0x803382A8: main.sym_var("weather_803382A8", "const double"),
	0x803382B0: main.sym_var("weather_803382B0", "const double"),

	# src/lava.c
	0x803382C0: main.sym_var("lava_803382C0", "const float"),
	0x803382C4: main.sym_var("lava_803382C4", "const float"),
	0x803382C8: main.sym_var("lava_803382C8", "const float"),
	0x803382CC: main.sym_var("lava_803382CC", "const float"),
	0x803382D0: main.sym_var("lava_803382D0", "const float"),
	0x803382D4: main.sym_var_fnc("lava_803382D4", "const", "[]"),

	# src/tag.c
	0x80338310: main.sym_var_fnc("tag_80338310", "const", "[]"),
	0x80338368: main.sym_var_fnc("tag_80338368", "const", "[]"),

	# src/hud.c
	0x80338380: main.sym_var("str_hud_life_icon", "const char", "[]"),
	0x80338384: main.sym_var("str_hud_life_x", "const char", "[]"),
	0x80338388: main.sym_var("str_hud_life_fmt", "const char", "[]"),
	0x8033838C: main.sym_var("str_hud_coin_icon", "const char", "[]"),
	0x80338390: main.sym_var("str_hud_coin_x", "const char", "[]"),
	0x80338394: main.sym_var("str_hud_coin_fmt", "const char", "[]"),
	0x80338398: main.sym_var("str_hud_star_icon", "const char", "[]"),
	0x8033839C: main.sym_var("str_hud_star_x", "const char", "[]"),
	0x803383A0: main.sym_var("str_hud_star_fmt", "const char", "[]"),
	0x803383A4: main.sym_var("str_hud_key", "const char", "[]"),
	0x803383A8: main.sym_var("str_hud_time_text", "const char", "[]"),
	0x803383B0: main.sym_var("str_hud_time_min", "const char", "[]"),
	0x803383B4: main.sym_var("str_hud_time_sec", "const char", "[]"),
	0x803383BC: main.sym_var("str_hud_time_frc", "const char", "[]"),
	0x803383C0: main.sym_var("hud_803383C0", "const double"),
	0x803383C8: main.sym_var("hud_803383C8", "const double"),

	# src/object_b.c
	0x803383D0: main.sym_var("object_b_803383D0", "const double"),
	0x803383D8: main.sym_var("object_b_803383D8", "const double"),
	0x803383E0: main.sym_var("object_b_803383E0", "const double"),
	0x803383E8: main.sym_var("object_b_803383E8", "const double"),
	0x803383F0: main.sym_var("object_b_803383F0", "const double"),
	0x803383F8: main.sym_var("object_b_803383F8", "const double"),
	0x80338400: main.sym_var("object_b_80338400", "const double"),
	0x80338408: main.sym_var("object_b_80338408", "const double"),
	0x80338410: main.sym_var("object_b_80338410", "const double"),
	0x80338418: main.sym_var("object_b_80338418", "const double"),
	0x80338420: main.sym_var("object_b_80338420", "const double"),
	0x80338428: main.sym_var("object_b_80338428", "const double"),
	0x80338430: main.sym_var("object_b_80338430", "const double"),
	0x80338438: main.sym_var("object_b_80338438", "const double"),
	0x80338440: main.sym_var("object_b_80338440", "const double"),
	0x80338448: main.sym_var("object_b_80338448", "const double"),
	0x80338450: main.sym_var("object_b_80338450", "const double"),
	0x80338458: main.sym_var("object_b_80338458", "const double"),
	0x80338460: main.sym_var("object_b_80338460", "const double"),
	0x80338468: main.sym_var("object_b_80338468", "const double"),
	0x80338470: main.sym_var("object_b_80338470", "const double"),
	0x80338478: main.sym_var("object_b_80338478", "const float"),
	0x80338480: main.sym_var("object_b_80338480", "const double"),
	0x80338488: main.sym_var("object_b_80338488", "const double"),
	0x80338490: main.sym_var("object_b_80338490", "const float"),
	0x80338494: main.sym_var_fnc("object_b_80338494", "const", "[]"),
	0x803384A8: main.sym_var_fnc("object_b_803384A8", "const", "[]"),
	0x803384BC: main.sym_var("object_b_803384BC", "const float"),
	0x803384C0: main.sym_var("object_b_803384C0", "const float"),
	0x803384C4: main.sym_var("object_b_803384C4", "const float"),
	0x803384C8: main.sym_var("object_b_803384C8", "const float"),
	0x803384CC: main.sym_var("object_b_803384CC", "const float"),
	0x803384D0: main.sym_var("object_b_803384D0", "const float"),
	0x803384D4: main.sym_var("object_b_803384D4", "const float"),
	0x803384D8: main.sym_var("object_b_803384D8", "const float"),
	0x803384DC: main.sym_var("object_b_803384DC", "const float"),
	0x803384E0: main.sym_var("object_b_803384E0", "const float"),
	0x803384E4: main.sym_var("object_b_803384E4", "const float"),
	0x803384E8: main.sym_var("object_b_803384E8", "const float"),
	0x803384EC: main.sym_var("object_b_803384EC", "const float"),
	0x803384F0: main.sym_var("object_b_803384F0", "const float"),
	0x803384F4: main.sym_var("object_b_803384F4", "const float"),
	0x803384F8: main.sym_var("object_b_803384F8", "const float"),
	0x803384FC: main.sym_var("object_b_803384FC", "const float"),
	0x80338500: main.sym_var("object_b_80338500", "const float"),
	0x80338508: main.sym_var("object_b_80338508", "const double"),
	0x80338510: main.sym_var("object_b_80338510", "const double"),
	0x80338518: main.sym_var_fnc("object_b_80338518", "const", "[]"),
	0x80338530: main.sym_var("object_b_80338530", "const double"),
	0x80338538: main.sym_var("object_b_80338538", "const float"),
	0x80338540: main.sym_var("object_b_80338540", "const double"),
	0x80338548: main.sym_var("object_b_80338548", "const double"),
	0x80338550: main.sym_var("object_b_80338550", "const double"),
	0x80338558: main.sym_var("object_b_80338558", "const double"),
	0x80338560: main.sym_var("object_b_80338560", "const double"),
	0x80338568: main.sym_var("object_b_80338568", "const double"),
	0x80338570: main.sym_var("object_b_80338570", "const float"),
	0x80338574: main.sym_var("object_b_80338574", "const float"),
	0x80338578: main.sym_var("object_b_80338578", "const float"),
	0x8033857C: main.sym_var("object_b_8033857C", "const float"),
	0x80338580: main.sym_var("object_b_80338580", "const float"),
	0x80338584: main.sym_var("object_b_80338584", "const float"),
	0x80338588: main.sym_var("object_b_80338588", "const float"),
	0x8033858C: main.sym_var("object_b_8033858C", "const float"),
	0x80338590: main.sym_var("object_b_80338590", "const float"),
	0x80338594: main.sym_var("object_b_80338594", "const float"),
	0x80338598: main.sym_var("object_b_80338598", "const float"),
	0x8033859C: main.sym_var_fnc("object_b_8033859C", "const", "[]"),
	0x803385B8: main.sym_var("object_b_803385B8", "const double"),
	0x803385C0: main.sym_var("object_b_803385C0", "const double"),
	0x803385C8: main.sym_var("object_b_803385C8", "const double"),
	0x803385D0: main.sym_var("object_b_803385D0", "const double"),
	0x803385D8: main.sym_var("object_b_803385D8", "const double"),
	0x803385E0: main.sym_var("object_b_803385E0", "const float"),
	0x803385E8: main.sym_var("object_b_803385E8", "const double"),
	0x803385F0: main.sym_var("object_b_803385F0", "const double"),
	0x803385F8: main.sym_var("object_b_803385F8", "const double"),
	0x80338600: main.sym_var("object_b_80338600", "const float"),
	0x80338604: main.sym_var("object_b_80338604", "const float"),
	0x80338608: main.sym_var("object_b_80338608", "const float"),
	0x8033860C: main.sym_var("object_b_8033860C", "const float"),
	0x80338610: main.sym_var("object_b_80338610", "const float"),
	0x80338614: main.sym_var("object_b_80338614", "const float"),
	0x80338618: main.sym_var("object_b_80338618", "const float"),
	0x8033861C: main.sym_var("object_b_8033861C", "const float"),
	0x80338620: main.sym_var("object_b_80338620", "const float"),
	0x80338624: main.sym_var("object_b_80338624", "const float"),
	0x80338628: main.sym_var("object_b_80338628", "const float"),
	0x8033862C: main.sym_var("object_b_8033862C", "const float"),
	0x80338630: main.sym_var("object_b_80338630", "const float"),
	0x80338634: main.sym_var("object_b_80338634", "const float"),
	0x80338638: main.sym_var("object_b_80338638", "const float"),
	0x8033863C: main.sym_var_fnc("object_b_8033863C", "const", "[]"),
	0x80338650: main.sym_var_fnc("object_b_80338650", "const", "[]"),
	0x80338668: main.sym_var_fnc("object_b_80338668", "const", "[]"),
	0x80338680: main.sym_var("object_b_80338680", "const double"),
	0x80338688: main.sym_var_fnc("object_b_80338688", "const", "[]"),
	0x8033869C: main.sym_var("object_b_8033869C", "const float"),
	0x803386A0: main.sym_var("object_b_803386A0", "const float"),
	0x803386A4: main.sym_var("object_b_803386A4", "const float"),
	0x803386A8: main.sym_var("object_b_803386A8", "const float"),
	0x803386AC: main.sym_var("object_b_803386AC", "const float"),
	0x803386B0: main.sym_var("object_b_803386B0", "const float"),
	0x803386B4: main.sym_var("object_b_803386B4", "const float"),
	0x803386B8: main.sym_var("object_b_803386B8", "const float"),
	0x803386BC: main.sym_var("object_b_803386BC", "const float"),
	0x803386C0: main.sym_var("object_b_803386C0", "const float"),
	0x803386C8: main.sym_var("object_b_803386C8", "const double"),
	0x803386D0: main.sym_var("object_b_803386D0", "const double"),
	0x803386D8: main.sym_var("object_b_803386D8", "const double"),
	0x803386E0: main.sym_var("object_b_803386E0", "const float"),
	0x803386E4: main.sym_var("object_b_803386E4", "const float"),
	0x803386E8: main.sym_var("object_b_803386E8", "const float"),
	0x803386EC: main.sym_var("object_b_803386EC", "const float"),
	0x803386F0: main.sym_var_fnc("object_b_803386F0", "const", "[]"),
	0x80338704: main.sym_var("object_b_80338704", "const float"),
	0x80338708: main.sym_var("object_b_80338708", "const float"),
	0x8033870C: main.sym_var("object_b_8033870C", "const float"),
	0x80338710: main.sym_var("object_b_80338710", "const float"),
	0x80338714: main.sym_var("object_b_80338714", "const float"),
	0x80338718: main.sym_var("object_b_80338718", "const float"),
	0x8033871C: main.sym_var_fnc("object_b_8033871C", "const", "[]"),
	0x80338730: main.sym_var("object_b_80338730", "const float"),
	0x80338734: main.sym_var("object_b_80338734", "const float"),
	0x80338738: main.sym_var("object_b_80338738", "const float"),
	0x8033873C: main.sym_var("object_b_8033873C", "const float"),
	0x80338740: main.sym_var("object_b_80338740", "const double"),
	0x80338748: main.sym_var_fnc("object_b_80338748", "const", "[]"),
	0x803387D8: main.sym_var("object_b_803387D8", "const float"),
	0x803387DC: main.sym_var("object_b_803387DC", "const float"),
	0x803387E0: main.sym_var("object_b_803387E0", "const float"),
	0x803387E8: main.sym_var("object_b_803387E8", "const double"),
	0x803387F0: main.sym_var("object_b_803387F0", "const double"),
	0x803387F8: main.sym_var("object_b_803387F8", "const float"),
	0x803387FC: main.sym_var("object_b_803387FC", "const float"),
	0x80338800: main.sym_var("object_b_80338800", "const float"),
	0x80338804: main.sym_var("object_b_80338804", "const float"),
	0x80338808: main.sym_var("object_b_80338808", "const float"),
	0x8033880C: main.sym_var("object_b_8033880C", "const float"),
	0x80338810: main.sym_var("object_b_80338810", "const float"),
	0x80338814: main.sym_var("object_b_80338814", "const float"),
	0x80338818: main.sym_var("object_b_80338818", "const float"),
	0x8033881C: main.sym_var("object_b_8033881C", "const float"),
	0x80338820: main.sym_var("object_b_80338820", "const float"),
	0x80338828: main.sym_var("object_b_80338828", "const double"),
	0x80338830: main.sym_var("object_b_80338830", "const double"),
	0x80338838: main.sym_var("object_b_80338838", "const double"),
	0x80338840: main.sym_var_fnc("object_b_80338840", "const", "[]"),
	0x80338860: main.sym_var("object_b_80338860", "const double"),
	0x80338868: main.sym_var("object_b_80338868", "const double"),
	0x80338870: main.sym_var("object_b_80338870", "const double"),
	0x80338878: main.sym_var("object_b_80338878", "const double"),
	0x80338880: main.sym_var("object_b_80338880", "const double"),
	0x80338888: main.sym_var("object_b_80338888", "const double"),
	0x80338890: main.sym_var("object_b_80338890", "const double"),
	0x80338898: main.sym_var("object_b_80338898", "const double"),
	0x803388A0: main.sym_var("object_b_803388A0", "const double"),
	0x803388A8: main.sym_var("object_b_803388A8", "const double"),
	0x803388B0: main.sym_var("object_b_803388B0", "const double"),
	0x803388B8: main.sym_var("object_b_803388B8", "const double"),
	0x803388C0: main.sym_var("object_b_803388C0", "const double"),
	0x803388C8: main.sym_var("object_b_803388C8", "const double"),
	0x803388D0: main.sym_var("object_b_803388D0", "const double"),
	0x803388D8: main.sym_var("object_b_803388D8", "const double"),
	0x803388E0: main.sym_var("object_b_803388E0", "const double"),
	0x803388E8: main.sym_var("object_b_803388E8", "const double"),
	0x803388F0: main.sym_var("object_b_803388F0", "const double"),
	0x803388F8: main.sym_var("object_b_803388F8", "const double"),
	0x80338900: main.sym_var("object_b_80338900", "const float"),
	0x80338904: main.sym_var("object_b_80338904", "const float"),
	0x80338908: main.sym_var("object_b_80338908", "const float"),
	0x80338910: main.sym_var("object_b_80338910", "const double"),
	0x80338918: main.sym_var("object_b_80338918", "const double"),
	0x80338920: main.sym_var("object_b_80338920", "const float"),
	0x80338924: main.sym_var("object_b_80338924", "const float"),
	0x80338928: main.sym_var("object_b_80338928", "const float"),
	0x8033892C: main.sym_var("object_b_8033892C", "const float"),
	0x80338930: main.sym_var("object_b_80338930", "const float"),
	0x80338934: main.sym_var("object_b_80338934", "const float"),
	0x80338938: main.sym_var("object_b_80338938", "const float"),
	0x8033893C: main.sym_var("object_b_8033893C", "const float"),
	0x80338940: main.sym_var_fnc("object_b_80338940", "const", "[]"),
	0x80338954: main.sym_var("object_b_80338954", "const float"),
	0x80338958: main.sym_var("object_b_80338958", "const float"),
	0x8033895C: main.sym_var("object_b_8033895C", "const float"),
	0x80338960: main.sym_var("object_b_80338960", "const double"),
	0x80338968: main.sym_var("object_b_80338968", "const float"),
	0x8033896C: main.sym_var("object_b_8033896C", "const float"),
	0x80338970: main.sym_var("object_b_80338970", "const float"),
	0x80338974: main.sym_var("object_b_80338974", "const float"),
	0x80338978: main.sym_var_fnc("object_b_80338978", "const", "[]"),

	# src/object_c.c
	0x803389B0: main.sym_var("object_c_803389B0", "const float"),
	0x803389B4: main.sym_var("object_c_803389B4", "const float"),
	0x803389B8: main.sym_var_fnc("object_c_803389B8", "const", "[]"),
	0x803389DC: main.sym_var("object_c_803389DC", "const float"),
	0x803389E0: main.sym_var("object_c_803389E0", "const float"),
	0x803389E4: main.sym_var("object_c_803389E4", "const float"),
	0x803389E8: main.sym_var("object_c_803389E8", "const float"),
	0x803389EC: main.sym_var("object_c_803389EC", "const float"),
	0x803389F0: main.sym_var("object_c_803389F0", "const float"),
	0x803389F4: main.sym_var("object_c_803389F4", "const float"),
	0x803389F8: main.sym_var("object_c_803389F8", "const float"),
	0x803389FC: main.sym_var("object_c_803389FC", "const float"),
	0x80338A00: main.sym_var("object_c_80338A00", "const float"),
	0x80338A04: main.sym_var("object_c_80338A04", "const float"),
	0x80338A08: main.sym_var("object_c_80338A08", "const float"),
	0x80338A0C: main.sym_var("object_c_80338A0C", "const float"),
	0x80338A10: main.sym_var("object_c_80338A10", "const float"),
	0x80338A14: main.sym_var("object_c_80338A14", "const float"),
	0x80338A18: main.sym_var("object_c_80338A18", "const float"),
	0x80338A1C: main.sym_var("object_c_80338A1C", "const float"),
	0x80338A20: main.sym_var("object_c_80338A20", "const float"),
	0x80338A24: main.sym_var("object_c_80338A24", "const float"),
	0x80338A28: main.sym_var("object_c_80338A28", "const float"),
	0x80338A2C: main.sym_var("object_c_80338A2C", "const float"),
	0x80338A30: main.sym_var_fnc("object_c_80338A30", "const", "[]"),
	0x80338A4C: main.sym_var("object_c_80338A4C", "const float"),
	0x80338A50: main.sym_var("object_c_80338A50", "const float"),
	0x80338A54: main.sym_var("object_c_80338A54", "const float"),
	0x80338A58: main.sym_var("object_c_80338A58", "const float"),
	0x80338A5C: main.sym_var("object_c_80338A5C", "const float"),
	0x80338A60: main.sym_var("object_c_80338A60", "const float"),
	0x80338A64: main.sym_var("object_c_80338A64", "const float"),
	0x80338A68: main.sym_var("object_c_80338A68", "const float"),
	0x80338A6C: main.sym_var("object_c_80338A6C", "const float"),
	0x80338A70: main.sym_var("object_c_80338A70", "const float"),
	0x80338A74: main.sym_var("object_c_80338A74", "const float"),
	0x80338A78: main.sym_var("object_c_80338A78", "const float"),
	0x80338A7C: main.sym_var("object_c_80338A7C", "const float"),
	0x80338A80: main.sym_var("object_c_80338A80", "const float"),
	0x80338A84: main.sym_var("object_c_80338A84", "const float"),
	0x80338A88: main.sym_var("object_c_80338A88", "const float"),
	0x80338A8C: main.sym_var("object_c_80338A8C", "const float"),
	0x80338A90: main.sym_var("object_c_80338A90", "const float"),
	0x80338A94: main.sym_var("object_c_80338A94", "const float"),
	0x80338A98: main.sym_var("object_c_80338A98", "const float"),
	0x80338A9C: main.sym_var("object_c_80338A9C", "const float"),
	0x80338AA0: main.sym_var("object_c_80338AA0", "const float"),
	0x80338AA4: main.sym_var_fnc("object_c_80338AA4", "const", "[]"),
	0x80338ABC: main.sym_var("object_c_80338ABC", "const float"),
	0x80338AC0: main.sym_var("object_c_80338AC0", "const float"),
	0x80338AC4: main.sym_var("object_c_80338AC4", "const float"),
	0x80338AC8: main.sym_var("object_c_80338AC8", "const float"),
	0x80338ACC: main.sym_var_fnc("object_c_80338ACC", "const", "[]"),
	0x80338AE0: main.sym_var("object_c_80338AE0", "const float"),
	0x80338AE4: main.sym_var("object_c_80338AE4", "const float"),
	0x80338AE8: main.sym_var("object_c_80338AE8", "const float"),
	0x80338AEC: main.sym_var("object_c_80338AEC", "const float"),
	0x80338AF0: main.sym_var("object_c_80338AF0", "const float"),
	0x80338AF4: main.sym_var("object_c_80338AF4", "const float"),
	0x80338AF8: main.sym_var("object_c_80338AF8", "const float"),
	0x80338AFC: main.sym_var("object_c_80338AFC", "const float"),
	0x80338B00: main.sym_var("object_c_80338B00", "const float"),
	0x80338B04: main.sym_var("object_c_80338B04", "const float"),
	0x80338B08: main.sym_var("object_c_80338B08", "const float"),
	0x80338B0C: main.sym_var("object_c_80338B0C", "const float"),
	0x80338B10: main.sym_var("object_c_80338B10", "const float"),
	0x80338B14: main.sym_var("object_c_80338B14", "const float"),
	0x80338B18: main.sym_var("object_c_80338B18", "const float"),
	0x80338B1C: main.sym_var("object_c_80338B1C", "const float"),
	0x80338B20: main.sym_var("object_c_80338B20", "const float"),
	0x80338B24: main.sym_var("object_c_80338B24", "const float"),
	0x80338B28: main.sym_var("object_c_80338B28", "const float"),
	0x80338B2C: main.sym_var("object_c_80338B2C", "const float"),
	0x80338B30: main.sym_var("object_c_80338B30", "const float"),
	0x80338B34: main.sym_var("object_c_80338B34", "const float"),
	0x80338B38: main.sym_var("object_c_80338B38", "const float"),
	0x80338B3C: main.sym_var_fnc("object_c_80338B3C", "const", "[]"),
	0x80338B5C: main.sym_var("object_c_80338B5C", "const float"),
	0x80338B60: main.sym_var("object_c_80338B60", "const float"),
	0x80338B64: main.sym_var("object_c_80338B64", "const float"),
	0x80338B68: main.sym_var("object_c_80338B68", "const float"),
	0x80338B6C: main.sym_var_fnc("object_c_80338B6C", "const", "[]"),
	0x80338B80: main.sym_var("object_c_80338B80", "const float"),
	0x80338B84: main.sym_var("object_c_80338B84", "const float"),
	0x80338B88: main.sym_var("object_c_80338B88", "const float"),
	0x80338B8C: main.sym_var("object_c_80338B8C", "const float"),
	0x80338B90: main.sym_var("object_c_80338B90", "const float"),
	0x80338B94: main.sym_var("object_c_80338B94", "const float"),
	0x80338B98: main.sym_var("object_c_80338B98", "const float"),
	0x80338B9C: main.sym_var("object_c_80338B9C", "const float"),
	0x80338BA0: main.sym_var("object_c_80338BA0", "const float"),
	0x80338BA4: main.sym_var("object_c_80338BA4", "const float"),
	0x80338BA8: main.sym_var("object_c_80338BA8", "const float"),
	0x80338BAC: main.sym_var("object_c_80338BAC", "const float"),
	0x80338BB0: main.sym_var("object_c_80338BB0", "const float"),
	0x80338BB4: main.sym_var("object_c_80338BB4", "const float"),
	0x80338BB8: main.sym_var("object_c_80338BB8", "const float"),
	0x80338BBC: main.sym_var("object_c_80338BBC", "const float"),
	0x80338BC0: main.sym_var("object_c_80338BC0", "const float"),
	0x80338BC4: main.sym_var("object_c_80338BC4", "const float"),
	0x80338BC8: main.sym_var_fnc("object_c_80338BC8", "const", "[]"),
	0x80338BE8: main.sym_var("object_c_80338BE8", "const float"),
	0x80338BEC: main.sym_var("object_c_80338BEC", "const float"),
	0x80338BF0: main.sym_var("object_c_80338BF0", "const float"),
	0x80338BF4: main.sym_var("object_c_80338BF4", "const float"),
	0x80338BF8: main.sym_var("object_c_80338BF8", "const float"),
	0x80338BFC: main.sym_var("object_c_80338BFC", "const float"),
	0x80338C00: main.sym_var("object_c_80338C00", "const float"),
	0x80338C04: main.sym_var("object_c_80338C04", "const float"),
	0x80338C08: main.sym_var_fnc("object_c_80338C08", "const", "[]"),
	0x80338C1C: main.sym_var("object_c_80338C1C", "const float"),
	0x80338C20: main.sym_var("object_c_80338C20", "const float"),
	0x80338C24: main.sym_var("object_c_80338C24", "const float"),
	0x80338C28: main.sym_var("object_c_80338C28", "const float"),
	0x80338C2C: main.sym_var("object_c_80338C2C", "const float"),
	0x80338C30: main.sym_var("object_c_80338C30", "const float"),
	0x80338C34: main.sym_var("object_c_80338C34", "const float"),
	0x80338C38: main.sym_var_fnc("object_c_80338C38", "const", "[]"),
	0x80338C4C: main.sym_var("object_c_80338C4C", "const float"),
	0x80338C50: main.sym_var("object_c_80338C50", "const float"),
	0x80338C54: main.sym_var("object_c_80338C54", "const float"),
	0x80338C58: main.sym_var("object_c_80338C58", "const float"),
	0x80338C5C: main.sym_var("object_c_80338C5C", "const float"),
	0x80338C60: main.sym_var("object_c_80338C60", "const float"),
	0x80338C64: main.sym_var("object_c_80338C64", "const float"),
	0x80338C68: main.sym_var("object_c_80338C68", "const float"),
	0x80338C6C: main.sym_var("object_c_80338C6C", "const float"),
	0x80338C70: main.sym_var("object_c_80338C70", "const float"),
	0x80338C74: main.sym_var("object_c_80338C74", "const float"),
	0x80338C78: main.sym_var("object_c_80338C78", "const float"),
	0x80338C7C: main.sym_var_fnc("object_c_80338C7C", "const", "[]"),
	0x80338C90: main.sym_var("object_c_80338C90", "const float"),
	0x80338C94: main.sym_var("object_c_80338C94", "const float"),
	0x80338C98: main.sym_var("object_c_80338C98", "const float"),
	0x80338C9C: main.sym_var("object_c_80338C9C", "const float"),
	0x80338CA0: main.sym_var_fnc("object_c_80338CA0", "const", "[]"),
	0x80338CDC: main.sym_var("object_c_80338CDC", "const float"),
	0x80338CE0: main.sym_var("object_c_80338CE0", "const float"),
	0x80338CE4: main.sym_var("object_c_80338CE4", "const float"),
	0x80338CE8: main.sym_var("object_c_80338CE8", "const float"),
	0x80338CEC: main.sym_var("object_c_80338CEC", "const float"),
	0x80338CF0: main.sym_var("object_c_80338CF0", "const float"),
	0x80338CF4: main.sym_var_fnc("object_c_80338CF4", "const", "[]"),
	0x80338D14: main.sym_var("object_c_80338D14", "const float"),
	0x80338D18: main.sym_var("object_c_80338D18", "const float"),
	0x80338D1C: main.sym_var("object_c_80338D1C", "const float"),
	0x80338D20: main.sym_var("object_c_80338D20", "const float"),
	0x80338D24: main.sym_var("object_c_80338D24", "const float"),
	0x80338D28: main.sym_var("object_c_80338D28", "const float"),
	0x80338D2C: main.sym_var("object_c_80338D2C", "const float"),
	0x80338D30: main.sym_var("object_c_80338D30", "const float"),
	0x80338D34: main.sym_var_fnc("object_c_80338D34", "const", "[]"),
	0x80338D4C: main.sym_var("object_c_80338D4C", "const float"),
	0x80338D50: main.sym_var("object_c_80338D50", "const float"),
	0x80338D54: main.sym_var("object_c_80338D54", "const float"),
	0x80338D58: main.sym_var("object_c_80338D58", "const float"),
	0x80338D5C: main.sym_var("object_c_80338D5C", "const float"),
	0x80338D60: main.sym_var("object_c_80338D60", "const float"),
	0x80338D64: main.sym_var("object_c_80338D64", "const float"),
	0x80338D68: main.sym_var("object_c_80338D68", "const float"),
	0x80338D6C: main.sym_var("object_c_80338D6C", "const float"),
	0x80338D70: main.sym_var("object_c_80338D70", "const float"),
	0x80338D74: main.sym_var("object_c_80338D74", "const float"),
	0x80338D78: main.sym_var("object_c_80338D78", "const float"),
	0x80338D7C: main.sym_var("object_c_80338D7C", "const float"),
	0x80338D80: main.sym_var("object_c_80338D80", "const float"),
	0x80338D84: main.sym_var("object_c_80338D84", "const float"),
	0x80338D88: main.sym_var("object_c_80338D88", "const float"),
	0x80338D8C: main.sym_var("object_c_80338D8C", "const float"),
	0x80338D90: main.sym_var("object_c_80338D90", "const float"),

	# src/audio/driver.c
	0x80338DA0: main.sym_var("Na_driver_80338DA0", "const float"),
	0x80338DA4: main.sym_var("Na_driver_80338DA4", "const float"),
	0x80338DA8: main.sym_var("Na_driver_80338DA8", "const float"),
	0x80338DAC: main.sym_var("Na_driver_80338DAC", "const float"),
	0x80338DB0: main.sym_var("Na_driver_80338DB0", "const float"),

	# src/audio/memory.c
	0x80338DC0: main.sym_var_fnc("Na_memory_80338DC0", "const", "[]"),
	0x80338E00: main.sym_var("Na_memory_80338E00", "const float"),
	0x80338E04: main.sym_var("Na_memory_80338E04", "const float"),

	# src/audio/voice.c
	0x80338E10: main.sym_var("Na_voice_80338E10", "const float"),
	0x80338E14: main.sym_var("Na_voice_80338E14", "const float"),
	0x80338E18: main.sym_var("Na_voice_80338E18", "const float"),
	0x80338E1C: main.sym_var("Na_voice_80338E1C", "const float"),
	0x80338E20: main.sym_var("Na_voice_80338E20", "const float"),
	0x80338E24: main.sym_var("Na_voice_80338E24", "const float"),

	# src/audio/effect.c
	0x80338E30: main.sym_var_fnc("Na_effect_80338E30", "const", "[]"),

	# src/audio/sequence.c
	0x80338E60: main.sym_var_fnc("Na_sequence_80338E60", "const", "[]"),
	0x80338E84: main.sym_var_fnc("Na_sequence_80338E84", "const", "[]"),
	0x80338EAC: main.sym_var_fnc("Na_sequence_80338EAC", "const", "[]"),
	0x80338EC0: main.sym_var_fnc("Na_sequence_80338EC0", "const", "[]"),
	0x80338FBC: main.sym_var_fnc("Na_sequence_80338FBC", "const", "[]"),
	0x80339280: main.sym_var_fnc("Na_sequence_80339280", "const", "[]"),
	0x80339360: main.sym_var_fnc("Na_sequence_80339360", "const", "[]"),

	# src/audio/game.c
	0x803394F0: main.sym_var("str_Na_game_803394F0", "const char", "[]"),
	0x803394FC: main.sym_var("str_Na_game_803394FC", "const char", "[]"),
	0x80339518: main.sym_var("str_Na_game_80339518", "const char", "[]"),
	0x80339524: main.sym_var("str_Na_game_80339524", "const char", "[]"),
	0x80339540: main.sym_var("str_Na_game_80339540", "const char", "[]"),
	0x8033954C: main.sym_var("str_Na_game_8033954C", "const char", "[]"),
	0x80339560: main.sym_var("str_Na_game_80339560", "const char", "[]"),
	0x80339568: main.sym_var("str_Na_game_80339568", "const char", "[]"),
	0x8033956C: main.sym_var("str_Na_game_8033956C", "const char", "[]"),
	0x80339578: main.sym_var("str_Na_game_80339578", "const char", "[]"),
	0x8033958C: main.sym_var("str_Na_game_8033958C", "const char", "[]"),
	0x80339594: main.sym_var("str_Na_game_80339594", "const char", "[]"),
	0x80339598: main.sym_var("str_Na_game_80339598", "const char", "[]"),
	0x803395C8: main.sym_var("str_Na_game_803395C8", "const char", "[]"),
	0x803395F8: main.sym_var("str_Na_game_803395F8", "const char", "[]"),
	0x80339600: main.sym_var("str_Na_game_80339600", "const char", "[]"),
	0x80339604: main.sym_var("str_Na_game_80339604", "const char", "[]"),
	0x80339608: main.sym_var("str_Na_game_80339608", "const char", "[]"),
	0x80339610: main.sym_var("str_Na_game_80339610", "const char", "[]"),
	0x80339614: main.sym_var("str_Na_game_80339614", "const char", "[]"),
	0x80339618: main.sym_var("str_Na_game_80339618", "const char", "[]"),
	0x80339624: main.sym_var("str_Na_game_80339624", "const char", "[]"),
	0x80339630: main.sym_var("str_Na_game_80339630", "const char", "[]"),
	0x8033963C: main.sym_var("str_Na_game_8033963C", "const char", "[]"),
	0x80339648: main.sym_var("str_Na_game_80339648", "const char", "[]"),
	0x80339660: main.sym_var("str_Na_game_80339660", "const char", "[]"),
	0x8033967C: main.sym_var("str_Na_game_8033967C", "const char", "[]"),
	0x8033968C: main.sym_var("str_Na_game_8033968C", "const char", "[]"),
	0x8033969C: main.sym_var("str_Na_game_8033969C", "const char", "[]"),
	0x803396AC: main.sym_var("str_Na_game_803396AC", "const char", "[]"),
	0x803396BC: main.sym_var("str_Na_game_803396BC", "const char", "[]"),
	0x803396CC: main.sym_var("str_Na_game_803396CC", "const char", "[]"),
	0x803396D8: main.sym_var("str_Na_game_803396D8", "const char", "[]"),
	0x803396EC: main.sym_var("str_Na_game_803396EC", "const char", "[]"),
	0x80339710: main.sym_var("Na_game_80339710", "const double"),
	0x80339718: main.sym_var("Na_game_80339718", "const double"),
	0x80339720: main.sym_var("Na_game_80339720", "const float"),
	0x80339724: main.sym_var("Na_game_80339724", "const float"),
	0x80339728: main.sym_var("Na_game_80339728", "const float"),
	0x8033972C: main.sym_var("Na_game_8033972C", "const float"),
	0x80339730: main.sym_var("Na_game_80339730", "const float"),
	0x80339734: main.sym_var("Na_game_80339734", "const float"),
	0x80339738: main.sym_var("Na_game_80339738", "const float"),
	0x8033973C: main.sym_var_fnc("Na_game_8033973C", "const", "[]"),
	0x80339764: main.sym_var_fnc("Na_game_80339764", "const", "[]"),
	0x8033978C: main.sym_var_fnc("Na_game_8033978C", "const", "[]"),

	# gu/perspective.c
	0x803397B0: main.sym_var("guPerspectiveF__803397B0", "const double"),

	# libc/llcvt.c
	0x803397C0: main.sym_var("__d_to_ull__803397C0", "const long long"),
	0x803397C8: main.sym_var("__f_to_ull__803397C8", "const long long"),

	# gu/cosf.c
	0x803397D0: main.sym_var("cosf__P", "const double", "[]"),
	0x803397F8: main.sym_var("cosf__rpi", "const double"),
	0x80339800: main.sym_var("cosf__pihi", "const double"),
	0x80339808: main.sym_var("cosf__pilo", "const double"),
	0x80339810: main.sym_var("cosf__zero", "const float"),

	# gu/sinf.c
	0x80339820: main.sym_var("sinf__P", "const double", "[]"),
	0x80339848: main.sym_var("sinf__rpi", "const double"),
	0x80339850: main.sym_var("sinf__pihi", "const double"),
	0x80339858: main.sym_var("sinf__pilo", "const double"),
	0x80339860: main.sym_var("sinf__zero", "const float"),

	# gu/rotate.c
	0x80339870: main.sym_var("guRotateF__80339870", "const float"),

	# rmon/xprintf.c
	0x80339880: main.sym_var("_Printf__80339880", "const char", "[]"),
	0x80339884: main.sym_var("fchar", "const char", "[]"),
	0x8033988C: main.sym_var("fbit", "const u32", "[]"),
	0x803398A4: main.sym_var_fnc("_Putfld__803398A4", "const", "[]"),

	# os/exceptasm.s
	0x80339980: main.sym("__osIntOffTable"),
	0x803399A0: main.sym("__osIntTable"),

	# gu/libm_vals.s
	0x803399D0: main.sym("__libm_qnan_f", flag={"GLOBL"}),

	# rmon/xldtob.c
	0x803399E0: main.sym_var("pows", "const double", "[]"),
	0x80339A28: main.sym_var("_Ldtob__80339A28", "const char", "[]"),
	0x80339A2C: main.sym_var("_Ldtob__80339A2C", "const char", "[]"),
	0x80339A30: main.sym_var("_Genld__80339A30", "const char", "[]"),
	0x80339A38: main.sym_var("_Ldtob__80339A38", "const double"),

	# os/setintmask.s
	0x80339A40: main.sym("__osRcpImTable", flag={"GLOBL"}),

	# ==========================================================================
	# bss
	# ==========================================================================

	# src/main.c
	0x8033A580: main.sym_var("rmon_thread", "OSThread", flag={"BALIGN"}),
	0x8033A730: main.sym_var("idle_thread", "OSThread", flag={"BALIGN"}),
	0x8033A8E0: main.sym_var("sched_thread", "OSThread", flag={"BALIGN"}),
	0x8033AA90: main.sym_var("gfx_thread", "OSThread", flag={"BALIGN"}),
	0x8033AC40: main.sym_var("aud_thread", "OSThread", flag={"BALIGN"}),
	0x8033ADF0: main.sym_var("pi_mq", "OSMesgQueue", flag={"BALIGN"}),
	0x8033AE08: main.sym_var("sched_mq", "OSMesgQueue", flag={"BALIGN"}),
	0x8033AE20: main.sym_var("sctask_mq", "OSMesgQueue", flag={"BALIGN"}),
	0x8033AE38: main.sym_var("dma_mbox", "OSMesg"),
	0x8033AE40: main.sym_var("pi_mbox", "OSMesg", "[32]", flag={"BALIGN"}),
	0x8033AEC0: main.sym_var("si_mbox", "OSMesg"),
	0x8033AEC8: main.sym_var("sched_mbox", "OSMesg", "[16]", flag={"BALIGN"}),
	0x8033AF08: main.sym_var("sctask_mbox", "OSMesg", "[16]", flag={"BALIGN"}),
	0x8033AF48: main.sym_var("dma_mb", "OSIoMesg", flag={"GLOBL","BALIGN"}),
	0x8033AF5C: main.sym_var("null_msg", "OSMesg", flag={"GLOBL"}),
	0x8033AF60: main.sym_var("dma_mq", "OSMesgQueue", flag={"GLOBL","BALIGN"}),
	0x8033AF78: main.sym_var("si_mq", "OSMesgQueue", flag={"GLOBL","BALIGN"}),

	# src/graphics.c
	0x8033AF90: main.sym_var("controller_data", "CONTROLLER", "[CONTROLLER_MAX+1]", flag={"GLOBL","BALIGN"}),
	0x8033AFE8: main.sym_var("cont_status", "OSContStatus", "[MAXCONTROLLERS]", flag={"BALIGN"}),
	0x8033AFF8: main.sym_var("cont_pad", "OSContPad", "[MAXCONTROLLERS]", flag={"BALIGN"}),
	0x8033B010: main.sym_var("gfx_vi_mq", "OSMesgQueue", flag={"BALIGN"}),
	0x8033B028: main.sym_var("gfx_dp_mq", "OSMesgQueue", flag={"BALIGN"}),
	0x8033B040: main.sym_var("gfx_vi_mbox", "OSMesg"),
	0x8033B044: main.sym_var("gfx_dp_mbox", "OSMesg"),
	0x8033B048: main.sym_var("gfx_client", "SCCLIENT", flag={"BALIGN"}),
	0x8033B050: main.sym_var("gfx_cimg", "unsigned long", "[3]", flag={"BALIGN"}),
	0x8033B05C: main.sym_var("gfx_zimg", "unsigned long"),
	0x8033B060: main.sym_var("mario_anime_buf", "void *"),
	0x8033B064: main.sym_var("demo_buf", "void *"),
	0x8033B068: main.sym_var("gfx_task", "SCTASK *", flag={"GLOBL"}),
	0x8033B06C: main.sym_var("glistp", "Gfx *", flag={"GLOBL"}),
	0x8033B070: main.sym_var("gfx_mem", "char *", flag={"GLOBL"}),
	0x8033B074: main.sym_var("framep", "FRAME *", flag={"GLOBL"}),
	0x8033B078: main.sym_var("cont_bitpattern", "u8", flag={"GLOBL"}),
	0x8033B079: main.sym_var("eeprom_status", "s8", flag={"GLOBL"}),
	0x8033B080: main.sym_var("mario_anime_bank", "BANK", flag={"GLOBL","BALIGN"}),
	0x8033B090: main.sym_var("demo_bank", "BANK", flag={"GLOBL","BALIGN"}),

	# src/audio.c
	0x8033B0A0: main.sym_var("aud_levelse_8033B0A0", "u32", "[]", flag={"BALIGN"}), # unused
	0x8033B130: main.sym_var("aud_0", "FVEC", flag={"BALIGN"}),
	0x8033B140: main.sym_var("aud_vi_mq", "OSMesgQueue", flag={"BALIGN"}),
	0x8033B158: main.sym_var("aud_vi_mbox", "OSMesg"),
	0x8033B160: main.sym_var("aud_client", "SCCLIENT", flag={"BALIGN"}),

	# src/game.c
	0x8033B170: main.sym_var("player_data", "PLAYER", "[1]", flag={"GLOBL","BALIGN"}),
	0x8033B238: main.sym_var("game_state", "s16"),
	0x8033B23A: main.sym_var("game_timer", "s16"),
	0x8033B23C: main.sym_var("freeze_timer", "short"),
	0x8033B240: main.sym_var("freeze_callback", "FREEZECALL *"),
	0x8033B248: main.sym_var("mario_entry", "PL_ENTRY", flag={"BALIGN"}),
	0x8033B250: main.sym_var("game_result", "s16"),
	0x8033B252: main.sym_var("fade_mode", "s16"),
	0x8033B254: main.sym_var("fade_timer", "s16"),
	0x8033B256: main.sym_var("fade_port", "s16"),
	0x8033B258: main.sym_var("fade_code", "u32"),
	0x8033B25C: main.sym_var("game_8033B25C", "s16"), # unused
	0x8033B25E: main.sym_var("time_flag", "char"),
	0x8033B260: main.sym_var("hud", "HUD", flag={"GLOBL","BALIGN"}),
	0x8033B26E: main.sym_var("first_msg", "char", flag={"GLOBL"}),

	# src/collision.c
	0x8033B270: main.sym_var("hit_enemy", "u8"),
	0x8033B272: main.sym_var("invincible", "short"),

	# src/player.c
	0x8033B280: main.sym_var("player_8033B280", "int"),

	# src/physics.c
	0x8033B290: main.sym_var("physics_8033B290", "int"), # unused

	# src/pldemo.c
	0x8033B2A0: main.sym_var("pldemo_8033B2A0", "OBJECT *", flag={"GLOBL"}),
	0x8033B2A4: main.sym_var("pldemo_8033B2A4", "OBJECT *", flag={"GLOBL"}),
	0x8033B2A8: main.sym_var("pldemo_8033B2A8", "OBJECT *", flag={"GLOBL"}),
	0x8033B2AC: main.sym_var("pldemo_8033B2AC", "OBJECT *", flag={"GLOBL"}),
	0x8033B2B0: main.sym_var("pldemo_8033B2B0", "OBJECT *", flag={"GLOBL"}),
	0x8033B2B4: main.sym_var("pldemo_8033B2B4", "OBJECT *", flag={"GLOBL"}), # unused
	0x8033B2B8: main.sym_var("pldemo_8033B2B8", "s16", flag={"GLOBL"}),
	0x8033B2BC: main.sym_var("pldemo_8033B2BC", "s16", "[2]", flag={"GLOBL"}),

	# src/plmove.c
	0x8033B2C0: main.sym_var("plmove_8033B2C0", "FMTX", "[2]", flag={"GLOBL"}),

	# src/plswim.c
	0x8033B340: main.sym_var("plswim_8033B340", "s16", flag={"GLOBL"}),
	0x8033B342: main.sym_var("plswim_8033B342", "s16", flag={"GLOBL"}),
	0x8033B344: main.sym_var("plswim_8033B344", "f32", flag={"GLOBL"}),

	# src/callback.c
	0x8033B350: main.sym_var("mario_mirror", "SOBJECT", flag={"BALIGN"}),
	0x8033B3B0: main.sym_var("pl_shape_data", "PL_SHAPE", "[2]", flag={"GLOBL","BALIGN"}),

	# src/memory.c
	0x8033B400: main.sym_var("segment_table", "unsigned long", "[32]", flag={"BALIGN"}),
	0x8033B480: main.sym_var("mem_size", "size_t"),
	0x8033B484: main.sym_var("mem_start", "char *"),
	0x8033B488: main.sym_var("mem_end", "char *"),
	0x8033B48C: main.sym_var("mem_blockl", "MEM_BLOCK *"),
	0x8033B490: main.sym_var("mem_blockr", "MEM_BLOCK *"),
	0x8033B494: main.sym_var("mem_heap", "HEAP *", flag={"GLOBL"}),

	# src/backup.c
	0x8033B4A0: main.sym_var("mid_level", "u8"),
	0x8033B4A1: main.sym_var("mid_course", "u8"),
	0x8033B4A2: main.sym_var("mid_stage", "u8"),
	0x8033B4A3: main.sym_var("mid_scene", "u8"),
	0x8033B4A4: main.sym_var("mid_port", "u8"),
	0x8033B4A5: main.sym_var("bu_info_dirty", "char"),
	0x8033B4A6: main.sym_var("bu_file_dirty", "char"),

	# src/scene.c
	0x8033B4B0: main.sym_var("player_actor", "ACTOR", "[1]", flag={"GLOBL","BALIGN"}),
	0x8033B4D0: main.sym_var("shape_data", "SHAPE *", "[SHAPE_MAX]", flag={"GLOBL","BALIGN"}),
	0x8033B8D0: main.sym_var("scene_data", "SCENE", "[SCENE_MAX]", flag={"GLOBL","BALIGN"}),
	0x8033BAB0: main.sym_var("wipe", "WIPE", flag={"GLOBL","BALIGN"}),
	0x8033BAC6: main.sym_var("course_index", "s16", flag={"GLOBL"}),
	0x8033BAC8: main.sym_var("level_index", "s16", flag={"GLOBL"}),
	0x8033BACA: main.sym_var("scene_index", "s16", flag={"GLOBL"}),
	0x8033BACC: main.sym_var("prev_course", "s16", flag={"GLOBL"}),
	0x8033BACE: main.sym_var("msg_status", "s16", flag={"GLOBL"}),
	0x8033BAD0: main.sym_var("msg_result", "s16", flag={"GLOBL"}),

	# src/draw.c
	0x8033BAE0: main.sym_var("draw_m", "s16"),
	0x8033BAE8: main.sym_var("draw_mtxf", "FMTX", "[32]", flag={"BALIGN"}),
	0x8033C2E8: main.sym_var("draw_mtx", "Mtx *", "[32]", flag={"BALIGN"}),
	0x8033C368: main.sym_var("joint_save_type", "u8"),
	0x8033C369: main.sym_var("joint_save_shadow", "u8"),
	0x8033C36A: main.sym_var("joint_save_frame", "s16"),
	0x8033C36C: main.sym_var("joint_save_scale", "float"),
	0x8033C370: main.sym_var("joint_save_tbl", "u16 *"),
	0x8033C374: main.sym_var("joint_save_val", "short *"),
	0x8033C378: main.sym_var("joint_type", "u8"),
	0x8033C379: main.sym_var("joint_shadow", "u8"),
	0x8033C37A: main.sym_var("joint_frame", "s16"),
	0x8033C37C: main.sym_var("joint_scale", "float"),
	0x8033C380: main.sym_var("joint_tbl", "u16 *"),
	0x8033C384: main.sym_var("joint_val", "short *"),
	0x8033C388: main.sym_var("draw_arena", "ARENA *"),

	# src/time.c
	0x8033C390: main.sym_var("time_data", "TIME", "[2]", flag={"BALIGN"}),

	# src/camera.c
	0x8033C520: main.sym_var("pl_camera_data", "PL_CAMERA", "[2]", flag={"GLOBL","BALIGN"}),
	0x8033C568: main.sym_var("_camera_bss_48", "char", "[0x178-0x48]", flag={"BALIGN"}),
	0x8033C698: main.sym_var("camdata", "CAMDATA", flag={"GLOBL","BALIGN"}),
	0x8033C758: main.sym_var("_camera_bss_238", "char", "[0x328-0x238]", flag={"BALIGN"}),
	0x8033C848: main.sym_var("camera_8033C848", "s16", flag={"GLOBL"}),
	0x8033C84A: main.sym_var("camera_8033C84A", "s16", flag={"GLOBL"}),
	0x8033C850: main.sym_var("_camera_bss_330", "char", "[0x6A8-0x330]", flag={"BALIGN"}),
	0x8033CBC8: main.sym_var("camera_8033CBC8", "int", flag={"GLOBL"}),
	0x8033CBCC: main.sym_var("camera_8033CBCC", "int", flag={"GLOBL"}),
	0x8033CBD0: main.sym_var("camerap", "CAMERA *", flag={"GLOBL"}),

	# src/object.c
	0x8033CBE0: main.sym_var("obj_rootdata", "OBJLIST", "[16]", flag={"BALIGN"}),
	0x8033D260: main.sym_var("debug_flag", "int", flag={"GLOBL"}),
	0x8033D264: main.sym_var("nullbg_count", "int", flag={"GLOBL"}),
	0x8033D268: main.sym_var("nullroof_count", "int", flag={"GLOBL"}), # unused
	0x8033D26C: main.sym_var("wall_count", "int", flag={"GLOBL"}),
	0x8033D270: main.sym_var("obj_count", "int", flag={"GLOBL"}),
	0x8033D274: main.sym_var("bgdebug", "BGDEBUG", flag={"GLOBL"}),
	0x8033D280: main.sym_var("db_work", "short", "[16][8]", flag={"GLOBL","BALIGN"}),
	0x8033D380: main.sym_var("db_save", "short", "[16][8]", flag={"GLOBL","BALIGN"}),
	0x8033D480: main.sym_var("object_flag", "int", flag={"GLOBL"}),
	0x8033D488: main.sym_var("object_data", "OBJECT", "[OBJECT_MAX]", flag={"GLOBL","BALIGN"}),
	0x80360E88: main.sym_var("object_dummy", "OBJECT", flag={"GLOBL","BALIGN"}),
	0x803610E8: main.sym_var("obj_rootlist", "OBJLIST *", flag={"GLOBL"}),
	0x803610F0: main.sym_var("obj_freelist", "OBJLIST", flag={"GLOBL","BALIGN"}),
	0x80361158: main.sym_var("mario_obj", "OBJECT *", flag={"GLOBL"}),
	0x8036115C: main.sym_var("luigi_obj", "OBJECT *", flag={"GLOBL"}),
	0x80361160: main.sym_var("object", "OBJECT *", flag={"GLOBL"}),
	0x80361164: main.sym_var("object_pc", "OBJLANG *", flag={"GLOBL"}),
	0x80361168: main.sym_var("obj_prevcount", "s16", flag={"GLOBL"}),
	0x8036116C: main.sym_var("bglist_count", "int", flag={"GLOBL"}),
	0x80361170: main.sym_var("bgface_count", "int", flag={"GLOBL"}),
	0x80361174: main.sym_var("bglist_static", "int", flag={"GLOBL"}),
	0x80361178: main.sym_var("bgface_static", "int", flag={"GLOBL"}),
	0x8036117C: main.sym_var("object_heap", "HEAP *", flag={"GLOBL"}),
	0x80361180: main.sym_var("object_80361180", "short", flag={"GLOBL"}),
	0x80361182: main.sym_var("object_80361182", "short", flag={"GLOBL"}),
	0x80361184: main.sym_var("waterp", "MAP *", flag={"GLOBL"}),
	0x80361188: main.sym_var("water_table", "int", "[20]", flag={"GLOBL","BALIGN"}),
	0x803611D8: main.sym_var("area_table", "AREA", "[60][2]", flag={"GLOBL","BALIGN"}),
	0x80361250: main.sym_var("object_80361250", "s16", flag={"GLOBL"}),
	0x80361252: main.sym_var("object_80361252", "s16", flag={"GLOBL"}),
	0x80361254: main.sym_var("object_80361254", "s16", flag={"GLOBL"}),
	0x80361256: main.sym_var("object_80361256", "s16", flag={"GLOBL"}),
	0x80361258: main.sym_var("object_80361258", "s16", flag={"GLOBL"}),
	0x8036125A: main.sym_var("object_8036125A", "s16", flag={"GLOBL"}),
	0x8036125C: main.sym_var("object_8036125C", "s16", flag={"GLOBL"}),
	0x8036125E: main.sym_var("object_8036125E", "s16", flag={"GLOBL"}),
	0x80361260: main.sym_var("object_80361260", "s16", flag={"GLOBL"}),
	0x80361262: main.sym_var("object_80361262", "s16", flag={"GLOBL"}),
	0x80361264: main.sym_var("object_80361264", "s16", flag={"GLOBL"}),

	# src/objectlib.c
	0x80361270: main.sym_var("objectlib_80361270", "s32", flag={"GLOBL"}),

	# src/object_a.c
	0x80361280: main.sym_var("object_a_80361280", "s16", flag={"GLOBL"}),

	# src/debug.c
	0x80361290: main.sym_var("db_out", "DBPRINT", flag={"BALIGN"}),
	0x803612A0: main.sym_var("db_err", "DBPRINT", flag={"BALIGN"}),

	# src/shadow.c
	0x803612B0: main.sym_var("shadow_offset", "char"),
	0x803612B2: main.sym_var("shadow_bgcode", "short"),
	0x803612B4: main.sym_var("shadow_onwater", "char", flag={"GLOBL"}),
	0x803612B5: main.sym_var("shadow_ondecal", "char", flag={"GLOBL"}),

	# src/background.c
	0x803612C0: main.sym_var("backdata", "BACKDATA", "[2]"),

	# src/water.c
	0x803612E0: main.sym_var("water_txt", "short"),

	# src/objshape.c
	0x803612F0: main.sym_var("objshape_803612F0", "s8", flag={"GLOBL"}),

	# src/wave.c
	0x80361300: main.sym_var("wave_bgcode", "short"),
	0x80361304: main.sym_var("wave_posx", "float"),
	0x80361308: main.sym_var("wave_posy", "float"),
	0x8036130C: main.sym_var("wave_posz", "float"),
	0x80361310: main.sym_var("wavevtx", "WAVEVTX *"),
	0x80361314: main.sym_var("wavenorm", "WAVENORM *"),
	0x80361318: main.sym_var("wavep", "WAVE *", flag={"GLOBL"}),
	0x8036131C: main.sym_var("wave_8036131C", "s8", flag={"GLOBL"}),

	# src/dprint.c
	0x80361320: main.sym_var("dprint_table", "DPRINT *", "[50]", flag={"BALIGN"}),

	# src/message.c
	0x803613F0: main.sym_var("msg_theta", "s16"),
	0x803613F2: main.sym_var("msg_cursor_line", "s8"),
	0x803613F4: main.sym_var("msg_value", "int"),
	0x803613F8: main.sym_var("msg_alpha", "u16"),
	0x803613FA: main.sym_var("caption_x", "short"),
	0x803613FC: main.sym_var("caption_y", "short"),
	0x803613FE: main.sym_var("redcoin_count", "s8", flag={"GLOBL"}),

	# src/weather.c
	0x80361400: main.sym_var("weatherp", "WEATHER *", flag={"GLOBL"}),
	0x80361408: main.sym_var("snow_pos", "int", "[3]", flag={"BALIGN"}),
	0x80361414: main.sym_var("snow_len", "s16"),
	0x80361416: main.sym_var("snow_max", "s16"),

	# src/lava.c
	0x80361420: main.sym_var("lava_info", "short", "[10]", flag={"GLOBL","BALIGN"}),
	0x80361434: main.sym_var("lava_glistp", "Gfx *"),
	0x80361438: main.sym_var("lava_max", "int"),
	0x8036143C: main.sym_var("lava_len", "int"),

	# src/hud.c
	0x80361440: main.sym_var("meter_power", "s16"),

	# src/object_b.c
	0x80361450: main.sym_var("object_b_80361450", "BGFACE *", flag={"GLOBL"}),

	# src/object_c.c
	0x80361460: main.sym_var("object_c_80361460", "s32", flag={"GLOBL"}),
	0x80361464: main.sym_var("object_c_80361464", "s32", flag={"GLOBL"}),
	0x80361468: main.sym_var("object_c_80361468", "f32", flag={"GLOBL"}),
	0x8036146C: main.sym_var("object_c_8036146C", "f32", flag={"GLOBL"}),
	0x80361470: main.sym_var("object_c_80361470", "f32", flag={"GLOBL"}),
	0x80361474: main.sym_var("object_c_80361474", "OBJECT *", flag={"GLOBL"}),
	0x80361478: main.sym_var("object_c_80361478", "s32", flag={"GLOBL"}),
	0x8036147C: main.sym_var("object_c_8036147C", "f32", flag={"GLOBL"}),
	0x80361480: main.sym_var("object_c_80361480", "f32", flag={"GLOBL"}),
	0x80361484: main.sym_var("object_c_80361484", "f32", flag={"GLOBL"}),
	0x80361488: main.sym_var("object_c_80361488", "OBJECT *", flag={"GLOBL"}),

	# src/audio/game.c
	0x80361490: main.sym_var("_Na_game_bss", "char", "[0x3710]", flag={"BALIGN"}),

	# os/seteventmesg.c
	0x80364BA0: main.sym_var("__osEventStateTab", "__OSEventState", "[OS_NUM_EVENTS]", flag={"BALIGN"}),

	# io/sptask.c
	0x80364C20: main.sym_var("tmp_task", "OSTask", flag={"BALIGN"}),

	# io/vimgr.c
	0x80364C60: main.sym_var("viThread", "OSThread", flag={"BALIGN"}),
	0x80364E10: main.sym_var("viThreadStack", "u64", "[0x1000/8]", flag={"BALIGN"}),
	0x80365E10: main.sym_var("viEventQueue", "OSMesgQueue", flag={"BALIGN"}),
	0x80365E28: main.sym_var("viEventBuf", "OSMesg", "[5]", flag={"BALIGN"}),
	0x80365E40: main.sym_var("viRetraceMsg", "OSIoMesg", flag={"BALIGN"}),
	0x80365E58: main.sym_var("viCounterMsg", "OSIoMesg", flag={"BALIGN"}),
	0x80365E6C: main.sym_var("viMgrMain__retrace", "u16"), # static

	# io/pimgr.c
	0x80365E70: main.sym_var("piThread", "OSThread", flag={"BALIGN"}),
	0x80366020: main.sym_var("piThreadStack", "u64", "[0x1000/8]", flag={"BALIGN"}),
	0x80367020: main.sym_var("piEventQueue", "OSMesgQueue", flag={"BALIGN"}),
	0x80367038: main.sym_var("piEventBuf", "OSMesg", "[1]", flag={"BALIGN"}),

	# os/initialize.c
	0x80367040: main.sym_var("__osFinalrom", "s32"),

	# io/controller.c
	0x80367050: main.sym_var("__osContPifRam", "u32", "[0x40/4]", flag={"BALIGN"}),
	0x80367090: main.sym_var("__osContLastCmd", "u8"),
	0x80367091: main.sym_var("__osMaxControllers", "u8"),
	0x80367098: main.sym_var("__osEepromTimer", "OSTimer", flag={"BALIGN"}),
	0x803670B8: main.sym_var("__osEepromTimerQ", "OSMesgQueue", flag={"BALIGN"}),
	0x803670D0: main.sym_var("__osEepromTimerMsg", "OSMesg", "[1]", flag={"BALIGN"}),

	# gu/rotate.c
	0x803670E0: main.sym_var("guRotateF__dtor", "float"), # static

	# os/timerintr.c
	0x803670F0: main.sym_var("__osBaseTimer", "OSTimer", flag={"BALIGN"}),
	0x80367110: main.sym_var("__osCurrentTime", "OSTime"),
	0x80367118: main.sym_var("__osBaseCounter", "u32"),
	0x8036711C: main.sym_var("__osViIntrCount", "u32"),
	0x80367120: main.sym_var("__osTimerCounter", "u32"),

	# io/piacs.c
	0x80367130: main.sym_var("piAccessBuf", "OSMesg", "[1]", flag={"BALIGN"}),
	0x80367138: main.sym_var("__osPiAccessQueue", "OSMesgQueue", flag={"BALIGN"}),

	# io/siacs.c
	0x80367150: main.sym_var("siAccessBuf", "OSMesg", "[1]", flag={"BALIGN"}),
	0x80367158: main.sym_var("__osSiAccessQueue", "OSMesgQueue", flag={"BALIGN"}),

	# io/conteepread.c
	0x80367170: main.sym_var("__osEepPifRam", "u32", "[0x40/4]", flag={"BALIGN"}),

	# os/kdebugserver.c
	0x803671B0: main.sym_var("kdebugserver__buffer", "u8", "[0x100]", flag={"BALIGN"}), # static
	0x803672B0: main.sym_var("__osThreadSave", "OSThread", flag={"BALIGN"}),

	# ==========================================================================
	# buffer
	# ==========================================================================

	# src/zimg.c
	0x80000400: main.sym_var("z_image", "u16", "[SCREEN_HT][SCREEN_WD]", flag={"GLOBL","BALIGN"}),

	# src/timg.c
	0x801C1000: main.sym_var("t_image", "u16", "[13][2048]", flag={"GLOBL","BALIGN"}),

	# src/audio/heap.c
	0x801CE000: main.sym_var("Na_Heap", "u64", "[0x31200/8]", flag={"GLOBL","BALIGN"}),
	0x801FF200: main.sym_var("Na_SpStack", "u64", "[4096/8]", flag={"GLOBL","BALIGN"}),

	# src/buffer.c
	0x80200200: main.sym_var("entry_stack", "long long", "[BOOT_STACK_LEN]", flag={"GLOBL","BALIGN"}),
	0x80200600: main.sym_var("idle_stack", "long long", "[IDLE_STACK_LEN]", flag={"GLOBL","BALIGN"}),
	0x80200E00: main.sym_var("sched_stack", "long long", "[MAIN_STACK_LEN]", flag={"GLOBL","BALIGN"}),
	0x80202E00: main.sym_var("aud_stack", "long long", "[MAIN_STACK_LEN]", flag={"GLOBL","BALIGN"}),
	0x80204E00: main.sym_var("gfx_stack", "long long", "[MAIN_STACK_LEN]", flag={"GLOBL","BALIGN"}),
	0x80206E00: main.sym_var("gfx_sp_yield", "u64", "[OS_YIELD_DATA_SIZE/8]", flag={"GLOBL","BALIGN"}),
	0x80207700: main.sym_var("backup", "BACKUP", flag={"GLOBL","BALIGN"}),
	0x80207900: main.sym_var("gfx_sp_stack", "u64", "[SP_DRAM_STACK_SIZE64]", flag={"GLOBL","BALIGN"}),
	0x80207D00: main.sym_var("frame_data", "FRAME", "[2]", flag={"GLOBL","BALIGN"}),

	# src/audio/work.c
	0x80220DA0: main.sym_var("Na_WorkStart", "char", "[16]", flag={"BALIGN"}),
	0x80220DB0: main.sym_var("_Na_work_bss_10", "char", "[0x5F08]", flag={"BALIGN"}),
	0x80226CB8: main.sym_var("Na_Random", "u32", flag={"GLOBL"}),
	0x80226CC0: main.sym_var("Na_WorkEnd", "char", "[16]", flag={"BALIGN"}),

	# src/fifo.c
	0x80227000: main.sym_var("gfx_fifo", "u64", "[FIFO_LEN]", flag={"GLOBL","BALIGN"}),

	# src/cimg.c
	0x8038F800: main.sym_var("c_image_a", "u16", "[SCREEN_HT][SCREEN_WD]", flag={"GLOBL","BALIGN"}),
	0x803B5000: main.sym_var("c_image_b", "u16", "[SCREEN_HT][SCREEN_WD]", flag={"GLOBL","BALIGN"}),
	0x803DA800: main.sym_var("c_image_c", "u16", "[SCREEN_HT][SCREEN_WD]", flag={"GLOBL","BALIGN"}),

	# water fix
	0x07001000: main.sym("(void *)0x07001000"),
}

seg_E0_code_data = {
	0x80330F00: "E0.BackgroundA",
	0x80330F04: "E0.BackgroundD",
	0x80330F08: "E0.BackgroundE",
	0x80330F0C: "E0.BackgroundF",
	0x80330F10: "E0.BackgroundB",
	0x80330F14: "E0.BackgroundG",
	0x80330F18: "E0.BackgroundH",
	0x80330F1C: "E0.BackgroundI",
	0x80330F20: "E0.BackgroundC",
	0x80330F24: "E0.BackgroundJ",
}

sym_G0_crt0_text = {
	# ==========================================================================
	# text
	# ==========================================================================

	# src/crt0.s
	0x80246000: main.sym("_start", flag={"GLOBL"}),

	0x80200600: main.sym("entry_stack+1024"),
	0x8030E6F0: main.sym("_codeSegmentBssStart"),
}

sym_G0_code_text = {
	# text

	# src/main.c
	0x80246050: main.sym("DebugCheck", flag={"GLOBL"}),
	0x80246C20: main.sym("entry", flag={"GLOBL"}),

	# src/graphics.c
	0x80246C90: main.sym("WriteGatewayRegister"),
	0x80246D30: main.sym("cont_read"),

	# libultra
	0x802F6AA0: main.sym("osRecvMesg"),
	0x802F7D30: main.sym("__osPiGetAccess"),
	0x802F7D74: main.sym("__osPiRelAccess"),
	0x802F7DA0: main.sym("osContStartReadData"),
	0x802F7E64: main.sym("osContGetReadData"),

	# data

	# src/main.c
	0x8030186C: main.sym("sys_halt"),

	# src/graphics.c
	0x803018C4: main.sym("cont1"),
	0x803018CC: main.sym("contp"),

	# bss

	# src/main.c
	0x8030EF74: main.sym("null_msg"),
	0x8030EF90: main.sym("si_mq"),

	# src/graphics.c
	0x8030F178: main.sym("cont_pad"),
}

sym_DD_crt0_text = {
	# ==========================================================================
	# text
	# ==========================================================================

	# src/crt0.s
	0x80400000: main.sym("_start", flag={"GLOBL"}),

	0x801E88A0: main.sym("entry_stack+1024"),
	0x804B5690: main.sym("_codeSegmentBssStart"),
}

sym_DD_code_text = {
	# text

	# src/main.c
	0x80400050: main.sym("DebugCheck", flag={"GLOBL"}),
	0x80400BE0: main.sym("entry", flag={"GLOBL"}),

	# src/disk.c
	0x8040B980: main.sym("DiskInit", flag={"GLOBL"}),
	0x8040B9A4: main.sym("DiskRead"),
	0x8040BA8C: main.sym("DiskWrite", flag={"GLOBL"}),
	0x8040BAEC: main.sym("disk_8040BAEC", flag={"GLOBL"}),
	0x8040BBE0: main.sym("MemRead", flag={"GLOBL"}),
}

sym_DD_code_data = {
	0x804A7CD0: main.sym("disk_audbuf"),
	0x804A7CD4: main.sym("disk_gfxbuf"),
	0x804A7CD8: main.sym("disk_lastlba"),
	0x804A7CDC: main.sym("disk_lastxfer"),
}

sym_P0_crt0_text = {
	# ==========================================================================
	# text
	# ==========================================================================

	# src/crt0.s
	0x80241800: main.sym("_start", flag={"GLOBL"}),

	0x8019BA00: main.sym("entry_stack+1024"),
	0x80307E50: main.sym("_codeSegmentBssStart"),
}

sym_P0_code_text = {
	# text

	0x80241850: main.sym("fault_80241850"),
	0x802422F0: main.sym("DebugCheck", flag={"GLOBL"}),
	0x80242E80: main.sym("entry", flag={"GLOBL"}),
}

sym_P0_code_data = {
	# data

	# src/game.c
	0x802F9880: main.sym_var("staff_01", "static const char *", "[]"),
	0x802F9888: main.sym_var("staff_02", "static const char *", "[]"),
	0x802F9894: main.sym_var("staff_03", "static const char *", "[]"),
	0x802F98A0: main.sym_var("staff_04", "static const char *", "[]"),
	0x802F98B0: main.sym_var("staff_05", "static const char *", "[]"),
	0x802F98C0: main.sym_var("staff_06", "static const char *", "[]"),
	0x802F98CC: main.sym_var("staff_07", "static const char *", "[]"),
	0x802F98D8: main.sym_var("staff_08", "static const char *", "[]"),
	0x802F98E8: main.sym_var("staff_09", "static const char *", "[]"),
	0x802F9900: main.sym_var("staff_10", "static const char *", "[]"),
	0x802F9914: main.sym_var("staff_11", "static const char *", "[]"),
	0x802F9924: main.sym_var("staff_12", "static const char *", "[]"),
	0x802F992C: main.sym_var("staff_13", "static const char *", "[]"),
	0x802F9938: main.sym_var("staff_14", "static const char *", "[]"),
	0x802F994C: main.sym_var("staff_15", "static const char *", "[]"),
	0x802F995C: main.sym_var("staff_16", "static const char *", "[]"),
	0x802F996C: main.sym_var("staff_17", "static const char *", "[]"),
	0x802F997C: main.sym_var("staff_18", "static const char *", "[]"),
	0x802F998C: main.sym_var("staff_19", "static const char *", "[]"),
	0x802F9994: main.sym_var("staff_20", "static const char *", "[]"),
	0x802F999C: main.sym("staff_table"),
}
