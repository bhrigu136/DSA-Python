"""
Queue - (linear data structure) --> FIFO (First In First Out)
Types -
- Simple Queue
- Double Ended Queue
- Circular Queue
- Priority Queue

## Basic Operations
Enqueue (insert) -> rear -> O(1)
Dequeue (delete) -> front -> O(1)
Front/Peek -> View the first element -> O(1)
isEmpty -> Check if queue is empty
isFull -> Check if queue is full (for array-based queue)

### Queue Overflow & Underflow
Overflow: Inserting when queue is full
Underflow: Deleting when queue is empty
Note: In python, we don't need to check 

"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)== 0
    
    def insert(self, value):
        self.items.append(value)

    def delete(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop(0)
        
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)

print(q.delete()) #10
print(q.delete()) #20
print(q.delete()) #30
print(q.delete()) #40
print(q.delete()) # Queue is Empty
        