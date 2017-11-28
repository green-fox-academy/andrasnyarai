# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

a = []
b = []
size = 4

for i in range(size):
   b = []
   for j in range(size):
       if i == j:
           b.append(' ')
       else:
           b.append('#')
   a.append(b)

print(a)