numbers = [45, 12, 89, 34, 89, 78, 23]
max_val = max(numbers)
without_max = list(filter(lambda x: x < max_val, numbers))
second_largest = max(without_max)
print(second_largest)
