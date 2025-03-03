def write_list_to_file(filename, data_list):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(str(item) + "\n")

data = ["Python", "Java", "C++", "JavaScript"]
filename = input("Enter the file path: ")
write_list_to_file(filename, data)
print("List written to file.")
