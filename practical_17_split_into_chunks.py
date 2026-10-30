# Practical 17: Split a list into chunks of size n

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

chunks = []
for i in range(0, len(items), n):
    chunks.append(items[i:i + n])

print("Original list:", items)
print(f"Chunks of size {n}:", chunks)
