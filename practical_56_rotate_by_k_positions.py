# Practical 56: Rotate list by k positions (left and right)

nums = [10, 20, 30, 40, 50, 60]
k = 2

k = k % len(nums)

# Left rotation
left_rot = nums[k:] + nums[:k]

# Right rotation
right_rot = nums[-k:] + nums[:-k]

print("Original list:", nums)
print(f"Left rotation by {k}:", left_rot)
print(f"Right rotation by {k}:", right_rot)
