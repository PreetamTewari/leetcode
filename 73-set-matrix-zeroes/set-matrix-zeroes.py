class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(mat), len(mat[0])
        rT, cT = [0] * ROWS, [0] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    rT[i] = 1
                    cT[j] = 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if rT[i] == 1:
                    mat[i][j] = 0
                if cT[j] == 1:
                    mat[i][j] = 0
                    