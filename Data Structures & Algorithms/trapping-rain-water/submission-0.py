class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxleft = height[left]
        maxright = height[right]
        result = []
        while left < right:
            if maxleft < maxright:
                left+=1
                store = min(maxleft,maxright) - height[left]
                if store > 0 :
                    result.append(store)
                maxleft = max(maxleft,height[left])
            elif maxleft == maxright:
                left+=1
                store = min(maxleft,maxright) - height[left]
                if store > 0:
                    result.append(store)
                maxleft = max(maxleft,height[left])
            else:
                right -=1
                store = min(maxleft,maxright) - height[right]
                if store > 0:
                    result.append(store)
                maxright = max(maxright,height[right])
        return sum(result)
            

        