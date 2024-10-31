# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _nano_trak
else:
    import _nano_trak

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


FT_OK = _nano_trak.FT_OK
FT_InvalidHandle = _nano_trak.FT_InvalidHandle
FT_DeviceNotFound = _nano_trak.FT_DeviceNotFound
FT_DeviceNotOpened = _nano_trak.FT_DeviceNotOpened
FT_IOError = _nano_trak.FT_IOError
FT_InsufficientResources = _nano_trak.FT_InsufficientResources
FT_InvalidParameter = _nano_trak.FT_InvalidParameter
FT_DeviceNotPresent = _nano_trak.FT_DeviceNotPresent
FT_IncorrectDevice = _nano_trak.FT_IncorrectDevice
MOT_NotMotor = _nano_trak.MOT_NotMotor
MOT_DCMotor = _nano_trak.MOT_DCMotor
MOT_StepperMotor = _nano_trak.MOT_StepperMotor
MOT_BrushlessMotor = _nano_trak.MOT_BrushlessMotor
MOT_CustomMotor = _nano_trak.MOT_CustomMotor
class TLI_DeviceInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    typeID = property(_nano_trak.TLI_DeviceInfo_typeID_get, _nano_trak.TLI_DeviceInfo_typeID_set)
    description = property(_nano_trak.TLI_DeviceInfo_description_get, _nano_trak.TLI_DeviceInfo_description_set)
    serialNo = property(_nano_trak.TLI_DeviceInfo_serialNo_get, _nano_trak.TLI_DeviceInfo_serialNo_set)
    PID = property(_nano_trak.TLI_DeviceInfo_PID_get, _nano_trak.TLI_DeviceInfo_PID_set)
    isKnownType = property(_nano_trak.TLI_DeviceInfo_isKnownType_get, _nano_trak.TLI_DeviceInfo_isKnownType_set)
    motorType = property(_nano_trak.TLI_DeviceInfo_motorType_get, _nano_trak.TLI_DeviceInfo_motorType_set)
    isPiezoDevice = property(_nano_trak.TLI_DeviceInfo_isPiezoDevice_get, _nano_trak.TLI_DeviceInfo_isPiezoDevice_set)
    isLaser = property(_nano_trak.TLI_DeviceInfo_isLaser_get, _nano_trak.TLI_DeviceInfo_isLaser_set)
    isCustomType = property(_nano_trak.TLI_DeviceInfo_isCustomType_get, _nano_trak.TLI_DeviceInfo_isCustomType_set)
    isRack = property(_nano_trak.TLI_DeviceInfo_isRack_get, _nano_trak.TLI_DeviceInfo_isRack_set)
    maxChannels = property(_nano_trak.TLI_DeviceInfo_maxChannels_get, _nano_trak.TLI_DeviceInfo_maxChannels_set)

    def __init__(self):
        _nano_trak.TLI_DeviceInfo_swiginit(self, _nano_trak.new_TLI_DeviceInfo())
    __swig_destroy__ = _nano_trak.delete_TLI_DeviceInfo

# Register TLI_DeviceInfo in _nano_trak:
_nano_trak.TLI_DeviceInfo_swigregister(TLI_DeviceInfo)
class TLI_HardwareInformation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    serialNumber = property(_nano_trak.TLI_HardwareInformation_serialNumber_get, _nano_trak.TLI_HardwareInformation_serialNumber_set)
    modelNumber = property(_nano_trak.TLI_HardwareInformation_modelNumber_get, _nano_trak.TLI_HardwareInformation_modelNumber_set)
    type = property(_nano_trak.TLI_HardwareInformation_type_get, _nano_trak.TLI_HardwareInformation_type_set)
    firmwareVersion = property(_nano_trak.TLI_HardwareInformation_firmwareVersion_get, _nano_trak.TLI_HardwareInformation_firmwareVersion_set)
    notes = property(_nano_trak.TLI_HardwareInformation_notes_get, _nano_trak.TLI_HardwareInformation_notes_set)
    deviceDependantData = property(_nano_trak.TLI_HardwareInformation_deviceDependantData_get, _nano_trak.TLI_HardwareInformation_deviceDependantData_set)
    hardwareVersion = property(_nano_trak.TLI_HardwareInformation_hardwareVersion_get, _nano_trak.TLI_HardwareInformation_hardwareVersion_set)
    modificationState = property(_nano_trak.TLI_HardwareInformation_modificationState_get, _nano_trak.TLI_HardwareInformation_modificationState_set)
    numChannels = property(_nano_trak.TLI_HardwareInformation_numChannels_get, _nano_trak.TLI_HardwareInformation_numChannels_set)

    def __init__(self):
        _nano_trak.TLI_HardwareInformation_swiginit(self, _nano_trak.new_TLI_HardwareInformation())
    __swig_destroy__ = _nano_trak.delete_TLI_HardwareInformation

