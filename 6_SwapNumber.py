# Program To Swap two variables

x = int(input("Enter  Value Of X: "))
y = int(input("Enter value of y: "))

# Create temporary variable and swap the values
temp = x
x = y
y = temp

print(f"The value of x after swapping {x}")
print(f"The value of x after swapping {y}")

