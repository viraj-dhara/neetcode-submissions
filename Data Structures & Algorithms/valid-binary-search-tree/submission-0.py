# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root, small, big) :

            if root is None : return True

            if root.val not in range(small + 1, big) : return False

            return dfs(root.left, small, root.val) and dfs(root.right, root.val, big)

        return dfs(root, - 2**31 - 1, 2**31 + 1)