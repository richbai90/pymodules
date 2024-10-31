# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _inertial_motor
else:
    import _inertial_motor

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


FT_OK = _inertial_motor.FT_OK
FT_InvalidHandle = _inertial_motor.FT_InvalidHandle
FT_DeviceNotFound = _inertial_motor.FT_DeviceNotFound
FT_DeviceNotOpened = _inertial_motor.FT_DeviceNotOpened
FT_IOError = _inertial_motor.FT_IOError
FT_InsufficientResources = _inertial_motor.FT_InsufficientResources
FT_InvalidParameter = _inertial_motor.FT_InvalidParameter
FT_DeviceNotPresent = _inertial_motor.FT_DeviceNotPresent
FT_IncorrectDevice = _inertial_motor.FT_IncorrectDevice
MOT_NotMotor = _inertial_motor.MOT_NotMotor
MOT_DCMotor = _inertial_motor.MOT_DCMotor
MOT_StepperMotor = _inertial_motor.MOT_StepperMotor
MOT_BrushlessMotor = _inertial_motor.MOT_BrushlessMotor
MOT_CustomMotor = _inertial_motor.MOT_CustomMotor
Channel1 = _inertial_motor.Channel1
Channel2 = _inertial_motor.Channel2
Channel3 = _inertial_motor.Channel3
Channel4 = _inertial_motor.Channel4
JogContinuous = _inertial_motor.JogContinuous
JogStep = _inertial_motor.JogStep
Jog = _inertial_motor.Jog
Position = _inertial_motor.Position
Forward = _inertial_motor.Forward
Reverse = _inertial_motor.Reverse
class TIM_DriveOPParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    _maxVoltage = property(_inertial_motor.TIM_DriveOPParameters__maxVoltage_get, _inertial_motor.TIM_DriveOPParameters__maxVoltage_set)
    _stepRate = property(_inertial_motor.TIM_DriveOPParameters__stepRate_get, _inertial_motor.TIM_DriveOPParameters__stepRate_set)
    _stepAcceleration = property(_inertial_motor.TIM_DriveOPParameters__stepAcceleration_get, _inertial_motor.TIM_DriveOPParameters__stepAcceleration_set)

    def __init__(self):
        _inertial_motor.TIM_DriveOPParameters_swiginit(self, _inertial_motor.new_TIM_DriveOPParameters())
    __swig_destroy__ = _inertial_motor.delete_TIM_DriveOPParameters

# Register TIM_DriveOPParameters in _inertial_motor:
_inertial_motor.TIM_DriveOPParameters_swigregister(TIM_DriveOPParameters)
class TIM_JogParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    _jogMode = property(_inertial_motor.TIM_JogParameters__jogMode_get, _inertial_motor.TIM_JogParameters__jogMode_set)
    _jogStepSize = property(_inertial_motor.TIM_JogParameters__jogStepSize_get, _inertial_motor.TIM_JogParameters__jogStepSize_set)
    _jogStepRate = property(_inertial_motor.TIM_JogParameters__jogStepRate_get, _inertial_motor.TIM_JogParameters__jogStepRate_set)
    _jogStepAcceleration = property(_inertial_motor.TIM_JogParameters__jogStepAcceleration_get, _inertial_motor.TIM_JogParameters__jogStepAcceleration_set)

    def __init__(self):
        _inertial_motor.TIM_JogParameters_swiginit(self, _inertial_motor.new_TIM_JogParameters())
    __swig_destroy__ = _inertial_motor.delete_TIM_JogParameters

# Register TIM_JogParameters in _inertial_motor:
_inertial_motor.TIM_JogParameters_swigregister(TIM_JogParameters)
class TIM_ButtonParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    _buttonMode = property(_inertial_motor.TIM_ButtonParameters__buttonMode_get, _inertial_motor.TIM_ButtonParameters__buttonMode_set)
    _position1 = property(_inertial_motor.TIM_ButtonParameters__position1_get, _inertial_motor.TIM_ButtonParameters__position1_set)
    _position2 = property(_inertial_motor.TIM_ButtonParameters__position2_get, _inertial_motor.TIM_ButtonParameters__position2_set)
    _reserved = property(_inertial_motor.TIM_ButtonParameters__reserved_get, _inertial_motor.TIM_ButtonParameters__reserved_set)

    def __init__(self):
        _inertial_motor.TIM_ButtonParameters_swiginit(self, _inertial_motor.new_TIM_ButtonParameters())
    __swig_destroy__ = _inertial_motor.delete_TIM_ButtonParameters

