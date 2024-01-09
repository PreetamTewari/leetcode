class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count1[s[i]] = 1 + count1.get(s[i], 0)
            count2[t[i]] = 1 + count2.get(t[i], 0)
        return count1 == count2