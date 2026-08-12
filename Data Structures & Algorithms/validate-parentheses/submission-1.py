class Solution:
    def isValid(self, s: str) -> bool:
        
        myqueue = list()
        my_brackets = {'(':')', '{':'}', '[':']'}

        for mychar in list(s) :
            if mychar in my_brackets :
                myqueue.append(mychar)
            else :
                if len(myqueue) == 0 : return False
                if my_brackets[myqueue[-1:][0]] == mychar :
                    myqueue.pop()
                else :
                    return False
            
        if len(myqueue) != 0 : return False

        return True
