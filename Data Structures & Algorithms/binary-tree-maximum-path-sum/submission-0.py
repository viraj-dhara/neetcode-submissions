# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = -1001

        if root is None : return 0
        if root.right is None and root.left is None : return root.val

        def post_order(root) -> int :

            nonlocal max_sum

            if root is None : return 0
            if root.right is None and root.left is None : 
                max_sum = max(max_sum, root.val)
                return root.val

            left_sum = post_order(root.left)
            right_sum = post_order(root.right)

            max_sum = max(max_sum, left_sum + right_sum + root.val, root.val, right_sum + root.val, left_sum + root.val)

            return max(left_sum + root.val, right_sum + root.val, root.val, 0)

        post_order(root)

        return max_sum


        