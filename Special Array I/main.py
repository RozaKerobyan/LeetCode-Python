class Solution(object):
    def isArraySpecial(self, nums):
        if not isinstance(nums[0], list):
            nums = [nums]

        for num in nums:
            for i in range(len(num) - 1):
                if ((num[i] % 2) == (num[i + 1] % 2)):
                    return False
        return True

sol = Solution()
print(sol.isArraySpecial([[1]]))