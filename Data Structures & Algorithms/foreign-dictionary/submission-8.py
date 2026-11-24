class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def isLexicoGraphic(a, b):
            """Determines if a is smaller than b. if smaller, returns the 
            index at which they differ """
            for i in range(min(len(a), len(b))):
                c1, c2 = a[i], b[i]
                if c1 != c2:  # first letter in which they differ
                    return True, i
            # no difference in letters, check length
            return len(a) <= len(b), -1

        visited = set()
        completed = set()

        def dfs(c, graph, visited):
            nonlocal res
            # if cycle no solution!
            if c in visited: return True
            if c in completed: return False  # dont add it again
            visited.add(c)
            for smaller in graph[c]:
                if dfs(smaller, graph, visited): return True  # if cycle
            # when all smaller processed, can add it to res
            res += c
            completed.add(c)
            visited.remove(c)
            return False

        graph = defaultdict(list)
        # seed every character so isolated nodes are visited
        for word in words:
            for c in word:
                graph.setdefault(c, [])

        # key is larger, the smaller children are in the value.
        res = ""
        for i in range(len(words) - 1):
            j = i + 1
            w1, w2 = words[i], words[j]
            isLexico, differ_idx = isLexicoGraphic(w1, w2)
            if not isLexico:  # w1 is a longer prefix of w2 — invalid
                return ""
            if differ_idx == -1: # a.length < b.length and no differing letters
                continue
            # the letter at w1 is smaller than the letter at w2
            graph[w1[differ_idx]].append(w2[differ_idx])

        for c in graph:
            if dfs(c, graph, visited): return ""
        return res[::-1]