class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = list()

        # the final string has to be exactly of 2 * n length
        def dfs(total, number_open, curr) :
            
            nonlocal n
            nonlocal result


            if total == n :
                if number_open == 0 :
                    result.append("".join(curr)) 
                else :
                    curr.append(")")
                    dfs(total, number_open - 1, curr)
                    curr.pop(-1)
                return 

            curr.append("(")
            dfs(total + 1, number_open + 1, curr)
            curr.pop(-1)
            
            if number_open > 0 :
                curr.append(")")
                dfs(total, number_open - 1, curr)
                curr.pop(-1)

        dfs(0, 0, [])
            
        return result
