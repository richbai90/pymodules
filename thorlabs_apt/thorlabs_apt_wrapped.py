import ctypes
import thorlabs_apt
import numpy as np

# Auto-generated wrapper functions


def APTInit(d: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for APTInit"""
    d = ctypes.c_void_p(d)
    return np.int64(thorlabs_apt.APTInit(d))


def APTCleanUp(d: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for APTCleanUp"""
    d = ctypes.c_void_p(d)
    return np.int64(thorlabs_apt.APTCleanUp(d))


def GetNumHWUnitsEx(lHWType: np.int64, plNumUnits: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for GetNumHWUnitsEx"""
    lHWType = ctypes.c_long(lHWType)
    plNumUnits_ptr = ctypes.pointer(ctypes.c_long)
    if plNumUnits is not None:
        plNumUnits_ptr.contents = plNumUnits
    return np.int64(thorlabs_apt.GetNumHWUnitsEx(lHWType, ctypes.byref(plNumUnits_ptr.contents))), np.int64(plNumUnits_ptr.contents)


def GetHWSerialNumEx(lHWType: np.int64, lIndex: np.int64, plSerialNum: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for GetHWSerialNumEx"""
    lHWType = ctypes.c_long(lHWType)
    lIndex = ctypes.c_long(lIndex)
    plSerialNum_ptr = ctypes.pointer(ctypes.c_long)
    if plSerialNum is not None:
        plSerialNum_ptr.contents = plSerialNum
    return np.int64(thorlabs_apt.GetHWSerialNumEx(lHWType, lIndex, ctypes.byref(plSerialNum_ptr.contents))), np.int64(plSerialNum_ptr.contents)


def GetHWInfo(lSerialNum: np.int64, lModelLen: np.int64, lSWVerLen: np.int64, lHWNotesLen: np.int64, szModel: np.int64 = None, szSWVer: np.int64 = None, szHWNotes: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for GetHWInfo"""
    lSerialNum = ctypes.c_long(lSerialNum)
    szModel_ptr = ctypes.pointer(ctypes.c_void_p)
    if szModel is not None:
        szModel_ptr.contents = szModel
    lModelLen = ctypes.c_long(lModelLen)
    szSWVer_ptr = ctypes.pointer(ctypes.c_void_p)
    if szSWVer is not None:
        szSWVer_ptr.contents = szSWVer
    lSWVerLen = ctypes.c_long(lSWVerLen)
    szHWNotes_ptr = ctypes.pointer(ctypes.c_void_p)
    if szHWNotes is not None:
        szHWNotes_ptr.contents = szHWNotes
    lHWNotesLen = ctypes.c_long(lHWNotesLen)
    return np.int64(thorlabs_apt.GetHWInfo(lSerialNum, ctypes.byref(szModel_ptr.contents), lModelLen, ctypes.byref(szSWVer_ptr.contents), lSWVerLen, ctypes.byref(szHWNotes_ptr.contents), lHWNotesLen)), np.int64(szModel_ptr.contents), np.int64(szSWVer_ptr.contents), np.int64(szHWNotes_ptr.contents)


def InitHWDevice(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for InitHWDevice"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.InitHWDevice(lSerialNum))


def EnableEventDlg(bEnable: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for EnableEventDlg"""
    bEnable = ctypes.c_void_p(bEnable)
    return np.int64(thorlabs_apt.EnableEventDlg(bEnable))


def DoEvents(d: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for DoEvents"""
    d = ctypes.c_void_p(d)
    return np.int64(thorlabs_apt.DoEvents(d))


def MOT_ConnectHomeCompleteCallback(lSerialNum: np.int64, pFnHomeCallback: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_ConnectHomeCompleteCallback"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pFnHomeCallback = ctypes.c_void_p(pFnHomeCallback)
    return np.int64(thorlabs_apt.MOT_ConnectHomeCompleteCallback(lSerialNum, pFnHomeCallback))


def MOT_DisconnectHomeCompleteCallback(lSerialNum: np.int64, pFnHomeCallback: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_DisconnectHomeCompleteCallback"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pFnHomeCallback = ctypes.c_void_p(pFnHomeCallback)
    return np.int64(thorlabs_apt.MOT_DisconnectHomeCompleteCallback(lSerialNum, pFnHomeCallback))


def MOT_ConnectMoveCompleteCallback(lSerialNum: np.int64, pFnMoveCallback: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_ConnectMoveCompleteCallback"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pFnMoveCallback = ctypes.c_void_p(pFnMoveCallback)
    return np.int64(thorlabs_apt.MOT_ConnectMoveCompleteCallback(lSerialNum, pFnMoveCallback))


def MOT_DisconnectMoveCompleteCallback(lSerialNum: np.int64, pFnMoveCallback: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_DisconnectMoveCompleteCallback"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pFnMoveCallback = ctypes.c_void_p(pFnMoveCallback)
    return np.int64(thorlabs_apt.MOT_DisconnectMoveCompleteCallback(lSerialNum, pFnMoveCallback))


def MOT_LLSetEncoderCount(lSerialNum: np.int64, lEncCount: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_LLSetEncoderCount"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lEncCount = ctypes.c_long(lEncCount)
    return np.int64(thorlabs_apt.MOT_LLSetEncoderCount(lSerialNum, lEncCount))


def MOT_LLGetEncoderCount(lSerialNum: np.int64, plEncCount: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_LLGetEncoderCount"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plEncCount_ptr = ctypes.pointer(ctypes.c_long)
    if plEncCount is not None:
        plEncCount_ptr.contents = plEncCount
    return np.int64(thorlabs_apt.MOT_LLGetEncoderCount(lSerialNum, ctypes.byref(plEncCount_ptr.contents))), np.int64(plEncCount_ptr.contents)


def MOT_LLSetGetDigOPs(lSerialNum: np.int64, bSet: ctypes.c_void_p, plBits: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_LLSetGetDigOPs"""
    lSerialNum = ctypes.c_long(lSerialNum)
    bSet = ctypes.c_void_p(bSet)
    plBits_ptr = ctypes.pointer(ctypes.c_long)
    if plBits is not None:
        plBits_ptr.contents = plBits
    return np.int64(thorlabs_apt.MOT_LLSetGetDigOPs(lSerialNum, bSet, ctypes.byref(plBits_ptr.contents))), np.int64(plBits_ptr.contents)


def MOT_LLGetADCInputs(lSerialNum: np.int64, plADCVal1: np.int64 = None, plADCVal2: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_LLGetADCInputs"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plADCVal1_ptr = ctypes.pointer(ctypes.c_long)
    if plADCVal1 is not None:
        plADCVal1_ptr.contents = plADCVal1
    plADCVal2_ptr = ctypes.pointer(ctypes.c_long)
    if plADCVal2 is not None:
        plADCVal2_ptr.contents = plADCVal2
    return np.int64(thorlabs_apt.MOT_LLGetADCInputs(lSerialNum, ctypes.byref(plADCVal1_ptr.contents), ctypes.byref(plADCVal2_ptr.contents))), np.int64(plADCVal1_ptr.contents), np.int64(plADCVal2_ptr.contents)


def MOT_SetChannel(lSerialNum: np.int64, lChanID: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetChannel"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lChanID = ctypes.c_long(lChanID)
    return np.int64(thorlabs_apt.MOT_SetChannel(lSerialNum, lChanID))


def MOT_Identify(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_Identify"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.MOT_Identify(lSerialNum))


def MOT_EnableHWChannel(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_EnableHWChannel"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.MOT_EnableHWChannel(lSerialNum))


def MOT_DisableHWChannel(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_DisableHWChannel"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.MOT_DisableHWChannel(lSerialNum))


def MOT_SetVelParams(lSerialNum: np.int64, fMinVel: np.float32, fAccn: np.float32, fMaxVel: np.float32) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetVelParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    fMinVel = ctypes.c_float(fMinVel)
    fAccn = ctypes.c_float(fAccn)
    fMaxVel = ctypes.c_float(fMaxVel)
    return np.int64(thorlabs_apt.MOT_SetVelParams(lSerialNum, fMinVel, fAccn, fMaxVel))


def MOT_GetVelParams(lSerialNum: np.int64, pfMinVel: np.float32 = None, pfAccn: np.float32 = None, pfMaxVel: np.float32 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetVelParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pfMinVel_ptr = ctypes.pointer(ctypes.c_float)
    if pfMinVel is not None:
        pfMinVel_ptr.contents = pfMinVel
    pfAccn_ptr = ctypes.pointer(ctypes.c_float)
    if pfAccn is not None:
        pfAccn_ptr.contents = pfAccn
    pfMaxVel_ptr = ctypes.pointer(ctypes.c_float)
    if pfMaxVel is not None:
        pfMaxVel_ptr.contents = pfMaxVel
    return np.int64(thorlabs_apt.MOT_GetVelParams(lSerialNum, ctypes.byref(pfMinVel_ptr.contents), ctypes.byref(pfAccn_ptr.contents), ctypes.byref(pfMaxVel_ptr.contents))), np.int64(pfMinVel_ptr.contents), np.int64(pfAccn_ptr.contents), np.int64(pfMaxVel_ptr.contents)


def MOT_GetVelParamLimits(lSerialNum: np.int64, pfMaxAccn: np.float32 = None, pfMaxVel: np.float32 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetVelParamLimits"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pfMaxAccn_ptr = ctypes.pointer(ctypes.c_float)
    if pfMaxAccn is not None:
        pfMaxAccn_ptr.contents = pfMaxAccn
    pfMaxVel_ptr = ctypes.pointer(ctypes.c_float)
    if pfMaxVel is not None:
        pfMaxVel_ptr.contents = pfMaxVel
    return np.int64(thorlabs_apt.MOT_GetVelParamLimits(lSerialNum, ctypes.byref(pfMaxAccn_ptr.contents), ctypes.byref(pfMaxVel_ptr.contents))), np.int64(pfMaxAccn_ptr.contents), np.int64(pfMaxVel_ptr.contents)


def MOT_SetHomeParams(lSerialNum: np.int64, lDirection: np.int64, lLimSwitch: np.int64, fHomeVel: np.float32, fZeroOffset: np.float32) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetHomeParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lDirection = ctypes.c_long(lDirection)
    lLimSwitch = ctypes.c_long(lLimSwitch)
    fHomeVel = ctypes.c_float(fHomeVel)
    fZeroOffset = ctypes.c_float(fZeroOffset)
    return np.int64(thorlabs_apt.MOT_SetHomeParams(lSerialNum, lDirection, lLimSwitch, fHomeVel, fZeroOffset))


def MOT_GetHomeParams(lSerialNum: np.int64, plDirection: np.float32 = None, plLimSwitch: np.float32 = None, pfHomeVel: np.float32 = None, pfZeroOffset: np.float32 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetHomeParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plDirection_ptr = ctypes.pointer(ctypes.c_long)
    if plDirection is not None:
        plDirection_ptr.contents = plDirection
    plLimSwitch_ptr = ctypes.pointer(ctypes.c_long)
    if plLimSwitch is not None:
        plLimSwitch_ptr.contents = plLimSwitch
    pfHomeVel_ptr = ctypes.pointer(ctypes.c_float)
    if pfHomeVel is not None:
        pfHomeVel_ptr.contents = pfHomeVel
    pfZeroOffset_ptr = ctypes.pointer(ctypes.c_float)
    if pfZeroOffset is not None:
        pfZeroOffset_ptr.contents = pfZeroOffset
    return np.int64(thorlabs_apt.MOT_GetHomeParams(lSerialNum, ctypes.byref(plDirection_ptr.contents), ctypes.byref(plLimSwitch_ptr.contents), ctypes.byref(pfHomeVel_ptr.contents), ctypes.byref(pfZeroOffset_ptr.contents))), np.int64(plDirection_ptr.contents), np.int64(plLimSwitch_ptr.contents), np.int64(pfHomeVel_ptr.contents), np.int64(pfZeroOffset_ptr.contents)


def MOT_SetJogParams(lSerialNum: np.int64, lMode: np.int64, lStopMode: np.int64, fStepSize: np.float32, fMinVel: np.float32, fAccn: np.float32, fMaxVel: np.float32) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetJogParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lMode = ctypes.c_long(lMode)
    lStopMode = ctypes.c_long(lStopMode)
    fStepSize = ctypes.c_float(fStepSize)
    fMinVel = ctypes.c_float(fMinVel)
    fAccn = ctypes.c_float(fAccn)
    fMaxVel = ctypes.c_float(fMaxVel)
    return np.int64(thorlabs_apt.MOT_SetJogParams(lSerialNum, lMode, lStopMode, fStepSize, fMinVel, fAccn, fMaxVel))


def MOT_GetJogParams(lSerialNum: np.int64, plMode: np.float32 = None, plStopMode: np.float32 = None, pfStepSize: np.float32 = None, pfMinVel: np.float32 = None, pfAccn: np.float32 = None, pfMaxVel: np.float32 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetJogParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plMode_ptr = ctypes.pointer(ctypes.c_long)
    if plMode is not None:
        plMode_ptr.contents = plMode
    plStopMode_ptr = ctypes.pointer(ctypes.c_long)
    if plStopMode is not None:
        plStopMode_ptr.contents = plStopMode
    pfStepSize_ptr = ctypes.pointer(ctypes.c_float)
    if pfStepSize is not None:
        pfStepSize_ptr.contents = pfStepSize
    pfMinVel_ptr = ctypes.pointer(ctypes.c_float)
    if pfMinVel is not None:
        pfMinVel_ptr.contents = pfMinVel
    pfAccn_ptr = ctypes.pointer(ctypes.c_float)
    if pfAccn is not None:
        pfAccn_ptr.contents = pfAccn
    pfMaxVel_ptr = ctypes.pointer(ctypes.c_float)
    if pfMaxVel is not None:
        pfMaxVel_ptr.contents = pfMaxVel
    return np.int64(thorlabs_apt.MOT_GetJogParams(lSerialNum, ctypes.byref(plMode_ptr.contents), ctypes.byref(plStopMode_ptr.contents), ctypes.byref(pfStepSize_ptr.contents), ctypes.byref(pfMinVel_ptr.contents), ctypes.byref(pfAccn_ptr.contents), ctypes.byref(pfMaxVel_ptr.contents))), np.int64(plMode_ptr.contents), np.int64(plStopMode_ptr.contents), np.int64(pfStepSize_ptr.contents), np.int64(pfMinVel_ptr.contents), np.int64(pfAccn_ptr.contents), np.int64(pfMaxVel_ptr.contents)


def MOT_GetStatusBits(lSerialNum: np.int64, plStatusBits: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetStatusBits"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plStatusBits_ptr = ctypes.pointer(ctypes.c_long)
    if plStatusBits is not None:
        plStatusBits_ptr.contents = plStatusBits
    return np.int64(thorlabs_apt.MOT_GetStatusBits(lSerialNum, ctypes.byref(plStatusBits_ptr.contents))), np.int64(plStatusBits_ptr.contents)


def MOT_SetBLashDist(lSerialNum: np.int64, fBLashDist: np.float32) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetBLashDist"""
    lSerialNum = ctypes.c_long(lSerialNum)
    fBLashDist = ctypes.c_float(fBLashDist)
    return np.int64(thorlabs_apt.MOT_SetBLashDist(lSerialNum, fBLashDist))


def MOT_GetBLashDist(lSerialNum: np.int64, pfBLashDist: np.float32 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetBLashDist"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pfBLashDist_ptr = ctypes.pointer(ctypes.c_float)
    if pfBLashDist is not None:
        pfBLashDist_ptr.contents = pfBLashDist
    return np.int64(thorlabs_apt.MOT_GetBLashDist(lSerialNum, ctypes.byref(pfBLashDist_ptr.contents))), np.int64(pfBLashDist_ptr.contents)


def MOT_SetMotorParams(lSerialNum: np.int64, lStepsPerRev: np.int64, lGearBoxRatio: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetMotorParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lStepsPerRev = ctypes.c_long(lStepsPerRev)
    lGearBoxRatio = ctypes.c_long(lGearBoxRatio)
    return np.int64(thorlabs_apt.MOT_SetMotorParams(lSerialNum, lStepsPerRev, lGearBoxRatio))


def MOT_GetMotorParams(lSerialNum: np.int64, plStepsPerRev: np.int64 = None, plGearBoxRatio: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetMotorParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plStepsPerRev_ptr = ctypes.pointer(ctypes.c_long)
    if plStepsPerRev is not None:
        plStepsPerRev_ptr.contents = plStepsPerRev
    plGearBoxRatio_ptr = ctypes.pointer(ctypes.c_long)
    if plGearBoxRatio is not None:
        plGearBoxRatio_ptr.contents = plGearBoxRatio
    return np.int64(thorlabs_apt.MOT_GetMotorParams(lSerialNum, ctypes.byref(plStepsPerRev_ptr.contents), ctypes.byref(plGearBoxRatio_ptr.contents))), np.int64(plStepsPerRev_ptr.contents), np.int64(plGearBoxRatio_ptr.contents)


def MOT_SetStageAxisInfo(lSerialNum: np.int64, fMinPos: np.float32, fMaxPos: np.float32, lUnits: np.int64, fPitch: np.float32) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetStageAxisInfo"""
    lSerialNum = ctypes.c_long(lSerialNum)
    fMinPos = ctypes.c_float(fMinPos)
    fMaxPos = ctypes.c_float(fMaxPos)
    lUnits = ctypes.c_long(lUnits)
    fPitch = ctypes.c_float(fPitch)
    return np.int64(thorlabs_apt.MOT_SetStageAxisInfo(lSerialNum, fMinPos, fMaxPos, lUnits, fPitch))


def MOT_GetStageAxisInfo(lSerialNum: np.int64, pfMinPos: np.float32 = None, pfMaxPos: np.float32 = None, plUnits: np.float32 = None, pfPitch: np.float32 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetStageAxisInfo"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pfMinPos_ptr = ctypes.pointer(ctypes.c_float)
    if pfMinPos is not None:
        pfMinPos_ptr.contents = pfMinPos
    pfMaxPos_ptr = ctypes.pointer(ctypes.c_float)
    if pfMaxPos is not None:
        pfMaxPos_ptr.contents = pfMaxPos
    plUnits_ptr = ctypes.pointer(ctypes.c_long)
    if plUnits is not None:
        plUnits_ptr.contents = plUnits
    pfPitch_ptr = ctypes.pointer(ctypes.c_float)
    if pfPitch is not None:
        pfPitch_ptr.contents = pfPitch
    return np.int64(thorlabs_apt.MOT_GetStageAxisInfo(lSerialNum, ctypes.byref(pfMinPos_ptr.contents), ctypes.byref(pfMaxPos_ptr.contents), ctypes.byref(plUnits_ptr.contents), ctypes.byref(pfPitch_ptr.contents))), np.int64(pfMinPos_ptr.contents), np.int64(pfMaxPos_ptr.contents), np.int64(plUnits_ptr.contents), np.int64(pfPitch_ptr.contents)


def MOT_SetHWLimSwitches(lSerialNum: np.int64, lRevLimSwitch: np.int64, lFwdLimSwitch: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetHWLimSwitches"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lRevLimSwitch = ctypes.c_long(lRevLimSwitch)
    lFwdLimSwitch = ctypes.c_long(lFwdLimSwitch)
    return np.int64(thorlabs_apt.MOT_SetHWLimSwitches(lSerialNum, lRevLimSwitch, lFwdLimSwitch))


def MOT_GetHWLimSwitches(lSerialNum: np.int64, plRevLimSwitch: np.int64 = None, plFwdLimSwitch: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetHWLimSwitches"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plRevLimSwitch_ptr = ctypes.pointer(ctypes.c_long)
    if plRevLimSwitch is not None:
        plRevLimSwitch_ptr.contents = plRevLimSwitch
    plFwdLimSwitch_ptr = ctypes.pointer(ctypes.c_long)
    if plFwdLimSwitch is not None:
        plFwdLimSwitch_ptr.contents = plFwdLimSwitch
    return np.int64(thorlabs_apt.MOT_GetHWLimSwitches(lSerialNum, ctypes.byref(plRevLimSwitch_ptr.contents), ctypes.byref(plFwdLimSwitch_ptr.contents))), np.int64(plRevLimSwitch_ptr.contents), np.int64(plFwdLimSwitch_ptr.contents)


def MOT_SetPIDParams(lSerialNum: np.int64, lProp: np.int64, lInt: np.int64, lDeriv: np.int64, lIntLimit: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetPIDParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lProp = ctypes.c_long(lProp)
    lInt = ctypes.c_long(lInt)
    lDeriv = ctypes.c_long(lDeriv)
    lIntLimit = ctypes.c_long(lIntLimit)
    return np.int64(thorlabs_apt.MOT_SetPIDParams(lSerialNum, lProp, lInt, lDeriv, lIntLimit))


def MOT_GetPIDParams(lSerialNum: np.int64, plProp: np.int64 = None, plInt: np.int64 = None, plDeriv: np.int64 = None, plIntLimit: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetPIDParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plProp_ptr = ctypes.pointer(ctypes.c_long)
    if plProp is not None:
        plProp_ptr.contents = plProp
    plInt_ptr = ctypes.pointer(ctypes.c_long)
    if plInt is not None:
        plInt_ptr.contents = plInt
    plDeriv_ptr = ctypes.pointer(ctypes.c_long)
    if plDeriv is not None:
        plDeriv_ptr.contents = plDeriv
    plIntLimit_ptr = ctypes.pointer(ctypes.c_long)
    if plIntLimit is not None:
        plIntLimit_ptr.contents = plIntLimit
    return np.int64(thorlabs_apt.MOT_GetPIDParams(lSerialNum, ctypes.byref(plProp_ptr.contents), ctypes.byref(plInt_ptr.contents), ctypes.byref(plDeriv_ptr.contents), ctypes.byref(plIntLimit_ptr.contents))), np.int64(plProp_ptr.contents), np.int64(plInt_ptr.contents), np.int64(plDeriv_ptr.contents), np.int64(plIntLimit_ptr.contents)


def MOT_SetPhaseCurrents(lSerialNum: np.int64, lRestVal: np.int64, lMoveVal: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetPhaseCurrents"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lRestVal = ctypes.c_long(lRestVal)
    lMoveVal = ctypes.c_long(lMoveVal)
    return np.int64(thorlabs_apt.MOT_SetPhaseCurrents(lSerialNum, lRestVal, lMoveVal))


def MOT_GetPhaseCurrents(lSerialNum: np.int64, plRestVal: np.int64 = None, plMoveVal: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetPhaseCurrents"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plRestVal_ptr = ctypes.pointer(ctypes.c_long)
    if plRestVal is not None:
        plRestVal_ptr.contents = plRestVal
    plMoveVal_ptr = ctypes.pointer(ctypes.c_long)
    if plMoveVal is not None:
        plMoveVal_ptr.contents = plMoveVal
    return np.int64(thorlabs_apt.MOT_GetPhaseCurrents(lSerialNum, ctypes.byref(plRestVal_ptr.contents), ctypes.byref(plMoveVal_ptr.contents))), np.int64(plRestVal_ptr.contents), np.int64(plMoveVal_ptr.contents)


def MOT_GetPosition(lSerialNum: np.int64, pfPosition: np.float32 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetPosition"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pfPosition_ptr = ctypes.pointer(ctypes.c_float)
    if pfPosition is not None:
        pfPosition_ptr.contents = pfPosition
    return np.int64(thorlabs_apt.MOT_GetPosition(lSerialNum, ctypes.byref(pfPosition_ptr.contents))), np.int64(pfPosition_ptr.contents)


def MOT_GetPositionEx(lSerialNum: np.int64, pfCalibPosition: np.float32 = None, pfUncalibPosition: np.float32 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetPositionEx"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pfCalibPosition_ptr = ctypes.pointer(ctypes.c_float)
    if pfCalibPosition is not None:
        pfCalibPosition_ptr.contents = pfCalibPosition
    pfUncalibPosition_ptr = ctypes.pointer(ctypes.c_float)
    if pfUncalibPosition is not None:
        pfUncalibPosition_ptr.contents = pfUncalibPosition
    return np.int64(thorlabs_apt.MOT_GetPositionEx(lSerialNum, ctypes.byref(pfCalibPosition_ptr.contents), ctypes.byref(pfUncalibPosition_ptr.contents))), np.int64(pfCalibPosition_ptr.contents), np.int64(pfUncalibPosition_ptr.contents)


def MOT_MoveHome(lSerialNum: np.int64, bWait: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_MoveHome"""
    lSerialNum = ctypes.c_long(lSerialNum)
    bWait = ctypes.c_void_p(bWait)
    return np.int64(thorlabs_apt.MOT_MoveHome(lSerialNum, bWait))


def MOT_MoveRelativeEx(lSerialNum: np.int64, fRelDist: np.float32, bWait: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_MoveRelativeEx"""
    lSerialNum = ctypes.c_long(lSerialNum)
    fRelDist = ctypes.c_float(fRelDist)
    bWait = ctypes.c_void_p(bWait)
    return np.int64(thorlabs_apt.MOT_MoveRelativeEx(lSerialNum, fRelDist, bWait))


def MOT_MoveAbsoluteEx(lSerialNum: np.int64, fAbsPos: np.float32, bWait: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_MoveAbsoluteEx"""
    lSerialNum = ctypes.c_long(lSerialNum)
    fAbsPos = ctypes.c_float(fAbsPos)
    bWait = ctypes.c_void_p(bWait)
    return np.int64(thorlabs_apt.MOT_MoveAbsoluteEx(lSerialNum, fAbsPos, bWait))


def MOT_MoveVelocity(lSerialNum: np.int64, lDirection: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_MoveVelocity"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lDirection = ctypes.c_long(lDirection)
    return np.int64(thorlabs_apt.MOT_MoveVelocity(lSerialNum, lDirection))


def MOT_MoveJog(lSerialNum: np.int64, lJogDir: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_MoveJog"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lJogDir = ctypes.c_long(lJogDir)
    return np.int64(thorlabs_apt.MOT_MoveJog(lSerialNum, lJogDir))


def MOT_MoveAbsoluteRot(lSerialNum: np.int64, fAnglePos: np.float32, lMoveMode: np.int64, bWait: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_MoveAbsoluteRot"""
    lSerialNum = ctypes.c_long(lSerialNum)
    fAnglePos = ctypes.c_float(fAnglePos)
    lMoveMode = ctypes.c_long(lMoveMode)
    bWait = ctypes.c_void_p(bWait)
    return np.int64(thorlabs_apt.MOT_MoveAbsoluteRot(lSerialNum, fAnglePos, lMoveMode, bWait))


def MOT_StopProfiled(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_StopProfiled"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.MOT_StopProfiled(lSerialNum))


def MOT_SetDCCurrentLoopParams(lSerialNum: np.int64, lProp: np.int64, lInt: np.int64, lIntLim: np.int64, lIntDeadBand: np.int64, lFFwd: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetDCCurrentLoopParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lProp = ctypes.c_long(lProp)
    lInt = ctypes.c_long(lInt)
    lIntLim = ctypes.c_long(lIntLim)
    lIntDeadBand = ctypes.c_long(lIntDeadBand)
    lFFwd = ctypes.c_long(lFFwd)
    return np.int64(thorlabs_apt.MOT_SetDCCurrentLoopParams(lSerialNum, lProp, lInt, lIntLim, lIntDeadBand, lFFwd))


def MOT_GetDCCurrentLoopParams(lSerialNum: np.int64, plProp: np.int64 = None, plInt: np.int64 = None, plIntLim: np.int64 = None, plIntDeadBand: np.int64 = None, plFFwd: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetDCCurrentLoopParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plProp_ptr = ctypes.pointer(ctypes.c_long)
    if plProp is not None:
        plProp_ptr.contents = plProp
    plInt_ptr = ctypes.pointer(ctypes.c_long)
    if plInt is not None:
        plInt_ptr.contents = plInt
    plIntLim_ptr = ctypes.pointer(ctypes.c_long)
    if plIntLim is not None:
        plIntLim_ptr.contents = plIntLim
    plIntDeadBand_ptr = ctypes.pointer(ctypes.c_long)
    if plIntDeadBand is not None:
        plIntDeadBand_ptr.contents = plIntDeadBand
    plFFwd_ptr = ctypes.pointer(ctypes.c_long)
    if plFFwd is not None:
        plFFwd_ptr.contents = plFFwd
    return np.int64(thorlabs_apt.MOT_GetDCCurrentLoopParams(lSerialNum, ctypes.byref(plProp_ptr.contents), ctypes.byref(plInt_ptr.contents), ctypes.byref(plIntLim_ptr.contents), ctypes.byref(plIntDeadBand_ptr.contents), ctypes.byref(plFFwd_ptr.contents))), np.int64(plProp_ptr.contents), np.int64(plInt_ptr.contents), np.int64(plIntLim_ptr.contents), np.int64(plIntDeadBand_ptr.contents), np.int64(plFFwd_ptr.contents)


def MOT_SetDCPositionLoopParams(lSerialNum: np.int64, lProp: np.int64, lInt: np.int64, lIntLim: np.int64, lDeriv: np.int64, lDerivTime: np.int64, lLoopGain: np.int64, lVelFFwd: np.int64, lAccFFwd: np.int64, lPosErrLim: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetDCPositionLoopParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lProp = ctypes.c_long(lProp)
    lInt = ctypes.c_long(lInt)
    lIntLim = ctypes.c_long(lIntLim)
    lDeriv = ctypes.c_long(lDeriv)
    lDerivTime = ctypes.c_long(lDerivTime)
    lLoopGain = ctypes.c_long(lLoopGain)
    lVelFFwd = ctypes.c_long(lVelFFwd)
    lAccFFwd = ctypes.c_long(lAccFFwd)
    lPosErrLim = ctypes.c_long(lPosErrLim)
    return np.int64(thorlabs_apt.MOT_SetDCPositionLoopParams(lSerialNum, lProp, lInt, lIntLim, lDeriv, lDerivTime, lLoopGain, lVelFFwd, lAccFFwd, lPosErrLim))


def MOT_GetDCPositionLoopParams(lSerialNum: np.int64, plProp: np.int64 = None, plInt: np.int64 = None, plIntLim: np.int64 = None, plDeriv: np.int64 = None, plDerivTime: np.int64 = None, plLoopGain: np.int64 = None, plVelFFwd: np.int64 = None, plAccFFwd: np.int64 = None, plPosErrLim: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetDCPositionLoopParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plProp_ptr = ctypes.pointer(ctypes.c_long)
    if plProp is not None:
        plProp_ptr.contents = plProp
    plInt_ptr = ctypes.pointer(ctypes.c_long)
    if plInt is not None:
        plInt_ptr.contents = plInt
    plIntLim_ptr = ctypes.pointer(ctypes.c_long)
    if plIntLim is not None:
        plIntLim_ptr.contents = plIntLim
    plDeriv_ptr = ctypes.pointer(ctypes.c_long)
    if plDeriv is not None:
        plDeriv_ptr.contents = plDeriv
    plDerivTime_ptr = ctypes.pointer(ctypes.c_long)
    if plDerivTime is not None:
        plDerivTime_ptr.contents = plDerivTime
    plLoopGain_ptr = ctypes.pointer(ctypes.c_long)
    if plLoopGain is not None:
        plLoopGain_ptr.contents = plLoopGain
    plVelFFwd_ptr = ctypes.pointer(ctypes.c_long)
    if plVelFFwd is not None:
        plVelFFwd_ptr.contents = plVelFFwd
    plAccFFwd_ptr = ctypes.pointer(ctypes.c_long)
    if plAccFFwd is not None:
        plAccFFwd_ptr.contents = plAccFFwd
    plPosErrLim_ptr = ctypes.pointer(ctypes.c_long)
    if plPosErrLim is not None:
        plPosErrLim_ptr.contents = plPosErrLim
    return np.int64(thorlabs_apt.MOT_GetDCPositionLoopParams(lSerialNum, ctypes.byref(plProp_ptr.contents), ctypes.byref(plInt_ptr.contents), ctypes.byref(plIntLim_ptr.contents), ctypes.byref(plDeriv_ptr.contents), ctypes.byref(plDerivTime_ptr.contents), ctypes.byref(plLoopGain_ptr.contents), ctypes.byref(plVelFFwd_ptr.contents), ctypes.byref(plAccFFwd_ptr.contents), ctypes.byref(plPosErrLim_ptr.contents))), np.int64(plProp_ptr.contents), np.int64(plInt_ptr.contents), np.int64(plIntLim_ptr.contents), np.int64(plDeriv_ptr.contents), np.int64(plDerivTime_ptr.contents), np.int64(plLoopGain_ptr.contents), np.int64(plVelFFwd_ptr.contents), np.int64(plAccFFwd_ptr.contents), np.int64(plPosErrLim_ptr.contents)


def MOT_SetDCMotorOutputParams(lSerialNum: np.int64, fContCurrLim: np.float32, fEnergyLim: np.float32, fMotorLim: np.float32, fMotorBias: np.float32) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetDCMotorOutputParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    fContCurrLim = ctypes.c_float(fContCurrLim)
    fEnergyLim = ctypes.c_float(fEnergyLim)
    fMotorLim = ctypes.c_float(fMotorLim)
    fMotorBias = ctypes.c_float(fMotorBias)
    return np.int64(thorlabs_apt.MOT_SetDCMotorOutputParams(lSerialNum, fContCurrLim, fEnergyLim, fMotorLim, fMotorBias))


def MOT_GetDCMotorOutputParams(lSerialNum: np.int64, pfContCurrLim: np.float32 = None, pfEnergyLim: np.float32 = None, pfMotorLim: np.float32 = None, pfMotorBias: np.float32 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetDCMotorOutputParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pfContCurrLim_ptr = ctypes.pointer(ctypes.c_float)
    if pfContCurrLim is not None:
        pfContCurrLim_ptr.contents = pfContCurrLim
    pfEnergyLim_ptr = ctypes.pointer(ctypes.c_float)
    if pfEnergyLim is not None:
        pfEnergyLim_ptr.contents = pfEnergyLim
    pfMotorLim_ptr = ctypes.pointer(ctypes.c_float)
    if pfMotorLim is not None:
        pfMotorLim_ptr.contents = pfMotorLim
    pfMotorBias_ptr = ctypes.pointer(ctypes.c_float)
    if pfMotorBias is not None:
        pfMotorBias_ptr.contents = pfMotorBias
    return np.int64(thorlabs_apt.MOT_GetDCMotorOutputParams(lSerialNum, ctypes.byref(pfContCurrLim_ptr.contents), ctypes.byref(pfEnergyLim_ptr.contents), ctypes.byref(pfMotorLim_ptr.contents), ctypes.byref(pfMotorBias_ptr.contents))), np.int64(pfContCurrLim_ptr.contents), np.int64(pfEnergyLim_ptr.contents), np.int64(pfMotorLim_ptr.contents), np.int64(pfMotorBias_ptr.contents)


def MOT_SetDCTrackSettleParams(lSerialNum: np.int64, lSettleTime: np.int64, lSettleWnd: np.int64, lTrackWnd: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetDCTrackSettleParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lSettleTime = ctypes.c_long(lSettleTime)
    lSettleWnd = ctypes.c_long(lSettleWnd)
    lTrackWnd = ctypes.c_long(lTrackWnd)
    return np.int64(thorlabs_apt.MOT_SetDCTrackSettleParams(lSerialNum, lSettleTime, lSettleWnd, lTrackWnd))


def MOT_GetDCTrackSettleParams(lSerialNum: np.int64, plSettleTime: np.int64 = None, plSettleWnd: np.int64 = None, plTrackWnd: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetDCTrackSettleParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plSettleTime_ptr = ctypes.pointer(ctypes.c_long)
    if plSettleTime is not None:
        plSettleTime_ptr.contents = plSettleTime
    plSettleWnd_ptr = ctypes.pointer(ctypes.c_long)
    if plSettleWnd is not None:
        plSettleWnd_ptr.contents = plSettleWnd
    plTrackWnd_ptr = ctypes.pointer(ctypes.c_long)
    if plTrackWnd is not None:
        plTrackWnd_ptr.contents = plTrackWnd
    return np.int64(thorlabs_apt.MOT_GetDCTrackSettleParams(lSerialNum, ctypes.byref(plSettleTime_ptr.contents), ctypes.byref(plSettleWnd_ptr.contents), ctypes.byref(plTrackWnd_ptr.contents))), np.int64(plSettleTime_ptr.contents), np.int64(plSettleWnd_ptr.contents), np.int64(plTrackWnd_ptr.contents)


def MOT_SetDCProfileModeParams(lSerialNum: np.int64, lProfMode: np.int64, fJerk: np.float32) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetDCProfileModeParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lProfMode = ctypes.c_long(lProfMode)
    fJerk = ctypes.c_float(fJerk)
    return np.int64(thorlabs_apt.MOT_SetDCProfileModeParams(lSerialNum, lProfMode, fJerk))


def MOT_GetDCProfileModeParams(lSerialNum: np.int64, plProfMode: np.float32 = None, pfJerk: np.float32 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetDCProfileModeParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plProfMode_ptr = ctypes.pointer(ctypes.c_long)
    if plProfMode is not None:
        plProfMode_ptr.contents = plProfMode
    pfJerk_ptr = ctypes.pointer(ctypes.c_float)
    if pfJerk is not None:
        pfJerk_ptr.contents = pfJerk
    return np.int64(thorlabs_apt.MOT_GetDCProfileModeParams(lSerialNum, ctypes.byref(plProfMode_ptr.contents), ctypes.byref(pfJerk_ptr.contents))), np.int64(plProfMode_ptr.contents), np.int64(pfJerk_ptr.contents)


def MOT_SetDCJoystickParams(lSerialNum: np.int64, fMaxVelLO: np.float32, fMaxVelHI: np.float32, fAccnLO: np.float32, fAccnHI: np.float32, lDirSense: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetDCJoystickParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    fMaxVelLO = ctypes.c_float(fMaxVelLO)
    fMaxVelHI = ctypes.c_float(fMaxVelHI)
    fAccnLO = ctypes.c_float(fAccnLO)
    fAccnHI = ctypes.c_float(fAccnHI)
    lDirSense = ctypes.c_long(lDirSense)
    return np.int64(thorlabs_apt.MOT_SetDCJoystickParams(lSerialNum, fMaxVelLO, fMaxVelHI, fAccnLO, fAccnHI, lDirSense))


def MOT_GetDCJoystickParams(lSerialNum: np.int64, pfMaxVelLO: np.int64 = None, pfMaxVelHI: np.int64 = None, pfAccnLO: np.int64 = None, pfAccnHI: np.int64 = None, plDirSense: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetDCJoystickParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pfMaxVelLO_ptr = ctypes.pointer(ctypes.c_float)
    if pfMaxVelLO is not None:
        pfMaxVelLO_ptr.contents = pfMaxVelLO
    pfMaxVelHI_ptr = ctypes.pointer(ctypes.c_float)
    if pfMaxVelHI is not None:
        pfMaxVelHI_ptr.contents = pfMaxVelHI
    pfAccnLO_ptr = ctypes.pointer(ctypes.c_float)
    if pfAccnLO is not None:
        pfAccnLO_ptr.contents = pfAccnLO
    pfAccnHI_ptr = ctypes.pointer(ctypes.c_float)
    if pfAccnHI is not None:
        pfAccnHI_ptr.contents = pfAccnHI
    plDirSense_ptr = ctypes.pointer(ctypes.c_long)
    if plDirSense is not None:
        plDirSense_ptr.contents = plDirSense
    return np.int64(thorlabs_apt.MOT_GetDCJoystickParams(lSerialNum, ctypes.byref(pfMaxVelLO_ptr.contents), ctypes.byref(pfMaxVelHI_ptr.contents), ctypes.byref(pfAccnLO_ptr.contents), ctypes.byref(pfAccnHI_ptr.contents), ctypes.byref(plDirSense_ptr.contents))), np.int64(pfMaxVelLO_ptr.contents), np.int64(pfMaxVelHI_ptr.contents), np.int64(pfAccnLO_ptr.contents), np.int64(pfAccnHI_ptr.contents), np.int64(plDirSense_ptr.contents)


def MOT_SetDCSettledCurrentLoopParams(lSerialNum: np.int64, lSettledProp: np.int64, lSettledInt: np.int64, lSettledIntLim: np.int64, lSettledIntDeadBand: np.int64, lSettledFFwd: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetDCSettledCurrentLoopParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lSettledProp = ctypes.c_long(lSettledProp)
    lSettledInt = ctypes.c_long(lSettledInt)
    lSettledIntLim = ctypes.c_long(lSettledIntLim)
    lSettledIntDeadBand = ctypes.c_long(lSettledIntDeadBand)
    lSettledFFwd = ctypes.c_long(lSettledFFwd)
    return np.int64(thorlabs_apt.MOT_SetDCSettledCurrentLoopParams(lSerialNum, lSettledProp, lSettledInt, lSettledIntLim, lSettledIntDeadBand, lSettledFFwd))


def MOT_GetDCSettledCurrentLoopParams(lSerialNum: np.int64, plSettledProp: np.int64 = None, plSettledInt: np.int64 = None, plSettledIntLim: np.int64 = None, plSettledIntDeadBand: np.int64 = None, plSettledFFwd: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetDCSettledCurrentLoopParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plSettledProp_ptr = ctypes.pointer(ctypes.c_long)
    if plSettledProp is not None:
        plSettledProp_ptr.contents = plSettledProp
    plSettledInt_ptr = ctypes.pointer(ctypes.c_long)
    if plSettledInt is not None:
        plSettledInt_ptr.contents = plSettledInt
    plSettledIntLim_ptr = ctypes.pointer(ctypes.c_long)
    if plSettledIntLim is not None:
        plSettledIntLim_ptr.contents = plSettledIntLim
    plSettledIntDeadBand_ptr = ctypes.pointer(ctypes.c_long)
    if plSettledIntDeadBand is not None:
        plSettledIntDeadBand_ptr.contents = plSettledIntDeadBand
    plSettledFFwd_ptr = ctypes.pointer(ctypes.c_long)
    if plSettledFFwd is not None:
        plSettledFFwd_ptr.contents = plSettledFFwd
    return np.int64(thorlabs_apt.MOT_GetDCSettledCurrentLoopParams(lSerialNum, ctypes.byref(plSettledProp_ptr.contents), ctypes.byref(plSettledInt_ptr.contents), ctypes.byref(plSettledIntLim_ptr.contents), ctypes.byref(plSettledIntDeadBand_ptr.contents), ctypes.byref(plSettledFFwd_ptr.contents))), np.int64(plSettledProp_ptr.contents), np.int64(plSettledInt_ptr.contents), np.int64(plSettledIntLim_ptr.contents), np.int64(plSettledIntDeadBand_ptr.contents), np.int64(plSettledFFwd_ptr.contents)


def MOT_SetBowIndex(lSerialNum: np.int64, lBowIndex: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetBowIndex"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lBowIndex = ctypes.c_long(lBowIndex)
    return np.int64(thorlabs_apt.MOT_SetBowIndex(lSerialNum, lBowIndex))


def MOT_GetBowIndex(lSerialNum: np.int64, plBowIndex: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetBowIndex"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plBowIndex_ptr = ctypes.pointer(ctypes.c_long)
    if plBowIndex is not None:
        plBowIndex_ptr.contents = plBowIndex
    return np.int64(thorlabs_apt.MOT_GetBowIndex(lSerialNum, ctypes.byref(plBowIndex_ptr.contents))), np.int64(plBowIndex_ptr.contents)


def MOT_SetDCTriggerParams(lSerialNum: np.int64, lTrigInMode: np.int64, lTrigOutMode: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetDCTriggerParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lTrigInMode = ctypes.c_long(lTrigInMode)
    lTrigOutMode = ctypes.c_long(lTrigOutMode)
    return np.int64(thorlabs_apt.MOT_SetDCTriggerParams(lSerialNum, lTrigInMode, lTrigOutMode))


def MOT_GetDCTriggerParams(lSerialNum: np.int64, plTrigInMode: np.int64 = None, plTrigOutMode: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetDCTriggerParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plTrigInMode_ptr = ctypes.pointer(ctypes.c_long)
    if plTrigInMode is not None:
        plTrigInMode_ptr.contents = plTrigInMode
    plTrigOutMode_ptr = ctypes.pointer(ctypes.c_long)
    if plTrigOutMode is not None:
        plTrigOutMode_ptr.contents = plTrigOutMode
    return np.int64(thorlabs_apt.MOT_GetDCTriggerParams(lSerialNum, ctypes.byref(plTrigInMode_ptr.contents), ctypes.byref(plTrigOutMode_ptr.contents))), np.int64(plTrigInMode_ptr.contents), np.int64(plTrigOutMode_ptr.contents)


def MOT_SetKCubePanelParams(lSerialNum: np.int64, lWheelMode: np.int64, fWheelVel: np.float32, fWheelAccn: np.float32, lWheelDirSense: np.int64, fPresetPos1: np.float32, fPresetPos2: np.float32, lDispBrightness: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetKCubePanelParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lWheelMode = ctypes.c_long(lWheelMode)
    fWheelVel = ctypes.c_float(fWheelVel)
    fWheelAccn = ctypes.c_float(fWheelAccn)
    lWheelDirSense = ctypes.c_long(lWheelDirSense)
    fPresetPos1 = ctypes.c_float(fPresetPos1)
    fPresetPos2 = ctypes.c_float(fPresetPos2)
    lDispBrightness = ctypes.c_long(lDispBrightness)
    return np.int64(thorlabs_apt.MOT_SetKCubePanelParams(lSerialNum, lWheelMode, fWheelVel, fWheelAccn, lWheelDirSense, fPresetPos1, fPresetPos2, lDispBrightness))


def MOT_GetKCubePanelParams(lSerialNum: np.int64, plWheelMode: np.int64 = None, pfWheelVel: np.int64 = None, pfWheelAccn: np.int64 = None, plWheelDirSense: np.int64 = None, pfPresetPos1: np.int64 = None, pfPresetPos2: np.int64 = None, plDispBrightness: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetKCubePanelParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plWheelMode_ptr = ctypes.pointer(ctypes.c_long)
    if plWheelMode is not None:
        plWheelMode_ptr.contents = plWheelMode
    pfWheelVel_ptr = ctypes.pointer(ctypes.c_float)
    if pfWheelVel is not None:
        pfWheelVel_ptr.contents = pfWheelVel
    pfWheelAccn_ptr = ctypes.pointer(ctypes.c_float)
    if pfWheelAccn is not None:
        pfWheelAccn_ptr.contents = pfWheelAccn
    plWheelDirSense_ptr = ctypes.pointer(ctypes.c_long)
    if plWheelDirSense is not None:
        plWheelDirSense_ptr.contents = plWheelDirSense
    pfPresetPos1_ptr = ctypes.pointer(ctypes.c_float)
    if pfPresetPos1 is not None:
        pfPresetPos1_ptr.contents = pfPresetPos1
    pfPresetPos2_ptr = ctypes.pointer(ctypes.c_float)
    if pfPresetPos2 is not None:
        pfPresetPos2_ptr.contents = pfPresetPos2
    plDispBrightness_ptr = ctypes.pointer(ctypes.c_long)
    if plDispBrightness is not None:
        plDispBrightness_ptr.contents = plDispBrightness
    return np.int64(thorlabs_apt.MOT_GetKCubePanelParams(lSerialNum, ctypes.byref(plWheelMode_ptr.contents), ctypes.byref(pfWheelVel_ptr.contents), ctypes.byref(pfWheelAccn_ptr.contents), ctypes.byref(plWheelDirSense_ptr.contents), ctypes.byref(pfPresetPos1_ptr.contents), ctypes.byref(pfPresetPos2_ptr.contents), ctypes.byref(plDispBrightness_ptr.contents))), np.int64(plWheelMode_ptr.contents), np.int64(pfWheelVel_ptr.contents), np.int64(pfWheelAccn_ptr.contents), np.int64(plWheelDirSense_ptr.contents), np.int64(pfPresetPos1_ptr.contents), np.int64(pfPresetPos2_ptr.contents), np.int64(plDispBrightness_ptr.contents)


def MOT_SetKCubeTriggerParams(lSerialNum: np.int64, lTrig1Mode: np.int64, lTrig1Polarity: np.int64, lTrig2Mode: np.int64, lTrig2Polarity: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetKCubeTriggerParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lTrig1Mode = ctypes.c_long(lTrig1Mode)
    lTrig1Polarity = ctypes.c_long(lTrig1Polarity)
    lTrig2Mode = ctypes.c_long(lTrig2Mode)
    lTrig2Polarity = ctypes.c_long(lTrig2Polarity)
    return np.int64(thorlabs_apt.MOT_SetKCubeTriggerParams(lSerialNum, lTrig1Mode, lTrig1Polarity, lTrig2Mode, lTrig2Polarity))


def MOT_GetKCubeTriggerParams(lSerialNum: np.int64, plTrig1Mode: np.int64 = None, plTrig1Polarity: np.int64 = None, plTrig2Mode: np.int64 = None, plTrig2Polarity: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetKCubeTriggerParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plTrig1Mode_ptr = ctypes.pointer(ctypes.c_long)
    if plTrig1Mode is not None:
        plTrig1Mode_ptr.contents = plTrig1Mode
    plTrig1Polarity_ptr = ctypes.pointer(ctypes.c_long)
    if plTrig1Polarity is not None:
        plTrig1Polarity_ptr.contents = plTrig1Polarity
    plTrig2Mode_ptr = ctypes.pointer(ctypes.c_long)
    if plTrig2Mode is not None:
        plTrig2Mode_ptr.contents = plTrig2Mode
    plTrig2Polarity_ptr = ctypes.pointer(ctypes.c_long)
    if plTrig2Polarity is not None:
        plTrig2Polarity_ptr.contents = plTrig2Polarity
    return np.int64(thorlabs_apt.MOT_GetKCubeTriggerParams(lSerialNum, ctypes.byref(plTrig1Mode_ptr.contents), ctypes.byref(plTrig1Polarity_ptr.contents), ctypes.byref(plTrig2Mode_ptr.contents), ctypes.byref(plTrig2Polarity_ptr.contents))), np.int64(plTrig1Mode_ptr.contents), np.int64(plTrig1Polarity_ptr.contents), np.int64(plTrig2Mode_ptr.contents), np.int64(plTrig2Polarity_ptr.contents)


def MOT_SetKCubePosTriggerParams(lSerialNum: np.int64, fStartPosFwd: np.float32, fPosIntervalFwd: np.float32, lNumPulsesFwd: np.int64, fStartPosRev: np.float32, fPosIntervalRev: np.float32, lNumPulsesRev: np.int64, fPulseWidth: np.float32, lNumCycles: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetKCubePosTriggerParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    fStartPosFwd = ctypes.c_float(fStartPosFwd)
    fPosIntervalFwd = ctypes.c_float(fPosIntervalFwd)
    lNumPulsesFwd = ctypes.c_long(lNumPulsesFwd)
    fStartPosRev = ctypes.c_float(fStartPosRev)
    fPosIntervalRev = ctypes.c_float(fPosIntervalRev)
    lNumPulsesRev = ctypes.c_long(lNumPulsesRev)
    fPulseWidth = ctypes.c_float(fPulseWidth)
    lNumCycles = ctypes.c_long(lNumCycles)
    return np.int64(thorlabs_apt.MOT_SetKCubePosTriggerParams(lSerialNum, fStartPosFwd, fPosIntervalFwd, lNumPulsesFwd, fStartPosRev, fPosIntervalRev, lNumPulsesRev, fPulseWidth, lNumCycles))


def MOT_GetKCubePosTriggerParams(lSerialNum: np.int64, pfStartPosFwd: np.int64 = None, pfPosIntervalFwd: np.int64 = None, plNumPulsesFwd: np.int64 = None, pfStartPosRev: np.int64 = None, pfPosIntervalRev: np.int64 = None, plNumPulsesRev: np.int64 = None, pfPulseWidth: np.int64 = None, plNumCycles: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetKCubePosTriggerParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pfStartPosFwd_ptr = ctypes.pointer(ctypes.c_float)
    if pfStartPosFwd is not None:
        pfStartPosFwd_ptr.contents = pfStartPosFwd
    pfPosIntervalFwd_ptr = ctypes.pointer(ctypes.c_float)
    if pfPosIntervalFwd is not None:
        pfPosIntervalFwd_ptr.contents = pfPosIntervalFwd
    plNumPulsesFwd_ptr = ctypes.pointer(ctypes.c_long)
    if plNumPulsesFwd is not None:
        plNumPulsesFwd_ptr.contents = plNumPulsesFwd
    pfStartPosRev_ptr = ctypes.pointer(ctypes.c_float)
    if pfStartPosRev is not None:
        pfStartPosRev_ptr.contents = pfStartPosRev
    pfPosIntervalRev_ptr = ctypes.pointer(ctypes.c_float)
    if pfPosIntervalRev is not None:
        pfPosIntervalRev_ptr.contents = pfPosIntervalRev
    plNumPulsesRev_ptr = ctypes.pointer(ctypes.c_long)
    if plNumPulsesRev is not None:
        plNumPulsesRev_ptr.contents = plNumPulsesRev
    pfPulseWidth_ptr = ctypes.pointer(ctypes.c_float)
    if pfPulseWidth is not None:
        pfPulseWidth_ptr.contents = pfPulseWidth
    plNumCycles_ptr = ctypes.pointer(ctypes.c_long)
    if plNumCycles is not None:
        plNumCycles_ptr.contents = plNumCycles
    return np.int64(thorlabs_apt.MOT_GetKCubePosTriggerParams(lSerialNum, ctypes.byref(pfStartPosFwd_ptr.contents), ctypes.byref(pfPosIntervalFwd_ptr.contents), ctypes.byref(plNumPulsesFwd_ptr.contents), ctypes.byref(pfStartPosRev_ptr.contents), ctypes.byref(pfPosIntervalRev_ptr.contents), ctypes.byref(plNumPulsesRev_ptr.contents), ctypes.byref(pfPulseWidth_ptr.contents), ctypes.byref(plNumCycles_ptr.contents))), np.int64(pfStartPosFwd_ptr.contents), np.int64(pfPosIntervalFwd_ptr.contents), np.int64(plNumPulsesFwd_ptr.contents), np.int64(pfStartPosRev_ptr.contents), np.int64(pfPosIntervalRev_ptr.contents), np.int64(plNumPulsesRev_ptr.contents), np.int64(pfPulseWidth_ptr.contents), np.int64(plNumCycles_ptr.contents)


def MOT_SetKCubeKSTLoopParams(lSerialNum: np.int64, lLoopMode: np.int64, lProp: np.int64, lInt: np.int64, lDiff: np.int64, lPIDClip: np.int64, lPIDTol: np.int64, lEncConst: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_SetKCubeKSTLoopParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lLoopMode = ctypes.c_long(lLoopMode)
    lProp = ctypes.c_long(lProp)
    lInt = ctypes.c_long(lInt)
    lDiff = ctypes.c_long(lDiff)
    lPIDClip = ctypes.c_long(lPIDClip)
    lPIDTol = ctypes.c_long(lPIDTol)
    lEncConst = ctypes.c_long(lEncConst)
    return np.int64(thorlabs_apt.MOT_SetKCubeKSTLoopParams(lSerialNum, lLoopMode, lProp, lInt, lDiff, lPIDClip, lPIDTol, lEncConst))


def MOT_GetKCubeKSTLoopParams(lSerialNum: np.int64, plLoopMode: np.int64 = None, plProp: np.int64 = None, plInt: np.int64 = None, plDiff: np.int64 = None, plPIDClip: np.int64 = None, lPIDTol: np.int64 = None, plEncConst: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetKCubeKSTLoopParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plLoopMode_ptr = ctypes.pointer(ctypes.c_long)
    if plLoopMode is not None:
        plLoopMode_ptr.contents = plLoopMode
    plProp_ptr = ctypes.pointer(ctypes.c_long)
    if plProp is not None:
        plProp_ptr.contents = plProp
    plInt_ptr = ctypes.pointer(ctypes.c_long)
    if plInt is not None:
        plInt_ptr.contents = plInt
    plDiff_ptr = ctypes.pointer(ctypes.c_long)
    if plDiff is not None:
        plDiff_ptr.contents = plDiff
    plPIDClip_ptr = ctypes.pointer(ctypes.c_long)
    if plPIDClip is not None:
        plPIDClip_ptr.contents = plPIDClip
    lPIDTol_ptr = ctypes.pointer(ctypes.c_long)
    if lPIDTol is not None:
        lPIDTol_ptr.contents = lPIDTol
    plEncConst_ptr = ctypes.pointer(ctypes.c_long)
    if plEncConst is not None:
        plEncConst_ptr.contents = plEncConst
    return np.int64(thorlabs_apt.MOT_GetKCubeKSTLoopParams(lSerialNum, ctypes.byref(plLoopMode_ptr.contents), ctypes.byref(plProp_ptr.contents), ctypes.byref(plInt_ptr.contents), ctypes.byref(plDiff_ptr.contents), ctypes.byref(plPIDClip_ptr.contents), ctypes.byref(lPIDTol_ptr.contents), ctypes.byref(plEncConst_ptr.contents))), np.int64(plLoopMode_ptr.contents), np.int64(plProp_ptr.contents), np.int64(plInt_ptr.contents), np.int64(plDiff_ptr.contents), np.int64(plPIDClip_ptr.contents), np.int64(lPIDTol_ptr.contents), np.int64(plEncConst_ptr.contents)


def MOT_GetInMotion(lSerialNum: np.int64, pbInMotionFlag: ctypes.c_void_p = None) -> ctypes.c_long:
    """Auto-generated wrapper for MOT_GetInMotion"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pbInMotionFlag_ptr = ctypes.pointer(ctypes.c_void_p)
    if pbInMotionFlag is not None:
        pbInMotionFlag_ptr.contents = pbInMotionFlag
    return np.int64(thorlabs_apt.MOT_GetInMotion(lSerialNum, ctypes.byref(pbInMotionFlag_ptr.contents))), np.int64(pbInMotionFlag_ptr.contents)


def MFF_Identify(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MFF_Identify"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.MFF_Identify(lSerialNum))


def MFF_EnableHWChannel(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MFF_EnableHWChannel"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.MFF_EnableHWChannel(lSerialNum))


def MFF_DisableHWChannel(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MFF_DisableHWChannel"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.MFF_DisableHWChannel(lSerialNum))


def MFF_MoveJog(lSerialNum: np.int64, lJogDir: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MFF_MoveJog"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lJogDir = ctypes.c_long(lJogDir)
    return np.int64(thorlabs_apt.MFF_MoveJog(lSerialNum, lJogDir))


def MFF_SetMFFOperParams(lSerialNum: np.int64, lTransitTime: np.int64, lDigIO1OperMode: np.int64, lDigIO1SigMode: np.int64, lDigIO1PulseWidth: np.int64, lDigIO2OperMode: np.int64, lDigIO2SigMode: np.int64, lDigIO2PulseWidth: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for MFF_SetMFFOperParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lTransitTime = ctypes.c_long(lTransitTime)
    lDigIO1OperMode = ctypes.c_long(lDigIO1OperMode)
    lDigIO1SigMode = ctypes.c_long(lDigIO1SigMode)
    lDigIO1PulseWidth = ctypes.c_long(lDigIO1PulseWidth)
    lDigIO2OperMode = ctypes.c_long(lDigIO2OperMode)
    lDigIO2SigMode = ctypes.c_long(lDigIO2SigMode)
    lDigIO2PulseWidth = ctypes.c_long(lDigIO2PulseWidth)
    return np.int64(thorlabs_apt.MFF_SetMFFOperParams(lSerialNum, lTransitTime, lDigIO1OperMode, lDigIO1SigMode, lDigIO1PulseWidth, lDigIO2OperMode, lDigIO2SigMode, lDigIO2PulseWidth))


def MFF_GetMFFOperParams(lSerialNum: np.int64, plTransitTime: np.int64 = None, plDigIO1OperMode: np.int64 = None, plDigIO1SigMode: np.int64 = None, plDigIO1PulseWidth: np.int64 = None, plDigIO2OperMode: np.int64 = None, plDigIO2SigMode: np.int64 = None, plDigIO2PulseWidth: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MFF_GetMFFOperParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plTransitTime_ptr = ctypes.pointer(ctypes.c_long)
    if plTransitTime is not None:
        plTransitTime_ptr.contents = plTransitTime
    plDigIO1OperMode_ptr = ctypes.pointer(ctypes.c_long)
    if plDigIO1OperMode is not None:
        plDigIO1OperMode_ptr.contents = plDigIO1OperMode
    plDigIO1SigMode_ptr = ctypes.pointer(ctypes.c_long)
    if plDigIO1SigMode is not None:
        plDigIO1SigMode_ptr.contents = plDigIO1SigMode
    plDigIO1PulseWidth_ptr = ctypes.pointer(ctypes.c_long)
    if plDigIO1PulseWidth is not None:
        plDigIO1PulseWidth_ptr.contents = plDigIO1PulseWidth
    plDigIO2OperMode_ptr = ctypes.pointer(ctypes.c_long)
    if plDigIO2OperMode is not None:
        plDigIO2OperMode_ptr.contents = plDigIO2OperMode
    plDigIO2SigMode_ptr = ctypes.pointer(ctypes.c_long)
    if plDigIO2SigMode is not None:
        plDigIO2SigMode_ptr.contents = plDigIO2SigMode
    plDigIO2PulseWidth_ptr = ctypes.pointer(ctypes.c_long)
    if plDigIO2PulseWidth is not None:
        plDigIO2PulseWidth_ptr.contents = plDigIO2PulseWidth
    return np.int64(thorlabs_apt.MFF_GetMFFOperParams(lSerialNum, ctypes.byref(plTransitTime_ptr.contents), ctypes.byref(plDigIO1OperMode_ptr.contents), ctypes.byref(plDigIO1SigMode_ptr.contents), ctypes.byref(plDigIO1PulseWidth_ptr.contents), ctypes.byref(plDigIO2OperMode_ptr.contents), ctypes.byref(plDigIO2SigMode_ptr.contents), ctypes.byref(plDigIO2PulseWidth_ptr.contents))), np.int64(plTransitTime_ptr.contents), np.int64(plDigIO1OperMode_ptr.contents), np.int64(plDigIO1SigMode_ptr.contents), np.int64(plDigIO1PulseWidth_ptr.contents), np.int64(plDigIO2OperMode_ptr.contents), np.int64(plDigIO2SigMode_ptr.contents), np.int64(plDigIO2PulseWidth_ptr.contents)


def MFF_GetStatusBits(lSerialNum: np.int64, plStatusBits: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for MFF_GetStatusBits"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plStatusBits_ptr = ctypes.pointer(ctypes.c_long)
    if plStatusBits is not None:
        plStatusBits_ptr.contents = plStatusBits
    return np.int64(thorlabs_apt.MFF_GetStatusBits(lSerialNum, ctypes.byref(plStatusBits_ptr.contents))), np.int64(plStatusBits_ptr.contents)


def SC_Identify(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for SC_Identify"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.SC_Identify(lSerialNum))


def SC_SetOperatingMode(lSerialNum: np.int64, lMode: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for SC_SetOperatingMode"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lMode = ctypes.c_long(lMode)
    return np.int64(thorlabs_apt.SC_SetOperatingMode(lSerialNum, lMode))


def SC_GetOperatingMode(lSerialNum: np.int64, plMode: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for SC_GetOperatingMode"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plMode_ptr = ctypes.pointer(ctypes.c_long)
    if plMode is not None:
        plMode_ptr.contents = plMode
    return np.int64(thorlabs_apt.SC_GetOperatingMode(lSerialNum, ctypes.byref(plMode_ptr.contents))), np.int64(plMode_ptr.contents)


def SC_SetCycleParams(lSerialNum: np.int64, fOnTime: np.float32, fOffTime: np.float32, lNumCycles: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for SC_SetCycleParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    fOnTime = ctypes.c_float(fOnTime)
    fOffTime = ctypes.c_float(fOffTime)
    lNumCycles = ctypes.c_long(lNumCycles)
    return np.int64(thorlabs_apt.SC_SetCycleParams(lSerialNum, fOnTime, fOffTime, lNumCycles))


def SC_GetCycleParams(lSerialNum: np.int64, pfOnTime: np.int64 = None, pfOffTime: np.int64 = None, plNumCycles: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for SC_GetCycleParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pfOnTime_ptr = ctypes.pointer(ctypes.c_float)
    if pfOnTime is not None:
        pfOnTime_ptr.contents = pfOnTime
    pfOffTime_ptr = ctypes.pointer(ctypes.c_float)
    if pfOffTime is not None:
        pfOffTime_ptr.contents = pfOffTime
    plNumCycles_ptr = ctypes.pointer(ctypes.c_long)
    if plNumCycles is not None:
        plNumCycles_ptr.contents = plNumCycles
    return np.int64(thorlabs_apt.SC_GetCycleParams(lSerialNum, ctypes.byref(pfOnTime_ptr.contents), ctypes.byref(pfOffTime_ptr.contents), ctypes.byref(plNumCycles_ptr.contents))), np.int64(pfOnTime_ptr.contents), np.int64(pfOffTime_ptr.contents), np.int64(plNumCycles_ptr.contents)


def SC_Enable(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for SC_Enable"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.SC_Enable(lSerialNum))


def SC_Disable(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for SC_Disable"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.SC_Disable(lSerialNum))


def SC_GetOPState(lSerialNum: np.int64, plState: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for SC_GetOPState"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plState_ptr = ctypes.pointer(ctypes.c_long)
    if plState is not None:
        plState_ptr.contents = plState
    return np.int64(thorlabs_apt.SC_GetOPState(lSerialNum, ctypes.byref(plState_ptr.contents))), np.int64(plState_ptr.contents)


def SC_GetStatusBits(lSerialNum: np.int64, plStatusBits: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for SC_GetStatusBits"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plStatusBits_ptr = ctypes.pointer(ctypes.c_long)
    if plStatusBits is not None:
        plStatusBits_ptr.contents = plStatusBits
    return np.int64(thorlabs_apt.SC_GetStatusBits(lSerialNum, ctypes.byref(plStatusBits_ptr.contents))), np.int64(plStatusBits_ptr.contents)


def PZMOT_ConnectMoveCompleteCallback(lSerialNum: np.int64, pFnMoveCallback: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_ConnectMoveCompleteCallback"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pFnMoveCallback = ctypes.c_void_p(pFnMoveCallback)
    return np.int64(thorlabs_apt.PZMOT_ConnectMoveCompleteCallback(lSerialNum, pFnMoveCallback))


def PZMOT_DisconnectMoveCompleteCallback(lSerialNum: np.int64, pFnMoveCallback: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_DisconnectMoveCompleteCallback"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pFnMoveCallback = ctypes.c_void_p(pFnMoveCallback)
    return np.int64(thorlabs_apt.PZMOT_DisconnectMoveCompleteCallback(lSerialNum, pFnMoveCallback))


def PZMOT_LLSetGetDigOPs(lSerialNum: np.int64, bSet: ctypes.c_void_p, plBits: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_LLSetGetDigOPs"""
    lSerialNum = ctypes.c_long(lSerialNum)
    bSet = ctypes.c_void_p(bSet)
    plBits_ptr = ctypes.pointer(ctypes.c_long)
    if plBits is not None:
        plBits_ptr.contents = plBits
    return np.int64(thorlabs_apt.PZMOT_LLSetGetDigOPs(lSerialNum, bSet, ctypes.byref(plBits_ptr.contents))), np.int64(plBits_ptr.contents)


def PZMOT_SetChannel(lSerialNum: np.int64, lChanID: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetChannel"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lChanID = ctypes.c_long(lChanID)
    return np.int64(thorlabs_apt.PZMOT_SetChannel(lSerialNum, lChanID))


def PZMOT_Identify(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_Identify"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.PZMOT_Identify(lSerialNum))


def PZMOT_EnableHWChannel(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_EnableHWChannel"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.PZMOT_EnableHWChannel(lSerialNum))


def PZMOT_SetDriveOPParams(lSerialNum: np.int64, lVoltage: np.int64, lStepRate: np.int64, lStepAccn: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetDriveOPParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lVoltage = ctypes.c_long(lVoltage)
    lStepRate = ctypes.c_long(lStepRate)
    lStepAccn = ctypes.c_long(lStepAccn)
    return np.int64(thorlabs_apt.PZMOT_SetDriveOPParams(lSerialNum, lVoltage, lStepRate, lStepAccn))


def PZMOT_GetDriveOPParams(lSerialNum: np.int64, plVoltage: np.int64 = None, plStepRate: np.int64 = None, plStepAccn: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetDriveOPParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plVoltage_ptr = ctypes.pointer(ctypes.c_long)
    if plVoltage is not None:
        plVoltage_ptr.contents = plVoltage
    plStepRate_ptr = ctypes.pointer(ctypes.c_long)
    if plStepRate is not None:
        plStepRate_ptr.contents = plStepRate
    plStepAccn_ptr = ctypes.pointer(ctypes.c_long)
    if plStepAccn is not None:
        plStepAccn_ptr.contents = plStepAccn
    return np.int64(thorlabs_apt.PZMOT_GetDriveOPParams(lSerialNum, ctypes.byref(plVoltage_ptr.contents), ctypes.byref(plStepRate_ptr.contents), ctypes.byref(plStepAccn_ptr.contents))), np.int64(plVoltage_ptr.contents), np.int64(plStepRate_ptr.contents), np.int64(plStepAccn_ptr.contents)


def PZMOT_SetJogMode(lSerialNum: np.int64, lMode: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetJogMode"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lMode = ctypes.c_long(lMode)
    return np.int64(thorlabs_apt.PZMOT_SetJogMode(lSerialNum, lMode))


def PZMOT_GetJogMode(lSerialNum: np.int64, plMode: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetJogMode"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plMode_ptr = ctypes.pointer(ctypes.c_long)
    if plMode is not None:
        plMode_ptr.contents = plMode
    return np.int64(thorlabs_apt.PZMOT_GetJogMode(lSerialNum, ctypes.byref(plMode_ptr.contents))), np.int64(plMode_ptr.contents)


def PZMOT_SetJogStepSize(lSerialNum: np.int64, lJogSteps: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetJogStepSize"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lJogSteps = ctypes.c_long(lJogSteps)
    return np.int64(thorlabs_apt.PZMOT_SetJogStepSize(lSerialNum, lJogSteps))


def PZMOT_GetJogStepSize(lSerialNum: np.int64, plJogSteps: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetJogStepSize"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plJogSteps_ptr = ctypes.pointer(ctypes.c_long)
    if plJogSteps is not None:
        plJogSteps_ptr.contents = plJogSteps
    return np.int64(thorlabs_apt.PZMOT_GetJogStepSize(lSerialNum, ctypes.byref(plJogSteps_ptr.contents))), np.int64(plJogSteps_ptr.contents)


def PZMOT_SetJogOPParams(lSerialNum: np.int64, lStepRate: np.int64, lStepAccn: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetJogOPParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lStepRate = ctypes.c_long(lStepRate)
    lStepAccn = ctypes.c_long(lStepAccn)
    return np.int64(thorlabs_apt.PZMOT_SetJogOPParams(lSerialNum, lStepRate, lStepAccn))


def PZMOT_GetJogOPParams(lSerialNum: np.int64, plStepRate: np.int64 = None, plStepAccn: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetJogOPParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plStepRate_ptr = ctypes.pointer(ctypes.c_long)
    if plStepRate is not None:
        plStepRate_ptr.contents = plStepRate
    plStepAccn_ptr = ctypes.pointer(ctypes.c_long)
    if plStepAccn is not None:
        plStepAccn_ptr.contents = plStepAccn
    return np.int64(thorlabs_apt.PZMOT_GetJogOPParams(lSerialNum, ctypes.byref(plStepRate_ptr.contents), ctypes.byref(plStepAccn_ptr.contents))), np.int64(plStepRate_ptr.contents), np.int64(plStepAccn_ptr.contents)


def PZMOT_SetPositionSteps(lSerialNum: np.int64, lPosSteps: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetPositionSteps"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lPosSteps = ctypes.c_long(lPosSteps)
    return np.int64(thorlabs_apt.PZMOT_SetPositionSteps(lSerialNum, lPosSteps))


def PZMOT_GetPositionSteps(lSerialNum: np.int64, plPosSteps: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetPositionSteps"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plPosSteps_ptr = ctypes.pointer(ctypes.c_long)
    if plPosSteps is not None:
        plPosSteps_ptr.contents = plPosSteps
    return np.int64(thorlabs_apt.PZMOT_GetPositionSteps(lSerialNum, ctypes.byref(plPosSteps_ptr.contents))), np.int64(plPosSteps_ptr.contents)


def PZMOT_SetButtonParams(lSerialNum: np.int64, lButMode: np.int64, lButPos1: np.int64, lButPos2: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetButtonParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lButMode = ctypes.c_long(lButMode)
    lButPos1 = ctypes.c_long(lButPos1)
    lButPos2 = ctypes.c_long(lButPos2)
    return np.int64(thorlabs_apt.PZMOT_SetButtonParams(lSerialNum, lButMode, lButPos1, lButPos2))


def PZMOT_GetButtonParams(lSerialNum: np.int64, plButMode: np.int64 = None, plButPos1: np.int64 = None, plButPos2: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetButtonParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plButMode_ptr = ctypes.pointer(ctypes.c_long)
    if plButMode is not None:
        plButMode_ptr.contents = plButMode
    plButPos1_ptr = ctypes.pointer(ctypes.c_long)
    if plButPos1 is not None:
        plButPos1_ptr.contents = plButPos1
    plButPos2_ptr = ctypes.pointer(ctypes.c_long)
    if plButPos2 is not None:
        plButPos2_ptr.contents = plButPos2
    return np.int64(thorlabs_apt.PZMOT_GetButtonParams(lSerialNum, ctypes.byref(plButMode_ptr.contents), ctypes.byref(plButPos1_ptr.contents), ctypes.byref(plButPos2_ptr.contents))), np.int64(plButMode_ptr.contents), np.int64(plButPos1_ptr.contents), np.int64(plButPos2_ptr.contents)


def PZMOT_SetPotParams(lSerialNum: np.int64, lMaxStepRate: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetPotParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lMaxStepRate = ctypes.c_long(lMaxStepRate)
    return np.int64(thorlabs_apt.PZMOT_SetPotParams(lSerialNum, lMaxStepRate))


def PZMOT_GetPotParams(lSerialNum: np.int64, plMaxStepRate: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetPotParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plMaxStepRate_ptr = ctypes.pointer(ctypes.c_long)
    if plMaxStepRate is not None:
        plMaxStepRate_ptr.contents = plMaxStepRate
    return np.int64(thorlabs_apt.PZMOT_GetPotParams(lSerialNum, ctypes.byref(plMaxStepRate_ptr.contents))), np.int64(plMaxStepRate_ptr.contents)


def PZMOT_SetKCubePanelParams(lSerialNum: np.int64, lJSMode: np.int64, lJSMaxStepRate: np.int64, lJSDirSense: np.int64, lPresetPos1: np.int64, lPresetPos2: np.int64, lDispBrightness: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetKCubePanelParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lJSMode = ctypes.c_long(lJSMode)
    lJSMaxStepRate = ctypes.c_long(lJSMaxStepRate)
    lJSDirSense = ctypes.c_long(lJSDirSense)
    lPresetPos1 = ctypes.c_long(lPresetPos1)
    lPresetPos2 = ctypes.c_long(lPresetPos2)
    lDispBrightness = ctypes.c_long(lDispBrightness)
    return np.int64(thorlabs_apt.PZMOT_SetKCubePanelParams(lSerialNum, lJSMode, lJSMaxStepRate, lJSDirSense, lPresetPos1, lPresetPos2, lDispBrightness))


def PZMOT_GetKCubePanelParams(lSerialNum: np.int64, plJSMode: np.int64 = None, plJSMaxStepRate: np.int64 = None, plJSDirSense: np.int64 = None, plPresetPos1: np.int64 = None, plPresetPos2: np.int64 = None, plDispBrightness: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetKCubePanelParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plJSMode_ptr = ctypes.pointer(ctypes.c_long)
    if plJSMode is not None:
        plJSMode_ptr.contents = plJSMode
    plJSMaxStepRate_ptr = ctypes.pointer(ctypes.c_long)
    if plJSMaxStepRate is not None:
        plJSMaxStepRate_ptr.contents = plJSMaxStepRate
    plJSDirSense_ptr = ctypes.pointer(ctypes.c_long)
    if plJSDirSense is not None:
        plJSDirSense_ptr.contents = plJSDirSense
    plPresetPos1_ptr = ctypes.pointer(ctypes.c_long)
    if plPresetPos1 is not None:
        plPresetPos1_ptr.contents = plPresetPos1
    plPresetPos2_ptr = ctypes.pointer(ctypes.c_long)
    if plPresetPos2 is not None:
        plPresetPos2_ptr.contents = plPresetPos2
    plDispBrightness_ptr = ctypes.pointer(ctypes.c_long)
    if plDispBrightness is not None:
        plDispBrightness_ptr.contents = plDispBrightness
    return np.int64(thorlabs_apt.PZMOT_GetKCubePanelParams(lSerialNum, ctypes.byref(plJSMode_ptr.contents), ctypes.byref(plJSMaxStepRate_ptr.contents), ctypes.byref(plJSDirSense_ptr.contents), ctypes.byref(plPresetPos1_ptr.contents), ctypes.byref(plPresetPos2_ptr.contents), ctypes.byref(plDispBrightness_ptr.contents))), np.int64(plJSMode_ptr.contents), np.int64(plJSMaxStepRate_ptr.contents), np.int64(plJSDirSense_ptr.contents), np.int64(plPresetPos1_ptr.contents), np.int64(plPresetPos2_ptr.contents), np.int64(plDispBrightness_ptr.contents)


def PZMOT_SetKCubeTriggerParams(lSerialNum: np.int64, lTrigChan1: np.int64, lTrigChan2: np.int64, lTrig1Mode: np.int64, lTrig1Polarity: np.int64, lTrig2Mode: np.int64, lTrig2Polarity: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetKCubeTriggerParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lTrigChan1 = ctypes.c_long(lTrigChan1)
    lTrigChan2 = ctypes.c_long(lTrigChan2)
    lTrig1Mode = ctypes.c_long(lTrig1Mode)
    lTrig1Polarity = ctypes.c_long(lTrig1Polarity)
    lTrig2Mode = ctypes.c_long(lTrig2Mode)
    lTrig2Polarity = ctypes.c_long(lTrig2Polarity)
    return np.int64(thorlabs_apt.PZMOT_SetKCubeTriggerParams(lSerialNum, lTrigChan1, lTrigChan2, lTrig1Mode, lTrig1Polarity, lTrig2Mode, lTrig2Polarity))


def PZMOT_GetKCubeTriggerParams(lSerialNum: np.int64, plTrigChan1: np.int64 = None, plTrigChan2: np.int64 = None, plTrig1Mode: np.int64 = None, plTrig1Polarity: np.int64 = None, plTrig2Mode: np.int64 = None, plTrig2Polarity: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetKCubeTriggerParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plTrigChan1_ptr = ctypes.pointer(ctypes.c_long)
    if plTrigChan1 is not None:
        plTrigChan1_ptr.contents = plTrigChan1
    plTrigChan2_ptr = ctypes.pointer(ctypes.c_long)
    if plTrigChan2 is not None:
        plTrigChan2_ptr.contents = plTrigChan2
    plTrig1Mode_ptr = ctypes.pointer(ctypes.c_long)
    if plTrig1Mode is not None:
        plTrig1Mode_ptr.contents = plTrig1Mode
    plTrig1Polarity_ptr = ctypes.pointer(ctypes.c_long)
    if plTrig1Polarity is not None:
        plTrig1Polarity_ptr.contents = plTrig1Polarity
    plTrig2Mode_ptr = ctypes.pointer(ctypes.c_long)
    if plTrig2Mode is not None:
        plTrig2Mode_ptr.contents = plTrig2Mode
    plTrig2Polarity_ptr = ctypes.pointer(ctypes.c_long)
    if plTrig2Polarity is not None:
        plTrig2Polarity_ptr.contents = plTrig2Polarity
    return np.int64(thorlabs_apt.PZMOT_GetKCubeTriggerParams(lSerialNum, ctypes.byref(plTrigChan1_ptr.contents), ctypes.byref(plTrigChan2_ptr.contents), ctypes.byref(plTrig1Mode_ptr.contents), ctypes.byref(plTrig1Polarity_ptr.contents), ctypes.byref(plTrig2Mode_ptr.contents), ctypes.byref(plTrig2Polarity_ptr.contents))), np.int64(plTrigChan1_ptr.contents), np.int64(plTrigChan2_ptr.contents), np.int64(plTrig1Mode_ptr.contents), np.int64(plTrig1Polarity_ptr.contents), np.int64(plTrig2Mode_ptr.contents), np.int64(plTrig2Polarity_ptr.contents)


def PZMOT_SetKCubePosTriggerParams(lSerialNum: np.int64, lStartPosFwd: np.int64, lPosIntervalFwd: np.int64, lNumPulsesFwd: np.int64, lStartPosRev: np.int64, lPosIntervalRev: np.int64, lNumPulsesRev: np.int64, lPulseWidth: np.int64, lNumCycles: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetKCubePosTriggerParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lStartPosFwd = ctypes.c_long(lStartPosFwd)
    lPosIntervalFwd = ctypes.c_long(lPosIntervalFwd)
    lNumPulsesFwd = ctypes.c_long(lNumPulsesFwd)
    lStartPosRev = ctypes.c_long(lStartPosRev)
    lPosIntervalRev = ctypes.c_long(lPosIntervalRev)
    lNumPulsesRev = ctypes.c_long(lNumPulsesRev)
    lPulseWidth = ctypes.c_long(lPulseWidth)
    lNumCycles = ctypes.c_long(lNumCycles)
    return np.int64(thorlabs_apt.PZMOT_SetKCubePosTriggerParams(lSerialNum, lStartPosFwd, lPosIntervalFwd, lNumPulsesFwd, lStartPosRev, lPosIntervalRev, lNumPulsesRev, lPulseWidth, lNumCycles))


def PZMOT_GetKCubePosTriggerParams(lSerialNum: np.int64, plStartPosFwd: np.int64 = None, plPosIntervalFwd: np.int64 = None, plNumPulsesFwd: np.int64 = None, plStartPosRev: np.int64 = None, plPosIntervalRev: np.int64 = None, plNumPulsesRev: np.int64 = None, plPulseWidth: np.int64 = None, plNumCycles: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetKCubePosTriggerParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plStartPosFwd_ptr = ctypes.pointer(ctypes.c_long)
    if plStartPosFwd is not None:
        plStartPosFwd_ptr.contents = plStartPosFwd
    plPosIntervalFwd_ptr = ctypes.pointer(ctypes.c_long)
    if plPosIntervalFwd is not None:
        plPosIntervalFwd_ptr.contents = plPosIntervalFwd
    plNumPulsesFwd_ptr = ctypes.pointer(ctypes.c_long)
    if plNumPulsesFwd is not None:
        plNumPulsesFwd_ptr.contents = plNumPulsesFwd
    plStartPosRev_ptr = ctypes.pointer(ctypes.c_long)
    if plStartPosRev is not None:
        plStartPosRev_ptr.contents = plStartPosRev
    plPosIntervalRev_ptr = ctypes.pointer(ctypes.c_long)
    if plPosIntervalRev is not None:
        plPosIntervalRev_ptr.contents = plPosIntervalRev
    plNumPulsesRev_ptr = ctypes.pointer(ctypes.c_long)
    if plNumPulsesRev is not None:
        plNumPulsesRev_ptr.contents = plNumPulsesRev
    plPulseWidth_ptr = ctypes.pointer(ctypes.c_long)
    if plPulseWidth is not None:
        plPulseWidth_ptr.contents = plPulseWidth
    plNumCycles_ptr = ctypes.pointer(ctypes.c_long)
    if plNumCycles is not None:
        plNumCycles_ptr.contents = plNumCycles
    return np.int64(thorlabs_apt.PZMOT_GetKCubePosTriggerParams(lSerialNum, ctypes.byref(plStartPosFwd_ptr.contents), ctypes.byref(plPosIntervalFwd_ptr.contents), ctypes.byref(plNumPulsesFwd_ptr.contents), ctypes.byref(plStartPosRev_ptr.contents), ctypes.byref(plPosIntervalRev_ptr.contents), ctypes.byref(plNumPulsesRev_ptr.contents), ctypes.byref(plPulseWidth_ptr.contents), ctypes.byref(plNumCycles_ptr.contents))), np.int64(plStartPosFwd_ptr.contents), np.int64(plPosIntervalFwd_ptr.contents), np.int64(plNumPulsesFwd_ptr.contents), np.int64(plStartPosRev_ptr.contents), np.int64(plPosIntervalRev_ptr.contents), np.int64(plNumPulsesRev_ptr.contents), np.int64(plPulseWidth_ptr.contents), np.int64(plNumCycles_ptr.contents)


def PZMOT_SetKCubeChanEnableMode(lSerialNum: np.int64, lMode: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetKCubeChanEnableMode"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lMode = ctypes.c_long(lMode)
    return np.int64(thorlabs_apt.PZMOT_SetKCubeChanEnableMode(lSerialNum, lMode))


def PZMOT_GetKCubeChanEnableMode(lSerialNum: np.int64, plMode: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetKCubeChanEnableMode"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plMode_ptr = ctypes.pointer(ctypes.c_long)
    if plMode is not None:
        plMode_ptr.contents = plMode
    return np.int64(thorlabs_apt.PZMOT_GetKCubeChanEnableMode(lSerialNum, ctypes.byref(plMode_ptr.contents))), np.int64(plMode_ptr.contents)


def PZMOT_SetKCubeJogParams(lSerialNum: np.int64, lJogMode: np.int64, lJogStepSizeFwd: np.int64, lJogStepSizeRev: np.int64, lJogStepRate: np.int64, lJogStepAccn: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetKCubeJogParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lJogMode = ctypes.c_long(lJogMode)
    lJogStepSizeFwd = ctypes.c_long(lJogStepSizeFwd)
    lJogStepSizeRev = ctypes.c_long(lJogStepSizeRev)
    lJogStepRate = ctypes.c_long(lJogStepRate)
    lJogStepAccn = ctypes.c_long(lJogStepAccn)
    return np.int64(thorlabs_apt.PZMOT_SetKCubeJogParams(lSerialNum, lJogMode, lJogStepSizeFwd, lJogStepSizeRev, lJogStepRate, lJogStepAccn))


def PZMOT_GetKCubeJogParams(lSerialNum: np.int64, plJogMode: np.int64 = None, plJogStepSizeFwd: np.int64 = None, plJogStepSizeRev: np.int64 = None, plJogStepRate: np.int64 = None, plJogStepAccn: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetKCubeJogParams"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plJogMode_ptr = ctypes.pointer(ctypes.c_long)
    if plJogMode is not None:
        plJogMode_ptr.contents = plJogMode
    plJogStepSizeFwd_ptr = ctypes.pointer(ctypes.c_long)
    if plJogStepSizeFwd is not None:
        plJogStepSizeFwd_ptr.contents = plJogStepSizeFwd
    plJogStepSizeRev_ptr = ctypes.pointer(ctypes.c_long)
    if plJogStepSizeRev is not None:
        plJogStepSizeRev_ptr.contents = plJogStepSizeRev
    plJogStepRate_ptr = ctypes.pointer(ctypes.c_long)
    if plJogStepRate is not None:
        plJogStepRate_ptr.contents = plJogStepRate
    plJogStepAccn_ptr = ctypes.pointer(ctypes.c_long)
    if plJogStepAccn is not None:
        plJogStepAccn_ptr.contents = plJogStepAccn
    return np.int64(thorlabs_apt.PZMOT_GetKCubeJogParams(lSerialNum, ctypes.byref(plJogMode_ptr.contents), ctypes.byref(plJogStepSizeFwd_ptr.contents), ctypes.byref(plJogStepSizeRev_ptr.contents), ctypes.byref(plJogStepRate_ptr.contents), ctypes.byref(plJogStepAccn_ptr.contents))), np.int64(plJogMode_ptr.contents), np.int64(plJogStepSizeFwd_ptr.contents), np.int64(plJogStepSizeRev_ptr.contents), np.int64(plJogStepRate_ptr.contents), np.int64(plJogStepAccn_ptr.contents)


def PZMOT_SetKCubeFeedbackSig(lSerialNum: np.int64, lFBMode: np.int64, lEncoderConst: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_SetKCubeFeedbackSig"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lFBMode = ctypes.c_long(lFBMode)
    lEncoderConst = ctypes.c_long(lEncoderConst)
    return np.int64(thorlabs_apt.PZMOT_SetKCubeFeedbackSig(lSerialNum, lFBMode, lEncoderConst))


def PZMOT_GetKCubeFeedbackSig(lSerialNum: np.int64, plFBMode: np.int64 = None, plEncoderConst: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetKCubeFeedbackSig"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plFBMode_ptr = ctypes.pointer(ctypes.c_long)
    if plFBMode is not None:
        plFBMode_ptr.contents = plFBMode
    plEncoderConst_ptr = ctypes.pointer(ctypes.c_long)
    if plEncoderConst is not None:
        plEncoderConst_ptr.contents = plEncoderConst
    return np.int64(thorlabs_apt.PZMOT_GetKCubeFeedbackSig(lSerialNum, ctypes.byref(plFBMode_ptr.contents), ctypes.byref(plEncoderConst_ptr.contents))), np.int64(plFBMode_ptr.contents), np.int64(plEncoderConst_ptr.contents)


def PZMOT_GetStatusBits(lSerialNum: np.int64, plStatusBits: np.int64 = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetStatusBits"""
    lSerialNum = ctypes.c_long(lSerialNum)
    plStatusBits_ptr = ctypes.pointer(ctypes.c_long)
    if plStatusBits is not None:
        plStatusBits_ptr.contents = plStatusBits
    return np.int64(thorlabs_apt.PZMOT_GetStatusBits(lSerialNum, ctypes.byref(plStatusBits_ptr.contents))), np.int64(plStatusBits_ptr.contents)


def PZMOT_MoveHome(lSerialNum: np.int64, bWait: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_MoveHome"""
    lSerialNum = ctypes.c_long(lSerialNum)
    bWait = ctypes.c_void_p(bWait)
    return np.int64(thorlabs_apt.PZMOT_MoveHome(lSerialNum, bWait))


def PZMOT_MoveRelativeStepsEx(lSerialNum: np.int64, lRelSteps: np.int64, bWait: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_MoveRelativeStepsEx"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lRelSteps = ctypes.c_long(lRelSteps)
    bWait = ctypes.c_void_p(bWait)
    return np.int64(thorlabs_apt.PZMOT_MoveRelativeStepsEx(lSerialNum, lRelSteps, bWait))


def PZMOT_MoveAbsoluteStepsEx(lSerialNum: np.int64, lAbsSteps: np.int64, bWait: ctypes.c_void_p) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_MoveAbsoluteStepsEx"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lAbsSteps = ctypes.c_long(lAbsSteps)
    bWait = ctypes.c_void_p(bWait)
    return np.int64(thorlabs_apt.PZMOT_MoveAbsoluteStepsEx(lSerialNum, lAbsSteps, bWait))


def PZMOT_MoveVelocity(lSerialNum: np.int64, lDirection: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_MoveVelocity"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lDirection = ctypes.c_long(lDirection)
    return np.int64(thorlabs_apt.PZMOT_MoveVelocity(lSerialNum, lDirection))


def PZMOT_Stop(lSerialNum: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_Stop"""
    lSerialNum = ctypes.c_long(lSerialNum)
    return np.int64(thorlabs_apt.PZMOT_Stop(lSerialNum))


def PZMOT_MoveJog(lSerialNum: np.int64, lJogDir: np.int64) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_MoveJog"""
    lSerialNum = ctypes.c_long(lSerialNum)
    lJogDir = ctypes.c_long(lJogDir)
    return np.int64(thorlabs_apt.PZMOT_MoveJog(lSerialNum, lJogDir))


def PZMOT_GetInMotion(lSerialNum: np.int64, pbInMotionFlag: ctypes.c_void_p = None) -> ctypes.c_long:
    """Auto-generated wrapper for PZMOT_GetInMotion"""
    lSerialNum = ctypes.c_long(lSerialNum)
    pbInMotionFlag_ptr = ctypes.pointer(ctypes.c_void_p)
    if pbInMotionFlag is not None:
        pbInMotionFlag_ptr.contents = pbInMotionFlag
    return np.int64(thorlabs_apt.PZMOT_GetInMotion(lSerialNum, ctypes.byref(pbInMotionFlag_ptr.contents))), np.int64(pbInMotionFlag_ptr.contents)
