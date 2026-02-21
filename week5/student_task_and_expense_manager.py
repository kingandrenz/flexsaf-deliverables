#!/usr/bin/python3

""" STUDENT TASK & EXPENSE MANAGER
"""

# ----- TO-DO LIST MANAGER --------
tasks = []

#------ EXPENSES TRACKER --------
expenses = []

def add_task():
    title = input("Enter Assignment Title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added successfully\n")

def view_tasks():
    if not tasks:
        print("No task available")
        return

    print("\nYour tasks are: ")
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index}. {task['title']} - {status}")
    print()

def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter task index to mark complete: "))
        tasks[index]["completed"] = True
        print("Task marked completed.\n")
    except (ValueError, IndexError):
        print("Invalid index.\n")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter index of task to remove: "))
        removed = tasks.pop(index)
        print(f"Removed: {removed['title']}\n")
    except (ValueError, IndexError):
        print("Invalid selection.\n")

def sort_tasks():
    tasks.sort(key=lambda x: x["title"])
    print("\nTasks sorted alphabetically\n")

def slice_tasks():
    print("First 2 tasks:", tasks[:2])
    print("Last 2 tasks:", tasks[-2:])
    print()

#=====================================================================================
# EXPENSE TRACKER
#=====================================================================================

def add_expense():
    item = input("Enter item: ")
    category = input("Enter category (Lunch/Transport/Books): ")
    try:
        amount = float(input("Enter amount: "))
        expenses.append((item, category, amount))
        print("Expense recorded.\n")
    except ValueError:
        print("Invalid amount!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\nExpenses List:")
    for index, expense in enumerate(expenses):
        item, category, amount = expense
        print(f"{index}. {item} | {category} | #{amount}")
    print()

def filter_by_category():
    category = input("Enter category to filter: ")
    filtered = [exp for exp in expenses if exp[1].lower() == category.lower()]
    print("Filtered Expenses:", filtered)
    print()

def filter_above_amount():
    try:
        minimum = float(input("Enter minimum amount to filter: "))
        filtered = [exp for exp in expenses if exp[2] > minimum]
        print("Filtered Expenses above Minimum:", filtered)
        print()
    except ValueError:
        print("Invalid amount.\n")

def slice_expenses():
    print("First 2 expenses:", expenses[:2])
    print("Last 2 expenses:", expenses[-2:])
    print()

# =======================================================================
# MAIN MENU
#========================================================================

def main():
    while True:
        print("============= STUDENT MANAGER =============")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task Completed")
        print("4. Remove Task")
        print("5. Sort Task")
        print("6. Slice Task")
        print("7. Add Expenses")
        print("8. View Expenses")
        print("9. Filter Expenses by Category")
        print("10. Filter Expenses above Minimum Value")
        print("11. Slice Expenses")
        print("12. Exit")

        choice = input("Select option: ")
        print()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            sort_tasks()
        elif choice == '6':
            slice_tasks()
        elif choice == '7':
            add_expense()
        elif choice == '8':
            view_expenses()
        elif choice == '9':
            filter_by_category()
        elif choice == '10':
            filter_above_amount()
        elif choice == '11':
            slice_expenses()
        elif choice == '12':
            print("Good bye...")
            break
        else:
            print("Invalid Choice\n")

main()

