class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        def backtrack(chars, res, tmp, begin):
            if begin >= len(chars):
                res.append(''.join(tmp))
                return

            for i in range(len(chars[begin])):
                tmp.append(chars[begin][i])
                backtrack(chars, res, tmp, begin+1)
                tmp.pop()
        ht = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        chars = [ht[d].copy() for d in digits]
        res = []

        backtrack(chars, res, [], 0)

        return res