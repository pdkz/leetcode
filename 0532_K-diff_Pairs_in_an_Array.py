class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hn = collections.Counter(nums)
        ht = collections.defaultdict(int)
        
        for n in nums:
            if k >= 0: 
                m = n + k
            else: 
                m = k - n

            if (n != m and hn[m] > 0) or (n == m and hn[m] > 1):
                if ht.get(m) != n and ht.get(n) != m:
                    hn[m] -= 1
                    ht[n] = m
                    
        return len(ht)
