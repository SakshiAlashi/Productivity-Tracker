import csv
import os

Tasks_File = r"D:\PycharmProjects\Productivity_tracker\data\tasks.csv"

if not os.path.exists(Tasks_File) or os.stat(Tasks_File).st_size == 0:
    with open(Tasks_File, 'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Task", "Status", "Date"])

def add_task(task,status="Pending",date=None):
    
    with open(Tasks_File, 'r', newline='') as f:
        data = csv.DictReader(f)
        for row in data:
            if row['Task'].strip().lower()== task.strip().lower() and row['Status'].lower() == "pending":
                print(f"⚠️ Task '{task}' already exists with status 'Pending'. Please rename it or mark it as done.")
                return 
                
    #count existing tasks excluding header
    with open(Tasks_File, 'r', newline='') as f:
        data = csv.reader(f)
        next(data,None)
        task_id = sum(1 for _ in data)+ 1 #auto-increament-- Start from 1

    with open(Tasks_File, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([task_id, task, status, date])
        print(f" Task '{task}' added successfully!")

def get_all_tasks():
    with open(Tasks_File,'r',newline='') as f:
        data = csv.DictReader(f)
        return list(data)

def update_task_status_by_name(task_name, new_status):
    tasks = get_all_tasks()
    updated = False
    for task in tasks:
        if task["Task"].lower().strip() == task_name.lower().strip():
            task["Status"] = new_status
            updated = True
            break

    if updated:
        with open(Tasks_File, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Task", "Status", "Date"])
            writer.writeheader()
            writer.writerows(tasks)
        return True
    else:
        return False
    
def delete_task(task_name):
    tasks = get_all_tasks()
    filtered_tasks = [task for task in tasks if task["Task"].strip().lower() != task_name.strip().lower()]

    # Reassign IDs
    for i, task in enumerate(filtered_tasks, start=1):
        task["ID"] = str(i)

    with open(Tasks_File, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Task", "Status", "Date"])
        writer.writeheader()
        writer.writerows(tasks)

# add_task("Learn Streamlit", date="2025-08-07")
# add_task("Buy groceries", date="2025-08-07")
# add_task("Learn Streamlit")  # Duplicate test

# print(get_all_tasks())
# update_task_status_by_name("Buy groceries", "Done")
# delete_task("Learn Streamlit")
# print(get_all_tasks())