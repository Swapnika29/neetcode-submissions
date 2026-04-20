class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result =[]
        nums.sort()
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                target = -(nums[i])
                if nums[left] + nums[right] > target:
                    right-=1
                elif nums[left] + nums[right] < target:
                    left+=1
                elif nums[left] + nums[right] == target:
                    result.append([nums[left],nums[right],nums[i]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
        return result
        