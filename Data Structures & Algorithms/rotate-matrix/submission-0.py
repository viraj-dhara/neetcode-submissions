class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        length = len(matrix)
        
        for i in range(length // 2) :

            for j in range(length - (2 * i) - 1 ) :
                temp = matrix[i][(i + j)], matrix[(i + j)][length - 1 - i], matrix[length - 1 - i][length - 1 - (i + j)], matrix[length - 1 - (i + j)][i]

                matrix[(i + j)][length - 1 - i], matrix[length - 1 - i][length - 1 - (i + j)], matrix[length - 1 - (i + j)][i], matrix[i][(i + j)] = temp

