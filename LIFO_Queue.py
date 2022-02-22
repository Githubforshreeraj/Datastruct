class lifoQue:
    def __init__ (self, capacity):
       self.capacity = capacity
       self.pointer =  0
       self.pipe = [None]*capacity
    
    def enquing (self, item):
        self.pipe[self.pointer]=item
        self.pointer += 1
        
    
    def dequeue(self):
        temp = self.pipe[self.pointer-1]
        self.pipe[self.pointer-1] = None
        self.pointer -= 1
        return temp