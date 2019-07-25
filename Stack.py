class Stack():
    def __init__(self):
        self.input = []
    
    def peek(self):
        return self.input[-1]   
        
    def push(self,value):
        self.input.append(value)
        return    
        
    def pop(self): 
        
        return self.input.pop()

    def empty(self):
        if len(self.input) == 0:
            return True
        else:
            return False

