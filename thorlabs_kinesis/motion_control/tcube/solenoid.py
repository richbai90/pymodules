# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _solenoid
else:
    import _solenoid

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


FT_OK = _solenoid.FT_OK
FT_InvalidHandle = _solenoid.FT_InvalidHandle
FT_DeviceNotFound = _solenoid.FT_DeviceNotFound
FT_DeviceNotOpened = _solenoid.FT_DeviceNotOpened
FT_IOError = _solenoid.FT_IOError
FT_InsufficientResources = _solenoid.FT_InsufficientResources
FT_InvalidParameter = _solenoid.FT_InvalidParameter
FT_DeviceNotPresent = _solenoid.FT_DeviceNotPresent
FT_IncorrectDevice = _solenoid.FT_IncorrectDevice
MOT_NotMotor = _solenoid.MOT_NotMotor
MOT_DCMotor = _solenoid.MOT_DCMotor
MOT_StepperMotor = _solenoid.MOT_StepperMotor
MOT_BrushlessMotor = _solenoid.MOT_BrushlessMotor
MOT_CustomMotor = _solenoid.MOT_CustomMotor
class TLI_DeviceInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    typeID = property(_solenoid.TLI_DeviceInfo_typeID_get, _solenoid.TLI_DeviceInfo_typeID_set)
    description = property(_solenoid.TLI_DeviceInfo_description_get, _solenoid.TLI_DeviceInfo_description_set)
    serialNo = property(_solenoid.TLI_DeviceInfo_serialNo_get, _solenoid.TLI_DeviceInfo_serialNo_set)
    PID = property(_solenoid.TLI_DeviceInfo_PID_get, _solenoid.TLI_DeviceInfo_PID_set)
    isKnownType = property(_solenoid.TLI_DeviceInfo_isKnownType_get, _solenoid.TLI_DeviceInfo_isKnownType_set)
    motorType = property(_solenoid.TLI_DeviceInfo_motorType_get, _solenoid.TLI_DeviceInfo_motorType_set)
    isPiezoDevice = property(_solenoid.TLI_DeviceInfo_isPiezoDevice_get, _solenoid.TLI_DeviceInfo_isPiezoDevice_set)
    isLaser = property(_solenoid.TLI_DeviceInfo_isLaser_get, _solenoid.TLI_DeviceInfo_isLaser_set)
    isCustomType = property(_solenoid.TLI_DeviceInfo_isCustomType_get, _solenoid.TLI_DeviceInfo_isCustomType_set)
    isRack = property(_solenoid.TLI_DeviceInfo_isRack_get, _solenoid.TLI_DeviceInfo_isRack_set)
    maxChannels = property(_solenoid.TLI_DeviceInfo_maxChannels_get, _solenoid.TLI_DeviceInfo_maxChannels_set)

    def __init__(self):
        _solenoid.TLI_DeviceInfo_swiginit(self, _solenoid.new_TLI_DeviceInfo())
    __swig_destroy__ = _solenoid.delete_TLI_DeviceInfo

# Register TLI_DeviceInfo in _solenoid:
_solenoid.TLI_DeviceInfo_swigregister(TLI_DeviceInfo)
class TLI_HardwareInformation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    serialNumber = property(_solenoid.TLI_HardwareInformation_serialNumber_get, _solenoid.TLI_HardwareInformation_serialNumber_set)
    modelNumber = property(_solenoid.TLI_HardwareInformation_modelNumber_get, _solenoid.TLI_HardwareInformation_modelNumber_set)
    type = property(_solenoid.TLI_HardwareInformation_type_get, _solenoid.TLI_HardwareInformation_type_set)
    firmwareVersion = property(_solenoid.TLI_HardwareInformation_firmwareVersion_get, _solenoid.TLI_HardwareInformation_firmwareVersion_set)
    notes = property(_solenoid.TLI_HardwareInformation_notes_get, _solenoid.TLI_HardwareInformation_notes_set)
    deviceDependantData = property(_solenoid.TLI_HardwareInformation_deviceDependantData_get, _solenoid.TLI_HardwareInformation_deviceDependantData_set)
    hardwareVersion = property(_solenoid.TLI_HardwareInformation_hardwareVersion_get, _solenoid.TLI_HardwareInformation_hardwareVersion_set)
    modificationState = property(_solenoid.TLI_HardwareInformation_modificationState_get, _solenoid.TLI_HardwareInformation_modificationState_set)
    numChannels = property(_solenoid.TLI_HardwareInformation_numChannels_get, _solenoid.TLI_HardwareInformation_numChannels_set)

    def __init__(self):
        _solenoid.TLI_HardwareInformation_swiginit(self, _solenoid.new_TLI_HardwareInformation())
    __swig_destroy__ = _solenoid.delete_TLI_HardwareInformation

