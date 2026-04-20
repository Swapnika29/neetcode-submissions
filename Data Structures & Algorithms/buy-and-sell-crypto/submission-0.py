class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       buy = prices[0]
       cp = 0
       profit = 0
       for i in prices:
            cp = i
            if buy > i:
                buy = i
            profit = max(profit, cp - buy)
       return profit

    


        