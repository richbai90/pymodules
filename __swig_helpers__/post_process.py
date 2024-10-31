import os

def main(base_dir):
    '''
    Walk through the base directory and delete anything that isn't a pyd or py file.
    '''
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if not file.endswith('.pyd') and not file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"Deleting {file_path}")
                os.remove(file_path)
                
if __name__ == '__main__':
    base_dir = r'D:\CZI_scope\code\pymodules\thorlabs_kinesis\motion_control'
    main(base_dir)