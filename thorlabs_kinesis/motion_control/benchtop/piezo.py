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
PZ_Undefined = _piezo.PZ_Undefined
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

def PBC_Open(serialNo):
    return _piezo.PBC_Open(serialNo)

def PBC_Close(serialNo):
    return _piezo.PBC_Close(serialNo)

def PBC_CheckConnection(serialNo):
    return _piezo.PBC_CheckConnection(serialNo)

def PBC_Identify(serialNo, channel):
    return _piezo.PBC_Identify(serialNo, channel)

def PBC_Disconnect(serialNo):
    return _piezo.PBC_Disconnect(serialNo)

def PBC_MaxChannelCount(serialNo):
    return _piezo.PBC_MaxChannelCount(serialNo)

def PBC_IsChannelValid(serialNo, channel):
    return _piezo.PBC_IsChannelValid(serialNo, channel)

def PBC_GetHardwareInfo(serialNo, channel, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState):
    return _piezo.PBC_GetHardwareInfo(serialNo, channel, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState)

def PBC_GetHardwareInfoBlock(serialNo, channel, hardwareInfo):
    return _piezo.PBC_GetHardwareInfoBlock(serialNo, channel, hardwareInfo)

def PBC_GetNumChannels(serialNo):
    return _piezo.PBC_GetNumChannels(serialNo)

def PBC_GetFirmwareVersion(serialNo):
    return _piezo.PBC_GetFirmwareVersion(serialNo)

def PBC_GetSoftwareVersion(serialNo):
    return _piezo.PBC_GetSoftwareVersion(serialNo)

def PBC_LoadSettings(serialNo, channel):
    return _piezo.PBC_LoadSettings(serialNo, channel)

def PBC_LoadNamedSettings(serialNo, channel, settingsName):
    return _piezo.PBC_LoadNamedSettings(serialNo, channel, settingsName)

def PBC_PersistSettings(serialNo, channel):
    return _piezo.PBC_PersistSettings(serialNo, channel)

def PBC_DisableChannel(serialNo, channel):
    return _piezo.PBC_DisableChannel(serialNo, channel)

def PBC_EnableChannel(serialNo, channel):
    return _piezo.PBC_EnableChannel(serialNo, channel)

def PBC_RegisterMessageCallback(serialNo, channel, functionPointer):
    return _piezo.PBC_RegisterMessageCallback(serialNo, channel, functionPointer)

def PBC_MessageQueueSize(serialNo, channel):
    return _piezo.PBC_MessageQueueSize(serialNo, channel)

def PBC_ClearMessageQueue(serialNo, channel):
    return _piezo.PBC_ClearMessageQueue(serialNo, channel)

def PBC_GetNextMessage(serialNo, channel, messageType, messageID, messageData):
    return _piezo.PBC_GetNextMessage(serialNo, channel, messageType, messageID, messageData)

def PBC_WaitForMessage(serialNo, channel, messageType, messageID, messageData):
    return _piezo.PBC_WaitForMessage(serialNo, channel, messageType, messageID, messageData)

def PBC_StartPolling(serialNo, channel, milliseconds):
    return _piezo.PBC_StartPolling(serialNo, channel, milliseconds)

def PBC_PollingDuration(serialNo, channel):
    return _piezo.PBC_PollingDuration(serialNo, channel)

def PBC_StopPolling(serialNo, channel):
    return _piezo.PBC_StopPolling(serialNo, channel)

def PBC_TimeSinceLastMsgReceived(serialNo, channel, lastUpdateTimeMS):
    return _piezo.PBC_TimeSinceLastMsgReceived(serialNo, channel, lastUpdateTimeMS)

def PBC_EnableLastMsgTimer(serialNo, channel, enable, lastMsgTimeout):
    return _piezo.PBC_EnableLastMsgTimer(serialNo, channel, enable, lastMsgTimeout)

def PBC_HasLastMsgTimerOverrun(serialNo, channel):
    return _piezo.PBC_HasLastMsgTimerOverrun(serialNo, channel)

def PBC_RequestSettings(serialNo, channel):
    return _piezo.PBC_RequestSettings(serialNo, channel)

def PBC_RequestStatus(serialNo, channel):
    return _piezo.PBC_RequestStatus(serialNo, channel)

def PBC_RequestStatusBits(serialNo, channel):
    return _piezo.PBC_RequestStatusBits(serialNo, channel)

def PBC_GetStatusBits(serialNo, channel):
    return _piezo.PBC_GetStatusBits(serialNo, channel)

def PBC_RequestActualPosition(serialNo, channel):
    return _piezo.PBC_RequestActualPosition(serialNo, channel)

def PBC_RequestPosition(serialNo, channel):
    return _piezo.PBC_RequestPosition(serialNo, channel)

def PBC_ResetParameters(serialNo, channel):
    return _piezo.PBC_ResetParameters(serialNo, channel)

def PBC_SetZero(serialNo, channel):
    return _piezo.PBC_SetZero(serialNo, channel)

