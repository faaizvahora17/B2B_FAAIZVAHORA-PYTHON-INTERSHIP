print("Simple Calculator Menu")
print("1. Add")
print("2. Subtract")
print("3. multipication")

choice = int(input("Enter choice (1 or 2 or 3): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
  result = num1 + num2
  print(f"Result: {int(result)}")
elif choice == 2:
  result = num1 - num2
  print(f"Result: {int(result)}")

elif choice ==3:
  result = num1 * num2
  print(f"Result: {int(result)}")

else:
  print("Invalid Choice")