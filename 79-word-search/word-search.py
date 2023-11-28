class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or board[r][c] != word[i]:
                return False
            visit.add((r, c))
            res = dfs(r+1, c, i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            if res:
                return True
            visit.remove((r,c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False