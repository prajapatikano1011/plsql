# Practical 33: Group elements by a condition (e.g. length of strings)

words = ["cat", "dog", "apple", "pear", "banana", "kiwi", "bat"]

groups = {}
for w in words:
    length = len(w)
    if length not in groups:
        groups[length] = []
    groups[length].append(w)

print("Words:", words)
print("Grouped by length:")
for length, w_list in groups.items():
    print(f"Length {length}: {w_list}")
