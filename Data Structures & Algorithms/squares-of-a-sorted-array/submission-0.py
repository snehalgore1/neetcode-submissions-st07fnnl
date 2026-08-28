class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        ret = []
        while l<=r:
            lsq = nums[l]**2
            rsq = nums[r]**2
            if (lsq)>(rsq):
                # ret.append(rsq)
                ret.append(lsq)
                l+=1
            else:
                ret.append(rsq)
                # ret.append(lsq)
                r-=1
            # l+=1
            # r-=1
        return ret[::-1]