# Register TIM_ButtonParameters in _inertial_motor:
_inertial_motor.TIM_ButtonParameters_swigregister(TIM_ButtonParameters)
class TIM_Status(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    _position = property(_inertial_motor.TIM_Status__position_get, _inertial_motor.TIM_Status__position_set)
    _encoderCount = property(_inertial_motor.TIM_Status__encoderCount_get, _inertial_motor.TIM_Status__encoderCount_set)
    _statusBits = property(_inertial_motor.TIM_Status__statusBits_get, _inertial_motor.TIM_Status__statusBits_set)

    def __init__(self):
        _inertial_motor.TIM_Status_swiginit(self, _inertial_motor.new_TIM_Status())
    __swig_destroy__ = _inertial_motor.delete_TIM_Status

# Register TIM_Status in _inertial_motor:
_inertial_motor.TIM_Status_swigregister(TIM_Status)
class TLI_DeviceInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    typeID = property(_inertial_motor.TLI_DeviceInfo_typeID_get, _inertial_motor.TLI_DeviceInfo_typeID_set)
    description = property(_inertial_motor.TLI_DeviceInfo_description_get, _inertial_motor.TLI_DeviceInfo_description_set)
    serialNo = property(_inertial_motor.TLI_DeviceInfo_serialNo_get, _inertial_motor.TLI_DeviceInfo_serialNo_set)
    PID = property(_inertial_motor.TLI_DeviceInfo_PID_get, _inertial_motor.TLI_DeviceInfo_PID_set)
    isKnownType = property(_inertial_motor.TLI_DeviceInfo_isKnownType_get, _inertial_motor.TLI_DeviceInfo_isKnownType_set)
    motorType = property(_inertial_motor.TLI_DeviceInfo_motorType_get, _inertial_motor.TLI_DeviceInfo_motorType_set)
    isPiezoDevice = property(_inertial_motor.TLI_DeviceInfo_isPiezoDevice_get, _inertial_motor.TLI_DeviceInfo_isPiezoDevice_set)
    isLaser = property(_inertial_motor.TLI_DeviceInfo_isLaser_get, _inertial_motor.TLI_DeviceInfo_isLaser_set)
    isCustomType = property(_inertial_motor.TLI_DeviceInfo_isCustomType_get, _inertial_motor.TLI_DeviceInfo_isCustomType_set)
    isRack = property(_inertial_motor.TLI_DeviceInfo_isRack_get, _inertial_motor.TLI_DeviceInfo_isRack_set)
    maxChannels = property(_inertial_motor.TLI_DeviceInfo_maxChannels_get, _inertial_motor.TLI_DeviceInfo_maxChannels_set)

    def __init__(self):
        _inertial_motor.TLI_DeviceInfo_swiginit(self, _inertial_motor.new_TLI_DeviceInfo())
    __swig_destroy__ = _inertial_motor.delete_TLI_DeviceInfo

# Register TLI_DeviceInfo in _inertial_motor:
_inertial_motor.TLI_DeviceInfo_swigregister(TLI_DeviceInfo)
class TLI_HardwareInformation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    serialNumber = property(_inertial_motor.TLI_HardwareInformation_serialNumber_get, _inertial_motor.TLI_HardwareInformation_serialNumber_set)
    modelNumber = property(_inertial_motor.TLI_HardwareInformation_modelNumber_get, _inertial_motor.TLI_HardwareInformation_modelNumber_set)
    type = property(_inertial_motor.TLI_HardwareInformation_type_get, _inertial_motor.TLI_HardwareInformation_type_set)
    firmwareVersion = property(_inertial_motor.TLI_HardwareInformation_firmwareVersion_get, _inertial_motor.TLI_HardwareInformation_firmwareVersion_set)
    notes = property(_inertial_motor.TLI_HardwareInformation_notes_get, _inertial_motor.TLI_HardwareInformation_notes_set)
    deviceDependantData = property(_inertial_motor.TLI_HardwareInformation_deviceDependantData_get, _inertial_motor.TLI_HardwareInformation_deviceDependantData_set)
    hardwareVersion = property(_inertial_motor.TLI_HardwareInformation_hardwareVersion_get, _inertial_motor.TLI_HardwareInformation_hardwareVersion_set)
    modificationState = property(_inertial_motor.TLI_HardwareInformation_modificationState_get, _inertial_motor.TLI_HardwareInformation_modificationState_set)
    numChannels = property(_inertial_motor.TLI_HardwareInformation_numChannels_get, _inertial_motor.TLI_HardwareInformation_numChannels_set)

    def __init__(self):
        _inertial_motor.TLI_HardwareInformation_swiginit(self, _inertial_motor.new_TLI_HardwareInformation())
    __swig_destroy__ = _inertial_motor.delete_TLI_HardwareInformation

# Register TLI_HardwareInformation in _inertial_motor:
_inertial_motor.TLI_HardwareInformation_swigregister(TLI_HardwareInformation)

def TLI_BuildDeviceList():
    return _inertial_motor.TLI_BuildDeviceList()

def TLI_GetDeviceListSize():
    return _inertial_motor.TLI_GetDeviceListSize()

def TLI_GetDeviceList(stringsReceiver):
    return _inertial_motor.TLI_GetDeviceList(stringsReceiver)

def TLI_GetDeviceListByType(stringsReceiver, typeID):
    return _inertial_motor.TLI_GetDeviceListByType(stringsReceiver, typeID)

def TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length):
    return _inertial_motor.TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length)

def TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer):
    return _inertial_motor.TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer)

def TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID):
    return _inertial_motor.TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID)

def TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length):
    return _inertial_motor.TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length)

def TLI_GetDeviceInfo(serialNo, info):
    return _inertial_motor.TLI_GetDeviceInfo(serialNo, info)

def TLI_InitializeSimulations():
    return _inertial_motor.TLI_InitializeSimulations()

def TLI_UninitializeSimulations():
    return _inertial_motor.TLI_UninitializeSimulations()

def TIM_Open(serialNo):
    return _inertial_motor.TIM_Open(serialNo)

def TIM_Close(serialNo):
    return _inertial_motor.TIM_Close(serialNo)

def TIM_CheckConnection(serialNo):
    return _inertial_motor.TIM_CheckConnection(serialNo)

def TIM_Identify(serialNo):
    return _inertial_motor.TIM_Identify(serialNo)

def TIM_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState):
    return _inertial_motor.TIM_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState)

def TIM_GetHardwareInfoBlock(serialNo, hardwareInfo):
    return _inertial_motor.TIM_GetHardwareInfoBlock(serialNo, hardwareInfo)

def TIM_GetFirmwareVersion(serialNo):
    return _inertial_motor.TIM_GetFirmwareVersion(serialNo)

def TIM_GetSoftwareVersion(serialNo):
    return _inertial_motor.TIM_GetSoftwareVersion(serialNo)

def TIM_LoadSettings(serialNo):
    return _inertial_motor.TIM_LoadSettings(serialNo)

def TIM_LoadNamedSettings(serialNo, settingsName):
    return _inertial_motor.TIM_LoadNamedSettings(serialNo, settingsName)

def TIM_PersistSettings(serialNo):
    return _inertial_motor.TIM_PersistSettings(serialNo)

def TIM_Disable(serialNo):
    return _inertial_motor.TIM_Disable(serialNo)

def TIM_Enable(serialNo):
    return _inertial_motor.TIM_Enable(serialNo)

def TIM_Reset(serialNo):
    return _inertial_motor.TIM_Reset(serialNo)

def TIM_Disconnect(serialNo):
    return _inertial_motor.TIM_Disconnect(serialNo)

def TIM_ClearMessageQueue(serialNo):
    return _inertial_motor.TIM_ClearMessageQueue(serialNo)

def TIM_RegisterMessageCallback(serialNo, functionPointer):
    return _inertial_motor.TIM_RegisterMessageCallback(serialNo, functionPointer)

def TIM_MessageQueueSize(serialNo):
    return _inertial_motor.TIM_MessageQueueSize(serialNo)

def TIM_GetNextMessage(serialNo, messageType, messageID, messageData):
    return _inertial_motor.TIM_GetNextMessage(serialNo, messageType, messageID, messageData)

def TIM_WaitForMessage(serialNo, messageType, messageID, messageData):
    return _inertial_motor.TIM_WaitForMessage(serialNo, messageType, messageID, messageData)

def TIM_Home(serialNo, channel):
    return _inertial_motor.TIM_Home(serialNo, channel)

def TIM_SetPosition(serialNo, channel, position):
    return _inertial_motor.TIM_SetPosition(serialNo, channel, position)

def TIM_MoveAbsolute(serialNo, channel, position):
    return _inertial_motor.TIM_MoveAbsolute(serialNo, channel, position)

def TIM_MoveJog(serialNo, channel, jogDirection):
    return _inertial_motor.TIM_MoveJog(serialNo, channel, jogDirection)

def TIM_MoveStop(serialNo, channel):
    return _inertial_motor.TIM_MoveStop(serialNo, channel)

def TIM_RequestDriveOPParameters(serialNo, channel):
    return _inertial_motor.TIM_RequestDriveOPParameters(serialNo, channel)

def TIM_SetDriveOPParameters(serialNo, channel, maxVoltage, stepRate, stepAcceleration):
    return _inertial_motor.TIM_SetDriveOPParameters(serialNo, channel, maxVoltage, stepRate, stepAcceleration)

