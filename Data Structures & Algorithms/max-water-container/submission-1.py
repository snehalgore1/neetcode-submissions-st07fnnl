class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights) - 1
        max_amt = 0
        while s<e:
            vol = min(heights[s],heights[e])*(e-s)
            max_amt = max(vol,max_amt)
            if heights[s]>heights[e]:
                e-=1
            else:
                s+=1
        return max_amt   