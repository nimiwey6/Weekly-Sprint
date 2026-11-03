#splitting bill payment
bill = float(input("Enter your Total bill: "))
print("Your total bill is " , bill)

people = int(input("How many people will be splitting the bill?: "))

if people > 0:
    print("Each person is to pay:", bill / people)
else:
    print("Error: Division by zero is not allowed.")
