class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        already_check = set()
        longest_streak = 0
        for num in nums:
            if num not in already_check:
                already_check.add(num)
                curr_streak = 1
                while num + 1 in num_set:
                    num = num+1
                    curr_streak += 1
                    already_check.add(num)
                longest_streak = max(longest_streak,curr_streak)
        return longest_streak

