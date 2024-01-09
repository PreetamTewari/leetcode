class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) > len(set(nums))
        dic = {}
        for n in nums:
            if n in dic:
                return True
            dic[n] = n
        return False