class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""
        for i in strs:
            temp += str(len(i)) + "#" + i
        return temp
       

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        numstr = ""
        while i < len(s):
            if s[i] != "#":
                numstr +=  s[i]
                i+=1
            if s[i] == "#":
                length = int(numstr)
                numstr = ""
                i+=1
                word = s[i:(i+length)]
                result.append(word)
                i+=length
                length = 0
        return result
       


