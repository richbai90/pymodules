import re
import ctypes
from typing import List, Dict
import logging

# Updated ctype mappings to include more types and clearer structured comments
ctype_to_python_ctype_mapping = {
    'void': 'None',
    'int': 'ctypes.c_int',
    'unsigned int': 'ctypes.c_uint',
    'long': 'ctypes.c_long',
    'unsigned long': 'ctypes.c_ulong',
    'long long': 'ctypes.c_longlong',
    'unsigned long long': 'ctypes.c_ulonglong',
    'short': 'ctypes.c_short',
    'unsigned short': 'ctypes.c_ushort',
    'char': 'ctypes.c_char',
    'unsigned char': 'ctypes.c_ubyte',
    'float': 'ctypes.c_float',
    'double': 'ctypes.c_double',
    'char*': 'ctypes.c_char_p'  # Enhanced support for char pointers (strings)
}

ctype_to_np_mapping = {
    'void': 'None',
    'int': 'np.int32',
    'unsigned int': 'np.uint32',
    'long': 'np.int64',
    'unsigned long': 'np.uint64',
    'long long': 'np.int64',
    'unsigned long long': 'np.uint64',
    'short': 'np.int16',
    'unsigned short': 'np.uint16',
    'char': 'np.int8',
    'unsigned char': 'np.uint8',
    'float': 'np.float32',
    'double': 'np.float64',
    'char*': 'str'
}


# Enhanced exception handling by extending the base Python Exception class specifically for C Header processing issues
class CHeaderProcessingError(Exception):
    """Specific exception class for C header processing errors."""
    pass


