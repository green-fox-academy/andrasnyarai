# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def takes_string(file_name):
    try:
        with open(str(file_name)) as text:
            return len(text.readlines())
    except FileNotFoundError:
        return 0

string_ = "reversed-lines.txt"

print(takes_string(string_))