# Register TLI_HardwareInformation in _solenoid:
_solenoid.TLI_HardwareInformation_swigregister(TLI_HardwareInformation)
class SC_CycleParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    openTime = property(_solenoid.SC_CycleParameters_openTime_get, _solenoid.SC_CycleParameters_openTime_set)
    closedTime = property(_solenoid.SC_CycleParameters_closedTime_get, _solenoid.SC_CycleParameters_closedTime_set)
    numCycles = property(_solenoid.SC_CycleParameters_numCycles_get, _solenoid.SC_CycleParameters_numCycles_set)

    def __init__(self):
        _solenoid.SC_CycleParameters_swiginit(self, _solenoid.new_SC_CycleParameters())
    __swig_destroy__ = _solenoid.delete_SC_CycleParameters

# Register SC_CycleParameters in _solenoid:
_solenoid.SC_CycleParameters_swigregister(SC_CycleParameters)
SC_Manual = _solenoid.SC_Manual
SC_Single = _solenoid.SC_Single
SC_Auto = _solenoid.SC_Auto
SC_Triggered = _solenoid.SC_Triggered
SC_Active = _solenoid.SC_Active
SC_Inactive = _solenoid.SC_Inactive
SC_SolenoidOpen = _solenoid.SC_SolenoidOpen
SC_SolenoidClosed = _solenoid.SC_SolenoidClosed

def TLI_BuildDeviceList():
    return _solenoid.TLI_BuildDeviceList()

def TLI_GetDeviceListSize():
    return _solenoid.TLI_GetDeviceListSize()

def TLI_GetDeviceList(stringsReceiver):
    return _solenoid.TLI_GetDeviceList(stringsReceiver)

def TLI_GetDeviceListByType(stringsReceiver, typeID):
    return _solenoid.TLI_GetDeviceListByType(stringsReceiver, typeID)

def TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length):
    return _solenoid.TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length)

def TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer):
    return _solenoid.TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer)

def TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID):
    return _solenoid.TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID)

def TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length):
    return _solenoid.TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length)

def TLI_GetDeviceInfo(serialNo, info):
    return _solenoid.TLI_GetDeviceInfo(serialNo, info)

def TLI_InitializeSimulations():
    return _solenoid.TLI_InitializeSimulations()

def TLI_UninitializeSimulations():
    return _solenoid.TLI_UninitializeSimulations()

def SC_Open(serialNo):
    return _solenoid.SC_Open(serialNo)

def SC_Close(serialNo):
    return _solenoid.SC_Close(serialNo)

def SC_CheckConnection(serialNo):
    return _solenoid.SC_CheckConnection(serialNo)

def SC_Identify(serialNo):
    return _solenoid.SC_Identify(serialNo)

def SC_RequestLEDswitches(serialNo):
    return _solenoid.SC_RequestLEDswitches(serialNo)

def SC_GetLEDswitches(serialNo):
    return _solenoid.SC_GetLEDswitches(serialNo)

def SC_SetLEDswitches(serialNo, LEDswitches):
    return _solenoid.SC_SetLEDswitches(serialNo, LEDswitches)

def SC_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState):
    return _solenoid.SC_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState)

def SC_GetHardwareInfoBlock(serialNo, hardwareInfo):
    return _solenoid.SC_GetHardwareInfoBlock(serialNo, hardwareInfo)

