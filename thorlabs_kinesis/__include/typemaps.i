%typemap(in) SAFEARRAY* {
    // Check if the input is a NumPy array
    if (!PyArray_Check($input)) {
        PyErr_SetString(PyExc_TypeError, "Expected a NumPy array.");
        return NULL;
    }

    PyArrayObject* arr = (PyArrayObject*) $input;
    int nd = PyArray_NDIM(arr); // Number of dimensions
    npy_intp* dims = PyArray_DIMS(arr); // Array of dimensions

    // Allocate and initialize SAFEARRAY structure
    SAFEARRAY* sa = (SAFEARRAY*) malloc(sizeof(SAFEARRAY));
    sa->cDims = nd;
    sa->cbElements = sizeof(PVOID); // Assuming array of pointers, adjust based on actual data type
    sa->pvData = PyArray_DATA(arr);
    if (nd > 0) {
        sa->rgsabound[0].cElements = dims[0];
        sa->rgsabound[0].lLbound = 0;
    }    

    $1 = sa; // Set the resulting SAFEARRAY* to the input parameter
}

%typemap(freearg) SAFEARRAY* {
    // Free the SAFEARRAY structure
    if ($1) {
        free($1->rgsabound);
        free($1);
    }
}

%typemap(in) SAFEARRAY** (SAFEARRAY* temp) {
    // Check if the input is a NumPy array
    if (!PyArray_Check($input)) {
        PyErr_SetString(PyExc_TypeError, "Expected a NumPy array.");
        return NULL;
    }

    PyArrayObject* arr = (PyArrayObject*) $input;
    int nd = PyArray_NDIM(arr); // Number of dimensions
    npy_intp* dims = PyArray_DIMS(arr); // Array of dimensions

    // Allocate and initialize SAFEARRAY structure for 'temp'
    temp = (SAFEARRAY*) malloc(sizeof(SAFEARRAY));
    temp->cDims = nd;
    temp->cbElements = sizeof(PVOID); // Assuming array of pointers, adjust based on actual data type
    temp->pvData = PyArray_DATA(arr);
    if (nd > 0) {
        temp->rgsabound[0].cElements = dims[0];
        temp->rgsabound[0].lLbound = 0;
    }
    $1 = &temp; // Set the resulting SAFEARRAY** to the address of 'temp'
}

%typemap(freearg) SAFEARRAY** {
    // Free the SAFEARRAY structure allocated in the 'SAFEARRAY*' typemap
    if ($1 && *$1) {
        free((*$1)->rgsabound);
        free(*$1);
    }
}

