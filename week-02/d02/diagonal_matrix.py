# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

l = []

for i in range(4):
    temp = []
    for j in range(4):
        if i == j:
            temp.append('1')
        else:
            temp.append('0')
    l.append(temp)

for s in l:
    print(*s)