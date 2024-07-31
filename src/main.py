from Task import Task,createTask
from Task_Manager import TaskManager as TS


tm = TS()

tm.load_from_file()     #loading data from file
print("Welcome!\n")

while True:
    print("\n1. View Tasks")    #printing menu
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Update Task")
    print("q. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":       #View tasks
        tm.view_tasks()

    elif choice == "2":     #add tasks
        while True:
            task = createTask()
            if tm.search_task(task.title) == -1:    #checking for dublicates
                break
            else:
                print("\nDublicate titles are not allowed.Enter again\n")
        
        tm.add_task(task)

    elif choice == "3":     #remove task
        if tm.tasks.__len__() == 0:      #if task list is empty
            print("Task List is empty")

        else:
            title = input("\nEnter the title of task: ")
            tm.delete_task(title)

    elif choice == "4":     #update task
        if tm.tasks.__len__() == 0:      #if task list is empty
            print("Task List is empty")

        else:
            title = input("\nEnter the title of task: ")
            tm.update_task(title)

    elif choice == "q":     #quit
        break
    
    else:
        print("Wrong Input")


tm.write_to_file()



