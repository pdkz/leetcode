class MyCalendar:
    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        if len(self.cal) == 0:
            self.cal.append([start, end])
            return True
        
        for s, e in self.cal:
            if s < end and start < e:
                return False
                
        self.cal.append([start, end])
        return True
