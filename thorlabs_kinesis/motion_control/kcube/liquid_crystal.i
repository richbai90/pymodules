%module liquid_crystal

%include <windows.i> // Required for Windows-specific types

#define KCUBELIQUIDCRYSTALDLL_EXPORTS 


%{
#define KCUBELIQUIDCRYSTALDLL_EXPORTS 
#define PY_ARRAY_UNIQUE_SYMBOL liquid_crystal_PY_ARRAY_UNIQUE_SYMBOL
#define SWIG_FILE_WITH_INIT
#include "Thorlabs.MotionControl.KCube.LiquidCrystal.h"
%}

%include "numpy.i" // Required for NumPy support
%include "typemaps.i" // Required for custom type mappings

%init %{
import_array();
%}

// ignore problematic functions that won't compile (I don't know why)
// TODO: Investigate why these functions are problematic and fix them
%ignore KLC_SetParamsBlock;
%ignore KLC_GetParamsExt;
%ignore KLC_GetParamsBlock;
%ignore KLC_GetParams;
%ignore KLC_SetParamsExt;
%ignore KLC_SetParams;
%ignore KLC_RequestParams;

%include "Thorlabs.MotionControl.KCube.LiquidCrystal.h"
