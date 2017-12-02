# Create a function that takes two strings as a parameter
# Returns the starting index where the second one is starting in the first one
# Returns -1 if the second string is not in the first one


input = "this is what I'm searching in"
input_word = "searching"

def searching(sentence, word):
    s_index = sentence.find(word, 1)
    return s_index
    
print(searching(input, input_word))
