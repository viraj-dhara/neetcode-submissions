class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        memoization = defaultdict(list)
        

        def dfs(index) -> bool :

            if index >= len(s) : return True

            if memoization[index] == -1 : return False
            if memoization[index] == [] :

                for word in wordDict :

                    if len(word) > len(s) - index : continue

                    i = index
                    for letter in word :
                        if letter != s[i]: 
                            break
                        i += 1
                    
                    if i == index + len(word) : 
                        memoization[index].append(word)

            for word in memoization[index] :
                    if dfs(index + len(word)) : return True

            memoization[index] = -1

            return False

        return dfs(0)