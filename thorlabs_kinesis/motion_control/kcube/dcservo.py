# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _dcservo
else:
    import _dcservo

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


FT_OK = _dcservo.FT_OK
FT_InvalidHandle = _dcservo.FT_InvalidHandle
FT_DeviceNotFound = _dcservo.FT_DeviceNotFound
FT_DeviceNotOpened = _dcservo.FT_DeviceNotOpened
FT_IOError = _dcservo.FT_IOError
FT_InsufficientResources = _dcservo.FT_InsufficientResources
FT_InvalidParameter = _dcservo.FT_InvalidParameter
FT_DeviceNotPresent = _dcservo.FT_DeviceNotPresent
FT_IncorrectDevice = _dcservo.FT_IncorrectDevice
MOT_NotMotor = _dcservo.MOT_NotMotor
MOT_DCMotor = _dcservo.MOT_DCMotor
MOT_StepperMotor = _dcservo.MOT_StepperMotor
MOT_BrushlessMotor = _dcservo.MOT_BrushlessMotor
MOT_CustomMotor = _dcservo.MOT_CustomMotor
MOT_TravelModeUndefined = _dcservo.MOT_TravelModeUndefined
MOT_Linear = _dcservo.MOT_Linear
MOT_Rotational = _dcservo.MOT_Rotational
MOT_TravelDirectionUndefined = _dcservo.MOT_TravelDirectionUndefined
MOT_Forwards = _dcservo.MOT_Forwards
MOT_Backwards = _dcservo.MOT_Backwards
MOT_LimitSwitchDirectionUndefined = _dcservo.MOT_LimitSwitchDirectionUndefined
MOT_ReverseLimitSwitch = _dcservo.MOT_ReverseLimitSwitch
MOT_ForwardLimitSwitch = _dcservo.MOT_ForwardLimitSwitch
MOT_Normal = _dcservo.MOT_Normal
MOT_Reverse = _dcservo.MOT_Reverse
MOT_JogModeUndefined = _dcservo.MOT_JogModeUndefined
MOT_Continuous = _dcservo.MOT_Continuous
MOT_SingleStep = _dcservo.MOT_SingleStep
MOT_StopModeUndefined = _dcservo.MOT_StopModeUndefined
MOT_Immediate = _dcservo.MOT_Immediate
MOT_Profiled = _dcservo.MOT_Profiled
MOT_LimitSwitchModeUndefined = _dcservo.MOT_LimitSwitchModeUndefined
MOT_LimitSwitchIgnoreSwitch = _dcservo.MOT_LimitSwitchIgnoreSwitch
MOT_LimitSwitchMakeOnContact = _dcservo.MOT_LimitSwitchMakeOnContact
MOT_LimitSwitchBreakOnContact = _dcservo.MOT_LimitSwitchBreakOnContact
MOT_LimitSwitchMakeOnHome = _dcservo.MOT_LimitSwitchMakeOnHome
MOT_LimitSwitchBreakOnHome = _dcservo.MOT_LimitSwitchBreakOnHome
MOT_PMD_Reserved = _dcservo.MOT_PMD_Reserved
MOT_LimitSwitchIgnoreSwitchSwapped = _dcservo.MOT_LimitSwitchIgnoreSwitchSwapped
MOT_LimitSwitchMakeOnContactSwapped = _dcservo.MOT_LimitSwitchMakeOnContactSwapped
MOT_LimitSwitchBreakOnContactSwapped = _dcservo.MOT_LimitSwitchBreakOnContactSwapped
MOT_LimitSwitchMakeOnHomeSwapped = _dcservo.MOT_LimitSwitchMakeOnHomeSwapped
MOT_LimitSwitchBreakOnHomeSwapped = _dcservo.MOT_LimitSwitchBreakOnHomeSwapped
MOT_LimitSwitchSWModeUndefined = _dcservo.MOT_LimitSwitchSWModeUndefined
MOT_LimitSwitchIgnored = _dcservo.MOT_LimitSwitchIgnored
MOT_LimitSwitchStopImmediate = _dcservo.MOT_LimitSwitchStopImmediate
MOT_LimitSwitchStopProfiled = _dcservo.MOT_LimitSwitchStopProfiled
MOT_LimitSwitchIgnored_Rotational = _dcservo.MOT_LimitSwitchIgnored_Rotational
MOT_LimitSwitchStopImmediate_Rotational = _dcservo.MOT_LimitSwitchStopImmediate_Rotational
MOT_LimitSwitchStopProfiled_Rotational = _dcservo.MOT_LimitSwitchStopProfiled_Rotational
DisallowIllegalMoves = _dcservo.DisallowIllegalMoves
AllowPartialMoves = _dcservo.AllowPartialMoves
AllowAllMoves = _dcservo.AllowAllMoves
KMOT_WM_Positive = _dcservo.KMOT_WM_Positive
KMOT_WM_Negative = _dcservo.KMOT_WM_Negative
KMOT_WM_Velocity = _dcservo.KMOT_WM_Velocity
KMOT_WM_Jog = _dcservo.KMOT_WM_Jog
KMOT_WM_MoveAbsolute = _dcservo.KMOT_WM_MoveAbsolute
KMOT_TrigDisabled = _dcservo.KMOT_TrigDisabled
KMOT_TrigIn_GPI = _dcservo.KMOT_TrigIn_GPI
KMOT_TrigIn_RelativeMove = _dcservo.KMOT_TrigIn_RelativeMove
KMOT_TrigIn_AbsoluteMove = _dcservo.KMOT_TrigIn_AbsoluteMove
KMOT_TrigIn_Home = _dcservo.KMOT_TrigIn_Home
KMOT_TrigIn_Stop = _dcservo.KMOT_TrigIn_Stop
KMOT_TrigIn_StartScan = _dcservo.KMOT_TrigIn_StartScan
KMOT_TrigIn_ShuttleMove = _dcservo.KMOT_TrigIn_ShuttleMove
KMOT_TrigOut_GPO = _dcservo.KMOT_TrigOut_GPO
KMOT_TrigOut_InMotion = _dcservo.KMOT_TrigOut_InMotion
KMOT_TrigOut_AtMaxVelocity = _dcservo.KMOT_TrigOut_AtMaxVelocity
KMOT_TrigOut_AtPositionSteps = _dcservo.KMOT_TrigOut_AtPositionSteps
KMOT_TrigOut_Synch = _dcservo.KMOT_TrigOut_Synch
KMOT_TrigPolarityHigh = _dcservo.KMOT_TrigPolarityHigh
KMOT_TrigPolarityLow = _dcservo.KMOT_TrigPolarityLow
LinearRange = _dcservo.LinearRange
RotationalUnlimited = _dcservo.RotationalUnlimited
RotationalWrapping = _dcservo.RotationalWrapping
Quickest = _dcservo.Quickest
Forwards = _dcservo.Forwards
Reverse = _dcservo.Reverse
class TLI_DeviceInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    typeID = property(_dcservo.TLI_DeviceInfo_typeID_get, _dcservo.TLI_DeviceInfo_typeID_set)
    description = property(_dcservo.TLI_DeviceInfo_description_get, _dcservo.TLI_DeviceInfo_description_set)
    serialNo = property(_dcservo.TLI_DeviceInfo_serialNo_get, _dcservo.TLI_DeviceInfo_serialNo_set)
    PID = property(_dcservo.TLI_DeviceInfo_PID_get, _dcservo.TLI_DeviceInfo_PID_set)
    isKnownType = property(_dcservo.TLI_DeviceInfo_isKnownType_get, _dcservo.TLI_DeviceInfo_isKnownType_set)
    motorType = property(_dcservo.TLI_DeviceInfo_motorType_get, _dcservo.TLI_DeviceInfo_motorType_set)
    isPiezoDevice = property(_dcservo.TLI_DeviceInfo_isPiezoDevice_get, _dcservo.TLI_DeviceInfo_isPiezoDevice_set)
    isLaser = property(_dcservo.TLI_DeviceInfo_isLaser_get, _dcservo.TLI_DeviceInfo_isLaser_set)
    isCustomType = property(_dcservo.TLI_DeviceInfo_isCustomType_get, _dcservo.TLI_DeviceInfo_isCustomType_set)
    isRack = property(_dcservo.TLI_DeviceInfo_isRack_get, _dcservo.TLI_DeviceInfo_isRack_set)
    maxChannels = property(_dcservo.TLI_DeviceInfo_maxChannels_get, _dcservo.TLI_DeviceInfo_maxChannels_set)

    def __init__(self):
        _dcservo.TLI_DeviceInfo_swiginit(self, _dcservo.new_TLI_DeviceInfo())
    __swig_destroy__ = _dcservo.delete_TLI_DeviceInfo

