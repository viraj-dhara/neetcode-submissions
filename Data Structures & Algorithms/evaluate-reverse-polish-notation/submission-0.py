class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        workingStack = list()

        for mystring in tokens :
            if mystring == "+" :
                workingStack.append(workingStack.pop() + workingStack.pop())
            elif mystring == "*" :
                workingStack.append(workingStack.pop() * workingStack.pop())
            elif mystring == "-" :
                workingStack.append(- workingStack.pop() + workingStack.pop())
            elif mystring == "/" :
                divisor = workingStack.pop()
                dividend = workingStack.pop()
                workingStack.append(int(dividend/divisor))
            else :
                workingStack.append(int(mystring))

        return workingStack.pop()