class Solution(object):
    def addSpaces(self, s, spaces):
        result = []
        last_index = 0
        for i in spaces:
            result.append(s[last_index:i])
            result.append(" ")
            last_index = i
        result.append(s[last_index:])
        return "".join(result)