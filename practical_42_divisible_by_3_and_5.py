# Practical 42: Filter numbers divisible by both 3 and 5

nums = list(range(1, 101))
div_3_and_5 = [n for n in nums if n % 3 == 0 and n % 5 == 0]

print("Numbers from 1 to 100 divisible by 3 and 5 (multiples of 15):")
print(div_3_and_5)
