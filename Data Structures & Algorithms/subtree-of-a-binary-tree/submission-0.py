# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recur(self, p, q):
        if p and q and p.val == q.val:
            return self.recur(p.left,q.left) and self.recur(p.right, q.right)
        return p == q
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        if root:
            q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.val == subRoot.val:
                    f = self.recur(node, subRoot)
                    if f:
                        return f
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False
        