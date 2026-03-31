class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(list(s))
        s2 = sorted(list(t))
        if s1 ==s2:
            return True
        return False
        