/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution
{
public:
    TreeNode *invertTree(TreeNode *root)
    {
        if (root == NULL)
        {
            return NULL; // terminal condition
        }
        auto left = invertTree(root->left);   // invert left sub-tree
        auto right = invertTree(root->right); // invert right sub-tree
        root->left = right;                   // put right on left
        root->right = left;                   // put left on right
        return root;
    }
};