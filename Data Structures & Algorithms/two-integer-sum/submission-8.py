class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0,len(nums)):
            x = target-nums[i]
            if (x) in d:
                return [d[x],i]
            d[nums[i]] = i