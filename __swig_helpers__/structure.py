import os
import re
from pathlib import Path
import logging

# Improved the template for SWIG interface files for better readability and management
swig_template = """%module {module_name}

%include <windows.i> // Required for Windows-specific types

#define {API_NAME}DLL_EXPORTS 


%{{
#define {API_NAME}DLL_EXPORTS 
#define PY_ARRAY_UNIQUE_SYMBOL {module_name}_PY_ARRAY_UNIQUE_SYMBOL
#define SWIG_FILE_WITH_INIT
#include "{header_file}"
%}}

%include "numpy.i" // Required for NumPy support
%include "typemaps.i" // Required for custom type mappings

%init %{{
import_array();
%}}

// ignore problematic functions that won't compile (I don't know why)
// TODO: Investigate why these functions are problematic and fix them
{ignore}

%include "{header_file}"
"""


def preprocess_h(root, file):

    with open(os.path.join(root, file), 'r') as f:
        lines = f.readlines()
    expr = re.compile(r'^\s*\w+_API\b\s(\w+)\b\s__cdecl')
    for i, line in enumerate(lines):
        if expr.match(line):
            lines[i] = re.sub(expr, r'\1', line)  # Remove API and __cdecl
    with open(os.path.join(root, file), 'w') as f:
        f.writelines(lines)


def proper_to_snake_case(name):
    # Simplified regex for converting camelCase or PascalCase to snake_case
    return re.sub(r'(?<![A-Z])(?=[A-Z])(?<!^)', '_', name).lower()


def ensure_dir_and_files(root, original_path, header_file):

    problem_defs = [
        'PPC2_RequestVoltageSource',
        'PPC2_GetVoltageSource',
        'PPC2_SetVoltageSource',
        'SBC_RequestTriggerSwitches',
        'KIM_SetTrigParamsParameters',
        'LD_GetMaxCurrentDigPot',
        'LS_GetMMIParams',
        'LS_SetMMIParams',
        'LS_GetMMIParams',
        'LS_SetMMIParams',
        'KLC_RequestParams',
        'KLC_GetParamsExt',
        'KLC_GetParams',
        'KLC_SetParamsExt',
        'KLC_SetParams',
        'KLC_GetParamsBlock',
        'KLC_SetParamsBlock',
        'SC_GetMMIParamsBlock',
        'SC_SetMMIParamsBlock',
        'SG_RequestIOsettings',
        'SG_RequestHubAnalogOutput',
    ]

    try:
        # Using pathlib for all path operations, enhancing reliability and simplifying code
        original_path = Path(original_path)
        base_name = original_path.stem
        parts = base_name.split('.')
        new_dir = root
        for part in parts[1:-1]:
            part = proper_to_snake_case(part)
            if part == 'thor_labs':
                part = 'thorlabs'
            new_dir = new_dir / part

        # Creating directories
        new_dir.mkdir(parents=True, exist_ok=True)
        new_name = '.'.join(
            map(proper_to_snake_case, original_path.name.split('.')))
        new_path = new_dir / new_name[1:]  # Removing the thorlabs prefix

        # Creating __init__.py file using pathlib to ensure it's treated as a package
        init_file = new_dir / '__init__.py'
        init_file.touch(exist_ok=True)
        print(f"Created file: {init_file}")

        module_name = new_path.stem.split('.')[-1]
        swig_file_path = new_dir / f'{module_name}.i'
        # Improved file reading using pathlib's read_text method
        header_lines = original_path.read_text().splitlines()
        api_name = next(
            (line.split()[1] for line in header_lines
             if '__declspec' in line),
            None)
        ignore_set = set()
        for problem_def in problem_defs:
            for header_line in header_lines:
                if problem_def in header_line:
                    ignore_set.add(problem_def)
                    break

        ignore = '\n'.join(f'%ignore {problem_def};' for problem_def in ignore_set)
        api_name = api_name.split('_')[0] if api_name else ''
        swig_file_content = swig_template.format(
            module_name=module_name, header_file=header_file,
            API_NAME=api_name or '_', ignore=ignore)
        swig_file_path.write_text(swig_file_content)
        print(f"Created SWIG interface file: {swig_file_path}")

        return new_dir, swig_file_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


def main(base_dir):
    try:
        base_dir = Path(base_dir)
        include_dir = base_dir / '__include'
        if not base_dir.is_dir():
            print(f"{base_dir} is not a directory or does not exist.")
            return

        for root, dirs, files in os.walk(include_dir):
            for file in files:
                if file.endswith('.h'):
                    original_path = Path(root) / file
                    new_directory, _ = ensure_dir_and_files(
                        base_dir, original_path, file)
                    if not new_directory:
                        continue
                    logging.info(f"Created directory: {new_directory}")
    except Exception as e:
        print(f"An error occurred in main: {e}")


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler(
            r'D:\CZI_scope\code\logs\pymodules_thorlabs_kinesis_structure.log',
            'w', 'utf-8')])
    try:
        base_dir = Path(r'D:\CZI_scope\code\pymodules\thorlabs_kinesis\__init__.py').resolve().parent
        main(base_dir)
    except Exception as e:
        print(f"Failed to start the process: {e}")
