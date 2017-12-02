x = "dog goat dad duck doodle never dog goat dad duck doodle never"

def search_palindrome(candidate):
    palindromes = []
    for l in range(len(candidate)-2):
        for i in range(len(candidate)-2-l):
            if candidate[i:i+l+3] == ''.join(reversed(list(candidate[i:i+l+3]))):
                palindromes.append(candidate[i:i+l+3])
    return palindromes

print(search_palindrome(x))
