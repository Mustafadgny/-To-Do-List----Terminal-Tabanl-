from datetime import datetime
todolist = []

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
    print(f"'{new_task}' has been added to the list.")

def delete_task():
    show_tasks()
    task_to_delete = input("Enter the task you want to delete: ")
    for task in todolist:
        if task['Task'] == task_to_delete:
            todolist.remove(task)
            print(f"'{task_to_delete}' has been deleted.")
            return
    print("No such task found.")

def show_tasks():
    if not todolist:
        print("No tasks in the list.")
    else:
        print("\nTo-do list:")
        for i, task in enumerate(todolist, 1):  # assigns values starting from 1 to each element
            print(f"{i}. {task}")

def complete_task():
    show_tasks()
    index = int(input("Enter the task number to mark as completed: ")) - 1  # indexes start from 0
    if 0 <= index < len(todolist):
        todolist[index]['completed'] = True
        print(f"'{todolist[index]['Task']}' has been marked as completed.")
    else:
        print("Invalid number!")

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