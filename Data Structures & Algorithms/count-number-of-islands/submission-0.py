class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        def island_destroyer(i, j) :

            try :
                if i<0 or j<0 or i>len(grid) or j>len(grid[0]) or grid[i][j] == "0" :
                    return
                else :
                    grid[i][j] = "0"

                    island_destroyer(i,j+1)
                    island_destroyer(i+1,j)
                    island_destroyer(i,j-1)
                    island_destroyer(i-1,j)
            except IndexError :
                print(i, j, " IndexError")
                return
        count = 0
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == "1" :
                    count += 1
                    island_destroyer(i, j)

        return count

            

            