weight=float(input("Enter your weight in kgs: "))
height=float(input("Enter your height in meter: "))
bmi=weight/height*height
print("Your bmi is: ", round(bmi,2))
if bmi<18.5
    print("category: Underweight")
elif bmi<25
    print("category: Normal weight")
elif bmi<30
    print("category: Over weight")
else
    print("Invalid")