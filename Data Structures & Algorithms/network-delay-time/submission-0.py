class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]
        heapify(heap)

        _times = defaultdict(list)
        for time in times:
            _times[time[0]].append((time[1], time[2]))
        times = _times

        visited = [math.inf for i in range(n + 1)]
        visited[k] = 0

        while heap:
            time, node = heapq.heappop(heap)
            if time != visited[node]:
                continue

            for (child, traverse_time) in times[node]:
                t = time + traverse_time

                if visited[child] <= t:
                    continue
                else:
                    visited[child] = t
                    heapq.heappush(heap, (t, child))

        _max = max(visited[1:])

        if _max is math.inf:
            return -1

        return _max
