class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self):
        
        title = input("Enter Title:")
        description = input("Enter Description")
        
        task = {
            "title": title,
            "description": description
        }
        self.tasks.append(task)
        print("Task added successfully!")
        
    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return
        
        print('\n===== Your Tasks =====')
        
        for i, task in enumerate(self.tasks):
            print(f"{i+1}.{task['title']} - {task['description']}")
            

    def delete_task(self):
        self.view_tasks()
        
        try:
            num= int(input("Enter task number to delete:"))
            index = num-1
            if 0 <= index < len(self.tasks):
                removed= self.tasks.pop(index)
                print(f"Deleted: {removed['title']}")
            else:
                print("Invalid task number.")
        
        except ValueError:
            print("Please enter a valid number.")
    
    def run(self):
        while True:
            print("\n===== Task Tracker =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
manager = TaskManager()
manager.run()
   