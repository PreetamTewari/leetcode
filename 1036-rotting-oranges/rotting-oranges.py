class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return -1

        fresh = 0
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        DIR = [(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIR:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1
        return time if fresh == 0 else -1
