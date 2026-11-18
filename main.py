
tasks = []

def add_task():
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    if any(task["title"].lower() == title.lower() for task in tasks):
        print("This task already exists.")
        return

    tasks.append({"title": title, "completed": False})
    print(f"Task added successfully! Total tasks: {len(tasks)}")

def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")

def complete_task():
    display_tasks()
    try:
        task_id = int(input("Enter task number to complete: "))
        if 1 <= task_id <= len(tasks):
            tasks[task_id - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    display_tasks()
    try:
        task_id = int(input("Enter task number to delete: "))
        if 1 <= task_id <= len(tasks):
            tasks.pop(task_id - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting Student Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
