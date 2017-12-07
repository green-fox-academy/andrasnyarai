# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def power_and_base(base,exp):
    if base**exp == base:
        return base
    else:
        return base * power_and_base(base,exp-1)

print(power_and_base(5,3))