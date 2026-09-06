class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten_queue = deque()

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 2 :
                    rotten_queue.append((i, j, 0))

        print(rotten_queue)

        time = 0

        while rotten_queue :

            curr_x, curr_y, curr_time = rotten_queue.popleft()

            print(rotten_queue, curr_time)
            time = max(time, curr_time)

            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)] :
                next_x, next_y = curr_x + dx , curr_y + dy
                if next_x >= 0 and next_x < len(grid) and next_y >= 0 and next_y < len(grid[0]) and grid[next_x][next_y] == 1 :
                    rotten_queue.append((next_x, next_y, curr_time + 1))
                    grid[next_x][next_y] = 2

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 1 :
                    return -1

        return time
