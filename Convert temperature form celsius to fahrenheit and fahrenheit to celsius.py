print("Temperature converter")
print("1. Celsius to fahrenheit")
print("2. Fahrenheit to celsius")
choice=int(input("Enter your choice(1 or 2): ")
if choice==1:
    C=float(input("Enter temperature in celsius: ")
    F=(C*9/5)+32
    print("Temperature in fahrenheit is: ", F)
elif choice==2:
    F=float(input("Enter temperature in fahrenheit: ")
    C=(F-32)*5/9
    print("Temperature in Celsius is: ", C)
else:
    print("Invalid choice")
