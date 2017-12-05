# Create a method that decrypts the duplicated-chars.txt
to_decrypt = "duplicated-chars.txt"


def decrypt(file_name):
    with open(file_name) as f:
        for line in f:
            k = line.rstrip()
            k = list(k)
            del k[::2]
            print(''.join(k))

decrypt(to_decrypt)





