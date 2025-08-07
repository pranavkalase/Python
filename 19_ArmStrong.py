 # Python Program To check if the given number is Armstrong number or not
number = int(input("Enter The Number : "))
sum = 0

temp = number
while temp >0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if number == sum:
    print("The Number Is Armstrong Number")
else:
    print("The Number Is Not Armstrong Number")
