class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)

        l = 0

        r = len(nums)-1

        pos = r        # where should this start?
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                ret[pos] = nums[l]**2
                l+=1
            else:
                ret[pos] = nums[r]**2
                r-=1
            pos -=1

        return ret