# Practical 46: Merge two lists, remove duplicates, and sort

list1 = [10, 45, 23, 78, 12, 45]
list2 = [50, 12, 89, 23, 67, 90]

merged = list1 + list2

# Remove duplicates
unique_list = []
for item in merged:
    if item not in unique_list:
        unique_list.append(item)

# Ascending order
unique_list.sort()
print("Ascending order:", unique_list)

# Descending order
unique_list.reverse()
print("Descending order:", unique_list)
