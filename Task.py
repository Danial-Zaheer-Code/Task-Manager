
class Task:
    """A class to model task having a title and description"""
    
    def __init__(self,title,description):
        """Initialize the member variable"""
        self.title = title.upper()
        self.description = description

    def __repr__(self):
        """Return the dtring format of task to save in json file"""
        return f"{self.title}-{self.description}"

    def __str__(self):
        """To display yo end user"""
        return f"{self.title}:\n\t{self.description}\n"
    
    #Getter/Seters
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title.upper()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @classmethod
    def from_str(cls,str):
        """Covert a string back to Task Object"""
        title,description = str.split('-')
        return cls(title,description)
    


