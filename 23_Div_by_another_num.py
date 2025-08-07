# Python Program to find number divisible by another number

# Take a list of numbers
num = [12, 24, 35, 70, 88, 120, 155]

#use anonymous function to filter
result = list(filter(lambda x: (x % 12 == 0), num))

print("Numbers divisible by 12 are",result)