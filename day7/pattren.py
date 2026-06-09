print("--- Method 1: String Multiplication ---")
for i in range(1, 6):
    print("*" * i)

print()  
print("--- Method 2: Nested Loop ---")
for i in range(1, 6):      
    for j in range(i):      
        print("*", end="")  
    print()            