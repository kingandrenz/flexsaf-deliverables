#!/usr/bin/python3

def add_task(tasks task_name):
    """ Add a new task to the list """
    tasks.append({"task": task_name, "done": False})
    return tasks


def view_tasks(tasks):
    """Display all tasks."""
    if len(tasks) == 0:
        print("\nNo tasks yet.\n")
        return

    print("\nYour To-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index}. {task['task']} - {status}")

        print(f"\nTotal tasks: {len(tasks)}\n")


def mark_done(tasks, task_number):
    """ Mark a task as Completed."""
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return tasks

    tasks[task_number - 1]["done"] = True
    print("Task marked as done.")
    return tasks

def delete_task(tasks, task_number):
    """Delete a task."""
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return tasks

    removed = tasks.pop(task_number - 1)
    print(f"Deleted task: {removed['task']}")
    return tasks

def task_statistics(tasks):
    """Show statistics using built-in functions."""
    done_tasks = sum(1 for t in tasks if t["done"])
    pending_task = len(tasks) - done_tasks

    print("\nTask Statistics")
    print("-----------------")
    print(f"Total Tasks: {len(tasks)}")
    print(f"Completed: {done_tasks}")
    print(f"Pending: {pending_tasks}")


