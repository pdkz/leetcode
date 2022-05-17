import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if len(nums1) == 0 or len(nums2) == 0 or k == 0:
            return res

        i = 0
        j = 0
        pq = []
        added = set()

        heapq.heapify(pq)
        heapq.heappush(pq, (nums1[i]+nums2[j], [i,j]))

        l = len(res)
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        while l < k and pq:
            _, pair = heapq.heappop(pq)

            i, j = pair

            res.append([nums1[i], nums2[j]])
            l += 1

            if i+1 < nums1_len and (i+1,j) not in added:
                heapq.heappush(pq, (nums1[i+1]+nums2[j], [i+1,j]))
                added.add((i+1,j))
            if j+1 < nums2_len and (i,j+1) not in added:
                heapq.heappush(pq, (nums1[i]+nums2[j+1], [i,j+1]))
                added.add((i,j+1))
        return res