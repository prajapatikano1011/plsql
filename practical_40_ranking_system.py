students = [("Aarav", 85), ("Bhavna", 92), ("Chirag", 78), ("Divya", 95), ("Eshan", 88)]
ranked_students = sorted(students, key=lambda s: s[1], reverse=True)

for rank, (name, marks) in enumerate(ranked_students, start=1):
    print(f"Rank {rank}: {name} - {marks}")
