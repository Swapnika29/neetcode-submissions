class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generateparen(openn,closen,string=""):
            if closen == openn == n:
                result.append(string)
                return
            if openn < n:
                generateparen(openn+1,closen,string+"(")
            if closen < openn:
                generateparen(openn, closen+1,string+")")
        generateparen(0,0,string="")
        return result
