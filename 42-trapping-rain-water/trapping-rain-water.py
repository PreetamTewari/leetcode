class Solution:
    def trap(self, h: List[int]) -> int:
        l, r = 0, len(h) - 1
        lM, rM = h[l], h[r]
        res = 0

        while l < r:
            if lM < rM:
                l += 1
                lM = max(lM, h[l])
                res += lM - h[l]
            else:
                r -= 1
                rM = max(rM, h[r])
                res += rM - h[r]
        return res