def read_c_header(file_path: str) -> str:
    """Refined file reading method with robust exception handling."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        if not content:
            raise ValueError(f"The file {file_path} is empty.")
        return content
    except FileNotFoundError as e:
        raise CHeaderProcessingError(f"File not found: {file_path}") from e
    except Exception as e:
        raise CHeaderProcessingError(
            f"Error reading file {file_path}: {str(e)}") from e


def parse_c_header(header_content: str) -> List[Dict]:
    # Improved regex for matching C functions, considering various return types and pointers
    func_pattern = re.compile(
        r'\b(\w+(\s+\w+)*\s*[*]*\s*\w+)\s*\(([^)]*)\)\s*;')
    # TODO: Ideally this would match whether the pointer was adjacent to the type or the name. Currently it only matches if it's adjacent to the name.
    param_pattern = re.compile(r'\s?(\w+)\s*([*])?(\w+)[,]?')

    if not header_content:
        raise CHeaderProcessingError("Header content cannot be empty.")

    functions = []
    for match in func_pattern.finditer(header_content):
        ret_type_name, _, params_section = match.groups()
        ret_type, func_name = ret_type_name.rsplit(" ", 1)
        # Handling for WINAPI and multi-word return types
        ret_type = ret_type.replace('WINAPI', '').strip().split()[-1]

        params = []
        for m in param_pattern.finditer(params_section):
            param_type, ptr, param_name = m.groups()
            # Normalizing param_type for consistency
            param_type = param_type.replace(' ', '')
            params.append(
                {'param_name': param_name, 'param_type': param_type,
                 'is_pointer': ptr is not None})

        functions.append({'func_name': func_name,
                          'return_type': ret_type.replace('WINAPI', '').strip(),
                          'params': params,
                          'has_pointer': any(p['is_pointer'] for p in params)})

    return functions

# Enhancing parameter transformation with clearer and more precise ctypes mappings


def pythonize_params(params: List[Dict]) -> List[str]:
    python_params = []
    for param in params:
        # Handling for typedefs and multi-word types
        ctype = '.'.join(param['param_type'].replace('*', '').split())
        python_type = ctype_to_python_ctype_mapping.get(
            ctype, f"Unhandled type: {ctype}")
        if 'Unhandled type' in python_type:
            raise CHeaderProcessingError(python_type)
        if param['is_pointer']:
            python_params.append(f'ctypes.pointer({python_type})')
        else:
            python_params.append(python_type)
    return python_params

# Generating more readable and idiomatic Python wrapper functions


def update_call_str_for_pointer(call_str: str, param: Dict) -> str:
    def wrap_pointer(s: str) -> str:
        if param['param_name'] == s.strip():
            s = f'ctypes.byref({param["param_name"]}_ptr.contents)'
        return s

    return ','.join(map(wrap_pointer, call_str.split(',')
        if ',' in call_str else [call_str]))

    # call_str.replace(
    #                 param['param_name'],
    #                 f"ctypes.byref({param['param_name']}_ptr.contents)")


def generate_wrapper(functions: List[Dict], module_name: str) -> str:
    wrapper_functions = [
        f"import ctypes\nimport {module_name}\nimport numpy as np\n\n# Auto-generated wrapper functions\n"]

    for func in functions:
        python_return_type = ctype_to_python_ctype_mapping.get(
            func['return_type'], 'ctypes.c_void_p')

        params_declaration, params_initialization = [], []
        pointers = []
        for i, param in enumerate(func['params']):
            # Simplifying to handle both pointer and non-pointer types accurately
            python_ctype = ctype_to_python_ctype_mapping.get(
                param['param_type'].replace('*', ''), 'ctypes.c_void_p')
            np_type = ctype_to_np_mapping.get(
                param['param_type'].replace('*', ''),
                'ctypes.c_void_p')
            if param['is_pointer']:
                # if the param is a pointer we handle this transparently
                pointers.append((i, param))
            else:
                params_declaration.append(f"{param['param_name']}: {np_type}")

            params_initialization.append(param['param_name'])
        for _, param in pointers:
            params_declaration.append(
                f"{param['param_name']}: {np_type} = None")

        params_str = ', '.join(params_declaration)
        call_str = ', '.join(params_initialization)

        wrapper_code = f"def {func['func_name']}({params_str}) -> {python_return_type}:\n"
        wrapper_code += f"    \"\"\"Auto-generated wrapper for {func['func_name']}\"\"\"\n"
        # Adding pointer handling
        for param in func['params']:
            python_ctype = ctype_to_python_ctype_mapping.get(
                param['param_type'].replace('*', ''), 'ctypes.c_void_p')
            if not param['is_pointer']:
                # Casting to the correct type
                wrapper_code += f"    {param['param_name']} = {python_ctype}({param['param_name']})\n"
            else:
                wrapper_code += f"    {param['param_name']}_ptr = ctypes.pointer({python_ctype})\n"
                wrapper_code += f"    if {param['param_name']} is not None:\n"
                wrapper_code += f"        {param['param_name']}_ptr.contents = {param['param_name']}\n"
                call_str = update_call_str_for_pointer(call_str, param)
        return_str = f"return {ctype_to_np_mapping[func['return_type']]}({module_name}.{func['func_name']}({call_str}))" if func[
            'return_type'] != 'void' else ""
        if func['return_type'] == 'void':
            return_str += f"    {module_name}.{func['func_name']}({call_str})\n\n"
        elif func['has_pointer']:
            for _, param in pointers:
                return_str += f",{ctype_to_np_mapping[func['return_type']]}({param['param_name']}_ptr.contents)"
        wrapper_code += f"    {return_str}\n\n"
        wrapper_functions.append(wrapper_code)

    return "".join(wrapper_functions)

# Streamlining the process of writing the generated code to a file


def write_wrapper_code(wrapper_code: str, output_path: str) -> None:
    try:
        import autopep8
        wrapper_code = autopep8.fix_code(wrapper_code) # Auto-formatting the code
    except ImportError:
        logging.warning("autopep8 not found. The generated code will not be auto-formatted.")
    try:
        with open(output_path, "w") as file:
            file.write(wrapper_code)
    except Exception as e:
        raise CHeaderProcessingError(
            f"Failed to write wrapper code: {str(e)}") from e


def main(header_path: str, output_path: str, module_name: str):
    try:
        header_content = read_c_header(header_path)
        functions = parse_c_header(header_content)
        wrapper_code = generate_wrapper(functions, module_name)
        write_wrapper_code(wrapper_code, output_path)
        print("Wrapper code successfully generated.")
    except CHeaderProcessingError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main(
        r"D:\CZI_scope\code\pymodules\thorlabs_apt\APTAPI.h",
        r"D:\CZI_scope\code\pymodules\thorlabs_apt\thorlabs_apt_wrapped.py",
        "thorlabs_apt")
