class Solution:
    def combinationSum(self, can: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(can) or total > target:
                return

            cur.append(can[i])
            dfs(i, cur, total + can[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0,[],0)
        return res