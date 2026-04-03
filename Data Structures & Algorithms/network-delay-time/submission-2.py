class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]
        heapify(heap)

        graph = {i: [] for i in range(n + 1)}
        for (u, v, t) in times:
            graph[u].append((v, t))

        visited = set()
        lv = 0

        while heap:
            # first time you pop a node is guranteed to be shortest path
            time, node = heapq.heappop(heap)
            visited.add(node)
            lv += 1

            if lv == n:
                return time

            for (child, traverse_time) in graph[node]:
                t = time + traverse_time

                if child not in visited:
                    heapq.heappush(heap, (t, child))

        return -1
