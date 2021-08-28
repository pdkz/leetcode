class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]
        L = len(intervals)
        
        for i in range(1, L):
            start, end = intervals[i]
            
            last_start = merged_intervals[-1][0]
            last_end = merged_intervals[-1][1]
        
            if start >= last_start and start <= last_end:
                if end > last_end:
                    merged_intervals.pop()
                    merged_intervals.append([last_start, end])
                else:
                    continue
            else:
                merged_intervals.append(intervals[i])
    
        return merged_intervals