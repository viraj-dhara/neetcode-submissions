class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = list()

        candidates.sort()
        print(candidates)

        def dfs(index, current, sum) :

            nonlocal result
            nonlocal target
            nonlocal candidates

            if sum == target : 
                result.append(current[:])
                return
            elif sum < target and index < len(candidates) :

                current.append(candidates[index])
                dfs(index + 1, current, sum + candidates[index])

                current.pop(-1)
                
                temp = candidates[index]
                index += 1
                while index < len(candidates) and candidates[index] == temp:
                    index += 1
                dfs(index, current, sum)

        dfs(0, [], 0)

        return result

