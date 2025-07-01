#added imports
import json
import os
from datetime import datetime

todolist = []
FILE_NAME="tasks1.json"

#load func.
def load_tasks():
    global todolist
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            todolist = json.load(f)

#save func.
def save_tasks():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(todolist, f, ensure_ascii=False, indent=4)

def show_menu():
    print("---TO-DO LIST---")
    print("1. Add task")
    print("2. Delete task")
    print("3. Show tasks")
    print("4. Mark task as completed")
    print("5. Exit")

def add_task():
    new_task = input("Enter the task you want to add: ")
    date = datetime.now().strftime("%d-%m-%Y %H:%M")
    todolist.append({'Task': new_task, 'completed': False, 'date': date})
    save_tasks()
    print(f"'{new_task}' has been added to the list.")

#making delete with number
def delete_task():
    show_tasks()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(todolist):
            deleted = todolist.pop(index)
            save_tasks()
            print(f"'{deleted['Task']}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#Added already func.
def complete_task():
    show_tasks()
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= index < len(todolist):
            if todolist[index]["completed"]:
                print(f"The task '{todolist[index]['Task']}' is already completed.")
            else:
                todolist[index]["completed"] = True
                save_tasks()
                print(f"Your task '{todolist[index]['Task']}' is now marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_tasks():
    if not todolist:
        print("No tasks in the list.")
    else:
        print("\nTo-do list:")
        for i, task in enumerate(todolist, 1):
            status = "✔️" if task["completed"] else "X"
            print(f"{i}. {task['Task']} - {task['date']} - {status}")

#Added already func.
def complete_task():
    show_tasks()
    index = int(input("Enter the task number to mark as completed: ")) - 1  # indexes start from 0
    if 0 <= index < len(todolist):
        if todolist[index]["completed"]:
            print(f"The task '{todolist[index]['Task']}' is already completed.")
        else:
            todolist[index]["completed"] = True
            save_tasks()
            print(f"Your task '{todolist[index]['Task']}' is now marked as complete.")
    else:
        print("No such task found.")

#uploud tasks
load_tasks()

while True:
    show_menu()
    choice = int(input("Please choose an option (1-2-3-4-5): "))
    if choice == 1:
        add_task()
    elif choice == 2:
        delete_task()
    elif choice == 3:
        show_tasks()
    elif choice == 4:
        complete_task()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")
