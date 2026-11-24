class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:  # too many edges -> cycle
            return False
        par = [i for i in range(n)]
        weight = [1 for i in range(n)]

        def find(n): # finds the root node
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n

        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2: return True # cycle found
            w1,w2 = weight[p1],weight[p2]
            if w1 < w2:
                par[p1] = p2
                weight[p2] += weight[p1]
            else:
                par[p2] = p1
                weight[p1] += weight[p2]
            return False
            
        for n1,n2 in edges:
            if union(n1,n2):
                return False
        return True
        