# To-Do List CLI App

# List to store tasks
tasks = []


# Function to add a task
def add_task():
    task = input("Enter a task: ")

    if task.strip():
        tasks.append(task)
        print("✅ Task added successfully!")
    else:
        print("❌ Task cannot be empty.")


# Function to view all tasks
def view_tasks():
    if not tasks:
        print("\n📋 No tasks available.")
        return

    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


# Function to remove a task
def remove_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"✅ Removed: {removed}")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# Main program
while True:
    print("\n===== TO-DO LIST APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("👋 Thank you for using To-Do List App!")
        break

    else:
        print("❌ Invalid choice. Please try again.")