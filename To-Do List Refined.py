# We need to import the 'csv' module to handle reading and writing to a CSV file.
import csv

class TDL:
    """Represents a single To-Do task item."""
    def __init__(self, task, date):
        self.task = task
        self.date = date

    def show_task(self):
        """Prints the details of a single task."""
        print(f"Task: {self.task}\nDate Created: {self.date}")

# IMPROVEMENT 3: Correct OOP Structure (Composition)
# Backend now manages TDL objects, but it is not a TDL object itself.
# So we remove the inheritance: class Backend(TDL) becomes class Backend:
class Backend:
    """Handles all the logic, data storage, and operations for the To-Do List."""
    def __init__(self):
        # The filename for storing tasks.
        self.filename = "tasks.csv"
        self.TL = []
        # IMPROVEMENT 1: Load tasks from the file when the app starts.
        self._load_tasks()

    def _load_tasks(self):
        """Internal method to load tasks from the CSV file into memory."""
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    # Each row in the CSV is [task, date]
                    if row: # Make sure the row is not empty
                        task, date = row
                        self.TL.append(TDL(task, date))
        except FileNotFoundError:
            # If the file doesn't exist yet, it's fine. It will be created on the first save.
            print("Welcome! No existing task file found. A new one will be created.")

    def _save_tasks(self):
        """Internal method to save the current list of tasks to the CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for tdl_item in self.TL:
                writer.writerow([tdl_item.task, tdl_item.date])

    def add(self):
        """Adds a new task to the list and saves it."""
        task = input("Enter Your Task: ")
        date = input("Enter The Date Created (DD/MM/YYYY): ")
        tdl = TDL(task, date)
        self.TL.append(tdl)
        # IMPROVEMENT 1: Save the list to the file after adding a new task.
        self._save_tasks()
        print("Successfully Added!")

    def show_all(self):
        """Displays all the tasks currently in the list."""
        if not self.TL:
            print("\n--- Your To-Do List is empty! ---")
            return
            
        print("\n--- All Your Tasks Are ---")
        for i, t in enumerate(self.TL, 1): # Use enumerate for automatic numbering
            print(f"Sr. No.: {i}")
            t.show_task()
            print("------")

    def delete(self):
        """Deletes a specific task or all tasks from the list."""
        if not self.TL:
            print("You have no tasks to delete!")
            return

        # IMPROVEMENT 4: Don't Repeat Yourself (DRY)
        # Call the existing show_all() method instead of rewriting the print logic.
        self.show_all()
        
        # IMPROVEMENT 2: Error Handling
        try:
            choice_str = input("\nWhich Task No. you want to delete? (Enter 0 to delete all): ")
            taskDEL = int(choice_str)

            if taskDEL == 0:
                confirm = input("Do you really want to delete the entire list? (y/n): ").lower()
                if confirm == "y":
                    self.TL.clear()
                    self._save_tasks() # Save changes
                    print("Successfully Deleted Every Task!")
                else:
                    print("Your tasks are safe.")
            elif 1 <= taskDEL <= len(self.TL):
                # Adjust for zero-based index
                removed_task = self.TL.pop(taskDEL - 1)
                self._save_tasks() # Save changes
                print(f"Deleted Task Number {taskDEL}!")
            else:
                print("Invalid task number. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    def edit(self):
        """Edits an existing task in the list."""
        if not self.TL:
            print("You have no tasks to edit!")
            return
            
        self.show_all()
        
        # IMPROVEMENT 2: Error Handling
        try:
            task_num_str = input("\nWhich task number you want to edit: ")
            task_num = int(task_num_str)

            if 1 <= task_num <= len(self.TL):
                task_to_edit = self.TL[task_num - 1]
                
                print("\nWhat do you want to edit?")
                print("1. The task description")
                print("2. The date")
                print("3. Both")
                choice_str = input("Enter your choice (1, 2, or 3): ")
                choice = int(choice_str)

                if choice == 1:
                    task_to_edit.task = input("Enter the new task description: ")
                elif choice == 2:
                    task_to_edit.date = input("Enter the new date: ")
                elif choice == 3:
                    task_to_edit.task = input("Enter the new task description: ")
                    task_to_edit.date = input("Enter the new date: ")
                else:
                    print("Invalid choice for editing.")
                    return # Exit without saving if choice is invalid

                self._save_tasks() # Save the changes to the file
                print(f"Successfully Edited Task {task_num}!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    a = Backend()
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. Show All Tasks")
        print("3. Edit Task")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            a.add()
        elif choice == "2":
            a.show_all()
        elif choice == "3":
            a.edit()
        elif choice == "4":
            a.delete()
        elif choice == "5":
            print("Exiting....!")
            break
        else:
            print("Invalid Input. Please enter a number from 1 to 5.")

# This ensures the main() function runs only when the script is executed directly
if __name__ == "__main__":
    main()
