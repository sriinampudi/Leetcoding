# Problem 1008: Construct Binary Tree from Pre-Order Traversal

# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

# Example 1:

# Input: [8, 5, 1, 7, 10, 12]
# Output: [8, 5, 10, 1, 7, null, 12]


# Constraints:

# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10 ^ 8
# The values of preorder are distinct.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return

        root = TreeNode(preorder[0])

        def insert(val, node):
            # we insert a single element using this function

            while True:
                # Here we check whether root's value is greater than the given value.
                # If yes then try to insert it in the left sub-tree.
                if node.val > val:
                    # Here we check if the left child does not exist then we add a left child with value = val and break the loop
                    if not node.left:
                        node.left = TreeNode(val)
                        break
                     # Since the left child exists we move towards the left.
                    else:
                        node = node.left
                # This will work similar to the left child.
                else:
                    if not node.right:
                        node.right = TreeNode(val)
                        break
                    else:
                        node = node.right
        head = root
        for i in range(1, len(preorder)):
            # Here we reset the head pointer so we are the top of the tree again.
            head = root
            insert(preorder[i], head)

        return head
