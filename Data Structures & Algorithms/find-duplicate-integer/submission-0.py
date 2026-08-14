class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 0

        while True :

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast :

                slow_old = slow
                slow = 0
                while True :
                    slow = nums[slow]
                    slow_old = nums[slow_old]

                    if slow == slow_old : 
                        break

                break
        
        return slow_old
        