# Practical 28: Find index of first and last occurrence of an element

nums = [10, 20, 30, 40, 20, 50, 20, 60]
target = 20

first_idx = -1
last_idx = -1

for i in range(len(nums)):
    if nums[i] == target:
        if first_idx == -1:
            first_idx = i
        last_idx = i

print("List:", nums)
print("Target:", target)
print("First occurrence index:", first_idx)
print("Last occurrence index:", last_idx)
