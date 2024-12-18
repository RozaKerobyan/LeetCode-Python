class Solution(object):
    def finalPrices(self, prices):
        result = prices[:]
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]: 
                index = stack.pop()
                result[index] -= prices[i]
            stack.append(i)
        return result