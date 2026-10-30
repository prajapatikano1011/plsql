# Practical 22: Remove all occurrences of a specific value

numbers = [10, 20, 30, 20, 40, 20, 50]
val_to_remove = 20

print("Original list:", numbers)

# Keep only values that are not target
filtered = [x for x in numbers if x != val_to_remove]

print(f"List after removing all {val_to_remove}:", filtered)
