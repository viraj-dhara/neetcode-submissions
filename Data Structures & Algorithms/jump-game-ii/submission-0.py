class Solution:
    def jump(self, nums: list[int]) -> int:
        
        n = len(nums)
        r = (l := 0)
        min_steps = 0

        while r < n - 1 :
            
            max_reach = r
            for j in range(l, r + 1) :
                if j + nums[j] > max_reach : 
                    max_reach = j + nums[j]

            l = r + 1
            r = max_reach

            min_steps += 1

        return min_steps

