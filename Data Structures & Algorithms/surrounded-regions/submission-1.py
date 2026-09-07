class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(x, y) :

            nonlocal board

            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) :
                return False
            return True

        my_queue = deque()
        
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if board[i][j] == 'O' and i != 0 and j != 0 and i != len(board) - 1 and j != len(board[0]) - 1:
                    board[i][j] = "XO"
                elif board[i][j] == 'O' :
                    my_queue.append((i, j))


        while my_queue :

            curr_x, curr_y = my_queue.popleft()

            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)] :

                next_x, next_y = curr_x + dx, curr_y + dy

                if valid(next_x, next_y) and board[next_x][next_y] == "XO" :

                    board[next_x][next_y] = 'O'
                    my_queue.append((next_x, next_y))

        # print(board)

        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if board[i][j] == "XO" :
                    board[i][j] = 'X'

        
