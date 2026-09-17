class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_no_zero = 1
        zero_count = 0
        zero_idx = 0
        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_idx = i
            else:
                total_no_zero *= num

        res = [0] * len(nums)

        if zero_count == 0:
            for i, num in enumerate(nums):
                res[i] = total_no_zero // num
        elif zero_count == 1:
            res[zero_idx] = total_no_zero
        return res