students = []

def show_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    # 1. Add Student
    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        student = {
            "roll": roll,
            "name": name,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully")

    # 2. View Students
    elif choice == "2":
        if not students:
            print("No students found")
        else:
            for s in students:
                print("Roll:", s["roll"], "Name:", s["name"], "Marks:", s["marks"])

    # 3. Search Student
    elif choice == "3":
        search_roll = input("Enter roll number to search: ")
        found = False

        for s in students:
            if s["roll"] == search_roll:
                print("Student Found")
                print("Roll:", s["roll"])
                print("Name:", s["name"])
                print("Marks:", s["marks"])
                found = True
                break

        if not found:
            print("Student not found")

    # 4. Delete Student
    elif choice == "4":
        del_roll = input("Enter roll number to delete: ")
        found = False

        for s in students:
            if s["roll"] == del_roll:
                students.remove(s)
                print("Student deleted successfully")
                found = True
                break

        if not found:
            print("Student not found")

    # 5. Exit
    elif choice == "5":
        print("Exit program")
        break

    else:
        print("Invalid choice")   