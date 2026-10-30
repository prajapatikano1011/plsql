numbers = [10, 20, 30, 40, 50, 60, 70]
avg = sum(numbers) / len(numbers)
above_avg = list(filter(lambda x: x > avg, numbers))
print("Average:", avg)
print(above_avg)
