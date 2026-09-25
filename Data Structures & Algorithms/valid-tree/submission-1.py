class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n == 1 : return True
        
        connected_with = defaultdict(list)

        for edge in edges :
            i, j = tuple(edge)

            connected_with[i].append(j)
            connected_with[j].append(i)

        # for node in range(n) :
        #     if connected_with[node] == [] :
        #         return False

        def backtracking_dfs(parent_id: int, node_id: int) :

            if curr_visited[node_id] == 1 : return False
            else :
                curr_visited[node_id] = 1

                for child_id in connected_with[node_id] :
                    if child_id == parent_id : continue

                    if backtracking_dfs(node_id, child_id) == False : return False

                return True

        curr_visited = defaultdict(int)

        if backtracking_dfs(-1, 0) == False : return False
        else :
            for i in range(n) :
                if curr_visited[i] == 0 : return False

            return True



                

        


