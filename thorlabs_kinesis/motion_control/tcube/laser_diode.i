%module laser_diode

%include <windows.i> // Required for Windows-specific types

#define TLASERDIODEDLL_EXPORTS 


%{
#define TLASERDIODEDLL_EXPORTS 
#define PY_ARRAY_UNIQUE_SYMBOL laser_diode_PY_ARRAY_UNIQUE_SYMBOL
#define SWIG_FILE_WITH_INIT
#include "Thorlabs.MotionControl.TCube.LaserDiode.h"
%}

%include "numpy.i" // Required for NumPy support
%include "typemaps.i" // Required for custom type mappings

%init %{
import_array();
%}

// ignore problematic functions that won't compile (I don't know why)
// TODO: Investigate why these functions are problematic and fix them
%ignore LD_GetMaxCurrentDigPot;

%include "Thorlabs.MotionControl.TCube.LaserDiode.h"
