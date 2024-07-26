'''class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def is_symmetric(root):
    inorder_list = inorder(root)
    return inorder_list == inorder_list[::-1]

# Take dynamic input
num_nodes = int(input("Enter the number of nodes: "))
root = None
for i in range(num_nodes):
    val = int(input(f"Enter value for node {i+1}: "))
    root = insert(root, val)

# Check if the tree is symmetric
print(is_symmetric(root))'''

from typing import Optional, List
class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.inOrderTraversalUtil(root, answer)
        return answer
    def inOrderTraversalUtil(self, root: Optional[TreeNode], answer: List[int]):
        if root is None:
            return
        self.inOrderTraversalUtil(root.left, answer)
        answer.append(root.val)
        self.inOrderTraversalUtil(root.right, answer)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kid_nodes = nodes[::-1]
    root = kid_nodes.pop()
    for node in nodes:
        if node:
            if kid_nodes: node.left = kid_nodes.pop()
            if kid_nodes: node.right = kid_nodes.pop()
    return root
# Dynamic input
input_values = input("Enter the tree nodes in level order (use 'null' for empty nodes): ").split()
values = [int(x) if x != 'null' else None for x in input_values]
# Building the tree
root = build_tree(values)
# Checking if the tree is symmetric
solution = Solution()
print(solution.isSymmetric(root))
