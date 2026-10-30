# Practical 19: Find common elements between two lists

list_a = [10, 20, 30, 40, 50]
list_b = [30, 40, 50, 60, 70]

common = []
for x in list_a:
    if x in list_b and x not in common:
        common.append(x)

print("List A:", list_a)
print("List B:", list_b)
print("Common elements:", common)
