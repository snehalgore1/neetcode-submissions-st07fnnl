class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in remainder:
                return [remainder[diff],i]
            else:
                remainder[nums[i]] = i