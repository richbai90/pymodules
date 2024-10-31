# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _laser_diode
else:
    import _laser_diode

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


FT_OK = _laser_diode.FT_OK
FT_InvalidHandle = _laser_diode.FT_InvalidHandle
FT_DeviceNotFound = _laser_diode.FT_DeviceNotFound
FT_DeviceNotOpened = _laser_diode.FT_DeviceNotOpened
FT_IOError = _laser_diode.FT_IOError
FT_InsufficientResources = _laser_diode.FT_InsufficientResources
FT_InvalidParameter = _laser_diode.FT_InvalidParameter
FT_DeviceNotPresent = _laser_diode.FT_DeviceNotPresent
FT_IncorrectDevice = _laser_diode.FT_IncorrectDevice
MOT_NotMotor = _laser_diode.MOT_NotMotor
MOT_DCMotor = _laser_diode.MOT_DCMotor
MOT_StepperMotor = _laser_diode.MOT_StepperMotor
MOT_BrushlessMotor = _laser_diode.MOT_BrushlessMotor
MOT_CustomMotor = _laser_diode.MOT_CustomMotor
class TLI_DeviceInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    typeID = property(_laser_diode.TLI_DeviceInfo_typeID_get, _laser_diode.TLI_DeviceInfo_typeID_set)
    description = property(_laser_diode.TLI_DeviceInfo_description_get, _laser_diode.TLI_DeviceInfo_description_set)
    serialNo = property(_laser_diode.TLI_DeviceInfo_serialNo_get, _laser_diode.TLI_DeviceInfo_serialNo_set)
    PID = property(_laser_diode.TLI_DeviceInfo_PID_get, _laser_diode.TLI_DeviceInfo_PID_set)
    isKnownType = property(_laser_diode.TLI_DeviceInfo_isKnownType_get, _laser_diode.TLI_DeviceInfo_isKnownType_set)
    motorType = property(_laser_diode.TLI_DeviceInfo_motorType_get, _laser_diode.TLI_DeviceInfo_motorType_set)
    isPiezoDevice = property(_laser_diode.TLI_DeviceInfo_isPiezoDevice_get, _laser_diode.TLI_DeviceInfo_isPiezoDevice_set)
    isLaser = property(_laser_diode.TLI_DeviceInfo_isLaser_get, _laser_diode.TLI_DeviceInfo_isLaser_set)
    isCustomType = property(_laser_diode.TLI_DeviceInfo_isCustomType_get, _laser_diode.TLI_DeviceInfo_isCustomType_set)
    isRack = property(_laser_diode.TLI_DeviceInfo_isRack_get, _laser_diode.TLI_DeviceInfo_isRack_set)
    maxChannels = property(_laser_diode.TLI_DeviceInfo_maxChannels_get, _laser_diode.TLI_DeviceInfo_maxChannels_set)

    def __init__(self):
        _laser_diode.TLI_DeviceInfo_swiginit(self, _laser_diode.new_TLI_DeviceInfo())
    __swig_destroy__ = _laser_diode.delete_TLI_DeviceInfo

# Register TLI_DeviceInfo in _laser_diode:
_laser_diode.TLI_DeviceInfo_swigregister(TLI_DeviceInfo)
class TLI_HardwareInformation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    serialNumber = property(_laser_diode.TLI_HardwareInformation_serialNumber_get, _laser_diode.TLI_HardwareInformation_serialNumber_set)
    modelNumber = property(_laser_diode.TLI_HardwareInformation_modelNumber_get, _laser_diode.TLI_HardwareInformation_modelNumber_set)
    type = property(_laser_diode.TLI_HardwareInformation_type_get, _laser_diode.TLI_HardwareInformation_type_set)
    firmwareVersion = property(_laser_diode.TLI_HardwareInformation_firmwareVersion_get, _laser_diode.TLI_HardwareInformation_firmwareVersion_set)
    notes = property(_laser_diode.TLI_HardwareInformation_notes_get, _laser_diode.TLI_HardwareInformation_notes_set)
    deviceDependantData = property(_laser_diode.TLI_HardwareInformation_deviceDependantData_get, _laser_diode.TLI_HardwareInformation_deviceDependantData_set)
    hardwareVersion = property(_laser_diode.TLI_HardwareInformation_hardwareVersion_get, _laser_diode.TLI_HardwareInformation_hardwareVersion_set)
    modificationState = property(_laser_diode.TLI_HardwareInformation_modificationState_get, _laser_diode.TLI_HardwareInformation_modificationState_set)
    numChannels = property(_laser_diode.TLI_HardwareInformation_numChannels_get, _laser_diode.TLI_HardwareInformation_numChannels_set)

    def __init__(self):
        _laser_diode.TLI_HardwareInformation_swiginit(self, _laser_diode.new_TLI_HardwareInformation())
    __swig_destroy__ = _laser_diode.delete_TLI_HardwareInformation

