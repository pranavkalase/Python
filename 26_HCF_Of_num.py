# Python Program To find HCF of two numbers

# Define a function
def Compute_hcf(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("The HCF of", num1, "and", num2, "is", Compute_hcf(num1, num2))