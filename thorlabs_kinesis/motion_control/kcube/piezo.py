# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _piezo
else:
    import _piezo

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


FT_OK = _piezo.FT_OK
FT_InvalidHandle = _piezo.FT_InvalidHandle
FT_DeviceNotFound = _piezo.FT_DeviceNotFound
FT_DeviceNotOpened = _piezo.FT_DeviceNotOpened
FT_IOError = _piezo.FT_IOError
FT_InsufficientResources = _piezo.FT_InsufficientResources
FT_InvalidParameter = _piezo.FT_InvalidParameter
FT_DeviceNotPresent = _piezo.FT_DeviceNotPresent
FT_IncorrectDevice = _piezo.FT_IncorrectDevice
MOT_NotMotor = _piezo.MOT_NotMotor
MOT_DCMotor = _piezo.MOT_DCMotor
MOT_StepperMotor = _piezo.MOT_StepperMotor
MOT_BrushlessMotor = _piezo.MOT_BrushlessMotor
MOT_CustomMotor = _piezo.MOT_CustomMotor
KPZ_WM_Positive = _piezo.KPZ_WM_Positive
KPZ_WM_Negative = _piezo.KPZ_WM_Negative
KPZ_WM_MoveAtVoltage = _piezo.KPZ_WM_MoveAtVoltage
KPZ_WM_JogVoltage = _piezo.KPZ_WM_JogVoltage
KPZ_WM_SetVoltage = _piezo.KPZ_WM_SetVoltage
KPZ_WM_High = _piezo.KPZ_WM_High
KPZ_WM_Medium = _piezo.KPZ_WM_Medium
KPZ_WM_Low = _piezo.KPZ_WM_Low
KPZ_TrigDisabled = _piezo.KPZ_TrigDisabled
KPZ_TrigIn_GPI = _piezo.KPZ_TrigIn_GPI
KPZ_TrigIn_VoltageStepUp = _piezo.KPZ_TrigIn_VoltageStepUp
KPZ_TrigIn_VoltageStepDown = _piezo.KPZ_TrigIn_VoltageStepDown
KPZ_TrigOut_GPO = _piezo.KPZ_TrigOut_GPO
KPZ_TrigPolarityHigh = _piezo.KPZ_TrigPolarityHigh
KPZ_TrigPolarityLow = _piezo.KPZ_TrigPolarityLow
class TLI_DeviceInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    typeID = property(_piezo.TLI_DeviceInfo_typeID_get, _piezo.TLI_DeviceInfo_typeID_set)
    description = property(_piezo.TLI_DeviceInfo_description_get, _piezo.TLI_DeviceInfo_description_set)
    serialNo = property(_piezo.TLI_DeviceInfo_serialNo_get, _piezo.TLI_DeviceInfo_serialNo_set)
    PID = property(_piezo.TLI_DeviceInfo_PID_get, _piezo.TLI_DeviceInfo_PID_set)
    isKnownType = property(_piezo.TLI_DeviceInfo_isKnownType_get, _piezo.TLI_DeviceInfo_isKnownType_set)
    motorType = property(_piezo.TLI_DeviceInfo_motorType_get, _piezo.TLI_DeviceInfo_motorType_set)
    isPiezoDevice = property(_piezo.TLI_DeviceInfo_isPiezoDevice_get, _piezo.TLI_DeviceInfo_isPiezoDevice_set)
    isLaser = property(_piezo.TLI_DeviceInfo_isLaser_get, _piezo.TLI_DeviceInfo_isLaser_set)
    isCustomType = property(_piezo.TLI_DeviceInfo_isCustomType_get, _piezo.TLI_DeviceInfo_isCustomType_set)
    isRack = property(_piezo.TLI_DeviceInfo_isRack_get, _piezo.TLI_DeviceInfo_isRack_set)
    maxChannels = property(_piezo.TLI_DeviceInfo_maxChannels_get, _piezo.TLI_DeviceInfo_maxChannels_set)

    def __init__(self):
        _piezo.TLI_DeviceInfo_swiginit(self, _piezo.new_TLI_DeviceInfo())
    __swig_destroy__ = _piezo.delete_TLI_DeviceInfo

