from functools import reduce

numbers = [23, 65, 12, 89, 45, 78, 34]
max_num = reduce(lambda a, b: a if a > b else b, numbers)
print(max_num)
