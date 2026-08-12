class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        counts = dict()

        for i in nums:
            if i in counts :
                return True
            else :
                counts[i] = 1
        
        return False