class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def neighbors(curr: tuple) -> list :
            
            nonlocal board
            neighbors_result = list()

            if curr[0] > 0 :
                neighbors_result.append((curr[0] - 1, curr[1]))
            if curr[1] > 0 :
                neighbors_result.append((curr[0], curr[1] - 1))
            if curr[0] < len(board) - 1 :
                neighbors_result.append((curr[0] + 1, curr[1]))
            if curr[1] < len(board[0]) - 1 :
                neighbors_result.append((curr[0], curr[1] + 1))

            return neighbors_result
            
        def dfs(index, visited: list) :

            nonlocal board
            nonlocal word

            if index == len(word) :
                return True
            else :
                truth = False
                for i, j in neighbors(visited[-1]) :
                    if (i,j) not in visited and board[i][j] == word[index]:
                        visited.append((i,j))
                        truth = truth or dfs(index + 1, visited)
                        visited.pop(-1)

            return truth

        
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if board[i][j] == word[0] and dfs(1, [(i,j)]) : return True

        return False