# Register TLI_HardwareInformation in _laser_diode:
_laser_diode.TLI_HardwareInformation_swigregister(TLI_HardwareInformation)
LD_SoftwareOnly = _laser_diode.LD_SoftwareOnly
LD_ExternalSignal = _laser_diode.LD_ExternalSignal
LD_Potentiometer = _laser_diode.LD_Potentiometer
LD_ILim = _laser_diode.LD_ILim
LD_ILD = _laser_diode.LD_ILD
LD_IPD = _laser_diode.LD_IPD
LD_PLD = _laser_diode.LD_PLD
LD_TIA_10uA = _laser_diode.LD_TIA_10uA
LD_TIA_100uA = _laser_diode.LD_TIA_100uA
LD_TIA_1mA = _laser_diode.LD_TIA_1mA
LD_TIA_10mA = _laser_diode.LD_TIA_10mA
LD_CathodeGrounded = _laser_diode.LD_CathodeGrounded
LD_AnodeGrounded = _laser_diode.LD_AnodeGrounded

def TLI_BuildDeviceList():
    return _laser_diode.TLI_BuildDeviceList()

def TLI_GetDeviceListSize():
    return _laser_diode.TLI_GetDeviceListSize()

def TLI_GetDeviceList(stringsReceiver):
    return _laser_diode.TLI_GetDeviceList(stringsReceiver)

def TLI_GetDeviceListByType(stringsReceiver, typeID):
    return _laser_diode.TLI_GetDeviceListByType(stringsReceiver, typeID)

def TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length):
    return _laser_diode.TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length)

def TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer):
    return _laser_diode.TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer)

def TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID):
    return _laser_diode.TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID)

def TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length):
    return _laser_diode.TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length)

def TLI_GetDeviceInfo(serialNo, info):
    return _laser_diode.TLI_GetDeviceInfo(serialNo, info)

def TLI_InitializeSimulations():
    return _laser_diode.TLI_InitializeSimulations()

def TLI_UninitializeSimulations():
    return _laser_diode.TLI_UninitializeSimulations()

def LD_Open(serialNo):
    return _laser_diode.LD_Open(serialNo)

def LD_Close(serialNo):
    return _laser_diode.LD_Close(serialNo)

def LD_CheckConnection(serialNo):
    return _laser_diode.LD_CheckConnection(serialNo)

def LD_Identify(serialNo):
    return _laser_diode.LD_Identify(serialNo)

def LD_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState):
    return _laser_diode.LD_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState)

def LD_GetHardwareInfoBlock(serialNo, hardwareInfo):
    return _laser_diode.LD_GetHardwareInfoBlock(serialNo, hardwareInfo)

def LD_GetFirmwareVersion(serialNo):
    return _laser_diode.LD_GetFirmwareVersion(serialNo)

def LD_GetSoftwareVersion(serialNo):
    return _laser_diode.LD_GetSoftwareVersion(serialNo)

def LD_LoadSettings(serialNo):
    return _laser_diode.LD_LoadSettings(serialNo)

def LD_LoadNamedSettings(serialNo, settingsName):
    return _laser_diode.LD_LoadNamedSettings(serialNo, settingsName)

def LD_PersistSettings(serialNo):
    return _laser_diode.LD_PersistSettings(serialNo)

def LD_Disable(serialNo):
    return _laser_diode.LD_Disable(serialNo)

def LD_Enable(serialNo):
    return _laser_diode.LD_Enable(serialNo)

def LD_ClearMessageQueue(serialNo):
    return _laser_diode.LD_ClearMessageQueue(serialNo)

def LD_RegisterMessageCallback(serialNo, functionPointer):
    return _laser_diode.LD_RegisterMessageCallback(serialNo, functionPointer)

def LD_MessageQueueSize(serialNo):
    return _laser_diode.LD_MessageQueueSize(serialNo)

def LD_GetNextMessage(serialNo, messageType, messageID, messageData):
    return _laser_diode.LD_GetNextMessage(serialNo, messageType, messageID, messageData)

def LD_WaitForMessage(serialNo, messageType, messageID, messageData):
    return _laser_diode.LD_WaitForMessage(serialNo, messageType, messageID, messageData)

def LD_SetOpenLoopMode(serialNo):
    return _laser_diode.LD_SetOpenLoopMode(serialNo)

def LD_SetClosedLoopMode(serialNo):
    return _laser_diode.LD_SetClosedLoopMode(serialNo)

def LD_EnableMaxCurrentAdjust(serialNo, enableAdjust, enableDiode):
    return _laser_diode.LD_EnableMaxCurrentAdjust(serialNo, enableAdjust, enableDiode)

def LD_RequestMaxCurrentDigPot(serialNo):
    return _laser_diode.LD_RequestMaxCurrentDigPot(serialNo)

