# - Create a recursive function called `refactorio`
#   that returns it's input's factorial
def refactorio(n):
    if n <= 1:
        return 1
    else:
        return n *refactorio(n-1)

print(refactorio(5))