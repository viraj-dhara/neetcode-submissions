class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def my_function(result, nums, curr_subset, indice) :
            
            if indice >= len(nums) : 
                result.append(curr_subset[:])
                return

            curr_subset.append(nums[indice])
            my_function(result, nums, curr_subset, indice + 1)
            curr_subset.pop(-1)
            my_function(result, nums, curr_subset, indice + 1)

        my_function(result, nums, [], 0)

        return result

            