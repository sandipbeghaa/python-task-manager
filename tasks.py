import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file if it exists."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Write the task list to the JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"'{title}' has been added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        checkbox = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {checkbox} {task['title']}")
    print("------------------")


def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        number = int(input("Number of the task to complete: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks(tasks)
            print("Marked as done.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        number = int(input("Number of the task to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"'{removed['title']}' has been deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")


def main_menu():
    tasks = load_tasks()
    while True:
        print("\n=== Task Manager ===")
        print("1 - Add task")
        print("2 - View tasks")
        print("3 - Mark task as done")
        print("4 - Delete task")
        print("5 - Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()