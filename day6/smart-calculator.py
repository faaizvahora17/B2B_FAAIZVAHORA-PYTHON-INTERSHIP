print("=====================================")
print("   PYTHON SMART CALCULATOR  ")
print("=====================================")

while True:
    print("\n---Main Menu---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
  
    choice = input("Enter choice (1-5): ")
  
    if choice == '5':
      print("\nThank you for using Smart Calculator. Goodbye! ")
      break
    
    if choice in ['1', '2', '3', '4']:
      try:
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))
    except ValueError:
      print(" Invalid input! Please enter numbers only.")
      continue