# Register TLI_DeviceInfo in _piezo:
_piezo.TLI_DeviceInfo_swigregister(TLI_DeviceInfo)
class TLI_HardwareInformation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    serialNumber = property(_piezo.TLI_HardwareInformation_serialNumber_get, _piezo.TLI_HardwareInformation_serialNumber_set)
    modelNumber = property(_piezo.TLI_HardwareInformation_modelNumber_get, _piezo.TLI_HardwareInformation_modelNumber_set)
    type = property(_piezo.TLI_HardwareInformation_type_get, _piezo.TLI_HardwareInformation_type_set)
    firmwareVersion = property(_piezo.TLI_HardwareInformation_firmwareVersion_get, _piezo.TLI_HardwareInformation_firmwareVersion_set)
    notes = property(_piezo.TLI_HardwareInformation_notes_get, _piezo.TLI_HardwareInformation_notes_set)
    deviceDependantData = property(_piezo.TLI_HardwareInformation_deviceDependantData_get, _piezo.TLI_HardwareInformation_deviceDependantData_set)
    hardwareVersion = property(_piezo.TLI_HardwareInformation_hardwareVersion_get, _piezo.TLI_HardwareInformation_hardwareVersion_set)
    modificationState = property(_piezo.TLI_HardwareInformation_modificationState_get, _piezo.TLI_HardwareInformation_modificationState_set)
    numChannels = property(_piezo.TLI_HardwareInformation_numChannels_get, _piezo.TLI_HardwareInformation_numChannels_set)

    def __init__(self):
        _piezo.TLI_HardwareInformation_swiginit(self, _piezo.new_TLI_HardwareInformation())
    __swig_destroy__ = _piezo.delete_TLI_HardwareInformation

