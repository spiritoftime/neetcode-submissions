class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        par,w = [i for i in range(n)],[1 for i in range(n)]

        def find(n):
            while par[n] != n:
                par[n] = par[par[n]]
                n = par[n]
            return n
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2: # same parent, didnt need to union
                return False
            w1,w2 = w[p1],w[p2]
            if w1<w2:
                par[p1] = p2
                w[p2] += w[p1]
            else:
                par[p2] = p1
                w[p1] += w[p2]

            return True
        for n1,n2 in edges:
            if union(n1,n2):
                res-=1
        return res

