class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""
        for i in strs:
            temp = temp + str(len(i)) + "#" + i
        return temp

            

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        length = ""
        while i < len(s):
            while s[i] != "#":
                length = length + s[i]
                i += 1
            i += 1
            length = int(length)
            result.append(s[i : (i+length)])
            i= i + length
            length = ""
        return result



