# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.


def string_x_to_y(words):
    if len(words) == 1:
        if words[0] == "x":
            return "y"
        else:
            return words[0]
    if len(words) > 1:
        if words[len(words)-1] == "x":
            return string_x_to_y(words[:len(words)-1]) + "y"
        else:
            return string_x_to_y(words[:len(words)-1]) + words[len(words)-1]

a = "xxxxxxxxxxabc123xxyxyxyxyxyxX"
print(string_x_to_y(str(a)))