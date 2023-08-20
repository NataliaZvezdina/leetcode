class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        item_gr = [[] for _ in range(n)]
        item_indegree = [0] * n

        group_gr = [[] for _ in range(group_id)]
        group_indegree =[0] * group_id

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_gr[prev].append(curr)
                item_indegree[curr] += 1

                if group[curr] != group[prev]:
                    group_gr[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        def topo_sort(graph,indegree):
            visited = []
            q = deque()
            for v in range(len(graph)):
                if indegree[v] == 0:
                    q.append(v)

            while q:
                curr = q.popleft()
                visited.append(curr)
                for neib in graph[curr]:
                    indegree[neib] -= 1
                    if indegree[neib] == 0:
                        q.append(neib)

            return visited if len(visited) == len(graph) else []

        item_order = topo_sort(item_gr,item_indegree)
        group_order = topo_sort(group_gr,group_indegree)

        if not item_order or not group_order:
            return []

        ordered_groups = defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        ans = []
        for group_idx in group_order:
            ans += ordered_groups[group_idx]

        return ans
