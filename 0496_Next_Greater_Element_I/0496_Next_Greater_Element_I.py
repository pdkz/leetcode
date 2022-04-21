class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht = {n:-1 for n in nums1}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                v = stack.pop()
                if ht.get(v, None) != None and n > v:
                    ht[v] = n
            stack.append(n)
        return list(ht.values())
