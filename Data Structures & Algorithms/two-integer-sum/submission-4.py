class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in hash:
                return [hash[diff],i]
            else:
                hash[nums[i]] = i
            
        