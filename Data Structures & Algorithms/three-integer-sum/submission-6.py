class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        res = []
        check_nl = set()
        nums.sort()
        while l < len(nums)-1:
            r = l+1
            nl = nums[l]
            if nl not in check_nl:
                check_nr = set()
                tmp = set()
                while r < len(nums):
                    nr = nums[r]
                    if nr not in check_nr:
                        target = -(nl + nr)
                        if target in tmp:
                            out = [nl,nr,target]
                            res.append(out)
                            check_nr.add(nr)
                        else:
                            tmp.add(nr)
                    r += 1
            check_nl.add(nl)
            l += 1
        return res