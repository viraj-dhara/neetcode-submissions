class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows_flag = 1 << len(matrix)
        cols_flag = 1 << len(matrix[0])

        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == 0 :
                    rows_flag |= 1 << i
                    cols_flag |= 1 << j

        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if (rows_flag & (1 << i)) or (cols_flag & (1 << j)) :
                    matrix[i][j] = 0

        
