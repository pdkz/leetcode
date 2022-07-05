class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, N = 0, len(digits)
        digits[N-1] += 1

        for i in range(N-1,-1,-1):
            if carry == 1:
                digits[i] += 1
            if digits[i] > 9:
                carry, digits[i] = 1, 0
            else:
                carry = 0
        if carry:
            digits.insert(0, 1)
        return digits