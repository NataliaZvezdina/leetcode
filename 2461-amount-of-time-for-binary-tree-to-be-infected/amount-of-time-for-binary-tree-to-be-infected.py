# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        def dfs(node):
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        visited = set()
        q = deque([start])
        minutes = -1

        while q:
            minutes += 1
            for _ in range(len(q)):
                curr = q.popleft()
                visited.add(curr)
                for neib in graph[curr]:
                    if neib not in visited:
                        q.append(neib)

        return minutes