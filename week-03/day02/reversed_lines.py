# Create a method that decrypts reversed-lines.txt
to_decrypt = "reversed-lines.txt"


def decrypt(file_name):
    with open(file_name) as f:
        for line in f:
            k = line.rstrip()
            k = list(k)
            print(''.join(reversed(k)))

decrypt(to_decrypt)