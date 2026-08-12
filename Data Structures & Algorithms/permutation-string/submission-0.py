class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #ensure s1 is larger string
        if len(s1) > len(s2) : 
            return False

        freq_of_chars = defaultdict(int)

        for i in range(len(s1)) :
            freq_of_chars[s1[i]] += 1

        print(dict(freq_of_chars))

        win_start = 0
        win_end = 0
        

        while win_end < len(s2) :
            print(s2[win_start], s2[win_end])
            freq_of_chars[s2[win_end]] -= 1
            print(dict(freq_of_chars))

            if min(freq_of_chars.values()) < 0 :
                freq_of_chars[s2[win_start]] += 1
                win_start += 1
            elif not any(freq_of_chars.values()) : return True

            if (win_end - win_start) < len(s1) : win_end += 1

        return False

