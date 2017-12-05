# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"


def open_file():
    try:
        file1 = open('my-file.txt')
        print(file1.readline())
    except FileNotFoundError:
        print("Unable to read file: my-file.txt")

open_file()
