import os

class Task:
    """Represents a Task with an ID, title, and description."""
    
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"ID: {self.task_id} | Title: {self.title} | Description: {self.description}"

class TaskManager:
    """Handles task operations such as Create, Read, Update, and Delete."""
    
    def __init__(self):
        self.tasks = []
        self.counter = 1  # Auto-incrementing Task ID

    def create_task(self, title, description):
        """Creates a new task and adds it to the list."""
        task = Task(self.counter, title, description)
        self.tasks.append(task)
        self.counter += 1
        print("\n✅ Task added successfully!")

    def read_tasks(self):
        """Displays all tasks."""
        if not self.tasks:
            print("\n⚠️ No tasks available.")
        else:
            print("\n📋 Task List:")
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, new_title, new_description):
        """Updates an existing task."""
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = new_title
                task.description = new_description
                print("\n✅ Task updated successfully!")
                return
        print("\n⚠️ Task not found.")

    def delete_task(self, task_id):
        """Deletes a task by ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("\n✅ Task deleted successfully!")
                return
        print("\n⚠️ Task not found.")

def main():
    """Main function to interact with the user."""
    manager = TaskManager()
    
    while True:
        print("\n====== 📝 TASK MANAGER ======")
        print("1️⃣ Create Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Update Task")
        print("4️⃣ Delete Task")
        print("5️⃣ Exit")

        choice = input("🔹 Enter your choice: ").strip()

        if choice == "1":
            title = input("📌 Enter task title: ").strip()
            description = input("📝 Enter task description: ").strip()
            manager.create_task(title, description)

        elif choice == "2":
            manager.read_tasks()

        elif choice == "3":
            try:
                task_id = int(input("✏️ Enter task ID to update: "))
                new_title = input("📌 Enter new title: ").strip()
                new_description = input("📝 Enter new description: ").strip()
                manager.update_task(task_id, new_title, new_description)
            except ValueError:
                print("\n⚠️ Invalid input! Please enter a number.")

        elif choice == "4":
            try:
                task_id = int(input("🗑 Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("\n⚠️ Invalid input! Please enter a number.")

        elif choice == "5":
            print("\n👋 Exiting Task Manager. Goodbye!")
            break

        else:
            print("\n⚠️ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()


TASK_FILE = "tasks.txt"

# Function to load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    task_id, description, status = parts
                    tasks.append({"id": int(task_id), "description": description, "status": status})
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['id']}|{task['description']}|{task['status']}\n")

# Function to display all tasks
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nTASK LIST:")
        for task in tasks:
            print(f"[{task['id']}] {task['description']} - {task['status']}")
        print("\n")

# Function to add a new task
def add_task(tasks):
    task_id = len(tasks) + 1
    description = input("Enter task description: ")
    tasks.append({"id": task_id, "description": description, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully!\n")

# Function to update a task status
def update_task(tasks):
    display_tasks(tasks)
    task_id = int(input("Enter task ID to mark as completed: "))
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print("Task updated successfully!\n")
            return
    print("Task not found!\n")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    task_id = int(input("Enter task ID to delete: "))
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully!\n")
    return tasks

# Main function
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTask Manager Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            tasks = delete_task(tasks)
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
