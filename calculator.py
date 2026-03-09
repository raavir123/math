
import os

num1 = int(os.getenv("NUM1"))
num2 = int(os.getenv("NUM2"))
choice = int(os.getenv("CHOICE"))

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

    