# Register TLI_DeviceInfo in _dcservo:
_dcservo.TLI_DeviceInfo_swigregister(TLI_DeviceInfo)
class TLI_HardwareInformation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    serialNumber = property(_dcservo.TLI_HardwareInformation_serialNumber_get, _dcservo.TLI_HardwareInformation_serialNumber_set)
    modelNumber = property(_dcservo.TLI_HardwareInformation_modelNumber_get, _dcservo.TLI_HardwareInformation_modelNumber_set)
    type = property(_dcservo.TLI_HardwareInformation_type_get, _dcservo.TLI_HardwareInformation_type_set)
    firmwareVersion = property(_dcservo.TLI_HardwareInformation_firmwareVersion_get, _dcservo.TLI_HardwareInformation_firmwareVersion_set)
    notes = property(_dcservo.TLI_HardwareInformation_notes_get, _dcservo.TLI_HardwareInformation_notes_set)
    deviceDependantData = property(_dcservo.TLI_HardwareInformation_deviceDependantData_get, _dcservo.TLI_HardwareInformation_deviceDependantData_set)
    hardwareVersion = property(_dcservo.TLI_HardwareInformation_hardwareVersion_get, _dcservo.TLI_HardwareInformation_hardwareVersion_set)
    modificationState = property(_dcservo.TLI_HardwareInformation_modificationState_get, _dcservo.TLI_HardwareInformation_modificationState_set)
    numChannels = property(_dcservo.TLI_HardwareInformation_numChannels_get, _dcservo.TLI_HardwareInformation_numChannels_set)

    def __init__(self):
        _dcservo.TLI_HardwareInformation_swiginit(self, _dcservo.new_TLI_HardwareInformation())
    __swig_destroy__ = _dcservo.delete_TLI_HardwareInformation

