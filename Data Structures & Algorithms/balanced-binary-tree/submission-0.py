# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None : return True

        isBalanced_flag = True

        def height(root) :

            nonlocal isBalanced_flag
            if root == None or isBalanced_flag is False : return 0

            height_right = height(root.right)
            height_left = height(root.left)

            if abs(height_right - height_left) > 1 :
                isBalanced_flag = False

            return max(height_right, height_left) + 1

        height(root)

        return isBalanced_flag

        