# Practical 4: Reverse a list without using reverse()

original_list = [10, 20, 30, 40, 50]
print("Original list:", original_list)

# Method 1: using slicing
reversed_list = original_list[::-1]
print("Reversed list (slicing):", reversed_list)

# Method 2: using loop
rev_manual = []
for i in range(len(original_list) - 1, -1, -1):
    rev_manual.append(original_list[i])
print("Reversed list (loop):", rev_manual)
