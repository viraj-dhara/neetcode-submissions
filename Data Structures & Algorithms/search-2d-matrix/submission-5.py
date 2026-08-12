class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        colSize = len(matrix)
        rowSize = len(matrix[0])

        if not rowSize and colSize : return False

        s = 0
        l = colSize * rowSize - 1

        while s <= l :
            mid = s + ((l - s) // 2)

            row = mid//rowSize
            col = mid - (row * rowSize)  # COULD've BEEN : col = mid % rowSize

            if matrix[row][col] == target :
                return True
            elif matrix[row][col] < target :
                s = mid + 1
            else :
                l = mid - 1

        return False
