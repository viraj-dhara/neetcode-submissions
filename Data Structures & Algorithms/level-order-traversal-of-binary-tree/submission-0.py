# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None : return []

        result = defaultdict(list)

        def dfs (root, level, result: dict) :

            root.left and dfs(root.left, level + 1, result)
            root.right and dfs(root.right, level + 1, result)
            result[level].append(root.val)

        dfs(root, 0, result)

        i = 0
        final_result = list()
        while result != {} :
            final_result.append(result[i])
            del result[i]
            i += 1

        return final_result
