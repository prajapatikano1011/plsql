# Practical 26: Swap two elements at given positions

items = [10, 20, 30, 40, 50]
print("Initial list:", items)

pos1 = 1  # 0-indexed position
pos2 = 3

items[pos1], items[pos2] = items[pos2], items[pos1]

print(f"After swapping index {pos1} and {pos2}:", items)
