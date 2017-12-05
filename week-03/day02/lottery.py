# Create a method that find the 5 most common lottery numbers otos.csv
to_decrypt = "otos.csv"

from collections import Counter

def five_most_frequent(file_name):
    with open(file_name) as f:
        tmp = []
        remap = []
        for line in f:
            tmp.append(''.join(reversed(list(line.rstrip()))))
        for i in tmp:
            remap += (i[:i.find(' ')].replace(';tF', '')).split(';')
        most_common_elements = [lot for lot, lot_count in Counter(remap).most_common(5)]
        for o in most_common_elements:
            print(o[::-1])



five_most_frequent(to_decrypt)