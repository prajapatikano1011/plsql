# Practical 67: Menu-driven Student Record Management System using lists
# Each student record: [roll_no, name, marks]

students = [
    [1, "Rohit", 85],
    [2, "Ananya", 92],
    [3, "Manish", 74]
]

while True:
    print("\n=============================")
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("=============================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Sort by name")
    print("7. Sort by marks")
    print("8. Display topper")
    print("9. Display average marks")
    print("10. Exit")

    choice = input("Enter choice (1-10): ").strip()

    if choice == '1':
        roll = int(input("Enter Roll No: "))
        name = input("Enter Student Name: ").strip()
        marks = float(input("Enter Marks: "))
        students.append([roll, name, marks])
        print("Student added successfully.")

    elif choice == '2':
        if not students:
            print("No records found.")
        else:
            print(f"{'Roll':<6} {'Name':<15} {'Marks':<6}")
            print("-" * 30)
            for s in students:
                print(f"{s[0]:<6} {s[1]:<15} {s[2]:<6}")

    elif choice == '3':
        roll = int(input("Enter Roll No to search: "))
        found = False
        for s in students:
            if s[0] == roll:
                print(f"Record found -> Roll: {s[0]}, Name: {s[1]}, Marks: {s[2]}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == '4':
        roll = int(input("Enter Roll No to update: "))
        found = False
        for s in students:
            if s[0] == roll:
                s[1] = input("Enter new Name: ").strip()
                s[2] = float(input("Enter new Marks: "))
                print("Record updated.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == '5':
        roll = int(input("Enter Roll No to delete: "))
        found = False
        for i in range(len(students)):
            if students[i][0] == roll:
                del students[i]
                print("Student record deleted.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == '6':
        students.sort(key=lambda x: x[1].lower())
        print("Records sorted alphabetically by name.")

    elif choice == '7':
        students.sort(key=lambda x: x[2], reverse=True)
        print("Records sorted by marks (highest first).")

    elif choice == '8':
        if students:
            topper = max(students, key=lambda x: x[2])
            print(f"Topper: {topper[1]} (Roll: {topper[0]}) with {topper[2]} marks.")
        else:
            print("No student records available.")

    elif choice == '9':
        if students:
            total_marks = sum(s[2] for s in students)
            avg = total_marks / len(students)
            print(f"Class Average Marks: {avg:.2f}")
        else:
            print("No student records available.")

    elif choice == '10':
        print("Exiting Student Management System.")
        break
    else:
        print("Invalid option! Please choose 1 to 10.")
