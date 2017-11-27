# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.
a = input("Insert number here: ")

if int(a) % 2 == 0:
  print("Even")
if int(a) % 2 > 0:
  print("Odd")

