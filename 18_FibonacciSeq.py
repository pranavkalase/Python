 # Python Program to Print Fibonacci sequnece upto n-th term
nterms = int(input("How many terms? "))

# First two terms
n1, n2 = 0, 1
count = 0

# check if the number term is valid
if nterms <= 0:
   print("Plese enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

