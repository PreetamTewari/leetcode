class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)
        res = ["JFK"]
        
        def dfs(cur):
            if len(res) == len(tickets)+1:
                return True
            if cur not in adj:
                return False
            
            tmp = list(adj[cur])
            for i,v in enumerate(tmp):
                adj[cur].remove(v)
                res.append(v)
                if dfs(v):
                    return res
                res.pop()
                adj[cur].insert(i, v)
            return False
        dfs("JFK")
        return res
