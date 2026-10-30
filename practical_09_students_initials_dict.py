students = {}

for i in range(5):
    name = input(f"Enter name of student {i+1}: ").strip()
    initials = "".join([part[0].upper() for part in name.split()])
    age = int(input(f"Enter age of {name}: "))
    degree = input(f"Enter degree of {name}: ").strip()
    fav_sub = input(f"Enter favorite subject of {name}: ").strip()
    students[initials] = [age, degree, fav_sub]

print("
Student Dictionary:")
print(students)
