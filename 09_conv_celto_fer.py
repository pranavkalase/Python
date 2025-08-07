# Python Program to convert in temprature celcius to Fahrenheit

celcius = float(input("Enter temprature in celcius: "))

fahrenheit = (celcius *1.8) + 32

print(f"{celcius} degree celcius is equal to {round(fahrenheit, 2)} degree fahrenheit ")

# Python Porgram to convert in temprature fahrenheit to celcius

fr = float(input("Enter temprature in fahrenheit: "))
cel = (fr - 32)/ 1.8

print(f"{fr} degree fahrenheit is equal to {round(cel, 1)} degree celcius")