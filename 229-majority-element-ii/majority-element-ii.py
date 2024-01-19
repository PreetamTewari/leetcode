class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        for n in nums:
            dic[n] = 1 + dic.get(n, 0)
        res = []
        threshold = len(nums) // 3

        for k, v in dic.items():
            if v > threshold:
                res.append(k)
        return res