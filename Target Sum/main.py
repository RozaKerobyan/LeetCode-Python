class Solution(object):
    def findTargetSumWays(self, nums, target):
        total = sum(nums)
        if target > total or (total - target) % 2 != 0:
            return 0
        n = (total - target) // 2

        k = [0] * (n + 1)
        k[0] = 1    
        for i in nums:
            for j in range(n, i - 1, -1):
                k[j] += k[j - i]
        return k[n]