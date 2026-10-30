# Practical 12: Copy a list (shallow copy) and show it doesn't affect the original

orig = [10, 20, 30, 40]
copied = orig.copy()

print("Original list before change:", orig)
print("Copied list before change:", copied)

copied.append(50)
copied[0] = 999

print("\nAfter modifying only copied list:")
print("Original list:", orig)
print("Copied list:", copied)
