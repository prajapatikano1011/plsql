salaries = [35000, 45000, 50000, 38000, 70000]
hike_salaries = list(map(lambda s: s * 1.10, filter(lambda s: s > 40000, salaries)))
print(hike_salaries)
