# Practical 11: Sort a list in ascending and descending order without sort()

arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

# Ascending order (Bubble Sort)
asc_arr = arr.copy()
for i in range(n):
    for j in range(0, n - i - 1):
        if asc_arr[j] > asc_arr[j + 1]:
            asc_arr[j], asc_arr[j + 1] = asc_arr[j + 1], asc_arr[j]

# Descending order
desc_arr = arr.copy()
for i in range(n):
    for j in range(0, n - i - 1):
        if desc_arr[j] < desc_arr[j + 1]:
            desc_arr[j], desc_arr[j + 1] = desc_arr[j + 1], desc_arr[j]

print("Original list:", arr)
print("Ascending order:", asc_arr)
print("Descending order:", desc_arr)
