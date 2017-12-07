# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def string_x_to_y(words):
    last_item = words[0]
    if len(words) == 1:
            return last_item
    else:
        return last_item + "*" + string_x_to_y(words[1:])

a = "xxxxxxxxxxabc123xxyxyxyxyxyxX"
print(string_x_to_y(str(a)))