# Register TLI_HardwareInformation in _piezo:
_piezo.TLI_HardwareInformation_swigregister(TLI_HardwareInformation)
PZ_ControlModeUndefined = _piezo.PZ_ControlModeUndefined
PZ_OpenLoop = _piezo.PZ_OpenLoop
PZ_CloseLoop = _piezo.PZ_CloseLoop
PZ_OpenLoopSmooth = _piezo.PZ_OpenLoopSmooth
PZ_CloseLoopSmooth = _piezo.PZ_CloseLoopSmooth
PZ_SoftwareOnly = _piezo.PZ_SoftwareOnly
PZ_ExternalSignal = _piezo.PZ_ExternalSignal
PZ_Potentiometer = _piezo.PZ_Potentiometer
PZ_All = _piezo.PZ_All
PZ_Continuous = _piezo.PZ_Continuous
PZ_Fixed = _piezo.PZ_Fixed
PZ_OutputTrigEnable = _piezo.PZ_OutputTrigEnable
PZ_InputTrigEnable = _piezo.PZ_InputTrigEnable
PZ_OutputTrigSenseHigh = _piezo.PZ_OutputTrigSenseHigh
PZ_InputTrigSenseHigh = _piezo.PZ_InputTrigSenseHigh
PZ_OutputGated = _piezo.PZ_OutputGated
PZ_OutputTrigRepeat = _piezo.PZ_OutputTrigRepeat
AnalogueCh1 = _piezo.AnalogueCh1
AnalogueCh2 = _piezo.AnalogueCh2
ExtSignalSMA = _piezo.ExtSignalSMA
class TPZ_IOSettings(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    _hubAnalogueInput = property(_piezo.TPZ_IOSettings__hubAnalogueInput_get, _piezo.TPZ_IOSettings__hubAnalogueInput_set)
    _maximumOutputVoltage = property(_piezo.TPZ_IOSettings__maximumOutputVoltage_get, _piezo.TPZ_IOSettings__maximumOutputVoltage_set)

    def __init__(self):
        _piezo.TPZ_IOSettings_swiginit(self, _piezo.new_TPZ_IOSettings())
    __swig_destroy__ = _piezo.delete_TPZ_IOSettings

# Register TPZ_IOSettings in _piezo:
_piezo.TPZ_IOSettings_swigregister(TPZ_IOSettings)
class PZ_FeedbackLoopConstants(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    proportionalTerm = property(_piezo.PZ_FeedbackLoopConstants_proportionalTerm_get, _piezo.PZ_FeedbackLoopConstants_proportionalTerm_set)
    integralTerm = property(_piezo.PZ_FeedbackLoopConstants_integralTerm_get, _piezo.PZ_FeedbackLoopConstants_integralTerm_set)

    def __init__(self):
        _piezo.PZ_FeedbackLoopConstants_swiginit(self, _piezo.new_PZ_FeedbackLoopConstants())
    __swig_destroy__ = _piezo.delete_PZ_FeedbackLoopConstants

# Register PZ_FeedbackLoopConstants in _piezo:
_piezo.PZ_FeedbackLoopConstants_swigregister(PZ_FeedbackLoopConstants)
class PZ_LUTWaveParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    mode = property(_piezo.PZ_LUTWaveParameters_mode_get, _piezo.PZ_LUTWaveParameters_mode_set)
    cycleLength = property(_piezo.PZ_LUTWaveParameters_cycleLength_get, _piezo.PZ_LUTWaveParameters_cycleLength_set)
    numCycles = property(_piezo.PZ_LUTWaveParameters_numCycles_get, _piezo.PZ_LUTWaveParameters_numCycles_set)
    LUTValueDelay = property(_piezo.PZ_LUTWaveParameters_LUTValueDelay_get, _piezo.PZ_LUTWaveParameters_LUTValueDelay_set)
    preCycleDelay = property(_piezo.PZ_LUTWaveParameters_preCycleDelay_get, _piezo.PZ_LUTWaveParameters_preCycleDelay_set)
    postCycleDelay = property(_piezo.PZ_LUTWaveParameters_postCycleDelay_get, _piezo.PZ_LUTWaveParameters_postCycleDelay_set)
    outTriggerStart = property(_piezo.PZ_LUTWaveParameters_outTriggerStart_get, _piezo.PZ_LUTWaveParameters_outTriggerStart_set)
    outTriggerDuration = property(_piezo.PZ_LUTWaveParameters_outTriggerDuration_get, _piezo.PZ_LUTWaveParameters_outTriggerDuration_set)
    numOutTriggerRepeat = property(_piezo.PZ_LUTWaveParameters_numOutTriggerRepeat_get, _piezo.PZ_LUTWaveParameters_numOutTriggerRepeat_set)

    def __init__(self):
        _piezo.PZ_LUTWaveParameters_swiginit(self, _piezo.new_PZ_LUTWaveParameters())
    __swig_destroy__ = _piezo.delete_PZ_LUTWaveParameters

# Register PZ_LUTWaveParameters in _piezo:
_piezo.PZ_LUTWaveParameters_swigregister(PZ_LUTWaveParameters)
class KPZ_MMIParams(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    JoystickMode = property(_piezo.KPZ_MMIParams_JoystickMode_get, _piezo.KPZ_MMIParams_JoystickMode_set)
    VoltageAdjustRate = property(_piezo.KPZ_MMIParams_VoltageAdjustRate_get, _piezo.KPZ_MMIParams_VoltageAdjustRate_set)
    VoltageStep = property(_piezo.KPZ_MMIParams_VoltageStep_get, _piezo.KPZ_MMIParams_VoltageStep_set)
    JoystickDirectionSense = property(_piezo.KPZ_MMIParams_JoystickDirectionSense_get, _piezo.KPZ_MMIParams_JoystickDirectionSense_set)
    PresetPos1 = property(_piezo.KPZ_MMIParams_PresetPos1_get, _piezo.KPZ_MMIParams_PresetPos1_set)
    PresetPos2 = property(_piezo.KPZ_MMIParams_PresetPos2_get, _piezo.KPZ_MMIParams_PresetPos2_set)
    DisplayIntensity = property(_piezo.KPZ_MMIParams_DisplayIntensity_get, _piezo.KPZ_MMIParams_DisplayIntensity_set)
    DisplayTimeout = property(_piezo.KPZ_MMIParams_DisplayTimeout_get, _piezo.KPZ_MMIParams_DisplayTimeout_set)
    DisplayDimIntensity = property(_piezo.KPZ_MMIParams_DisplayDimIntensity_get, _piezo.KPZ_MMIParams_DisplayDimIntensity_set)
    reserved = property(_piezo.KPZ_MMIParams_reserved_get, _piezo.KPZ_MMIParams_reserved_set)

    def __init__(self):
        _piezo.KPZ_MMIParams_swiginit(self, _piezo.new_KPZ_MMIParams())
    __swig_destroy__ = _piezo.delete_KPZ_MMIParams

# Register KPZ_MMIParams in _piezo:
_piezo.KPZ_MMIParams_swigregister(KPZ_MMIParams)
class KPZ_TriggerConfig(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Trigger1Mode = property(_piezo.KPZ_TriggerConfig_Trigger1Mode_get, _piezo.KPZ_TriggerConfig_Trigger1Mode_set)
    Trigger1Polarity = property(_piezo.KPZ_TriggerConfig_Trigger1Polarity_get, _piezo.KPZ_TriggerConfig_Trigger1Polarity_set)
    Trigger2Mode = property(_piezo.KPZ_TriggerConfig_Trigger2Mode_get, _piezo.KPZ_TriggerConfig_Trigger2Mode_set)
    Trigger2Polarity = property(_piezo.KPZ_TriggerConfig_Trigger2Polarity_get, _piezo.KPZ_TriggerConfig_Trigger2Polarity_set)
    reserved = property(_piezo.KPZ_TriggerConfig_reserved_get, _piezo.KPZ_TriggerConfig_reserved_set)

    def __init__(self):
        _piezo.KPZ_TriggerConfig_swiginit(self, _piezo.new_KPZ_TriggerConfig())
    __swig_destroy__ = _piezo.delete_KPZ_TriggerConfig

# Register KPZ_TriggerConfig in _piezo:
_piezo.KPZ_TriggerConfig_swigregister(KPZ_TriggerConfig)

def TLI_BuildDeviceList():
    return _piezo.TLI_BuildDeviceList()

def TLI_GetDeviceListSize():
    return _piezo.TLI_GetDeviceListSize()

def TLI_GetDeviceList(stringsReceiver):
    return _piezo.TLI_GetDeviceList(stringsReceiver)

def TLI_GetDeviceListByType(stringsReceiver, typeID):
    return _piezo.TLI_GetDeviceListByType(stringsReceiver, typeID)

def TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length):
    return _piezo.TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length)

def TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer):
    return _piezo.TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer)

def TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID):
    return _piezo.TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID)

def TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length):
    return _piezo.TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length)

def TLI_GetDeviceInfo(serialNo, info):
    return _piezo.TLI_GetDeviceInfo(serialNo, info)

def TLI_InitializeSimulations():
    return _piezo.TLI_InitializeSimulations()

def TLI_UninitializeSimulations():
    return _piezo.TLI_UninitializeSimulations()

def PCC_Open(serialNo):
    return _piezo.PCC_Open(serialNo)

def PCC_Close(serialNo):
    return _piezo.PCC_Close(serialNo)

def PCC_CheckConnection(serialNo):
    return _piezo.PCC_CheckConnection(serialNo)

def PCC_Disconnect(serialNo):
    return _piezo.PCC_Disconnect(serialNo)

def PCC_Identify(serialNo):
    return _piezo.PCC_Identify(serialNo)

def PCC_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState):
    return _piezo.PCC_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState)

def PCC_GetHardwareInfoBlock(serialNo, hardwareInfo):
    return _piezo.PCC_GetHardwareInfoBlock(serialNo, hardwareInfo)

def PCC_GetFirmwareVersion(serialNo):
    return _piezo.PCC_GetFirmwareVersion(serialNo)

def PCC_GetSoftwareVersion(serialNo):
    return _piezo.PCC_GetSoftwareVersion(serialNo)

