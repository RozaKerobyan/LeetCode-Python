import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        n = len(classes)
        heap = []
        
        for passed, total in classes:
            gain = (passed + 1) / float(total + 1) - passed / float(total)
            heapq.heappush(heap, (-gain, passed, total))
        
        for _ in range(extraStudents):
            gain, passed, total = heapq.heappop(heap)
            passed += 1
            total += 1
            new_gain = (passed + 1) / float(total + 1) - passed / float(total)
            heapq.heappush(heap, (-new_gain, passed, total))

        total_ratio = 0.0
        for _, passed, total in heap:
            total_ratio += passed / float(total)
        
        return total_ratio / n