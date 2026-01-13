"""
Deque (Double Ended Queue Implementation) - 
insertion and deletion can be performed at both ends — front and rear.

## Basic Operations
InsertAtEnd (insert at rear) -> O(1)
DeleteAtFront (delete from front) -> O(1)   
InsertAtFront (insert at front) -> O(1)
DeleteAtEnd (delete from rear) -> O(1)
peekFront/peekRear -> View the first/last element -> O(1)
isEmpty -> Check if deque is empty
isFull -> Check if deque is full (for array-based deque)
"""
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)== 0
    
    def insertAtEnd(self, value):
        self.items.append(value)

    def deleteAtFront(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop(0)
        
    def insertAtFront(self, value):
        self.items.insert(0, value)

    def deleteAtEnd(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop()

dq = Deque()
dq.insertAtEnd(10)
dq.insertAtFront(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtFront(50)
print(dq.deleteAtEnd()) #40
print(dq.deleteAtEnd()) #30
print(dq.deleteAtFront()) #50
print(dq.deleteAtFront()) #20
print(dq.deleteAtFront()) #10
print(dq.deleteAtFront()) #Queue is Empty
print(dq.deleteAtEnd()) #Queue is Empty

        