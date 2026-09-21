class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            curr_h = heights[i]
            if i == 0:
                stack.append((i,curr_h))
            else:
                top_start, top_h = stack[-1]
                if curr_h > top_h:
                    stack.append((i,curr_h))
                elif curr_h == top_h:
                    stack.append((top_start,curr_h))
                else:
                    curr_start = i
                    while curr_h < top_h and len(stack) != 0:
                        res = max(res, top_h * (i - top_start))
                        curr_start = top_start
                        stack.pop()
                        if len(stack) != 0:
                            top_start, top_h = stack[-1]
                    stack.append((curr_start,curr_h))
                
        width = len(heights)
        while len(stack) != 0:
            top_start, top_h = stack.pop()
            res = max((width - top_start) * top_h, res)
        return res

