class Solution:
    def checkvalid(self, mp, curr_len, k) -> bool:
        for letter, freq in mp.items():
            if curr_len - freq <= k:
                return True
        return False
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