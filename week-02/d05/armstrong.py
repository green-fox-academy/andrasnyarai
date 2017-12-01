# Armstrong number checker

def armstrong(x):
    out = []
    tmp = list(str(x))
    l = len(str(x))
    for i in tmp:
        out.append(int(i)**l)
    if x == sum(out):
        return "the " + str(x) + " is an Armstrong number."
    else:
        return "the " + str(x) + " is not an Armstrong number."

q = input("Insert a number, and see if its Armstrong or not. --- ")

print(armstrong(int(q)))

