# Anagram function, that can takes sentences as well


word_a = "Ne at"
word_b = "anet"


def compare_words(first, second):
    lower_f = str.lower(first)
    lower_s = str.lower(second)
    first_sorted = ''.join(sorted(lower_f))
    second_sorted = ''.join(sorted(lower_s))
    f_replaced = first_sorted.replace(" ", "")
    s_replaced = second_sorted.replace(" ", "")
    return f_replaced == s_replaced

print(compare_words(word_a, word_b))

