class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for ind,val in enumerate(temperatures):
            while stack and val>stack[-1][0]:
                stackVal, stackidx = stack.pop()
                result[stackidx] = ind - stackidx
            stack.append([val,ind])
        return result