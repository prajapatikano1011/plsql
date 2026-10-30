numbers = [2, 3, 5, 6, 8, 9, 11, 12]
cubes = list(map(lambda x: x ** 3, filter(lambda x: x % 3 == 0, numbers)))
print(cubes)
