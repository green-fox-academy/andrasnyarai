# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

marks = [4 ,8 ,12 ,16]


x = 0
for i in marks:
    if i in list_of_numbers:
        x += 1

if x == 0
    print(True)
          