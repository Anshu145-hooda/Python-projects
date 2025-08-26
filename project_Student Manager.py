class StudentManager:
    def __init__(self, filename="Student.txt"):
        self.filename = filename

    def add_student(self, name, marks):
        with open(self.filename, "a+") as file:
            file.seek(0)
            for line in file:
                if name.lower() in line.lower():
                    print("The name already exists.")
                    return
            file.write(f"\n{name} : {marks}")
            print("Student added successfully.")

    def search_student(self, name):
        found = False
        with open(self.filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                if name.lower() in line.lower():
                    print(f"Found in line {line_number}: {line.strip()}")
                    found = True
        if not found:
            print("Student not found.")

    def show_all(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read().strip()
                if content:
                    print("\n--- Student List ---")
                    print(content)
                else:
                    print("No student records yet.")
        except FileNotFoundError:
            print("No student records yet.")

    def update_student(self, name, new_marks):
        updated = False
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            with open(self.filename, "w") as file:
                for line in lines:
                    if name.lower() in line.lower():
                        file.write(f"{name} : {new_marks}\n")
                        updated = True
                    else:
                        file.write(line)
        except FileNotFoundError:
            print("No student records yet.")
            return

        if updated:
            print(f"{name}'s marks updated successfully.")
        else:
            print(f"{name} not found.")

# === Program menu ===
manager = StudentManager()

while True:
    print('''\nWelcome to Student Manager
1. Add Student
2. Search Student
3. Show All Students
4. Update Student
5. Exit''')

    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        manager.add_student(name, marks)
    elif choice == "2":
        name = input("Enter name to search: ")
        manager.search_student(name)
    elif choice == "3":
        manager.show_all()
    elif choice == "4":
        name = input("Enter name to update: ")
        marks = input("Enter new marks: ")
        manager.update_student(name, marks)
    elif choice == "5":
        print("Thank you for using Student Manager.")
        break
    else:
        print("Invalid choice.")