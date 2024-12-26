from collections import deque

class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        def diameter(edges):
            n = len(edges) + 1
            degree = [0] * n
            adjacency_list = [[] for _ in range(n)]
            for v, w in edges:
                adjacency_list[v].append(w)
                adjacency_list[w].append(v)
                degree[v] += 1
                degree[w] += 1
            queue = deque()
            for i, d in enumerate(degree):
                if d == 1:
                    queue.append(i)
            level, left = 0, n
            while left > 2:
                queue_size = len(queue)
                left -= queue_size
                for _ in range(queue_size):
                    v = queue.popleft()
                    for w in adjacency_list[v]:
                        degree[w] -= 1
                        if degree[w] == 1:
                            queue.append(w)
                level += 1
            return 2 * level + 1 if left == 2 else 2 * level

        d1 = diameter(edges1)
        d2 = diameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)