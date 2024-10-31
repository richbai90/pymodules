# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _filter_flipper
else:
    import _filter_flipper

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


FT_OK = _filter_flipper.FT_OK
FT_InvalidHandle = _filter_flipper.FT_InvalidHandle
FT_DeviceNotFound = _filter_flipper.FT_DeviceNotFound
FT_DeviceNotOpened = _filter_flipper.FT_DeviceNotOpened
FT_IOError = _filter_flipper.FT_IOError
FT_InsufficientResources = _filter_flipper.FT_InsufficientResources
FT_InvalidParameter = _filter_flipper.FT_InvalidParameter
FT_DeviceNotPresent = _filter_flipper.FT_DeviceNotPresent
FT_IncorrectDevice = _filter_flipper.FT_IncorrectDevice
MOT_NotMotor = _filter_flipper.MOT_NotMotor
MOT_DCMotor = _filter_flipper.MOT_DCMotor
MOT_StepperMotor = _filter_flipper.MOT_StepperMotor
MOT_BrushlessMotor = _filter_flipper.MOT_BrushlessMotor
MOT_CustomMotor = _filter_flipper.MOT_CustomMotor
FF_PositionError = _filter_flipper.FF_PositionError
Position1 = _filter_flipper.Position1
Position2 = _filter_flipper.Position2
class TLI_DeviceInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    typeID = property(_filter_flipper.TLI_DeviceInfo_typeID_get, _filter_flipper.TLI_DeviceInfo_typeID_set)
    description = property(_filter_flipper.TLI_DeviceInfo_description_get, _filter_flipper.TLI_DeviceInfo_description_set)
    serialNo = property(_filter_flipper.TLI_DeviceInfo_serialNo_get, _filter_flipper.TLI_DeviceInfo_serialNo_set)
    PID = property(_filter_flipper.TLI_DeviceInfo_PID_get, _filter_flipper.TLI_DeviceInfo_PID_set)
    isKnownType = property(_filter_flipper.TLI_DeviceInfo_isKnownType_get, _filter_flipper.TLI_DeviceInfo_isKnownType_set)
    motorType = property(_filter_flipper.TLI_DeviceInfo_motorType_get, _filter_flipper.TLI_DeviceInfo_motorType_set)
    isPiezoDevice = property(_filter_flipper.TLI_DeviceInfo_isPiezoDevice_get, _filter_flipper.TLI_DeviceInfo_isPiezoDevice_set)
    isLaser = property(_filter_flipper.TLI_DeviceInfo_isLaser_get, _filter_flipper.TLI_DeviceInfo_isLaser_set)
    isCustomType = property(_filter_flipper.TLI_DeviceInfo_isCustomType_get, _filter_flipper.TLI_DeviceInfo_isCustomType_set)
    isRack = property(_filter_flipper.TLI_DeviceInfo_isRack_get, _filter_flipper.TLI_DeviceInfo_isRack_set)
    maxChannels = property(_filter_flipper.TLI_DeviceInfo_maxChannels_get, _filter_flipper.TLI_DeviceInfo_maxChannels_set)

    def __init__(self):
        _filter_flipper.TLI_DeviceInfo_swiginit(self, _filter_flipper.new_TLI_DeviceInfo())
    __swig_destroy__ = _filter_flipper.delete_TLI_DeviceInfo

# Register TLI_DeviceInfo in _filter_flipper:
_filter_flipper.TLI_DeviceInfo_swigregister(TLI_DeviceInfo)
class TLI_HardwareInformation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    serialNumber = property(_filter_flipper.TLI_HardwareInformation_serialNumber_get, _filter_flipper.TLI_HardwareInformation_serialNumber_set)
    modelNumber = property(_filter_flipper.TLI_HardwareInformation_modelNumber_get, _filter_flipper.TLI_HardwareInformation_modelNumber_set)
    type = property(_filter_flipper.TLI_HardwareInformation_type_get, _filter_flipper.TLI_HardwareInformation_type_set)
    firmwareVersion = property(_filter_flipper.TLI_HardwareInformation_firmwareVersion_get, _filter_flipper.TLI_HardwareInformation_firmwareVersion_set)
    notes = property(_filter_flipper.TLI_HardwareInformation_notes_get, _filter_flipper.TLI_HardwareInformation_notes_set)
    deviceDependantData = property(_filter_flipper.TLI_HardwareInformation_deviceDependantData_get, _filter_flipper.TLI_HardwareInformation_deviceDependantData_set)
    hardwareVersion = property(_filter_flipper.TLI_HardwareInformation_hardwareVersion_get, _filter_flipper.TLI_HardwareInformation_hardwareVersion_set)
    modificationState = property(_filter_flipper.TLI_HardwareInformation_modificationState_get, _filter_flipper.TLI_HardwareInformation_modificationState_set)
    numChannels = property(_filter_flipper.TLI_HardwareInformation_numChannels_get, _filter_flipper.TLI_HardwareInformation_numChannels_set)

    def __init__(self):
        _filter_flipper.TLI_HardwareInformation_swiginit(self, _filter_flipper.new_TLI_HardwareInformation())
    __swig_destroy__ = _filter_flipper.delete_TLI_HardwareInformation

