class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for _ in range(k):
            index = nums.index(min(nums))
            nums[index] *= multiplier
        return nums