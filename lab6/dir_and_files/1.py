import os

def list_contents(path):
    try:
        directories = []
        files = []
        all_items = os.listdir(path)

        for item in all_items:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                directories.append(item)
            elif os.path.isfile(full_path):
                files.append(item)

        print("Directories:", directories)
        print("Files:", files)
        print("All items:", all_items)

    except FileNotFoundError:
        print("The specified path does not exist.")

path = input("Enter the directory path: ")
list_contents(path)
