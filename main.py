import pickle

# Define an empty list to hold the tasks
tasks = []

# Define a function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

# Define a function to remove a task from the list
def remove_task(task):
    try:
        tasks.remove(task)
        print(f"Task '{task}' removed from the list.")
    except ValueError:
        print(f"Task '{task}' not found in the list.")

# Define a function to view the current list of tasks
def view_tasks():
    print("Current list of tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Define a function to save the list to a file
def save_tasks(filename):
    with open(filename, "wb") as f:
        pickle.dump(tasks, f)
    print(f"Tasks saved to file '{filename}'.")

# Define a function to load the list from a file
def load_tasks(filename):
    global tasks
    with open(filename, "rb") as f:
        tasks = pickle.load(f)
    print(f"Tasks loaded from file '{filename}'.")

while True:
    # Print menu options
    print("\nMenu:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Save tasks to file")
    print("5. Load tasks from file")
    print("6. Exit")

    # Get user input
    choice = input("Enter choice: ")

    # Handle user input
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        filename = input("Enter filename to save to: ")
        save_tasks(filename)
    elif choice == "5":
        filename = input("Enter filename to load from: ")
        load_tasks(filename)
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
