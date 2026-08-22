class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        i = 0

        while 2 ** i <= n :
            if (2 ** i) & n : 
                count += 1
            i += 1

        return count