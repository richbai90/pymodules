# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _precision_piezo
else:
    import _precision_piezo

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


FT_OK = _precision_piezo.FT_OK
FT_InvalidHandle = _precision_piezo.FT_InvalidHandle
FT_DeviceNotFound = _precision_piezo.FT_DeviceNotFound
FT_DeviceNotOpened = _precision_piezo.FT_DeviceNotOpened
FT_IOError = _precision_piezo.FT_IOError
FT_InsufficientResources = _precision_piezo.FT_InsufficientResources
FT_InvalidParameter = _precision_piezo.FT_InvalidParameter
FT_DeviceNotPresent = _precision_piezo.FT_DeviceNotPresent
FT_IncorrectDevice = _precision_piezo.FT_IncorrectDevice
MOT_NotMotor = _precision_piezo.MOT_NotMotor
MOT_DCMotor = _precision_piezo.MOT_DCMotor
MOT_StepperMotor = _precision_piezo.MOT_StepperMotor
MOT_BrushlessMotor = _precision_piezo.MOT_BrushlessMotor
MOT_CustomMotor = _precision_piezo.MOT_CustomMotor
class TLI_DeviceInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    typeID = property(_precision_piezo.TLI_DeviceInfo_typeID_get, _precision_piezo.TLI_DeviceInfo_typeID_set)
    description = property(_precision_piezo.TLI_DeviceInfo_description_get, _precision_piezo.TLI_DeviceInfo_description_set)
    serialNo = property(_precision_piezo.TLI_DeviceInfo_serialNo_get, _precision_piezo.TLI_DeviceInfo_serialNo_set)
    PID = property(_precision_piezo.TLI_DeviceInfo_PID_get, _precision_piezo.TLI_DeviceInfo_PID_set)
    isKnownType = property(_precision_piezo.TLI_DeviceInfo_isKnownType_get, _precision_piezo.TLI_DeviceInfo_isKnownType_set)
    motorType = property(_precision_piezo.TLI_DeviceInfo_motorType_get, _precision_piezo.TLI_DeviceInfo_motorType_set)
    isPiezoDevice = property(_precision_piezo.TLI_DeviceInfo_isPiezoDevice_get, _precision_piezo.TLI_DeviceInfo_isPiezoDevice_set)
    isLaser = property(_precision_piezo.TLI_DeviceInfo_isLaser_get, _precision_piezo.TLI_DeviceInfo_isLaser_set)
    isCustomType = property(_precision_piezo.TLI_DeviceInfo_isCustomType_get, _precision_piezo.TLI_DeviceInfo_isCustomType_set)
    isRack = property(_precision_piezo.TLI_DeviceInfo_isRack_get, _precision_piezo.TLI_DeviceInfo_isRack_set)
    maxChannels = property(_precision_piezo.TLI_DeviceInfo_maxChannels_get, _precision_piezo.TLI_DeviceInfo_maxChannels_set)

    def __init__(self):
        _precision_piezo.TLI_DeviceInfo_swiginit(self, _precision_piezo.new_TLI_DeviceInfo())
    __swig_destroy__ = _precision_piezo.delete_TLI_DeviceInfo

# Register TLI_DeviceInfo in _precision_piezo:
_precision_piezo.TLI_DeviceInfo_swigregister(TLI_DeviceInfo)
class TLI_HardwareInformation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    serialNumber = property(_precision_piezo.TLI_HardwareInformation_serialNumber_get, _precision_piezo.TLI_HardwareInformation_serialNumber_set)
    modelNumber = property(_precision_piezo.TLI_HardwareInformation_modelNumber_get, _precision_piezo.TLI_HardwareInformation_modelNumber_set)
    type = property(_precision_piezo.TLI_HardwareInformation_type_get, _precision_piezo.TLI_HardwareInformation_type_set)
    firmwareVersion = property(_precision_piezo.TLI_HardwareInformation_firmwareVersion_get, _precision_piezo.TLI_HardwareInformation_firmwareVersion_set)
    notes = property(_precision_piezo.TLI_HardwareInformation_notes_get, _precision_piezo.TLI_HardwareInformation_notes_set)
    deviceDependantData = property(_precision_piezo.TLI_HardwareInformation_deviceDependantData_get, _precision_piezo.TLI_HardwareInformation_deviceDependantData_set)
    hardwareVersion = property(_precision_piezo.TLI_HardwareInformation_hardwareVersion_get, _precision_piezo.TLI_HardwareInformation_hardwareVersion_set)
    modificationState = property(_precision_piezo.TLI_HardwareInformation_modificationState_get, _precision_piezo.TLI_HardwareInformation_modificationState_set)
    numChannels = property(_precision_piezo.TLI_HardwareInformation_numChannels_get, _precision_piezo.TLI_HardwareInformation_numChannels_set)

    def __init__(self):
        _precision_piezo.TLI_HardwareInformation_swiginit(self, _precision_piezo.new_TLI_HardwareInformation())
    __swig_destroy__ = _precision_piezo.delete_TLI_HardwareInformation

