# Practical 24: Separate even and odd numbers into two lists

numbers = [12, 7, 19, 24, 33, 40, 55, 62]

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Original numbers:", numbers)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
