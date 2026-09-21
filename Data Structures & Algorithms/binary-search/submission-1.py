class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if nums[l] == target:
                return l
        if nums[r] == target:
            return r
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target: 
                l = m + 1
            else:
                return m
        return -1
