class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""
        for i in strs:
            temp += str(len(i)) + '#' + i
        return temp

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        nums = ""
        while i < len(s):
            if s[i] != '#':
                nums = nums + s[i]
                i+=1
            if s[i] == '#':
                length = int(nums)
                nums = ""
                i+=1
                result.append(s[i:(i+length)])
                i+=length
                length = 0
        return result

