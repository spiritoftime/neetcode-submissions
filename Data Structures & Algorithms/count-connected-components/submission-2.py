class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            da = par[n1]
            while da != par[da]:
                par[da] = par[par[da]]
                da = par[da]
            return da
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
        for e1,e2 in edges:
            union(e1,e2)
        return len(set(find(i) for i in range(n)))
        