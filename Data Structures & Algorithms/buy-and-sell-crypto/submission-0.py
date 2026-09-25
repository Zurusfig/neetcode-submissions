class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        s = 0
        e = s + 1
        while s < len(prices)-1 and e < len(prices):
            ps = prices[s]
            pe = prices[e]
            best = max(pe-ps,best)
            if pe > ps:
                e += 1
            else:
                s = e
                e = s + 1
        return best


        