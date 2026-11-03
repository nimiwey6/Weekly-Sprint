#Calculating and displaying the total and average marks of 3 subjects
subject1 = int(input("Enter the score of the first subject: "))
subject2 = int(input("Enter the score of the second subject: "))
subject3 = int(input("Enter the score of the third subject: "))

Total = subject1 + subject2 + subject3

Averge = Total / 3

print(f"The Total score of all three subject is {Total} and the Averge score is {Averge}")