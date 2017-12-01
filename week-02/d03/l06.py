# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

# a set solution to the problem

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

marks = [4 ,8 ,14 ,16]


def matching(list_of):
    z = set(marks) & set(list_of)
    if set(marks) == z:
        return True
    else:
        return False

print(matching(list_of_numbers))
    
