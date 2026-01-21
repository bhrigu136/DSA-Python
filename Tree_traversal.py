class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def preorder(self, root):
        if root != None:
            print(root.value, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print(root.value, end = ' ')
            self.inorder(root.right)

    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end = ' ')


root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)


print("Preorder Traversal:")
root.preorder(root)   # 1 3 2 4 5 8
print("\nInorder Traversal:")
root.inorder(root)    # 2 3 4 1 5 8 
print("\nPostorder Traversal:")
root.postorder(root)  # 2 4 3 8 5 1 