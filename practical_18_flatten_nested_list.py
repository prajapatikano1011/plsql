# Practical 18: Flatten a nested list

nested = [[1, 2], [3, 4], [5, 6], [7, 8]]
print("Nested list:", nested)

flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)

print("Flattened list:", flat)