# Register TLI_HardwareInformation in _nano_trak:
_nano_trak.TLI_HardwareInformation_swigregister(TLI_HardwareInformation)
NT_BadSignal = _nano_trak.NT_BadSignal
NT_GoodSignal = _nano_trak.NT_GoodSignal
NT_ModeUndefined = _nano_trak.NT_ModeUndefined
NT_Piezo = _nano_trak.NT_Piezo
NT_Latch = _nano_trak.NT_Latch
NT_Tracking = _nano_trak.NT_Tracking
NT_HorizontalTracking = _nano_trak.NT_HorizontalTracking
NT_VerticalTracking = _nano_trak.NT_VerticalTracking
NT_ControlModeUndefined = _nano_trak.NT_ControlModeUndefined
NT_OpenLoop = _nano_trak.NT_OpenLoop
NT_ClosedLoop = _nano_trak.NT_ClosedLoop
NT_OpenLoopSmoothed = _nano_trak.NT_OpenLoopSmoothed
NT_ClosedLoopSmoothed = _nano_trak.NT_ClosedLoopSmoothed
NT_FeedbackSourceUndefined = _nano_trak.NT_FeedbackSourceUndefined
NT_TIA = _nano_trak.NT_TIA
NT_IO1_5v = _nano_trak.NT_IO1_5v
NUM_TIA_RANGES = _nano_trak.NUM_TIA_RANGES
KNA_TIARange1_5nA = _nano_trak.KNA_TIARange1_5nA
KNA_TIARange2_16_6nA = _nano_trak.KNA_TIARange2_16_6nA
KNA_TIARange3_50nA = _nano_trak.KNA_TIARange3_50nA
KNA_TIARange4_166nA = _nano_trak.KNA_TIARange4_166nA
KNA_TIARange5_500nA = _nano_trak.KNA_TIARange5_500nA
KNA_TIARange6_1_66uA = _nano_trak.KNA_TIARange6_1_66uA
KNA_TIARange7_5uA = _nano_trak.KNA_TIARange7_5uA
KNA_TIARange8_16_6uA = _nano_trak.KNA_TIARange8_16_6uA
KNA_TIARange9_50uA = _nano_trak.KNA_TIARange9_50uA
KNA_TIARange10_166uA = _nano_trak.KNA_TIARange10_166uA
KNA_TIARange11_500uA = _nano_trak.KNA_TIARange11_500uA
KNA_TIARange12_1_66mA = _nano_trak.KNA_TIARange12_1_66mA
KNA_TIARange13_5mA = _nano_trak.KNA_TIARange13_5mA
NT_OddAndEven = _nano_trak.NT_OddAndEven
NT_Odd = _nano_trak.NT_Odd
NT_Even = _nano_trak.NT_Even
NT_InRange = _nano_trak.NT_InRange
NT_UnderRange = _nano_trak.NT_UnderRange
NT_OverRange = _nano_trak.NT_OverRange
NT_ParameterCircleMode = _nano_trak.NT_ParameterCircleMode
NT_AbsPowerCircleMode = _nano_trak.NT_AbsPowerCircleMode
NT_LUTCircleMode = _nano_trak.NT_LUTCircleMode
NT_LinearCircleAdjustment = _nano_trak.NT_LinearCircleAdjustment
NT_LogCircleAdjustment = _nano_trak.NT_LogCircleAdjustment
NT_SquareCircleAdjustment = _nano_trak.NT_SquareCircleAdjustment
NT_CubeCircleAdjustment = _nano_trak.NT_CubeCircleAdjustment
NT_TIARangeModeUndefined = _nano_trak.NT_TIARangeModeUndefined
NT_AutoRangeAtSelected = _nano_trak.NT_AutoRangeAtSelected
NT_ManualRangeAtSelected = _nano_trak.NT_ManualRangeAtSelected
NT_ManualRangeAtParameter = _nano_trak.NT_ManualRangeAtParameter
NT_AutoRangeAtParameter = _nano_trak.NT_AutoRangeAtParameter
KNA_VoltageRange_10v = _nano_trak.KNA_VoltageRange_10v
KNA_IO1Only = _nano_trak.KNA_IO1Only
KNA_Default_Range = _nano_trak.KNA_Default_Range
KNA_VoltageRange_CH1_75v = _nano_trak.KNA_VoltageRange_CH1_75v
KNA_VoltageRange_CH1_150v = _nano_trak.KNA_VoltageRange_CH1_150v
KNA_VoltageRange_CH2_75v = _nano_trak.KNA_VoltageRange_CH2_75v
KNA_VoltageRange_CH2_150v = _nano_trak.KNA_VoltageRange_CH2_150v
KNA_Default_Route = _nano_trak.KNA_Default_Route
KNA_ExtIn_PIN = _nano_trak.KNA_ExtIn_PIN
KNA_ExtIn_IO1 = _nano_trak.KNA_ExtIn_IO1
KNA_ExtOut_Dis = _nano_trak.KNA_ExtOut_Dis
KNA_ExtOut_IO2 = _nano_trak.KNA_ExtOut_IO2
KNA_EnableInputBoost = _nano_trak.KNA_EnableInputBoost
NT_VoltageRangeUndefined = _nano_trak.NT_VoltageRangeUndefined
NT_VoltageRange_5v = _nano_trak.NT_VoltageRange_5v
NT_VoltageRange_10v = _nano_trak.NT_VoltageRange_10v
NT_IO1Only = _nano_trak.NT_IO1Only
NT_HubOrIO1 = _nano_trak.NT_HubOrIO1
NT_Amps = _nano_trak.NT_Amps
NT_Watts = _nano_trak.NT_Watts
NT_Db = _nano_trak.NT_Db
NT_Voltage = _nano_trak.NT_Voltage
NT_FullRange = _nano_trak.NT_FullRange
NT_UserDefined = _nano_trak.NT_UserDefined
KNA_WM_Low = _nano_trak.KNA_WM_Low
KNA_WM_Medium = _nano_trak.KNA_WM_Medium
KNA_WM_High = _nano_trak.KNA_WM_High
KNA_TrigDisabled = _nano_trak.KNA_TrigDisabled
KNA_TrigIn_GPI = _nano_trak.KNA_TrigIn_GPI
KNA_TrigIn_VoltageStepUp = _nano_trak.KNA_TrigIn_VoltageStepUp
KNA_TrigIn_VoltageStepDown = _nano_trak.KNA_TrigIn_VoltageStepDown
KNA_TrigOut_GPO = _nano_trak.KNA_TrigOut_GPO
KNA_TrigPolarityHigh = _nano_trak.KNA_TrigPolarityHigh
KNA_TrigPolarityLow = _nano_trak.KNA_TrigPolarityLow
KNA_ChannelUndefined = _nano_trak.KNA_ChannelUndefined
KNA_Channel1 = _nano_trak.KNA_Channel1
KNA_Channel2 = _nano_trak.KNA_Channel2
PZ_ControlModeUndefined = _nano_trak.PZ_ControlModeUndefined
PZ_OpenLoop = _nano_trak.PZ_OpenLoop
PZ_CloseLoop = _nano_trak.PZ_CloseLoop
PZ_OpenLoopSmooth = _nano_trak.PZ_OpenLoopSmooth
PZ_CloseLoopSmooth = _nano_trak.PZ_CloseLoopSmooth
class NT_HVComponent(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    horizontalComponent = property(_nano_trak.NT_HVComponent_horizontalComponent_get, _nano_trak.NT_HVComponent_horizontalComponent_set)
    verticalComponent = property(_nano_trak.NT_HVComponent_verticalComponent_get, _nano_trak.NT_HVComponent_verticalComponent_set)

    def __init__(self):
        _nano_trak.NT_HVComponent_swiginit(self, _nano_trak.new_NT_HVComponent())
    __swig_destroy__ = _nano_trak.delete_NT_HVComponent

# Register NT_HVComponent in _nano_trak:
_nano_trak.NT_HVComponent_swigregister(NT_HVComponent)
class NT_CircleParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    mode = property(_nano_trak.NT_CircleParameters_mode_get, _nano_trak.NT_CircleParameters_mode_set)
    diameter = property(_nano_trak.NT_CircleParameters_diameter_get, _nano_trak.NT_CircleParameters_diameter_set)
    samplesPerRevolution = property(_nano_trak.NT_CircleParameters_samplesPerRevolution_get, _nano_trak.NT_CircleParameters_samplesPerRevolution_set)
    minDiameter = property(_nano_trak.NT_CircleParameters_minDiameter_get, _nano_trak.NT_CircleParameters_minDiameter_set)
    maxDiameter = property(_nano_trak.NT_CircleParameters_maxDiameter_get, _nano_trak.NT_CircleParameters_maxDiameter_set)
    algorithmAdjustment = property(_nano_trak.NT_CircleParameters_algorithmAdjustment_get, _nano_trak.NT_CircleParameters_algorithmAdjustment_set)

    def __init__(self):
        _nano_trak.NT_CircleParameters_swiginit(self, _nano_trak.new_NT_CircleParameters())
    __swig_destroy__ = _nano_trak.delete_NT_CircleParameters

# Register NT_CircleParameters in _nano_trak:
_nano_trak.NT_CircleParameters_swigregister(NT_CircleParameters)
class NT_CircleDiameterLUT(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    LUTdiameter = property(_nano_trak.NT_CircleDiameterLUT_LUTdiameter_get, _nano_trak.NT_CircleDiameterLUT_LUTdiameter_set)

    def __init__(self):
        _nano_trak.NT_CircleDiameterLUT_swiginit(self, _nano_trak.new_NT_CircleDiameterLUT())
    __swig_destroy__ = _nano_trak.delete_NT_CircleDiameterLUT

# Register NT_CircleDiameterLUT in _nano_trak:
_nano_trak.NT_CircleDiameterLUT_swigregister(NT_CircleDiameterLUT)
class KNA_TIARangeParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    mode = property(_nano_trak.KNA_TIARangeParameters_mode_get, _nano_trak.KNA_TIARangeParameters_mode_set)
    upLimit = property(_nano_trak.KNA_TIARangeParameters_upLimit_get, _nano_trak.KNA_TIARangeParameters_upLimit_set)
    downLimit = property(_nano_trak.KNA_TIARangeParameters_downLimit_get, _nano_trak.KNA_TIARangeParameters_downLimit_set)
    settleSamples = property(_nano_trak.KNA_TIARangeParameters_settleSamples_get, _nano_trak.KNA_TIARangeParameters_settleSamples_set)
    changeToOddOrEven = property(_nano_trak.KNA_TIARangeParameters_changeToOddOrEven_get, _nano_trak.KNA_TIARangeParameters_changeToOddOrEven_set)
    newRange = property(_nano_trak.KNA_TIARangeParameters_newRange_get, _nano_trak.KNA_TIARangeParameters_newRange_set)

    def __init__(self):
        _nano_trak.KNA_TIARangeParameters_swiginit(self, _nano_trak.new_KNA_TIARangeParameters())
    __swig_destroy__ = _nano_trak.delete_KNA_TIARangeParameters

# Register KNA_TIARangeParameters in _nano_trak:
_nano_trak.KNA_TIARangeParameters_swigregister(KNA_TIARangeParameters)
class KNA_TIAReading(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    absoluteReading = property(_nano_trak.KNA_TIAReading_absoluteReading_get, _nano_trak.KNA_TIAReading_absoluteReading_set)
    relativeReading = property(_nano_trak.KNA_TIAReading_relativeReading_get, _nano_trak.KNA_TIAReading_relativeReading_set)
    selectedRange = property(_nano_trak.KNA_TIAReading_selectedRange_get, _nano_trak.KNA_TIAReading_selectedRange_set)
    underOrOverRead = property(_nano_trak.KNA_TIAReading_underOrOverRead_get, _nano_trak.KNA_TIAReading_underOrOverRead_set)

    def __init__(self):
        _nano_trak.KNA_TIAReading_swiginit(self, _nano_trak.new_KNA_TIAReading())
    __swig_destroy__ = _nano_trak.delete_KNA_TIAReading

# Register KNA_TIAReading in _nano_trak:
_nano_trak.KNA_TIAReading_swigregister(KNA_TIAReading)
class KNA_IOSettings(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    lowVoltageOutRange = property(_nano_trak.KNA_IOSettings_lowVoltageOutRange_get, _nano_trak.KNA_IOSettings_lowVoltageOutRange_set)
    lowVoltageOutputRoute = property(_nano_trak.KNA_IOSettings_lowVoltageOutputRoute_get, _nano_trak.KNA_IOSettings_lowVoltageOutputRoute_set)
    highVoltageOutRange = property(_nano_trak.KNA_IOSettings_highVoltageOutRange_get, _nano_trak.KNA_IOSettings_highVoltageOutRange_set)
    highVoltageOutputRoute = property(_nano_trak.KNA_IOSettings_highVoltageOutputRoute_get, _nano_trak.KNA_IOSettings_highVoltageOutputRoute_set)

    def __init__(self):
        _nano_trak.KNA_IOSettings_swiginit(self, _nano_trak.new_KNA_IOSettings())
    __swig_destroy__ = _nano_trak.delete_KNA_IOSettings

# Register KNA_IOSettings in _nano_trak:
_nano_trak.KNA_IOSettings_swigregister(KNA_IOSettings)
class NT_GainParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    controlMode = property(_nano_trak.NT_GainParameters_controlMode_get, _nano_trak.NT_GainParameters_controlMode_set)
    gain = property(_nano_trak.NT_GainParameters_gain_get, _nano_trak.NT_GainParameters_gain_set)

    def __init__(self):
        _nano_trak.NT_GainParameters_swiginit(self, _nano_trak.new_NT_GainParameters())
    __swig_destroy__ = _nano_trak.delete_NT_GainParameters

# Register NT_GainParameters in _nano_trak:
_nano_trak.NT_GainParameters_swigregister(NT_GainParameters)
class KNA_MMIParams(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    WheelAdjustRate = property(_nano_trak.KNA_MMIParams_WheelAdjustRate_get, _nano_trak.KNA_MMIParams_WheelAdjustRate_set)
    DisplayIntensity = property(_nano_trak.KNA_MMIParams_DisplayIntensity_get, _nano_trak.KNA_MMIParams_DisplayIntensity_set)
    reserved = property(_nano_trak.KNA_MMIParams_reserved_get, _nano_trak.KNA_MMIParams_reserved_set)

    def __init__(self):
        _nano_trak.KNA_MMIParams_swiginit(self, _nano_trak.new_KNA_MMIParams())
    __swig_destroy__ = _nano_trak.delete_KNA_MMIParams

# Register KNA_MMIParams in _nano_trak:
_nano_trak.KNA_MMIParams_swigregister(KNA_MMIParams)
class KNA_TriggerConfig(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Trigger1Mode = property(_nano_trak.KNA_TriggerConfig_Trigger1Mode_get, _nano_trak.KNA_TriggerConfig_Trigger1Mode_set)
    Trigger1Polarity = property(_nano_trak.KNA_TriggerConfig_Trigger1Polarity_get, _nano_trak.KNA_TriggerConfig_Trigger1Polarity_set)
    unused1 = property(_nano_trak.KNA_TriggerConfig_unused1_get, _nano_trak.KNA_TriggerConfig_unused1_set)
    Trigger2Mode = property(_nano_trak.KNA_TriggerConfig_Trigger2Mode_get, _nano_trak.KNA_TriggerConfig_Trigger2Mode_set)
    Trigger2Polarity = property(_nano_trak.KNA_TriggerConfig_Trigger2Polarity_get, _nano_trak.KNA_TriggerConfig_Trigger2Polarity_set)
    unused2 = property(_nano_trak.KNA_TriggerConfig_unused2_get, _nano_trak.KNA_TriggerConfig_unused2_set)
    reserved = property(_nano_trak.KNA_TriggerConfig_reserved_get, _nano_trak.KNA_TriggerConfig_reserved_set)

    def __init__(self):
        _nano_trak.KNA_TriggerConfig_swiginit(self, _nano_trak.new_KNA_TriggerConfig())
    __swig_destroy__ = _nano_trak.delete_KNA_TriggerConfig

# Register KNA_TriggerConfig in _nano_trak:
_nano_trak.KNA_TriggerConfig_swigregister(KNA_TriggerConfig)
class KNA_FeedbackLoopConstants(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    proportionalTerm = property(_nano_trak.KNA_FeedbackLoopConstants_proportionalTerm_get, _nano_trak.KNA_FeedbackLoopConstants_proportionalTerm_set)
    integralTerm = property(_nano_trak.KNA_FeedbackLoopConstants_integralTerm_get, _nano_trak.KNA_FeedbackLoopConstants_integralTerm_set)

    def __init__(self):
        _nano_trak.KNA_FeedbackLoopConstants_swiginit(self, _nano_trak.new_KNA_FeedbackLoopConstants())
    __swig_destroy__ = _nano_trak.delete_KNA_FeedbackLoopConstants

# Register KNA_FeedbackLoopConstants in _nano_trak:
_nano_trak.KNA_FeedbackLoopConstants_swigregister(KNA_FeedbackLoopConstants)

def TLI_BuildDeviceList():
    return _nano_trak.TLI_BuildDeviceList()

def TLI_GetDeviceListSize():
    return _nano_trak.TLI_GetDeviceListSize()

def TLI_GetDeviceList(stringsReceiver):
    return _nano_trak.TLI_GetDeviceList(stringsReceiver)

def TLI_GetDeviceListByType(stringsReceiver, typeID):
    return _nano_trak.TLI_GetDeviceListByType(stringsReceiver, typeID)

def TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length):
    return _nano_trak.TLI_GetDeviceListByTypes(stringsReceiver, typeIDs, length)

def TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer):
    return _nano_trak.TLI_GetDeviceListExt(receiveBuffer, sizeOfBuffer)

def TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID):
    return _nano_trak.TLI_GetDeviceListByTypeExt(receiveBuffer, sizeOfBuffer, typeID)

def TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length):
    return _nano_trak.TLI_GetDeviceListByTypesExt(receiveBuffer, sizeOfBuffer, typeIDs, length)

def TLI_GetDeviceInfo(serialNo, info):
    return _nano_trak.TLI_GetDeviceInfo(serialNo, info)

def TLI_InitializeSimulations():
    return _nano_trak.TLI_InitializeSimulations()

def TLI_UninitializeSimulations():
    return _nano_trak.TLI_UninitializeSimulations()

def NT_Open(serialNo):
    return _nano_trak.NT_Open(serialNo)

def NT_Close(serialNo):
    return _nano_trak.NT_Close(serialNo)

def NT_CheckConnection(serialNo):
    return _nano_trak.NT_CheckConnection(serialNo)

def NT_CanDeviceLockFrontPanel(serialNo):
    return _nano_trak.NT_CanDeviceLockFrontPanel(serialNo)

def NT_GetFrontPanelLocked(serialNo):
    return _nano_trak.NT_GetFrontPanelLocked(serialNo)

def NT_RequestFrontPanelLocked(serialNo):
    return _nano_trak.NT_RequestFrontPanelLocked(serialNo)

def NT_SetFrontPanelLock(serialNo, locked):
    return _nano_trak.NT_SetFrontPanelLock(serialNo, locked)

def NT_Identify(serialNo):
    return _nano_trak.NT_Identify(serialNo)

def NT_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState):
    return _nano_trak.NT_GetHardwareInfo(serialNo, modelNo, sizeOfModelNo, type, numChannels, notes, sizeOfNotes, firmwareVersion, hardwareVersion, modificationState)

def NT_GetHardwareInfoBlock(serialNo, hardwareInfo):
    return _nano_trak.NT_GetHardwareInfoBlock(serialNo, hardwareInfo)

def NT_GetFirmwareVersion(serialNo):
    return _nano_trak.NT_GetFirmwareVersion(serialNo)

def NT_GetSoftwareVersion(serialNo):
    return _nano_trak.NT_GetSoftwareVersion(serialNo)

def NT_LoadSettings(serialNo):
    return _nano_trak.NT_LoadSettings(serialNo)

def NT_LoadNamedSettings(serialNo, settingsName):
    return _nano_trak.NT_LoadNamedSettings(serialNo, settingsName)

def NT_PersistSettings(serialNo):
    return _nano_trak.NT_PersistSettings(serialNo)

def NT_Disconnect(serialNo):
    return _nano_trak.NT_Disconnect(serialNo)

def NT_RequestSignalState(serialNo):
    return _nano_trak.NT_RequestSignalState(serialNo)

def NT_GetSignalState(serialNo):
    return _nano_trak.NT_GetSignalState(serialNo)

def NT_RequestMode(serialNo):
    return _nano_trak.NT_RequestMode(serialNo)

def NT_GetMode(serialNo):
    return _nano_trak.NT_GetMode(serialNo)

def NT_SetMode(serialNo, mode):
    return _nano_trak.NT_SetMode(serialNo, mode)

def NT_RequestTrackingThresholdSignal(serialNo):
    return _nano_trak.NT_RequestTrackingThresholdSignal(serialNo)

def NT_GetTrackingThresholdSignal(serialNo):
    return _nano_trak.NT_GetTrackingThresholdSignal(serialNo)

def NT_SetTrackingThresholdSignal(serialNo, threshold):
    return _nano_trak.NT_SetTrackingThresholdSignal(serialNo, threshold)

def NT_RequestCircleHomePosition(serialNo):
    return _nano_trak.NT_RequestCircleHomePosition(serialNo)

def NT_GetCircleHomePosition(serialNo, position):
    return _nano_trak.NT_GetCircleHomePosition(serialNo, position)

def NT_SetCircleHomePosition(serialNo, position):
    return _nano_trak.NT_SetCircleHomePosition(serialNo, position)

def NT_HomeCircle(serialNo):
    return _nano_trak.NT_HomeCircle(serialNo)

def NT_RequestCirclePosition(serialNo):
    return _nano_trak.NT_RequestCirclePosition(serialNo)

def NT_GetCirclePosition(serialNo, position):
    return _nano_trak.NT_GetCirclePosition(serialNo, position)

def NT_RequestCircleParams(serialNo):
    return _nano_trak.NT_RequestCircleParams(serialNo)

def NT_GetCircleParams(serialNo, params):
    return _nano_trak.NT_GetCircleParams(serialNo, params)

def NT_SetCircleParams(serialNo, params):
    return _nano_trak.NT_SetCircleParams(serialNo, params)

def NT_GetCircleDiameter(serialNo):
    return _nano_trak.NT_GetCircleDiameter(serialNo)

def NT_SetCircleDiameter(serialNo, diameter):
    return _nano_trak.NT_SetCircleDiameter(serialNo, diameter)

def NT_RequestCircleDiameterLUT(serialNo):
    return _nano_trak.NT_RequestCircleDiameterLUT(serialNo)

def NT_GetCircleDiameterLUT(serialNo, LUT):
    return _nano_trak.NT_GetCircleDiameterLUT(serialNo, LUT)

def NT_SetCircleDiameterLUT(serialNo, LUT):
    return _nano_trak.NT_SetCircleDiameterLUT(serialNo, LUT)

def NT_RequestPhaseCompensationParams(serialNo):
    return _nano_trak.NT_RequestPhaseCompensationParams(serialNo)

def NT_GetPhaseCompensationParams(serialNo, params):
    return _nano_trak.NT_GetPhaseCompensationParams(serialNo, params)

def NT_SetPhaseCompensationParams(serialNo, params):
    return _nano_trak.NT_SetPhaseCompensationParams(serialNo, params)

def NT_RequestTIArangeParams(serialNo):
    return _nano_trak.NT_RequestTIArangeParams(serialNo)

def NT_GetTIArangeParams(serialNo, params):
    return _nano_trak.NT_GetTIArangeParams(serialNo, params)

def NT_SetTIArangeParams(serialNo, params):
    return _nano_trak.NT_SetTIArangeParams(serialNo, params)

def NT_GetRangeMode(serialNo, mode, oddOrEven):
    return _nano_trak.NT_GetRangeMode(serialNo, mode, oddOrEven)

def NT_SetRangeMode(serialNo, mode, oddOrEven):
    return _nano_trak.NT_SetRangeMode(serialNo, mode, oddOrEven)

def NT_GetTIARange(serialNo):
    return _nano_trak.NT_GetTIARange(serialNo)

def NT_SetTIARange(serialNo, range):
    return _nano_trak.NT_SetTIARange(serialNo, range)

def NT_RequestGain(serialNo):
    return _nano_trak.NT_RequestGain(serialNo)

def NT_GetGain(serialNo):
    return _nano_trak.NT_GetGain(serialNo)

def NT_SetGain(serialNo, gain):
    return _nano_trak.NT_SetGain(serialNo, gain)

def NT_RequestFeedbackSource(serialNo):
    return _nano_trak.NT_RequestFeedbackSource(serialNo)

def NT_GetFeedbackSource(serialNo):
    return _nano_trak.NT_GetFeedbackSource(serialNo)

def NT_SetFeedbackSource(serialNo, input):
    return _nano_trak.NT_SetFeedbackSource(serialNo, input)

def NT_GetLEDBrightness(serialNo):
    return _nano_trak.NT_GetLEDBrightness(serialNo)

def NT_SetLEDBrightness(serialNo, brightness):
    return _nano_trak.NT_SetLEDBrightness(serialNo, brightness)

def NT_RequestIOsettings(serialNo):
    return _nano_trak.NT_RequestIOsettings(serialNo)

def NT_GetIOsettingsBlock(serialNo, IOsettings):
    return _nano_trak.NT_GetIOsettingsBlock(serialNo, IOsettings)

def NT_SetIOsettingsBlock(serialNo, IOsettings):
    return _nano_trak.NT_SetIOsettingsBlock(serialNo, IOsettings)

def NT_GetIOsettings(serialNo, highVoltageOutRange, highVoltageOutputRoute):
    return _nano_trak.NT_GetIOsettings(serialNo, highVoltageOutRange, highVoltageOutputRoute)

def NT_SetIOsettings(serialNo, highVoltageOutRange, highVoltageOutputRoute):
    return _nano_trak.NT_SetIOsettings(serialNo, highVoltageOutRange, highVoltageOutputRoute)

def NT_GetFeedbackMode(serialNo, channel):
    return _nano_trak.NT_GetFeedbackMode(serialNo, channel)

def NT_RequestFeedbackMode(serialNo, channel):
    return _nano_trak.NT_RequestFeedbackMode(serialNo, channel)

def NT_SetFeedbackMode(serialNo, channel, mode):
    return _nano_trak.NT_SetFeedbackMode(serialNo, channel, mode)

def NT_RequestFeedbackLoopPIconsts(serialNo, channel):
    return _nano_trak.NT_RequestFeedbackLoopPIconsts(serialNo, channel)

def NT_GetFeedbackLoopPIconsts(serialNo, channel, proportionalTerm, integralTerm):
    return _nano_trak.NT_GetFeedbackLoopPIconsts(serialNo, channel, proportionalTerm, integralTerm)

def NT_SetFeedbackLoopPIconsts(serialNo, channel, proportionalTerm, integralTerm):
    return _nano_trak.NT_SetFeedbackLoopPIconsts(serialNo, channel, proportionalTerm, integralTerm)

def NT_GetFeedbackLoopPIconstsBlock(serialNo, channel, proportionalAndIntegralConstants):
    return _nano_trak.NT_GetFeedbackLoopPIconstsBlock(serialNo, channel, proportionalAndIntegralConstants)

def NT_SetFeedbackLoopPIconstsBlock(serialNo, channel, proportionalAndIntegralConstants):
    return _nano_trak.NT_SetFeedbackLoopPIconstsBlock(serialNo, channel, proportionalAndIntegralConstants)

def NT_RequestMMIParams(serialNo):
    return _nano_trak.NT_RequestMMIParams(serialNo)

def NT_GetMMIParams(serialNo, wheelAdjustRate, displayIntensity):
    return _nano_trak.NT_GetMMIParams(serialNo, wheelAdjustRate, displayIntensity)

def NT_SetMMIParams(serialNo, wheelAdjustRate, displayIntensity):
    return _nano_trak.NT_SetMMIParams(serialNo, wheelAdjustRate, displayIntensity)

def NT_RequestTriggerConfigParams(serialNo):
    return _nano_trak.NT_RequestTriggerConfigParams(serialNo)

def NT_GetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity):
    return _nano_trak.NT_GetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)