def PCC_LoadSettings(serialNo):
    return _piezo.PCC_LoadSettings(serialNo)

def PCC_LoadNamedSettings(serialNo, settingsName):
    return _piezo.PCC_LoadNamedSettings(serialNo, settingsName)

def PCC_PersistSettings(serialNo):
    return _piezo.PCC_PersistSettings(serialNo)

def PCC_Disable(serialNo):
    return _piezo.PCC_Disable(serialNo)

def PCC_Enable(serialNo):
    return _piezo.PCC_Enable(serialNo)

def PCC_CanDeviceLockFrontPanel(serialNo):
    return _piezo.PCC_CanDeviceLockFrontPanel(serialNo)

def PCC_GetFrontPanelLocked(serialNo):
    return _piezo.PCC_GetFrontPanelLocked(serialNo)

def PCC_RequestFrontPanelLocked(serialNo):
    return _piezo.PCC_RequestFrontPanelLocked(serialNo)

def PCC_SetFrontPanelLock(serialNo, locked):
    return _piezo.PCC_SetFrontPanelLock(serialNo, locked)

def PCC_ClearMessageQueue(serialNo):
    return _piezo.PCC_ClearMessageQueue(serialNo)

def PCC_RegisterMessageCallback(serialNo, functionPointer):
    return _piezo.PCC_RegisterMessageCallback(serialNo, functionPointer)

def PCC_MessageQueueSize(serialNo):
    return _piezo.PCC_MessageQueueSize(serialNo)

def PCC_GetNextMessage(serialNo, messageType, messageID, messageData):
    return _piezo.PCC_GetNextMessage(serialNo, messageType, messageID, messageData)

def PCC_WaitForMessage(serialNo, messageType, messageID, messageData):
    return _piezo.PCC_WaitForMessage(serialNo, messageType, messageID, messageData)

def PCC_RequestSettings(serialNo):
    return _piezo.PCC_RequestSettings(serialNo)

def PCC_RequestStatus(serialNo):
    return _piezo.PCC_RequestStatus(serialNo)

def PCC_RequestStatusBits(serialNo):
    return _piezo.PCC_RequestStatusBits(serialNo)

def PCC_GetStatusBits(serialNo):
    return _piezo.PCC_GetStatusBits(serialNo)

def PCC_RequestActualPosition(serialNo):
    return _piezo.PCC_RequestActualPosition(serialNo)

def PCC_RequestPosition(serialNo):
    return _piezo.PCC_RequestPosition(serialNo)

def PCC_StartPolling(serialNo, milliseconds):
    return _piezo.PCC_StartPolling(serialNo, milliseconds)

def PCC_PollingDuration(serialNo):
    return _piezo.PCC_PollingDuration(serialNo)

def PCC_StopPolling(serialNo):
    return _piezo.PCC_StopPolling(serialNo)

def PCC_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS):
    return _piezo.PCC_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS)

def PCC_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout):
    return _piezo.PCC_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout)

def PCC_HasLastMsgTimerOverrun(serialNo):
    return _piezo.PCC_HasLastMsgTimerOverrun(serialNo)

def PCC_GetPositionControlMode(serialNo):
    return _piezo.PCC_GetPositionControlMode(serialNo)

