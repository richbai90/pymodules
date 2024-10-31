%module brushless_motor

%include <windows.i> // Required for Windows-specific types

#define MODULARRACKDLL_EXPORTS 


%{
#define MODULARRACKDLL_EXPORTS 
#define PY_ARRAY_UNIQUE_SYMBOL brushless_motor_PY_ARRAY_UNIQUE_SYMBOL
#define SWIG_FILE_WITH_INIT
#include "Thorlabs.MotionControl.ModularRack.BrushlessMotor.h"
%}

%include "numpy.i" // Required for NumPy support
%include "typemaps.i" // Required for custom type mappings

%init %{
import_array();
%}

// ignore problematic functions that won't compile (I don't know why)
// TODO: Investigate why these functions are problematic and fix them


%include "Thorlabs.MotionControl.ModularRack.BrushlessMotor.h"
