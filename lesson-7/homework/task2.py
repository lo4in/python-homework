class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        self.load_employees()

    def load_employees(self):
        """Load employees from the file into a dictionary."""
        self.employees = {}
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    employee_id, name, position, salary = line.strip().split(", ")
                    self.employees[employee_id] = Employee(employee_id, name, position, float(salary))
        except FileNotFoundError:
            with open(self.FILE_NAME, "w") as file:
                pass  # Create the file if it doesn't exist.

    def save_employees(self):
        """Save all employees back to the file."""
        with open(self.FILE_NAME, "w") as file:
            for employee in self.employees.values():
                file.write(str(employee) + "\n")

    def add_employee(self, employee_id, name, position, salary):
        if employee_id in self.employees:
            print("Error: Employee ID must be unique.")
            return
        self.employees[employee_id] = Employee(employee_id, name, position, salary)
        self.save_employees()
        print("Employee added successfully!")

    def view_all_employees(self):
        if not self.employees:
            print("No employees found.")
            return
        print("Employee Records:")
        for employee in self.employees.values():
            print(employee)

    def search_employee(self, employee_id):
        employee = self.employees.get(employee_id)
        if employee:
            print("Employee Found:")
            print(employee)
        else:
            print("Employee not found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        employee = self.employees.get(employee_id)
        if not employee:
            print("Employee not found.")
            return
        if name:
            employee.name = name
        if position:
            employee.position = position
        if salary:
            employee.salary = salary
        self.save_employees()
        print("Employee updated successfully!")

    def delete_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            self.save_employees()
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                try:
                    salary = float(input("Enter Salary: "))
                except ValueError:
                    print("Invalid salary. Please enter a number.")
                    continue
                self.add_employee(employee_id, name, position, salary)
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                self.search_employee(employee_id)
            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (leave blank to keep current): ") or None
                position = input("Enter new Position (leave blank to keep current): ") or None
                try:
                    salary_input = input("Enter new Salary (leave blank to keep current): ")
                    salary = float(salary_input) if salary_input else None
                except ValueError:
                    print("Invalid salary. Please enter a number.")
                    continue
                self.update_employee(employee_id, name, position, salary)
            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
