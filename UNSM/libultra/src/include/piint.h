#if REVISION >= 199707
extern OSPiHandle *__osCurrentHandle[];
extern OSPiHandle __CartRomHandle;
extern OSPiHandle __LeoDiskHandle;
extern OSPiHandle __DriveRomHandle;
extern OSPiHandle __Dom1SpeedParam, __Dom2SpeedParam;
#endif
extern void __osPiGetAccess(void);
extern void __osPiRelAccess(void);
