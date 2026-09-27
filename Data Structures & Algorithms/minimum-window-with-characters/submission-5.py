class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s):
            return res
        if s == t:
            return s
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

        s_counter = [0] * (ord('z') - ord('A')+ 1 )
        for sc in s[l:r+1]:
            idx = ord('z') - ord(sc)
            s_counter[idx] += 1

        req = set()
        while r < len(s): 
            if len(req) == 0:
                for tc in t:
                    idx = ord('z') - ord(tc)
                    if t_counter[idx] <= s_counter[idx]:
                        # passed req
                        req.add(idx)
            while len(req) == set_t_len:
                if res == "" or len(s[l:r+1]) < len(res):
                    res = s[l:r+1]
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
        return res  
                