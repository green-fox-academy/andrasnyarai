# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def string_x_to_y(words):
    if len(words) == 1:
        if words[0] == "x":
            return ""
        else:
            return words[0]
    if len(words) > 1:
        if words[len(words)-1] == "x":
            return string_x_to_y(words[:len(words)-1]) + ""
        else:
            return string_x_to_y(words[:len(words)-1]) + words[len(words)-1]

a = "xxxxxxxxxxabc123xxyxyxyxyxyxX"
print(string_x_to_y(str(a)))