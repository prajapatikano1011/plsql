numbers = [12, 45, 23, 12, 78, 45, 90, 23, 11]
unique_numbers = sorted(filter(lambda x: numbers.index(x) == numbers.index(x) if numbers.count(x) >= 1 else False, dict.fromkeys(numbers)))
print(unique_numbers)
