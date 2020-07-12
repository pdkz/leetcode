class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        l = len(sorted_intervals)
        
        for i in range(0, l-1):
            s_i, e_i = sorted_intervals[i]
            s_j, e_j = sorted_intervals[i+1]
            if e_i > s_j:
                return False
        return True
