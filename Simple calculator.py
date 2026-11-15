def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Division is not allowed"
a=float(input("Enter first number: ")
b=float(input("Enter second number: ")
print("1. Addition")
print("2. substraction")
print("3. Multiplication")
print("4. Division")
choice=int(input("Enter your choice(1 to 4): ")
if choice==1:
    print("result= ", add(a,b))
elif choice==2:
    print("result= ", sub(a,b))
elif choice==3:
    print("result= ", mul(a,b))
elif choice==4:
    print("result= ", div(a,b))
else:
    print("Invalid choice")
