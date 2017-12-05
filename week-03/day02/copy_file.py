# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

filename_1 = "multiple-lines.txt"
filename_2 = "multiple-lines-copy.txt"

def copy_machine(a, b):
    try:
        with open(a) as f:
            with open(b, "w") as f1:    
                for line in f:
                    f1.write(line)
                return True
    except:
        pass
        



print(copy_machine(filename_1, filename_2))

