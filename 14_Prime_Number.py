 # Program To check if Number is Prime or not

 # To Take Input From User
num = int(input("Enter a Number: "))

 # Define flag variable

flag = False


if num == 0 or num == 1 :
     print(f"{num} is not prime number")
elif num >1 :
     for i in range( 2, num):
         if num % i == 0:
             flag = True
             break

if flag :
     print(f"{num} is Not Prime Number")
else:
     print(f"{num} is A Prime Number")


