class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        topo_sort = []

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            sz = len(q)
            for _ in range(sz):
                v = q.popleft()
                topo_sort.append(v)
                for neib in graph[v]:
                    indegree[neib] -= 1
                    if indegree[neib] == 0:
                        q.append(neib)

        return topo_sort if len(topo_sort) == numCourses else []
