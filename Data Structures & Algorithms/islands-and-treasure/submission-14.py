class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def my_neigh(curr: tuple) -> list :
            
            nonlocal grid

            result = list()
            i, j = curr

            if i > 0 :
                result.append((i - 1, j))
            if j > 0 :
                result.append((i, j - 1))
            if i < len(grid) - 1 :
                result.append((i + 1, j))
            if j < len(grid[0]) - 1 :
                result.append((i, j + 1))

            return result

        distance = 0
        exploring_pts = list()
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 0 :
                    exploring_pts.append((i,j))

        while exploring_pts :

            new_exploring_pts = list()

            for i,j in exploring_pts :

                for neigh_x, neigh_y in my_neigh((i,j)) :
                    if grid[neigh_x][neigh_y] == 2 ** 31 - 1 :
                        grid[neigh_x][neigh_y] = distance + 1
                        new_exploring_pts.append((neigh_x, neigh_y))

            exploring_pts = new_exploring_pts
            new_exploring_pts = list()
            distance += 1

        

        

        

