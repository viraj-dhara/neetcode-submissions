# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if (root == None) ^ (subRoot == None) : return False
        elif root == None and subRoot == None : return True
        
        def isSameTree(p, q) -> bool:
            if p == None and q == None : return True
            elif p == None : return False
            elif q == None : return False
            elif p.val != q.val : return False
            else:
                return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)

        return isSameTree(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot) 