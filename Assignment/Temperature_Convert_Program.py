# Fahrenheit and Celsius Conversion Program
fah = 0
cel = 0
# input > Select to Convert C to F or F to C
print("Temperature Convertion selected: \n1.Celsius to Fahrenheit. \n2.Fahrenheit to Celsius.")
sel = int(input("Select to Convert: "))

# input > number of C and number of F for Temp Convert
if sel == 1:
    print("Celsius to Fahrenheit.")
    cel = int(input("Enter number of Celsius: "))
    # process
    fDeg = (9/5) * cel + 32
    # output convert C and F
    print("°F = ", fDeg)
elif sel == 2:
    print("Fahrenheit to Celsius.")
    fah = int(input("Enter number of Fahrenheit: "))
    # process
    cDeg = (5/9) * (fah - 32)
    # output convert F and C
    print("°C =", cDeg)
else:
    print("Not Found!")