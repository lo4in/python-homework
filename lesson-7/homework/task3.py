import json
import csv
from abc import ABC, abstractmethod
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        due_date_str = self.due_date if self.due_date else "None"
        return f"{self.task_id}, {self.title}, {self.description}, {due_date_str}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            task_id=data["task_id"],
            title=data["title"],
            description=data["description"],
            due_date=data.get("due_date"),
            status=data["status"],
        )

class StorageHandler(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass

class JSONStorageHandler(StorageHandler):
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, tasks):
        with open(self.file_name, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load(self):
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            return []

class CSVStorageHandler(StorageHandler):
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, tasks):
        with open(self.file_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self):
        try:
            with open(self.file_name, "r") as file:
                reader = csv.DictReader(file)
                return [Task.from_dict(row) for row in reader]
        except FileNotFoundError:
            return []

class ToDoApp:
    def __init__(self, storage_handler):
        self.storage_handler = storage_handler
        self.tasks = self.storage_handler.load()

    def add_task(self, task_id, title, description, due_date=None, status="Pending"):
        if any(task.task_id == task_id for task in self.tasks):
            print("Error: Task ID must be unique.")
            return
        new_task = Task(task_id, title, description, due_date, status)
        self.tasks.append(new_task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks found with the specified status.")
            return
        print("Filtered Tasks:")
        for task in filtered_tasks:
            print(task)

    def save_tasks(self):
        self.storage_handler.save(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage_handler.load()
        print("Tasks loaded successfully!")

    def menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                task_id = input("Enter Task ID: ")
                title = input("Enter Title: ")
                description = input("Enter Description: ")
                due_date = input("Enter Due Date (YYYY-MM-DD): ") or None
                status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
                self.add_task(task_id, title, description, due_date, status)

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                task_id = input("Enter Task ID to update: ")
                title = input("Enter new Title (leave blank to keep current): ") or None
                description = input("Enter new Description (leave blank to keep current): ") or None
                due_date = input("Enter new Due Date (YYYY-MM-DD, leave blank to keep current): ") or None
                status = input("Enter new Status (leave blank to keep current): ") or None
                self.update_task(task_id, title, description, due_date, status)

            elif choice == "4":
                task_id = input("Enter Task ID to delete: ")
                self.delete_task(task_id)

            elif choice == "5":
                status = input("Enter status to filter by (Pending/In Progress/Completed): ")
                self.filter_tasks(status)

            elif choice == "6":
                self.save_tasks()

            elif choice == "7":
                self.load_tasks()

            elif choice == "8":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Select storage format:")
    print("1. JSON")
    print("2. CSV")
    storage_choice = input("Enter your choice: ")

    if storage_choice == "1":
        storage_handler = JSONStorageHandler("tasks.json")
    elif storage_choice == "2":
        storage_handler = CSVStorageHandler("tasks.csv")
    else:
        print("Invalid choice. Defaulting to JSON.")
        storage_handler = JSONStorageHandler("tasks.json")

    app = ToDoApp(storage_handler)
    app.menu()

