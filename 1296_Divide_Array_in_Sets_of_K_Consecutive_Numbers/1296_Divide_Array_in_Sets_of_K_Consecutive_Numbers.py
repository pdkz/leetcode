class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = collections.Counter(nums)
        nums = sorted(nums)
        
        for n in nums:
            if not counter.get(n):
                continue
            
            counter[n] -= 1
            
            for i in range(1, k):
                if counter.get(n+i):
                    counter[n+i] -= 1
                else:
                    return False
        return True
