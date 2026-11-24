class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal's algorithm, keep connecting the min point, as long as it doesnt
        # cause a cycle.
        class UnionFind:
            def __init__(self, n):
                self.par = [i for i in range(n)]
                self.weight = [1] * (n)
            def find(self,n):
                while n != self.par[n]:
                    self.par[n] = self.par[self.par[n]]
                    n = self.par[n]
                return n
            def union(self,n1,n2):
                p1,p2=self.find(n1), self.find(n2)
                if p1 == p2: return False
                weight1,weight2 = self.weight[p1], self.weight[p2]
                if weight1 > weight2:
                    self.weight[p1] += self.weight[p2]
                    self.par[p2] = self.par[p1]
                else:
                    self.weight[p2] += self.weight[p1]
                    self.par[p1] = self.par[p2]
                return True
        edges = []
        dsu = UnionFind(len(points))
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append(( dist,i,j))
        edges.sort()
        res = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res

        