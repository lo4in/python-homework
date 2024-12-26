f = open("employees.txt")
def add_file(Id, name, pos, salary):
    f = open("employees.txt", "a")
    emp_list=[]
    
    emp_list.append(Id)
    emp_list.append(name)
    emp_list.append(pos)
    emp_list.append(salary)
    print(emp_list)
    record = ' '.join(emp_list)
    f.write(f'{record}\n')
    f.close

def display_file():
    f = open("employees.txt")
    print(f.read())
print("Menu:\n")
print("1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit")

def find_emp(user_id):
    f = open("employees.txt")
    lines = f.readlines()
    for line in lines:
        
        a = line.count(user_id)
        print(a) 
       

option = int(input())

if option == 1:
    
    Id = input("Employee ID: ").strip()
    name = input("Name: ").strip()
    pos = input("Position: ").strip()
    salary = input("Salary $: ").strip()
    add_file(Id, name, pos, salary)
if option == 2:
    display_file()
if option == 3:
    user_id = input()
    find_emp(user_id)
    
    


