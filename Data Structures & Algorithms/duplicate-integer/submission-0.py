class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevmap={}
        for i in range(0,len(nums)):
            if nums[i] in prevmap:
                return True
            else:
                prevmap[nums[i]] = i
        return False
         