# Register TLI_HardwareInformation in _precision_piezo:
_precision_piezo.TLI_HardwareInformation_swigregister(TLI_HardwareInformation)
PZ_Undefined = _precision_piezo.PZ_Undefined
PZ_OpenLoop = _precision_piezo.PZ_OpenLoop
PZ_CloseLoop = _precision_piezo.PZ_CloseLoop
PZ_OpenLoopSmooth = _precision_piezo.PZ_OpenLoopSmooth
PZ_CloseLoopSmooth = _precision_piezo.PZ_CloseLoopSmooth
PZ_SoftwareOnly = _precision_piezo.PZ_SoftwareOnly
PZ_ExternalSignal = _precision_piezo.PZ_ExternalSignal
PZ_Potentiometer = _precision_piezo.PZ_Potentiometer
PZ_All = _precision_piezo.PZ_All
PZ_Continuous = _precision_piezo.PZ_Continuous
PZ_Fixed = _precision_piezo.PZ_Fixed
PZ_OutputTrigEnable = _precision_piezo.PZ_OutputTrigEnable
PZ_InputTrigEnable = _precision_piezo.PZ_InputTrigEnable
PZ_OutputTrigSenseHigh = _precision_piezo.PZ_OutputTrigSenseHigh
PZ_InputTrigSenseHigh = _precision_piezo.PZ_InputTrigSenseHigh
PZ_OutputGated = _precision_piezo.PZ_OutputGated
PZ_OutputTrigRepeat = _precision_piezo.PZ_OutputTrigRepeat
DerivFilterOn = _precision_piezo.DerivFilterOn
DerivFilterOff = _precision_piezo.DerivFilterOff
NotchFilterOn = _precision_piezo.NotchFilterOn
NotchFilterOff = _precision_piezo.NotchFilterOff
NotchFilter1 = _precision_piezo.NotchFilter1
NotchFilter2 = _precision_piezo.NotchFilter2
NotchFilterBoth = _precision_piezo.NotchFilterBoth
SWOnly = _precision_piezo.SWOnly
ExtBNC = _precision_piezo.ExtBNC
Joystick = _precision_piezo.Joystick
JoystickBnc = _precision_piezo.JoystickBnc
HV = _precision_piezo.HV
PosRaw = _precision_piezo.PosRaw
PosCorrected = _precision_piezo.PosCorrected
OP_Unfiltered = _precision_piezo.OP_Unfiltered
OP_200Hz = _precision_piezo.OP_200Hz
StrainGauge = _precision_piezo.StrainGauge
Capacitive = _precision_piezo.Capacitive
Optical = _precision_piezo.Optical
NonInverted = _precision_piezo.NonInverted
Inverted = _precision_piezo.Inverted
Bright = _precision_piezo.Bright
Dim = _precision_piezo.Dim
Off = _precision_piezo.Off
class PPC_PIDConsts(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    PIDConstsP = property(_precision_piezo.PPC_PIDConsts_PIDConstsP_get, _precision_piezo.PPC_PIDConsts_PIDConstsP_set)
    PIDConstsI = property(_precision_piezo.PPC_PIDConsts_PIDConstsI_get, _precision_piezo.PPC_PIDConsts_PIDConstsI_set)
    PIDConstsD = property(_precision_piezo.PPC_PIDConsts_PIDConstsD_get, _precision_piezo.PPC_PIDConsts_PIDConstsD_set)
    PIDConstsDFc = property(_precision_piezo.PPC_PIDConsts_PIDConstsDFc_get, _precision_piezo.PPC_PIDConsts_PIDConstsDFc_set)
    PIDDerivFilterOn = property(_precision_piezo.PPC_PIDConsts_PIDDerivFilterOn_get, _precision_piezo.PPC_PIDConsts_PIDDerivFilterOn_set)
    PIDIndex = property(_precision_piezo.PPC_PIDConsts_PIDIndex_get, _precision_piezo.PPC_PIDConsts_PIDIndex_set)

    def __init__(self):
        _precision_piezo.PPC_PIDConsts_swiginit(self, _precision_piezo.new_PPC_PIDConsts())
    __swig_destroy__ = _precision_piezo.delete_PPC_PIDConsts

# Register PPC_PIDConsts in _precision_piezo:
_precision_piezo.PPC_PIDConsts_swigregister(PPC_PIDConsts)
class PPC_NotchParams(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    filterNo = property(_precision_piezo.PPC_NotchParams_filterNo_get, _precision_piezo.PPC_NotchParams_filterNo_set)
    filter1Fc = property(_precision_piezo.PPC_NotchParams_filter1Fc_get, _precision_piezo.PPC_NotchParams_filter1Fc_set)
    filter1Q = property(_precision_piezo.PPC_NotchParams_filter1Q_get, _precision_piezo.PPC_NotchParams_filter1Q_set)
    notchFilter1On = property(_precision_piezo.PPC_NotchParams_notchFilter1On_get, _precision_piezo.PPC_NotchParams_notchFilter1On_set)
    filter2Fc = property(_precision_piezo.PPC_NotchParams_filter2Fc_get, _precision_piezo.PPC_NotchParams_filter2Fc_set)
    filter2Q = property(_precision_piezo.PPC_NotchParams_filter2Q_get, _precision_piezo.PPC_NotchParams_filter2Q_set)
    notchFilter2On = property(_precision_piezo.PPC_NotchParams_notchFilter2On_get, _precision_piezo.PPC_NotchParams_notchFilter2On_set)

    def __init__(self):
        _precision_piezo.PPC_NotchParams_swiginit(self, _precision_piezo.new_PPC_NotchParams())
    __swig_destroy__ = _precision_piezo.delete_PPC_NotchParams

# Register PPC_NotchParams in _precision_piezo:
_precision_piezo.PPC_NotchParams_swigregister(PPC_NotchParams)
class PPC_IOSettings(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    controlSrc = property(_precision_piezo.PPC_IOSettings_controlSrc_get, _precision_piezo.PPC_IOSettings_controlSrc_set)
    monitorOPSig = property(_precision_piezo.PPC_IOSettings_monitorOPSig_get, _precision_piezo.PPC_IOSettings_monitorOPSig_set)
    monitorOPBandwidth = property(_precision_piezo.PPC_IOSettings_monitorOPBandwidth_get, _precision_piezo.PPC_IOSettings_monitorOPBandwidth_set)
    feedbackSrc = property(_precision_piezo.PPC_IOSettings_feedbackSrc_get, _precision_piezo.PPC_IOSettings_feedbackSrc_set)
    FPBrightness = property(_precision_piezo.PPC_IOSettings_FPBrightness_get, _precision_piezo.PPC_IOSettings_FPBrightness_set)
    feedbackPolarity = property(_precision_piezo.PPC_IOSettings_feedbackPolarity_get, _precision_piezo.PPC_IOSettings_feedbackPolarity_set)

    def __init__(self):
        _precision_piezo.PPC_IOSettings_swiginit(self, _precision_piezo.new_PPC_IOSettings())
    __swig_destroy__ = _precision_piezo.delete_PPC_IOSettings

# Register PPC_IOSettings in _precision_piezo:
_precision_piezo.PPC_IOSettings_swigregister(PPC_IOSettings)

def TLI_BuildDeviceList():
    return _precision_piezo.TLI_BuildDeviceList()

def TLI_GetDeviceListSize():
    return _precision_piezo.TLI_GetDeviceListSize()

def TLI_GetDeviceList(stringsReceiver):
    return _precision_piezo.TLI_GetDeviceList(stringsReceiver)

def TLI_GetDeviceListByType(stringsReceiver, typeID):
    return _precision_piezo.TLI_GetDeviceListByType(stringsReceiver, typeID)

def TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length):
    return _precision_piezo.TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length)

def TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer):
    return _precision_piezo.TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer)

def TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID):
    return _precision_piezo.TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID)

def TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length):
    return _precision_piezo.TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length)

def TLI_GetDeviceInfo(serialNo, info):
    return _precision_piezo.TLI_GetDeviceInfo(serialNo, info)

def TLI_InitializeSimulations():
    return _precision_piezo.TLI_InitializeSimulations()

def TLI_UninitializeSimulations():
    return _precision_piezo.TLI_UninitializeSimulations()

def PPC_Open(serialNo):
    return _precision_piezo.PPC_Open(serialNo)

def PPC_Close(serialNo):
    return _precision_piezo.PPC_Close(serialNo)

def PPC_CheckConnection(serialNo):
    return _precision_piezo.PPC_CheckConnection(serialNo)

def PPC_Identify(serialNo):
    return _precision_piezo.PPC_Identify(serialNo)

def PPC_Disconnect(serialNo):
    return _precision_piezo.PPC_Disconnect(serialNo)

def PPC_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState):
    return _precision_piezo.PPC_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState)

def PPC_GetHardwareInfoBlock(serialNo, hardwareInfo):
    return _precision_piezo.PPC_GetHardwareInfoBlock(serialNo, hardwareInfo)

def PPC_GetFirmwareVersion(serialNo):
    return _precision_piezo.PPC_GetFirmwareVersion(serialNo)

