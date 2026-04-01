class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list_words = [0]*26
        for i in range(len(s)):
            list_words[ord(s[i]) - ord('a')] += 1
            list_words[ord(t[i]) - ord('a')] -= 1
        
        for i in list_words:
            if i!=0:
                return False
        return True