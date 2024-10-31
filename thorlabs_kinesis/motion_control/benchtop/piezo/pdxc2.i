%module pdxc2

%include <windows.i> // Required for Windows-specific types

#define BENCHPIEZODLL_EXPORTS 


%{
#define BENCHPIEZODLL_EXPORTS 
#define PY_ARRAY_UNIQUE_SYMBOL pdxc2_PY_ARRAY_UNIQUE_SYMBOL
#define SWIG_FILE_WITH_INIT
#include "Thorlabs.MotionControl.Benchtop.Piezo.PDXC2.h"
%}

%include "numpy.i" // Required for NumPy support
%include "typemaps.i" // Required for custom type mappings

%init %{
import_array();
%}

// ignore problematic functions that won't compile (I don't know why)
// TODO: Investigate why these functions are problematic and fix them


%include "Thorlabs.MotionControl.Benchtop.Piezo.PDXC2.h"