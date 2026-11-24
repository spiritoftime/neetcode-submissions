class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p,w = [i for i in range(len(edges)+1)], [1 for i in range(len(edges)+1)]
        res=None
        def find(n):
            while n != p[n]:
                p[n] = p[p[n]]
                n=p[n]
            return n
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1 == p2:
                return True
            w1,w2=w[p1],w[p2]
            if w1<w2:
                p[p1]=p2
                w[p2] += w[p1]
            else:
                p[p2]=p1
                w[p1] += w[p2]
            return False
        for e1,e2 in edges:
            if union(e1,e2):res=[e1,e2]
        return res
            