def PPC_GetSoftwareVersion(serialNo):
    return _precision_piezo.PPC_GetSoftwareVersion(serialNo)

def PPC_LoadSettings(serialNo):
    return _precision_piezo.PPC_LoadSettings(serialNo)

def PPC_LoadNamedSettings(serialNo, settingsName):
    return _precision_piezo.PPC_LoadNamedSettings(serialNo, settingsName)

def PPC_PersistSettings(serialNo):
    return _precision_piezo.PPC_PersistSettings(serialNo)

def PPC_DisableChannel(serialNo):
    return _precision_piezo.PPC_DisableChannel(serialNo)

def PPC_EnableChannel(serialNo):
    return _precision_piezo.PPC_EnableChannel(serialNo)

def PPC_RegisterMessageCallback(serialNo, functionPointer):
    return _precision_piezo.PPC_RegisterMessageCallback(serialNo, functionPointer)

def PPC_MessageQueueSize(serialNo):
    return _precision_piezo.PPC_MessageQueueSize(serialNo)

def PPC_ClearMessageQueue(serialNo):
    return _precision_piezo.PPC_ClearMessageQueue(serialNo)

def PPC_GetNextMessage(serialNo, messageType, messageID, messageData):
    return _precision_piezo.PPC_GetNextMessage(serialNo, messageType, messageID, messageData)

def PPC_WaitForMessage(serialNo, messageType, messageID, messageData):
    return _precision_piezo.PPC_WaitForMessage(serialNo, messageType, messageID, messageData)

def PPC_StartPolling(serialNo, milliseconds):
    return _precision_piezo.PPC_StartPolling(serialNo, milliseconds)

def PPC_PollingDuration(serialNo):
    return _precision_piezo.PPC_PollingDuration(serialNo)

def PPC_StopPolling(serialNo):
    return _precision_piezo.PPC_StopPolling(serialNo)

def PPC_RequestSettings(serialNo):
    return _precision_piezo.PPC_RequestSettings(serialNo)

def PPC_RequestStatus(serialNo):
    return _precision_piezo.PPC_RequestStatus(serialNo)

