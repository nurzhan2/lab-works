import string

def generate_text_files():
    letters = string.ascii_uppercase

    for letter in letters:
        filename = f"{letter}.txt"

        with open(filename, 'w'):
            filename.write(f"This is file {filename}")

    print("26 text files created.")

generate_text_files()
