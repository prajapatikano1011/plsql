numbers = [15, 20, 30, 45, 50, 60, 72, 90]
divisible = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print(divisible)
