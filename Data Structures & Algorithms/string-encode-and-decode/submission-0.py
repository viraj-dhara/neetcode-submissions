class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""
        temp_list = list()

        for mystr in strs :
            temp_list.append(mystr)
            temp_list.append(chr(257))
        
        output = "".join(temp_list)

        return output


    def decode(self, s: str) -> List[str]:
        
        output = list()
        temp_string = list()

        for mychar in s : 
            if mychar != chr(257) :
                temp_string.append(mychar)
            else :
                output.append("".join(temp_string))
                temp_string = list()

        return output
