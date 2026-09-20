class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) != 0:
                    lc = stack.pop()
                    if not (lc == "(" and c == ")" or lc == "[" and c == "]" or lc == "{" and c == "}"):
                        stack.append(lc)
                        stack.append(c)
                else:
                    return False
        return len(stack) == 0
