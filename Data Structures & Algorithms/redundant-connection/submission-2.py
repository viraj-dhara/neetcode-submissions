class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        
        par = [ i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        def find(node_id : int) -> int :
            parent_id = par[node_id]
            while parent_id != node_id :
                node_id = parent_id
                parent_id = par[parent_id]

            return parent_id


        def union(node_1 : int, node_2 : int) :

            parent_1, parent_2 = find(node_1), find(node_2)

            if parent_1 == parent_2 : return False
            elif rank[parent_1] < rank[parent_2] :
                par[parent_1] = parent_2
                rank[parent_1] += 1
            else :
                par[parent_2] = parent_1
                rank[parent_2] += 1

            return True

        for i in range(len(edges)) :
            if not union(edges[i][0], edges[i][1]) :
                return [edges[i][0], edges[i][1]]

 