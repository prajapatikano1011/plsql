# Practical 64: Frequency table of elements in a list

items = [1, 2, 3, 2, 4, 1, 5, 2, 3, 1, 4, 4]

# Count frequencies
freq_dict = {}
for x in items:
    freq_dict[x] = freq_dict.get(x, 0) + 1

print("List:", items)
print("\n--- FREQUENCY TABLE ---")
print(f"{'Element':<10} | {'Frequency':<10}")
print("-" * 25)
for elem in sorted(freq_dict.keys()):
    print(f"{elem:<10} | {freq_dict[elem]:<10}")
