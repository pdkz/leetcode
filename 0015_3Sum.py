class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        i = 0
        j = i + 1
        N = len(nums)
        ans = set()
        while i < N:
            j = i+1
            k = N-1
            while  j<k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    if not (nums[i], nums[j], nums[k]) in ans:
                        ans.add((nums[i], nums[j], nums[k]))
                    j += 1
            i += 1

        return [list(_) for _ in ans]

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        i = 0
        N = len(nums)
        ht = dict()
        ans = set()
        while i < N:
            target = 0 - nums[i]
            j = i + 1
            ht.clear()
            while j < N:
                if target - nums[j] in ht and not (nums[i], target - nums[j], nums[j]) in ans:
                    ans.add((nums[i], target - nums[j], nums[j]))
                if not nums[j] in ht:
                    ht[nums[j]] = j

                j += 1
            i += 1

        return [list(_) for _ in ans]
