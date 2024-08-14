tasks = {}

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_num = input("Enter task number: ")
        description = input("Enter task description: ")
        tasks[task_num] = description
        print(f"Task '{task_num}' added successfully!")
    elif choice == "2":
        if not tasks:
            print("No tasks available!")
        else:
            print("Available Tasks:")
            for task_num, description in tasks.items():
                print(f"{task_num}: {description}")
    elif choice == "3":
        task_num = input("Enter task number to update: ")
        if task_num in tasks:
            new_description = input("Enter new task description: ")
            tasks[task_num] = new_description
            print(f"Task '{task_num}' updated successfully!")
        else:
            print(f"Task '{task_num}' not found!")
    elif choice == "4":
        task_num = input("Enter task number to delete: ")
        if task_num in tasks:
            del tasks[task_num]
            print(f"Task '{task_num}' deleted successfully!")
        else:
            print(f"Task '{task_num}' not found!")
    elif choice == "5":
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")