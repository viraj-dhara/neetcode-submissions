class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        answer = 0
        
        for i, val in enumerate(prices[:-1]) :
            for j in prices[i+1:] :
                if j-val > answer :
                    print(val, j)
                    answer = j-val

        return answer