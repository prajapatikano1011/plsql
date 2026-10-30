# Practical 7: Count how many times a value appears in a list

items = [10, 20, 30, 20, 40, 20, 50]
target = 20

count = 0
for x in items:
    if x == target:
        count += 1

print("List:", items)
print("Value", target, "appears", count, "times.")
