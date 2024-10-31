import os
from os import path
import sys

if __name__ == '__main__':
    base_dir = path.realpath(path.dirname(__file__))
    # run structure.py
    python_exe = sys.executable
    ok = os.system(f'{python_exe} {base_dir}/structure.py')
    if ok != 0:
        print('Error in structure.py')
        sys.exit(1)
    # run gen.py
    ok = os.system(f'{python_exe} {base_dir}/gen.py')
    if ok != 0:
        print('Error in gen.py')
        sys.exit(1)
    # run compile.py
    ok = os.system(f'{python_exe} {base_dir}/compile.py')
    if ok != 0:
        print('Error in compile.py')
        sys.exit(1)
    # run post_process.py
    # ok = os.system(f'{python_exe} {base_dir}/post_process.py')
    # if ok != 0:
    #     print('Error in post_process.py')
    #     sys.exit(1)
    