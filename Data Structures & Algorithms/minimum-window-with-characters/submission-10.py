class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best_l = 0
        best_len = float("inf")
        #t counter -> for checking
        t_counter = [0] * (ord('z') - ord('A') + 1)
        set_t_len = 0
        for tc in t:
            idx = ord('z') - ord(tc)
            if t_counter[idx] == 0:
                set_t_len += 1
            t_counter[idx] += 1
        
        min_window_size = len(t)
        l = 0
        r  = min_window_size - 1

        req = set()
        s_counter = [0] * (ord('z') - ord('A')+ 1 )
        for sc in s[l:r+1]:
            idx = ord('z') - ord(sc)
            s_counter[idx] += 1
            if t_counter[idx] == s_counter[idx]:
                req.add(idx)
        
        curr = s[l:r+1]
        while r < len(s):
            while len(req) == set_t_len:
                curr_len = r - l + 1
                if curr_len < best_len:
                    best_len = curr_len
                    best_l = l
                # move l
                l_idx = ord('z') - ord(s[l])
                s_counter[l_idx] -= 1
                if t_counter[l_idx] > s_counter[l_idx]:
                    req.discard(l_idx)
                l += 1
            r += 1
            if r < len(s):
                r_idx = ord('z') - ord(s[r])
                s_counter[r_idx] += 1 
                if t_counter[r_idx] <= s_counter[r_idx] and t_counter[r_idx] != 0:
                        req.add(r_idx)
        if best_len == float("inf"):
            return ""

        return s[best_l : best_l + best_len] 
                