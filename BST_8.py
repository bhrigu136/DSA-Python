class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, value):
    if root == None:
        return Node(value)
    if root.value == value:
        return root
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root == None:
        print("Value not found in the BST.", end = '\n')
        return
    if root.value == value:
        print("Value found in the BST.", end = '\n')
        return
    if value < root.value:
        root.left = search(root.left, value)
    else:
        root.right = search(root.right, value)
    return root

def get_successor(node):
    current = node.right    
    while current != None and current.left != None:
        current = current.left
    return current


def delete(root, value):
    if root == None:
        return root
    if root.value > value:
        root.left = delete(root.left, value)
    elif root.value < value:
        root.right = delete(root.right, value)
    else:
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left
        else:
            successor = get_successor(root)
            root.value = successor.value
            root.right = delete(root.right, successor.value)
    return root

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.value, end = ' ')
        inorder(root.right)
            
root = Node(20)
root.left = Node(15)
root.right = Node(30)
root.right.left = Node(25)
root.right.right = Node(40)
root.right.left.left = Node(23)
root.right.right.right = Node(50)

print("Inorder Traversal of the BST:")
inorder(root)  # 15 20 23 25 30 40 50

print("\n\nInserting values into the BST:")
insert(root, 10)
inorder(root)  # 10 15 20 23 25 30 40 50

print("\n\nDeleting values from the BST:")
delete(root, 30)
delete(root, 15)
inorder(root)  # 10 20 23 25 40 50   

print("\n\nSearching for values in the BST:")
search(root, 25)  # Value found in the BST.
search(root, 100)  # Value not found in the BST.    

