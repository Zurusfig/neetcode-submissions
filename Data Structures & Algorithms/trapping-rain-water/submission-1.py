class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        output = 0
        left_max = height[l]
        right_max = height[r]
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max,height[l])
                output += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max,height[r])
                output += right_max - height[r]
        return output