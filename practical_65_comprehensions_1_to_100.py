# Practical 65: List comprehensions for numbers 1 to 100

squares = [x**2 for x in range(1, 101)]
cubes = [x**3 for x in range(1, 101)]
evens = [x for x in range(1, 101) if x % 2 == 0]
odds = [x for x in range(1, 101) if x % 2 != 0]
multiples_of_5 = [x for x in range(1, 101) if x % 5 == 0]

print("1. First 10 Squares:", squares[:10], "...")
print("2. First 10 Cubes:", cubes[:10], "...")
print("3. Even numbers (1 to 20):", evens[:10], "...")
print("4. Odd numbers (1 to 20):", odds[:10], "...")
print("5. Multiples of 5:", multiples_of_5)
