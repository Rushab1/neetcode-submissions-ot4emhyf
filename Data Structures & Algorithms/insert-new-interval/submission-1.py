class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]
            
        n = len(intervals)
        ns, ne = newInterval

        if ne < intervals[0][0]:
            return [newInterval] + intervals

        if intervals[-1][1] < ns:
            return intervals + [newInterval]

        def is_overlapping(interval1, interval2):
            s, e = interval1
            ns, ne = interval2
            if ns <= s <= ne or s <= ns <= e:
                return True
            return False

        ret = []
        merge_stream = False
        for i, interval in enumerate(intervals):
            s, e = interval
            if merge_stream and is_overlapping(interval, ret[-1]):
                    ret[-1] = (min(s, ret[-1][0]), max(e, ret[-1][1]))

            elif is_overlapping(interval, newInterval):
                    merge_stream = True
                    ret.append((min(s, ns), max(e, ne)))

            else:
                merge_stream = False
                ret.append(interval)
                
                if e <= ns and (i == n-1 or ne < intervals[i+1][0]):
                    ret.append(newInterval)
        return ret

