# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recur(self, p , q):
        if p and q:
            if p.val == q.val:
                return self.recur(p.left, q.left) and self.recur(p.right, q.right)
            else:
                return False
        return p == q
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.recur(p,q)