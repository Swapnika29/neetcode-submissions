class MinStack:

    def __init__(self):
        self.mainstack = []
        self.minimumstack = []
        

    def push(self, val: int) -> None:
        self.mainstack.append(val)
        if len(self.minimumstack) == 0:
            self.minimumstack.append(val)
        else:
            val = min(val,self.minimumstack[-1])
            self.minimumstack.append(val)
        

    def pop(self) -> None:
        self.mainstack.pop()
        self.minimumstack.pop()
        

    def top(self) -> int:
        return self.mainstack[-1]
        

    def getMin(self) -> int:
        return self.minimumstack[-1]
        
