# Practical 25: Find frequency of each element (build dictionary)

data = ["apple", "banana", "apple", "cherry", "banana", "apple"]

freq = {}
for item in data:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("List:", data)
print("Element frequencies:")
for k, v in freq.items():
    print(f"{k}: {v}")
