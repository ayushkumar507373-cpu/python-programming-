unit=int(input("Enter units: ")
if unit<0:
    print("Invalid unit")
elif unit<=100:
    bill=unit*5
    print("Your electricity bill is:Rs. ", bill)
elif unit<=200:
    bill=unit*7
    print("Your electricity bill is:Rs.", bill)
elif unit<=300:
    bill=unit*9
    print("Your electricity bill is:Rs. ", bill)
else:
    bill=unit*12
    print("Your electricity bill is:Rs.", bill)