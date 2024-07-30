from Task import Task
import json
class TaskManager:
    """
    This class with model a Task_Manger that will let user
    add/delete/update/view tasks
    """

    def __init__(self):
        """Initializing the main list"""
        self.tasks = []      #List of Task Objects

    def write_to_file(self):
        """write all the Tasks to the .json file"""
        
        #Coverting all objects to string format and storin in list "data"
        data = []
        for t in self.tasks:
            data.append(t.__repr__())
        
        #Dumping "data" list in the .json file
        with open("Tasks.json",'w') as obj:
            json.dump(data,obj)
    
    def load_from_file(self):
        """Rading all data from .json file as a list f strings and then convert it to list of Task objects"""
        try:
            with open("Task.json") as obj:  #Opening the task file if it exist
                data = json.load(obj)
        except FileNotFoundError:   #if the file don't exist than we will just pass
            pass
        else:               #if the file exist than convert all the data to list of Task objects
            for t in data:
                self.tasks.append(Task.from_str(t))
        

    def add_task(self,task):
        """Add a new task to the tasks"""
        if isinstance(task,Task):       #if passed object is an instance of Task class
            self.tasks.append(task)
        else:
            raise ValueError("Invalid Type passed int add_task")
        
    def view_tasks(self):
        """Diplay all tasks on console in a formatted manner"""
        if self.tasks.__len__() != 0:
            for task in self.tasks:
                print(task)
        
    def search_task(self,title):
        """Search a task by title and return its index"""
        i = 0
        while i < self.tasks.__len__():     #Iterating through the task list
            if self.tasks[i].title == title:
                return i                    #if found return index
            i += 1
        return -1       #if not found return -1



