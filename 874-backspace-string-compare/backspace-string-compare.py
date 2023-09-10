class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS, stackT = self.helper(s), self.helper(t)
        return stackS == stackT


    def helper(self, s):
        stack = []
        for c in s:
            if c == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return stack