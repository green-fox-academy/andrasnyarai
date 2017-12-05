# Create a method that find the 5 most common lottery numbers otos.csv

to_decrypt = "otos.csv"

def five_most_frequent(file_name):
    with open(file_name) as f:
        tmp = []
        remap = []
        for line in f:
            tmp.append(''.join(reversed(list(line.rstrip()))))
        for i in tmp:
            remap += (i[:i.find(' ')].replace(';tF', '')).split(';')

        out = []
        A = True
        while A is True:
            out.append(max(remap, key= remap.count))
            for i in out:
                while i in remap: remap.remove(i)
            if len(out) == 5:
                A = False

        for o in out:
            print(o[::-1])


five_most_frequent(to_decrypt)



