from Task import Task,createTask
from Task_Manager import TaskManager as TS


tm = TS()

tm.load_from_file()
print("Welcome!\n")

while True:
    #Printing menu
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Update Task")
    print("q. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        tm.view_tasks()
    elif choice == "2":
        task = createTask()
        tm.add_task(task)
    elif choice == "3":
        title = input("\nEnter the title of task: ")
        tm.delete_task(title)
    elif choice == "4":
        title = input("\nEnter the title of task: ")
        tm.update_task(title)
    elif choice == "q":
        break
    else:
        print("Wrong Input")


tm.write_to_file()



