# Simple To-Do List Application

# Initialize an empty list to store tasks
tasks = []

# Function to display the list of tasks
def display_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour to-do list:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to add a new task to the list
def add_task():
    task = input("\nEnter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list!")

# Function to remove a task by its number
def remove_task():
    display_tasks()
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from the list!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop to display the menu and get user input
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")

# Run the application
if __name__ == "__main__":
    main()
