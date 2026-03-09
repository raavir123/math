
import os
print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Divison")

num1 = float(os.environ.get("NUM1", 10))
num2 = float(os.environ.get("NUM2", 5))
choice = os.environ.get("CHOICE", "1")


if choice == '1':
    print("Result:", num1 + num2)

 elif choice == '2':
    print("Result:", num1 - num2)

 elif choice == '3':
    print("Result:", num1 * num2)

 elif choice =='4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! division by zero.")

else:
    print("Invalid option")        

    
