#dictionary
students={
    "alice":50,
    "bob":78,
    "charlie":56,
    "path":50
}

choice = input("Enter your choice: ").upper()

    # A - Add a student
if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    # B - Update marks
elif choice == 'B':
        name = input("Enter student name to update: ")
        if name in students:
            new_marks = int(input("Enter new marks: "))
            students[name] = new_marks
            print("Marks updated!")
        else:
            print("Student not found!")

    # C - Search for a student
elif choice == 'C':
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name} : {students[name]}")
        else:
            print("Student not found!")

    # D - Display all
elif choice == 'D':
        if len(students) == 0:
            print("No students in the record.")
        else:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(name, ":", marks)