%module filter_flipper

%include <windows.i> // Required for Windows-specific types

#define FILTERFLIPPERDLLDLL_EXPORTS 


%{
#define FILTERFLIPPERDLLDLL_EXPORTS 
#define PY_ARRAY_UNIQUE_SYMBOL filter_flipper_PY_ARRAY_UNIQUE_SYMBOL
#define SWIG_FILE_WITH_INIT
#include "ThorLabs.MotionControl.FilterFlipper.h"
%}

%include "numpy.i" // Required for NumPy support
%include "typemaps.i" // Required for custom type mappings

%init %{
import_array();
%}

// ignore problematic functions that won't compile (I don't know why)
// TODO: Investigate why these functions are problematic and fix them


%include "ThorLabs.MotionControl.FilterFlipper.h"
