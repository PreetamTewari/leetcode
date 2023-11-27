class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] != '1':
                return False

            visit.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return True

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands
