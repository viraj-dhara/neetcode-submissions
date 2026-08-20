# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None : return []

        tree_hashmap = defaultdict(list)

        def record_tree (root, level, tree_hashmap: dict) :

            root.left and record_tree(root.left, level + 1, tree_hashmap)
            root.right and record_tree(root.right, level + 1, tree_hashmap)
            tree_hashmap[level].append(root.val)

        record_tree(root, 0, tree_hashmap)

        result = []
        for i in range(len(tree_hashmap)) :
            result.append(tree_hashmap[i][-1])

        return result