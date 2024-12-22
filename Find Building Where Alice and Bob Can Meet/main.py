import heapq
from collections import defaultdict

class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        n = defaultdict(list)
        query = len(queries)
        result = [-1] * query
        
        for index, j in enumerate(queries):
            left, right = sorted(j)
            if left == right or heights[right] > heights[left]:
                result[index] = right
            else:
                h = max(heights[left], heights[right])
                n[right].append((h, index))
        
        min_heap = []
        for index, h in enumerate(heights):
            for query_h, query_index in n[index]:
                heapq.heappush(min_heap, (query_h, query_index))
            
            while min_heap and h > min_heap[0][0]:
                query_h, query_index = heapq.heappop(min_heap)
                result[query_index] = index
        
        return result