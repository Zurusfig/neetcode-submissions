# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        mp = {}
        low = None
        q = deque()

        if root:
            q.append(root)
            val = root.val
            low = val
            mp[val] = (None,None) #(prev,next)
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                val = node.val
                low = min(low, val)
                if node.left:
                    q.append(node.left)
                    left = node.left.val
                    mp[left] = (mp[val][0],val)
                    if mp[val][0]:
                        mp[mp[val][0]] = (mp[mp[val][0]][0], left)
                    mp[val] = (left, mp[val][1])
                if node.right:
                    q.append(node.right)
                    right = node.right.val
                    mp[right] = (val, mp[val][1])
                    if mp[val][1]:
                        mp[mp[val][1]] = (right, mp[mp[val][1]][1])
                    mp[val] = (mp[val][0],right)
        
        res = low
        i = 1
        while i < k:
            res = mp[res][1]
            i += 1
        return res
        