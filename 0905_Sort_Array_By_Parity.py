class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for el in A:
            if el % 2 == 0:
                even.append(el)
            else:
                odd.append(el)
        return even + odd
