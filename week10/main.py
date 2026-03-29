import math_tools

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = math_tools.add(num1, num2)
elif choice == '2':
    result = math_tools.subtract(num1, num2)
elif choice == '3':
    result = math_tools.multiply(num1, num2)
elif choice == '4':
    result = math_tools.divide(num1, num2)
else:
    result = "Invalid Choice"

print("Result:", result)
