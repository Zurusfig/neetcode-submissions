# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recur(self, root, target, ancestors):
        ancestors.append(root)
        if root == target:
            return ancestors
        if root.left:
            find_left = self.recur(root.left, target, ancestors.copy())
            if find_left:
                return find_left
        if root.right:
            find_right = self.recur(root.right, target, ancestors.copy())
            if find_right:
                return find_right
        return None
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_ancs = self.recur(root, p, [])
        q_ancs = self.recur(root, q, [])
        res = None
        i = 0
        while i < len(p_ancs) and i < len(q_ancs) and p_ancs[i] == q_ancs[i]:
            res = p_ancs[i]
            i += 1
        return res
        

        
        