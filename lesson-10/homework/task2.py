import csv

def read_grades(file_name):
    """Reads data from grades.csv and returns a list of dictionaries."""
    grades = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])  # Convert grade to integer
            grades.append(row)
    return grades

def calculate_average_grades(grades):
    """Calculates the average grade for each subject."""
    subject_totals = {}
    subject_counts = {}

    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']

        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0

        subject_totals[subject] += grade
        subject_counts[subject] += 1

    averages = {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}
    return averages

def write_averages(file_name, averages):
    """Writes the average grades to a CSV file."""
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 2)])

# Main execution
# Create the initial grades.csv file
grade_data = [
    {'Name': 'Alice', 'Subject': 'Math', 'Grade': 85},
    {'Name': 'Bob', 'Subject': 'Science', 'Grade': 78},
    {'Name': 'Carol', 'Subject': 'Math', 'Grade': 92},
    {'Name': 'Dave', 'Subject': 'History', 'Grade': 74},
]

with open('grades.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Subject', 'Grade'])
    writer.writeheader()
    writer.writerows(grade_data)

# Read, calculate averages, and write the results
grades = read_grades('grades.csv')
averages = calculate_average_grades(grades)
write_averages('average_grades.csv', averages)

print("Average grades have been written to average_grades.csv.")