def PBC_GetPositionControlMode(serialNo, channel):
    return _piezo.PBC_GetPositionControlMode(serialNo, channel)

def PBC_RequestPositionControlMode(serialNo, channel):
    return _piezo.PBC_RequestPositionControlMode(serialNo, channel)

def PBC_SetPositionControlMode(serialNo, channel, mode):
    return _piezo.PBC_SetPositionControlMode(serialNo, channel, mode)

def PBC_GetMaxOutputVoltage(serialNo, channel):
    return _piezo.PBC_GetMaxOutputVoltage(serialNo, channel)

def PBC_RequestMaxOutputVoltage(serialNo, channel):
    return _piezo.PBC_RequestMaxOutputVoltage(serialNo, channel)

def PBC_SetMaxOutputVoltage(serialNo, channel, maxVoltage):
    return _piezo.PBC_SetMaxOutputVoltage(serialNo, channel, maxVoltage)

def PBC_GetOutputVoltage(serialNo, channel):
    return _piezo.PBC_GetOutputVoltage(serialNo, channel)

def PBC_RequestOutputVoltage(serialNo, channel):
    return _piezo.PBC_RequestOutputVoltage(serialNo, channel)

def PBC_SetOutputVoltage(serialNo, channel, volts):
    return _piezo.PBC_SetOutputVoltage(serialNo, channel, volts)

def PBC_RequestVoltageSource(serialNo, channel):
    return _piezo.PBC_RequestVoltageSource(serialNo, channel)

def PBC_GetVoltageSource(serialNo, channel):
    return _piezo.PBC_GetVoltageSource(serialNo, channel)

def PBC_SetVoltageSource(serialNo, channel, source):
    return _piezo.PBC_SetVoltageSource(serialNo, channel, source)

def PBC_RequestMaximumTravel(serialNo, channel):
    return _piezo.PBC_RequestMaximumTravel(serialNo, channel)

def PBC_GetMaximumTravel(serialNo, channel):
    return _piezo.PBC_GetMaximumTravel(serialNo, channel)

def PBC_GetPosition(serialNo, channel):
    return _piezo.PBC_GetPosition(serialNo, channel)

def PBC_SetPosition(serialNo, channel, position):
    return _piezo.PBC_SetPosition(serialNo, channel, position)

def PBC_SetPositionToTolerance(serialNo, channel, position, tolerance):
    return _piezo.PBC_SetPositionToTolerance(serialNo, channel, position, tolerance)

def PBC_RequestFeedbackLoopPIconsts(serialNo, channel):
    return _piezo.PBC_RequestFeedbackLoopPIconsts(serialNo, channel)

def PBC_GetFeedbackLoopPIconsts(serialNo, channel, proportionalTerm, integralTerm):
    return _piezo.PBC_GetFeedbackLoopPIconsts(serialNo, channel, proportionalTerm, integralTerm)

def PBC_SetFeedbackLoopPIconsts(serialNo, channel, proportionalTerm, integralTerm):
    return _piezo.PBC_SetFeedbackLoopPIconsts(serialNo, channel, proportionalTerm, integralTerm)

def PBC_GetFeedbackLoopPIconstsBlock(serialNo, channel, proportionalAndIntegralConstants):
    return _piezo.PBC_GetFeedbackLoopPIconstsBlock(serialNo, channel, proportionalAndIntegralConstants)

def PBC_SetFeedbackLoopPIconstsBlock(serialNo, channel, proportionalAndIntegralConstants):
    return _piezo.PBC_SetFeedbackLoopPIconstsBlock(serialNo, channel, proportionalAndIntegralConstants)

def PBC_SetLUTwaveParams(serialNo, channel, LUTwaveParams):
    return _piezo.PBC_SetLUTwaveParams(serialNo, channel, LUTwaveParams)

def PBC_SetLUTwaveSample(serialNo, channel, index, value):
    return _piezo.PBC_SetLUTwaveSample(serialNo, channel, index, value)

def PBC_StartLUTwave(serialNo, channel):
    return _piezo.PBC_StartLUTwave(serialNo, channel)

def PBC_StopLUTwave(serialNo, channel):
    return _piezo.PBC_StopLUTwave(serialNo, channel)

def PBC_RequestRackDigitalOutputs(serialNo):
    return _piezo.PBC_RequestRackDigitalOutputs(serialNo)

def PBC_GetRackDigitalOutputs(serialNo):
    return _piezo.PBC_GetRackDigitalOutputs(serialNo)

def PBC_SetRackDigitalOutputs(serialNo, outputsBits):
    return _piezo.PBC_SetRackDigitalOutputs(serialNo, outputsBits)

def PBC_RequestRackStatusBits(serialNo):
    return _piezo.PBC_RequestRackStatusBits(serialNo)

def PBC_GetRackStatusBits(serialNo):
    return _piezo.PBC_GetRackStatusBits(serialNo)
