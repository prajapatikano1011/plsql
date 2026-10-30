# Practical 23: Find all pairs in a list that sum to a target value

arr = [2, 4, 3, 5, 7, 8, 9, 1]
target = 10

pairs = []
seen = set()

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            pair = tuple(sorted((arr[i], arr[j])))
            if pair not in seen:
                seen.add(pair)
                pairs.append(pair)

print("List:", arr)
print("Target:", target)
print("Pairs summing to target:", pairs)
