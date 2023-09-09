class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS, stackT = self.checkBackspace(s), self.checkBackspace(t)
        return stackS == stackT

    
    def checkBackspace(self, s):
        stack = []
        for c in s:
            if c != '#':
                stack.append(c)
            else:
                stack.pop() if stack else stack
        return stack