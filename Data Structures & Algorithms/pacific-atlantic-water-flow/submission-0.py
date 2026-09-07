class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        check_upwards = deque()
        flows_to = defaultdict(lambda: [0,0])

        for i in range(len(heights)) :
            for j in range(len(heights[0])) :
                if i == 0 or j == 0:
                    flows_to[(i, j)][0] = 1     
                    check_upwards.append((i, j, 0)) # marking pacific
                if i == len(heights) - 1 or j == len(heights[0]) - 1 :
                    flows_to[(i, j)][1] = 1     # marking atlantic
                    check_upwards.append((i, j, 1))

        while check_upwards :

            curr_x, curr_y, ocean = check_upwards.popleft()

            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)] :

                next_x, next_y = curr_x + dx , curr_y + dy

                if next_x >= 0 and next_x < len(heights) and next_y >= 0 and next_y < len(heights[0]) and heights[next_x][next_y] >= heights[curr_x][curr_y]:

                    if not flows_to[(next_x, next_y)][ocean] :
                        flows_to[(next_x, next_y)][ocean] = 1
                        check_upwards.append((next_x, next_y, ocean))

        results = list()

        for key, value in flows_to.items() :
            if value == [1,1] :
                results.append([key[0], key[1]])

        return results



        

