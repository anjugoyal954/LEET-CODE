class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        res = []
        n = len(s)
        for i in range(1, n) :
            if n % i == 0:
                res.append(i)

        for x in res:
            y = n // x
            if s[:x] * y == s:
                return True
        return False

        