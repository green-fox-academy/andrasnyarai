# Create a function that takes a list of numbers as a parameter
# Returns a list of numbers where every number in the list occurs only once


input = [1, 11, 34, 11, 52, 61, 1, 34]

new_list = []

for i in input:
  if i not in new_list:
    new_list.append(i)

print(new_list)