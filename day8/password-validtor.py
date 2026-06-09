password = input("Enter password: ")

has_min_length = len(password) >= 8

has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break  
if has_min_length and has_digit:
    print("Valid Password")
else:
    print("Invalid Password")
   
    if not has_min_length:
        print("  - Password must be at least 8 characters long.")
    if not has_digit:
        print("  - Password must contain at least one number.")