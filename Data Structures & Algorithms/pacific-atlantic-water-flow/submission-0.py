class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        if m == 1 or n == 1:
            return [(i,j) for i in range(m) for j in range(n)]

        qp = deque([(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)])
        qa = deque([(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n - 1)])

        vp = set(qp)
        va = set(qa)

        def bfs (q: deque, v: set):
            while q:
                node = q.popleft()
                i, j = node

                children = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                children = [(ii, jj) for ii, jj in children 
                            if ii >= 0 and ii < m 
                            and jj >= 0 and jj < n 
                            and heights[i][j] <= heights[ii][jj]]

                for child in children:
                    if child not in v:
                        q.append(child)
                        v.add(child)

        bfs(qa, va)
        bfs(qp, vp)

        ret = [node for node in vp if node in va]
        return ret
