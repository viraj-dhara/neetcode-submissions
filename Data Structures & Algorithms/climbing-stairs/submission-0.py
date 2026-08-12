class Solution:
    def climbStairs(self, n: int) -> int:
        
        self.steps = [0] * n

        for i in range(n) :
            if i == 0 : self.steps[i] = 1
            elif i == 1 : self.steps[i] = 2
            else :
                self.steps[i] = self.steps[i-1] + self.steps[i-2]

        return self.steps[n - 1]