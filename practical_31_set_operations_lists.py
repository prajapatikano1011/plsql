# Practical 31: Intersection, union, and difference of two lists

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

# Intersection
intersection = [x for x in a if x in b]

# Union (unique elements from both)
union = a.copy()
for x in b:
    if x not in union:
        union.append(x)

# Difference (a - b)
difference = [x for x in a if x not in b]

print("List A:", a)
print("List B:", b)
print("Intersection:", intersection)
print("Union:", union)
print("Difference (A - B):", difference)
