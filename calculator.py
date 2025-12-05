
def add(x,y):
    return x+y 
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        print("cannot divide by 0")
    else:
        return x/y
print("Press 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice =='1':
    print(add(num1,num2))
elif choice =='2':
    print(subtract(num1,num2))
elif choice =='3':
    print(multiply(num1,num2))
elif choice =='4':
    print(divide(num1,num2))
else:
    print("Invalid input")

