from collections import deque

class queue:
    def __init__(self):
        self.buf = deque()


    def enqueue(self,data):
        self.buf.appendleft(data)


    def dequeue(self):
        return self.buf.pop()


    def peek(self):
        return self.buf[-1]




qu = queue()
qu.enqueue(76) 
qu.enqueue(44)  
qu.enqueue(56)  
qu.enqueue(78)    
print(qu.dequeue())   
print(qu.dequeue())               