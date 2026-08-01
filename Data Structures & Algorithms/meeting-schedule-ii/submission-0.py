"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        dct = defaultdict(int)
        
        for i in intervals:
            dct[i.start] += 1
            dct[i.end] -= 1

        rooms = 0
        min_rooms = 0
        for k in sorted(dct.keys()):
            rooms += dct[k]
            min_rooms = max(min_rooms, rooms)
        
        return min_rooms