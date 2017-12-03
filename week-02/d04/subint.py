# Create a function that takes a number and a list of numbers as a parameter
# Returns the indeces of the numbers in the list where the first number is part of
# Returns an empty list if the number is not part any of the numbers in the list


input = [1, 11, 50, 16, 1, 18, 19, 29, 21]

num = 1
out = []

def search_number_index(indicator, num_list):
    for i in num_list:
        out.append(str(i))
    return [i for i, s in enumerate(out) if str(num) in s]

print(search_number_index(num, input))
