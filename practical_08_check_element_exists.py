# Practical 8: Check if an element exists in a list

numbers = [10, 25, 40, 55, 70]
search_item = int(input("Enter number to search: "))

found = False
for val in numbers:
    if val == search_item:
        found = True
        break

if found:
    print(search_item, "is found in the list.")
else:
    print(search_item, "is not found in the list.")
