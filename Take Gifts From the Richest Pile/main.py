import math

class Solution(object):
    def pickGifts(self, gifts, k):
        gifts.sort(reverse=True)
        result = sum(gifts)
        
        for _ in range(k):
            top = gifts.pop(0)
            reduced_value = int(math.sqrt(top))
            result -= (top - reduced_value)
            gifts.append(reduced_value)
            gifts.sort(reverse=True)
        return result


sol = Solution()
print(sol.pickGifts([25,64,9,4,100], 4))