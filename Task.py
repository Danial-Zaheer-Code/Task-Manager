
class Task:
    """A class to model tasks having a title and description"""
    
    def __init__(self,title,description):
        """Initialize the member variable"""
        self.title = title
        self.description = description

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}"
    

a = Task("D","NNNNN")

print("1:",a)


    
