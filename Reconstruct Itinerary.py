# https://leetcode.com/problems/reconstruct-itinerary/description/?envType=daily-question&envId=2023-09-14
from queue import LifoQueue

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        ans = []
        
        for src, dst in tickets:
            adj[src].append(dst)
        
        for key in adj:
            adj[key].sort()
        
        def dfs():

            while adj[node]:
                next_node = adj[node].pop(0)
                dfs(next_node)
            ans.append(node)
        
        dfs("JFK")
        
        return ans[::-1]  node
