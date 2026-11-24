
class Solution:
    def determineOrder(self, w1: str, w2: str, orderMap):
        # 1. Find the first differing character to establish the order constraint (edge)
        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]:
                # Edge: w1[i] -> w2[i] (w1[i] must come before w2[i])
                orderMap[w1[i]].append(w2[i])
                return True  # Constraint found, successfully processed.

        # 2. Handle Prefix Cases
        # If no difference was found, one word is a prefix of the other.
        # Invalid order: A longer word comes immediately before its shorter prefix (e.g., "abc" followed by "ab").
        if len(w1) > len(w2):
            return False

        return True  # Valid prefix case (e.g., "ab" followed by "abc" or "a" followed by "a").

    def dfs(self, c, orderMap, res, visited, seen):
        if c in seen:
            return False  # cycle
        if c in visited:
            return True  # seen this char before
        seen.add(c)
        for s in orderMap[c]:
            if not self.dfs(s, orderMap, res, visited, seen):  # cycle
                return False
        seen.remove(c)
        visited.add(c)
        res.append(c)
        return True

    def foreignDictionary(self, words: List[str]) -> str:
        visited = set()
        seen = set()
        orderMap = defaultdict(list)
        unique_chars = set("".join(words))
        res = []
        for i in range(len(words) - 1):
            if not self.determineOrder(words[i], words[i + 1], orderMap):
                return ""
        for c in unique_chars:
            if not self.dfs(c, orderMap, res, visited, seen):  # cycle
                return ""
        return "".join(res[::-1])
