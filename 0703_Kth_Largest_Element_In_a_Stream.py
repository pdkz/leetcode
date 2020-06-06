class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        sorted_nums = sorted(nums, reverse=True)
        self.top = sorted_nums[0:k]

    def add(self, val: int) -> int:
        if len(self.top) < self.k or (val > self.top[-1] and val < self.top[0]):
            self.top.append(val)
            self.top = sorted(self.top, reverse=True)
        elif val >= self.top[0]:
            self.top.insert(0, val)

        return self.top[self.k-1]