def PCC_RequestPositionControlMode(serialNo):
    return _piezo.PCC_RequestPositionControlMode(serialNo)

def PCC_SetPositionControlMode(serialNo, mode):
    return _piezo.PCC_SetPositionControlMode(serialNo, mode)

def PCC_SetZero(serialNo):
    return _piezo.PCC_SetZero(serialNo)

def PCC_GetMaxOutputVoltage(serialNo):
    return _piezo.PCC_GetMaxOutputVoltage(serialNo)

def PCC_RequestMaxOutputVoltage(serialNo):
    return _piezo.PCC_RequestMaxOutputVoltage(serialNo)

def PCC_SetMaxOutputVoltage(serialNo, maxVoltage):
    return _piezo.PCC_SetMaxOutputVoltage(serialNo, maxVoltage)

def PCC_GetOutputVoltage(serialNo):
    return _piezo.PCC_GetOutputVoltage(serialNo)

def PCC_RequestOutputVoltage(serialNo):
    return _piezo.PCC_RequestOutputVoltage(serialNo)

def PCC_SetOutputVoltage(serialNo, volts):
    return _piezo.PCC_SetOutputVoltage(serialNo, volts)

def PCC_RequestVoltageSource(serialNo):
    return _piezo.PCC_RequestVoltageSource(serialNo)

def PCC_GetVoltageSource(serialNo):
    return _piezo.PCC_GetVoltageSource(serialNo)

def PCC_SetVoltageSource(serialNo, source):
    return _piezo.PCC_SetVoltageSource(serialNo, source)

def PCC_GetPosition(serialNo):
    return _piezo.PCC_GetPosition(serialNo)

def PCC_SetPosition(serialNo, position):
    return _piezo.PCC_SetPosition(serialNo, position)

def PCC_SetPositionToTolerance(serialNo, position, tolerance):
    return _piezo.PCC_SetPositionToTolerance(serialNo, position, tolerance)

def PCC_RequestFeedbackLoopPIconsts(serialNo):
    return _piezo.PCC_RequestFeedbackLoopPIconsts(serialNo)

def PCC_GetFeedbackLoopPIconsts(serialNo, proportionalTerm, integralTerm):
    return _piezo.PCC_GetFeedbackLoopPIconsts(serialNo, proportionalTerm, integralTerm)

def PCC_SetFeedbackLoopPIconsts(serialNo, proportionalTerm, integralTerm):
    return _piezo.PCC_SetFeedbackLoopPIconsts(serialNo, proportionalTerm, integralTerm)

def PCC_GetFeedbackLoopPIconstsBlock(serialNo, proportionalAndIntegralConstants):
    return _piezo.PCC_GetFeedbackLoopPIconstsBlock(serialNo, proportionalAndIntegralConstants)

def PCC_SetFeedbackLoopPIconstsBlock(serialNo, proportionalAndIntegralConstants):
    return _piezo.PCC_SetFeedbackLoopPIconstsBlock(serialNo, proportionalAndIntegralConstants)

def PCC_SetLUTwaveParams(serialNo, LUTwaveParams):
    return _piezo.PCC_SetLUTwaveParams(serialNo, LUTwaveParams)

def PCC_SetLUTwaveSample(serialNo, index, value):
    return _piezo.PCC_SetLUTwaveSample(serialNo, index, value)

def PCC_StartLUTwave(serialNo):
    return _piezo.PCC_StartLUTwave(serialNo)

def PCC_StopLUTwave(serialNo):
    return _piezo.PCC_StopLUTwave(serialNo)

def PCC_RequestLEDBrightness(serialNo):
    return _piezo.PCC_RequestLEDBrightness(serialNo)

def PCC_GetLEDBrightness(serialNo):
    return _piezo.PCC_GetLEDBrightness(serialNo)

def PCC_SetLEDBrightness(serialNo, brightness):
    return _piezo.PCC_SetLEDBrightness(serialNo, brightness)

