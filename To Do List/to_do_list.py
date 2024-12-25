import json

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully")

    def view_task(self):
        if not self.tasks:
            print("No task is in list")
        else:
            print("\nTo-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{index}. {task['task']} - {status}")
    
    def mark_completed(self, index):
        try:
            self.tasks[index-1]["completed"] = True
            print(f"Task {index} marked as completed")
        except IndexError:
            print("Invalid task number!!")
    
    def delete_task(self, index):
        try:
            remove_task = self.tasks.pop(index-1)
            print(f"Task {remove_task['task']} deleted successfully")
        except IndexError:
            print("Invalid task number!!!")
    
    def save_to_file(self, file_name = 'tasks.json'):
        try:
            with open(file_name, "w") as file:
                json.dump(self.tasks, file, indent=4)
            print("Tasks saved successfully!")
        except IOError:
            print("Error saving tasks to file!")
    
    def load_from_file(self, file_name="tasks.json"):
        try:
            with open(file_name, "r") as file:
                self.tasks = json.load(file)
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("No saved tasks found!")
        except json.JSONDecodeError:
            print("Error reading tasks file!")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List App:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save Tasks to File")
        print("6. Load Tasks from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_task()
        elif choice == "3":
            todo.view_task()
            try:
                index_num = int(input("Enter the task number to mark as completed: "))
                todo.mark_completed(index_num)
            except IndexError:
                print("Invalid index number!!!")
        elif choice == '4':
            todo.view_task()
            try:
                task_num = int(input("Enter a task number to delete: "))
                todo.delete_task(task_num)
            except ValueError:
                print("Invalid task number!!!")
        elif choice == "5":
            todo.save_to_file()
        elif choice == "6":
            todo.load_from_file()
        elif choice == "7":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()