def NT_SetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity):
    return _nano_trak.NT_SetTriggerConfigParams(serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)

def NT_GetMMIParamsBlock(serialNo, mmiParams):
    return _nano_trak.NT_GetMMIParamsBlock(serialNo, mmiParams)

def NT_SetMMIParamsBlock(serialNo, mmiParams):
    return _nano_trak.NT_SetMMIParamsBlock(serialNo, mmiParams)

def NT_GetTriggerConfigParamsBlock(serialNo, triggerConfigParams):
    return _nano_trak.NT_GetTriggerConfigParamsBlock(serialNo, triggerConfigParams)

def NT_SetTriggerConfigParamsBlock(serialNo, triggerConfigParams):
    return _nano_trak.NT_SetTriggerConfigParamsBlock(serialNo, triggerConfigParams)

def NT_ClearMessageQueue(serialNo):
    return _nano_trak.NT_ClearMessageQueue(serialNo)

def NT_RegisterMessageCallback(serialNo, functionPointer):
    return _nano_trak.NT_RegisterMessageCallback(serialNo, functionPointer)

def NT_MessageQueueSize(serialNo):
    return _nano_trak.NT_MessageQueueSize(serialNo)

def NT_GetNextMessage(serialNo, messageType, messageID, messageData):
    return _nano_trak.NT_GetNextMessage(serialNo, messageType, messageID, messageData)

