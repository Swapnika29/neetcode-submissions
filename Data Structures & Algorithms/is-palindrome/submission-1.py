class Solution:
    def isPalindrome(self, s: str) -> bool:
        combineds = "".join(i for i in s if i.isalnum())
        combineds = combineds.lower()
        left = 0
        right = len(combineds) - 1
        while left < right:
            if combineds[left] != combineds[right]:
                return False
            else:
                left+=1
                right-=1
        return True
        