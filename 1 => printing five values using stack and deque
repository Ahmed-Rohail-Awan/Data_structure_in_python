#printing five values using stack and deque

from collections import deque
stack = deque()

# defining function like pop() push() top() etc ao we can use them anywhere by passing arguments
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
        
#example

s=Stack()
for x in range(1,5):
    s.push(x)
for x in range(s.size()):
    print(s.pop())        
