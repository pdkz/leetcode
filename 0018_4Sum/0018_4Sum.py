class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        result = []
        ht = collections.defaultdict(list)
        count = collections.Counter(nums)

        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                s = nums[i]
                t = nums[j]
                pair = sorted([s, t])
                if not ht.get(s+t) or pair not in ht[s+t]:
                    ht[s+t].append(pair)

        for k, v in ht.items():
            d = target - k
            if not ht.get(d):
                continue

            for pl in v:
                choiced = collections.defaultdict(int)
                i, j = pl
                choiced[i] += 1
                choiced[j] += 1
                for pr in ht[d]:
                    u, v = pr
                    choiced[u] += 1
                    choiced[v] += 1
                    pair = sorted([i, j, u, v])
                    if pair in result or choiced[u] > count[u] or choiced[v] > count[v]:
                        choiced[u] -= 1
                        choiced[v] -= 1
                        continue

                    result.append(pair)
                    choiced[u] -= 1
                    choiced[v] -= 1
                    
        return result
