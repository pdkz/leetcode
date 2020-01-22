class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d_nums1 = collections.Counter(nums1)
        d_nums2 = collections.Counter(nums2)
        
        result = []
        for k, v_1 in d_nums1.items():
            if k in d_nums2:
                v_2 = d_nums2.get(k)
                v = min(v_1, v_2)
                for i in range(v):
                    result.append(k)
        return result
