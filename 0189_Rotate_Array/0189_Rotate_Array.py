class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        n = len(nums)
        if k == 0 or k == n: return
        
        for i in range(k):
            tail = nums.pop()
            nums.insert(0, tail)
        """ 
        
        tmps = []
        sz = len(nums)
        if k > sz:
            k = k % sz
        #print("k:%s, %s %s %s" % (k, sz-1, sz-1-k, -1))
        for i in range(sz-1, sz-1-k, -1):
            tmps.append(nums[i])
        for i in range(sz - k -1, -1, -1):
            #print("%s <- %s" % (i+k, i))
            nums[i+k] = nums[i]
        i = 0
        while len(tmps) > 0:
            x = tmps.pop()
            nums[i] = x
            i+=1
