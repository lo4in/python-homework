import csv

with open("lesson-10/homework/grades.csv", "r") as file:
    csv_file = csv.reader(file)
    next(csv_file)
    for line in csv_file:
        grades =[]
        grades1 = grades.append(int(line[2]))
        subjects = []
        sub = subjects.append(line[1])
        subs = []
        for x in subjects:
            if x not in subs:
                subs.append(x)
        sub_avg ={
        }
    print(subjects)

    sum = sum(grades)
    len = len(grades)
    avg = sum/len
    print(avg)    
    # with open("lesson-10/homework/average_grades.csv", "r") as fl:
        