def NT_WaitForMessage(serialNo, messageType, messageID, messageData):
    return _nano_trak.NT_WaitForMessage(serialNo, messageType, messageID, messageData)

def NT_RequestReading(serialNo):
    return _nano_trak.NT_RequestReading(serialNo)

def NT_GetReading(serialNo, reading):
    return _nano_trak.NT_GetReading(serialNo, reading)

def NT_RequestStatus(serialNo):
    return _nano_trak.NT_RequestStatus(serialNo)

def NT_RequestStatusBits(serialNo):
    return _nano_trak.NT_RequestStatusBits(serialNo)

def NT_GetStatusBits(serialNo):
    return _nano_trak.NT_GetStatusBits(serialNo)

def NT_StartPolling(serialNo, milliseconds):
    return _nano_trak.NT_StartPolling(serialNo, milliseconds)

def NT_PollingDuration(serialNo):
    return _nano_trak.NT_PollingDuration(serialNo)

def NT_StopPolling(serialNo):
    return _nano_trak.NT_StopPolling(serialNo)

def NT_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS):
    return _nano_trak.NT_TimeSinceLastMsgReceived(serialNo, lastUpdateTimeMS)

def NT_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout):
    return _nano_trak.NT_EnableLastMsgTimer(serialNo, enable, lastMsgTimeout)

def NT_HasLastMsgTimerOverrun(serialNo):
    return _nano_trak.NT_HasLastMsgTimerOverrun(serialNo)

def NT_RequestSettings(serialNo):
    return _nano_trak.NT_RequestSettings(serialNo)

def NT_RequestXYScan(serialNo):
    return _nano_trak.NT_RequestXYScan(serialNo)

def NT_StopXYScan(serialNo):
    return _nano_trak.NT_StopXYScan(serialNo)

def NT_IsXYScanning(serialNo):
    return _nano_trak.NT_IsXYScanning(serialNo)

def NT_IsXYScanLineAvailable(serialNo, lineNo):
    return _nano_trak.NT_IsXYScanLineAvailable(serialNo, lineNo)

def NT_IsXYScanAvailable(serialNo):
    return _nano_trak.NT_IsXYScanAvailable(serialNo)

def NT_GetXYScanRange(serialNo):
    return _nano_trak.NT_GetXYScanRange(serialNo)

def NT_GetXYScanLine(serialNo, lineNo, line, bufferSize):
    return _nano_trak.NT_GetXYScanLine(serialNo, lineNo, line, bufferSize)
