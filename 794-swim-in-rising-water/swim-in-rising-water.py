class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        visit.add((0, 0))
        DIR = [[0,1],(0,-1),(1,0),(-1,0)]

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in DIR:
                nr, nc = r + dr, c + dc
                if  nr < 0 or nc < 0 or nr == N or nc == N or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])