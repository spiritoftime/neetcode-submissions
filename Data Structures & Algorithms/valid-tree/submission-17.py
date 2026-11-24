class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:return False
        par = [i for i in range(n)]
        weight = [1] * n
        def find(n):
            parent = par[n]
            grandparent = par[parent]
            while grandparent !=parent:
                grandparent = par[grandparent]
                parent = grandparent
            return parent
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return True # cycle detected
            if p1 != p2:
                if weight[p1] > weight[p2]:
                    par[p2] = p1
                    weight[p1] += weight[p2]
                else:
                    par[p1] = p2
                    weight[p2] += weight[p1]
            return False
        for e1,e2 in edges:
            if union(e1,e2):
                return False
        return True 