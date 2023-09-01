class Solution:
    def maxProfit(self, p: List[int]) -> int:
        maxPro = 0
        l = 0
        for r in range(len(p)):
            maxPro = max(maxPro, p[r] - p[l])
            if p[l] > p[r]:
                l = r
        
        return maxPro