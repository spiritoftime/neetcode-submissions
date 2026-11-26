class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [1] * (len(edges)+1)
        parent = [i for i in range(len(edges)+1)]
        res = []
        def find(n1):
            if parent[n1] != n1:
                parent[n1] = find(parent[n1])
            return parent[n1]

        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        for e1,e2 in edges:
            cyclic = union(e1,e2)
            if not cyclic:
                res = [e1,e2]
        return res