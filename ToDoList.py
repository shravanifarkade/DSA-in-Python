# Problem Statement: Develop a stack-based to-do list application for managing tasks. Tasks consist of
# descriptions and priority levels. Implement functionalities to add, remove, and display tasks based on
# priority. Optimize memory usage and facilitate efficient task management using the stack data structure
# Consider the following initial tasks in the to-do list:
#  Task: Complete project proposal
#  Priority: High
#  Task: Schedule team meeting
#  Priority: Medium
#  Task: Review draft presentation
#  Priority: Low
#  Task: Prepare weekly report
#  Priority: High
#  Task: Respond to client emails
#  Priority: Medium.
class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __repr__(self):
        return f"Task(description='{self.description}', priority='{self.priority}')"

class Stack:
    def __init__(self):
        self.items = []

    def push(self, task):
        self.items.append(task)
        print(f"Added task: {task.description} with priority: {task.priority}")

    def pop(self):
        if not self.is_empty():
            removed_task = self.items.pop()
            print(f"Removed task: {removed_task.description}")
            return removed_task
        print("No tasks to remove.")
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display_tasks(self):
        if self.is_empty():
            print("No tasks in the to-do list.")
            return
        
        # Sort tasks based on priority (High > Medium > Low)
        priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
        sorted_tasks = sorted(self.items, key=lambda x: priority_order[x.priority])
        
        print("Current To-Do List (sorted by priority):")
        for task in sorted_tasks:
            print(f"- {task.description} (Priority: {task.priority})")

def main():
    task_stack = Stack()

    # Initial tasks
    initial_tasks = [
        Task("Complete project proposal", "High"),
        Task("Schedule team meeting", "Medium"),
        Task("Review draft presentation", "Low"),
        Task("Prepare weekly report", "High"),
        Task("Respond to client emails", "Medium"),
    ]

    # Add initial tasks to the stack
    for task in initial_tasks:
        task_stack.push(task)

    while True:
        print("\nTo-Do List Application")
        print("1: Add Task")
        print("2: Remove Task")
        print("3: Display Tasks")
        print("4: Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            description = input("Enter task description: ")
            priority = input("Enter task priority (High, Medium, Low): ")
            task_stack.push(Task(description, priority))
        elif choice == 2:
            task_stack.pop()
        elif choice == 3:
            task_stack.display_tasks()
        elif choice == 4:
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
