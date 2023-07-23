# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0: [], 1: [TreeNode(0)]}

        def helper(n):
            if n not in dp:
                dp[n] = [TreeNode(0, left, right)
                         for i in range(1, n, 2)
                         for left in helper(i)
                         for right in helper(n-i-1)]
            return dp[n]
        
        return helper(n)
