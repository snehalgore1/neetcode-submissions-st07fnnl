class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        k = ""
        for i in range(0,len(s)):
            if ((ord(s[i]) >= ord('a')) and (ord(s[i])<= ord('z')) or (ord(s[i]))>= ord('0') and (ord(s[i]) <= ord('9'))):
                k = k+s[i]
        left = 0
        right = len(k)-1
        while left<right:
            print(k[left],k[right])
            if k[left] == k[right]:
                left+=1
                right-=1
            else:
                return False
        return True