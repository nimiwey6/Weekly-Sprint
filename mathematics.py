number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))

#Addition
add = number1 + number2
print("Addition:", add)

#subtraction
sub = number1 - number2
print("Subtraction:", sub)

#product
product = number1 * number2
print("Product:", product)

#Division
if number2 != 0:
    print("Quotient:", number1 / number2)
else:
    print("Error: Division by zero is not allowed.")