def TIM_GetDriveOPParameters(serialNo, channel, maxVoltage, stepRate, stepAcceleration):
    return _inertial_motor.TIM_GetDriveOPParameters(serialNo, channel, maxVoltage, stepRate, stepAcceleration)

def TIM_SetDriveOPParametersStruct(serialNo, channel, driveOPParameters):
    return _inertial_motor.TIM_SetDriveOPParametersStruct(serialNo, channel, driveOPParameters)

def TIM_GetDriveOPParametersStruct(serialNo, channel, driveOPParameters):
    return _inertial_motor.TIM_GetDriveOPParametersStruct(serialNo, channel, driveOPParameters)

def TIM_RequestJogParameters(serialNo, channel):
    return _inertial_motor.TIM_RequestJogParameters(serialNo, channel)

def TIM_SetJogParameters(serialNo, channel, jogMode, jogStepSize, jogStepRate, jogStepAcceleration):
    return _inertial_motor.TIM_SetJogParameters(serialNo, channel, jogMode, jogStepSize, jogStepRate, jogStepAcceleration)

def TIM_GetJogParameters(serialNo, channel, jogMode, jogStepSize, jogStepRate, jogStepAcceleration):
    return _inertial_motor.TIM_GetJogParameters(serialNo, channel, jogMode, jogStepSize, jogStepRate, jogStepAcceleration)

def TIM_SetJogParametersStruct(serialNo, channel, jogParameters):
    return _inertial_motor.TIM_SetJogParametersStruct(serialNo, channel, jogParameters)

def TIM_GetJogParametersStruct(serialNo, channel, jogParameters):
    return _inertial_motor.TIM_GetJogParametersStruct(serialNo, channel, jogParameters)

def TIM_RequestButtonParameters(serialNo, channel):
    return _inertial_motor.TIM_RequestButtonParameters(serialNo, channel)

def TIM_SetButtonParameters(serialNo, channel, buttonMode, position1, position2):
    return _inertial_motor.TIM_SetButtonParameters(serialNo, channel, buttonMode, position1, position2)

def TIM_GetButtonParameters(serialNo, channel, buttonMode, position1, position2):
    return _inertial_motor.TIM_GetButtonParameters(serialNo, channel, buttonMode, position1, position2)

def TIM_SetButtonParametersStruct(serialNo, channel, buttonParameters):
    return _inertial_motor.TIM_SetButtonParametersStruct(serialNo, channel, buttonParameters)

def TIM_GetButtonParametersStruct(serialNo, channel, buttonParameters):
    return _inertial_motor.TIM_GetButtonParametersStruct(serialNo, channel, buttonParameters)

def TIM_SetMaxPotStepRate(serialNo, channel, maxPotStepRate):
    return _inertial_motor.TIM_SetMaxPotStepRate(serialNo, channel, maxPotStepRate)

def TIM_RequestMaxPotStepRate(serialNo, channel):
    return _inertial_motor.TIM_RequestMaxPotStepRate(serialNo, channel)

def TIM_GetMaxPotStepRate(serialNo, channel):
    return _inertial_motor.TIM_GetMaxPotStepRate(serialNo, channel)

def TIM_GetLEDBrightness(serialNo):
    return _inertial_motor.TIM_GetLEDBrightness(serialNo)

def TIM_SetLEDBrightness(serialNo, brightness):
    return _inertial_motor.TIM_SetLEDBrightness(serialNo, brightness)

def TIM_RequestStatus(serialNo):
    return _inertial_motor.TIM_RequestStatus(serialNo)

def TIM_RequestStatusBits(serialNo):
    return _inertial_motor.TIM_RequestStatusBits(serialNo)

def TIM_RequestCurrentPosition(serialNo, channel):
    return _inertial_motor.TIM_RequestCurrentPosition(serialNo, channel)

def TIM_GetCurrentPosition(serialNo, channel):
    return _inertial_motor.TIM_GetCurrentPosition(serialNo, channel)

def TIM_GetStatusBits(serialNo, channel):
    return _inertial_motor.TIM_GetStatusBits(serialNo, channel)

def TIM_StartPolling(serialNo, milliseconds):
    return _inertial_motor.TIM_StartPolling(serialNo, milliseconds)

def TIM_PollingDuration(serialNo):
    return _inertial_motor.TIM_PollingDuration(serialNo)

def TIM_StopPolling(serialNo):
    return _inertial_motor.TIM_StopPolling(serialNo)

def TIM_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS):
    return _inertial_motor.TIM_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS)

def TIM_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout):
    return _inertial_motor.TIM_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout)

def TIM_HasLastMsgTimerOverrun(serialNo):
    return _inertial_motor.TIM_HasLastMsgTimerOverrun(serialNo)

def TIM_RequestSettings(serialNo):
    return _inertial_motor.TIM_RequestSettings(serialNo)
