class CountSquares:

    def __init__(self):

        self.all_points = defaultdict(int)
        # self.iterations = 0
        self.non_z_points = list()

    def add(self, point: List[int]) -> None:
        
        self.all_points[(point[0], point[1])] += 1
        self.non_z_points.append(point)
        
    def count(self, point: List[int]) -> int:
        
        x, y = point
        count_squares = 0

        for i, j in self.non_z_points :
            if i != x and j != y and abs(i-x) == abs(j-y) :
                count_squares += self.all_points[(i,y)] * self.all_points[(x,j)] 

        # self.iterations += 1
        # if self.iterations < 20 and count_squares in [5,15,9]:
        #     print(f"\n{point = }\n{count_squares = }\n{self.all_points = }\n")

        return count_squares
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
