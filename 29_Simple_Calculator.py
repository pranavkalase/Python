# Python Program to create Simple Calculator

# This function Add Two numbers
def add(x, y):
    return x + y

#This function Subtracts Two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y
# This function divide two numbers
def divide(x, y):
    return x / y

print("select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.divide")

while True :
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1','2','3','4'):
        try :
            num1 = float(input("Enter First Number : "))
            num2 = float(input("Enter second NUmber : "))
        except ValueError:
            print("Invalid input.please enter a number")
            continue
        if choice == '1':
            print(f" {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice =='3':
            print(f"{num1} * {num2}= {multiply(num1 , num2)}")
        elif choice =='4':
            print(f"{num1} / {num2}= {divide(num1, num2)}")

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
                break
    else:
        print("Invalid Input")

