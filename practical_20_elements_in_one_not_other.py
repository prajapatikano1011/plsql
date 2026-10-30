# Practical 20: Elements present in one list but not another (Difference)

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

diff_a_b = []
for item in list_a:
    if item not in list_b:
        diff_a_b.append(item)

print("List A:", list_a)
print("List B:", list_b)
print("Elements in A but not in B:", diff_a_b)
