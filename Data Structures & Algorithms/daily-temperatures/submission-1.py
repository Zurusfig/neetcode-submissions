class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        max_t = 0
        stack = []
        for i in range(len(temperatures)-1,-1,-1):
            t = temperatures[i]
            if max_t <= t:
                stack.append(t)
                max_t = t
            else:
                count = 1
                j = len(stack) - 1
                found = False
                while j >= 0 and not found:
                    s = stack[j]
                    if s <= t:
                        count += 1
                        j -= 1
                    else:
                        res[i] = count
                        found = True
                stack.append(t)
        return res
                