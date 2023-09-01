class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = [] #index, temp
        out = [0] * len(temp)
        for i, t in enumerate(temp):
            while stack and stack[-1][1] < t:
                index, tem = stack.pop()
                out[index] = (i - index)
            stack.append([i, t])
        return out