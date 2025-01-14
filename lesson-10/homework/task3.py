import json
import csv

# Load tasks from JSON file
def load_tasks(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# Save tasks to JSON file
def save_tasks(file_name, tasks):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def display_tasks(tasks):
    print("ID | Task Name          | Completed | Priority")
    print("-- | ------------------ | --------- | --------")
    for task in tasks:
        print(f"{task['id']:2} | {task['task']:<18} | {task['completed']:<9} | {task['priority']}")

# Calculate task completion stats
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks

    stats = {
        "Total Tasks": total_tasks,
        "Completed Tasks": completed_tasks,
        "Pending Tasks": pending_tasks,
        "Average Priority": round(average_priority, 2)
    }

    return stats

# Convert tasks to CSV
def tasks_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

# Main execution
# Create initial tasks.json file
task_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

# Save initial data to tasks.json
save_tasks('tasks.json', task_data)

# Load tasks from JSON
tasks = load_tasks('tasks.json')

# Display tasks
print("Task List:")
display_tasks(tasks)

# Calculate and display stats
stats = calculate_stats(tasks)
print("\nTask Statistics:")
for key, value in stats.items():
    print(f"{key}: {value}")

# Convert tasks to CSV
tasks_to_csv('tasks.json', 'tasks.csv')
print("\nTasks have been saved to tasks.csv.")
