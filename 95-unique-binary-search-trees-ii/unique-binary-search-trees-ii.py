# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def find(start, end, memo):
            res = []
            if start > end:
                res.append(None)
                return res

            if (start, end) in memo:
                return memo[(start, end)]

            for i in range(start, end+1):
                leftTrees = find(start, i-1, memo)
                rightTrees = find(i+1, end, memo)

                for left in leftTrees:
                    for right in rightTrees:
                        root = TreeNode(i, left, right)
                        res.append(root)

            memo[(start, end)] = res
            return res

        memo = {}
        return find(1, n, memo)
        