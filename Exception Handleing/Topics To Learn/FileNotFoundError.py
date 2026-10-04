try:
    filename = input("Enter the file name: ")

    file = open(filename, "r")
    content = file.read()

    print(content.title())

    file.close()

except FileNotFoundError:
    print("File does not exist.")