class TDL:
    def __init__(self, task, date):
        self.task = task
        self.date = date

    def show_task(self):
        print(f"Task: {self.task} \nDate Created: {self.date}")
        

class Backend(TDL):
    def __init__(self):
        self.TL = []
    
    def add(self):
        task = input("Enter Your Task: ")
        date = input("Enter The Date Created(DD/MM/YYYY): ")
        tdl = TDL(task, date)
        self.TL.append(tdl)
        print("Successfully Added!")
    
    def show_all(self):
        print(f"\n---All Your Tasks Are---")
        count = 1
        for t in self.TL:
            print(f"Sr. No.: {count}")
            count += 1
            t.show_task()
            print("------")
    
    def delete(self):
        count = 1
        for t in self.TL:
            print(f"Sr. No.: {count}")
            count += 1
            t.show_task()
            print("------")
        print(f"\nWhich Task You Want To Delete Write Your Choice As Shown Or Deleting Everytask Stored Type (0): ")
        taskDEL = int(input())
        

        if taskDEL == 0:
            print("Do you really want to delete entire task(y or n): ")
            inp1 = input()
            if inp1 == "y":
                if not self.TL:
                    print("You have no tasks to delete!")
                    return
                else:
                    self.TL.clear()
                    print("Successfully Deleted Every Task...!")
            elif inp1 == "n":
                print("Your taska are safe nothing is deleted.")
            else:
                print("Invalid input try again later.")
        
            
        elif taskDEL >= 1 and taskDEL < (len(self.TL) + 1):
            taskDEL -= 1
            if not self.TL:
                print("You have no tasks to delete!")
                return
            else:
                print("Deleting......")
                self.TL.pop(taskDEL)
                print(f"Deleted Your Task Number {taskDEL + 1}!")

        else:
            print("Invalid input try again.")  
    def edit(self):
        count = 1
        for t in self.TL:
            print(f"Sr. No.: {count}")
            count += 1
            t.show_task()
            print("------")
        print(f"\nWhich task you want to edit: ")
        taskEDIT = int(input())
        taskEDIT -= 1
        task_to_edit = self.TL[taskEDIT]
        if 1 <= (taskEDIT + 1) < (len(self.TL) + 1):
            print("\nDo you want to edit task or date created or both(1, 2, 3): ")
            inp2 = int(input())
            if inp2 == 1:
                task_to_edit.task = input("Enter Your Task Which You Want To Change: ")
            elif inp2 == 2:
                task_to_edit.date = input("Enter Your Date Which You Want To Change: ")
            elif inp2 == 3:
                task_to_edit.task = input("Enter Your Task Which You Want To Change: ")
                task_to_edit.date = input("Enter Your Date Which You Want To Change: ")
            else:
                print("Invalid Input...!")
        print(f"Successfully Edited Your Task {taskEDIT + 1}...!")



def main():
    a = Backend()
    while True:
        print("\n1. Add Task")
        print("2. Show Task")
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
            print("Invalid Input Try Again Later...!")

main()