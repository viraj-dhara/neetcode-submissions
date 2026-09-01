class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def dfs(index, curr) :

            nonlocal result
            nonlocal nums

            if index == len(nums) :
                result.append(curr[:])
                return
            
            for i in range(len(curr) + 1) :
                curr.insert(i, nums[index])
                dfs(index+1, curr)
                curr.pop(i)

        dfs(0, list())

        return result