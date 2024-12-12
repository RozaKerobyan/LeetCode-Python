class Solution(object):
    def maximumBeauty(self, nums, k):
        nums.sort()
        max_length = 0
        i = 0
        for j in range(len(nums)):
            curr = nums[j] - k
            while nums[i] + k < curr:
                i += 1
            max_length = max(max_length, j - i + 1)
        return max_length