class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(mat), len(mat[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    mat[0][c] = 0
                    if r > 0:
                        mat[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if mat[r][0] == 0 or mat[0][c] == 0:
                    mat[r][c] = 0
        
        if mat[0][0] == 0:
            for r in range(ROWS):
                mat[r][0] = 0
        
        if rowZero:
            for c in range(COLS):
                mat[0][c] = 0



        # rT, cT = [0] * ROWS, [0] * COLS

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if mat[i][j] == 0:
        #             rT[i] = 1
        #             cT[j] = 1
        
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if rT[i] == 1:
        #             mat[i][j] = 0
        #         if cT[j] == 1:
        #             mat[i][j] = 0
