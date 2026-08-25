class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 : return 1
        if x == 0 : return 0

        _ = self.myPow(x, abs(n) // 2)
        result = _ * _

        if n % 2 == 1 : result *= x

        if n < 0 :
            return 1/result
        else :
            return result
        


        