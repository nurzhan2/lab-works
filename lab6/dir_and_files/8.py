import os

def delete_file(path):
    if os.path.exists(path) and os.path.isfile(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted successfully.")
        else:
            print("No permission to delete the file.")
    else:
        print("File does not exist.")

file_path = input("Enter the file path to delete: ")
delete_file(file_path)
