class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        for i, n in enumerate(nums) :
            indices[n] = i

        for i, n in enumerate(nums) :
            more = target - n
            if more in indices and indices[more] != i:
                return [i, indices[more]]

        return []