# Register TLI_HardwareInformation in _dcservo:
_dcservo.TLI_HardwareInformation_swigregister(TLI_HardwareInformation)
class MOT_VelocityParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    minVelocity = property(_dcservo.MOT_VelocityParameters_minVelocity_get, _dcservo.MOT_VelocityParameters_minVelocity_set)
    acceleration = property(_dcservo.MOT_VelocityParameters_acceleration_get, _dcservo.MOT_VelocityParameters_acceleration_set)
    maxVelocity = property(_dcservo.MOT_VelocityParameters_maxVelocity_get, _dcservo.MOT_VelocityParameters_maxVelocity_set)

    def __init__(self):
        _dcservo.MOT_VelocityParameters_swiginit(self, _dcservo.new_MOT_VelocityParameters())
    __swig_destroy__ = _dcservo.delete_MOT_VelocityParameters

# Register MOT_VelocityParameters in _dcservo:
_dcservo.MOT_VelocityParameters_swigregister(MOT_VelocityParameters)
class MOT_JogParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    mode = property(_dcservo.MOT_JogParameters_mode_get, _dcservo.MOT_JogParameters_mode_set)
    stepSize = property(_dcservo.MOT_JogParameters_stepSize_get, _dcservo.MOT_JogParameters_stepSize_set)
    velParams = property(_dcservo.MOT_JogParameters_velParams_get, _dcservo.MOT_JogParameters_velParams_set)
    stopMode = property(_dcservo.MOT_JogParameters_stopMode_get, _dcservo.MOT_JogParameters_stopMode_set)

    def __init__(self):
        _dcservo.MOT_JogParameters_swiginit(self, _dcservo.new_MOT_JogParameters())
    __swig_destroy__ = _dcservo.delete_MOT_JogParameters

# Register MOT_JogParameters in _dcservo:
_dcservo.MOT_JogParameters_swigregister(MOT_JogParameters)
class MOT_HomingParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    direction = property(_dcservo.MOT_HomingParameters_direction_get, _dcservo.MOT_HomingParameters_direction_set)
    limitSwitch = property(_dcservo.MOT_HomingParameters_limitSwitch_get, _dcservo.MOT_HomingParameters_limitSwitch_set)
    velocity = property(_dcservo.MOT_HomingParameters_velocity_get, _dcservo.MOT_HomingParameters_velocity_set)
    offsetDistance = property(_dcservo.MOT_HomingParameters_offsetDistance_get, _dcservo.MOT_HomingParameters_offsetDistance_set)

    def __init__(self):
        _dcservo.MOT_HomingParameters_swiginit(self, _dcservo.new_MOT_HomingParameters())
    __swig_destroy__ = _dcservo.delete_MOT_HomingParameters

# Register MOT_HomingParameters in _dcservo:
_dcservo.MOT_HomingParameters_swigregister(MOT_HomingParameters)
class MOT_LimitSwitchParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    clockwiseHardwareLimit = property(_dcservo.MOT_LimitSwitchParameters_clockwiseHardwareLimit_get, _dcservo.MOT_LimitSwitchParameters_clockwiseHardwareLimit_set)
    anticlockwiseHardwareLimit = property(_dcservo.MOT_LimitSwitchParameters_anticlockwiseHardwareLimit_get, _dcservo.MOT_LimitSwitchParameters_anticlockwiseHardwareLimit_set)
    clockwisePosition = property(_dcservo.MOT_LimitSwitchParameters_clockwisePosition_get, _dcservo.MOT_LimitSwitchParameters_clockwisePosition_set)
    anticlockwisePosition = property(_dcservo.MOT_LimitSwitchParameters_anticlockwisePosition_get, _dcservo.MOT_LimitSwitchParameters_anticlockwisePosition_set)
    softLimitMode = property(_dcservo.MOT_LimitSwitchParameters_softLimitMode_get, _dcservo.MOT_LimitSwitchParameters_softLimitMode_set)

    def __init__(self):
        _dcservo.MOT_LimitSwitchParameters_swiginit(self, _dcservo.new_MOT_LimitSwitchParameters())
    __swig_destroy__ = _dcservo.delete_MOT_LimitSwitchParameters

# Register MOT_LimitSwitchParameters in _dcservo:
_dcservo.MOT_LimitSwitchParameters_swigregister(MOT_LimitSwitchParameters)
class MOT_DC_PIDParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    proportionalGain = property(_dcservo.MOT_DC_PIDParameters_proportionalGain_get, _dcservo.MOT_DC_PIDParameters_proportionalGain_set)
    integralGain = property(_dcservo.MOT_DC_PIDParameters_integralGain_get, _dcservo.MOT_DC_PIDParameters_integralGain_set)
    differentialGain = property(_dcservo.MOT_DC_PIDParameters_differentialGain_get, _dcservo.MOT_DC_PIDParameters_differentialGain_set)
    integralLimit = property(_dcservo.MOT_DC_PIDParameters_integralLimit_get, _dcservo.MOT_DC_PIDParameters_integralLimit_set)
    parameterFilter = property(_dcservo.MOT_DC_PIDParameters_parameterFilter_get, _dcservo.MOT_DC_PIDParameters_parameterFilter_set)

    def __init__(self):
        _dcservo.MOT_DC_PIDParameters_swiginit(self, _dcservo.new_MOT_DC_PIDParameters())
    __swig_destroy__ = _dcservo.delete_MOT_DC_PIDParameters

