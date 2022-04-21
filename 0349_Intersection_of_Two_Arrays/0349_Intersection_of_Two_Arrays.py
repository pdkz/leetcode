class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = []
        s1 = set(nums1)
        s2 = set(nums2)
        """
        if len(s1) < len(s2):
            x = s1
            y = s2
        else:
            x = s2
            y = s1
        """
        for el in s1:
            if el in s2:
                if el not in results: results.append(el)
        return results
