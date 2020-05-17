# Problem 94: Binary Tree Inorder Traversal
# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1, null, 2, 3]
#   1
#     \
#          2
#     /
#    3

# Output: [1,3,2]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left

#Recusrive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    def __init__(self):
        self.s = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        self.inorderTraversal(root.left)
        self.s.append(root.val)
        self.inorderTraversal(root.right)
        return self.s
