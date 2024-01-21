class Solution:
    def myAtoi(self, s: str) -> int:
        MAX, MIN = pow(2,31) - 1, pow(2, 31)
        s = s.strip()
        if not s:
            return 0
        neg = False
        out = 0

        if s[0] == '-':
            neg = True
        elif s[0] == '+':
            neg = False
        elif not s[0].isnumeric():
            return 0
        else:
            out = out * 10 + (ord(s[0]) - ord('0'))

        for i in range(1, len(s)):
            if s[i].isnumeric():
                out = out * 10 + (ord(s[i]) - ord('0'))
                if neg and out >= MIN:
                    return -MIN
                if not neg and out >= MAX:
                    return MAX
            else:
                break
        if neg:
            return -out
        else:
            return out