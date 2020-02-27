class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k == 0 or k == n: return
        
        for i in range(k):
            tail = nums.pop()
            nums.insert(0, tail)
