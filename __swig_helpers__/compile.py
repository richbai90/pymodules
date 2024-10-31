import os
import subprocess
from pathlib import Path
import sys
import logging


def get_module_structure(root, base_dir):
    """
    Determines the module structure based on the directory structure.
    """
    if type(base_dir) == str:
        base_dir = Path(base_dir)
    if type(root) == str:
        root = Path(root)
    module_structure = '.'.join(root.relative_to(base_dir).parts)
    return module_structure


def find_lib(lib_name, lib_dir):
    """
    Finds the library name based on the module structure and the library directory.
    """
    lib_name = lib_name.replace('_', '')
    for f in os.listdir(lib_dir):
        if lib_name.lower() in f.lower():
            return f


def compile_module(base_dir, root, module_name, lib_dir='__lib'):
    """
    Compiles the module using g++ and captures any compilation errors.
    """
    path = Path(root)
    module_structure = get_module_structure(root, base_dir)
    base_path = Path(base_dir)
    # Determine the module structure based on the directory structure
    # Relative to the base directory

    lib_name = find_lib(module_structure + f'.{module_name}', lib_dir)
    # strip the .dll extension. We do it this way to account for periods in the library name
    if lib_name is not None:
        lib_name = '.'.join(lib_name.split('.')[:-1])
        lib_path = base_path / lib_dir
    else:
        lib_name = None
        lib_path = None
    output_path = path / f'_{module_name}.pyd'.replace(
        path.anchor, path.anchor.upper())
    cxx_file = path / f'{module_name}_wrap.cxx'.replace(
        path.anchor, path.anchor.upper())
    path_to_python = Path(sys.executable).parent
    python_include = path_to_python / 'include'
    local_include = base_path / '__include'
    numpy_include = r"C:\Users\User\mambaforge\envs\rich\Lib\site-packages\numpy\core\include"
    numpy_lib = r"C:\Users\User\mambaforge\envs\rich\Lib\site-packages\numpy\core\lib"
    
    gcc_cmd = [
        'g++', '-shared',
        '-g',
        '-O0', 
        f'-o',
        str(output_path),
        f'{cxx_file}',
        f'-I{python_include}',
        f'-I{local_include}',
        f'-I{numpy_include}',
        f'-L{path_to_python}',
        f'-L{numpy_lib}',
        f'-L{lib_path}' if lib_path else '',
        '-lpython39',
        f'-l{lib_name}' if lib_name else '',
        f'-lnpymath',
        '-Wno-error'  # Suppress errors
    ]

    # Remove empty strings and convert to strings
    gcc_cmd = [str(x) for x in gcc_cmd if x != '']

    try:
        subprocess.run(gcc_cmd, capture_output=True, text=True, check=True)
        print(f"Successfully compiled {module_name}")
    except subprocess.CalledProcessError as error:
        log = '''
        ------------------------------
        Error compiling {module_name}:
        
        Error code: {error.returncode}
        Error: {error.stderr}
        g++ command: {error.cmd}        
        ------------------------------
        
        '''
        logging.error(log.format(module_name=module_name, error=error))


def main(base_dir):
    """
    Walks through directories within the base directory and compiles the modules.
    """
    compiled = set()
    for root, dirs, files in os.walk(base_dir):
        if root.endswith('__include'):
            continue # Skip the __include directory
        for file in files:
            if file.endswith('.i') and file not in compiled:
                # header_file = os.path.join(root, (get_module_structure(
                #    root, base_dir) + '.' + file[:-2]).replace('_', '') + '.h')
                # add_extern_c_guards(header_file)

                module_name = os.path.splitext(file)[0]
                compile_module(base_dir, root, module_name,
                               os.path.join(base_dir, '__lib'))
                compiled.add(file)


if __name__ == "__main__":
    # setup the standard logger to log to a file
    logging.basicConfig(
        filename=r'D:\CZI_scope\code\logs\pymodules_thorlabs_kineses_compile.log',
        level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
    main(r"D:\CZI_scope\code\pymodules\thorlabs_kinesis")
