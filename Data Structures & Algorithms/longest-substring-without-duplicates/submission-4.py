class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        output = int()
        output = 0

        s = list(s)
        print(s)

        counter = 0
        charachterRecord = list()

        for i, mystart in enumerate(s) :
            counter = 0
            charachterRecord = list()
            for mychar in s[i:] :
                if mychar in charachterRecord : 
                    break
                else : 
                    charachterRecord.append(mychar)
                    counter += 1
            if counter > output : 
                output = counter

        return output
                