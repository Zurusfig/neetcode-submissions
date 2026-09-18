class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            cl = s[l].lower()
            cr = s[r].lower()
            if not cl.isalnum():
                l += 1
            if not cr.isalnum():
                r -= 1
            if cl.isalnum() and cr.isalnum():
                if cl != cr:
                    return False
                else:
                    l += 1
                    r -= 1
        return True            
