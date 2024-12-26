class Student:
    def __init__(self, std_id, name, age, address, grade):
        self.std_id = std_id
        self.name = name
        self.age = age
        self.address = address
        self.grade = grade
    
    
class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, std_id, name, age, address, grade):
        if std_id in self.students:
            print(f" Student Id '{std_id}' already exists.")
        else:
            self.students[std_id] = Student(std_id, name, address, age, grade)
            print(f" Student '{name}' added successfully.")
    def view_all_students(self):
        if not self.students:
            print("No Student found!!!")
        else:
            print("Student List:")
            for student in self.students.values():
                print(f"{student.name}")
    def view_student_detail(self, std_id):
        if std_id not in self.students:
            print(f"Student Id {std_id} not found!!!")
        else:
            print(f"\nStudent Detail of Student Id: {std_id}\n")
            student = self.students[std_id]
            print(f"Student ID: {student.std_id}\nStudent Name: {student.name}\nStudent Age: {student.age}\nStudent Address: {student.address}\nStudent Grade: {student.grade}")

def main():
    sms = StudentManagementSystem()

    while True:
        print("\n******************************")
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student Details")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("******************************\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter student id: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            address = input("Enter student address: ")
            grade = input("Enter student grade: ")
            sms.add_student(id, name, age, address, grade)
        elif choice == '2':
            sms.view_all_students()
        elif choice == '3':
            id = input("Enter student id: ")
            sms.view_student_detail(id)
        else:
            print("Invalid Choice!!!")

if __name__ == '__main__':
    main()