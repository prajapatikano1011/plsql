students = {
    "RS": [20, "B.Tech", "Python"],
    "PP": [19, "BCA", "Java"],
    "AV": [22, "B.Sc", "Maths"],
    "SM": [18, "B.Tech", "Physics"],
    "KD": [21, "BCA", "Database"]
}

youngest_key = min(students, key=lambda k: students[k][0])
youngest_age = students[youngest_key][0]

print("Youngest student initial:", youngest_key)
print("Details (Age, Degree, Favorite Subject):", students[youngest_key])
