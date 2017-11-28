# - Create a variable named `ai`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Print the sum of the elements in `ai`


ai = [3, 4, 5, 6, 7]

sum = 0

for i in range(int(len(ai))):
    sum += ai[i]

print("The list :" + str(ai))
print("The sum of the elements of the list is :" + str(sum))