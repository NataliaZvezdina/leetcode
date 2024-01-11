# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        self.res = 0
        def dfs(node, mn, mx):
            if not node: return

            self.res = max(self.res, abs(node.val-mn), abs(node.val-mx))
            mn = min(mn, node.val)
            mx = max(mx, node.val)

            dfs(node.left, mn, mx)
            dfs(node.right, mn, mx)


        dfs(root, root.val, root.val)
        return self.res