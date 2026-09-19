class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s : return ""
        
        dp = list()

        for i in range(len(s)) :
            dp.append(list())
            for j in range(len(s)) :
                dp[i].append(False)

        # print(dp)

        max_len = 0
        max_idx = 0


        for i in range(len(s) - 1, -1, -1) :
            for j in range(i, len(s)) :

                size = j - i + 1

                if s[j] == s[i] and (size < 4 or dp[i+1][j-1] == True) :

                    dp[i][j] = True
                    if size > max_len :
                        max_len = size
                        max_idx = i

        return s[max_idx: max_idx + max_len]

