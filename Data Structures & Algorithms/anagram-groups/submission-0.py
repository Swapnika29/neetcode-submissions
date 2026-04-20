class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            temp = "".join(sorted(i))
            if temp not in result:
                result[temp] = [i]
            else:
                result[temp].append(i)
        return result.values()

        