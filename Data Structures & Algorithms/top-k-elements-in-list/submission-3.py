class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        l=[]
        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        result = dict(sorted(result.items(),key = lambda x:x[1],reverse = True))
        x = list(result.keys())
        for j in range(0,k):
            l.append(x[j])  
        return l
        