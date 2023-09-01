class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1, c2 = {}, {}
        for c in s:
            c1[c] = 1 + c1.get(c, 0)

        for c in t:
            c2[c] = 1 + c2.get(c, 0)

        return c1 == c2