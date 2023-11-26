class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxA = 0
        l, r = 0, len(h) - 1
        while l < r:
            maxA = max(maxA, min(h[l], h[r]) * (r - l) )
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return maxA