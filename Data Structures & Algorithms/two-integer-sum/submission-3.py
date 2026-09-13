class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)-1):
            result.append(i)
            if target-nums[i] in nums[i+1:]:
                idx = nums[i+1:].index(target-nums[i])
                result.append(idx+i+1)
                return result
            result = []