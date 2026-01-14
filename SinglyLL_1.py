"""
Singly Linked List --> linear data structure
 -Each node has:
    Data -> The value stored
    Next -> Pointer to the next node

- Traversal is in one direction only, from head → tail.
Head → First node of the list
Tail → Last node, points to None

| Operation     | Description                                            | Time Complexity                    |
| ------------- | ------------------------------------------------------ | ---------------------------------- |
| **Traversal** | Visit all nodes from head to tail                      | O(n)                               |
| **Insertion** | Add a node at beginning, end, or a given position      | O(1) at head, O(n) at end/position |
| **Deletion**  | Remove a node from beginning, end, or a given position | O(1) at head, O(n) at end/position |
| **Search**    | Find a node by value                                   | O(n)                               |

## Insertion Types
**At beginning** -> Node becomes new head
**At end** -> Node added after tail (traverse to end)
**At Middle** -> Node inserted at specific position

## Deletion Types
From beginning -> Head moves to next node
From end -> Traverse to second last node, set its next = None
From position -> Skip the node at that position


"""
class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
    
    def insertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertInMid(self, value, x):
        temp = Node(value)
        t1 = self.head

        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deleteLL(self, value):
        t1 = self.head
        prev = t1
        if(t1.data == value):
            self.head = t1.next
        while(t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next

        if(t1.data == value):
            prev.next = None

    def display(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data, end=" ")
            t1 = t1.next
        print(t1.data)
        
obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertInMid(40,20)
obj.deleteLL(30)
obj.display()