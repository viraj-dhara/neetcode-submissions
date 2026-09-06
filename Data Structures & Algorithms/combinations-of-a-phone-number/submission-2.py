class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits : return list()

        num_letters = {1: None, 2: "abc", 3:"def" ,4:"ghi" ,5:"jkl" ,6:"mno" ,7:"pqrs", 8:"tuv", 9:"wxyz", 0:" "}

        def dfs(index: int, curr_sequence: list) -> None :

            nonlocal digits
            nonlocal num_letters
            nonlocal results

            if index >= len(digits):
                results.append("".join(curr_sequence))
                return

            for char in num_letters[int(digits[index])] :
                curr_sequence.append(char)
                dfs(index + 1, curr_sequence)
                curr_sequence.pop()


        results = list()

        dfs(0, list())

        return results