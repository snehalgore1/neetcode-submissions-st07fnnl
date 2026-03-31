class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = 0
        fast = len(numbers) - 1
        if len(numbers)==2:
            return [1,2]
        while slow<fast and fast<len(numbers):
            if numbers[slow]+numbers[fast] == target:
                return [slow+1,fast+1]
            elif numbers[slow]+numbers[fast] < target:
                slow += 1
            elif numbers[slow]+numbers[fast] > target:
                fast -= 1