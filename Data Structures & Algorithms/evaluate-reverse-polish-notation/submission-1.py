class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mainstack = []
        val = 0
        for i in tokens:
            if i == "+":
                b = mainstack.pop()
                a = mainstack.pop()
                val = a + b
                mainstack.append(val)
            elif i == "-":
                b = mainstack.pop()
                a = mainstack.pop()
                val = a - b
                mainstack.append(val)
            elif i == "*":
                b = mainstack.pop()
                a = mainstack.pop()
                val = a * b
                mainstack.append(val)
            elif i == "/":
                b = mainstack.pop()
                a = mainstack.pop()
                val = int(a / b)
                mainstack.append(val)
            else:
                mainstack.append(int(i))
        return mainstack[-1]
        