def PPC_RequestStatusBits(serialNo):
    return _precision_piezo.PPC_RequestStatusBits(serialNo)

def PPC_GetStatusBits(serialNo):
    return _precision_piezo.PPC_GetStatusBits(serialNo)

def PPC_ResetParameters(serialNo):
    return _precision_piezo.PPC_ResetParameters(serialNo)

def PPC_SetZero(serialNo):
    return _precision_piezo.PPC_SetZero(serialNo)

def PPC_RequestActualPosition(serialNo):
    return _precision_piezo.PPC_RequestActualPosition(serialNo)

def PPC_RequestPosition(serialNo):
    return _precision_piezo.PPC_RequestPosition(serialNo)

def PPC_GetPositionControlMode(serialNo):
    return _precision_piezo.PPC_GetPositionControlMode(serialNo)

def PPC_RequestPositionControlMode(serialNo):
    return _precision_piezo.PPC_RequestPositionControlMode(serialNo)

def PPC_SetPositionControlMode(serialNo, mode):
    return _precision_piezo.PPC_SetPositionControlMode(serialNo, mode)

def PPC_GetMinOutputVoltage(serialNo):
    return _precision_piezo.PPC_GetMinOutputVoltage(serialNo)

def PPC_GetMaxOutputVoltage(serialNo):
    return _precision_piezo.PPC_GetMaxOutputVoltage(serialNo)

def PPC_RequestMaxOutputVoltage(serialNo):
    return _precision_piezo.PPC_RequestMaxOutputVoltage(serialNo)

def PPC_SetMaxOutputVoltage(serialNo, maxVoltage):
    return _precision_piezo.PPC_SetMaxOutputVoltage(serialNo, maxVoltage)

def PPC_GetOutputVoltage(serialNo):
    return _precision_piezo.PPC_GetOutputVoltage(serialNo)

def PPC_RequestOutputVoltage(serialNo):
    return _precision_piezo.PPC_RequestOutputVoltage(serialNo)

def PPC_SetOutputVoltage(serialNo, volts):
    return _precision_piezo.PPC_SetOutputVoltage(serialNo, volts)

def PPC_RequestVoltageSource(serialNo):
    return _precision_piezo.PPC_RequestVoltageSource(serialNo)

def PPC_GetVoltageSource(serialNo):
    return _precision_piezo.PPC_GetVoltageSource(serialNo)

def PPC_SetVoltageSource(serialNo, source):
    return _precision_piezo.PPC_SetVoltageSource(serialNo, source)

def PPC_GetMaximumTravel(serialNo):
    return _precision_piezo.PPC_GetMaximumTravel(serialNo)

def PPC_GetPosition(serialNo):
    return _precision_piezo.PPC_GetPosition(serialNo)

def PPC_SetPosition(serialNo, position):
    return _precision_piezo.PPC_SetPosition(serialNo, position)

def PPC_SetPositionToTolerance(serialNo, position, tolerance):
    return _precision_piezo.PPC_SetPositionToTolerance(serialNo, position, tolerance)

def PPC_GetIOSettings(serialNo, ioSettings):
    return _precision_piezo.PPC_GetIOSettings(serialNo, ioSettings)

def PPC_SetIOSettings(serialNo, ioSettings):
    return _precision_piezo.PPC_SetIOSettings(serialNo, ioSettings)

def PPC_GetNotchParams(serialNo, notchParams):
    return _precision_piezo.PPC_GetNotchParams(serialNo, notchParams)

def PPC_SetNotchParams(serialNo, notchParams):
    return _precision_piezo.PPC_SetNotchParams(serialNo, notchParams)

def PPC_RequestPIDConsts(serialNo):
    return _precision_piezo.PPC_RequestPIDConsts(serialNo)

def PPC_GetPIDConsts(serialNo, pidConsts):
    return _precision_piezo.PPC_GetPIDConsts(serialNo, pidConsts)

def PPC_SetPIDConsts(serialNo, pidConsts):
    return _precision_piezo.PPC_SetPIDConsts(serialNo, pidConsts)

def PPC_RequestRackDigitalOutputs(serialNo):
    return _precision_piezo.PPC_RequestRackDigitalOutputs(serialNo)

