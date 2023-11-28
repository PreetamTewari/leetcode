class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(h), len(h[0])
        pac, atl = set(), set()

        

        def dfs(r, c, visit, prev):
            if r < 0 or c < 0 or (r, c) in visit or r == ROWS or c == COLS or h[r][c] < prev:
                return False

            visit.add((r, c))
            dfs(r+1, c, visit, h[r][c])
            dfs(r-1, c, visit, h[r][c])
            dfs(r, c+1, visit, h[r][c])
            dfs(r, c-1, visit, h[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, h[r][0])
            dfs(r, COLS - 1, atl, h[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pac, h[0][c])
            dfs(ROWS - 1, c, atl, h[ROWS - 1][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res