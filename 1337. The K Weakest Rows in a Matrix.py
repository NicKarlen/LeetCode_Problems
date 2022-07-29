class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        matrix = []
        for idx, li in enumerate(mat):
            li.append(idx)
            matrix.append(li)

        matrix = sorted(matrix)
        res = []
        for idx, li in enumerate(matrix):
            res.append(li[-1])
            if idx+1 >= k:
                print(res)
                return res


sol = Solution()

sol.kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2)