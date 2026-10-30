# Practical 63: Find missing numbers between min and max value

nums = [4, 7, 10, 2, 9, 3]
print("Given list:", nums)

min_val = min(nums)
max_val = max(nums)

missing = []
for val in range(min_val, max_val + 1):
    if val not in nums:
        missing.append(val)

print(f"Range: from {min_val} to {max_val}")
print("Missing numbers:", missing)
