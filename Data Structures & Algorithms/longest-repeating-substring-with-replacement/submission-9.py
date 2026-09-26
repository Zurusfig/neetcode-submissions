class Solution:
    def checkvalid(self, mp, curr_len, k) -> bool:
        max_freq = max(mp.values())
        return curr_len - max_freq <= k
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        r = 0
        res = 0
        while r < len(s):
            c = s[r]
            # add char to map
            if c not in mp:
                mp[c] = 0
            mp[c] += 1
            # check valid
            curr_len = r - l+1
            while not self.checkvalid(mp, curr_len, k):
                mp[s[l]] -= 1
                l += 1
                curr_len -= 1
            res = max(res, r-l+1)
            r += 1
        return res