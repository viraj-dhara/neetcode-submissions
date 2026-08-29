"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None : return None

        def create_copy_node(node) :
            if node_pointers[node.val] != 0 :
                return 
            else :
                node_pointers[node.val] = Node(node.val)

                for neighbor in node.neighbors :
                    create_copy_node(neighbor)

                return 
        
        def make_copy_connections(og_node, new_node) :
            if len(og_node.neighbors) == len(new_node.neighbors) :
                return

            elif og_node.val != new_node.val :

                print("U done messed up man. Values on nodes don't match")

                return

            else :
                for og_neigh in og_node.neighbors :
                    new_node.neighbors.append(node_pointers[og_neigh.val])
                    
                for n1, n2 in zip(og_node.neighbors, new_node.neighbors) :
                    make_copy_connections(n1, n2)

                return 
        
        # val -> pointer
        node_pointers = defaultdict(int)

        create_copy_node(node)
        make_copy_connections(node, node_pointers[node.val])

        return node_pointers[node.val]

