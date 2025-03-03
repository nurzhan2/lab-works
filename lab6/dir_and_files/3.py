import os

def check_path_info(path):
    if os.path.exists(path):
        directory = os.path.dirname(path)
        filename = os.path.basename(path)

        print("The path exists.")
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("The specified path does not exist.")

path = input("Enter the path: ")
check_path_info(path)
