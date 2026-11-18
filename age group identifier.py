age=int(input("Enter your age: "))
if age<0:
    print("Invalid age")
elif age<10:
    print("You are in child age")
elif age<18:
    print("You are in teenage")
elif age<25:
    print("You are in young age")
elif age<60:
    print("You are adult")
else:
    print("You are in old age")