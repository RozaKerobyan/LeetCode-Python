class Solution(object):
    def continuousSubarrays(self, nums):
        num_counts = {}
        left = 0
        right = 0
        sub_count = 0
        while right < len(nums):
            num_counts[nums[right]] = num_counts.get(nums[right], 0) + 1
            while max(num_counts) - min(num_counts) > 2:
                num_counts[nums[left]] -= 1
                if num_counts[nums[left]] == 0:
                    del num_counts[nums[left]]
                left += 1
            sub_count += right - left + 1
            right += 1
        return sub_count
