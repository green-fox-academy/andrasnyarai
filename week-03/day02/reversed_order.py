# Create a method that decrypts reversed-order.txt
to_decrypt = "reversed-order.txt"


def decrypt(file_name):
    with open(file_name) as f:
        for line in f:
            l = f.readlines()
        for item in l[::-1]:
            print(item)

decrypt(to_decrypt)