"""
Stack (linear data structure)--> LIFO (Last In First Out)

## Basic Operations
Push -> Insert at top -> O(1)
Pop -> Remove from top -> O(1)
Peek/Top -> View the top element without removing it -> O(1)
isEmpty -> Check if the stack is empty

Top → [ 30 ] 
        [ 20 ]
        [ 10 ]  ← Bottom

## Stack Overflow & Underflow
Overflow: Inserting when stack is full (array implementation)
Underflow: Removing when stack is empty

"""
class stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    #Insertion fron Top 
    def push(self, value):
        self.s.insert(0,value)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s[0]
        

    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s.pop(0)
        
stk = stack()
stk.push(10)
stk.push(20)
stk.push(30)
# print(stk.peek())
print(stk.pop()) #30
print(stk.pop()) #20
print(stk.pop()) #10

""" Assignment:
Insert at the end using append() and 
delete from the end using pop(). 
(more efficient)
"""

class Stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    def push(self, value):
        self.s.append(value)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s[-1]
        
    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s.pop()
        
obj = Stack()
obj.push(100) 
obj.push(200)
obj.push(300)

# print(obj.peek())

print(obj.pop()) #300
print(obj.pop()) #200
print(obj.pop()) #100