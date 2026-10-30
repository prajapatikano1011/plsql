# Practical 61: Check palindrome without converting into string

lst = [10, 20, 30, 20, 10]
print("Input list:", lst)

is_pal = True
left = 0
right = len(lst) - 1

while left < right:
    if lst[left] != lst[right]:
        is_pal = False
        break
    left += 1
    right -= 1

if is_pal:
    print("The list is a Palindrome.")
else:
    print("The list is NOT a Palindrome.")
