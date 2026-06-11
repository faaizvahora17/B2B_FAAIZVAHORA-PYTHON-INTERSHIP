numbers = [10, 20, 30, 40, 50,100]
print(f"List: {numbers}\n")

built_in_sum = sum(numbers)
print("--- Method 1 (Built-in) ---")
print(f"Total = {built_in_sum}\n")

total = 0
for num in numbers:
    total += num  # Add each element to total

print("--- Method 2 (Manual Loop) ---")
print(f"Total = {total}")