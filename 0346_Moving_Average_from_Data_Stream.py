class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.size = size
        self.p = 0

    def next(self, val: int) -> float:
        self.data.append(val)
        data_len = len(self.data)
        if data_len > self.size:
            self.p += 1
            size = self.size
        else:
            size = data_len
            
        return sum(self.data[self.p:]) / size
