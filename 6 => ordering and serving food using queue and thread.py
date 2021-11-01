#importing time and thread
import time   
import threading

#Queue class 
class Queue:
    def __init__(self):
        self.container= []
    def enqueue(self,val):
        self.container.insert(0,val)
    def dequeue(self):
        return self.container.pop()
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)


q=Queue()
#function 1 to insert value in queue after 0.5 seconds
def place_order():
    orders=['pizza','samosa','pasta','biryani','burger']
    for x in orders:
        q.enqueue(x)
        time.sleep(0.5)
#function to print all order after 2 seconds
def serve_order():
    for x in range(1,6):
        print(q.dequeue())
        time.sleep(2)



#creating thread
t1 = threading.Thread(target = place_order )
t2 = threading.Thread(target = serve_order )

#starting threads 
t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()
