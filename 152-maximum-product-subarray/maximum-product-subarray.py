class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cMin, cMax = 1, 1

        for n in nums:
            if n == 0:
                cMin, cMax = 1, 1
                continue
            
            tmp = cMax * n
            cMax = max(n*cMax, n*cMin, n)
            cMin = min(tmp, n*cMin, n)
            res = max(res, cMax)
        return res