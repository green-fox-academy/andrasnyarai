# Create a method that decrypts encoded-lines.txt
to_decrypt = "encoded-lines.txt"


def decrypt(file_name):
    with open(file_name) as f:
        for line in f:
            k = list(line.rstrip())
            tmp = []
            for i in k:
                if i is " ":
                    tmp.append(i)
                else:
                    tmp.append(chr(ord(i)-1))
            tmp_join = ''.join(tmp)
            print(tmp_join)


decrypt(to_decrypt)