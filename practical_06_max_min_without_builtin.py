# Practical 6: Find maximum and minimum without using max() and min()

arr = [34, 12, 89, 5, 67, 23]
print("List:", arr)

maximum = arr[0]
minimum = arr[0]

for val in arr:
    if val > maximum:
        maximum = val
    if val < minimum:
        minimum = val

print("Maximum element:", maximum)
print("Minimum element:", minimum)
