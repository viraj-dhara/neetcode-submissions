# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_count = 0

        def dfs(root, current_max) :

            if root is None : return

            nonlocal good_count

            if root.val >= current_max :
                good_count += 1
                current_max = root.val

            if root.val < current_max : 
                pass    # current_max, good_count stay same

            dfs(root.left, current_max)
            dfs(root.right, current_max)

        dfs(root, root.val)

        return good_count