# Register MOT_DC_PIDParameters in _dcservo:
_dcservo.MOT_DC_PIDParameters_swigregister(MOT_DC_PIDParameters)
class KMOT_MMIParams(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    WheelMode = property(_dcservo.KMOT_MMIParams_WheelMode_get, _dcservo.KMOT_MMIParams_WheelMode_set)
    WheelMaxVelocity = property(_dcservo.KMOT_MMIParams_WheelMaxVelocity_get, _dcservo.KMOT_MMIParams_WheelMaxVelocity_set)
    WheelAcceleration = property(_dcservo.KMOT_MMIParams_WheelAcceleration_get, _dcservo.KMOT_MMIParams_WheelAcceleration_set)
    WheelDirectionSense = property(_dcservo.KMOT_MMIParams_WheelDirectionSense_get, _dcservo.KMOT_MMIParams_WheelDirectionSense_set)
    PresetPos1 = property(_dcservo.KMOT_MMIParams_PresetPos1_get, _dcservo.KMOT_MMIParams_PresetPos1_set)
    PresetPos2 = property(_dcservo.KMOT_MMIParams_PresetPos2_get, _dcservo.KMOT_MMIParams_PresetPos2_set)
    DisplayIntensity = property(_dcservo.KMOT_MMIParams_DisplayIntensity_get, _dcservo.KMOT_MMIParams_DisplayIntensity_set)
    DisplayTimeout = property(_dcservo.KMOT_MMIParams_DisplayTimeout_get, _dcservo.KMOT_MMIParams_DisplayTimeout_set)
    DisplayDimIntensity = property(_dcservo.KMOT_MMIParams_DisplayDimIntensity_get, _dcservo.KMOT_MMIParams_DisplayDimIntensity_set)
    reserved = property(_dcservo.KMOT_MMIParams_reserved_get, _dcservo.KMOT_MMIParams_reserved_set)

    def __init__(self):
        _dcservo.KMOT_MMIParams_swiginit(self, _dcservo.new_KMOT_MMIParams())
    __swig_destroy__ = _dcservo.delete_KMOT_MMIParams

# Register KMOT_MMIParams in _dcservo:
_dcservo.KMOT_MMIParams_swigregister(KMOT_MMIParams)
class KMOT_TriggerConfig(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Trigger1Mode = property(_dcservo.KMOT_TriggerConfig_Trigger1Mode_get, _dcservo.KMOT_TriggerConfig_Trigger1Mode_set)
    Trigger1Polarity = property(_dcservo.KMOT_TriggerConfig_Trigger1Polarity_get, _dcservo.KMOT_TriggerConfig_Trigger1Polarity_set)
    Trigger2Mode = property(_dcservo.KMOT_TriggerConfig_Trigger2Mode_get, _dcservo.KMOT_TriggerConfig_Trigger2Mode_set)
    Trigger2Polarity = property(_dcservo.KMOT_TriggerConfig_Trigger2Polarity_get, _dcservo.KMOT_TriggerConfig_Trigger2Polarity_set)
    reserved = property(_dcservo.KMOT_TriggerConfig_reserved_get, _dcservo.KMOT_TriggerConfig_reserved_set)

    def __init__(self):
        _dcservo.KMOT_TriggerConfig_swiginit(self, _dcservo.new_KMOT_TriggerConfig())
    __swig_destroy__ = _dcservo.delete_KMOT_TriggerConfig

# Register KMOT_TriggerConfig in _dcservo:
_dcservo.KMOT_TriggerConfig_swigregister(KMOT_TriggerConfig)
class KMOT_TriggerParams(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    TriggerStartPositionFwd = property(_dcservo.KMOT_TriggerParams_TriggerStartPositionFwd_get, _dcservo.KMOT_TriggerParams_TriggerStartPositionFwd_set)
    TriggerIntervalFwd = property(_dcservo.KMOT_TriggerParams_TriggerIntervalFwd_get, _dcservo.KMOT_TriggerParams_TriggerIntervalFwd_set)
    TriggerPulseCountFwd = property(_dcservo.KMOT_TriggerParams_TriggerPulseCountFwd_get, _dcservo.KMOT_TriggerParams_TriggerPulseCountFwd_set)
    TriggerStartPositionRev = property(_dcservo.KMOT_TriggerParams_TriggerStartPositionRev_get, _dcservo.KMOT_TriggerParams_TriggerStartPositionRev_set)
    TriggerIntervalRev = property(_dcservo.KMOT_TriggerParams_TriggerIntervalRev_get, _dcservo.KMOT_TriggerParams_TriggerIntervalRev_set)
    TriggerPulseCountRev = property(_dcservo.KMOT_TriggerParams_TriggerPulseCountRev_get, _dcservo.KMOT_TriggerParams_TriggerPulseCountRev_set)
    TriggerPulseWidth = property(_dcservo.KMOT_TriggerParams_TriggerPulseWidth_get, _dcservo.KMOT_TriggerParams_TriggerPulseWidth_set)
    CycleCount = property(_dcservo.KMOT_TriggerParams_CycleCount_get, _dcservo.KMOT_TriggerParams_CycleCount_set)
    reserved = property(_dcservo.KMOT_TriggerParams_reserved_get, _dcservo.KMOT_TriggerParams_reserved_set)

    def __init__(self):
        _dcservo.KMOT_TriggerParams_swiginit(self, _dcservo.new_KMOT_TriggerParams())
    __swig_destroy__ = _dcservo.delete_KMOT_TriggerParams

# Register KMOT_TriggerParams in _dcservo:
_dcservo.KMOT_TriggerParams_swigregister(KMOT_TriggerParams)

def TLI_BuildDeviceList():
    return _dcservo.TLI_BuildDeviceList()

def TLI_GetDeviceListSize():
    return _dcservo.TLI_GetDeviceListSize()

def TLI_GetDeviceList(stringsReceiver):
    return _dcservo.TLI_GetDeviceList(stringsReceiver)

def TLI_GetDeviceListByType(stringsReceiver, typeID):
    return _dcservo.TLI_GetDeviceListByType(stringsReceiver, typeID)

def TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length):
    return _dcservo.TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length)

def TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer):
    return _dcservo.TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer)

def TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID):
    return _dcservo.TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID)

def TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length):
    return _dcservo.TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length)

def TLI_GetDeviceInfo(serialNo, info):
    return _dcservo.TLI_GetDeviceInfo(serialNo, info)

def TLI_InitializeSimulations():
    return _dcservo.TLI_InitializeSimulations()

def TLI_UninitializeSimulations():
    return _dcservo.TLI_UninitializeSimulations()

def CC_Open(serialNo):
    return _dcservo.CC_Open(serialNo)

def CC_Close(serialNo):
    return _dcservo.CC_Close(serialNo)

def CC_CheckConnection(serialNo):
    return _dcservo.CC_CheckConnection(serialNo)

def CC_Identify(serialNo):
    return _dcservo.CC_Identify(serialNo)

def CC_RequestLEDswitches(serialNo):
    return _dcservo.CC_RequestLEDswitches(serialNo)

def CC_GetLEDswitches(serialNo):
    return _dcservo.CC_GetLEDswitches(serialNo)

def CC_SetLEDswitches(serialNo, LEDswitches):
    return _dcservo.CC_SetLEDswitches(serialNo, LEDswitches)

def CC_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState):
    return _dcservo.CC_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState)

def CC_GetHardwareInfoBlock(serialNo, hardwareInfo):
    return _dcservo.CC_GetHardwareInfoBlock(serialNo, hardwareInfo)

def CC_GetHubBay(serialNo):
    return _dcservo.CC_GetHubBay(serialNo)

def CC_GetSoftwareVersion(serialNo):
    return _dcservo.CC_GetSoftwareVersion(serialNo)

def CC_LoadSettings(serialNo):
    return _dcservo.CC_LoadSettings(serialNo)

def CC_LoadNamedSettings(serialNo, settingsName):
    return _dcservo.CC_LoadNamedSettings(serialNo, settingsName)

def CC_PersistSettings(serialNo):
    return _dcservo.CC_PersistSettings(serialNo)

def CC_ResetStageToDefaults(serialNo):
    return _dcservo.CC_ResetStageToDefaults(serialNo)

def CC_DisableChannel(serialNo):
    return _dcservo.CC_DisableChannel(serialNo)

def CC_EnableChannel(serialNo):
    return _dcservo.CC_EnableChannel(serialNo)

def CC_CanDeviceLockFrontPanel(serialNo):
    return _dcservo.CC_CanDeviceLockFrontPanel(serialNo)

def CC_GetFrontPanelLocked(serialNo):
    return _dcservo.CC_GetFrontPanelLocked(serialNo)

def CC_RequestFrontPanelLocked(serialNo):
    return _dcservo.CC_RequestFrontPanelLocked(serialNo)

def CC_SetFrontPanelLock(serialNo, locked):
    return _dcservo.CC_SetFrontPanelLock(serialNo, locked)

def CC_GetNumberPositions(serialNo):
    return _dcservo.CC_GetNumberPositions(serialNo)

def CC_MoveToPosition(serialNo, index):
    return _dcservo.CC_MoveToPosition(serialNo, index)

def CC_GetPosition(serialNo):
    return _dcservo.CC_GetPosition(serialNo)

def CC_CanHome(serialNo):
    return _dcservo.CC_CanHome(serialNo)

def CC_NeedsHoming(serialNo):
    return _dcservo.CC_NeedsHoming(serialNo)

def CC_CanMoveWithoutHomingFirst(serialNo):
    return _dcservo.CC_CanMoveWithoutHomingFirst(serialNo)

def CC_Home(serialNo):
    return _dcservo.CC_Home(serialNo)

def CC_ClearMessageQueue(serialNo):
    return _dcservo.CC_ClearMessageQueue(serialNo)

def CC_RegisterMessageCallback(serialNo, functionPointer):
    return _dcservo.CC_RegisterMessageCallback(serialNo, functionPointer)

def CC_MessageQueueSize(serialNo):
    return _dcservo.CC_MessageQueueSize(serialNo)

def CC_GetNextMessage(serialNo, messageType, messageID, messageData):
    return _dcservo.CC_GetNextMessage(serialNo, messageType, messageID, messageData)

def CC_WaitForMessage(serialNo, messageType, messageID, messageData):
    return _dcservo.CC_WaitForMessage(serialNo, messageType, messageID, messageData)

def CC_RequestHomingParams(serialNo):
    return _dcservo.CC_RequestHomingParams(serialNo)

def CC_GetHomingVelocity(serialNo):
    return _dcservo.CC_GetHomingVelocity(serialNo)

def CC_SetHomingVelocity(serialNo, velocity):
    return _dcservo.CC_SetHomingVelocity(serialNo, velocity)

def CC_MoveRelative(serialNo, displacement):
    return _dcservo.CC_MoveRelative(serialNo, displacement)

