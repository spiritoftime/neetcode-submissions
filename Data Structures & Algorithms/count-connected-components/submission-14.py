class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        weight = [1] * n
        def find(node):
            current = node
            # Path compression: traverse up to root while compressing path
            while current != par[current]:
                par[current] = par[par[current]]  # Point to grandparent
                current = par[current]
            return current
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:return False
            if weight[p1] > weight[p2]:
                par[p2] = p1
                weight[p1] += weight[p2]
            else:
                par[p1] = p2
                weight[p2] += weight[p1]
            return True 
        res = n # there may be n unconnected components at the start
        for e1,e2 in edges:
            if union(e1,e2):
                res -=1
        return res
