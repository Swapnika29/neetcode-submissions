class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        l=[[] for i in range(len(nums)+1)]
        res=[]
        length = 0
        for i in result:
            v = result[i]
            l[v].append(i)
        for i in range(len(l) - 1, 0, -1):
            for num in l[i]:
                res.append(num)
                if len(res) == k:
                    return res



        