class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        lM, rM = height[l], height[r]
        res = 0

        while l < r:
            if lM < rM:
                l += 1
                lM = max(lM, height[l])
                res += lM - height[l]
            else:
                r -= 1
                rM = max(rM, height[r])
                res += rM - height[r]
        return res