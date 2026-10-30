# Practical 21: Rotate a list left/right by n positions

nums = [1, 2, 3, 4, 5, 6, 7]
n = 2
n = n % len(nums)

# Left rotate: elements shift left
left_rotated = nums[n:] + nums[:n]

# Right rotate: elements shift right
right_rotated = nums[-n:] + nums[:-n]

print("Original list:", nums)
print(f"Left rotated by {n}:", left_rotated)
print(f"Right rotated by {n}:", right_rotated)
