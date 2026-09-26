class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        connected_to = defaultdict(list)

        for n1, n2 in edges :
            connected_to[n1].append(n2)
            connected_to[n2].append(n1)

        result = [-1] * n
        

        def mark_recursive(parent: int, node: int) -> None :

            for child in connected_to[node] :
                if result[child] == 1 : continue
                result[child] = 1
                mark_recursive(node, child)

        parts = 0
        while True :

            completion_flag = True
            unmarked_node = -1

            for i in range(n) :
                if result[i] == -1 :
                    unmarked_node = i
                    completion_flag = False
                    break

            if completion_flag : break
            else :
                result[unmarked_node] = 1
                mark_recursive(-1, unmarked_node)
                parts += 1



        return parts

            
