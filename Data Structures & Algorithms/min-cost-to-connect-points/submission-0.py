class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst = set([0])
        dct = defaultdict(lambda: None)
        n = len(points)

        def _dist(i, j):
            p1, p2 = points[i], points[j]
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def _argmin():
            _min_idx, _min_dist = -1, float("inf")
            for i in range(n):
                if i in mst: 
                    continue
                    
                for j in mst:
                    dct[(i,j)] = dct[(i,j)] or _dist(i, j)
                    _min_dist = min(dct[(i,j)], _min_dist)
                    _min_idx = i if _min_dist == dct[(i,j)] else _min_idx

            return _min_idx, _min_dist
            
        _d = 0
        for _ in range(n-1):
            _min_idx, _min_dist = _argmin()
            mst.add(_min_idx)
            _d += _min_dist
            # print(f"adding {_min_idx}: {points[_min_idx]} at distance={_min_dist}")
            # print(_min_idx, _min_dist, _d, mst)

        # print(dct)
        return _d