def CC_RequestJogParams(serialNo):
    return _dcservo.CC_RequestJogParams(serialNo)

def CC_GetJogMode(serialNo, mode, stopMode):
    return _dcservo.CC_GetJogMode(serialNo, mode, stopMode)

def CC_SetJogMode(serialNo, mode, stopMode):
    return _dcservo.CC_SetJogMode(serialNo, mode, stopMode)

def CC_GetJogStepSize(serialNo):
    return _dcservo.CC_GetJogStepSize(serialNo)

def CC_SetJogStepSize(serialNo, stepSize):
    return _dcservo.CC_SetJogStepSize(serialNo, stepSize)

def CC_GetJogVelParams(serialNo, acceleration, maxVelocity):
    return _dcservo.CC_GetJogVelParams(serialNo, acceleration, maxVelocity)

def CC_SetJogVelParams(serialNo, acceleration, maxVelocity):
    return _dcservo.CC_SetJogVelParams(serialNo, acceleration, maxVelocity)

def CC_MoveJog(serialNo, jogDirection):
    return _dcservo.CC_MoveJog(serialNo, jogDirection)

def CC_RequestVelParams(serialNo):
    return _dcservo.CC_RequestVelParams(serialNo)

def CC_GetVelParams(serialNo, acceleration, maxVelocity):
    return _dcservo.CC_GetVelParams(serialNo, acceleration, maxVelocity)

def CC_SetVelParams(serialNo, acceleration, maxVelocity):
    return _dcservo.CC_SetVelParams(serialNo, acceleration, maxVelocity)

def CC_MoveAtVelocity(serialNo, direction):
    return _dcservo.CC_MoveAtVelocity(serialNo, direction)

def CC_SetDirection(serialNo, reverse):
    return _dcservo.CC_SetDirection(serialNo, reverse)

def CC_StopImmediate(serialNo):
    return _dcservo.CC_StopImmediate(serialNo)

def CC_StopProfiled(serialNo):
    return _dcservo.CC_StopProfiled(serialNo)

def CC_RequestBacklash(serialNo):
    return _dcservo.CC_RequestBacklash(serialNo)

def CC_GetBacklash(serialNo):
    return _dcservo.CC_GetBacklash(serialNo)

def CC_SetBacklash(serialNo, distance):
    return _dcservo.CC_SetBacklash(serialNo, distance)

def CC_GetPositionCounter(serialNo):
    return _dcservo.CC_GetPositionCounter(serialNo)

def CC_SetPositionCounter(serialNo, count):
    return _dcservo.CC_SetPositionCounter(serialNo, count)

def CC_RequestEncoderCounter(serialNo):
    return _dcservo.CC_RequestEncoderCounter(serialNo)

def CC_GetEncoderCounter(serialNo):
    return _dcservo.CC_GetEncoderCounter(serialNo)

def CC_SetEncoderCounter(serialNo, count):
    return _dcservo.CC_SetEncoderCounter(serialNo, count)

def CC_RequestLimitSwitchParams(serialNo):
    return _dcservo.CC_RequestLimitSwitchParams(serialNo)

def CC_GetLimitSwitchParams(serialNo, clockwiseHardwareLimit, anticlockwiseHardwareLimit, clockwisePosition, anticlockwisePosition, softLimitMode):
    return _dcservo.CC_GetLimitSwitchParams(serialNo, clockwiseHardwareLimit, anticlockwiseHardwareLimit, clockwisePosition, anticlockwisePosition, softLimitMode)

def CC_SetLimitSwitchParams(serialNo, clockwiseHardwareLimit, anticlockwiseHardwareLimit, clockwisePosition, anticlockwisePosition, softLimitMode):
    return _dcservo.CC_SetLimitSwitchParams(serialNo, clockwiseHardwareLimit, anticlockwiseHardwareLimit, clockwisePosition, anticlockwisePosition, softLimitMode)

def CC_GetSoftLimitMode(serialNo):
    return _dcservo.CC_GetSoftLimitMode(serialNo)

def CC_SetLimitsSoftwareApproachPolicy(serialNo, limitsSoftwareApproachPolicy):
    return _dcservo.CC_SetLimitsSoftwareApproachPolicy(serialNo, limitsSoftwareApproachPolicy)

def CC_RequestMMIparams(serialNo):
    return _dcservo.CC_RequestMMIparams(serialNo)

def CC_GetMMIParamsExt(serialNo, wheelMode, wheelMaxVelocity, wheelAcceleration, directionSense, presetPosition1, presetPosition2, displayIntensity, displayTimeout, displayDimIntensity):
    return _dcservo.CC_GetMMIParamsExt(serialNo, wheelMode, wheelMaxVelocity, wheelAcceleration, directionSense, presetPosition1, presetPosition2, displayIntensity, displayTimeout, displayDimIntensity)

def CC_GetMMIParams(serialNo, wheelMode, wheelMaxVelocity, wheelAcceleration, directionSense, presetPosition1, presetPosition2, displayIntensity):
    return _dcservo.CC_GetMMIParams(serialNo, wheelMode, wheelMaxVelocity, wheelAcceleration, directionSense, presetPosition1, presetPosition2, displayIntensity)

def CC_SetMMIParamsExt(serialNo, wheelMode, wheelMaxVelocity, wheelAcceleration, directionSense, presetPosition1, presetPosition2, displayIntensity, displayTimeout, displayDimIntensity):
    return _dcservo.CC_SetMMIParamsExt(serialNo, wheelMode, wheelMaxVelocity, wheelAcceleration, directionSense, presetPosition1, presetPosition2, displayIntensity, displayTimeout, displayDimIntensity)

