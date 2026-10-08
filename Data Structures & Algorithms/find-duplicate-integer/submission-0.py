class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = set()
        for n in nums:
            if n in mp:
                return n
            mp.add(n)