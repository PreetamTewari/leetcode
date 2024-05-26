class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0

        for r in range(len(prices)):
            maxP = max(maxP, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
        return maxP
        