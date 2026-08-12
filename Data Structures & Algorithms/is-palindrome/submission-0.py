class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = list(s)
        sanitized = list()
        valid_chars = [chr(i) for i in range(65,91)] + [chr(i) for i in range(48,58)]

        for mychar in s:
            if mychar.upper() in valid_chars :
                sanitized.append(mychar.upper())


        for i in range(0, int(len(sanitized)/2)) : 
            opposite_index = len(sanitized)-i-1
            if sanitized[i] != sanitized[opposite_index] :
                return False

        return True