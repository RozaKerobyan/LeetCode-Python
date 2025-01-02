class Solution(object):
    def maxScore(self, s):
        result = 0
        ones = s.count("1")
        zeros = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            
            result = max(result, zeros + ones)

        return result