# Practical 47: 15 numbers separated into even and odd with statistics

numbers = [14, 27, 33, 40, 52, 61, 78, 85, 92, 101, 12, 23, 34, 45, 56]
print("Numbers:", numbers)

evens = []
odds = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print("\n--- EVEN NUMBERS ---")
print("List:", evens)
print("Count:", len(evens))
print("Sum:", sum(evens))
print("Max:", max(evens) if evens else None)
print("Min:", min(evens) if evens else None)

print("\n--- ODD NUMBERS ---")
print("List:", odds)
print("Count:", len(odds))
print("Sum:", sum(odds))
print("Max:", max(odds) if odds else None)
print("Min:", min(odds) if odds else None)
