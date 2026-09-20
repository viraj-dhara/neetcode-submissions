class Solution:
    def countSubstrings(self, s: str) -> int:
        
        dp = list()
        n = len(s)

        for i in range(n) :
            dp.append(list())
            for j in range(n) :
                dp[i].append(False)

        
        for i in range(n - 1 , -1 , -1) :
            for j in range(i, n) :

                curr_size = j - i + 1

                if s[i] == s[j] and (curr_size <= 3 or dp[i + 1][j - 1] == True) :
                    dp[i][j] = True

        result = 0

        for i in range(n) :
            for j in range(n) :
                if dp[i][j] == True :
                    result += 1

        return result