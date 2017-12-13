def anagram_check(first, second):
    lower_f = str.lower(first)
    lower_s = str.lower(second)
    first_sorted = ''.join(sorted(lower_f))
    second_sorted = ''.join(sorted(lower_s))
    f_replaced = first_sorted.replace(" ", "")
    s_replaced = second_sorted.replace(" ", "")
    return f_replaced == s_replaced