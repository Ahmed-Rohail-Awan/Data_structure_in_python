#function to reverse string

from collections import deque
stack = deque()
class Stack : 
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def top(self):
        return container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    
    #reverse function which will reverse our string
    def reverse(self,val):
        for x in val:
            self.container.append(x)
        for i in range(len(self.container)):
            print(self.container.pop())
            
            
# example

r=Stack()
r.reverse("your name is ahmed")            
