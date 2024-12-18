import heapq
from collections import Counter

class Solution:
    def repeatLimitedString(self, s, repeatLimit):
        char_count = Counter(s)
        max_heap = []
        for char, count in char_count.items():
            heapq.heappush(max_heap, (-ord(char), count))
        
        result = []
        while max_heap:
            val, count = heapq.heappop(max_heap)
            char = chr(-val)
            use_count = min(count, repeatLimit)
            result.append(char * use_count)
            count -= use_count
            if count > 0:
                if not max_heap:
                    break
                next_val, next_count = heapq.heappop(max_heap)
                next_char = chr(-next_val)
                result.append(next_char)
                next_count -= 1
                if next_count > 0:
                    heapq.heappush(max_heap, (next_val, next_count))
                heapq.heappush(max_heap, (val, count))
        
        return ''.join(result)