class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for n in nums:
            if n in dic.keys():
                return True
            dic[n] = 1 + dic.get(n, 0)
        return False