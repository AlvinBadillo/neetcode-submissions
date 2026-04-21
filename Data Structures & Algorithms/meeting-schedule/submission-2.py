"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # If there is only one item in the list we can always return true
        if len(intervals) == 1:
            return True
        for i in range(len(intervals) - 1):
            if intervals[i].start == intervals[i + 1].start:
                return False
            # Check if start of current is smaller than the start of the next one
            elif intervals[i].start < intervals[i + 1].start:
                # Check if end if current is smaller than start of next, if it isnt, return false
                if intervals[i].end > intervals[i+1].start:
                    return False
            else:
                if intervals[i].end < intervals[i+1].start:
                    return False
        return True