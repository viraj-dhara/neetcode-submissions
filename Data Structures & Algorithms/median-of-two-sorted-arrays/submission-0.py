class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = nums1 + nums2

        nums.sort()

        half_length = len(nums) // 2

        if len(nums) % 2 == 0 :
            median = ( nums[half_length] + nums[half_length - 1] ) / 2
        else :
            median = nums[half_length]

        return median