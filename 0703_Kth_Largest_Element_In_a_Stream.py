class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k = sorted(nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        if len(self.top_k) == self.k and val <= self.top_k[-1]:
            return self.top_k[-1]
        
        left = -1
        right = len(self.top_k) 

        while (right - left) > 1:
            mid = (left + right) // 2
            #print(left, right, mid)
            if self.top_k[mid] >= val:
                left = mid
            else:
                right = mid
                
        self.top_k.insert(right, val)
        if len(self.top_k) > self.k:
            self.top_k.pop()

        return self.top_k[-1]