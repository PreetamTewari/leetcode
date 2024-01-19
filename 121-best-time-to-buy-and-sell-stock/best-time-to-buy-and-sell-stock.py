class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        for r in range(len(prices)):
            maxP = max(maxP, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
        return maxP