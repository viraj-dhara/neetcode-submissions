class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()

        triplets = set()

        k = 0

        while k <= len(nums) - 3 :
            
            front = k+1
            back = len(nums) - 1

            while front < back :
                if nums[front] + nums[back] < - nums[k] :
                    front += 1
                elif nums[front] + nums[back] > - nums[k] :
                    back -= 1
                else :
                    triplets.add(tuple([nums[k], nums[front], nums[back]]))
                    back -= 1

            k += 1


        return [list(i) for i in triplets]