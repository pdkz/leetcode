class MyCalendar:
    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        if len(self.cal) == 0:
            self.cal.append([start, end])
            return True
        
        for s, e in self.cal:
            if (start < s and end <= s) or (e <= start and e <= end):
                continue
            else:
                return False
                
        self.cal.append([start, end])
        
        return True
