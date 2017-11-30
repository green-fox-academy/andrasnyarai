# Create a function that takes a list of numbers as a parameter
# Returns a list of numbers where every number in the list occurs only once

input = [1, 11, 34, 11, 52, 61, 1, 34, 66, 66, 7]

new_list = []
def only_once(l_numbers):

  for i in l_numbers:
    if i not in new_list:
      new_list.append(i)

  return new_list

print(only_once(input))
