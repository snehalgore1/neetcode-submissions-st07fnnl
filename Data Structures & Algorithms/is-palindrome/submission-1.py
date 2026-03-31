class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 =""
        for i in range(0,len(s)):
            if s[i].isalnum():
                s1=s[i]+s1
        s1 = s1.lower()
        lo=0
        hi=len(s1)-1
        while(lo<hi):
            if s1[lo]!=s1[hi]:
                return False
            lo = lo+1
            hi = hi-1
        return True
            