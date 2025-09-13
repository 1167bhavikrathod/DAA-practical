"""Implement DFS on a tree to perform preorder,
inorder, and postorder traversals."""

class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None   

def preorder(node):
    if node:
        print(node.value , end=' ')
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value , end=' ')
        inorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value , end=' ')


#creating a tree 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Preorder traversal:", end=' ')
preorder(root)
print("\nInorder traversal:", end=' ')
inorder(root)
print("\nPostorder traversal:", end=' ')
postorder(root)

