def count_lines(filename):
    try:
        line_count = 0

        with open(filename, 'r'):
            for _ in filename:
                line_count += 1

        return line_count

    except FileNotFoundError:
        print("File not found.")
        return 0

filename = input("Enter the file path: ")
print("Number of lines:", count_lines(filename))
