class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t) :
            return False

        counts1 = {chr(i): 0 for i in range(65, 91)}
        counts2 = {chr(i): 0 for i in range(65, 91)}

        for c in list(s.upper()) :
            counts1[c] += 1
        
        for c in list(t.upper()) :
            counts2[c] += 1

        for c in counts1 : 
            if counts1[c] != counts2[c] :
                return False

        return True