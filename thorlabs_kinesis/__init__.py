import os

# Add the common_dlls directory to the PATH
dll_directory = os.path.join(os.path.dirname(__file__), '__lib')
os.add_dll_directory(dll_directory)

if __name__ == '__main__':
    from motion_control import vertical_stage
    import numpy as np

    vertical_stage.TLI_BuildDeviceList()
    size = vertical_stage.TLI_GetDeviceListSize()
    if size > 0:
        device_list = np.zeros(size, dtype=np.uint8)
        vertical_stage.TLI_GetDeviceList(device_list)
        print(device_list)
    