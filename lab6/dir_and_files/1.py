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

        print("Каталоги:", directories)
        print("Файлы:", files)
        print("Все элементы:", all_items)

    except FileNotFoundError:
        print("Указанный путь не существует.")

path = input("Введите путь к директории: ")
list_contents(path)
