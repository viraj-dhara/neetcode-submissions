class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = list()

        def dfs(index, curr) :

            nonlocal nums
            nonlocal result

            if index == len(nums) :
                result.append(sorted(curr[:]))
                return
            
            curr.append(nums[index])
            dfs(index+1, curr)
            curr.pop(-1)
            dfs(index+1, curr)

        dfs(0, [])

        new = set()
        for item in result :
            new.add(tuple(item))
        

        return list(new)
