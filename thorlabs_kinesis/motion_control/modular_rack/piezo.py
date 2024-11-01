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

def PBC_DisableChannel(serialNo, channel):
    return _piezo.PBC_DisableChannel(serialNo, channel)

def PBC_EnableChannel(serialNo, channel):
    return _piezo.PBC_EnableChannel(serialNo, channel)

def PBC_RequestStatus(serialNo, channel):
    return _piezo.PBC_RequestStatus(serialNo, channel)

def PBC_GetStatusBits(serialNo, channel):
    return _piezo.PBC_GetStatusBits(serialNo, channel)

def PBC_RequestStatusBits(serialNo, channel):
    return _piezo.PBC_RequestStatusBits(serialNo, channel)

def PBC_RequestPosition(serialNo, channel):
    return _piezo.PBC_RequestPosition(serialNo, channel)

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

def PBC_ResetParameters(serialNo, channel):
    return _piezo.PBC_ResetParameters(serialNo, channel)

def PBC_SetZero(serialNo, channel):
    return _piezo.PBC_SetZero(serialNo, channel)

def PBC_GetPositionControlMode(serialNo, channel):
    return _piezo.PBC_GetPositionControlMode(serialNo, channel)

def PBC_SetPositionControlMode(serialNo, channel, mode):
    return _piezo.PBC_SetPositionControlMode(serialNo, channel, mode)

def PBC_GetMaxOutputVoltage(serialNo, channel):
    return _piezo.PBC_GetMaxOutputVoltage(serialNo, channel)

def PBC_SetMaxOutputVoltage(serialNo, channel, maxVoltage):
    return _piezo.PBC_SetMaxOutputVoltage(serialNo, channel, maxVoltage)

def PBC_GetOutputVoltage(serialNo, channel):
    return _piezo.PBC_GetOutputVoltage(serialNo, channel)

def PBC_SetOutputVoltage(serialNo, channel, volts):
    return _piezo.PBC_SetOutputVoltage(serialNo, channel, volts)

def PBC_GetVoltageSource(serialNo, channel):
    return _piezo.PBC_GetVoltageSource(serialNo, channel)

def PBC_SetVoltageSource(serialNo, channel, source):
    return _piezo.PBC_SetVoltageSource(serialNo, channel, source)

def PBC_GetMaximumTravel(serialNo, channel):
    return _piezo.PBC_GetMaximumTravel(serialNo, channel)

def PBC_GetPosition(serialNo, channel):
    return _piezo.PBC_GetPosition(serialNo, channel)

def PBC_SetPosition(serialNo, channel, position):
    return _piezo.PBC_SetPosition(serialNo, channel, position)

def PBC_SetPositionToTolerance(serialNo, channel, position, tolerance):
    return _piezo.PBC_SetPositionToTolerance(serialNo, channel, position, tolerance)

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

