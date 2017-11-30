# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

expression = input("Type the expression in the following format <* 4 5> or <// 9 3> which means <4 * 5> or <9 // 3>  ")
expression = expression.replace(" ", "")
a = (expression[0])
b = (expression[1])
c = (expression[2])

b = str(b)
c = str(c)

A = False
B = False
tmp = ""

operators = ["+", "-", "*", "/", "%"]
for g in operators:
    if g == a:
        tmp += g
        A = True

operators_ext = ["/", "*"]
for m in operators_ext:
    if m == b and a:
        tmpx = ""
        tmpx += m + m
        B = True

if A is True and B is False:
    print(eval(b + tmp + c))
if A is True and B is True:
    d = (expression[3])
    print(eval(c + tmpx + d))
if A is False and B is False:
    print("ERROR!")