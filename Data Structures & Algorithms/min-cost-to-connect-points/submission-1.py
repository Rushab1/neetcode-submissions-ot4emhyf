class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst = set([0])
        n = len(points)

        def _dist(i, j):
            p1, p2 = points[i], points[j]
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        dct = [[(_dist(i, j), j) for j in range(n)] for i in range(n)]

        for i in range(n):
            heapq.heapify(dct[i])


        def _argmin():
            _min_dist = float("inf")
            _min_idx = None
            for i in mst:
                # print(f"finding {dct[i][0][1]} at dist {dct[i][0][0]}")
                while dct[i][0][1] in mst:
                    heapq.heappop(dct[i])
                
                if dct[i][0][0] < _min_dist:
                    _min_dist, _min_idx = dct[i][0][0], i
            
            return heapq.heappop(dct[_min_idx])
            
        _d = 0
        for _ in range(n-1):
            _min_dist, _min_idx = _argmin()
            mst.add(_min_idx)
            _d += _min_dist
            # print(f"adding {_min_idx}: {points[_min_idx]} at distance={_min_dist}")
            # print(_min_idx, _min_dist, _d, mst)

        # print(dct)
        return _d