%module laser_source

%include <windows.i> // Required for Windows-specific types

#define TLASERSOURCEDLL_EXPORTS 


%{
#define TLASERSOURCEDLL_EXPORTS 
#define PY_ARRAY_UNIQUE_SYMBOL laser_source_PY_ARRAY_UNIQUE_SYMBOL
#define SWIG_FILE_WITH_INIT
#include "Thorlabs.MotionControl.TCube.LaserSource.h"
%}

%include "numpy.i" // Required for NumPy support
%include "typemaps.i" // Required for custom type mappings

%init %{
import_array();
%}

// ignore problematic functions that won't compile (I don't know why)
// TODO: Investigate why these functions are problematic and fix them


%include "Thorlabs.MotionControl.TCube.LaserSource.h"
