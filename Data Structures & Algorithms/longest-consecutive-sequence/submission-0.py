class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums : return 0

        nums.sort()

        max_length = 1
        length = 0
        expected_element = nums[0]

        while nums :
            if nums[0] == expected_element :
                length += 1
                max_length = max(length, max_length)
                expected_element += 1
                nums.pop(0)
            elif nums[0] == expected_element - 1 :
                nums.pop(0)
            else :
                length = 1
                expected_element = nums.pop(0) + 1

        return max_length
