# Practical 44: Accept integers and remove duplicates without using set

raw_input = input("Enter integers separated by space: ")
numbers = [int(x) for x in raw_input.split()]

unique_nums = []
for n in numbers:
    if n not in unique_nums:
        unique_nums.append(n)

print("Original list:", numbers)
print("Unique list:", unique_nums)
