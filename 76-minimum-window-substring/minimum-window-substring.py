class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        cS, cT = {}, {}

        for c in t:
            cT[c] = 1 + cT.get(c, 0)
        
        have, need = 0, len(cT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            cS[s[r]] = 1 + cS.get(s[r],0)

            if s[r] in cT and cS[s[r]] == cT[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                cS[s[l]] -= 1
                if s[l] in cT and cS[s[l]] < cT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
        