def LD_SetMaxCurrentDigPot(serialNo, maxCurrent):
    return _laser_diode.LD_SetMaxCurrentDigPot(serialNo, maxCurrent)

def LD_FindTIAGain(serialNo):
    return _laser_diode.LD_FindTIAGain(serialNo)

def LD_EnableTIAGainAdjust(serialNo, enable):
    return _laser_diode.LD_EnableTIAGainAdjust(serialNo, enable)

def LD_DisableOutput(serialNo):
    return _laser_diode.LD_DisableOutput(serialNo)

def LD_EnableOutput(serialNo):
    return _laser_diode.LD_EnableOutput(serialNo)

def LD_RequestControlSource(serialNo):
    return _laser_diode.LD_RequestControlSource(serialNo)

def LD_GetControlSource(serialNo):
    return _laser_diode.LD_GetControlSource(serialNo)

def LD_SetControlSource(serialNo, source):
    return _laser_diode.LD_SetControlSource(serialNo, source)

def LD_GetInterlockState(serialNo):
    return _laser_diode.LD_GetInterlockState(serialNo)

def LD_RequestDisplay(serialNo):
    return _laser_diode.LD_RequestDisplay(serialNo)

def LD_GetDisplayUnits(serialNo):
    return _laser_diode.LD_GetDisplayUnits(serialNo)

def LD_SetDisplayUnits(serialNo, units):
    return _laser_diode.LD_SetDisplayUnits(serialNo, units)

def LD_GetLEDBrightness(serialNo):
    return _laser_diode.LD_GetLEDBrightness(serialNo)

def LD_SetLEDBrightness(serialNo, brightness):
    return _laser_diode.LD_SetLEDBrightness(serialNo, brightness)

def LD_RequestLaserSetPoint(serialNo):
    return _laser_diode.LD_RequestLaserSetPoint(serialNo)

def LD_GetLaserSetPoint(serialNo):
    return _laser_diode.LD_GetLaserSetPoint(serialNo)

def LD_SetLaserSetPoint(serialNo, laserDiodeCurrent):
    return _laser_diode.LD_SetLaserSetPoint(serialNo, laserDiodeCurrent)

def LD_RequestStatus(serialNo):
    return _laser_diode.LD_RequestStatus(serialNo)

def LD_RequestReadings(serialNo):
    return _laser_diode.LD_RequestReadings(serialNo)

def LD_RequestStatusBits(serialNo):
    return _laser_diode.LD_RequestStatusBits(serialNo)

def LD_GetPhotoCurrentReading(serialNo):
    return _laser_diode.LD_GetPhotoCurrentReading(serialNo)

def LD_GetVoltageReading(serialNo):
    return _laser_diode.LD_GetVoltageReading(serialNo)

def LD_GetLaserDiodeCurrentReading(serialNo):
    return _laser_diode.LD_GetLaserDiodeCurrentReading(serialNo)

def LD_RequestLaserDiodeMaxCurrentLimit(serialNo):
    return _laser_diode.LD_RequestLaserDiodeMaxCurrentLimit(serialNo)

def LD_GetLaserDiodeMaxCurrentLimit(serialNo):
    return _laser_diode.LD_GetLaserDiodeMaxCurrentLimit(serialNo)

def LD_RequestWACalibFactor(serialNo):
    return _laser_diode.LD_RequestWACalibFactor(serialNo)

def LD_GetWACalibFactor(serialNo):
    return _laser_diode.LD_GetWACalibFactor(serialNo)

def LD_SetWACalibFactor(serialNo, calibFactor):
    return _laser_diode.LD_SetWACalibFactor(serialNo, calibFactor)

def LD_RequestLaserPolarity(serialNo):
    return _laser_diode.LD_RequestLaserPolarity(serialNo)

def LD_GetLaserPolarity(serialNo):
    return _laser_diode.LD_GetLaserPolarity(serialNo)

def LD_SetLaserPolarity(serialNo, polarity):
    return _laser_diode.LD_SetLaserPolarity(serialNo, polarity)

def LD_GetStatusBits(serialNo):
    return _laser_diode.LD_GetStatusBits(serialNo)

def LD_StartPolling(serialNo, milliseconds):
    return _laser_diode.LD_StartPolling(serialNo, milliseconds)

def LD_PollingDuration(serialNo):
    return _laser_diode.LD_PollingDuration(serialNo)

def LD_StopPolling(serialNo):
    return _laser_diode.LD_StopPolling(serialNo)

def LD_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS):
    return _laser_diode.LD_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS)

def LD_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout):
    return _laser_diode.LD_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout)

def LD_HasLastMsgTimerOverrun(serialNo):
    return _laser_diode.LD_HasLastMsgTimerOverrun(serialNo)

def LD_RequestSettings(serialNo):
    return _laser_diode.LD_RequestSettings(serialNo)

