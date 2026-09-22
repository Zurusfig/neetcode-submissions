class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r-l)//2)
            nl = nums[l]
            nr = nums[r]
            nm = nums[m]
            res = min(res, nm)
            if nm > nl and nm > nr:
                l = m + 1
            elif nm > nl and nm < nr:
                r = m - 1
            elif nm < nr and nm < nl:
                r = m - 1
            else:
                l = m + 1
        return res     
