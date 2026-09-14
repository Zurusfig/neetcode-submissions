class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        for key, value in counter.items():
            freq[value].append(key)
        res = []
        for f in reversed(freq):
            for x in f:
                res.append(x)
                if len(res) == k:
                    return res
        return res
            