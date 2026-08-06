class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphabet = [0]*26
        for i in range(0,len(s)):
            alphabet[ord(s[i])-ord('a')] += 1
            alphabet[ord(t[i])-ord('a')] -= 1
        for i in alphabet:
            if i!=0:
                return False
        return True
        
            