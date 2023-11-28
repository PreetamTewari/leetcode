class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def back(i, cur, total):
            if total > target or i >= len(candidates):
                return
            if total == target:
                res.append(cur[::])
                return
            cur.append(candidates[i])
            back(i, cur, total+candidates[i])
            cur.pop()
            back(i+1, cur, total)

        back(0, [], 0)
        return res