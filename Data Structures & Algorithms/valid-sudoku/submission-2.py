class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [[0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9)]
        boxes = [[0 for _ in range(9)] for _ in range(9)]

        # validate rows
        for i in range(9):
            for j in range(9):
                if board[i][j] == "." : continue
                
                num = int(board[i][j]) - 1

                if rows[i][num] == 1 : return False
                else : rows[i][num] = 1

        # validate cols
        for i in range(9):
            for j in range(9):
                if board[i][j] == "." : continue
                
                num = int(board[i][j]) - 1

                if cols[j][num] == 1 : return False
                else : cols[j][num] = 1

        # validate boxes
        for i in range(9):
            for j in range(9):
                if board[i][j] == "." : continue
                
                num = int(board[i][j]) - 1

                if boxes[ (i//3) * 3 + (j//3) ][num] == 1 : return False
                else : boxes[ (i//3) * 3 + (j//3) ][num] = 1

        return True