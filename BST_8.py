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
    
def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.value, end = ' ')
        inorder(root.right)
            
root = insert(None, 20)
root = insert(root, 30)
root = insert(root, 15)
root = insert(root, 25)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 23)
print("Inorder Traversal of the BST:")
inorder(root)  # 15 20 23 25 30 40s
    

# root = Node(20)
# root.left = Node(15)
# root.right = Node(30)
# root.right.left = Node(25)
# root.right.right = Node(40)
# root.right.left.left = Node(23)
# root.right.right.right = Node(50)
    # print("Inorder Traversal of the BST:")
    # root.inorder(root)  # 15 20 23 25 30 40