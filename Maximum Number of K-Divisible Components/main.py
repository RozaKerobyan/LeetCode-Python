from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        node_map = defaultdict(list)

        for node1, node2 in edges:
            node_map[node1].append(node2)
            node_map[node2].append(node1)

        res = [0]

        def DFS(cur, parent):
            total = values[cur]
            for child in node_map[cur]:
                if child != parent:
                    total += DFS(child, cur)
            if total % k == 0:
                res[0] += 1
            return total

        DFS(0, -1)
        return res[0]