class Solution:
    def canJump(self, nums: list[int]) -> bool:
        

        max_reach = 0

        for i in range(len(nums)) :

            if max_reach >= len(nums) - 1 : return True

            if max_reach <  i : return False

            if i + nums[i] > max_reach :
                max_reach = i + nums[i]
