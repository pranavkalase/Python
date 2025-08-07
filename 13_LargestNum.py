 # Program To Find the Largest Number among the three input numbers
number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
number3 = int(input("Enter Third Number: "))
if number1 > number2 and number1 > number3:
    largest = number1
elif number2 > number1 and number2 > number3:
    largest = number2
else:
    largest = number3
print("The Largest Number among the three numbers is:", largest)
