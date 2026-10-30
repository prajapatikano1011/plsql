# Practical 30: Interleave two lists

list1 = [1, 3, 5]
list2 = [2, 4, 6]

interleaved = []
len1 = len(list1)
len2 = len(list2)
max_len = max(len1, len2)

for i in range(max_len):
    if i < len1:
        interleaved.append(list1[i])
    if i < len2:
        interleaved.append(list2[i])

print("List 1:", list1)
print("List 2:", list2)
print("Interleaved list:", interleaved)
