class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = -1

        while True :
            
            print(i)
            if digits[i] < 9 :
                digits[i] += 1
                return digits
            else :
                digits[i] = 0
                i -= 1
                if abs(i) > len(digits):
                    return [1] + digits
                