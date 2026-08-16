class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = 0
        e = len(s)-1
        s1 = ""
        for i in range(0, len(s)):
            if s[i].isalnum():
                s1 += s[i].lower()
        start = 0
        end = len(s1)-1
        while start<=end:
            if s1[start] != s1[end]:
                return False
            start += 1
            end -= 1
        return True
