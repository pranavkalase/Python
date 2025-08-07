# Program to display power of 2 using annyomas function
nterms = int(input("How many terms? "))

result = list(map(lambda x: 2 ** x, range(nterms)))

print("The total terms are: ", nterms)
print("The series is: ")
for i in result:
    print("2 raised to power",i,"is" ,i)