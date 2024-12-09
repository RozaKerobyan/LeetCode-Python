class Solution(object):
    def maxTwoEvents(self, events):
        n = len(events)
        events.sort(key = lambda x : x[0])
        max_value_after = [0] * n
        max_value_after[n - 1] = events[n - 1][2]
        for i in range(n-2, -1, -1):
            max_value_after[i] = max(events[i][2], max_value_after[i + 1])
        max_sum = 0
        for i in range(n):
            left = i + 1
            right = n - 1
            next_event = -1
            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] > events[i][1]:
                    next_event = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if next_event != -1:
                max_sum = max(max_sum, events[i][2] + max_value_after[next_event])
            max_sum = max(max_sum, events[i][2])
        return max_sum