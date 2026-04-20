class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstmap={}
        secondmap={}
        l = 1
        if len(s) == len(t):
            for i in s:
                if i not in firstmap:
                    firstmap[i] = l
                if i in firstmap:
                    firstmap[i] += 1 
            for j in t:
                if j not in secondmap:
                    secondmap[j] = l
                if j in secondmap:
                    secondmap[j] += 1                       
            if firstmap == secondmap:
                return True
            return False
        return False
            
        