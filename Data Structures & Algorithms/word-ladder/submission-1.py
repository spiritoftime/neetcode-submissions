from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def compareWord(s1,s2):
            """Returns True if word is a possible candidate for transformation"""
            numDiff=0
            for i in range(len(s1)):
                numDiff+= s1[i] != s2[i]
                if numDiff>1: return False
            return True
        if endWord not in wordList:return 0
        q = deque()
        res = float('inf')
        q.append(beginWord)
        numTransformations = 0
        visited = set() # dont allow transformations back
        while q:
            numTransformations += 1
            if numTransformations > res: # no need to explore further
                return res if res!= float('inf') else 0
            for i in range(len(q)):
                currWord = q.popleft()
                visited.add(currWord)
                if currWord == endWord:
                    res = min(res, numTransformations)
                    continue
                for w in wordList:
                    # dont go back to the previous words
                    if w not in visited and compareWord(currWord, w):
                        q.append(w)
        return res if res!= float('inf') else 0