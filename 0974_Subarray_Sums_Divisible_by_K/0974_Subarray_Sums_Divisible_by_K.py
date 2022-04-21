class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = Counter()        
        prefix[0] = 1

        counts = 0
        s = 0

        for n in nums:
            s += n
            prefix[s % k] += 1
                
        for _, c in prefix.items():
            counts += c * (c - 1) // 2
        
        return counts 