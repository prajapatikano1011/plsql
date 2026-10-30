# Practical 59: Separate numbers into positive, negative, and zero lists

nums = [15, -4, 0, 23, -8, 0, 42, -1, 0, 7]

positive = []
negative = []
zeroes = []

for n in nums:
    if n > 0:
        positive.append(n)
    elif n < 0:
        negative.append(n)
    else:
        zeroes.append(n)

print("Original list:", nums)
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeroes:", zeroes)
