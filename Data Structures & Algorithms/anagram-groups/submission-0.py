class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sorted_str_map = {}
        i = 0
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in sorted_str_map:
                result[sorted_str_map[sorted_s]].append(s)
            else:
                sorted_str_map[sorted_s] = i
                result.append([s])
                i += 1
        return result
