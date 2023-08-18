class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        for u,v in roads:
            if u not in graph:
                graph[u] = set()
            graph[u].add(v)

            if v not in graph:
                graph[v] = set()
            graph[v].add(u)

        max_rank = 0
        for u in graph:
            for v in graph:
                if u == v: continue
                cnt = len(graph[u]) + len(graph[v])
                if v in graph[u]:
                    cnt -= 1

                max_rank = max(max_rank, cnt)

        return max_rank
