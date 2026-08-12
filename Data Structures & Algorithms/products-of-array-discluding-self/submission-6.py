class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [0] * len(nums)
        flag, zeroIndex = 0, -1
        total = 1

        for i in range(len(nums)) :
            if nums[i] != 0 :
                total *= nums[i]
            elif flag == 1 :
                return output
            else :
                flag = 1
                zeroIndex = i

        if flag == 1 : 
            output[zeroIndex] = total
            return output

        for i in range(len(nums)) :
            output[i] = total//nums[i]

        return output