def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found!")
            else:
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found! Start adding tasks.")

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task added: {task}")

def delete_task(task_number):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Deleted task: {removed_task.strip()}")
        else:
            print("Invalid task number!")
    except FileNotFoundError:
        print("No tasks file found!")

# Example usage
while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "3":
        show_tasks()
        task_num = int(input("Enter task number to delete: "))
        delete_task(task_num)
    elif choice == "4":
        break
    else:
        print("Invalid choice! Try again.")
