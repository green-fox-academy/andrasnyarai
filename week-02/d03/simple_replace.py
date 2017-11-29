example = "In a dishwasher far far away";

# I would like to replace "dishwasher" with "galaxy" in this example
# Please fix it for me!
# Expected ouput: In a galaxy far far away

print(example.replace("dishwasher", "galaxy"))

# more permanent solution

b = example.split()

b[2] = "galaxy"

print(*b)

c = ' '.join(b)

print(c)