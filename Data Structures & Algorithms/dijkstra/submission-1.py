class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        # Create adjacency list
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # Distance from src to every node
        dist = {i: float("inf") for i in range(n)}
        dist[src] = 0

        # Min heap: (distance, node)
        heap = [(0, src)]

        while heap:
            current_dist, u = heapq.heappop(heap)

            # Skip old/outdated value
            if current_dist > dist[u]:
                continue

            # Explore neighbors
            for v, weight in graph[u]:

                new_dist = current_dist + weight

                # Found a shorter path
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        # Convert unreachable nodes to -1
        for node in dist:
            if dist[node] == float("inf"):
                dist[node] = -1

        return dist