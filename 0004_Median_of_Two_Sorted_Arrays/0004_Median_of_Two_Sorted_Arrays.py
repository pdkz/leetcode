class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        mid = (l1+l2) // 2
        i, j = 0, 0
        out = []
        for n in range(0, mid+1):
            if i < l1 and (j > l2-1 or nums1[i] < nums2[j]):
                out.append(nums1[i])
                i += 1
            else:
                out.append(nums2[j])
                j += 1
        return float(out[mid]) if (l1+l2) % 2 else float((out[mid] + out[mid-1]) / 2)
