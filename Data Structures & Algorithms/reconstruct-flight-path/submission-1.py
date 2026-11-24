class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(source, res, source_dest):
            res.append(source) # add it to the path
            if len(res) == len(tickets) + 1: # explored all tickets
                return True
            for i,d in enumerate(source_dest[source]):
                # explore the destination as a possible path of the path
                # remove the ticket first
                source_dest[source].pop(i)

                if dfs(d, res, source_dest):  # terminate when found a solution
                    return True
                # add back the ticket
                source_dest[source].insert(i, d)
            res.pop() # backtrack if no valid path found
            return False
        res = []
        tickets.sort() # make sure the first we get is the lexicographic solution
        source_dest = defaultdict(list)
        for s,d in tickets:
            source_dest[s].append(d)
        dfs("JFK", res,source_dest)
        return res
