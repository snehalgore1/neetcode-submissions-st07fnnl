class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        ans = [0]*len(nums)
        product = 1
        for i in range(0,len(nums)-1):
            product = product*nums[i]
            left[i+1] = product
        # print(left)
        # print(right) 
        product = 1       
        for i in range(len(nums)-2,-1,-1):
            # print(i)
            product = product*nums[i+1]
            right[i] = product
        for i in range(len(nums)):
            ans[i] = left[i]*right[i]

        return ans