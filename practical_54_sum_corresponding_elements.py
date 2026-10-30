# Practical 54: Sum of corresponding elements from two lists

list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 7, 9]

result = []
for i in range(len(list1)):
    result.append(list1[i] + list2[i])

print("List 1:", list1)
print("List 2:", list2)
print("Corresponding sum list:", result)
