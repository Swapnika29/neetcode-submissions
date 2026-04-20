class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combinedarray = [[x,y] for x,y in zip(position,speed)]
        stack = []
        combinedarray = sorted(combinedarray, reverse = True)
        for i in combinedarray:
            time = (target - i[0])/i[1]
            if len(stack)!=0 and stack[-1] < time:
                stack.append(time)
            elif len(stack) == 0 :
                stack.append(time)
        return len(stack) 
        