# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

fix = ["always", "takes", "longer", "than"]

quote2 = quote.split()

quote_begin = quote2[0:3]

quote_end = quote2[3:]

merge = quote_begin + fix + quote_end

longquote = ' '.join(merge)

print(longquote)