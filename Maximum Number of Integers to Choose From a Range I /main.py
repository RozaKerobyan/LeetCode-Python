class Solution(object):
    def maxCount(self, banned, n, maxSum):
        count = 0
        sum_num = 0
        for i in range(1, n + 1):
            if i in banned:
                continue
            sum_num += i
            if sum_num > maxSum:
                break
            count += 1
        return count
        