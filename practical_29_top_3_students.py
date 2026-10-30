students = [
    ("Aarav", 85),
    ("Bhavna", 92),
    ("Chirag", 78),
    ("Divya", 95),
    ("Eshan", 88),
    ("Farhan", 91)
]
top_3 = sorted(students, key=lambda s: s[1], reverse=True)[:3]
print(top_3)
