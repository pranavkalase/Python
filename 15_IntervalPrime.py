 # Python Program to check prime mumbers within an interval

lower = 900
upper = 1000

print(f"Prime numbers between the range of {upper} and {lower}  are")

for num in range(lower, upper +1):
    if num > 1 :
        for i in range(2 ,num ):
            if num % i == 0:
                break

        else:
             print(num)