def PPC_GetRackDigitalOutputs(serialNo):
    return _precision_piezo.PPC_GetRackDigitalOutputs(serialNo)

def PPC_SetRackDigitalOutputs(serialNo, outputsBits):
    return _precision_piezo.PPC_SetRackDigitalOutputs(serialNo, outputsBits)

def PPC_RequestRackStatusBits(serialNo):
    return _precision_piezo.PPC_RequestRackStatusBits(serialNo)

def PPC_GetRackStatusBits(serialNo):
    return _precision_piezo.PPC_GetRackStatusBits(serialNo)

def PPC2_Identify(serialNo, channel):
    return _precision_piezo.PPC2_Identify(serialNo, channel)

def PPC2_GetHardwareInfo(serialNo, channel, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState):
    return _precision_piezo.PPC2_GetHardwareInfo(serialNo, channel, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState)

def PPC2_GetHardwareInfoBlock(serialNo, channel, hardwareInfo):
    return _precision_piezo.PPC2_GetHardwareInfoBlock(serialNo, channel, hardwareInfo)

def PPC2_LoadSettings(serialNo, channel):
    return _precision_piezo.PPC2_LoadSettings(serialNo, channel)

def PPC2_LoadNamedSettings(serialNo, channel, settingsName):
    return _precision_piezo.PPC2_LoadNamedSettings(serialNo, channel, settingsName)

def PPC2_PersistSettings(serialNo, channel):
    return _precision_piezo.PPC2_PersistSettings(serialNo, channel)

def PPC2_DisableChannel(serialNo, channel):
    return _precision_piezo.PPC2_DisableChannel(serialNo, channel)

def PPC2_EnableChannel(serialNo, channel):
    return _precision_piezo.PPC2_EnableChannel(serialNo, channel)

def PPC2_RegisterMessageCallback(serialNo, channel, functionPointer):
    return _precision_piezo.PPC2_RegisterMessageCallback(serialNo, channel, functionPointer)

def PPC2_MessageQueueSize(serialNo, channel):
    return _precision_piezo.PPC2_MessageQueueSize(serialNo, channel)

def PPC2_ClearMessageQueue(serialNo, channel):
    return _precision_piezo.PPC2_ClearMessageQueue(serialNo, channel)

def PPC2_GetNextMessage(serialNo, channel, messageType, messageID, messageData):
    return _precision_piezo.PPC2_GetNextMessage(serialNo, channel, messageType, messageID, messageData)

def PPC2_WaitForMessage(serialNo, channel, messageType, messageID, messageData):
    return _precision_piezo.PPC2_WaitForMessage(serialNo, channel, messageType, messageID, messageData)

def PPC2_StartPolling(serialNo, channel, milliseconds):
    return _precision_piezo.PPC2_StartPolling(serialNo, channel, milliseconds)

def PPC2_PollingDuration(serialNo, channel):
    return _precision_piezo.PPC2_PollingDuration(serialNo, channel)

def PPC2_StopPolling(serialNo, channel):
    return _precision_piezo.PPC2_StopPolling(serialNo, channel)

def PPC2_RequestSettings(serialNo, channel):
    return _precision_piezo.PPC2_RequestSettings(serialNo, channel)

def PPC2_RequestStatus(serialNo, channel):
    return _precision_piezo.PPC2_RequestStatus(serialNo, channel)

def PPC2_RequestStatusBits(serialNo, channel):
    return _precision_piezo.PPC2_RequestStatusBits(serialNo, channel)

def PPC2_GetStatusBits(serialNo, channel):
    return _precision_piezo.PPC2_GetStatusBits(serialNo, channel)

def PPC2_ResetParameters(serialNo, channel):
    return _precision_piezo.PPC2_ResetParameters(serialNo, channel)

def PPC2_SetZero(serialNo, channel):
    return _precision_piezo.PPC2_SetZero(serialNo, channel)

def PPC2_RequestActualPosition(serialNo, channel):
    return _precision_piezo.PPC2_RequestActualPosition(serialNo, channel)

