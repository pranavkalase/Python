# Taking Kilometers Input from user
km = float(input("Enter value in kilometers"))

# conversion factor
conv_fact = 0.621371

# calculate miles
miles = km * conv_fact
print('%0.2f kilometers is equal to %0.2f miles' %(km,miles))