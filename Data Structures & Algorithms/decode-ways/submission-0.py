class Solution:
    def numDecodings(self, s: str) -> int:
        
        def isValid(num) :
            return num > 0 and num < 27

        if s[0] == '0' : return 0

        dp = defaultdict(int) 
        dp[-1] = 1
        dp[-2] = 1

        for index, char in enumerate(s) :

            if char != '0' : 
                dp[index] += dp[index - 1]

            if index == 0 : continue

            two_chars = s[index - 1] + char
            if isValid(int(two_chars)) and s[index - 1] != '0' :
                dp[index] += dp[index - 2]

            if dp[index] == 0 : return 0

        return dp[len(s) - 1]