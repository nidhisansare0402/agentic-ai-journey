import calculator

print("Welcome to the calculator!")

a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide") 

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = calculator.add(a, b)
    print(f"The result of addition is: {result}")
elif choice == '2':
    result = calculator.subtract(a, b)
    print(f"The result of subtraction is: {result}")
elif choice == '3':
    result = calculator.multiply(a, b)
    print(f"The result of multiplication is: {result}")
elif choice == '4':
    result = calculator.divide(a, b)
    print(f"The result of division is: {result}")

