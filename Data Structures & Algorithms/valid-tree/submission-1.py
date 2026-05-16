class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        egdes = [(u,v) for (u,v) in edges if u!=v]
        if n == 1:
            return True

        if not edges:
            return False

        if len(edges) != n-1:
            return False

        dct = defaultdict(set)
        for (u, v) in edges:
            dct[u].add(v)
            dct[v].add(u)

        visited = set()
        def bfs(root):
            q = deque([root])

            while q:
                node = q.popleft()
                visited.add(node)
                children = dct[node]

                for child in children:
                    if child in visited:
                        continue
                        
                    visited.add(child)
                    q.append(child)

            return True

        return bfs(0) and len(visited) == n

                