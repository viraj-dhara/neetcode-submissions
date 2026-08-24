class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 1 : return matrix[0]

        visited = defaultdict(lambda: False)
        result = list()

        i, j = 0, 0
        direction = 0

        while visited[(i,j)] != True and i >= 0 and j >= 0:

            result.append(matrix[i][j])

            visited[(i,j)] = True

            if direction == 0 :
                if (j + 1) < len(matrix[0]) and visited[(i, j+1)] != True :
                    j += 1
                else :
                    direction = 1
                    i += 1
            elif direction == 1 :
                if (i + 1) < len(matrix) and visited[(i+1, j)] != True :
                    i += 1
                else :
                    direction = 2
                    j -= 1
            elif direction == 2 :
                if (j - 1) >= 0 and visited[(i, j-1)] != True :
                    j -= 1
                else :
                    direction = 3
                    i -= 1
            elif direction == 3 :
                if (i - 1) >= 0 and visited[(i-1, j)] != True :
                    i -= 1
                else :
                    direction = 0
                    j += 1 

        return result