# Register TLI_HardwareInformation in _filter_flipper:
_filter_flipper.TLI_HardwareInformation_swigregister(TLI_HardwareInformation)
FF_ToggleOnPositiveEdge = _filter_flipper.FF_ToggleOnPositiveEdge
FF_SetPositionOnPositiveEdge = _filter_flipper.FF_SetPositionOnPositiveEdge
FF_OutputHighAtSetPosition = _filter_flipper.FF_OutputHighAtSetPosition
FF_OutputHighWhemMoving = _filter_flipper.FF_OutputHighWhemMoving
FF_InputButton = _filter_flipper.FF_InputButton
FF_InputLogic = _filter_flipper.FF_InputLogic
FF_InputSwap = _filter_flipper.FF_InputSwap
FF_OutputLevel = _filter_flipper.FF_OutputLevel
FF_OutputPulse = _filter_flipper.FF_OutputPulse
FF_OutputSwap = _filter_flipper.FF_OutputSwap
class FF_IOSettings(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    transitTime = property(_filter_flipper.FF_IOSettings_transitTime_get, _filter_flipper.FF_IOSettings_transitTime_set)
    ADCspeedValue = property(_filter_flipper.FF_IOSettings_ADCspeedValue_get, _filter_flipper.FF_IOSettings_ADCspeedValue_set)
    digIO1OperMode = property(_filter_flipper.FF_IOSettings_digIO1OperMode_get, _filter_flipper.FF_IOSettings_digIO1OperMode_set)
    digIO1SignalMode = property(_filter_flipper.FF_IOSettings_digIO1SignalMode_get, _filter_flipper.FF_IOSettings_digIO1SignalMode_set)
    digIO1PulseWidth = property(_filter_flipper.FF_IOSettings_digIO1PulseWidth_get, _filter_flipper.FF_IOSettings_digIO1PulseWidth_set)
    digIO2OperMode = property(_filter_flipper.FF_IOSettings_digIO2OperMode_get, _filter_flipper.FF_IOSettings_digIO2OperMode_set)
    digIO2SignalMode = property(_filter_flipper.FF_IOSettings_digIO2SignalMode_get, _filter_flipper.FF_IOSettings_digIO2SignalMode_set)
    digIO2PulseWidth = property(_filter_flipper.FF_IOSettings_digIO2PulseWidth_get, _filter_flipper.FF_IOSettings_digIO2PulseWidth_set)
    reserved1 = property(_filter_flipper.FF_IOSettings_reserved1_get, _filter_flipper.FF_IOSettings_reserved1_set)
    reserved2 = property(_filter_flipper.FF_IOSettings_reserved2_get, _filter_flipper.FF_IOSettings_reserved2_set)

    def __init__(self):
        _filter_flipper.FF_IOSettings_swiginit(self, _filter_flipper.new_FF_IOSettings())
    __swig_destroy__ = _filter_flipper.delete_FF_IOSettings

# Register FF_IOSettings in _filter_flipper:
_filter_flipper.FF_IOSettings_swigregister(FF_IOSettings)

def TLI_BuildDeviceList():
    return _filter_flipper.TLI_BuildDeviceList()

def TLI_GetDeviceListSize():
    return _filter_flipper.TLI_GetDeviceListSize()

def TLI_GetDeviceList(stringsReceiver):
    return _filter_flipper.TLI_GetDeviceList(stringsReceiver)

def TLI_GetDeviceListByType(stringsReceiver, typeID):
    return _filter_flipper.TLI_GetDeviceListByType(stringsReceiver, typeID)

def TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length):
    return _filter_flipper.TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length)

def TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer):
    return _filter_flipper.TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer)

def TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID):
    return _filter_flipper.TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID)

def TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length):
    return _filter_flipper.TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length)

def TLI_GetDeviceInfo(serialNo, info):
    return _filter_flipper.TLI_GetDeviceInfo(serialNo, info)

def TLI_InitializeSimulations():
    return _filter_flipper.TLI_InitializeSimulations()

def TLI_UninitializeSimulations():
    return _filter_flipper.TLI_UninitializeSimulations()

def FF_Open(serialNo):
    return _filter_flipper.FF_Open(serialNo)

def FF_Close(serialNo):
    return _filter_flipper.FF_Close(serialNo)

def FF_CheckConnection(serialNo):
    return _filter_flipper.FF_CheckConnection(serialNo)

def FF_Identify(serialNo):
    return _filter_flipper.FF_Identify(serialNo)

def FF_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState):
    return _filter_flipper.FF_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState)

def FF_GetFirmwareVersion(serialNo):
    return _filter_flipper.FF_GetFirmwareVersion(serialNo)

def FF_GetSoftwareVersion(serialNo):
    return _filter_flipper.FF_GetSoftwareVersion(serialNo)

def FF_LoadSettings(serialNo):
    return _filter_flipper.FF_LoadSettings(serialNo)

def FF_LoadNamedSettings(serialNo, settingsName):
    return _filter_flipper.FF_LoadNamedSettings(serialNo, settingsName)

def FF_PersistSettings(serialNo):
    return _filter_flipper.FF_PersistSettings(serialNo)

def FF_GetNumberPositions(serialNo):
    return _filter_flipper.FF_GetNumberPositions(serialNo)

def FF_Home(serialNo):
    return _filter_flipper.FF_Home(serialNo)

def FF_MoveToPosition(serialNo, position):
    return _filter_flipper.FF_MoveToPosition(serialNo, position)

def FF_GetPosition(serialNo):
    return _filter_flipper.FF_GetPosition(serialNo)

def FF_GetIOSettings(serialNo, settings):
    return _filter_flipper.FF_GetIOSettings(serialNo, settings)

def FF_RequestIOSettings(serialNo):
    return _filter_flipper.FF_RequestIOSettings(serialNo)

def FF_SetIOSettings(serialNo, settings):
    return _filter_flipper.FF_SetIOSettings(serialNo, settings)

def FF_GetTransitTime(serialNo):
    return _filter_flipper.FF_GetTransitTime(serialNo)

def FF_SetTransitTime(serialNo, transitTime):
    return _filter_flipper.FF_SetTransitTime(serialNo, transitTime)

def FF_RequestStatus(serialNo):
    return _filter_flipper.FF_RequestStatus(serialNo)

def FF_GetStatusBits(serialNo):
    return _filter_flipper.FF_GetStatusBits(serialNo)

def FF_StartPolling(serialNo, milliseconds):
    return _filter_flipper.FF_StartPolling(serialNo, milliseconds)

def FF_PollingDuration(serialNo):
    return _filter_flipper.FF_PollingDuration(serialNo)

def FF_StopPolling(serialNo):
    return _filter_flipper.FF_StopPolling(serialNo)

def FF_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS):
    return _filter_flipper.FF_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS)

def FF_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout):
    return _filter_flipper.FF_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout)

def FF_HasLastMsgTimerOverrun(serialNo):
    return _filter_flipper.FF_HasLastMsgTimerOverrun(serialNo)

def FF_RequestSettings(serialNo):
    return _filter_flipper.FF_RequestSettings(serialNo)

def FF_ClearMessageQueue(serialNo):
    return _filter_flipper.FF_ClearMessageQueue(serialNo)

def FF_RegisterMessageCallback(serialNo, functionPointer):
    return _filter_flipper.FF_RegisterMessageCallback(serialNo, functionPointer)

def FF_MessageQueueSize(serialNo):
    return _filter_flipper.FF_MessageQueueSize(serialNo)

def FF_GetNextMessage(serialNo, messageType, messageID, messageData):
    return _filter_flipper.FF_GetNextMessage(serialNo, messageType, messageID, messageData)

def FF_WaitForMessage(serialNo, messageType, messageID, messageData):
    return _filter_flipper.FF_WaitForMessage(serialNo, messageType, messageID, messageData)
