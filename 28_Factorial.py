# Python Program to find Factorial of a Number

def factorial(n):
    print("The factors of", n, "are:")
    for i in range (1, n+1):
        if n % i == 0:
           print(i)

num = int(input("Enter a number: "))

factorial(num)