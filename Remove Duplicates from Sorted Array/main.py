class Solution(object):
    def removeDuplicates(self, nums):
        numbers = []
        for num in nums:
            if num not in numbers:
                numbers.append(num)
        k = len(numbers)
        return "{}, nums = {}".format(k, numbers)

sol = Solution()
print(sol.removeDuplicates([1,1,2]))