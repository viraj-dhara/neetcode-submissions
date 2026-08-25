class Solution:
    def reverseBits(self, n: int) -> int:
        
        negative = True if n < 0 else False
        n = abs(n)

        string = bin(n)
        print(string)

        string = string[2:]
        string = string[::-1]
        print(string)

        if len(string) < 31 :
            string += "".join(['0'] * (31 - len(string)))
        print(string)
        
        if negative : string = string + "1"
        else : string = string + "0"
        print(string)
        
        ans = int(string[:32], 2)

        return ans