# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs


verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

out = []

def create_new_verbs(q, w):
    for k in q:
        plus = w + k
        out.append(plus)
    return out

print(create_new_verbs(verbs, preverb))
