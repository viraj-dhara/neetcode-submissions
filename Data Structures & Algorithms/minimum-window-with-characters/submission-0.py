class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t) : return ""

        freq = defaultdict(int)

        for i in range(len(t)) :
            freq[t[i]] += 1

        win_start = 0
        win_end = 0
        min_length = len(s) + 1
        result = ""
        flag = 0

        while win_end < len(s) and win_start < len(s) :
            
            if flag == 0  :
                freq[s[win_end]] -= 1
                flag = 1


            if max(freq.values()) <= 0 and min_length > win_end - win_start +1:
                min_length = win_end - win_start + 1
                result = s[win_start:win_end + 1]
            
            if freq[s[win_start]] < 0 :
                freq[s[win_start]] += 1
                win_start += 1
            else : 
                win_end += 1
                flag = 0

        return result