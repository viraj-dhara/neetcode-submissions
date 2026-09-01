# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def __buildTree__(pre: tuple, inO: tuple) -> Optional[TreeNode] :

            nonlocal preorder
            nonlocal inorder
            nonlocal inorder_indices

            size = pre[1] - pre[0]
            if size == 0 :
                root = None
            elif size == 1 :
                root = TreeNode(val = preorder[pre[0]])
            else :

                root = preorder[pre[0]]

                root_index = inorder_indices[root] - inO[0]

                left_tree = __buildTree__((pre[0] + 1, pre[0] + root_index + 1), (inO[0], inO[0] + root_index))

                right_tree = __buildTree__((pre[0] + root_index + 1, pre[1]), (inO[0] + root_index + 1, inO[1]))

                root = TreeNode(root, left_tree, right_tree)

            return root
        
        inorder_indices = dict()
        for i, value in enumerate(inorder):
            inorder_indices[value] = i

        root = __buildTree__((0, len(preorder)), (0, len(inorder)))

        return root
            