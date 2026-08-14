class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = list()
        curr_candidates = []
        
        def dfs(index, curr_candidates, curr_sum ) :
            
            if curr_sum == target : 
                results.append(curr_candidates[:])
                return
            elif curr_sum > target : return
            elif index > len(candidates) - 1 : return
            else :
                curr_candidates.append(candidates[index])
                dfs( index, curr_candidates, curr_sum + candidates[index])
                curr_candidates.pop()
                dfs( index + 1, curr_candidates, curr_sum)

        dfs(0, curr_candidates, 0)

        return results