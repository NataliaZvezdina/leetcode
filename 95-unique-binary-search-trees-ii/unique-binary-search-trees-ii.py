# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        @cache
        def find(start, end):
            return [None] if start > end else [
                TreeNode(i, left, right)
                for i in range(start, end+1)
                for left in find(start, i-1)
                for right in find(i+1, end)
            ]
            
        return find(1, n)
        