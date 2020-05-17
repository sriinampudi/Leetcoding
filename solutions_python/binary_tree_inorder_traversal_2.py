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

# Iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return_list = []
        stack = []
        node = root

        while True:

            if node is not None:
                stack.append(node)
                node = node.left

            elif(stack):
                node = stack.pop()
                return_list.append(node.val)
                node = node.right
            else:
                break
        return return_list
