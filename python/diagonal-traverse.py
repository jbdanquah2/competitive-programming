class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        if not mat:
            return []

        n, m = len(mat), len(mat[0])
        num_of_diagonal = n + m - 1
        res = [0] * (n * m)

        idx = 0

        for d in range(num_of_diagonal):
            for x in range(d + 1):
                row, col = x, d - x

                if d % 2 == 0:
                    row, col = col, row
                if row < n and col < m:
                    res[idx] = mat[row][col]
                    idx += 1
        return res