def CC_SetMMIParams(serialNo, wheelMode, wheelMaxVelocity, wheelAcceleration, directionSense, presetPosition1, presetPosition2, displayIntensity):
    return _dcservo.CC_SetMMIParams(serialNo, wheelMode, wheelMaxVelocity, wheelAcceleration, directionSense, presetPosition1, presetPosition2, displayIntensity)

def CC_RequestTriggerConfigParams(serialNo):
    return _dcservo.CC_RequestTriggerConfigParams(serialNo)

def CC_GetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity):
    return _dcservo.CC_GetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)

def CC_SetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity):
    return _dcservo.CC_SetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)

def CC_RequestPosTriggerParams(serialNo):
    return _dcservo.CC_RequestPosTriggerParams(serialNo)

def CC_GetTriggerParamsParams(serialNo, triggerStartPositionFwd, triggerIntervalFwd, triggerPulseCountFwd, triggerStartPositionRev, triggerIntervalRev, triggerPulseCountRev, triggerPulseWidth, cycleCount):
    return _dcservo.CC_GetTriggerParamsParams(serialNo, triggerStartPositionFwd, triggerIntervalFwd, triggerPulseCountFwd, triggerStartPositionRev, triggerIntervalRev, triggerPulseCountRev, triggerPulseWidth, cycleCount)

def CC_SetTriggerParamsParams(serialNo, triggerStartPositionFwd, triggerIntervalFwd, triggerPulseCountFwd, triggerStartPositionRev, triggerIntervalRev, triggerPulseCountRev, triggerPulseWidth, cycleCount):
    return _dcservo.CC_SetTriggerParamsParams(serialNo, triggerStartPositionFwd, triggerIntervalFwd, triggerPulseCountFwd, triggerStartPositionRev, triggerIntervalRev, triggerPulseCountRev, triggerPulseWidth, cycleCount)

def CC_GetMMIParamsBlock(serialNo, mmiParams):
    return _dcservo.CC_GetMMIParamsBlock(serialNo, mmiParams)

def CC_SetMMIParamsBlock(serialNo, mmiParams):
    return _dcservo.CC_SetMMIParamsBlock(serialNo, mmiParams)

def CC_GetTriggerConfigParamsBlock(serialNo, triggerConfigParams):
    return _dcservo.CC_GetTriggerConfigParamsBlock(serialNo, triggerConfigParams)

def CC_SetTriggerConfigParamsBlock(serialNo, triggerConfigParams):
    return _dcservo.CC_SetTriggerConfigParamsBlock(serialNo, triggerConfigParams)

def CC_GetTriggerParamsParamsBlock(serialNo, triggerParamsParams):
    return _dcservo.CC_GetTriggerParamsParamsBlock(serialNo, triggerParamsParams)

def CC_SetTriggerParamsParamsBlock(serialNo, triggerParamsParams):
    return _dcservo.CC_SetTriggerParamsParamsBlock(serialNo, triggerParamsParams)

def CC_GetVelParamsBlock(serialNo, velocityParams):
    return _dcservo.CC_GetVelParamsBlock(serialNo, velocityParams)

def CC_SetVelParamsBlock(serialNo, velocityParams):
    return _dcservo.CC_SetVelParamsBlock(serialNo, velocityParams)

def CC_SetMoveAbsolutePosition(serialNo, position):
    return _dcservo.CC_SetMoveAbsolutePosition(serialNo, position)

def CC_RequestMoveAbsolutePosition(serialNo):
    return _dcservo.CC_RequestMoveAbsolutePosition(serialNo)

def CC_GetMoveAbsolutePosition(serialNo):
    return _dcservo.CC_GetMoveAbsolutePosition(serialNo)

def CC_MoveAbsolute(serialNo):
    return _dcservo.CC_MoveAbsolute(serialNo)

def CC_SetMoveRelativeDistance(serialNo, distance):
    return _dcservo.CC_SetMoveRelativeDistance(serialNo, distance)

def CC_RequestMoveRelativeDistance(serialNo):
    return _dcservo.CC_RequestMoveRelativeDistance(serialNo)

def CC_GetMoveRelativeDistance(serialNo):
    return _dcservo.CC_GetMoveRelativeDistance(serialNo)

def CC_MoveRelativeDistance(serialNo):
    return _dcservo.CC_MoveRelativeDistance(serialNo)

def CC_GetHomingParamsBlock(serialNo, homingParams):
    return _dcservo.CC_GetHomingParamsBlock(serialNo, homingParams)

def CC_SetHomingParamsBlock(serialNo, homingParams):
    return _dcservo.CC_SetHomingParamsBlock(serialNo, homingParams)

def CC_GetJogParamsBlock(serialNo, jogParams):
    return _dcservo.CC_GetJogParamsBlock(serialNo, jogParams)

def CC_SetJogParamsBlock(serialNo, jogParams):
    return _dcservo.CC_SetJogParamsBlock(serialNo, jogParams)

def CC_GetLimitSwitchParamsBlock(serialNo, limitSwitchParams):
    return _dcservo.CC_GetLimitSwitchParamsBlock(serialNo, limitSwitchParams)

