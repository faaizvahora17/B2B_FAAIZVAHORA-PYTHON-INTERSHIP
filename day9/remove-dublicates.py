original_list = [1, 2, 2, 3, 4, 4, 5,5, 1, 3]
print(f"Original List: {original_list}\n")

unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("--- Method 1 (Loop) ---")
print(f"Clean List: {unique_list}\n")

clean_set_list = list(set(original_list))
print("--- Method 2 (set) ---")
print(f"Clean List: {clean_set_list}")