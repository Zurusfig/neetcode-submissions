# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recur(self, root, curr_height, max_height):
        if root:
            curr_height += 1
            max_height = max(curr_height, max_height)

            max_height = self.recur(root.left, curr_height, max_height)
            max_height = self.recur(root.right, curr_height, max_height)
        return max_height
    def maxDepth(self, root: Optional[TreeNode]) -> int:    
        return self.recur(root,0,0)



        