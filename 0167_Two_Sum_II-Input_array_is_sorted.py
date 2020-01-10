class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = collections.Counter(numbers)
        for i, el in enumerate(numbers):
            diff = target - el
            if d[diff] >= 1:
                nums = numbers[i+1:]
                j = nums.index(diff)
                return [i+1, i+1+j+1]
        return None
            
