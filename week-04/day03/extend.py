
# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > b and c > a:
        return c

# Returns the median value of a list given as param
def median(pool):
    if len(pool) % 2 == 0:
        return pool[int((len(pool) - 1) / 2)], pool[int((len(pool)) / 2)]
    return pool[int((len(pool) - 1) / 2)]

# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouéáőűöüóí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    hun = list(hungarian)
    for i in range(len(hun)):
        if is_vovel(hun[i]):
            hun[i] = str(hun[i]) + 'v' + str(hun[i])
    return ''.join(hun)

