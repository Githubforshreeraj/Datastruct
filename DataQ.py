
from sqlalchemy import false


class Queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.pipe = [None]*capacity
        self.pointer = 0
        print("initialized new Q : ",self.pipe)
    
    def addElement (self,item):
        if self.isQuefull():
           print("list is full ")
           return False
        else:
            self.pipe[self.pointer]=item
            self.pointer += 1
            print("Added new Item :",item)
            print("Queue :->   ", self.pipe)
            return True
    
    def isQuefull( self):
        if self.pipe[-1] == None:
            return False
        else:
            return True
    
    def getElement (self):
        temp = self.pipe[0]
        for j in range(1, self.pointer):
            self.pipe[j-1] = self.pipe[j]
        self.pointer -= 1
        self.pipe[self.pointer]=None
        print("Giving back : ", temp)
        print("Queue -> ", self.pipe)
        return temp
        
    
        

        





        