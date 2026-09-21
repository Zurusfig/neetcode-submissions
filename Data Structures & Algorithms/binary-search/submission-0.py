class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if nums[l] == target:
                return l
        if nums[r] == target:
            return r
        while l < r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
                if nums[r] == target:
                    return r
            else:
                l = m + 1
                if nums[l] == target:
                    return l
        return -1
