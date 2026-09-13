class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            x = t.find(s[i])
            if x == -1:
                return False
            else:
                t = t[:x] + t[x+1:]
        return True
            