class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges))]
        weight = [1] * len(edges)
        def find(n):
            curr= n
            while curr != par[curr]:
                par[curr] = par[par[curr]]
                curr = par[par[curr]]
            return curr
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return True # cycle
            if weight[p1] > weight[p2]:
                par[p2] = p1
                weight[p1] += weight[p2]
            else:
                par[p2] = p1
                weight[p2] += weight[p1]
            return False
        res = None
        for e1,e2 in edges:
            if union(e1-1,e2-1):
                res = [e1,e2]
        return res