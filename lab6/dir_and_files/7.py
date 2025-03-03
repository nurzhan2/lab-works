import shutil

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")

src = input("Enter the source file path: ")
dest = input("Enter the destination file path: ")
copy_file(src, dest)
