# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        if root:
            q.append((root, [float('-inf'), float('inf')]))
        
        while q:
            for i in range(len(q)):
                node, interval = q.popleft()
                val = node.val
                lower = interval[0]
                upper = interval[1]
                if node.left:
                    new = node.left.val
                    if new >= val or new <= lower or new >= upper:
                        return False
                    q.append((node.left, [lower, val]))
                if node.right:
                    new = node.right.val
                    if new <= val or new <= lower or new >= upper:
                        return False
                    q.append((node.right, [val, upper]))
        return True
        