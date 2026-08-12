# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root.left == None and root.right == None :  return 0

        # apply dfs to visit every Node
        # calc diameter at every Node
        # keep track of maximum all throughout

        max_diameter = 0

        def do_recursive_dfs(root) :

            if root == None : return 0

            left_height = do_recursive_dfs(root.left)
            right_height = do_recursive_dfs(root.right)

            my_diameter =  left_height + right_height + 1

            nonlocal max_diameter
            max_diameter = max(max_diameter, my_diameter)

            return max(left_height, right_height) + 1

        do_recursive_dfs(root)

        return max_diameter - 1