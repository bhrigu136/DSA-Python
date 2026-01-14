"""
Doubly Linked List --> linear data structure

Each node has:
+-------+------+------+
| Prev  | Data | Next |
+-------+------+------+
- Prev -> pointer to previous node
- Data -> value stored in the node
- Next -> pointer to next node

Head & Tail
- Head -> First node of the list (Prev = None)
- Tail -> Last node of the list (Next = None)

| Operation     | Description                                            | Time Complexity                              |
| ------------- | ------------------------------------------------------ | -------------------------------------------- |
| **Traversal** | Visit all nodes forward or backward                    | O(n)                                         |
| **Insertion** | Add a node at beginning, end, or a given position      | O(1) at head, O(1) at tail, O(n) at position |
| **Deletion**  | Remove a node from beginning, end, or a given position | O(1) at head/tail, O(n) at position          |
| **Search**    | Find a node by value                                   | O(n)                                         |


### Insertion Types
At beginning -> Node becomes new head
At end -> Node added after tail
At Middle -> Node inserted at specific position

### Deletion Types
From beginning -> Head moves to next node, new head's Prev = None
From end -> Tail moves to previous node, new tail's Next = None
From Middle -> Adjust pointers of previous and next nodes to skip the target node

"""

class Node:
    def __init__(self, value=None):
        self.prev = None
        self.data = value
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        else:
            t = self.head
            while t.next != None:
                t = t.next
            
            t.next = temp
            temp.prev = t

    def insertAtBeg(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertAtMid(self, value, x):
        t = self.head

        while(t.next != None):
            if(t.data == x):
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def deleteDLL(self, value):
        if(self.head == None):
            print("Linked List is empty")
            return
        
        t = self.head
        if(t.data == value):
            self.head = t.next
            self.head.prev = None
            return
        while(t.next != None):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next
        if(t.data == value):
            t.prev.next = None
        
    def displayDLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data, end = " <--> ")
            t1 = t1.next
        print(t1.data)

obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBeg(5)
obj.insertAtMid(50, 20)
obj.deleteDLL(5)
obj.deleteDLL(50)
obj.deleteDLL(40)
obj.displayDLL()


"""
**Circular Linked List** is a linear data structure where:
The last node points back to the first node, forming a circle.
Nodes can be singly or doubly linked.
Unlike standard linked lists, there is no NULL at the end.
"""