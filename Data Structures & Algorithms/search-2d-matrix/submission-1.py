class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        N = m * n
        s = 0
        e = N - 1

        def _get(z):
            i = z // n
            j = z % n
            return matrix[i][j]

        while s <= e:
            mid = (s + e) // 2
            midval = _get(mid)
            if midval == target:
                return True

            if midval > target:
                e = mid - 1

            else:
                s = mid + 1
        return False
