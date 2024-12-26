f = open("employees.txt")

def add_file():

    Id = input("Employee ID: ").strip()
    name = input("Name: ").strip()
    pos = input("Position: ").strip()
    salary = input("Salary $: ").strip()

    add = False
    with open("employees.txt", "a") as f:
        emp_list=[]
    
        emp_list.append(Id)
        emp_list.append(name)
        emp_list.append(pos)
        emp_list.append(salary)
        print(emp_list)
        record = ' '.join(emp_list)
        f.write(f'{record}\n')
        add = True
    
    if not add:
        print("Employee Add Error")
    
def display_file():
    with open("employees.txt") as f:
        print(f.read())


def find_emp(user_id):
    with open("employees.txt") as f:
        lines = f.readlines()
        for line in lines:
            if user_id in line.split():
                print(line)
            else:
                print("Incorrect ID")
   
            
def update_emp(user_id):
    with open("employees.txt") as f:
        lines = f.readlines() 

    updated = False

    with open("employees.txt", "w") as f:
        for line in lines:
            if user_id in line.split():
                print(f"Current record: {line.strip()}")
                print("Enter new details:")
                
                
                new_id = input("New Employee ID: ").strip()
                new_name = input("New Name: ").strip()
                new_pos = input("New Position: ").strip()
                new_salary = input("New Salary $: ").strip()
                emp_list=[]
    
                emp_list.append(new_id)
                emp_list.append(new_name)
                emp_list.append(new_pos)
                emp_list.append(new_salary)
                print(emp_list)
                record = ' '.join(emp_list)
                f.write(f'{record}\n')    
                updated = True
                print("Record updated successfully.")
            else:
                f.write(line)
        if not updated:
            print("Employee ID not found.")

def Delete_emp(user_id):
    with open("employees.txt") as f:
        lines = f.readlines()
    deleted = False

    with open("employees.txt", "w") as f:
        for line in lines:
            if user_id in line.split():
                print(f"Current record: {line.strip()}")
                new_record = "\n"
                f.write(new_record)
                deleted = True
                print(f"User {user_id} Deleted")
            else:
                f.write(line)
    if not deleted:
        print("Employee ID not found.")

print("Menu:\n")
print("1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit")

option = int(input("Select option: "))

if option == 1:
    add_file()  
if option == 2:
    display_file()
if option == 3:
    user_id = input("Enter user's ID:")
    find_emp(user_id)
if option == 4:
    user_id = input("Enter user's ID:")
    update_emp(user_id)
if option == 5:
    user_id = input("Enter user's ID:")
    Delete_emp(user_id)
if option == 6:
    exit()

