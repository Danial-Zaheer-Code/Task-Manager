
class Task:
    """A class to model tasks having a title and description"""
    
    def __init__(self,title,description):
        """Initialize the member variable"""
        self.title = title
        self.description = description

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}"
    
    #Getter/Seters
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description



a = Task("D","NNNNN")

print("1:",a)


    
a.title = "n"
print("1:",a)