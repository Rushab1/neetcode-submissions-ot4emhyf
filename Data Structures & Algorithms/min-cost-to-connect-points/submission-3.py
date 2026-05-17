class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst = set()
        n = len(points)

        def _dist(i, j):
            p1, p2 = points[i], points[j]
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        min_arr = {i: float("inf") for i in range(n)}
        min_arr[0] = 0

        dist = 0
        for i in range(n):
            # find minimum from current mst
            j = min(min_arr, key= min_arr.get)

            # add and update min_arr
            mst.add(j)
            dist += min_arr[j]

            min_arr = {k: min(min_arr[k], _dist(j, k)) for k in min_arr}
            del min_arr[j]


        return dist