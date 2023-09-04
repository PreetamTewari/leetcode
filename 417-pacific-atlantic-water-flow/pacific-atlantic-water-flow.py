class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(h), len(h[0])

        def dfs(r, c, visit,prevH):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or h[r][c] < prevH:
                return
            visit.add((r, c))
            dfs(r+1, c, visit, h[r][c])
            dfs(r-1, c, visit, h[r][c])
            dfs(r, c+1, visit, h[r][c])
            dfs(r, c-1, visit, h[r][c])

        for c in range(COLS):
            dfs(0, c, pac, h[0][c])
            dfs(ROWS-1, c, atl, h[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, h[r][0])
            dfs(r, COLS - 1, atl, h[r][COLS - 1])

        out = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    out.append([r, c])
        return out