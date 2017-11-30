# Create a function that takes a string and a list of string as a parameter
# Returns the index of the string in the list where the first string is part of
# Returns -1 if the string is not part any of the strings in the list
input1 = ["this", "is", "what", "I'm", "searching", "in"]
key = "search"

# it can look for multiple instances

def find_index(string, list_of_string):
    look_up = []
    for i in list_of_string:
        if i.find(string) > -1:
            look_up += i
    if len(look_up) == 0:
        return -1
    else:
        return [i for i, s in enumerate(list_of_string) if str(string) in s]
     


print(find_index(key, input1))




