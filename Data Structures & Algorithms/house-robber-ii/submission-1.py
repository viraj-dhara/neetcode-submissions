class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) in [0,1] : 
            return 0 if len(nums) == 0 else nums[0]
        
        # either first and second last, or second and last

        # if we rob first one, we remove last one from array and solve like house robber 1

        nums_a = nums[:-1]
        mymoney = [0] * len(nums_a)

        for i in range(len(nums_a)) :
            if i == 0 or i == 1 : mymoney[i] = nums_a[i]
            else :
                mymoney[i] = max(mymoney[i-2], mymoney[i-3]) + nums_a[i]

        possibility_a = max(mymoney[len(nums_a) - 1], mymoney[len(nums_a) - 2])

        # if we rob second one, we *may* rob right untill the last one, so remove first and solve as before.

        nums_b = nums[1:]
        mymoney = [0] * len(nums_b)

        for i in range(len(nums_b)) :
            if i == 0 or i == 1 : mymoney[i] = nums_b[i]
            else :
                mymoney[i] = max(mymoney[i-2], mymoney[i-3]) + nums_b[i]

        possibility_b = max(mymoney[len(nums_b) - 1], mymoney[len(nums_b) - 2])

        return max(possibility_a, possibility_b)