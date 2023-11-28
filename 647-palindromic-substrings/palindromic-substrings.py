class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.count(i, i+1, s)
            res += self.count(i, i, s)
        return res

    def count(self, l, r, s):
        res = 0
        for i in range(len(s)):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res