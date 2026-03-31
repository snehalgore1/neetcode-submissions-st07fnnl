class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        pref.append(1)
        for i in range (1,len(nums)):
            pref.append(pref[i-1]*nums[i-1])
        print(pref)
        suff = [1]*len(nums)
        # print(suff)
        for i in range (len(nums)-2,-1,-1):
            suff[i] = suff[i+1]*nums[i+1]
        print(suff)
        ans = [1]*len(nums)
        for i in range(0,len(nums)):
            ans[i] = pref[i]*suff[i]
        print(ans)
        return (ans)