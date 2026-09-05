# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def height(self, root) -> int:

        if root is None :
            return 0
        else :
            return max(self.height(root.right), self.height(root.left)) + 1
    
    def __serialize_recursive__(self, root, store_at, serialized: dict) :

        if root is None : return
        self.__serialize_recursive__(root.left, 2 * store_at + 1, serialized) if root.left is not None else None
        self.__serialize_recursive__(root.right, 2 * store_at + 2, serialized) if root.right is not None else None
        serialized[store_at] = root.val

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root : return ""

        serialized = dict()

        self.__serialize_recursive__(root, 0, serialized)

        # print(f"{serialized=}")
        
        # print(str(serialized))

        return str(serialized)

    def __str_to_dict__(self, data) -> dict :

        output = defaultdict(lambda: None)
        curr_val = ""
        curr_key = ""

        for char in data :
            if char in ",}" :
                output[int(curr_key)] = int(curr_val)
                curr_val = ""
                curr_key = ""
            elif char == ":" :
                curr_key = curr_val[:]
                curr_val = ""
            elif char != "{" :
                curr_val += char

        # print("__str_to_dict__ output = ", output)

        return output
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if data == "" : return None

        data = self.__str_to_dict__(data)

        for key, val in data.items() :
            data[key] = TreeNode(val)
        
        for key, node in list(data.items()) :
            data[key].left = data[2 * key + 1]
            data[key].right = data[2 * key + 2]


        return data[0]
