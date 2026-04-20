class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        stack.append([-1,-1])
        maxarea = 0
        for i,h in enumerate(heights):
            while stack[-1][0] != -1 and h < stack[-1][0]:
                height = stack[-1][0]
                stack.pop()
                width = i - stack[-1][1] - 1
                area = height * width
                maxarea = max(maxarea, area)
            stack.append([h,i])
        while stack[-1][0]!=-1:
            height = stack[-1][0]
            stack.pop()
            width = len(heights) - stack[-1][1] - 1
            area = height * width
            maxarea = max(maxarea, area)
        return maxarea