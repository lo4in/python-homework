def teacher():
    admin = "admin"
    password = "admin"
    user_Name = input("Login:")
    user_pas= input("Password:")
    if user_Name == admin and user_pas == password:
        #test_name = input("")
        new_test_name = input("Name Test:")
        key_list = input("")
        key_list = key_list.upper()
        key_list = key_list.split()
        print(key_list)
        record = ' '.join(key_list)
         
        with open(new_test_name , "a") as file:
            file.write(f'{record}\n') 

    else:
        print("Incorrect Login or password")

def student():

    Name_of_student = input("Name: ")
    check_test = input("Name of test you want to check: ")
    
    with open(check_test, "r") as file:
        key_list = file.read()
        key_list = key_list.split()
        print(key_list)
        stud_answ_list = input("Your answers: ")
        stud_answ_list = stud_answ_list.upper()
        stud_answ_list = stud_answ_list.split()
        print(stud_answ_list)
        correct_ans = [item for item in stud_answ_list if item in key_list]
        incorrect_ans = [item for item in stud_answ_list if item not in key_list]
        len_correct_ans = len(correct_ans)
        len_incorrect_ans = len(incorrect_ans)
        
        print(f"{correct_ans} Your correct answers")            
        print(f"{incorrect_ans} Your incorrect answers")

        print(f"You have {len_correct_ans} correct answers")
        print(f"You have {len_incorrect_ans} incorrect answers")        
        
            
        
option1 = int(input())
if option1 == 0:
    
    teacher()

if option1 == 1:
    student()








