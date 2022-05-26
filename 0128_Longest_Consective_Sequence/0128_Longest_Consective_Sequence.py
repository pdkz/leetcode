def longestConsecutive(self, nums: List[int]) -> int:
    hashset = set(nums)
    i, length, max_length = 0, 0, 0
    for i in range(0, len(nums)):
        n = nums[i]
        length = 0
        if n-1 not in hashset:
            while n in hashset:
                n += 1
                length += 1
            max_length = max(length, max_length)
    return max_length