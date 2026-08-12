class MinStack:

    def __init__(self):
        self.mystack = list()
        self.minstack = [2**31 -1]

    def push(self, val: int) -> None:
        self.mystack.append(val)

        if self.minstack[-1:][0] < val : 
            self.minstack.append(self.minstack[-1:][0])
        else :
            self.minstack.append(val)

    def pop(self) -> None:
        print(self.minstack)
        self.minstack.pop()
        self.mystack.pop()

    def top(self) -> int:
        return self.mystack[-1:][0]

    def getMin(self) -> int:
        return self.minstack[-1:][0]
