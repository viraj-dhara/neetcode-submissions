class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        s = 1
        l = len(nums) - 1

        if nums[0] == target : return 0

        while s <= l :
            mid = l//s
            if nums[mid] == target : return mid
            elif nums[mid] < target : s = mid + 1
            else : l = mid - 1

        return -1