%module solenoid

%include <windows.i> // Required for Windows-specific types

#define KCUBESOLENOIDDLL_EXPORTS 


%{
#define KCUBESOLENOIDDLL_EXPORTS 
#define PY_ARRAY_UNIQUE_SYMBOL solenoid_PY_ARRAY_UNIQUE_SYMBOL
#define SWIG_FILE_WITH_INIT
#include "Thorlabs.MotionControl.KCube.Solenoid.h"
%}

%include "numpy.i" // Required for NumPy support
%include "typemaps.i" // Required for custom type mappings

%init %{
import_array();
%}

// ignore problematic functions that won't compile (I don't know why)
// TODO: Investigate why these functions are problematic and fix them
%ignore SC_SetMMIParamsBlock;
%ignore SC_GetMMIParamsBlock;

%include "Thorlabs.MotionControl.KCube.Solenoid.h"
