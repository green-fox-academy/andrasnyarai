x = "kerek kerek"

out = []
out_unique = []

def search_palindrome(candidate):
    for l in range(len(candidate)-2):
        for i in range(len(candidate)-2):
            if (candidate[i:i+l+3]) == ''.join(reversed(list((candidate[i:i+l+3])))):
                out.append(candidate[i:i+l+3])
    for i in out:
        if i not in out_unique:
            out_unique.append(i)
    return out_unique

print(search_palindrome(x))