class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        s = list(s)
        win_start = 0
        max_length = 0
        freq = defaultdict(int)

        for win_end in range(len(s)) :
            
            # expand window
            freq[s[win_end]] += 1

            #check condition and shrink window from left
            if freq[max(freq, key= freq.get)] + k < win_end - win_start + 1:
                freq[s[win_start]] -= 1
                win_start += 1
            
            # calculate desired value
            max_length = max(max_length, win_end - win_start + 1)

        return max_length


             
