# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

open_file = open('my-file.txt', "w")
try:
    open_file.write("Nyárai András")
    open_file.close()
except:
    Print("Unable to write file: my-file.txt")