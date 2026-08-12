class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # nums.append(0)
        mymoney = [0] * len(nums)

        for i in range(len(nums)) :
            if i == 0 or i == 1 : mymoney[i] = nums[i]
            else :
                mymoney[i] = max(mymoney[i-2], mymoney[i-3]) + nums[i]

        print(mymoney)
        return max(mymoney[len(nums) - 1], mymoney[len(nums) - 2])