def PPC2_RequestPosition(serialNo, channel):
    return _precision_piezo.PPC2_RequestPosition(serialNo, channel)

def PPC2_GetPositionControlMode(serialNo, channel):
    return _precision_piezo.PPC2_GetPositionControlMode(serialNo, channel)

def PPC2_SetPositionControlMode(serialNo, channel, mode):
    return _precision_piezo.PPC2_SetPositionControlMode(serialNo, channel, mode)

def PPC2_GetMinOutputVoltage(serialNo, channel):
    return _precision_piezo.PPC2_GetMinOutputVoltage(serialNo, channel)

def PPC2_GetMaxOutputVoltage(serialNo, channel):
    return _precision_piezo.PPC2_GetMaxOutputVoltage(serialNo, channel)

def PPC2_RequestMaxOutputVoltage(serialNo, channel):
    return _precision_piezo.PPC2_RequestMaxOutputVoltage(serialNo, channel)

def PPC2_SetMaxOutputVoltage(serialNo, channel, maxVoltage):
    return _precision_piezo.PPC2_SetMaxOutputVoltage(serialNo, channel, maxVoltage)

def PPC2_GetOutputVoltage(serialNo, channel):
    return _precision_piezo.PPC2_GetOutputVoltage(serialNo, channel)

def PPC2_RequestOutputVoltage(serialNo, channel):
    return _precision_piezo.PPC2_RequestOutputVoltage(serialNo, channel)

def PPC2_SetOutputVoltage(serialNo, channel, volts):
    return _precision_piezo.PPC2_SetOutputVoltage(serialNo, channel, volts)

def PPC2_GetMaximumTravel(serialNo, channel):
    return _precision_piezo.PPC2_GetMaximumTravel(serialNo, channel)

def PPC2_GetPosition(serialNo, channel):
    return _precision_piezo.PPC2_GetPosition(serialNo, channel)

def PPC2_SetPosition(serialNo, channel, position):
    return _precision_piezo.PPC2_SetPosition(serialNo, channel, position)

def PPC2_SetPositionToTolerance(serialNo, channel, position, tolerance):
    return _precision_piezo.PPC2_SetPositionToTolerance(serialNo, channel, position, tolerance)

def PPC2_GetIOSettings(serialNo, channel, ioSettings):
    return _precision_piezo.PPC2_GetIOSettings(serialNo, channel, ioSettings)

def PPC2_SetIOSettings(serialNo, channel, ioSettings):
    return _precision_piezo.PPC2_SetIOSettings(serialNo, channel, ioSettings)

def PPC2_GetNotchParams(serialNo, channel, notchParams):
    return _precision_piezo.PPC2_GetNotchParams(serialNo, channel, notchParams)

def PPC2_SetNotchParams(serialNo, channel, notchParams):
    return _precision_piezo.PPC2_SetNotchParams(serialNo, channel, notchParams)

def PPC2_RequestPIDConsts(serialNo, channel):
    return _precision_piezo.PPC2_RequestPIDConsts(serialNo, channel)

def PPC2_GetPIDConsts(serialNo, channel, pidConsts):
    return _precision_piezo.PPC2_GetPIDConsts(serialNo, channel, pidConsts)

def PPC2_SetPIDConsts(serialNo, channel, pidConsts):
    return _precision_piezo.PPC2_SetPIDConsts(serialNo, channel, pidConsts)

def PPC2_RequestRackDigitalOutputs(serialNo):
    return _precision_piezo.PPC2_RequestRackDigitalOutputs(serialNo)

def PPC2_GetRackDigitalOutputs(serialNo):
    return _precision_piezo.PPC2_GetRackDigitalOutputs(serialNo)

def PPC2_SetRackDigitalOutputs(serialNo, outputsBits):
    return _precision_piezo.PPC2_SetRackDigitalOutputs(serialNo, outputsBits)

def PPC2_RequestRackStatusBits(serialNo):
    return _precision_piezo.PPC2_RequestRackStatusBits(serialNo)

def PPC2_GetRackStatusBits(serialNo):
    return _precision_piezo.PPC2_GetRackStatusBits(serialNo)

