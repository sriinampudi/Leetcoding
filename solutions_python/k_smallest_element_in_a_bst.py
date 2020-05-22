# Problem 230: K-Smallest Element in a BST 

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.


# Example 1:

# Input: root = [3, 1, 4, null, 2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

# Constraints:

# The number of elements of the BST is between 1 to 10^4.
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cur = root
        while cur:
            if cur.left is None:
                # There is no left subtree, do not create any links
                # just print or decrement k
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right is not cur:
                    # Find predecessor of cur
                    pre = pre.right
                if pre.right is None:
                    # Create a temporary link from predecessor to cur, 1 pass
                    pre.right = cur
                    cur = cur.left
                else:
                    # Remove the link from predecessor to cur from 1 pass
                    # and print or decrement k
                    pre.right = None
                    k -= 1
                    if k == 0:
                        return cur.val
                    cur = cur.right
