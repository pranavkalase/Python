# Python Program to check if year is leaf year or not

# To get year integer input from user

year = int(input("Enter a Year: "))

if(year % 400 == 0 ) and (year % 100 == 0):
    print(f"{year} is a Leaf year")
elif(year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a Leaf Year")
else:
    print(f"{year} is not leaf year")