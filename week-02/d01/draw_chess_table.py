# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#
x = 0

while x < 8:
    if x % 2 == 0:
        print(r" % % % %")
    if x % 2 > 0:
        print(r"  % % % %")
    x += 1