class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t in {'+', '-', '*', '/'}:
                b = nums.pop()
                a = nums.pop()
                if t == "+":
                    c = a + b 
                if t == "-":
                    c = a - b
                if t == "*":
                    c = a * b
                if t == "/":
                    c = a / b
                    c = int(c)
                nums.append(c)
            else:
                nums.append(int(t))
        return nums[-1]