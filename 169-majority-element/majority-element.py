class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]
        count = 0
        res = 0
        for n in nums:
            if count == 0:
                res = n
            if res == n:
                count += 1
            else:
                count -= 1
        return res