class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)) :
            if curr_sum < 0 and nums[i] > curr_sum : # reset window
                curr_sum = nums[i]
                max_sum = max(max_sum, curr_sum)
            elif curr_sum < 0 : # continue window, sum decreases
                curr_sum += nums[i]
            else : # continue window, sum may increase or decrease
                curr_sum += nums[i]
                max_sum = max(max_sum, curr_sum)

        return max_sum

        return max_sum