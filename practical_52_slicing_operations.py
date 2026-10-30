# Practical 52: Slicing operations on list of numbers

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("List:", numbers)

# First five elements
first_five = numbers[:5]
print("First five elements:", first_five)

# Last five elements
last_five = numbers[-5:]
print("Last five elements:", last_five)

# Alternate elements
alternate = numbers[::2]
print("Alternate elements:", alternate)

# Reverse list using slicing
reversed_list = numbers[::-1]
print("Reverse using slicing:", reversed_list)
