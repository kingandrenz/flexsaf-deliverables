
# main.py

from todo_functions import (
    add_task,
    view_tasks,
    mark_done,
    delete_task,
    task_statistics
)

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Task Statistics")
    print("6. Exit")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(tasks, task_name)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            try:
                task_number = int(input("Enter task number to mark done: "))
                mark_done(tasks, task_number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(tasks, task_number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            task_statistics(tasks)

        elif choice == "6":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
