tasks = []

def show_menu():
    print("\n==== TO-DO MENU ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        if not tasks:
            print("No tasks yet.")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")

    elif choice == '2':
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == '3':
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        task_num = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
