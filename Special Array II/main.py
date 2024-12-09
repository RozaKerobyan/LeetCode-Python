class Solution(object):
    def isArraySpecial(self, nums, queries):
        n = len(nums)
        count_parity = [0] * (n)

        for i in range(1, n):
            count_parity[i] = count_parity[i - 1]
            if nums[i] % 2 == nums[i - 1] % 2:
                count_parity[i] += 1

        results = []
        for j in queries:
            start, end = j[0], j[1]
            if start > 0:
                not_special = count_parity[end] - count_parity[start]
            else:
                not_special = count_parity[end]

            if not_special and start != end:
                results.append(False)
            else:
                results.append(True)
        return results

sol = Solution()
print(sol.isArraySpecial([3,4,1,2,6], [[0,4]]))
        