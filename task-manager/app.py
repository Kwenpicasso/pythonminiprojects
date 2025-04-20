
tasks = []


def display_header():
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("0. Exit")


def add_task():
    title = input("Enter task title:")
    new_task = tasks.append({'title': title, 'completed': False})
    print(f"Task {new_task} has been added succesfully")


def view_task():
    if not tasks:
        print("no task found")
        return
    else:
        print("====Task====")
        for index, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{index + 1}. {status} {task['title']}")


def complete_task():
    view_task()
    try:
        value = int(input("Enter task number to mark as completed:")) - 1
        if value < 0 or value >= len(tasks):
            print("Invalid task number.")
        else:
            tasks[value]['completed'] = True
            print("Task marked as completed.")
    except ValueError:
       print("Please enter a valid number.")


def delete_task():
    view_task()
    try:
        value = int(input("Enter task number to delete:")) - 1
        if value < 0 or value >= len(tasks):
            print("Invalid task number.")
        else:
            deleted =tasks.pop(value) 
            print(f"{deleted['title']} deleted")
    except ValueError:
        print("Please enter a valid number.")


def main():

    while True:
        display_header()
        choice = input("Enter your choice (0-4):")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == "0":
            print("goodbye")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 4.")


main()
