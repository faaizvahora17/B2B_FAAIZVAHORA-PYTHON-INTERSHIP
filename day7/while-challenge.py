count = 0         
number = -1      
print("Keep entering numbers. Enter 0 to stop.")
print("-" * 40)

while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    if number != 0:
        print(f"  You entered: {number}")
        count += 1  
print("-" * 40)
print(f"You entered {count} number(s) before stopping.")