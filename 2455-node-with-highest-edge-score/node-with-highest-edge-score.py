class Solution:
    def edgeScore(self, edges: List[int]) -> int:            

        ins = [0] * len(edges)
        for u in range(len(edges)):
            ins[edges[u]] += u

        idx = 0
        max_score = ins[0]
        for u in range(len(ins)):
            if ins[u] > max_score:
                max_score = ins[u]
                idx = u

        return idx
