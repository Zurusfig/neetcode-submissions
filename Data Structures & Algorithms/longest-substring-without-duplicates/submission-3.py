class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        e = 0
        best = 0
        curr = ""
        curr_start = 0
        while e < len(s):
            c = s[e]
            if c not in curr:
                curr += c
                best = max(best,len(curr))
            else:
                l = curr.find(c) + 1
                curr = curr[l:] + c
            e += 1
        return best


        