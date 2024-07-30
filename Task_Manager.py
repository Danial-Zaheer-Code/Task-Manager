from Task import Task
import json
class TaskManager:
    """
    This class with model a Task_Manger that will let user
    add/delete/update/view tasks
    """

    def __init__():
        """Initializing the main list"""
        tasks = []      #List of Task Objects

    def write_to_file():
        """write all the Tasks to the .json file"""
        
        #Coverting all objects to string format and storin in list "data"
        data = []
        for t in tasks:
            data.append(t.__repr__())
        
        #Dumping "data" list in the .json file
        with open("Tasks.json",'w') as obj:
            json.dump(data,obj)
    
    def load_from_file():
        """Rading all data from .json file as a list f strings and then convert it to list of Task objects"""
        try:
            with open("Task.json") as obj:  #Opening the task file if it exist
                data = json.load(obj)
        except FileNotFoundError:   #if the file don't exist than we will just pass
            pass
        else:               #if the file exist than convert all the data to list of Task objects
            for t in data:
                tasks.append(Task.from_str(t))
        

          
         