def CC_SetLimitSwitchParamsBlock(serialNo, limitSwitchParams):
    return _dcservo.CC_SetLimitSwitchParamsBlock(serialNo, limitSwitchParams)

def CC_RequestDCPIDParams(serialNo):
    return _dcservo.CC_RequestDCPIDParams(serialNo)

def CC_GetDCPIDParams(serialNo, DCproportionalIntegralDerivativeParams):
    return _dcservo.CC_GetDCPIDParams(serialNo, DCproportionalIntegralDerivativeParams)

def CC_SetDCPIDParams(serialNo, DCproportionalIntegralDerivativeParams):
    return _dcservo.CC_SetDCPIDParams(serialNo, DCproportionalIntegralDerivativeParams)

def CC_SuspendMoveMessages(serialNo):
    return _dcservo.CC_SuspendMoveMessages(serialNo)

def CC_ResumeMoveMessages(serialNo):
    return _dcservo.CC_ResumeMoveMessages(serialNo)

def CC_RequestPosition(serialNo):
    return _dcservo.CC_RequestPosition(serialNo)

def CC_RequestStatusBits(serialNo):
    return _dcservo.CC_RequestStatusBits(serialNo)

def CC_GetStatusBits(serialNo):
    return _dcservo.CC_GetStatusBits(serialNo)

def CC_StartPolling(serialNo, milliseconds):
    return _dcservo.CC_StartPolling(serialNo, milliseconds)

def CC_PollingDuration(serialNo):
    return _dcservo.CC_PollingDuration(serialNo)

def CC_StopPolling(serialNo):
    return _dcservo.CC_StopPolling(serialNo)

def CC_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS):
    return _dcservo.CC_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS)

def CC_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout):
    return _dcservo.CC_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout)

def CC_HasLastMsgTimerOverrun(serialNo):
    return _dcservo.CC_HasLastMsgTimerOverrun(serialNo)

def CC_RequestSettings(serialNo):
    return _dcservo.CC_RequestSettings(serialNo)

def CC_GetStageAxisMinPos(serialNo):
    return _dcservo.CC_GetStageAxisMinPos(serialNo)

def CC_GetStageAxisMaxPos(serialNo):
    return _dcservo.CC_GetStageAxisMaxPos(serialNo)

def CC_SetStageAxisLimits(serialNo, minPosition, maxPosition):
    return _dcservo.CC_SetStageAxisLimits(serialNo, minPosition, maxPosition)

def CC_SetMotorTravelMode(serialNo, travelMode):
    return _dcservo.CC_SetMotorTravelMode(serialNo, travelMode)

def CC_GetMotorTravelMode(serialNo):
    return _dcservo.CC_GetMotorTravelMode(serialNo)

def CC_SetMotorParams(serialNo, stepsPerRev, gearBoxRatio, pitch):
    return _dcservo.CC_SetMotorParams(serialNo, stepsPerRev, gearBoxRatio, pitch)

def CC_GetMotorParams(serialNo, stepsPerRev, gearBoxRatio, pitch):
    return _dcservo.CC_GetMotorParams(serialNo, stepsPerRev, gearBoxRatio, pitch)

def CC_SetMotorParamsExt(serialNo, stepsPerRev, gearBoxRatio, pitch):
    return _dcservo.CC_SetMotorParamsExt(serialNo, stepsPerRev, gearBoxRatio, pitch)

def CC_GetMotorParamsExt(serialNo, stepsPerRev, gearBoxRatio, pitch):
    return _dcservo.CC_GetMotorParamsExt(serialNo, stepsPerRev, gearBoxRatio, pitch)

def CC_SetMotorVelocityLimits(serialNo, maxVelocity, maxAcceleration):
    return _dcservo.CC_SetMotorVelocityLimits(serialNo, maxVelocity, maxAcceleration)

def CC_GetMotorVelocityLimits(serialNo, maxVelocity, maxAcceleration):
    return _dcservo.CC_GetMotorVelocityLimits(serialNo, maxVelocity, maxAcceleration)

def CC_ResetRotationModes(serialNo):
    return _dcservo.CC_ResetRotationModes(serialNo)

def CC_SetRotationModes(serialNo, mode, direction):
    return _dcservo.CC_SetRotationModes(serialNo, mode, direction)

def CC_SetMotorTravelLimits(serialNo, minPosition, maxPosition):
    return _dcservo.CC_SetMotorTravelLimits(serialNo, minPosition, maxPosition)

def CC_GetMotorTravelLimits(serialNo, minPosition, maxPosition):
    return _dcservo.CC_GetMotorTravelLimits(serialNo, minPosition, maxPosition)

def CC_GetRealValueFromDeviceUnit(serialNo, device_unit, real_unit, unitType):
    return _dcservo.CC_GetRealValueFromDeviceUnit(serialNo, device_unit, real_unit, unitType)

def CC_GetDeviceUnitFromRealValue(serialNo, real_unit, device_unit, unitType):
    return _dcservo.CC_GetDeviceUnitFromRealValue(serialNo, real_unit, device_unit, unitType)

def CC_RequestDigitalOutputs(serialNo):
    return _dcservo.CC_RequestDigitalOutputs(serialNo)

def CC_GetDigitalOutputs(serialNo):
    return _dcservo.CC_GetDigitalOutputs(serialNo)

def CC_SetDigitalOutputs(serialNo, outputsBits):
    return _dcservo.CC_SetDigitalOutputs(serialNo, outputsBits)