def PCC_RequestIOSettings(serialNo):
    return _piezo.PCC_RequestIOSettings(serialNo)

def PCC_GetIOSettings(serialNo):
    return _piezo.PCC_GetIOSettings(serialNo)

def PCC_SetIOSettings(serialNo, ioSettings):
    return _piezo.PCC_SetIOSettings(serialNo, ioSettings)

def PCC_GetHubAnalogInput(serialNo):
    return _piezo.PCC_GetHubAnalogInput(serialNo)

def PCC_SetHubAnalogInput(serialNo, hubAnalogInput):
    return _piezo.PCC_SetHubAnalogInput(serialNo, hubAnalogInput)

def PCC_RequestMMIParams(serialNo):
    return _piezo.PCC_RequestMMIParams(serialNo)

def PCC_GetMMIParamsExt(serialNo, wheelMode, voltageAdjustRate, voltageStep, directionSense, presetVoltage1, presetVoltage2, displayIntensity, displayTimeout, displayDimIntensity):
    return _piezo.PCC_GetMMIParamsExt(serialNo, wheelMode, voltageAdjustRate, voltageStep, directionSense, presetVoltage1, presetVoltage2, displayIntensity, displayTimeout, displayDimIntensity)

def PCC_GetMMIParams(serialNo, wheelMode, voltageAdjustRate, voltageStep, directionSense, presetVoltage1, presetVoltage2, displayIntensity):
    return _piezo.PCC_GetMMIParams(serialNo, wheelMode, voltageAdjustRate, voltageStep, directionSense, presetVoltage1, presetVoltage2, displayIntensity)

def PCC_SetMMIParamsExt(serialNo, wheelMode, voltageAdjustRate, voltageStep, directionSense, presetVoltage1, presetVoltage2, displayIntensity, displayTimeout, displayDimIntensity):
    return _piezo.PCC_SetMMIParamsExt(serialNo, wheelMode, voltageAdjustRate, voltageStep, directionSense, presetVoltage1, presetVoltage2, displayIntensity, displayTimeout, displayDimIntensity)

def PCC_SetMMIParams(serialNo, wheelMode, voltageAdjustRate, voltageStep, directionSense, presetVoltage1, presetVoltage2, displayIntensity):
    return _piezo.PCC_SetMMIParams(serialNo, wheelMode, voltageAdjustRate, voltageStep, directionSense, presetVoltage1, presetVoltage2, displayIntensity)

def PCC_RequestTriggerConfigParams(serialNo):
    return _piezo.PCC_RequestTriggerConfigParams(serialNo)

def PCC_GetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity):
    return _piezo.PCC_GetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)

def PCC_SetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity):
    return _piezo.PCC_SetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)

def PCC_GetMMIParamsBlock(serialNo, mmiParams):
    return _piezo.PCC_GetMMIParamsBlock(serialNo, mmiParams)

def PCC_SetMMIParamsBlock(serialNo, mmiParams):
    return _piezo.PCC_SetMMIParamsBlock(serialNo, mmiParams)

def PCC_GetTriggerConfigParamsBlock(serialNo, triggerConfigParams):
    return _piezo.PCC_GetTriggerConfigParamsBlock(serialNo, triggerConfigParams)

def PCC_SetTriggerConfigParamsBlock(serialNo, triggerConfigParams):
    return _piezo.PCC_SetTriggerConfigParamsBlock(serialNo, triggerConfigParams)

def PCC_RequestDigitalOutputs(serialNo):
    return _piezo.PCC_RequestDigitalOutputs(serialNo)

def PCC_GetDigitalOutputs(serialNo):
    return _piezo.PCC_GetDigitalOutputs(serialNo)

def PCC_SetDigitalOutputs(serialNo, outputsBits):
    return _piezo.PCC_SetDigitalOutputs(serialNo, outputsBits)

