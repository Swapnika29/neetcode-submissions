class Solution:
    def isValid(self, s: str) -> bool:
        prevstack = []
        prevmap = {"}":"{","]":"[",")":"("}
        for i in s:
            if i in prevmap and len(prevstack)!=0:
                if prevstack[-1] == prevmap[i]:
                    prevstack.pop()
                else:
                    return False
            elif i in prevmap and len(prevstack) == 0:
                return False
            else:
                prevstack.append(i)
        if len(prevstack) == 0:
            return True
        else:
            return False 
            