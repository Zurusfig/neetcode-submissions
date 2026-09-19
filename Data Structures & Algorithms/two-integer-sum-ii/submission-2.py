class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            res = []
            l = 0
            r  = len(numbers)-1
            while l < r:
                nl = numbers[l]
                nr = numbers[r]
                if nl + nr == target:
                    res.append(l+1)
                    res.append(r+1)
                    return res
                if nl + nr > target:
                    r -= 1
                else:
                    l += 1
            
                
