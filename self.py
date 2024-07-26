class Operations:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):  # Need to include the 'self' parameter
        print("inside add")
        return self.x + self.y  # Accessing class variables using 'self'
    
    def sub(self):  # Need to include the 'self' parameter
        print("inside sub")
        return self.x - self.y  # Accessing class variables using 'self'

ActualOps = Operations(4, 36)

print(ActualOps.add())  # Calling the 'add' method of the 'Operations' class
print(ActualOps.sub()) 
