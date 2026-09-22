class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = 0
        piles.sort()
        total = piles[-1] * len(piles)
        ub = total / h
        if ub > int(ub):
            ub = int(ub) + 1
        else:
            ub = int(ub)

        l = 1
        r = ub
        k = r
        # check for the minimum k we can get from 1 to ub
        while l <= r:
            m = l + ((r-l) // 2)
            tt = 0
            for pile in piles:
                tt += math.ceil(pile/m)
            if tt > h:
                l = m + 1
            else:
                k = min(k,m)
                r = m - 1
        return k
