"""
# Circular Queue -
linear data structure that follows the FIFO (First In First Out) principle 
last position is connected back to the first position, forming a circle. 
This allows for efficient use of space by reusing empty slots created by dequeued elements.

## Basic Operations
Enqueue (insert) -> rear -> O(1)
Dequeue (delete) -> front -> O(1)
Front/Peek -> View the first element -> O(1)
isEmpty -> Check if queue is empty
isFull -> Check if queue is full (for array-based queue)

"""

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.dequeue() #10
cq.enqueue(60) 
cq.dequeue() #20
cq.dequeue() #30
cq.dequeue() #40
cq.dequeue() #50
cq.dequeue() #60
cq.dequeue() #Queue is Empty