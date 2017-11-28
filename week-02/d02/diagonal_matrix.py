# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

newlist = []
for x in range(0, 4):
    x = 1*x
    innerlist = []
    for y in range(1, 5):
        innerlist.append(y - y)
    newlist.append(innerlist)

print(newlist)

'''





a = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print() '''