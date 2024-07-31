import sys
import os

# Add the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now you can import modules from src
from Task import Task
from Task_Manager import TaskManager

import unittest
class TaskTesting(unittest.TestCase):
    """Test Cases for the Task Class"""

    def test_task_initilizer(self):
        """Check  __init__() method"""
        title = "task 1"
        description = "create task"
        task = Task(title,description)
        self.assertEqual(task.title,title.upper())
        self.assertEqual(task.description,description)

    def test_src_method(self):
        """Test __src__() method"""
        title = "task 1"
        description = "create task"
        task = Task(title,description)
        self.assertEqual(task.__str__(),f"{title.upper()}:\n\t{description}\n")

    def test_repr_method(self):
        """Test __repr__() method"""
        title = "task 1"
        description = "create task"
        task = Task(title,description)
        self.assertEqual(task.__repr__(),f"{title.upper()}-{description}")

    def test_set_title(self):
        """Test setter for title"""
        title = "task 1"
        description = "create task"
        task = Task(title,description)
        newTitle = "task 2"
        task.title = newTitle

        self.assertEqual(task.title,newTitle.upper())
        

class TaskMangerTest(unittest.TestCase):
    """Test the Task_Manager Class"""

    def setUp(self):

        self.tm = TaskManager()

    def test_init(self):
        """Test __init()__ method"""
        self.tm = TaskManager()
        self.assertEqual(self.tm.tasks.__len__(),0)

    def test_add_task(self):
        "Check add_task() function"
        task = Task("Task 1", "My Name is Danial")
        self.tm.add_task(task)
        self.assertIn(task, self.tm.tasks)

    def test_add_invalid_task(self):
        """Test adding invalid task in add_task()"""
        with self.assertRaises(ValueError) as context:
            self.tm.add_task("Not a Task")
            self.assertEqual(str(context.exception), "Invalid Type passed in add_task")

    def test_search_task_found(self):
        """Test search() for found item"""
        task = Task("TaskTitle", "Description")
        self.tm.add_task(task)
        index = self.tm.search_task("TaskTitle")
        self.assertEqual(index, 0)  # Assuming it's the first task added

    def test_search_task_not_found(self):
        """Tes search for not found item"""
        index = self.tm.search_task("NonExistentTitle")
        self.assertEqual(index, -1)

if __name__ == '__main__':
    unittest.main()