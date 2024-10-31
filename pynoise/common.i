/* libnoise.i: Example SWIG interface file for the libnoise library */

%module pynoise
%{
#include "noise/noise.h"
%}

// Include the windows header file if we are on a Windows platform
#ifdef _WIN32
    %include "windows.i"
#endif

// include the math library
%include "math.i"

// include the standard library
%include "std_string.i"
%include "std_vector.i"


