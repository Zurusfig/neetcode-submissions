class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s1.sort()

        l = 0
        r = len(s1)

        while r <= len(s2):
            ss = list(s2[l:r])
            ss.sort()
            if s1 == ss:
                return True
            l += 1
            r += 1
        return False
