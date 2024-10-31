%module strain_gauge

%include <windows.i> // Required for Windows-specific types

#define KCUBESTRAINGAUGEDLL_EXPORTS 


%{
#define KCUBESTRAINGAUGEDLL_EXPORTS 
#define PY_ARRAY_UNIQUE_SYMBOL strain_gauge_PY_ARRAY_UNIQUE_SYMBOL
#define SWIG_FILE_WITH_INIT
#include "Thorlabs.MotionControl.KCube.StrainGauge.h"
%}

%include "numpy.i" // Required for NumPy support
%include "typemaps.i" // Required for custom type mappings

%init %{
import_array();
%}

// ignore problematic functions that won't compile (I don't know why)
// TODO: Investigate why these functions are problematic and fix them
%ignore SG_RequestIOsettings;
%ignore SG_RequestHubAnalogOutput;

%include "Thorlabs.MotionControl.KCube.StrainGauge.h"
