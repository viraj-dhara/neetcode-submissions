class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        # for line in grid:
        #     print(line)

        def island_traverse(i, j, area) -> int:

            nonlocal max_area

            try :
                if i<0 or j<0 or grid[i][j] == 0 :
                    max_area = max(max_area, area)
                    return area
                else :
                    area += 1
                    grid[i][j] = 0

                    max_area = max(max_area, area)

                    area = island_traverse(i, j+1, area)
                    area = island_traverse(i+1, j, area)
                    area = island_traverse(i, j-1, area)
                    area = island_traverse(i-1, j, area)

                    return area

            except IndexError :
                max_area = max(max_area, area)
                return area

        max_area = 0
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 1 :
                    # print(f"\nIsland at: {i, j}\n")
                    island_traverse(i, j, 0)
                    # for line in grid : print(line)

        return max_area