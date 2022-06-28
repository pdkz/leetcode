class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = set()
        while True:
            a, s = 0, str(n)
            if n in hashmap:
                return False

            hashmap.add(n)
            for c in s:
                a += pow(int(c), 2)
            if a == 1:
                return True

            n = str(a)