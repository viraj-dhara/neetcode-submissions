class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        first = 0
        last = len(nums) - 1


        while (first < last) :
            mid = (first + last) // 2

            if nums[first] > nums[mid] :
                last = mid
            elif nums[mid] > nums[last] :
                first = mid + 1
            else :
                return nums[first]

        return nums[first]

        