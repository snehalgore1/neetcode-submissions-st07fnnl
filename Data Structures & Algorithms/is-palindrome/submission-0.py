class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        # print(s)
        for i in range(0,len(s)):
            print(i)
            print(s[i].isalnum())
            if s[i].isalnum():
                s1=s[i]+s1
        s1 = s1.lower()
        print(s1)
        s = s1[::-1]
        print(s)
        if s1==s:
            return True
        else:
            return False