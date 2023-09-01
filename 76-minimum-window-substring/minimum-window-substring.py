class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        cT, cS = {}, {}
        for c in t:
            cT[c] = 1 + cT.get(c, 0)
        have, need = 0, len(cT)
        res, resLen = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            cS[c] = 1 + cS.get(c, 0)

            if c in cT and cT[c] == cS[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                cS[s[l]] -= 1
                if s[l] in cT and cT[s[l]] > cS[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1]
