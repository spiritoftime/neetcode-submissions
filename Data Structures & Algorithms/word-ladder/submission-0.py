class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        res = float('inf')
        def compareWord(s1,s2):
            """Compare two words, and check if they only have 1 char diff.
            Returns true if it is a possible word to transform into"""
            diffChar=0
            for i in range(len(s1)):
                diffChar+= s1[i] != s2[i]
                if diffChar > 1:return False
            return True

        def dfs(beginWord, endWord, wordList, numTransformations):
            nonlocal res
            if beginWord == endWord:
                res = min(res,numTransformations)
                return
            if numTransformations > res: # prune it
                return
            visited.add(beginWord)
            for w in wordList:
                if w not in visited and compareWord(beginWord, w): #possible transformation candidate
                    dfs(w,endWord,wordList,numTransformations +1)
            visited.remove(beginWord)
        if endWord not in wordList:
            return 0
        dfs(beginWord,endWord,wordList, 1)
        return res if res != float('inf') else 0