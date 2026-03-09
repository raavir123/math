print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Divison")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

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

    
