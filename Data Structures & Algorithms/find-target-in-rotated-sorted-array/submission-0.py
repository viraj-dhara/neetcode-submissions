class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1 :
            if nums[0] == target : return 0
            else : return -1

        first = 0
        last = len(nums) - 1

        k = 0

        while (first < last) :
            mid = (first + last) // 2

            if nums[first] > nums[mid] :
                last = mid
            elif nums[mid] > nums[last] :
                first = mid + 1
            else :
                break
        
        if first != 0 : 
            if first != last :
                k = first - 1
            else :
                k = first

        print(k)        

        first = 0
        last = len(nums) - 1

        if k != 0 : unrotated = [nums[(i - k) % len(nums)] for i in range(len(nums))]
        else : unrotated = nums
        print(unrotated)

        ## simple linear search:
        
        index = -1

        for i in range(len(nums)) : 
            if unrotated[i] == target :
                index = (i - k) % len(nums)
                break

        return index