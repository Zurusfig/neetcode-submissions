class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        most = 0
        r = len(heights) - 1
        while l < r:
            diff = r - l
            hl = heights[l]
            hr = heights[r]
            most = max(most, min(hl,hr) * diff)
            if hl < hr:
                l += 1
            else:
                r -= 1
        return most
            