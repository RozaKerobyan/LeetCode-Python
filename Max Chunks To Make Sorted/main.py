class Solution(object):
    def maxChunksToSorted(self, arr):
        if not arr:
            return 0
        count, max_val = 0, 0
        for i in range(len(arr)):
            max_val = max(max_val, arr[i])
            if max_val == i:
                count += 1
        return count