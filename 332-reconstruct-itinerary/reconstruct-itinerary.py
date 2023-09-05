class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {src: deque() for src, dst in tickets}
        for s, d in tickets:
            adj[s].append(d)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                res.append(v)
                adj[src].popleft()
                if dfs(v) : return True
                res.pop()
                adj[src].append(v)
            return False
        dfs("JFK")
        return res
