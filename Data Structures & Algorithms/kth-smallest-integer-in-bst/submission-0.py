# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        for i in range(k - 1) :

            curr = root
            prev = curr

            while curr.left is not None : 
                prev = curr
                curr = curr.left

            prev.left = curr.right
            
        while root.left is not None :   
            root = root.left
        
        return root.val