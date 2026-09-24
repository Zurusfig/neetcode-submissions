class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 1:
            return nums[int(len(nums) / 2)] / 1
        else:
            return (nums[int(len(nums) / 2) - 1] + nums[int(len(nums) / 2)]) / 2