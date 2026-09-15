import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        queens_by_row = [(-1,-1)] * n
        results = list()
        curr_board = list()
        
        def isPossible(position: tuple) -> bool :

            nonlocal queens_by_row
            nonlocal n

            x, y = position

            if queens_by_row[x] != (-1,-1) :
                return False
            else :
                for i in range(n) :
                    queen = queens_by_row[i]
                    if queen != (-1,-1) and abs(queen[0] - x) == abs(queen[1] - y) :
                        return False

                return True


        def dfs(column: int, no_of_queens: int, curr_board: List[list]) -> None :

            nonlocal n
            nonlocal results
            nonlocal queens_by_row

            if no_of_queens >= n :
                results.append(copy.deepcopy(curr_board))
                return
            elif column >= n : return
            else :

                for i in range(n) :
                    position = (i, column)
                    if isPossible(position) :
                        queens_by_row[i] = (position)
                        curr_board[i][column] = 'Q'

                        dfs(column + 1, no_of_queens + 1, curr_board)

                        queens_by_row[i] = (-1, -1)
                        curr_board[i][column] = '.'

                        # dfs(column + 1, no_of_queens, curr_board)




                
            

        # Initialize curr_board
        for i in range(n) :
            curr_board.append(list())
            for j in range(n) :
                curr_board[i].append('.')


        dfs(0, 0, curr_board)

        # print(results)

        for board in results :
            for i, row in enumerate(board) :
                board[i] = "".join(row)

        return results