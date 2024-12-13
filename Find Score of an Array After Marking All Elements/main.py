class Solution(object):
    def findScore(self, nums):
        n = len(nums)
        sort = []
        for index, num in enumerate(nums):
            sort.append((num, index))
        sort.sort()

        result = 0
        for num, index in sort:
            if nums[index] != -1:
                result += num
                nums[index] = -1
                if index > 0:
                    nums[index - 1] = -1
                if index < n -1:
                    nums[index + 1]  = -1
        return result

sol = Solution()
print(sol.findScore([2,1,3,4,5,2]))