def SC_RequestHubBay(serialNo):
    return _solenoid.SC_RequestHubBay(serialNo)

def SC_GetHubBay(serialNo):
    return _solenoid.SC_GetHubBay(serialNo)

def SC_GetSoftwareVersion(serialNo):
    return _solenoid.SC_GetSoftwareVersion(serialNo)

def SC_LoadSettings(serialNo):
    return _solenoid.SC_LoadSettings(serialNo)

def SC_LoadNamedSettings(serialNo, settingsName):
    return _solenoid.SC_LoadNamedSettings(serialNo, settingsName)

def SC_PersistSettings(serialNo):
    return _solenoid.SC_PersistSettings(serialNo)

def SC_ClearMessageQueue(serialNo):
    return _solenoid.SC_ClearMessageQueue(serialNo)

def SC_RegisterMessageCallback(serialNo, functionPointer):
    return _solenoid.SC_RegisterMessageCallback(serialNo, functionPointer)

def SC_MessageQueueSize(serialNo):
    return _solenoid.SC_MessageQueueSize(serialNo)

def SC_GetNextMessage(serialNo, messageType, messageID, messageData):
    return _solenoid.SC_GetNextMessage(serialNo, messageType, messageID, messageData)

def SC_WaitForMessage(serialNo, messageType, messageID, messageData):
    return _solenoid.SC_WaitForMessage(serialNo, messageType, messageID, messageData)

def SC_StartPolling(serialNo, milliseconds):
    return _solenoid.SC_StartPolling(serialNo, milliseconds)

def SC_PollingDuration(serialNo):
    return _solenoid.SC_PollingDuration(serialNo)

def SC_StopPolling(serialNo):
    return _solenoid.SC_StopPolling(serialNo)

def SC_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS):
    return _solenoid.SC_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS)

def SC_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout):
    return _solenoid.SC_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout)

def SC_HasLastMsgTimerOverrun(serialNo):
    return _solenoid.SC_HasLastMsgTimerOverrun(serialNo)

def SC_RequestSettings(serialNo):
    return _solenoid.SC_RequestSettings(serialNo)

def SC_RequestStatus(serialNo):
    return _solenoid.SC_RequestStatus(serialNo)

def SC_RequestStatusBits(serialNo):
    return _solenoid.SC_RequestStatusBits(serialNo)

def SC_GetStatusBits(serialNo):
    return _solenoid.SC_GetStatusBits(serialNo)

def SC_RequestOperatingMode(serialNo):
    return _solenoid.SC_RequestOperatingMode(serialNo)

def SC_GetOperatingMode(serialNo):
    return _solenoid.SC_GetOperatingMode(serialNo)

def SC_SetOperatingMode(serialNo, mode):
    return _solenoid.SC_SetOperatingMode(serialNo, mode)

def SC_GetSolenoidState(serialNo):
    return _solenoid.SC_GetSolenoidState(serialNo)

def SC_RequestOperatingState(serialNo):
    return _solenoid.SC_RequestOperatingState(serialNo)

def SC_GetOperatingState(serialNo):
    return _solenoid.SC_GetOperatingState(serialNo)

def SC_SetOperatingState(serialNo, state):
    return _solenoid.SC_SetOperatingState(serialNo, state)

def SC_RequestCycleParams(serialNo):
    return _solenoid.SC_RequestCycleParams(serialNo)

def SC_GetCycleParams(serialNo, pOpenTime, pClosedTime, numCycles):
    return _solenoid.SC_GetCycleParams(serialNo, pOpenTime, pClosedTime, numCycles)

def SC_SetCycleParams(serialNo, openTime, closedTime, numCycles):
    return _solenoid.SC_SetCycleParams(serialNo, openTime, closedTime, numCycles)

def SC_GetCycleParamsBlock(serialNo, cycleParams):
    return _solenoid.SC_GetCycleParamsBlock(serialNo, cycleParams)

def SC_SetCycleParamsBlock(serialNo, cycleParams):
    return _solenoid.SC_SetCycleParamsBlock(serialNo, cycleParams)

