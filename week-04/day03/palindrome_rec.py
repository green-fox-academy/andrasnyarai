def palindrome_check(candidate):
    if candidate == "" or len(candidate) == 1:
        return True
    if candidate[0] == candidate[len(candidate)-1]:
        n = 0
        return palindrome_check(candidate[n+1:len(candidate)-1])
    return False 