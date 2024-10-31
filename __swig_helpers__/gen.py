import os
import subprocess

# Base directory containing the SWIG interface files
base_dir = r'D:\CZI_scope\code\pymodules\thorlabs_kinesis\motion_control'

# Path to the SWIG executable
swig_path = r'D:\swigwin-4.2.1\swig.exe'

# Include directory path for SWIG
include_dirs = [
    r'C:\Users\User\mambaforge\envs\rich\include',
    os.path.join(os.path.dirname(base_dir), '__include')
]

# Walk through the base directory and process each .i SWIG interface file
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.i'):
            interface_file = os.path.join(root, file)
            print(f"Processing SWIG interface file: {interface_file}")

            # Construct and execute the SWIG command
            swig_cmd = [
                swig_path,
                '-python',
                '-c++',
                *map(lambda x: f'-I{x}', include_dirs),
                interface_file
            ]
            result = subprocess.run(swig_cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Successfully generated Python wrapper for {file}")
            else:
                print(
                    f"Error generating Python wrapper for {file}: {result.stderr}")
