class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0]) # sort by start_i

        def merge(i1, i2):
            s1, e1 = i1
            s2, e2 = i2
            if s2 <= s1 <= e2 or s1 <= s2 <= e1:
                return [min(s1,s2), max(e1, e2)]
            return None

        ret = [intervals[0]]
        n = len(intervals)
        for i in range(1, n):
            new = merge(intervals[i], ret[-1])

            if new is not None:
                ret[-1] = new
            else:
                ret.append(intervals[i])
        return ret
