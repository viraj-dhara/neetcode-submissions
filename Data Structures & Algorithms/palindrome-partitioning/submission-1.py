import copy

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_pallindrome(snippet) -> bool :

            if not snippet : return True

            if len(snippet) % 2 == 0 :
                for i in range(len(snippet) // 2) :
                    if snippet[i] != snippet[ - i - 1] :
                        return False
            else :
                for i in range(len(snippet) // 2 + 1) :
                    if snippet[i] != snippet[ - i - 1] :
                        return False
            
            return True


        def dfs(index, curr_partitions) :

            nonlocal s
            nonlocal results

            if index >= len(s) :
                if is_pallindrome(curr_partitions[-1]) :
                    results.append(copy.deepcopy(curr_partitions))
                return


            curr_partitions[-1].append(s[index])
            dfs(index + 1, curr_partitions)
            curr_partitions[-1].pop()

            if not curr_partitions[-1] or not is_pallindrome(curr_partitions[-1]) :
                return

            curr_partitions.append([])
            dfs(index, curr_partitions)
            curr_partitions.pop()

        results = list()

        dfs(0, [[]])

        return list(map(lambda mylist : ["".join(element) for element in mylist], results))