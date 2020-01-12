from collections import deque 

class Stack:
    def __init__(self):
        self.container = deque()

    def isempty(self):
        if len(self.container) > 0:
            return False
        else:
            return True
    
    def push(self,data):
        self.container.append(data)
    
    def pop(self):
        if not self.isempty():
            self.container.pop()
        else:
            raise Exception("Trying to get value from empty stack.")
    
    def peek(self):
        if not self.isempty():
            return self.container[-1]
        else:
            raise Exception("Trying to get value from empty stack.")