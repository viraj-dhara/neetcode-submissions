class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        if not (n := len(nums)) : return 0

        maxSum = nums[0]
        minSum = nums[0]

        result = nums[0]

        for num in nums[1:] :

            temp = maxSum

            maxSum = max(num, maxSum * num, minSum * num)
            minSum = min(num, minSum * num, temp * num)

            result = max(result, maxSum)

        return result

