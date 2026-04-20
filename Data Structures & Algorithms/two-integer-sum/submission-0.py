class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        firstmap = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in firstmap:
                return [firstmap[diff],i]
            firstmap[nums[i]] = i
        return []
        