class Solution:
    def canFinish(self, numCou: int, prereq: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCou)}
        for pre, crs in prereq:
            adj[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if adj[crs] == []:
                return True
            visit.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False

            adj[crs] = []
            visit.remove(crs)
            return True

        for crs in range(numCou):
            if not dfs(crs):
                return False
        return True