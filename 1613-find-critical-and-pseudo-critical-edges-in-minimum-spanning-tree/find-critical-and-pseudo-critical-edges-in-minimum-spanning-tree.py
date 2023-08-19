class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v):
        while v != self.parent[v]:
            self.parent[self.parent[v]]
            v = self.parent[v]
        return v

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

            for i,e in enumerate(edges):
                e.append(i)

            edges.sort(key=lambda edge: edge[2])

            mst_weight = 0
            uf = UnionFind(n)
            for v1,v2,w,i in edges:
                if uf.union(v1,v2):
                    mst_weight += w

            critical, pseudo = [], []

            for n1,n2,e_weight,i in edges:
                weight = 0
                uf = UnionFind(n)
                for v1,v2,w,j in edges:
                    if i != j and uf.union(v1,v2):
                        weight += w 
                if max(uf.rank) != n or weight > mst_weight:
                    critical.append(i)
                    continue

                weight = e_weight
                uf = UnionFind(n)
                uf.union(n1,n2)
                for v1,v2,w,j in edges:
                    if uf.union(v1,v2):
                        weight += w 
                if weight == mst_weight:
                    pseudo.append(i)
                    
            return critical, pseudo