class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = list()
        already_taken = set()
        counts = [{chr(i): 0 for i in range(65, 91)} for _ in range(len(strs))]

        # make anagram signature
        for i, mystr in enumerate(strs) :
            for mychar in list(mystr.upper()):
                counts[i][mychar] += 1

        for i, mystr1 in enumerate(strs) :

            if i in already_taken : continue
            temp_output = [mystr1]

            for j, mystr2 in enumerate(strs) :

                if j in already_taken : continue
                if counts[i] == counts[j] and i != j :
                    already_taken.add(i)
                    already_taken.add(j)
                    temp_output.append(mystr2)
            
            output.append(temp_output)

        return output

                    